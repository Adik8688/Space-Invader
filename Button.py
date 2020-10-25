import pygame


class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @classmethod
    def make_buttons(cls, x, y, w, h, n):
        buttons = []
        for i in range(n):
            buttons.append(Button(x, y + i * 150, w, h))
        return buttons

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def is_pressed(self, x, y):
        if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
            return True
        return False
