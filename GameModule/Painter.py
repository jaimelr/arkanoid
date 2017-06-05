#!/usr/bin/python2.7
#Encoding: utf-8

import pygame
import GameModule.Constants

class Painter:
  def __init__( self, display, objects, state ):
    self.display = display
    self.objects = objects
    self.state = state
    self.paused = False
    if self.paused != False:
      raise ValueError('El juego ha sido pausado')
    #else:
     # raise ValueError('Todo es correcto')

  def draw(self):
    if self.objects.background() != None:
      self.display.blit( self.objects.background(), (0,0) )

    self.display.blit( self.objects.pad().makeSurface(), self.objects.pad().pos() )
    balls = self.objects.balls()
    for ball in balls:
      self.display.blit( ball.image, ball.pos() )

    grid = self.objects.grid()
    for elem in grid:
      self.display.blit( elem.image, elem.rect.topleft )

    powerups = self.objects.powerups()
    for power in powerups:
      self.display.blit( power.image, power.rect.topleft )

    font = pygame.font.SysFont( "monospace", 12, True )

    points = font.render( "Nivel " + str(self.state.level+1) + " Puntos: " + str(self.state.points) + " Vida: " + str(self.state.lives), True, (0,0,0), (255,255,255) )

    self.display.blit( points, ( 10, 10 ) )

    if self.paused:
      font2 = pygame.font.SysFont( "sans-serif", 48, True )
      pauseText = font2.render( "PAUSA", True, (0,0,0) )
      px,py = pauseText.get_size()
      self.display.blit( pauseText, ( 320 - px/2, 240 - py/2 ) )
