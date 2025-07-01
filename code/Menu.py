import pygame
from code.Const import COLOR_ORANGE, COLOR_WHITE, MENU_OPTION
from pygame.rect import Rect
from pygame.surface import Surface




class Menu:
    def __init__(self, window, volume=0.5):
        self.window = window
        self.surf = pygame.image.load("./asset/Level1bg0.png").convert()
        self.rect = self.surf.get_rect(left=0, top=0)  # definir a posição do menu
        self.volume = volume

    def run(self,):
        menu_option: int = 0  # variável para armazenar a opção do menu selecionada
        pygame.mixer.music.load("./asset/Menu.mp3")  # carregar música de fundo
        pygame.mixer.music.play(-1)  # tocar música de fundo em loop
        pygame.mixer.music.set_volume(self.volume)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # desenha o fundo do menu

            self.menu_text(text_size=60, text="BEYOND", text_color=COLOR_WHITE,
                           text_center_pos=(self.window.get_width() // 2, 200))
            self.menu_text(text_size=60, text="THE STARS", text_color=COLOR_WHITE,
                           text_center_pos=(self.window.get_width() // 2, 260))

            for option in range(len(MENU_OPTION)):

                #  se a opção do menu for a opção selecionada, desenhar com cor branca, caso contrário, desenhar com cor laranja
                if option == menu_option:
                    self.menu_text(text_size=40, text=MENU_OPTION[option], text_color=COLOR_WHITE,
                                   text_center_pos=(self.window.get_width() // 2, 350 + option * 50))
                else:
                    self.menu_text(text_size=40, text=MENU_OPTION[option], text_color=COLOR_ORANGE,
                                   text_center_pos=(self.window.get_width() // 2, 350 + option * 50))

            pygame.display.flip()  # atualizar a tela

            # checar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # fechar a janela
                    pygame.quit()  # fechar o pygame
                    quit()  # sair do jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # tecla para baixo
                        menu_option += 1
                        if menu_option >= len(MENU_OPTION):
                            menu_option = 0

                    if event.key == pygame.K_UP:  # tecla para cima
                        menu_option -= 1
                        if menu_option < 0:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:  # tecla enter
                        return MENU_OPTION[menu_option], self.volume

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(None, size=text_size)  # carregar a fonte
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # renderizar o texto
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # definir a posição do texto
        self.window.blit(source=text_surf, dest=text_rect)  # desenhar o texto na tela
