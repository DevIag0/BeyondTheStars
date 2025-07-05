import sys
import pygame
from code.DatabaseProxy import DatabaseProxy
from code.Const import COLOR_WHITE, COLOR_ORANGE, MENU_FPS
from code.Menu import Menu


class Score(Menu):
    def __init__(self, window):
        super().__init__(window)
        self.db_proxy = DatabaseProxy()
        self.selected_option = 0
        self.clock = pygame.time.Clock()
        self.options = ["VER TOP 10", "ESTATÍSTICAS POR JOGADOR", "VOLTAR"]

    def save_score(self, player_name, score):
        """Salva a pontuação de um jogador"""
        self.db_proxy.save_score(player_name, score)

    def display_top_scores(self):
        """Exibe as 10 maiores pontuações organizadas em linha"""
        while True:
            # Atualizar e desenhar backgrounds
            for bg in self.backgrounds:
                bg.move()
                self.window.blit(bg.surf, bg.rect)

            # Título
            self.menu_text(text_size=50, text="TOP 10 PONTUAÇÕES", text_color=COLOR_WHITE,
                           text_center_pos=(self.window.get_width() // 2, 80))

            # Obter e exibir top scores
            top_scores = self.db_proxy.get_top_scores(10)

            if not top_scores:
                self.menu_text(text_size=30, text="Nenhuma pontuação registrada ainda", text_color=COLOR_ORANGE,
                               text_center_pos=(self.window.get_width() // 2, 300))
            else:
                # Cabeçalho organizado em colunas
                self.menu_text(text_size=25, text="POS", text_color=COLOR_ORANGE,
                               text_center_pos=(150, 150))
                self.menu_text(text_size=25, text="JOGADOR", text_color=COLOR_ORANGE,
                               text_center_pos=(300, 150))
                self.menu_text(text_size=25, text="PONTOS", text_color=COLOR_ORANGE,
                               text_center_pos=(450, 150))
                self.menu_text(text_size=25, text="DATA", text_color=COLOR_ORANGE,
                               text_center_pos=(600, 150))

                for i, (player_name, score, date) in enumerate(top_scores):
                    pos = i + 1
                    # Limitar o nome do jogador a 12 caracteres
                    display_name = player_name[:12] if len(player_name) > 12 else player_name
                    # Formatar a data (pegar apenas data, sem hora)
                    formatted_date = date.split(' ')[0] if ' ' in date else date

                    y_position = 180 + i * 35
                    color = COLOR_WHITE if pos <= 3 else COLOR_ORANGE

                    # Exibir em colunas organizadas
                    self.menu_text(text_size=20, text=f"{pos:2d}", text_color=color,
                                   text_center_pos=(150, y_position))
                    self.menu_text(text_size=20, text=display_name, text_color=color,
                                   text_center_pos=(300, y_position))
                    self.menu_text(text_size=20, text=f"{score:,}", text_color=color,
                                   text_center_pos=(450, y_position))
                    self.menu_text(text_size=20, text=formatted_date, text_color=color,
                                   text_center_pos=(600, y_position))

            # Instruções
            self.menu_text(text_size=25, text="Pressione qualquer tecla para voltar", text_color=COLOR_ORANGE,
                           text_center_pos=(self.window.get_width() // 2, 650))

            pygame.display.flip()
            self.clock.tick(MENU_FPS)

            # Aguardar tecla para voltar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    return

    def display_player_stats(self):
        """Exibe estatísticas de jogadores"""
        selected_player = 0
        players = self.db_proxy.get_all_players()

        while True:
            # Atualizar e desenhar backgrounds
            for bg in self.backgrounds:
                bg.move()
                self.window.blit(bg.surf, bg.rect)

            # Título
            self.menu_text(text_size=50, text="ESTATÍSTICAS POR JOGADOR", text_color=COLOR_WHITE,
                           text_center_pos=(self.window.get_width() // 2, 80))

            if not players:
                self.menu_text(text_size=30, text="Nenhum jogador encontrado", text_color=COLOR_ORANGE,
                               text_center_pos=(self.window.get_width() // 2, 300))
                self.menu_text(text_size=25, text="Pressione qualquer tecla para voltar", text_color=COLOR_ORANGE,
                               text_center_pos=(self.window.get_width() // 2, 650))
            else:
                # Lista de jogadores
                self.menu_text(text_size=30, text="Selecione um jogador:", text_color=COLOR_WHITE,
                               text_center_pos=(self.window.get_width() // 2, 150))

                for i, player in enumerate(players):
                    color = COLOR_WHITE if i == selected_player else COLOR_ORANGE
                    self.menu_text(text_size=25, text=player, text_color=color,
                                   text_center_pos=(self.window.get_width() // 2, 200 + i * 40))

                # Exibir estatísticas do jogador selecionado
                if players:
                    current_player = players[selected_player]
                    stats = self.db_proxy.get_player_stats(current_player)

                    self.menu_text(text_size=30, text=f"Estatísticas de {current_player}:", text_color=COLOR_WHITE,
                                   text_center_pos=(self.window.get_width() // 2, 400))

                    self.menu_text(text_size=25, text=f"Total de jogos: {stats['total_games']}", text_color=COLOR_ORANGE,
                                   text_center_pos=(self.window.get_width() // 2, 450))

                    self.menu_text(text_size=25, text=f"Melhor pontuação: {stats['best_score']}", text_color=COLOR_ORANGE,
                                   text_center_pos=(self.window.get_width() // 2, 480))

                # Instruções
                self.menu_text(text_size=20, text="↑↓ - Navegar | ENTER - Confirmar | ESC - Voltar", text_color=COLOR_ORANGE,
                               text_center_pos=(self.window.get_width() // 2, 650))

            pygame.display.flip()
            self.clock.tick(MENU_FPS)

            # Gerenciar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if not players:  # Se não há jogadores, qualquer tecla volta
                        return
                    if event.key == pygame.K_DOWN:
                        selected_player = (selected_player + 1) % len(players)
                    if event.key == pygame.K_UP:
                        selected_player = (selected_player - 1) % len(players)

    def run(self):
        """Menu principal do sistema de scores"""
        while True:
            # Atualizar e desenhar backgrounds
            for bg in self.backgrounds:
                bg.move()
                self.window.blit(bg.surf, bg.rect)

            # Título
            self.menu_text(text_size=60, text="PONTUAÇÕES", text_color=COLOR_WHITE,
                           text_center_pos=(self.window.get_width() // 2, 200))

            # Opções do menu
            for i, option in enumerate(self.options):
                color = COLOR_WHITE if i == self.selected_option else COLOR_ORANGE
                self.menu_text(text_size=40, text=option, text_color=color,
                               text_center_pos=(self.window.get_width() // 2, 320 + i * 60))

            pygame.display.flip()
            self.clock.tick(MENU_FPS)

            # Gerenciar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    if event.key == pygame.K_RETURN:
                        if self.selected_option == 0:  # VER TOP 10
                            self.display_top_scores()
                        elif self.selected_option == 1:  # ESTATÍSTICAS POR JOGADOR
                            self.display_player_stats()
                        elif self.selected_option == 2:  # VOLTAR
                            return
                    if event.key == pygame.K_ESCAPE:
                        return
