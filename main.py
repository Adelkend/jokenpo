import pygame
from random import choice
import utils
import engine
import menu
import sys

pygame.init()

# ------------ VARIABLES --------------

yellow = 186, 149, 13
grey = 61, 59, 52

# ------------ SETUP -----------------

window = utils.generate_window()
running = True

# Lista das jogadas válidas
play = ["pedra", "papel", "tesoura"]

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
        window.screen.fill(grey)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ----- GAME SYSTEM AND LOGS -----

        h = engine.combat()
        utils.drawText(window.screen, f"Você escolheu {h}", 100, 100)
        
        c = choice(play)

        utils.drawText(window.screen, f"  O computador jogou {c}", 300, 200)
        utils.drawText(window.screen, text[rule[play.index(h)][play.index(c)]], 250, 500)

    # ----- UPDATE -----

    pygame.display.flip()

    pygame.time.delay(2500)

    popUp = engine.play_again(window)

    again = engine.play_again.choose(popUp.window)

    if again == "SIM": 
        running = True

    else:
        running = False

# ----------- QUIT --------------

pygame.quit()
sys.exit()