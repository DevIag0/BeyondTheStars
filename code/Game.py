import sys
import pygame
from code.Menu import Menu
from code.Const import ALTURA_JANELA, LARGURA_JANELA, MENU_OPTION
from code.Level import Level
from code.Opcoes import Opcoes
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()  # inicializar o pygame
        self.window = pygame.display.set_mode(size=(ALTURA_JANELA, LARGURA_JANELA))  # cria a janela do jogo
        pygame.display.set_caption("Beyond the Stars")  # define nome na janela
        self.volume = 0.2  # volume global
        self.fps_index = 1  # FPS global (0 = 60 FPS, 1 = 90 FPS) - Padrão: 90 FPS
        self.countdown_index = 0  # Tempo de jogo global (0 = 60s, 1 = 120s, 2 = ilimitado) - Padrão: 60s
        self.score_system = Score(self.window)  # Sistema de pontuação

    def run(self):
        # loop principal do jogo
        while True:

            # criar o menu
            menu = Menu(self.window, self.volume)  # Passa backgrounds para o Menu
            menu_return, self.volume = menu.run()  # recebe também o volume atualizado

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                # se a opção selecionada for "NEW GAME 1P" ou "NEW GAME 2P - COOPERATIVE"
                level = Level(self.window, "Level1", menu_return, self.fps_index, self.countdown_index)
                level_result = level.run()  # Recebe o resultado do level

                # Verifica se o level retornou 3 valores (incluindo nomes) ou 2 valores (sem nomes)
                if len(level_result) == 3:
                    level_return, final_scores, final_names = level_result
                else:
                    level_return, final_scores = level_result
                    final_names = {}

                # Salvar scores no banco de dados se o jogo terminou
                if level_return == "game_over" and final_scores:
                    # Determinar o modo de jogo baseado no countdown_index
                    if self.countdown_index == 0:  # 60 segundos
                        game_mode = '60_seconds'
                    elif self.countdown_index == 1:  # 120 segundos
                        game_mode = '120_seconds'
                    else:  # Tempo ilimitado - não salvar no banco
                        game_mode = None

                    # Só salvar se não for modo ilimitado
                    if game_mode:
                        # Salvar score do Player 1 com nome personalizado
                        if final_scores.get('Player1', 0) > 0:
                            player1_name = final_names.get('Player1', 'Player 1')
                            self.score_system.save_score(player1_name, final_scores['Player1'], game_mode)

                        # Salvar score do Player 2 com nome personalizado se existir
                        if final_scores.get('Player2', 0) > 0:
                            player2_name = final_names.get('Player2', 'Player 2')
                            self.score_system.save_score(player2_name, final_scores['Player2'], game_mode)

                # retorna ao menu se o jogo for pausado ou finalizado
                if level_return in ["menu", "game_over"]:
                    continue

            elif menu_return == MENU_OPTION[2]:  # se a opção selecionada for "SCORE"
                self.score_system.run()

            elif menu_return == MENU_OPTION[3]:   # se a opção selecionada for "OPÇÕES"
                options_game = Opcoes(self.window, self.volume, self.fps_index, self.countdown_index)
                self.volume, self.fps_index, self.countdown_index = options_game.run()  # atualiza volume, FPS e tempo global

            elif menu_return == MENU_OPTION[4]:  # se a opção selecionada for "EXIT"
                pygame.quit()  # fechar o pygame
                sys.exit()  # sair do programa