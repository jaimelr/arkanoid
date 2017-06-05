import unittest
import sys
from GameModule import Painter

class GuiTestCase(unittest.TestCase):

"""Prueba si el reloj para refrescar la pantall fue inicializado correctamente"""

    def test_is_clock_enable(self):
        game = Game()
        self.failUnlessRaises(ValueError, game)

if __name__=='__main__':
    unittest.main()
