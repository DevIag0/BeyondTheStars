import random
import sys
import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import COLOR_WHITE, COLOR_ORANGE, FPS_GAME, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COLOR_RED
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode, fps_index=1):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.fps_index = fps_index  # Índice do FPS selecionado (0 = 60 FPS, 1 = 90 FPS) - Padrão: 90 FPS
        self.entity_list: list[Entity] = []  # lista de entidades no nível
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))  # adiciona entidades ao nível
        self.entity_list.append(EntityFactory.get_entity('Player1'))  # adiciona o jogador ao nível
        self.paused = False  # adiciona um estado para controlar a pausa
        self.timeout = 150000  # tempo limite do nível em milissegundos
        if game_mode in [MENU_OPTION[1]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # define um evento para gerar inimigos a cada 2 segundos
        self.score = 0  # Inicializa o score

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
            self.level_text(20, f"SOBREVIVA: {self.timeout // 1000} segundos", COLOR_RED, (30, 10))
            self.level_text(20, f"{self.name}", COLOR_RED, (self.window.get_width() // 2 - 20, 10))
            self.level_text(20, f"FPS: {int(clock.get_fps())}", COLOR_RED, (self.window.get_width() - 180, 10))
            self.level_text(20, f"SCORE: {self.score}", COLOR_ORANGE, (self.window.get_width() - 100, 10))
            self.level_text(20, f"Entidades: {len(self.entity_list) - 9}", COLOR_RED, (self.window.get_width() - 300, 10))
            # Mostra a pontuação do jogador

            # Mostra a vida do player atual (Player1)
            player1 = next((e for e in self.entity_list if isinstance(e, Player) and e.name == 'Player1'), None)
            vida_player1 = player1.health if player1 else 0
            self.level_text(20, f"PLAYER 1 - VIDA: {vida_player1}", COLOR_RED, (30, 30))

            # Mostra a vida do Player2, se existir
            player2 = next((e for e in self.entity_list if isinstance(e, Player) and e.name == 'Player2'), None)
            if player2:
                vida_player2 = player2.health
                self.level_text(20, f"PLAYER 2 - VIDA: {vida_player2}", COLOR_RED, (30, 50))

            pygame.display.flip()

            #Só verifica colisões e saúde quando não está pausado
            if not self.paused:
                # Verifica colisões e recebe o número de inimigos destruídos por tiros
                enemies_destroyed_by_shots = EntityMediator.verify_collision(entity_list=self.entity_list)
                EntityMediator.verify_health(entity_list=self.entity_list)

                # Incrementa o score apenas com inimigos destruídos por tiros
                self.score += enemies_destroyed_by_shots

            # Verifica se algum jogador morreu para exibir Game Over
            jogadores = [e for e in self.entity_list if isinstance(e, Player)]  # Lista de jogadores
            if any(jogador.health <= 0 for jogador in jogadores):
                self.game_over()
                return "menu"

            # Gerencia os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # IMPORTANTE: Só gera inimigos quando não está pausado
                if event.type == EVENT_ENEMY and not self.paused:  # Evento para gerar inimigos
                    choice = random.choice(('Enemy1', 'Enemy2'))  # Escolhe um inimigo aleatório
                    self.entity_list.append(EntityFactory.get_entity(choice))

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Tecla P para pausar/despausar
                        self.pause_musica()
                    elif event.key == pygame.K_ESCAPE:  # Tecla ESC para sair do nível
                        if self.paused:
                            # Se estiver pausado, ESC sai do nível
                            return "menu"
                        else:
                            # Se não estiver pausado, ESC pausa o jogo
                            self.pause_musica()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(None, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_center_pos[0], top=text_center_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def game_over(self):
        overlay = pygame.Surface(self.window.get_size())
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.window.blit(overlay, (0, 0))
        font = pygame.font.SysFont(None, 100)
        text = font.render("GAME OVER", True, COLOR_ORANGE)
        text_rect = text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))
        self.window.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
