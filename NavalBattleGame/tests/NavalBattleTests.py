import sys
import os

# Agregar la ruta al directorio raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Program import NavalBattle
import unittest

class GameTest(unittest.TestCase):

#Funcionalidad #1
#Inicializar campo de juego
    
    #Casos normales

    def testBoard(self):
        expected_board = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]
        
        game = NavalBattle.NavalBattle()
        board = game.generateBoard()
        self.assertEqual(expected_board, board)

    def testBoardSizes(self):
        expexted_board=[
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],]

        game = NavalBattle.NavalBattle()
        board= game.generateBoard()
        self.assertEqual(expexted_board, board)

    def testFourShips(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard(5,5)
        game.addShips(4)
        self.assertEqual(4, game.ships)

    #Casos extraordinarios
    def testSmallBoard(self):
        expexted_board=[
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],]

        game = NavalBattle.NavalBattle()
        board= game.generateBoard(5,5)
        self.assertEqual(expexted_board, board)



    def testBigBoard(self):
        game= NavalBattle.NavalBattle()
        self.assertRaises(NavalBattle.BoardIsTooBig, game.generateBoard, 21, 5)

    def testBigAndSmall(self):
        expexted_board=[
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],]

        game = NavalBattle.NavalBattle()
        board= game.generateBoard(9,9)
        self.assertEqual(expexted_board, board)


    #Casos de error
    def testZeroBoard(self):
        game= NavalBattle.NavalBattle()
        self.assertRaises(NavalBattle.BoardError, game.generateBoard, 0, 6)
    
    def testnegativeBoard(self):
        game= NavalBattle.NavalBattle()
        self.assertRaises(NavalBattle.BoardError, game.generateBoard, 6, -5)

    def testShipsInNoBoard(self):
        game = NavalBattle.NavalBattle()
        self.assertRaises(NavalBattle.BoardError, game.addShips, 4)

    def testIDontKnow(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()


#Funcionalidad 2
#Disparar
    #Casos normales
    def testHitShot(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard(5,5)
        game.addShipsInPosition((1,2))
        resultado = game.shoot("B3")

        self.assertEqual(resultado, True)

    def testMissedShot(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard(5,5)
        resultado = game.shoot("C2")

        self.assertEqual(resultado, False)

    def testDownedShip(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        game.addShipsInPosition((0,0), False, 2)
        game.shoot("A1")
        game.shoot("B1")
        
        self.assertTrue(game.downedShip())


    def testNotDownedShip(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        game.addShipsInPosition((0,0), False, 2)
        game.shoot("A1")
        
        self.assertFalse(game.downedShip())

    #Casos extraordinarios
    def testShotSamePlace(self):
        game= NavalBattle.NavalBattle()
        game.generateBoard()
        game.addShipsInPosition((2,1), False, 2)
        game.shoot("C2")
        self.assertFalse(game.shoot("C2"))


    def testCornerShot(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard(5,5)
        game.addShipsInPosition((4,0))
        self.assertEqual(game.shoot("e1"), True)


    def testLastOne(self):
        
        game = NavalBattle.NavalBattle()
        game.generateBoard(5,5)
        game.addShipsInPosition((4,0))
        self.assertEqual(game.shoot("e3"), True)

    #Casos de error
    def testInvalidCoordinate(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        self.assertRaises(NavalBattle.InvalidCoordinate, game.shoot, "A21")

    def testInvalidCoordinate2(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        self.assertRaises(NavalBattle.ColumnOutOfRange, game.shoot, "44")

    def testColumnOutOfRange(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        self.assertRaises(NavalBattle.ColumnOutOfRange, game.shoot, "K1")

    def testRowOutOfRange(self):
        game = NavalBattle.NavalBattle()
        game.generateBoard()
        self.assertRaises(NavalBattle.RowOutOfRange, game.shoot, "A9")


if __name__ == '__main__':
    unittest.main()