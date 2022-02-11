import pygame
import engine
import utils
import sys

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
        self.font = pygame.font.Font("fonts\\KellySlab-Regular.ttf", 24)
        self.menu_open = True
        self.colors  =   {"red": (255, 0, 0),
                        "green": (0, 255, 0),
                        "white": (255, 255, 255),
                        "black": (0, 0, 0),
                        "grey": (61, 59, 52),
                        "bright_red": (155, 0, 56),
                        "purple" : (205, 48, 238),
                        "green" : (175, 251, 205)
                        }

    def setup(self):
        self.screen.fill(self.colors["black"])
        pygame.display.set_caption("Jokenpo!")
        wallpaper = pygame.image.load("graphics\\fundo_temp.jpg")
        self.background = self.screen.blit(wallpaper, (0, 0))
        utils.drawText(self.screen, "Jokenpo!", 97, 55, 219, self.colors["white"])
        utils.drawText(self.screen, "Intergalactic Tournament", 97, 278, 44, self.colors["white"])

    def exit(self):
        self.screen.fill(self.colors["black"])
        text = self.font.render("Bom jogo, até a próxima!", True,
                                (self.colors["white"]))
        text_rect = text.get_rect(center=(self.rect.w/2, self.rect.h/2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.quit()
        sys.exit()

    def jogar(self):
        engine.window.scene = "game"
        self.menu_open = False

    def reset(self):
        engine.score_reset()
        engine.window.scene = "menu"
        self.menu_open = True

class Button(pygame.sprite.Sprite):
    def __init__(self,pos, text, window, callback):
        super().__init__()
        self.window = window
        self.text = text
        self.font = pygame.font.Font("fonts\\KellySlab-Regular.ttf", 72)
        self.text_surf = self.font.render(text, True, window.colors["white"])
        self.image = pygame.Surface((self.text_surf.get_width()+20,
                                self.text_surf.get_height()+8), pygame.SRCALPHA, 32)
        self.image.blit(self.text_surf, (20, 10))
        self.rect = self.image.get_rect(topleft=pos)
        self.callback = callback

    def handle_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.text_surf = self.font.render(self.text, True, self.window.colors["green"])
            self.image.blit(self.text_surf, (20, 10))
            pygame.display.flip()

        if not self.rect.collidepoint(pygame.mouse.get_pos()):
            self.text_surf = self.font.render(self.text, True, self.window.colors["white"])
            self.image.blit(self.text_surf, (20, 10))
            pygame.display.flip()

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

    start_game = Button(pos=(97, 646),text= "play",window=window, callback=window.jogar)
    reset_button = Button(pos=(97, 742),text= "reset score",window=window, callback=window.reset)
    quit_game = Button(pos=(97,838),text= "exit",window=window, callback=window.exit)
    
    gui.add(start_game, quit_game, reset_button)

    #Button Colors
    btn=(100,149,237)
    gold=(255,215,0)
    #Hoover colors
    bright_red=(155,0,56)
    bright_gold=(255,255,0)

    while window.menu_open == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window.exit()

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