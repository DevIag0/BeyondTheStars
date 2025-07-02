from code.Const import ALTURA_JANELA
from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # Verifica se as entidades estão dentro dos limites da janela
        if isinstance(ent, Enemy):
            if ent.rect.top > ALTURA_JANELA + 100:  # Se o inimigo sair da janela, ele é destruído
                ent.health = 0  # Se o inimigo sair da janela, ele é destruído

    @staticmethod
    def verify_collision(entity_list: list[Entity]):  # Verifica colisões entre entidades
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity) # Verifica se a entidade está dentro da janela

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)