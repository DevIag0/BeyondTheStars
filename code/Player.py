import pygame
from code.Const import PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT, PLAYER_KEY_DOWN, PLAYER_KEY_UP, ENTITY_SPEED, \
    PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot

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

    def animacao_lateral(self, ):
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx -4, self.rect.top - 25))
        return None
