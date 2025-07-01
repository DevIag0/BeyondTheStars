from code.Const import ALTURA_JANELA, ENTITY_SPEED
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= ALTURA_JANELA:
            self.rect.top = -ALTURA_JANELA

