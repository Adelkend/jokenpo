from cgitb import text
import pygame
from pygame.locals import *

pygame.init()

font = pygame.font.Font("fonts\\KellySlab-Regular.ttf", 72)

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

class generate_window():
    def __init__(self):
        self.size = width, height = 1920, 1080
        self.window_title = "Jokenpo"
        pygame.display.set_caption(self.window_title)
        self.screen = pygame.display.set_mode(self.size)
        self.font = font

def drawText(screen, t, x, y                                   , size, color):
    font = pygame.font.Font("fonts\\KellySlab-Regular.ttf", size)
    text = font.render(t, True, color)
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x, y)
    screen.blit(text, text_rectangle)

class choice_button(pygame.sprite.Sprite):
    def __init__(self, pos, text, size, window):
        super().__init__()
        self.font  = pygame.font.Font("fonts\\KellySlab-Regular.ttf", size)
        self.text = text
        self.text_surf = self.font.render(text, True, colors["white"])
        self.image = pygame.Surface((self.text_surf.get_width()+40,
                                self.text_surf.get_height()+20), pygame.SRCALPHA, 32)
        self.image.blit(self.text_surf, (20, 10))
        self.rect = self.image.get_rect(topleft=pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return self.text