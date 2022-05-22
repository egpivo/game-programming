import tkinter as tk

from .game_object import GameObject

DIRECTIONS = {
    "bottom_right": [1, 1],
    "top_left": [-1, -1],
    "top_right": [1, -1],
    "bottom_left": [-1, 1],
}


class Ball(GameObject):
    def __init__(self, canvas: tk.Canvas, x: int, y: int) -> None:
        self.radius = 10
        self.direction = DIRECTIONS["top_right"]
        self.speed = 10
        item = canvas.create_oval(
            x - self.radius,
            y - self.radius,
            x + self.radius,
            y + self.radius,
            fill="white",
        )

        super().__init__(canvas, item)
