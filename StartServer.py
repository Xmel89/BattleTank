# -*- coding:utf-8 -*-
import pygame, os, json
import Render, Phisics
from socket import *

#############Сервер##############
port = 9090
addr = ('', port)

tcp_socket = socket(AF_INET, SOCK_STREAM)

#bind - связывает адрес и порт с сокетом
tcp_socket.bind(addr)

#listen - запускает прием TCP
tcp_socket.listen(2)
################################

wi = 1200
hi = 800
screen2 = pygame.display.set_mode((wi, hi))
pygame.display.set_caption('Battle tank server')            #name window
loc = os.getcwd()+'/img/'

Pz5 = Render.Render(loc+'Pz-5corpM.png', 50, 50, 300, screen2, 0)
TurmPz5 = Render.Render(loc+'TurmPz5MC.png', 500, 250, 300, screen2, 0)

Pz5USSR = Render.Render(loc+'Pz-5corpUSSR.png', 50, 50, 300, screen2, 0)
TurmPz5USSR = Render.Render(loc+'TurmPz5USSR.png', 500, 250, 300, screen2, 0)
Xmark = Render.Render(loc+'X.png', TurmPz5.x, TurmPz5.y, 0, screen2, 0, 150)
Shell = Render.Render(loc+'Shellmini3.png', 50, 50, 0, screen2, 0, None, 0, 0)
clock = pygame.time.Clock()

while True:
    #Phisics.phisics(Pz5, TurmPz5, Xmark, Shell)
    screen2.fill((50, 50, 0))           #color field
    Pz5.render
    TurmPz5.x, TurmPz5.y = Pz5.x, Pz5.y
    TurmPz5.render


    # accept - принимает запрос и устанавливает соединение, (по умолчанию работает в блокирующем режиме)
    conn, addr = tcp_socket.accept()

    # recv - получает сообщение TCP
    response = conn.recv(4096)
    response = json.loads(response.decode())
    toClientData = [Pz5.x, Pz5.y, Pz5.angle,TurmPz5.angle]
    toClientData = json.dumps(toClientData, ensure_ascii=False).encode()
    conn.send(toClientData)
    conn.close()

    Pz5USSR.x, Pz5USSR.y, Pz5USSR.angle, TurmPz5USSR.angle = response[0], response[1], response[2], response[3]
    Pz5USSR.render
    TurmPz5USSR.x, TurmPz5USSR.y = Pz5USSR.x, Pz5USSR.y
    TurmPz5USSR.render
    Shell.render
    Xmark.render
    Phisics.phisics(Pz5, TurmPz5, Xmark, Shell)
    clock.tick(100)
    pygame.display.update()