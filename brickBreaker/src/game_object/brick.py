import tkinter as tk

from .game_object import GameObject

COLORS = {1: "#999999", 2: "#555555", 3: "#222222"}


class Brick(GameObject):
    def __init__(self, canvas: tk.Canvas, x: int, y: int, hits: int) -> None:
        self.width = 75
        self.height = 20
        self.hits = hits
        item = canvas.create_rectangle(
            x - self.width / 2,
            y - self.height / 2,
            x + self.width / 2,
            y + self.height / 2,
            fill=COLORS[hits],
            tags="brick"
        )

        super().__init__(canvas, item)

    def hit(self):
        self.hits -= 1
        if self.hits == 0:
            self.delete()
        else:
            self.canvas.itemconfig(
                self.item,
                fill=COLORS[self.hits]
            )
