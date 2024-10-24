import sys
sys.path.append("src")

from Model.NavalBattleModel import Model_NB
from Controller.NavalBattleController import Controller_NB

# Crear una instancia del Modelo

"""A REVISION"""
#Controller_NB.CrearTabla()

game = Model_NB( starting_code=0, rows=0, columns=0, ship_count=0, hits=0, misses=0, total_shots=0, max_possible_shots=0, score=0)

# Pedir al usuario, los datos para llenar la instancia
game.starting_code = input( "Ingrese el codigo de la partida: ") # Maximo 5 digitos
game.rows = input("Ingrese el numero filas del tablero: ") # Maximo 1 digito
game.columns = input("Ingrese el numero de columnas: ")# Maximo 1 digito
game.ship_count = input("Ingrese el numero de barcos con los que quiere jugar: ") # Maximo 1 digito
game.score = input("Ingrese el puntaje de la partida: ") 

# Llamar al controlador para que inserte en la BD
Controller_NB.Insertar( game )

print( "Los datos de la partida se ingresaron exitosamente!")