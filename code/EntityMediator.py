from code.EnemyShot import EnemyShot
from code.Const import ALTURA_JANELA, PLAYER_KEY_SHOOT
from code.Enemy import Enemy
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # Verifica se as entidades estão dentro dos limites da janela
        if isinstance(ent, Enemy):
            if ent.rect.top >= ALTURA_JANELA + 100:  # Se o inimigo sair da janela, ele é destruído
                ent.health = 0  # Se o inimigo sair da janela, ele é destruído
        if isinstance(ent, PlayerShot):
            if ent.rect.top < 0:  # Se o tiro sair da janela, ele é destruído
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.top >= ALTURA_JANELA:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):  # Verifica colisões entre entidades
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity) # Verifica se a entidade está dentro da janela

    @staticmethod
    def verify_health(entity_list: list[Entity]):   # Verifica a saúde das entidades
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)