import pygame
from random import choice
import utils
import engine
import menu

pygame.init()

# ------------ VARIABLES --------------

yellow = 186, 149, 13
gray = 61, 59, 52

# ------------ SETUP -----------------

screen = utils.generate_window()
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
        screen.fill(gray)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ----- GAME SYSTEM AND LOGS -----

        utils.drawText(screen, "Faça a sua jogada: ", 0, 0)

        pygame.display.update()

        h = engine.wait_for_command()
        utils.drawText(screen, f"Você escolheu {h}", 100, 100)
        
        c = choice(play)

        if h in play:
            utils.drawText(screen, f"  O computador jogou {c}", 300, 200)
            utils.drawText(screen, text[rule[play.index(h)][play.index(c)]], 250, 500)
        
        else:
            utils.drawText(screen, f"  As jogadas válidas são:\n {play}", 250,500)

    pygame.display.flip()

    pygame.time.delay(5000)

    engine.play_again()

# ----------- QUIT ------------------ 

pygame.quit()