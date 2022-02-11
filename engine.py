import pygame
from pygame.locals import *
import utils, login
import sys
import json
import os

pygame.init()

keys = pygame.key.get_pressed()
font = pygame.font.Font("fonts\\KellySlab-Regular.ttf", 24)

size = width, height = 1920, 1080
colors  =   {"red": (255, 0, 0),
            "green": (0, 255, 0),
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "grey": (61, 59, 52),
            "bright_red": (155, 0, 56),
            "purple" : (205, 48, 238),
            "green" : (175, 251, 205)
            }

class window:
    scene = "login"

class login_window(pygame.sprite.Sprite):
    def __init__(self,window):
        super().__init__()
        self.size = 600, 300
        self.image = pygame.Surface(self.size)
        red = pygame.image.load("graphics\\red.png")
        self.window = window
        self.pos = self.w, self.h = (1920 * 0.3, 1080 * 0.3)
        window.screen.fill(colors["black"])
        window.screen.blit(red, self.pos)
        self.rect = self.image.get_rect(topleft=self.pos)

        pygame.display.update()

    def get_id(self):
        waiting = True

        while waiting == True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        username = input('username')
                        password = input('password')
                        waiting = False

        result = login.login(username, password)
        return result
                
class play_again(pygame.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self.size = width, height = 600, 300
        self.image = pygame.Surface(self.size)
        red = pygame.image.load("graphics\\red.png")
        self.window = window
        self.pos = self.w, self.h = (1920 * 0.3, 1080 * 0.3)

        window.screen.blit(red, self.pos)
        utils.drawText(window.screen, "Deseja continuar a jogar?", self.w + 10, self.h + 10, 24, colors["white"])

    def choose(window):

        pos = w, h = (1920 * 0.3, 1080 * 0.3)

        gui = pygame.sprite.Group()

        sim_button = utils.choice_button((w + 20, h + 200), "SIM", 24, window)
        nao_button = utils.choice_button((w + 20 + 150, h + 200), "NAO", 24, window)

        gui.add(sim_button, nao_button)

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

            gui.update()
            gui.draw(window.screen)

def combat():
    
    gui = pygame.sprite.Group()

    window = utils.generate_window()

    window.screen.fill(colors["black"])

    score_track(window.screen)
    utils.drawText(window.screen, "Choose your weapon", 325, 89, 144, colors["white"])

    pedra_image = pygame.image.load("graphics\\stone.png")
    papel_image = pygame.image.load("graphics\\paper.png")
    tesoura_image = pygame.image.load("graphics\\scissors.png")

    window.screen.blit(pedra_image, (854, 498))
    window.screen.blit(papel_image, (1436, 498))
    window.screen.blit(tesoura_image, (264, 510))
    
    pedra_button = utils.choice_button((251, 792), "scissors", 72, window)
    papel_button = utils.choice_button((904, 792), "rock", 72, window)
    tesoura_button = utils.choice_button((1453, 792), "paper", 72, window)

    gui.add(pedra_button, papel_button, tesoura_button)
    

    pygame.display.update()

    h = None

    while h != "rock" or h != "paper" or h != "scissors":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for button in gui:
                h = button.handle_event(event)
                if h != None:
                    return h

        gui.update()
        gui.draw(window.screen)


def score_track(screen):
    filepath = os.path.join(os.path.dirname("jokenpo"), 'score.json')
    with open(filepath, "r") as json_file:
        score = json.load(json_file)

    vitorias = str(score["vitorias"])
    empates = str(score["empates"])
    derrotas = str(score["derrotas"])

    utils.drawText(screen, "Vitorias: " + vitorias, 1500, 10, 24, colors["white"])
    utils.drawText(screen, "Empates: " + empates, 1500, 40, 24, colors["white"])
    utils.drawText(screen, "Derrotas: " + derrotas, 1500, 70, 24, colors["white"])

def score_update(result):
    filepath = os.path.join(os.path.dirname("jokenpo"), 'score.json')
    with open(filepath, "r") as json_file:
        score = json.load(json_file)

    new_score = {}

    if result == "e":
        score_increase = score["empates"] + 1
        new_score = {"vitorias": score["vitorias"], "empates": score_increase, "derrotas": score["derrotas"]}
        with open(filepath, "w") as json_file:
            json.dump(new_score, json_file)

    elif result == "v":
        score_increase = score["vitorias"] + 1
        new_score = {"vitorias": score_increase, "empates": score["empates"], "derrotas": score["derrotas"]}
        with open(filepath, "w") as json_file:
            json.dump(new_score, json_file)
        
    elif result == "d":
        score_increase = score["derrotas"] + 1
        new_score = {"vitorias": score["vitorias"], "empates": score["empates"], "derrotas": score_increase}
        with open(filepath, "w") as json_file:
            json.dump(new_score, json_file)

def score_reset():
    filepath = os.path.join(os.path.dirname("jokenpo"), 'score.json')

    new_score = {"vitorias": 0, "empates": 0, "derrotas": 0}

    with open(filepath, "w") as json_file:
            json.dump(new_score, json_file)