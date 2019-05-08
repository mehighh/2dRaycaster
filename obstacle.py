#!/usr/bin/env python3
import pygame
import random

white = (255,255,255)

class Obstacle:
    def __init__(self,args):
        self.screen = args.screen
        self.size = args.size

        self.width = 5
        self.start_pos = [50,100]
        self.end_pos = [10,300]

    def draw(self):
        pygame.draw.line(self.screen,white,
                self.start_pos,self.end_pos,self.width)
