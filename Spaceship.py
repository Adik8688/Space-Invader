import pygame
import os
from Bullet import Bullet


class SpaceShip:
    textures = [pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "s1.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "s3.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "s2.png")))]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
        self.textures = SpaceShip.textures
        self.move = 0
        self.bullets = []
        self.lives = 3
        self.max_bullets = 1

    def move_right(self, tick):
        self.move = 1
        if tick % 2 == 0:
            self.x = self.x + self.vel if self.x <= 545 else 550

    def move_left(self, tick):
        self.move = 2
        if tick % 2 == 0:
            self.x = self.x - self.vel if self.x >= 15 else 10

    def draw(self, window):
        window.blit(self.textures[self.move], (self.x, self.y))
        self.move = 0

    def shot(self, tick):
        if tick % 2 == 0 and len(self.bullets) < self.max_bullets:
            self.bullets.append(Bullet(self.x + 14, self.y, 0))

    def is_collide(self, bullet):
        bullet_mask = bullet.get_mask()
        ship_mask = pygame.mask.from_surface(self.textures[0])

        point = (bullet.x - self.x, self.y - bullet.y + 20)

        collide = ship_mask.overlap(bullet_mask, point)

        if collide:
            return True
        return False
