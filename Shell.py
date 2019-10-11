import pygame

class Shell():
    def __init__(self, xid, yid, namesh = None, filename = None, \
ranged = None, breake = None, burst = None):
        self.x = xid
        self.y = yid
        self.namesh = namesh
        self.ranged = ranged
        self.breake = breake
        self.burst = burst
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))