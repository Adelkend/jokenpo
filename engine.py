import pygame
from pygame.locals import *
import utils

pygame.init()

keys = pygame.key.get_pressed()

yellow = 186, 149, 13
gray = 61, 59, 52

class window:
    scene = "menu"

def wait_for_command():
    h = "esperando"

    while h == "esperando":
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_1:
                h = "pedra"
                return h
            if event.type == KEYDOWN and event.key == K_2:
                h = "papel"
                return h
            if event.type == KEYDOWN and event.key == K_3:
                h = "tesoura"
                return h

def play_again():

    running = False
    screen = utils.generate_window()
    screen.fill(gray)
    utils.drawText(screen, "Se você deseja jogar novamente, aperte 4", 150, 150)
    utils.drawText(screen, "Se você deseja sair, aperte 5", 200, 200)

    pygame.display.update()

    while running == False:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_5:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_4:
                running = True
                return running
            
