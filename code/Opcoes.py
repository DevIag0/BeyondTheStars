import sys

import pygame
from code.Const import COLOR_WHITE, OPTIONS_GAME, COLOR_ORANGE, FPS_GAME, CONTROLS_P1, CONTROLS_P2, GENERAL_CONTROLS, MENU_FPS, COUNTDOWN_OPTIONS
from code.Menu import Menu
from code.Background import Background


class Opcoes(Menu):
    def __init__(self, window, volume=0.5, fps_index=1, countdown_index=0):
        super().__init__(window, volume)
        self.volume = volume
        self.fps_index = fps_index  # 0 = 60 FPS, 1 = 90 FPS - Padrão: 90 FPS
        self.countdown_index = countdown_index  # 0 = 60s, 1 = 120s, 2 = ilimitado
        self.selected_option = 0
        self.clock = pygame.time.Clock()

        # Criar múltiplas camadas de background para efeito parallax
        self.backgrounds = []

        # Camada de fundo (Level2bg0)
        for i in range(2):
            bg = Background('Level2bg0', (0, -i * 800))
            self.backgrounds.append(bg)

        # Camadas intermediárias (Level1bg1, Level1bg2, Level1bg3) - velocidades crescentes
        bg_layers = ['Level1bg1', 'Level1bg2', 'Level1bg3']
        for layer in bg_layers:
            for i in range(2):
                bg = Background(layer, (0, -i * 800))
                self.backgrounds.append(bg)

    def show_controls(self):
        """Exibe a listagem de todos os comandos do jogo"""
        while True:
            # Atualizar e desenhar backgrounds com efeito parallax
            for bg in self.backgrounds:
                bg.move()
                self.window.blit(bg.surf, bg.rect)

            # Título
            self.menu_text(text_size=50, text="CONTROLES DO JOGO", text_color=COLOR_WHITE,
                           text_center_pos=(self.window.get_width() // 2, 80))

            # Controles Player 1
            self.menu_text(text_size=35, text="PLAYER 1:", text_color=COLOR_ORANGE,
                           text_center_pos=(200, 150))

            for i, control in enumerate(CONTROLS_P1):
                self.menu_text(text_size=25, text=control, text_color=COLOR_WHITE,
                               text_center_pos=(200, 190 + i * 30))

            # Controles Player 2
            self.menu_text(text_size=35, text="PLAYER 2:", text_color=COLOR_ORANGE,
                           text_center_pos=(600, 150))

            for i, control in enumerate(CONTROLS_P2):
                self.menu_text(text_size=25, text=control, text_color=COLOR_WHITE,
                               text_center_pos=(600, 190 + i * 30))

            # Controles Gerais
            self.menu_text(text_size=35, text="CONTROLES GERAIS:", text_color=COLOR_ORANGE,
                           text_center_pos=(self.window.get_width() // 2, 380))

            for i, control in enumerate(GENERAL_CONTROLS):
                self.menu_text(text_size=25, text=control, text_color=COLOR_WHITE,
                               text_center_pos=(self.window.get_width() // 2, 420 + i * 30))

            # Instruções
            self.menu_text(text_size=30, text="Pressione qualquer tecla para voltar", text_color=COLOR_ORANGE,
                           text_center_pos=(self.window.get_width() // 2, 650))

            pygame.display.flip()
            self.clock.tick(MENU_FPS)  # Limitar FPS do menu a 30

            # Aguardar tecla para voltar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    return

    def run(self):
        while True:
            # Atualizar e desenhar backgrounds com efeito parallax
            for bg in self.backgrounds:
                bg.move()
                self.window.blit(bg.surf, bg.rect)

            self.menu_text(text_size=60, text="OPÇÕES", text_color=COLOR_WHITE,
                           text_center_pos=(self.window.get_width() // 2, 260))

            # Desenha as opções do menu de opções
            for index, option in enumerate(OPTIONS_GAME):
                color = COLOR_WHITE if index == self.selected_option else COLOR_ORANGE
                self.menu_text(text_size=40, text=option, text_color=color,
                               text_center_pos=(self.window.get_width() // 2, 330 + index * 50))

            # Exibe o volume se a opção selecionada para volume estiver ativa
            if self.selected_option == 0:
                font = pygame.font.SysFont(None, 40)
                text = font.render(f"Volume: {self.volume:.1f}", True, COLOR_WHITE)
                self.window.blit(text, (self.window.get_width() // 2 - text.get_width() // 2, 570))

            # Exibe o FPS se a opção selecionada para taxa de quadros estiver ativa
            if self.selected_option == 2:
                font = pygame.font.SysFont(None, 40)
                text = font.render(f"FPS: {FPS_GAME[self.fps_index]}", True, COLOR_WHITE)
                self.window.blit(text, (self.window.get_width() // 2 - text.get_width() // 2, 570))

            # Exibe o TEMPO DE JOGO se a opção selecionada estiver ativa
            if self.selected_option == 3:
                font = pygame.font.SysFont(None, 40)
                if COUNTDOWN_OPTIONS[self.countdown_index] == -1:
                    text = font.render("Tempo: Ilimitado", True, COLOR_WHITE)
                else:
                    text = font.render(f"Tempo: {COUNTDOWN_OPTIONS[self.countdown_index]}s", True, COLOR_WHITE)
                self.window.blit(text, (self.window.get_width() // 2 - text.get_width() // 2, 570))

            pygame.display.flip()
            self.clock.tick(MENU_FPS)  # Limitar FPS do menu a 30

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return self.volume, self.fps_index, self.countdown_index  # retorna volume, fps e countdown ao apertar ESC
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(OPTIONS_GAME)
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(OPTIONS_GAME)
                    if self.selected_option == 0:  # Se volume estiver selecionado
                        if event.key == pygame.K_RIGHT:
                            self.volume = min(self.volume + 0.1, 1.0)
                            pygame.mixer.music.set_volume(self.volume)
                        if event.key == pygame.K_LEFT:
                            self.volume = max(self.volume - 0.1, 0.0)
                            pygame.mixer.music.set_volume(self.volume)
                    if self.selected_option == 1:  # Se CONTROLES estiver selecionado
                        if event.key == pygame.K_RETURN:
                            # Mostrar tela de controles
                            self.show_controls()
                    if self.selected_option == 2:  # Se FPS estiver selecionado
                        if event.key == pygame.K_RIGHT:
                            self.fps_index = (self.fps_index + 1) % len(FPS_GAME)
                        if event.key == pygame.K_LEFT:
                            self.fps_index = (self.fps_index - 1) % len(FPS_GAME)
                    if self.selected_option == 3:  # Se TEMPO DE JOGO estiver selecionado
                        if event.key == pygame.K_RIGHT:
                            self.countdown_index = (self.countdown_index + 1) % len(COUNTDOWN_OPTIONS)
                        if event.key == pygame.K_LEFT:
                            self.countdown_index = (self.countdown_index - 1) % len(COUNTDOWN_OPTIONS)
                    if self.selected_option == 4:  # Se a opção selecionada for "RETORNAR"
                        if event.key == pygame.K_RETURN:
                            return self.volume, self.fps_index, self.countdown_index
