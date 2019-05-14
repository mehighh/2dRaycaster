#!/usr/bin/env python3
import pygame
from obstacle import Obstacle
from point import Point

class Args:
  def __init__(self):
    self.size = (800,800)
    self.screen = pygame.display.set_mode(self.size)
    pygame.display.set_caption('Raycaster')

    self.obstaclecount = 9
    self.obstacles = []
    for _ in range(self.obstaclecount):
      self.obstacles.append(Obstacle(self))

    self.point = Point(self)

def run(args):
  args.screen.fill(0)
  args.point.update()
  for o in args.obstacles:
    o.draw()

if __name__ == '__main__':
  pygame.init()
  ARGS = Args()

  view_right = False
  view_left = False

  move_right = False
  move_left = False
  move_fwd = False
  move_bwd = False

while True:
    if view_right:
      ARGS.point.view_angle += 3
      if ARGS.point.view_angle > 360: ARGS.point.view_angle = 0
    if view_left:
      ARGS.point.view_angle -= 3
      if ARGS.point.view_angle < 0: ARGS.point.view_angle = 360
    if move_fwd: pass
    if move_bwd: pass
    if move_left: pass
    if move_right: pass
    for event in pygame.event.get():
      # This sets the pos by mouse
      ARGS.point.pos = pygame.mouse.get_pos()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          view_right = True
        if event.key == pygame.K_LEFT:
          view_left = True

        if event.key == pygame.K_w:
          move_fwd = True
        if event.key == pygame.K_s:
          move_bwd = True
        if event.key == pygame.K_a:
          move_left = True
        if event.key == pygame.K_d:
          move_right = True

      if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
          view_right = False
        if event.key == pygame.K_LEFT:
          view_left = False

        if event.key == pygame.K_w:
          move_fwd = False
        if event.key == pygame.K_s:
          move_bwd = False
        if event.key == pygame.K_a:
          move_left = False
        if event.key == pygame.K_d:
          move_right = False

      if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    run(ARGS)
    pygame.display.update()

