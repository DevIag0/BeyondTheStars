import sys

import pygame
from code.Menu import Menu
from code.Const import ALTURA_JANELA, LARGURA_JANELA, MENU_OPTION
from code.Level import Level
from code.Opcoes import Opcoes

class Game:
    def __init__(self):
        pygame.init()  # inicializar o pygame
        self.window = pygame.display.set_mode(size=(ALTURA_JANELA, LARGURA_JANELA))  # cria a janela do jogo
        pygame.display.set_caption("Beyond the Stars")  # define nome na janela
        self.volume = 0.2  # volume global
        self.fps_index = 1  # FPS global (0 = 60 FPS, 1 = 90 FPS) - Padrão: 90 FPS

    def run(self):
        # loop principal do jogo
        while True:

            # criar o menu
            menu = Menu(self.window, self.volume)  # Passa backgrounds para o Menu
            menu_return, self.volume = menu.run()  # recebe também o volume atualizado

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                # se a opção selecionada for "NEW GAME 1P", "NEW GAME 2P - COOPERATIVE" ou "PLAYER VS PLAYER"
                level = Level(self.window, "Level1", menu_return, self.fps_index)
                level_return = level.run()

                # retorna ao menu se o jogo for pausado ou finalizado
                if level_return == "menu":
                    continue

            elif menu_return == MENU_OPTION[3]:  # se a opção selecionada for "SCORE"
                print("Exibir pontuação")

            elif menu_return == MENU_OPTION[4]:   # se a opção selecionada for "OPÇÕES"
                options_game = Opcoes(self.window, self.volume, self.fps_index)
                self.volume, self.fps_index = options_game.run()  # atualiza o volume e FPS global


            elif menu_return == MENU_OPTION[5]:  # se a opção selecionada for "EXIT"
                pygame.quit()  # fechar o pygame
                sys.exit()  # sair do programa