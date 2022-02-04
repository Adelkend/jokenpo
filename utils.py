import pygame
from pygame.locals import *
pygame.init()

font = pygame.font.Font(pygame.font.get_default_font(), 24)

yellow = 186, 149, 13
gray = 61, 59, 52

def generate_window():
    size = width, height = 1920, 1080
    window_title = "Jokenpo"
    pygame.display.set_caption(window_title)
    screen = pygame.display.set_mode(size)

    return screen

def drawText(screen, t, x, y):
    text = font.render(t, True, yellow, gray)
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x, y)
    screen.blit(text, text_rectangle)
