import pygame
import os
from Bullet import Bullet


class Invader:
    textures = [[pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "i11.png"))),
                 pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "i12.png")))],
                [pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "i21.png"))),
                 pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "i22.png")))],
                [pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "i31.png"))),
                 pygame.transform.scale2x(pygame.image.load(os.path.join("textures", "i32.png")))]
                ]
    bullets = []
    pace = 60

    def __init__(self, x, y, type_of_inv):
        self.x = x
        self.y = y
        self.tick = 0
        self.type = type_of_inv
        self.textures = Invader.textures[type_of_inv]
        self.vel = 10
        self.move_x = 0
        self.move_y = 0

    @classmethod
    def make_enemies(cls):
        enemies = []
        for i in range(10):
            col = []
            for j in range(6):
                if j == 0:
                    col.append(Invader(50 * (i + 1), 50 * (j + 1), 2))
                elif j == 1 or j == 2:
                    col.append(Invader(50 * (i + 1), 50 * (j + 1), 1))
                else:
                    col.append(Invader(50 * (i + 1), 50 * (j + 1), 0))

            enemies.append(col)
        return enemies

    def draw(self, window, tick):
        window.blit(self.textures[self.tick], (self.x, self.y))
        if tick % (Invader.pace // 2) == 0:
            if self.tick == 0:
                self.tick = 1
            else:
                self.tick = 0

    def move_in_x(self, tick):
        if tick % 1 == 0:
            self.move_x += 1
        if self.move_x >= Invader.pace:
            self.move_x = 0
            self.x += self.vel

    def move_in_y(self, tick):
        if tick % 1 == 0:
            self.move_y += 1
        if self.move_y >= Invader.pace * 30:
            self.move_y = 0
            self.y += 50

    def shot(self):
        Invader.bullets.append(Bullet(self.x + 14, self.y, 1))

    def is_collide(self, bullet):
        bullet_mask = bullet.get_mask()
        inv_mask = pygame.mask.from_surface(self.textures[0])

        point = (bullet.x - self.x, bullet.y - self.y - 20)

        collide = inv_mask.overlap(bullet_mask, point)

        if collide:
            return True
        return False
