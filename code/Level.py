import random
import sys
import pygame
from pygame.rect import Rect
from pygame.surface import Surface
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import COLOR_WHITE, COLOR_ORANGE, FPS_GAME, MENU_OPTION, EVENT_ENEMY, EVENT_METEOR, SPAWN_TIME, COLOR_RED, COUNTDOWN_OPTIONS
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode, fps_index=1, countdown_index=0):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.fps_index = fps_index  # Índice do FPS selecionado (0 = 60 FPS, 1 = 90 FPS) - Padrão: 90 FPS
        self.countdown_index = countdown_index  # Índice do tempo de jogo selecionado
        self.countdown_time = COUNTDOWN_OPTIONS[countdown_index]  # Tempo de jogo baseado na configuração
        self.entity_list: list[Entity] = []  # lista de entidades no nível
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))  # adiciona entidades ao nível
        self.entity_list.append(EntityFactory.get_entity('Player1'))  # adiciona o jogador ao nível
        self.paused = False  # adiciona um estado para controlar a pausa
        self.timeout = 150000  # tempo limite do nível em milissegundos
        if game_mode in [MENU_OPTION[1]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # define um evento para gerar inimigos a cada 2 segundos
        pygame.time.set_timer(EVENT_METEOR, 5000)  # define um evento para gerar meteoros a cada 5 segundos
        self.score_player1 = 0  # Score separado para Player 1
        self.score_player2 = 0  # Score separado para Player 2


        # Relógio de contagem regressiva
        self.start_time = pygame.time.get_ticks()  # Tempo inicial em milissegundos

    def pause_menu(self):
        overlay = pygame.Surface(self.window.get_size())
        overlay.set_alpha(128)  # define a transparência (0-255)
        self.window.blit(overlay, (0, 0))

        # Desenha o texto "PAUSADO"
        font = pygame.font.SysFont(None, 80)
        pause_text = font.render("PAUSADO", True, COLOR_WHITE)
        text_rect = pause_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 - 50))
        self.window.blit(pause_text, text_rect)

        # Desenha as instruções
        font_small = pygame.font.SysFont(None, 40)
        continue_text = font_small.render("Pressione P para continuar", True, COLOR_ORANGE)
        exit_text = font_small.render("Pressione ESC para sair", True, COLOR_ORANGE)

        continue_rect = continue_text.get_rect(
            center=(self.window.get_width() // 2, self.window.get_height() // 2 + 30))
        exit_rect = exit_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 + 80))

        self.window.blit(continue_text, continue_rect)
        self.window.blit(exit_text, exit_rect)

    def pause_musica(self):
        self.paused = not self.paused
        # Pausa ou retoma a música dependendo do pause do jogo
        if self.paused:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def run(self, ):
        clock = pygame.time.Clock()  # para controlar a taxa de quadros

        while True:
            # Limita a taxa de quadros usando o FPS selecionado
            clock.tick(FPS_GAME[self.fps_index])  # FPS do jogo baseado na seleção do usuário

            # Desenhar entidades
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                # CHAVE: Só move entidades quando não está pausado
                if not self.paused:
                    ent.move()
                    if isinstance(ent, (Player, Enemy)):
                        shoot = ent.shoot()  # Verifica se a entidade pode atirar
                        if shoot is not None:
                            self.entity_list.append(shoot)

            # Se o jogo estiver pausado, desenha o menu de pausa
            if self.paused:
                self.pause_menu()

            # imprimir o texto do nível
            self.level_text(20, f"{self.name}", COLOR_RED, (self.window.get_width() // 2 - 20, 10))
            self.level_text(20, f"FPS: {int(clock.get_fps())}", COLOR_RED, (self.window.get_width() - 180, 10))


            # Mostra a vida e score do Player1
            player1 = next((e for e in self.entity_list if isinstance(e, Player) and e.name == 'Player1'), None)
            vida_player1 = player1.health if player1 else 0
            self.level_text(20, f"PLAYER 1 - VIDA: {vida_player1} - SCORE: {self.score_player1}", COLOR_RED, (30, 30))

            # Mostra a vida e score do Player2, se existir
            player2 = next((e for e in self.entity_list if isinstance(e, Player) and e.name == 'Player2'), None)
            if player2:
                vida_player2 = player2.health
                self.level_text(20, f"PLAYER 2 - VIDA: {vida_player2} - SCORE: {self.score_player2}", COLOR_RED, (30, 50))

            # Cálculo e exibição do tempo restante
            if not self.paused:
                # Se o tempo for ilimitado (-1), não mostra countdown
                if self.countdown_time == -1:
                    self.level_text(20, f"Tempo: Ilimitado", COLOR_RED, (30, 10))
                else:
                    # Calcula o tempo decorrido
                    elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000  # em segundos
                    # Calcula o tempo restante
                    remaining_time = self.countdown_time - elapsed_time

                    if remaining_time <= 0:
                        remaining_time = 0
                        # Quando o tempo acaba, capturar nomes dos jogadores ANTES do game over
                        # APENAS se não for modo ilimitado
                        player_names = {}

                        # Só capturar nomes se não for modo ilimitado (countdown_index != 2)
                        if self.countdown_index != 2:
                            # Capturar nome do Player 1 se ele tem score > 0
                            if self.score_player1 > 0:
                                player_names['Player1'] = Player.get_player_name(self.window, self.entity_list, 1)

                            # Capturar nome do Player 2 se existe e tem score > 0
                            if player2 and self.score_player2 > 0:
                                player_names['Player2'] = Player.get_player_name(self.window, self.entity_list, 2)

                        # AGORA mostrar game over e retornar
                        self.game_over(reason="timeout")
                        final_scores = {'Player1': self.score_player1, 'Player2': self.score_player2}
                        final_names = player_names
                        return "game_over", final_scores, final_names

                    # Exibe o tempo restante
                    self.level_text(20, f"Tempo Restante: {remaining_time} seg", COLOR_RED, (30, 10))

            pygame.display.flip()

            #Só verifica colisões e saúde quando não está pausado
            if not self.paused:
                # Verifica colisões e recebe o número de inimigos destruídos por tiros de cada jogador
                enemies_destroyed_by_shots = EntityMediator.verify_collision(entity_list=self.entity_list)
                EntityMediator.verify_health(entity_list=self.entity_list, game_mode=self.game_mode)

                # Incrementa o score de cada jogador separadamente
                self.score_player1 += enemies_destroyed_by_shots['Player1']
                self.score_player2 += enemies_destroyed_by_shots['Player2']

            # Verifica se algum jogador morreu para exibir Game Over
            jogadores = [e for e in self.entity_list if isinstance(e, Player)]  # Lista de jogadores

            # Lógica diferente para single player vs cooperativo
            game_over_condition = False

            if self.game_mode == MENU_OPTION[1]:  # Modo cooperativo (2 players)
                # No modo cooperativo, jogo termina apenas quando AMBOS os jogadores morrem
                game_over_condition = all(jogador.health <= 0 for jogador in jogadores)
            else:  # Modo single player
                # No modo single player, jogo termina quando o único jogador morre
                game_over_condition = any(jogador.health <= 0 for jogador in jogadores)

            if game_over_condition:
                # Capturar nomes dos jogadores antes do game over por morte
                # APENAS se não for modo ilimitado
                player_names = {}

                # Só capturar nomes se não for modo ilimitado (countdown_index != 2)
                if self.countdown_index != 2:
                    # Capturar nome do Player 1 se ele tem score > 0
                    if self.score_player1 > 0:
                        player_names['Player1'] = Player.get_player_name(self.window, self.entity_list, 1)

                    # Capturar nome do Player 2 se existe e tem score > 0
                    if player2 and self.score_player2 > 0:
                        player_names['Player2'] = Player.get_player_name(self.window, self.entity_list, 2)

                self.game_over()
                final_scores = {'Player1': self.score_player1, 'Player2': self.score_player2}
                final_names = player_names
                return "game_over", final_scores, final_names

            # Gerencia os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # IMPORTANTE: Só gera inimigos quando não está pausado
                if event.type == EVENT_ENEMY and not self.paused:  # Evento para gerar inimigos
                    choice = random.choice(('Enemy1', 'Enemy2'))  # Escolhe um inimigo aleatório
                    self.entity_list.append(EntityFactory.get_entity(choice))

                # Só gera meteoros quando não está pausado
                if event.type == EVENT_METEOR and not self.paused:  # Evento para gerar meteoros
                    meteor_choice = random.choice(('Meteor', 'Meteor2'))  # Escolhe um meteoro aleatório
                    self.entity_list.append(EntityFactory.get_entity(meteor_choice))  # Spawna um meteoro

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Tecla P para pausar/despausar
                        self.pause_musica()
                    elif event.key == pygame.K_ESCAPE:  # Tecla ESC para sair do nível
                        if self.paused:
                            # Se estiver pausado, ESC sai do nível
                            return "menu", None, None
                        else:
                            # Se não estiver pausado, ESC pausa o jogo
                            self.pause_musica()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(None, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_center_pos[0], top=text_center_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def game_over(self, reason="death"):
        overlay = pygame.Surface(self.window.get_size())
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.window.blit(overlay, (0, 0))
        font = pygame.font.SysFont(None, 100)

        if reason == "timeout":
            text = font.render("TEMPO ACABOU!", True, COLOR_ORANGE)
            text_rect = text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 - 80))
            self.window.blit(text, text_rect)

            # Verifica se é modo cooperativo (2 players)
            if self.game_mode == MENU_OPTION[1]:  # "NEW GAME 2P - COOPERATIVE"
                # Mostra pontuação individual de cada jogador
                font_score = pygame.font.SysFont(None, 50)

                # Player 1 Score
                score_text1 = font_score.render(f"Player 1 Score: {self.score_player1}", True, COLOR_WHITE)
                score_rect1 = score_text1.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 - 20))
                self.window.blit(score_text1, score_rect1)

                # Player 2 Score
                score_text2 = font_score.render(f"Player 2 Score: {self.score_player2}", True, COLOR_WHITE)
                score_rect2 = score_text2.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 + 20))
                self.window.blit(score_text2, score_rect2)

                # Score Total
                total_score = self.score_player1 + self.score_player2
                total_text = font_score.render(f"Score Total: {total_score}", True, COLOR_ORANGE)
                total_rect = total_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 + 60))
                self.window.blit(total_text, total_rect)

            # Modo single player - mostra apenas o score do Player 1
            if self.game_mode != MENU_OPTION[1]:
                font_score = pygame.font.SysFont(None, 60)
                score_text = font_score.render(f"Sua pontuação foi: {self.score_player1}", True, COLOR_WHITE)
                score_rect = score_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 + 20))
                self.window.blit(score_text, score_rect)
        else:
            # Game over por morte
            text = font.render("GAME OVER", True, COLOR_ORANGE)
            text_rect = text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))
            self.window.blit(text, text_rect)

        pygame.display.flip()
        pygame.time.wait(3000)

        # CORREÇÃO: Limpar todos os eventos acumulados durante o wait
        pygame.event.clear()

        # CORREÇÃO: Aguardar até que todas as teclas sejam liberadas
        while any(pygame.key.get_pressed()):
            pygame.event.pump()  # Processa eventos sem consumi-los
            pygame.time.wait(50)  # Pequena pausa para não sobrecarregar o CPU

        # CORREÇÃO: Limpar eventos mais uma vez após liberação das teclas
        pygame.event.clear()
