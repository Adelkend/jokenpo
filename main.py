import pygame
from random import choice
import utils
import json
import engine
import menu
import sys
import os

pygame.init()

# ------------ VARIABLES --------------

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

# ------------ SETUP -----------------

window = utils.generate_window()
running = True

# Lista das jogadas válidas
play = ["rock", "paper", "scissors"]

# Matriz de decisão do resultado, contendo as regras do jogo
rule = (("e", "d", "v"), ("v", "e", "d"), ("d", "v", "e"))

# Texto a ser exibido na tela para cada resultado possível
text = {
    "e": "    Empatou!",
    "v": "    Parabéns, você venceu!",
    "d": "    Você foi derrotado!",
    }

# ------------ GAME LOOP --------------

while running:

    if engine.window.scene == "menu":
        menu.game_intro(utils.generate_window())

        pygame.display.update()

    if engine.window.scene == "game":

        window.screen.fill(colors["black"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ----- GAME SYSTEM AND LOGS -----

        h = engine.combat()
        utils.drawText(window.screen, f"Você escolheu {h}", 400, 400, 24, colors["white"])
        
        c = choice(play)

        result = rule[play.index(h)][play.index(c)]

        utils.drawText(window.screen, f"  O computador jogou {c}", 600, 500, 24, colors["white"])
        utils.drawText(window.screen, text[result], 550, 650, 24, colors["white"])

        engine.score_update(result)

    # ----- UPDATE -----

    pygame.display.flip()

    pygame.time.delay(2500)

    popUp = engine.play_again(window)

    again = engine.play_again.choose(popUp.window)

    if again == "SIM": 
        engine.window.scene = "game"

    else:
        engine.window.scene = "menu"

# ----------- QUIT --------------

pygame.quit()
sys.exit()