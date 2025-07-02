from abc import ABC, abstractmethod
import pygame.image

from code.Const import ENTITY_VIDA


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0  # velocidade da entidade
        self.health = ENTITY_VIDA[self.name] # vida da entidade

    @abstractmethod
    def move(self, ):
        pass

