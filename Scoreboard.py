import pygame
from Menu import Menu


class Scoreboard(Menu):
    @staticmethod
    def check_scores(result, scores):
        for x, s in enumerate(scores):
            if result > int(scores[x][1]):
                return x
        return len(scores)

    @classmethod
    def show_scores(cls):
        tick = 0
        run = True
        scores = cls.get_score()

        while run:
            tick += 1
            if tick == 5:
                tick = 0

            run = cls.is_run()
            if not run:
                return False
            cls.print_scores(scores)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                run = False
            cls.update()
        return True

    @classmethod
    def print_scores(cls, scores):
        cls.window.fill((0, 0, 0))
        for i in range(10):
            try:
                result = str(i + 1) + ". " + " ".join(scores[i])
            except IndexError:
                result = str(i + 1) + ". AAA 999999"
            cls.print_caption(result, 300 - len(result) * 11, 50 + i * 55, 60)
            cls.print_caption("Press space to continue", 300 - len("Press space to continue") * 8, 640, 50)

    @classmethod
    def get_score(cls):
        scores = []
        score = open("Score")
        for s in score:
            scores.append(s.split())
        return scores
