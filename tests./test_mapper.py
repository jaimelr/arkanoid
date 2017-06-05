#prueba para la clase Mapper, la cual acciona el error cuando uno de los bloques no es seleccionado para pintar
import unittest

from Arkanoid import *
from Mapper import Mapper

class TestMapper(unittest.TestCase):
	def test_is_type_brick(self):
		brick = Mapper()
		self.failUnlessRaises(ValueError, brick)

if __name__=='__main__':
    unittest.main()
