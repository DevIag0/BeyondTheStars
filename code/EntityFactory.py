from code.Background import Background
from code.Const import ALTURA_JANELA, LARGURA_JANELA


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "Level1bg":
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(name=f'Level1bg{i}',position=(0, 0)))
                    list_bg.append(Background(name=f'Level1bg{i}', position=(0, -ALTURA_JANELA)))

                return list_bg
