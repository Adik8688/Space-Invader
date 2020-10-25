import pygame
import os


class Bullet:
    textures = [[pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "m1.png"))),
                 pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "m1.png")))],
                [pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "mi1.png"))),
                 pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "mi2.png")))]
                ]

    def __init__(self, x, y, mode):
        self.x = x
        self.y = y
        self.vel = 10 if mode == 0 else -10
        self.texture = Bullet.textures[mode]
        self.tick = 0

    def move(self):
        self.y -= self.vel

    def draw(self, window, tick):
        if tick % 3 == 0:
            if self.tick == 0:
                self.tick = 1
            else:
                self.tick = 0

        window.blit(self.texture[self.tick], (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.texture[self.tick])
