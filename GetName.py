import pygame
from Menu import Menu


class GetName(Menu):

    @classmethod
    def get_name(cls):
        tick = 0
        run = True
        letters = [ord("A")] * 3
        index = 2

        while run:
            tick += 1
            run = cls.is_run()
            if not run:
                return -1

            if tick == 5:
                tick = 0
                keys = pygame.key.get_pressed()

                if keys[pygame.K_w]:
                    if letters[index] == ord("Z"):
                        letters[index] = ord("A")
                    else:
                        letters[index] += 1

                if keys[pygame.K_s]:
                    if letters[index] == ord("A"):
                        letters[index] = ord("Z")
                    else:
                        letters[index] -= 1

                if keys[pygame.K_d]:
                    if index == 2:
                        index = 0
                    else:
                        index += 1

                if keys[pygame.K_a]:
                    if index == 0:
                        index = 2
                    else:
                        index -= 1

                if keys[pygame.K_RETURN]:
                    run = False

            cls.print_letters(letters)
            cls.print_arrows(index)
            cls.update()

        return "".join([chr(x) for x in letters])

    @classmethod
    def print_letters(cls, letters):
        cls.window.fill((0, 0, 0))

        for x, l in enumerate(letters):
            cls.print_caption(chr(l), 190 + x * 80, 200, 120)

        cls.print_caption("Press enter to confirm", 60, 450, 65)

    @classmethod
    def print_arrows(cls, i):
        pygame.draw.polygon(cls.window, (255, 255, 255),
                            [(210 + i * 80, 180), (230 + i * 80, 180), (220 + i * 80, 160)])
        pygame.draw.polygon(cls.window, (255, 255, 255),
                            [(210 + i * 80, 290), (230 + i * 80, 290), (220 + i * 80, 310)])
