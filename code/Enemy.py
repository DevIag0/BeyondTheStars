import pygame
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.EnemyShot import EnemyShot


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.frames = [
            pygame.image.load(f"./asset/{name}_slow.png").convert_alpha(),
            pygame.image.load(f"./asset/{name}.png").convert_alpha(),
            pygame.image.load(f"./asset/{name}_boost.png").convert_alpha()
        ]
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Tempo de espera entre os tiros

        # Configuração da animação
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 150  # milissegundos entre frames
        self.last_update_time = pygame.time.get_ticks()

    # Lista para armazenar os frames da animação

    def move(self, ):
        self.rect.centery += ENTITY_SPEED[self.name]

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

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx - 4 , self.rect.centery))
        return None