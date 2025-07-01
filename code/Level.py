import pygame
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import COLOR_WHITE, COLOR_ORANGE


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []  # lista de entidades no nível
        self.entity_list.extend(EntityFactory.get_entity('Level1bg')) # adiciona entidades ao nível
        self.paused = False  # adiciona um estado para controlar a pausa

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

        continue_rect = continue_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 + 30))
        exit_rect = exit_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2 + 80))

        self.window.blit(continue_text, continue_rect)
        self.window.blit(exit_text, exit_rect)

    def pause_musica(self):
        self.paused = not self.paused
        # Pausa ou retoma a música dependendo do pause do do jogo
        if self.paused:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def run(self,):
        clock = pygame.time.Clock()  # para controlar a taxa de quadros

        while True:
            # Desenhar entidades
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                # Só move as entidades se o jogo não estiver pausado
                if not self.paused:
                    ent.move()

            # Se o jogo estiver pausado, desenha o menu de pausa
            if self.paused:
                self.pause_menu()

            pygame.display.flip()

            # Gerencia os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Tecla P para pausar/despausar
                        self.pause_musica()
                    elif event.key == pygame.K_ESCAPE:
                        if self.paused:
                            # Se estiver pausado, ESC sai do nível
                            return "menu"
                        else:
                            # Se não estiver pausado, ESC pausa o jogo
                            self.pause_musica()

            # Limita a taxa de quadros
            clock.tick(60)
