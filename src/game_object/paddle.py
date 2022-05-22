import tkinter as tk

from .ball import Ball
from .game_object import GameObject


class Paddle(GameObject):
    def __init__(self, canvas: tk.Canvas, x: int, y: int) -> None:
        self.width = 80
        self.height = 10
        self.ball = None
        self.direction = [1, -1]
        self.speed = 10
        item = canvas.create_rectangle(
            x - self.width / 2,
            y - self.height / 2,
            x + self.width / 2,
            y + self.height / 2,
            fill="blue"
        )

        super().__init__(canvas, item)

    @property
    def ball(self) -> None:
        return self._ball

    @property.setter
    def ball(self, ball: Ball) -> None:
        self._ball = ball

    def move(self, offset: int) -> None:
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super(Paddle, self).move(offset, 0)
            if self.ball is not None:
                self.ball.move(offset, 0)
                self.ball.move(offset, 0)
