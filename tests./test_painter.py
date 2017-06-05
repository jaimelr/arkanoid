import unittest

from Arkanoid import * 
from Painter import *

class TestPainter(unittest.TestCase):
	def test_is_it_pause(self):
		pause = Painter()
		self.failUnlessRaises(ValueError, pause)

if __name__=='__main__':
    unittest.main()
