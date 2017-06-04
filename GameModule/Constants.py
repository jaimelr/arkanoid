#!/usr/bin/python2.7
# Encoding: utf-8

version = "1.0"

states = {
  "START": 0,
  "PROGRESS": 1,
  "GAMEOVER": 2,
  "PAUSE": 3
}

levels = [
  "first.map",
  "second.map",
  "third.map",
]

startState = {
  "lives": 2,
}

gfx = {
  "framerate": 40,
  "screen": (640,480),
  "grid": (40,20)
}
