#!/usr/bin/env python3
import pygame
import math
from obstacle import Obstacle
from point import Point

class Args:
  def __init__(self):
    self.size = (1000,700)
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
    degree = ARGS.point.view_angle + (ARGS.point.view_range / 2)
    move_rate = 5
    turn_rate = 3

    # CONTROL VIEW ANGLE
    if view_right:
      ARGS.point.view_angle += turn_rate
      if ARGS.point.view_angle > 360: ARGS.point.view_angle = 0
    if view_left:
      ARGS.point.view_angle -= turn_rate
      if ARGS.point.view_angle < 0: ARGS.point.view_angle = 360

    # CONTROL MOVEMENT
    if move_fwd:
      ARGS.point.pos = [int(ARGS.point.pos[0] + math.cos(math.radians(degree)) * move_rate),
                        int(ARGS.point.pos[1] + math.sin(math.radians(degree)) * move_rate)]
    if move_bwd:
      ARGS.point.pos = [int(ARGS.point.pos[0] + math.cos(math.radians(degree + 180)) * move_rate),
                        int(ARGS.point.pos[1] + math.sin(math.radians(degree + 180)) * move_rate)]
    if move_left:
      ARGS.point.pos = [int(ARGS.point.pos[0] + math.cos(math.radians(degree - 90)) * move_rate),
                        int(ARGS.point.pos[1] + math.sin(math.radians(degree - 90)) * move_rate)]
    if move_right:
      ARGS.point.pos = [int(ARGS.point.pos[0] + math.cos(math.radians(degree + 90)) * move_rate),
                        int(ARGS.point.pos[1] + math.sin(math.radians(degree + 90)) * move_rate)]

    for event in pygame.event.get():
      # This sets the pos by mouse
      # ARGS.point.pos = pygame.mouse.get_pos()

      # MANAGE INPUT (holding keys)
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
