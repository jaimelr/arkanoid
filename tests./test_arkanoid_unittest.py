import unittest
from Arkanoid import Game

class GuiTestCase(unittest.TestCase):
    """Prueba si el juego termino o no correctamente"""

    def test_is_state_start(self):
        game = Game()
        self.failUnlessRaises(ValueError, game)

    def test_is_clock_enable(self):
        game = Game()
        self.failUnlessRaises(ValueError, game)

if __name__=='__main__':
    unittest.main()
