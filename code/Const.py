import pygame

# Constantes Game
# C
COLOR_ORANGE = (255, 255, 255)
COLOR_WHITE = (0, 139, 139)
COLOR_RED = (255, 0, 0)
COUNTDOWN_TIME = 60  # Tempo de contagem regressiva em segundos
COUNTDOWN_OPTIONS = (60, 120, -1)  # -1 representa ilimitado

# Controles do jogo
CONTROLS_P1 = [
    "^ - Mover para cima",
    "v - Mover para baixo",
    "< - Mover para esquerda",
    "> - Mover para direita",
    "ESPAÇO - Atirar"
]

CONTROLS_P2 = [
    "W - Mover para cima",
    "S - Mover para baixo",
    "A - Mover para esquerda",
    "D - Mover para direita",
    "G - Atirar"
]

GENERAL_CONTROLS = [
    "P - Pausar/Despausar jogo",
    "ESC - Pausar jogo ou voltar ao menu",
    "ENTER - Confirmar seleção",
    "^v - Navegar nos menus",
    "<> - Ajustar volume/FPS nas opções"
]

# E
ENTITY_SPEED = {
    'Level1bg0': 1,
    'Level1bg1': 2,
    'Level1bg2': 3,
    'Level1bg3': 4,
    'Level1bg4': 5,
    'Level2bg0': 1,  # Velocidade do background do menu
    'Player1': 5,
    'Player1Shot': 8,
    'Player2': 5,
    'Player2Shot': 7,
    'Enemy1': 3,
    'Enemy1Shot': 5,
    'Enemy2': 2,
    'Enemy2Shot': 4,
    'Meteor': 4,  # Velocidade do meteoro
    'Meteor2': 3,  # Velocidade do segundo meteoro (um pouco mais lento)
}

ENTITY_SHOT_DELAY = {
    'Player1': 15,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 120,
    # Meteor não tem shot delay pois não atira
}

ENTITY_VIDA = {
    'Level1bg0': 9999,
    'Level1bg1': 9999,
    'Level1bg2': 9999,
    'Level1bg3': 9999,
    'Level1bg4': 9999,
    'Level2bg0': 9999,  # Vida do background do menu
    'Player1': 200,
    'Player1Shot':1,
    'Player2': 200,
    'Player2Shot':1,
    'Enemy1': 100,
    'Enemy1Shot': 1,
    'Enemy2': 100,
    'Enemy2Shot': 1,
    'Meteor': 150,  # Vida do meteoro
    'Meteor2': 200,  # Vida do segundo meteoro (mais resistente)
}




EVENT_ENEMY = pygame.USEREVENT + 1  # Evento personalizado para gerar inimigos
EVENT_METEOR = pygame.USEREVENT + 2  # Evento personalizado para gerar meteoros

# F

FPS_GAME = (60, 90)  # 90 FPS como padrão (índice 1)
MENU_FPS = 30  # FPS específico para o menu

# M
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "SCORE",
               "OPÇÕES",
               "EXIT")

# O
OPTIONS_GAME = ("VOLUME",
                "CONTROLES",
                "TAXA DE QUADROS",
                "TEMPO DE JOGO",
                "RETORNAR")

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_g}

PLAYER_SHOOT_DAMAGE ={
    'Player': 50,
}
# s
SPAWN_TIME = 1000

# w
ALTURA_JANELA = 800
LARGURA_JANELA = 800
