import unittest
import pygame
from GameModule import Ball
from GameModule.Constants import *

class BallTestCase(unittest.TestCase):

    """Prueba para clase independiente Ball"""

    def setUp(self):
        pygame.init()
        pygame.mixer.init(11025)
        self.display = pygame.display.set_mode( gfx["screen"] )

    def test_ball_init_speed(self):
        ball = Ball()
        ball.speedChange(10, 10)
        self.assertEqual(ball.velocity, [0, 0])

if __name__=='__main__':
    unittest.main()
