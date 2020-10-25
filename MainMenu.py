import pygame
from Button import Button
from Game import Game
from Menu import Menu
from Scoreboard import Scoreboard
from GetName import GetName


class MainMenu(Menu):
    @classmethod
    def main_menu(cls):
        run = True
        buttons = Button.make_buttons(150, 200, 300, 100, 3)
        # pygame.mixer_music.init

        while run:
            if cls.music == 0:
                cls.music = 1
                # pygame.mixer_music.load("sounds/menu.mp3")
                # pygame.mixer.music.play(9999)
            run = cls.is_run()
            cls.draw(buttons)
            cls.update()

            if pygame.mouse.get_pressed()[0]:
                for x, b in enumerate(buttons):
                    if b.is_pressed(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        run = cls.action(x)
                        break

    @classmethod
    def action(cls, n):
        if n == 0:
           # pygame.mixer_music.stop()
            cls.music = 0
            return cls.result_to_scoreboard()

        if n == 1:
            return Scoreboard.show_scores()

        if n == 2:
            return False
        return True

    @classmethod
    def result_to_scoreboard(cls):
        result = Game.run_game()
        scores = Scoreboard.get_score()
        place = Scoreboard.check_scores(result, scores)
        name = "AAA"

        if place < 10 and result != -1:
            name = GetName.get_name()
            if name != -1:
                scores.insert(place, [name, str(result)])
                file = open("Score", "w")
                for s in scores:
                    file.write(s[0] + " " + s[1] + "\n")
                file.close()
                Scoreboard.show_scores()

        if result == -1 or name == -1:
            return False
        return True

    @classmethod
    def draw(cls, buttons):
        cls.window.fill((0, 0, 0))
        for x, b in enumerate(buttons):
            # b.draw(cls.window)
            cls.print_caption(cls.captions[x], 300 - len(cls.captions[x]) * 13, b.y + 25, 70)
        cls.print_caption("Space Invaders", 300 - len("Space Invaders") * 20, 50, 110)
