#!/usr/bin/env python3
import pygame
import random

red = (255,0,0)

class Obstacle:
    def __init__(self,args):
        self.screen = args.screen
        self.size = args.size

        self.width = 9
        self.start_pos = [random.randint(0,self.size[0]),random.randint(0,self.size[1])]
        self.end_pos = [random.randint(0,self.size[0]),random.randint(0,self.size[1])]
    def draw(self):
        pygame.draw.line(self.screen,red,self.start_pos,self.end_pos,self.width)
