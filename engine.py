import pygame
from pygame.locals import *
import utils
import sys

pygame.init()

keys = pygame.key.get_pressed()
font = pygame.font.Font(pygame.font.get_default_font(), 24)

size = width, height = 1920, 1080
colors  =   {"red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "brown": (153, 76, 0),
            "grey": (61, 59, 52),
            "gold": (255, 215, 0),
            "bright_red": (155, 0, 56),
            "bright_gold": (255, 255, 0),
            "yellow" : (186, 149, 13)
            }

class window:
    scene = "menu"

# def wait_for_command():
#     h = "esperando"

#     while h == "esperando":
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN and event.key == K_1:
#                 h = "pedra"
#                 return h
#             if event.type == KEYDOWN and event.key == K_2:
#                 h = "papel"
#                 return h
#             if event.type == KEYDOWN and event.key == K_3:
#                 h = "tesoura"
#                 return h

# def play_again():

#     running = False
#     window = utils.generate_window()
#     window.screen.fill("gray")
#     utils.drawText(window.screen, "Se você deseja jogar novamente, aperte 4", 150, 150)
#     utils.drawText(window.screen, "Se você deseja sair, aperte 5", 200, 200)

#     pygame.display.update()

#     while running == False:
#         for event in pygame.event.get():
#             if event.type == QUIT or event.type == KEYDOWN and event.key == K_5:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN and event.key == K_4:
#                 running = True
#                 return running

class play_again(pygame.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self.size = width, height = 600, 300
        self.image = pygame.Surface(self.size)
        red = pygame.image.load("graphics\\red.png")
        self.window = window
        self.pos = self.w, self.h = (1920 * 0.3, 1080 * 0.3)

        window.screen.blit(red, self.pos)
        utils.drawText(window.screen, "Deseja continuar a jogar?", self.w + 10, self.h + 10)

    def choose(window):

        pos = w, h = (1920 * 0.3, 1080 * 0.3)

        gui = pygame.sprite.Group()

        sim_button = utils.choice_button((w + 20, h + 200), "SIM", window)
        nao_button = utils.choice_button((w + 20 + 150, h + 200), "NAO", window)

        gui.add(sim_button, nao_button)
        gui.update()
        gui.draw(window.screen)

        pygame.display.update()

        choice = None

        while choice != "SIM" or choice != "NAO":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for button in gui:
                    choice = button.handle_event(event)
                    if choice != None:
                        return choice

def combat():
    
    gui = pygame.sprite.Group()

    window = utils.generate_window()

    window.screen.fill(colors["grey"])
    utils.drawText(window.screen, "Faça a sua jogada: ", 0, 0)
    
    pedra_button = utils.choice_button((width * 0.20, height * 0.6), "pedra", window)
    papel_button = utils.choice_button((width * 0.20 + 300, height * 0.6), "papel", window)
    tesoura_button = utils.choice_button((width * 0.20 + 600, height * 0.6), "tesoura", window)

    gui.add(pedra_button, papel_button, tesoura_button)
    gui.update()
    gui.draw(window.screen)

    pygame.display.update()

    h = None

    while h != "pedra" or h != "papel" or h != "tesoura":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for button in gui:
                h = button.handle_event(event)
                if h != None:
                    return h