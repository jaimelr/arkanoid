import unittest
import pygame
from GameModule import Brick
from GameModule.Constants import *

class BrickTestCase(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.mixer.init(11025)
        self.display = pygame.display.set_mode( gfx["screen"] )

    def test_brick_init_pos_x(self):
        brick = Brick(0, 0)
        self.assertEqual(brick.x, 0)

    def test_brick_init_pos_y(self):
        brick = Brick(0, 0)
        self.assertEqual(brick.y, 0)

    def test_brick_init_pos_realx(self):
        brick = Brick(0, 0)
        self.assertEqual(brick.realx, 0)

    def test_brick_init_pos_realx(self):
        brick = Brick(0, 0)
        self.assertEqual(brick.realy, 0)

    def test_brick_form(self):
        brick = Brick(0, 0)
        rect = pygame.Rect(0,0,0,0)
        self.assertEqual(brick.rect, rect)

    def test_get_brick_type(self):
        brick = Brick(0, 0)
        self.assertEqual(brick.getType(), "brick")

if __name__=='__main__':
    unittest.main()
