#!/usr/bin/env python3
import pygame
import math

white = (255,255,255)

class Point:
    def __init__(self,args):
        self.screen = args.screen
        self.size = args.size
        self.obstacles = args.obstacles

        self.rays = []
        self.pos = [self.size[0]//2,self.size[1]//2]
        self.width = 1
        self.density = 10

    def update(self):
        degree = 0
        dif = 3
        length = 1000
        for _ in range(360//dif):
            point = [
                    self.pos[0] + math.cos(math.radians(degree)) * length,
                    self.pos[1] + math.sin(math.radians(degree)) * length
                    ]
            self.drawray(point)
            degree+=dif

    def intersect(self):
        is_points = []


    def drawray(self,point):
        pygame.draw.line(self.screen,white,self.pos,point,1)
