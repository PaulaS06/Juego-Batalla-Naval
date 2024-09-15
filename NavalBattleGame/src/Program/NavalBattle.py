import random

# Excepciones personalizadas para diferentes errores relacionados con el juego.
class NotEnoughSpace(Exception):
    """Se lanza cuando no hay suficiente espacio para los barcos."""
    pass

class BoardIsTooSmall(Exception):
    """Se lanza cuando el tablero es demasiado pequeño."""
    pass

class BoardIsTooBig(Exception):
    """Se lanza cuando el tablero es demasiado grande."""
    pass

class RowOutOfRange(Exception):
    """Se lanza cuando la fila seleccionada está fuera del rango permitido."""
    pass

class ColumnOutOfRange(Exception):
    """Se lanza cuando la columna seleccionada está fuera del rango permitido."""
    pass

class BoardIsBigAndSmall(Exception):
    """Se lanza cuando el tablero tiene dimensiones conflictivas."""
    pass

class BoardError(Exception):
    """Error genérico relacionado con el tablero."""
    pass

class InvalidCoordinate(Exception):
    """Se lanza cuando se ingresa una coordenada inválida."""
    pass

class NavalBattle:
    # Atributos de clase
    last_hit = None
    ships_quantity = 0
    COLUMNS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
    FIXED_COLUMNS = [" A"," B"," C"," D"," E"," F"," G"," H"," I"," J"," K"," L"," M"," N"," O"," P"," Q"," R"," S"," T"]
    board = None
    EMOJIS={
    "colition" : "\U0001F4A5",
    "water" : "\U0001F4A6",
    "ship" :"\U0001F6A2",
    "question" :"\U00002754",
    "wave" : "\U0001F30A"
    }
    shooting_history=set()


    
    def validateBoardDimensions(self, w, h):
        """
        Valida las dimensiones del tablero y lanza excepciones si no son válidas.

        Parámetros:
        w -- número de columnas del tablero.
        h -- número de filas del tablero.

        Excepciones:
        Lanza BoardError si las dimensiones son negativas o inválidas.
        """
        if w < 0 or h < 0:
            raise BoardError("Board can't have negative rows or columns")
        elif w == 0 or h == 0:
            raise BoardError("Board can't have zero rows or columns")
        elif (w < 5 and h > 9) or (h < 5 and w > 9):
            raise BoardIsBigAndSmall
        elif w < 5 or h < 5:
            raise BoardIsTooSmall
        elif w > 9 or h > 9:
            raise BoardIsTooBig


    def generateBoard(self, w=8, h=5):
        """
        Genera un tablero de juego con dimensiones especificadas.

        Parámetros:
        w -- número de columnas del tablero.
        h -- número de filas del tablero.

        Retorna:
        El tablero generado como una lista de listas.
        """
        # Validar las dimensiones antes de generar el tablero
        self.validateBoardDimensions(w, h)
        
        self.w = w
        self.h = h
        self.board = [[0 for j in range(w)] for i in range(h)] 
        self.player_board = [[self.EMOJIS["question"] for i in range(w)] for i in range(h)]  # Tablero visual para el jugador

        return self.board


        return self.board
    
    def addShipsInPosition(self, position, vertical=True, len=3):
        """
        Añade un barco en una posición específica del tablero.

        Parámetros:
        position -- una tupla con las coordenadas (columna, fila) donde colocar el barco.
        vertical -- indica si el barco se coloca verticalmente o no.
        len -- longitud del barco.
        """
        enough_space = True

        i = position[1]
        j = position[0]

        if vertical:
            # Verifica si hay suficiente espacio verticalmente
            for s in range(len):
                if self.board[i][j] != 0:
                    enough_space = False
                i += 1
            i -= len
            # Si hay espacio suficiente, coloca el barco
            if enough_space:
                for s in range(len):
                    self.board[i][j] = len
                    i += 1
                self.ships_quantity += 1
                len -= 1
            else:
                raise NotEnoughSpace
            
        elif not vertical:
            # Verifica si hay suficiente espacio horizontalmente
            for s in range(len):
                if self.board[i][j] != 0:
                    enough_space = False
                j += 1
            j -= len
            # Si hay espacio suficiente, coloca el barco
            if enough_space:
                for s in range(len):
                    self.board[i][j] = len
                    j += 1
                self.ships_quantity += 1
                len -= 1
            else:
                raise NotEnoughSpace
             
    def addShips(self, num_ships, limit=8):
        """
        Añade una cantidad específica de barcos al tablero aleatoriamente.

        Parámetros:
        num_ships -- número de barcos a añadir.
        limit -- límite máximo de barcos permitidos.

        Excepciones:
        Lanza NotEnoughSpace si la cantidad de barcos supera el límite.
        """
        if num_ships > limit:
            raise NotEnoughSpace
        ship_len = num_ships + 1
        if self.board is None:
            raise BoardError
        # Intenta añadir barcos hasta alcanzar la cantidad deseada
        while self.ships_quantity < num_ships:
            enough_space = True
            vertical = random.choice([True, False])

            if vertical:
                # Coloca el barco verticalmente
                i = random.randint(0, self.h - ship_len)
                j = random.randint(0, self.w - 1)
                for s in range(ship_len):
                    if self.board[i][j] != 0:
                        enough_space = False
                    i += 1
                i -= ship_len
                if enough_space:
                    for s in range(ship_len):
                        self.board[i][j] = ship_len
                        i += 1
                    self.ships_quantity += 1
                    ship_len -= 1
            else:
                # Coloca el barco horizontalmente
                i = random.randint(0, self.h - 1)
                j = random.randint(0, self.w - ship_len)
                for s in range(ship_len):
                    if self.board[i][j] != 0:
                        enough_space = False
                    j += 1
                j -= ship_len
                if enough_space:
                    for s in range(ship_len):
                        self.board[i][j] = ship_len
                        j += 1
                    self.ships_quantity += 1
                    ship_len -= 1

    def validateCoordinate(self, coordinate: str):
        """
        Valida la coordenada proporcionada para un disparo.

        Parámetros:
        coordinate -- coordenada en formato "C2" (columna, fila).

        Excepciones:
        Lanza InvalidCoordinate si la coordenada es inválida.
        Lanza RowOutOfRange y ColumnOutOfRange si la coordenada está fuera de los límites.

        Retorna:
        Una tupla con el índice de la fila y la columna válidos.
        """
        coordinate = coordinate.upper()
        if len(coordinate) != 2:
            raise InvalidCoordinate
        
        column = coordinate[0]
        try:
            row = int(coordinate[1]) - 1
        except ValueError:
            raise InvalidCoordinate

        # Verifica si la fila está en el rango válido
        if row < 0 or row >= len(self.board):
            raise RowOutOfRange
        
        # Verifica si la columna está en el rango válido
        if column not in self.COLUMNS:
            raise ColumnOutOfRange
        
        column_index = self.COLUMNS.index(column)
        if column_index >= len(self.board[0]):
            raise ColumnOutOfRange
        
        return row, column_index




    def shoot(self, coordinate: str):
        """
        Realiza un disparo a una coordenada específica.

        Parámetros:
        coordinate -- coordenada en formato "C2" (columna, fila).

        Retorna:
        True si el disparo impacta un barco, False si impacta agua.
        """
        # Validar la coordenada antes de realizar el disparo
        row, column = self.validateCoordinate(coordinate)

        # Verifica si el disparo impacta un barco
        if self.board[row][column] != 0:
            self.last_hit = self.board[row][column]
            self.board[row][column] = True
            self.player_board[row][column] = self.EMOJIS["colition"]  # Muestra el impacto en el tablero del jugador
            return True
        else:
            # Disparo en el agua
            self.player_board[row][column] = self.EMOJIS["wave"]
            return False
        
    def isCoordinateAlreadyShot(self, coordinate):
        if coordinate in self.shooting_history:
            return True
        else:
            self.shooting_history.add(coordinate)
            return False
        
    def isShipDowned(self):
        """
        Verifica si el último barco impactado ha sido hundido completamente.
        """
        # Revisa si aún quedan partes del barco en el tablero
        for h in range(len(self.board)):
            for w in range(len(self.board[0])):
                if self.last_hit == self.board[h][w]:
                    return False

        self.ships_quantity -= 1
        # Muestra el número de impactos del barco hundido
        self.showInfo()
        return True

    def showInfo(self):
        """Muestra la cantidad de barcos restantes en el juego."""
        print(f"Missing Ships: {self.ships_quantity}")
        
    def showPlayerBoard(self):
        """Muestra el tablero del jugador."""
        print(self.FIXED_COLUMNS[:self.w])
        for fila in self.player_board:
            print(fila)

