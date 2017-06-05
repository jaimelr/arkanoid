import unittest
import sys
from GameModule import *
#from Arkanoid import Game


class EventTestCase(unittest.TestCase):

    """Prueba si el reloj para refrescar la pantall fue inicializado correctamente"""

    #def test_is_clock_enable(self):
        #game = Game()
        #self.failUnlessRaises(ValueError, game)

    #def test_level_map_file_exists(self):
		#objects = Objects()
        #mapper = Mapper(self, objects)
		#self.failUnlessRaises(ValueError, level)

    #def test_is_it_pause(self):
		#objects = Objects(self)
        #painter = Painter(self, objects)
		#self.failUnlessRaises(ValueError, pause)

if __name__=='__main__':
    unittest.main()
