import pygame
import random
from Spaceship import SpaceShip
from Invader import Invader
from Explosion import Explosion


class Game:
    tick = 0
    pygame.init()
    window_width = 600
    window_height = 700
    window = pygame.display.set_mode((window_width, window_height))
    level = 1
    score = 0

    @classmethod
    def run_game(cls):
        run = True
        while run:
            for _ in range(100):
                run = cls.is_run()
                if not run:
                    cls.score = -1
                    break
                cls.window.fill((0, 0, 0))
                cls.print_caption("Level: " + str(Game.level), 200, 300, 70)
                cls.update()

            spaceship = SpaceShip((cls.window_width + 40) // 2, cls.window_height - 50)
            enemies = Invader.make_enemies()
            Explosion.explosions = []
            spaceship.bullets = []
            spaceship.max_bullets = cls.level / 10
            Invader.bullets = []

            while run:
                if cls.tick == 60:
                    cls.tick = 0

                run = cls.is_run()
                if not run:
                    cls.score = -1
                    break

                cls.set_pace(enemies)
                cls.check_collisions(enemies, spaceship)
                cls.control(spaceship)
                cls.move(spaceship, enemies)
                cls.draw(spaceship, enemies)
                cls.update()
                cls.tick += 1

                if not enemies or spaceship.lives == 0:
                    run = False

            if spaceship.lives == 0:
                for _ in range(200):
                    cls.print_game_over()
                    if not cls.is_run():
                        cls.score = -1
                        break
                    cls.update()

            elif not enemies:
                for _ in range(100):
                    cls.print_caption("Score: " + str(Game.score), 300 - len("Score: " + str(Game.score)) * 11, 300, 70)
                    if not cls.is_run():
                        cls.score = - 1
                        break
                    cls.update()
                run = True
                Game.level += 1

        return Game.score

    @staticmethod
    def set_pace(enemies):
        len1 = 0
        for col in enemies:
            len1 += len(col)
        if len1 == 60:
            Invader.pace = 30
        if len1 == 30:
            Invader.pace = 30
        elif len1 == 15:
            Invader.pace = 15
        elif len1 == 10:
            Invader.pace = 6
        elif len1 == 2:
            Invader.pace = 2

    @classmethod
    def print_caption(cls, caption, x, y, size):
        font = pygame.font.SysFont("comicsans", size)
        lvl = font.render(caption, 1, (255, 255, 255))
        cls.window.blit(lvl, (x, y))

    @classmethod
    def print_game_over(cls):
        pygame.draw.rect(cls.window, (0, 0, 0), (0, 200, 600, 300))
        cls.print_caption("Game over", 170, 250, 70)
        cls.print_caption("Score: " + str(Game.score), 300 - len("Score: " + str(Game.score)) * 11, 350, 70)

    @classmethod
    def print_stats(cls, lives):
        cls.print_caption("Score: " + str(Game.score), 5, 5, 60)
        cls.print_caption("Lives: " + str(lives), 400, 5, 60)

    @classmethod
    def check_collisions(cls, enemies, spaceship):
        for x, m in enumerate(Invader.bullets):
            if spaceship.is_collide(m):
                cls.boom()
                Explosion.make_explosion(spaceship.x, spaceship.y)
                Invader.bullets.pop(x)
                spaceship.lives -= 1

        for x, m in enumerate(spaceship.bullets):
            for col in enemies:
                for n, e in enumerate(col):
                    if e.is_collide(m):
                        cls.boom()
                        Explosion.make_explosion(e.x, e.y)
                        col.pop(n)
                        spaceship.bullets.pop(x)
                        if e.type == 0:
                            cls.score += 30
                        elif e.type == 1:
                            cls.score += 50
                        elif e.type == 2:
                            cls.score += 100

    @staticmethod
    def boom():
        return 1
        # pygame.mixer_music.load("sounds/ex1.mp3")
        # pygame.mixer_music.play()

    @classmethod
    def move(cls, spaceship, enemies):
        for x, m in enumerate(spaceship.bullets):
            m.move()
            if m.y < 0:
                spaceship.bullets.pop(x)

        for x, m in enumerate(Invader.bullets):
            m.move()
            if m.y > 700:
                Invader.bullets.pop(x)

        limit = 0
        for x, col in enumerate(enemies):
            if not col:
                enemies.pop(x)
            for e in col:
                if e.y >= 500:
                    limit = 1
                if (e.vel > 0 and e.x >= 550) or (e.vel < 10 and e.x < 10):
                    for col1 in enemies:
                        for e1 in col1:
                            e1.vel *= -1
                    break

        for col in enemies:
            for e in col:
                if limit == 0:
                    e.move_in_y(cls.tick)
                e.move_in_x(cls.tick)

        if (cls.tick % (60 - Game.level * 2 if Game.level * 2 <= 55 else 5)) == 0 and enemies:
            n = random.choice(enemies)
            n[-1].shot()

    @classmethod
    def control(cls, spaceship):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            spaceship.move_left(cls.tick)
        if keys[pygame.K_d]:
            spaceship.move_right(cls.tick)
        if keys[pygame.K_SPACE]:
            spaceship.shot(cls.tick)

    @classmethod
    def draw(cls, spaceship, enemies):
        cls.window.fill((0, 0, 0))

        spaceship.draw(cls.window)
        for m in spaceship.bullets:
            m.draw(cls.window, cls.tick)

        for m in Invader.bullets:
            m.draw(cls.window, cls.tick)
        for col in enemies:
            for e in col:
                e.draw(cls.window, cls.tick)

        for x, e in enumerate(Explosion.explosions):
            if e.tick == 3:
                Explosion.explosions.pop(x)
            else:
                e.draw(cls.window, cls.tick)

        cls.print_stats(spaceship.lives)

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
