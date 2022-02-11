from cgitb import text
import pygame
from pygame.locals import *

pygame.init()

font = pygame.font.Font("fonts\\KellySlab-Regular.ttf", 72)

colors  =   {"red": (255, 0, 0),
            "green": (0, 255, 0),
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "grey": (61, 59, 52),
            "bright_red": (155, 0, 56),
            "purple" : (205, 48, 238),
            "green" : (175, 251, 205)
            }

class generate_window():
    def __init__(self):
        self.size = width, height = 1920, 1080
        self.window_title = "Jokenpo!"
        pygame.display.set_caption(self.window_title)
        self.screen = pygame.display.set_mode(self.size)
        self.font = font

def drawText(screen, t, x, y, size, color):
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
        self.image = pygame.Surface((self.text_surf.get_width()+20,
                                self.text_surf.get_height()+10), pygame.SRCALPHA, 32)
        self.image.blit(self.text_surf, (20, 10))
        self.rect = self.image.get_rect(topleft=pos)

    def handle_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.text_surf = self.font.render(self.text, True, colors["green"])
            self.image.blit(self.text_surf, (20, 10))
            pygame.display.update()

        if not self.rect.collidepoint(pygame.mouse.get_pos()):
            self.text_surf = self.font.render(self.text, True, colors["white"])
            self.image.blit(self.text_surf, (20, 10))
            pygame.display.update()    

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return self.text

class Animation():
    def __init__(self, imageList):
        self.imageList = imageList
        self.imageIndex = 0
        self.animationTimer = 0
        self.animationSpeed = 10

    def update(self):
        self.animationTimer += 1
        if self.animationTimer >= self.animationSpeed:
            self.animationTimer = 0
            self.imageIndex += 1
            if self.imageIndex > len(self.imageList) - 1:
                self.imageIndex = 0

    def draw(self, screen, x, y):
        image = self.imageList[self.imageIndex]
        screen.blit(image, (x, y))