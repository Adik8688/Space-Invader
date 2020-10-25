import pygame
import os


class Explosion:
    textures = [pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "b1.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "b2.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "b3.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "b4.png")))]
    explosions = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tick = 0
        self.textures = Explosion.textures

    @classmethod
    def make_explosion(cls, x, y):
        cls.explosions.append(Explosion(x, y))

    def draw(self, window, tick):
        if tick % 8 == 0:
            self.tick += 1
        if self.tick == 4:
            self.tick = 0
        window.blit(self.textures[self.tick], (self.x, self.y))
