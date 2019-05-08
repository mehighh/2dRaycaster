#!/usr/bin/env python3
import pygame
from obstacle import Obstacle
from point import Point

class Args:
    def __init__(self):
        self.size = (800,800)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Raycaster')

        self.obstaclecount = 5
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
    run(ARGS)
    while True:
        for event in pygame.event.get():
            ARGS.point.pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        run(ARGS)
        pygame.display.update()
