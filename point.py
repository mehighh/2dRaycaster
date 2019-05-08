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
        dif = 0.5
        length = 1000
        loopr = 0
        if dif >= 1:
            loopr = 360//dif
        else:
            loopr = int(360*(1/dif))
        for _ in range(loopr):
            point = [
                    self.pos[0] + math.cos(math.radians(degree)) * length,
                    self.pos[1] + math.sin(math.radians(degree)) * length
                    ]
            if not self.intersect(point): self.drawray(point)
            degree+=dif

    def intersect(self,point):
        is_points = []
        x3,y3 = self.pos
        x4,y4 = point
        for o in self.obstacles:
            x1,y1 = o.start_pos
            x2,y2 = o.end_pos

            den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
            if den != 0:
                t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)) / den
                u = -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3)) / den

                if t > 0 and t < 1 and u > 0:
                    is_points.append([x1+t*(x2-x1),y1+t*(y2-y1)])

        if is_points == []: return

        is_distances = []
        for p in is_points:
            is_distances.append(math.sqrt((p[0]-x3)**2+(p[1]-y3)**2))
        self.drawray(is_points[is_distances.index(min(is_distances))])
        return True

    def drawray(self,point):
        pygame.draw.line(self.screen,white,self.pos,point,1)
