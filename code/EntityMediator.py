from code.EnemyShot import EnemyShot
from code.Const import ALTURA_JANELA, PLAYER_KEY_SHOOT
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
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
    def verify_collision(entity_list: list[Entity]):
        # Sistema simples e didático de colisão
        tiros_player = [e for e in entity_list if isinstance(e, PlayerShot)]
        tiros_inimigo = [e for e in entity_list if isinstance(e, EnemyShot)]
        inimigos = [e for e in entity_list if isinstance(e, Enemy)]
        jogadores = [e for e in entity_list if isinstance(e, Player)]

        # Tiros do player e do inimigo se anulam se colidirem
        for tiro_player in tiros_player:
            for tiro_inimigo in tiros_inimigo:
                if tiro_player.rect.colliderect(tiro_inimigo.rect):
                    tiro_player.health = 0
                    tiro_inimigo.health = 0

        # Tiros do player atingem inimigos
        for tiro in tiros_player:
            for inimigo in inimigos:
                if tiro.rect.colliderect(inimigo.rect):
                    inimigo.health -= 50
                    tiro.health = 0

        # Tiros do inimigo atingem jogadores
        for tiro in tiros_inimigo:
            for jogador in jogadores:
                if tiro.rect.colliderect(jogador.rect):
                    jogador.health -= 50
                    tiro.health = 0

        # Verifica se entidades saíram da tela
        for ent in entity_list:
            EntityMediator.__verify_collision_window(ent)

    @staticmethod
    def verify_health(entity_list: list[Entity]):   # Verifica a saúde das entidades
        for ent in entity_list[:]:
            # Só remove se não for Player
            if ent.health <= 0 and not isinstance(ent, Player):
                entity_list.remove(ent)