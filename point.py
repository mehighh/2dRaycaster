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

    self.view_angle = 0
    self.view_range = 40
    self.view_distance = int(self.size[0]//2)

    self.points = []
    self.dists = []

  def update(self):
    degree = self.view_angle
    dif = self.view_range / self.size[0]

    self.points = []
    self.dists = []

    target_angle = self.view_angle + self.view_range
    while int(degree) != target_angle:
      point = [self.pos[0] + math.cos(math.radians(degree)) * self.view_distance,
              self.pos[1] + math.sin(math.radians(degree)) * self.view_distance]
      try:
        point = self.intersect(point)
      except:
        # if the ray does not intersect
        pass

      # This draws the separate rays
      # self.drawray(point)

      self.points.append(point)
      self.dists.append(math.sqrt((point[0]-self.pos[0])**2+
                                  (point[1]-self.pos[1])**2))
      degree+=dif

    # This draws the solid poligon
    # pygame.draw.polygon(self.screen,white,self.points,0)
    # This draws the view point
    # print('update')
    self.drawwalls()
    pygame.draw.circle(self.screen,(0,0,255),self.pos,8,2)

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

    is_distances = []
    for p in is_points:
      is_distances.append(math.sqrt((p[0]-x3)**2+(p[1]-y3)**2))
    if min(is_distances) > self.view_distance: is_distances = []
    return is_points[is_distances.index(min(is_distances))]

  def drawray(self,point):
    pygame.draw.line(self.screen,white,self.pos,point,1)

  def drawwalls(self):
    i = 0
    for point,dist in zip(self.points,self.dists):
      shade = 255 * (self.view_distance - dist) / self.view_distance
      size = self.size[1]*(dist/self.view_distance)
      pygame.draw.line(self.screen,(shade,shade,shade),
          (i,int(size/2)),(i,self.size[1]-int(size/2)),1)
      i += 1
    for point in self.points:
      self.drawray(point)
