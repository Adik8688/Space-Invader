import pygame


class Menu:
    pygame.init()
    window = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Space invaders by ADR")
    captions = ["Start", "Score board", "Exit"]
    music = 0

    @staticmethod
    def is_run():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    @staticmethod
    def update():
        pygame.display.update()
        pygame.time.Clock().tick(60)
        pygame.time.delay(1)

    @classmethod
    def print_caption(cls, caption, x, y, size):
        font = pygame.font.SysFont("comicsans", size)
        lvl = font.render(caption, 1, (255, 255, 255))
        cls.window.blit(lvl, (x, y))
