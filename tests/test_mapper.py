import unittest
import pygame
from GameModule import Objects
from GameModule import Mapper
from GameModule.Constants import *


class TestMapperCase(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.mixer.init(11025)
        self.display = pygame.display.set_mode( gfx["screen"] )

    def test_get_brick_to_map(self):
        objects = Objects()
        mapper = Mapper(objects)
        self.assertIsNotNone(mapper.getBrick("solid", 10, 10))
        self.assertIsNotNone(mapper.getBrick("ghost", 10, 10))
        self.assertIsNotNone(mapper.getBrick("simple", 10, 10))
        self.assertIsNone(mapper.getBrick("unknown", 10, 10))
