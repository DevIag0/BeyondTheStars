import sys

import pygame
from code.Const import COLOR_WHITE, OPTIONS_GAME, COLOR_ORANGE, FPS_GAME, CONTROLS_P1, CONTROLS_P2, GENERAL_CONTROLS
from code.Menu import Menu


class Opcoes(Menu):
    def __init__(self, window, volume=0.5, fps_index=1):
        super().__init__(window, volume)
        self.volume = volume
        self.fps_index = fps_index  # 0 = 60 FPS, 1 = 90 FPS - Padrão: 90 FPS
        self.selected_option = 0
        # Carregar a imagem de fundo para o menu de opções
        self.surf = pygame.image.load("./asset/Level1bg0.png").convert()
        self.rect = self.surf.get_rect(left=0, top=0)

    def show_controls(self):
        """Exibe a listagem de todos os comandos do jogo"""
        # Limpar a tela
        self.window.blit(source=self.surf, dest=self.rect)

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

    def run(self):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
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
                self.window.blit(text, (self.window.get_width() // 2 - text.get_width() // 2, 520))

            # Exibe o FPS se a opção selecionada para taxa de quadros estiver ativa
            if self.selected_option == 2:
                font = pygame.font.SysFont(None, 40)
                text = font.render(f"FPS: {FPS_GAME[self.fps_index]}", True, COLOR_WHITE)
                self.window.blit(text, (self.window.get_width() // 2 - text.get_width() // 2, 520))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return self.volume, self.fps_index  # retorna o volume e fps ao apertar ESC
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
                            # Aguardar tecla para voltar
                            waiting = True
                            while waiting:
                                for control_event in pygame.event.get():
                                    if control_event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    if control_event.type == pygame.KEYDOWN:
                                        waiting = False
                                        break
                    if self.selected_option == 2:  # Se FPS estiver selecionado
                        if event.key == pygame.K_RIGHT:
                            self.fps_index = (self.fps_index + 1) % len(FPS_GAME)
                        if event.key == pygame.K_LEFT:
                            self.fps_index = (self.fps_index - 1) % len(FPS_GAME)
                    if self.selected_option == 3:  # Se a opção selecionada for "Voltar"
                        if event.key == pygame.K_RETURN:
                            return self.volume, self.fps_index
