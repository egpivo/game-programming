import tkinter as tk
from .game_object import GameObject

class Ball(GameObject):
    def __init__(self, canvas: tk.Canvas, x: int, y: int) -> None:
        self.radius = 10
        self.direction = [1, -1]
        self.speed = 10
        item = canvas.create_oval(
            x - self.radius,
            y - self.radius,
            x + self.radius,
            y + self.radius,
            fill="white"
        )

        super().__init__(canvas, item)