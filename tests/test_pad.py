import unittest
import pygame
from GameModule import Pad
from GameModule.Constants import *

class TestPadCase(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.mixer.init(11025)
        self.display = pygame.display.set_mode( gfx["screen"] )

    def test_grid_width(self):
        pad = Pad()
        self.assertEqual(pad.gridWidth, 3)

    def test_pad_init_pos(self):
        pad = Pad()
        self.assertEqual(pad.position, [280, 460])

    def test_tab_images_loaded(self):
        pad = Pad()
        self.assertNotEqual(pad.graphics, {})

    def test_tab_rect(self):
        pad = Pad()
        rect = pygame.Rect(280, 460, 120, 20)
        self.assertEqual(pad.rect, rect)

    def test_last_move_init_state(self):
        pad = Pad()
        self.assertEqual(pad.lastMove, -1)

    def test_pad_reset_state(self):
        pad = Pad()
        self.assertEqual(pad.gridWidth, 3)
        self.assertEqual(pad.position, [280, 460])
        self.assertEqual(pad.lastMove, -1)

    def test_is_pad_move(self):
        pad = Pad()
        self.assertTrue(pad.move(10))

    def test_tab_rect(self):
        pad = Pad()
        pad.setWidth(4)
        rect = pygame.Rect(280, 460, 160, 20)
        self.assertEqual(pad.rect, rect)

    def test_get_pad_pos(self):
        pad = Pad()
        (x, y) = (pad.position[0], pad.position[1])
        self.assertEqual(pad.pos(), (x, y))
