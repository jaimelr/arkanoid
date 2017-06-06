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

    def test_init_pos(self):
        ball = Ball()
        self.assertEqual(ball.position, [320, 450])

    def test_init_vel(self):
        ball = Ball()
        self.assertEqual(ball.velocity, [0, 0])

    def test_reset_ball_status(self):
        ball = Ball()
        ball.reset()
        self.assertEqual(ball.position, [320, 450])
        self.assertEqual(ball.velocity, [0, 0])

    def test_get_ball_position(self):
        ball = Ball()
        [x, y] = ball.pos()
        self.assertEqual([x, y], [320, 450])

    def test_get_ball_speed(self):
        ball = Ball()
        vel = ball.speed()
        self.assertEqual(vel, [0, 0])

    def test_ball_speed_change(self):
        ball = Ball()
        ball.speedChange(10, 10)
        self.assertIsNot(ball.velocity, [0, 0])

    def test_ball_collision_limits(self):
        ball = Ball()
        self.assertFalse(ball.collideWithWall())

    def test_ball_move(self):
        ball = Ball()
        ball.move(25, 35)
        self.assertEqual(ball.position[0], 345)
        self.assertEqual(ball.position[1], 469)

if __name__=='__main__':
    unittest.main()
