import pygame
from code.Const import ENTITY_SPEED, ENTITY_VIDA
from code.Entity import Entity


class Meteor(Entity):
    def __init__(self, name: str, position: tuple):
        # Inicializar Entity sem carregar imagem automaticamente
        self.name = name
        self.rect = pygame.Rect(position[0], position[1], 0, 0)
        self.health = ENTITY_VIDA[self.name]  # Inicializar a saúde do meteoro

        # Carregar a imagem específica do meteoro (Meteor1.png)
        self.surf = pygame.image.load("./asset/Meteor1.png").convert_alpha()
        self.rect = self.surf.get_rect(center=position)

        # Configuração de rotação para dar efeito visual
        self.rotation_angle = 0
        self.rotation_speed = 2  # Velocidade de rotação
        self.original_surf = self.surf.copy()  # Manter imagem original para rotação

    def move(self):
        # Movimento vertical
        self.rect.centery += ENTITY_SPEED[self.name]

        # Rotação do meteoro
        self.rotation_angle += self.rotation_speed
        if self.rotation_angle >= 360:
            self.rotation_angle = 0

        # Aplicar rotação
        self.surf = pygame.transform.rotate(self.original_surf, self.rotation_angle)
        # Reajustar o rect para manter a posição central
        old_center = self.rect.center
        self.rect = self.surf.get_rect()
        self.rect.center = old_center

    def shoot(self):
        # Meteoro não atira, então retorna None
        return None

    def get_collision_rect(self):
        """Retorna o rect de colisão baseado no sprite atual"""
        return self.rect
