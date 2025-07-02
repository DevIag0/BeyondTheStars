import pygame
# Constantes Game
# C
COLOR_ORANGE = (139,0,0)
COLOR_WHITE = (255, 255, 255)

#E
ENTITY_SPEED = {
    'Level1bg0': 1,
    'Level1bg1': 2,
    'Level1bg2': 3,
    'Level1bg3': 4,
    'Level1bg4': 5,
    'Player1': 5,
    'Player2': 5,
}

# F

FPS_GAME = (30, 60)


# M
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "PLAYER VS PLAYER",
               "SCORE",
               "OPÇÕES",
               "EXIT")

#O
OPTIONS_GAME = ("VOLUME",
                "DIFICULDADE",
                "TAXA DE QUADROS",
                "RETORNAR")

#P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                    'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                     'Player2': pygame.K_d}

# w
ALTURA_JANELA = 800
LARGURA_JANELA = 800
