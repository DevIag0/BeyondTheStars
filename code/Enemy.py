from code.Const import ENTITY_SPEED, ALTURA_JANELA
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # Lista para armazenar os frames da animação

    def move(self, ):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= ALTURA_JANELA:
            self.rect.top = -ALTURA_JANELA

