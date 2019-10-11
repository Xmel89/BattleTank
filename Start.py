# -*- coding:utf-8 -*-
import pygame, os
import Render, Phisics

wi = 1200
hi = 800
screen2 = pygame.display.set_mode((wi, hi))
pygame.display.set_caption('Battle tank')            #name window
loc = os.getcwd()+'/img/'
Pz5 = Render.Render(loc+'Pz-5corpM.png', 50, 50, 300, screen2, 0)
TurmPz5 = Render.Render(loc+'TurmPz5MC.png', 500, 250, 300, screen2, 0)
Pz5USSR = Render.Render(loc+'Pz-5corpUSSR.png', 50, 50, 300, screen2, 0)
TurmPz5USSR = Render.Render(loc+'TurmPz5USSR.png', 500, 250, 300, screen2, 0)
Xmark = Render.Render(loc+'X.png', TurmPz5.x, TurmPz5.y, 0, screen2, 0, 150)
Shell = Render.Render(loc+'Shellmini3.png', 50, 50, 0, screen2, 0, None, 0, 0)
clock = pygame.time.Clock()
done = True


while done:
    #Phisics.phisics(Pz5, TurmPz5, Xmark, Shell)
    screen2.fill((50, 50, 0))           #color field
    Pz5.render
    Pz5USSR.render
    TurmPz5.x, TurmPz5.y = Pz5.x, Pz5.y
    TurmPz5USSR.x, TurmPz5USSR.y = Pz5USSR.x, Pz5USSR.y
    Shell.render
    TurmPz5.render
    TurmPz5USSR.render
    Xmark.render
    Phisics.phisics(Pz5, TurmPz5, Xmark, Shell)
    clock.tick(100)
    pygame.display.update()