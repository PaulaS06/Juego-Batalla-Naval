import sys
sys.path.append("src")
# Importar NavalBattle desde donde está definido
from Program.NavalBattle import NavalBattle


import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class NavalBattleApp(App):
    def build(self):
        self.title = 'Batalla Naval'
        
        # Mostrar el popup para que el usuario ingrese las dimensiones del tablero y el número de barcos
        self.show_board_size_popup()

        return BoxLayout()  # Retornamos un layout vacío mientras tanto

    def show_board_size_popup(self):
        # Layout para el Popup
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text='Ingrese las dimensiones del tablero (min: 5, max: 9)'))

        # Entrada para las filas
        self.row_input = TextInput(hint_text='Número de filas', input_filter='int', multiline=False)
        box.add_widget(self.row_input)

        # Entrada para las columnas
        self.col_input = TextInput(hint_text='Número de columnas', input_filter='int', multiline=False)
        box.add_widget(self.col_input)

        # Entrada para el número de barcos
        self.ship_input = TextInput(hint_text='Número de barcos', input_filter='int', multiline=False)
        box.add_widget(self.ship_input)

        # Botón para confirmar
        confirm_button = Button(text='Confirmar')
        confirm_button.bind(on_press=self.on_confirm_board_size)
        box.add_widget(confirm_button)

        # Crear y mostrar el Popup
        self.popup = Popup(title='Configuración del Tablero',
                           content=box,
                           size_hint=(0.75, 0.5),
                           auto_dismiss=False)
        self.popup.open()

    def on_confirm_board_size(self, instance):
        # Obtener y validar las dimensiones ingresadas
        try:
            rows = int(self.row_input.text)
            cols = int(self.col_input.text)
        except ValueError:
            self.show_error_popup('Por favor, ingrese números válidos.')
            return

        # Validar que las dimensiones estén entre 5 y 9
        if not (5 <= rows <= 9) or not (5 <= cols <= 9):
            self.show_error_popup('Las dimensiones deben estar entre 5 y 9.')
            return
        
        # Obtener el número máximo de barcos
        max_ships = min(rows, cols) - 1  # El límite máximo de barcos

        # Obtener y validar el número de barcos
        try:
            ships = int(self.ship_input.text)
        except ValueError:
            self.show_error_popup(f'Por favor, ingrese un número de barcos válido (1 a {max_ships}).')
            return

        # Validar que el número de barcos esté dentro del rango permitido
        if not (1 <= ships <= max_ships):
            self.show_error_popup(f'El número de barcos debe estar entre 1 y {max_ships}.')
            return
        
        # Si todo es válido, cerrar el Popup y empezar el juego
        self.popup.dismiss()
        self.start_game(rows, cols, ships)  # Iniciar el juego con el número de barcos

    def show_error_popup(self, message):
        """
        Muestra un popup de error con el mensaje especificado y un botón para cerrar el popup.
        """
        # Crear el layout del popup con un botón de cerrar
        content = BoxLayout(orientation='vertical')
        error_message = Label(text=message)
        close_button = Button(text='Cerrar', size_hint=(1, 0.2))

        content.add_widget(error_message)
        content.add_widget(close_button)

        # Crear el popup
        error_popup = Popup(title='Error',
                            content=content,
                            size_hint=(0.75, 0.5),
                            auto_dismiss=False)  # No se cierra automáticamente, solo con el botón

        # Asignar la función para cerrar el popup cuando se presione el botón
        close_button.bind(on_press=error_popup.dismiss)

        # Mostrar el popup
        error_popup.open()



    def start_game(self, rows, cols, ships):
        # Crear una instancia del juego
        self.game = NavalBattle()  
        
        # Generar el tablero con las dimensiones ingresadas
        self.game.generateBoard(w=cols, h=rows)
        
        # Añadir los barcos de acuerdo al número especificado
        self.game.addShips(ships)

        # Crear el tablero visual en la interfaz
        self.create_game_board(rows, cols)

    def create_game_board(self, rows, cols):
        # Configuraciones del tablero con las dimensiones ingresadas
        self.board_width = cols
        self.board_height = rows
        self.buttons = {}  # Diccionario para almacenar los botones

        # Crear un layout de cuadrícula para el tablero
        layout = GridLayout(cols=self.board_width, rows=self.board_height)
        
        # Crear botones para representar cada casilla del tablero
        for row in range(self.board_height):
            for col in range(self.board_width):
                btn = Button(text='?', font_size=32, background_normal='', background_color=[.5, .5, 1, .5])
                btn.bind(on_press=self.on_button_click)  # Vincular a evento
                self.buttons[(row, col)] = btn
                layout.add_widget(btn)

        # Añadir el layout del tablero al root widget
        self.root.clear_widgets()
        self.root.add_widget(layout)

    def on_button_click(self, instance):
    # Obtener la posición del botón clicado
        for pos, button in self.buttons.items():
            if button == instance:
                row, col = pos
                break

        # Lógica que manejará el clic de un botón
        hit = self.game.shoot(row, col)  # Suponiendo que shoot actualiza el tablero y devuelve True si acierta
        
        if hit:
            self.game.board[row][col] = 0  # Reemplazar con 0 ya que fue un impacto
            
            # Cambiar el color del botón
            instance.background_color = [1, 36/255, 26/255, 5]  # Rojo para un disparo acertado
            instance.text = 'X'
            
            # Verificar si el barco fue hundido
            if self.game.check_ship_sunk(self.game.last_hit):
                self.show_sunk_ship_popup(self.game.last_hit)
            
        else:
            instance.background_color = [127/255, 181/255, 246/255, 5]  # Azul para un disparo fallido
            instance.text = '~'
        
        instance.disabled = True  # Deshabilitar el botón después de un disparo

        # Verificar si todos los barcos han sido hundidos
        if self.game.all_ships_sunk():
            self.show_victory_popup()

    def show_sunk_ship_popup(self, ship_length):
        # Obtener la cantidad de barcos restantes
        remaining_ships = len(set(sum(self.game.board, []))) - 1  # Restar 1 porque el '0' también cuenta

        # Crear el layout del popup con un botón de cerrar
        content = BoxLayout(orientation='vertical')
        message = Label(text=f"¡Has hundido un barco de longitud {ship_length}! Quedan {remaining_ships} barcos restantes.")
        close_button = Button(text='Cerrar', size_hint=(1, 0.2))
        
        content.add_widget(message)
        content.add_widget(close_button)

        # Crear el popup
        sunk_ship_popup = Popup(title='¡Barco hundido!',
                                content=content,
                                size_hint=(0.75, 0.5),
                                auto_dismiss=False)  # No se cierra automáticamente, solo con el botón

        # Asignar la función para cerrar el popup cuando se presione el botón
        close_button.bind(on_press=sunk_ship_popup.dismiss)

        # Mostrar el popup
        sunk_ship_popup.open()

    def show_victory_popup(self):
        # Crear el layout del popup con un botón de cerrar
        content = BoxLayout(orientation='vertical')
        message = Label(text="¡Felicidades! Has hundido todos los barcos. ¡Has ganado!")
        close_button = Button(text='Cerrar', size_hint=(1, 0.2))
        
        content.add_widget(message)
        content.add_widget(close_button)

        # Crear el popup
        victory_popup = Popup(title='¡Victoria!',
                            content=content,
                            size_hint=(0.75, 0.5),
                            auto_dismiss=False)  # No se cierra automáticamente, solo con el botón

        # Asignar la función para cerrar el popup cuando se presione el botón
        close_button.bind(on_press=victory_popup.dismiss)

        # Mostrar el popup
        victory_popup.open()


    
if __name__ == '__main__':
    NavalBattleApp().run()
