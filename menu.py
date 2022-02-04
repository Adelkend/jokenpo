import pygame
import engine
from pygame import time
import utils

pygame.init()

size = width, height = 1920, 1080

class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode(size)
        wallpaper = pygame.image.load("graphics\\fundo_temp.jpg")
        self.background = self.screen.blit(wallpaper, (100, 100))
        self.rect = self.screen.get_rect()
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.menu_open = True
        self.colors = {"red": (255, 0, 0),
                       "green": (0, 255, 0),
                       "blue": (0, 0, 255),
                       "white": (255, 255, 255),
                       "black": (0, 0, 0),
                       "brown": (153, 76, 0),
                       "grey": (100, 100, 100),
                       "gold": (255, 215, 0),
                       "bright_red": (155, 0, 56),
                       "bright_gold": (255, 255, 0)}

    def setup(self):
        self.screen.fill(self.colors["black"])
        pygame.display.set_caption("Jokenpo")
        wallpaper = pygame.image.load("graphics\\fundo_temp.jpg")
        self.background = self.screen.blit(wallpaper, (0, 0))
        text = self.font.render("Choose your destiny", True,
                                (self.colors["white"]))
        text_rect = text.get_rect(center=(self.rect.w/2, self.rect.h/2))
        self.screen.blit(text, text_rect)

    def exit(self):
        self.screen.fill(self.colors["black"])
        text = self.font.render("Bom jogo, até a próxima!", True,
                                (self.colors["white"]))
        text_rect = text.get_rect(center=(self.rect.w/2, self.rect.h/2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.quit()

    def jogar(self):
        engine.window.scene = "game"
        self.menu_open = False

class Button(pygame.sprite.Sprite):
    def __init__(self,pos, text,window, callback):
        super().__init__()
        self.font = pygame.font.SysFont("app850.fon", 20)
        self.text_surf = window.font.render(text, True, window.colors["brown"])
        self.image = pygame.Surface((self.text_surf.get_width()+40,
                                self.text_surf.get_height()+20))
        self.image.fill(window.colors["gold"])
        self.image.blit(self.text_surf, (20, 10))
        self.rect = self.image.get_rect(topleft=pos)
        self.callback = callback

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

def game_intro(action):
    display_width, display_height = size
    window = Menu()
    window.setup()
    black = (0,0,0)
    white = (255,255,255)
    red=(129,0,56)
    wall = (201,198,206)
    clock = pygame.time.Clock()
    gui = pygame.sprite.Group()

    start_game = Button(pos=(display_width * 0.20, display_height * 0.7),text= "START",window=window, callback=window.jogar)
    quit_game = Button(pos=(display_width * 0.55, display_height * 0.7),text= "QUIT",window=window, callback=window.exit)

    gui.add(start_game, quit_game)

    #Button Colors
    btn=(100,149,237)
    gold=(255,215,0)
    #Hoover colors
    bright_red=(155,0,56)
    bright_gold=(255,255,0)

    while window.menu_open == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Menu.exit()

            for button in gui:
                button.handle_event(event)

        gui.update()
        #pygame.display.set_mode((display_width, display_height)).fill(black)
        gui.draw(window.screen)
        #largeText = pygame.font.SysFont('app850.fon', 80)
        #TextSurf, TextRect = text_objects("Dragons & Dungeons", largeText, white)
        #TextRect.center = ((display_width * 0.5, display_height / 2))
        #gameDisplay.blit(TextSurf, TextRect)
        pygame.display.flip()
        clock.tick(30)