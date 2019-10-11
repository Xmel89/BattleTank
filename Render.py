import pygame

class Render:
    def __init__(self, name, x, y, angle, screen, v,  r = None, begtime = None, lenXmark = None):
        self.image2 = pygame.image.load(name)
        self.rect = self.image2.get_rect()
        self.x = x
        self.y = y
        self.angle = angle
        self.screen = screen
        self.v = v
        self.r = r
        self.begtime = begtime
        self.lenXmark = lenXmark
    @property
    def render (self):         #rotate image
        image = pygame.transform.rotate(self.image2, self.angle)
        self.rect.center = (self.x, self.y)
        self.rect = image.get_rect(center=self.rect.center)
        self.screen.blit(image, self.rect)