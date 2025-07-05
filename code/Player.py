import pygame
from code.Const import PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT, PLAYER_KEY_DOWN, PLAYER_KEY_UP, ENTITY_SPEED, \
    PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY, COLOR_WHITE, COLOR_ORANGE
from code.Entity import Entity
from code.PlayerShot import PlayerShot
import sys

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        if self.name == 'Player1':
            self.frames = [
            pygame.image.load(f"./asset/{name}.png").convert_alpha(),
            pygame.image.load(f"./asset/{name}_slow.png").convert_alpha(),
            pygame.image.load(f"./asset/{name}_boost.png").convert_alpha()
        ]
        if self.name == 'Player2':
            self.frames = [
            pygame.image.load(f"./asset/{name}.png").convert_alpha(),
            pygame.image.load(f"./asset/{name}_slow.png").convert_alpha(),
            pygame.image.load(f"./asset/{name}_boost.png").convert_alpha()
        ]

        self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Tempo de espera entre os tiros
        # Configuração da animação
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 150  # milissegundos entre frames
        self.last_update_time = pygame.time.get_ticks()

    def move(self, ):

        # Verifica se as teclas de seta estão pressionadas e move o jogador
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
            self.frame_index = 0  # Reseta o frame para o primeiro ao mover para cima
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < pygame.display.get_surface().get_height():
            self.rect.centery += ENTITY_SPEED[self.name]
            self.frame_index = 2  # Reseta o frame para o primeiro ao mover para baixo
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < pygame.display.get_surface().get_width():
            self.rect.centerx += ENTITY_SPEED[self.name]

        self.animacao_frente_atras()

    def animacao_frente_atras(self, ):  # Lógica de animação
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_speed:
            self.last_update_time = current_time
            # Avança para o próximo frame e volta ao início se chegou ao final
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            # Atualiza a imagem atual para o frame correto
            self.surf = self.frames[self.frame_index]
        # Define a imagem do jogador como o frame atual

    def animacao_lateral(self, ):  #implementar futuramente
        pass

    def animacao_explosao(self): # implementar futuramente
        pass


    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx -4, self.rect.top - 25))
        return None

    @staticmethod
    def get_player_name(window, entity_list, player_number):
        """Captura o nome do jogador via teclado (máximo 6 caracteres)"""
        player_name = ""
        clock = pygame.time.Clock()

        while True:
            # Atualizar e desenhar o fundo
            for ent in entity_list:
                if ent.name.startswith('Level1bg'):
                    window.blit(source=ent.surf, dest=ent.rect)

            # Overlay escuro
            overlay = pygame.Surface(window.get_size())
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            window.blit(overlay, (0, 0))

            # Título
            font_title = pygame.font.SysFont(None, 60)
            title_text = font_title.render(f"DIGITE O NOME DO PLAYER {player_number}", True, COLOR_WHITE)
            title_rect = title_text.get_rect(center=(window.get_width() // 2, 250))
            window.blit(title_text, title_rect)

            # Campo de texto com o nome atual
            font_input = pygame.font.SysFont(None, 80)
            input_text = font_input.render(player_name + "_", True, COLOR_ORANGE)
            input_rect = input_text.get_rect(center=(window.get_width() // 2, 350))

            # Desenhar caixa de texto
            box_rect = pygame.Rect(input_rect.left - 20, input_rect.top - 10, max(200, input_rect.width + 40), input_rect.height + 20)
            pygame.draw.rect(window, COLOR_WHITE, box_rect, 3)

            window.blit(input_text, input_rect)

            # Instruções
            font_inst = pygame.font.SysFont(None, 30)
            inst_text1 = font_inst.render("Digite seu nome (máximo 6 caracteres)", True, COLOR_WHITE)
            inst_rect1 = inst_text1.get_rect(center=(window.get_width() // 2, 450))
            window.blit(inst_text1, inst_rect1)

            inst_text2 = font_inst.render("Pressione ENTER para confirmar", True, COLOR_WHITE)
            inst_rect2 = inst_text2.get_rect(center=(window.get_width() // 2, 480))
            window.blit(inst_text2, inst_rect2)

            # Contador de caracteres
            counter_text = font_inst.render(f"{len(player_name)}/6", True, COLOR_ORANGE)
            counter_rect = counter_text.get_rect(center=(window.get_width() // 2, 520))
            window.blit(counter_text, counter_rect)

            pygame.display.flip()
            clock.tick(60)

            # Gerenciar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Se não digitou nada, usar nome padrão
                        if not player_name.strip():
                            return f"Player{player_number}"
                        return player_name.strip()

                    elif event.key == pygame.K_BACKSPACE:
                        # Remover último caractere
                        player_name = player_name[:-1]

                    elif event.key == pygame.K_ESCAPE:
                        # Cancelar e usar nome padrão
                        return f"Player{player_number}"

                    else:
                        # Adicionar caractere se não exceder 6 caracteres
                        if len(player_name) < 6:
                            char = event.unicode
                            # Só aceitar letras, números e alguns caracteres especiais
                            if char.isprintable() and char not in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']:
                                player_name += char
