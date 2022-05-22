import tkinter as tk

from game_object.ball import Ball
from game_object.brick import Brick
from game_object.paddle import Paddle

PADDLE_HEIGHT = 326
BRICK_WIDTH = 75


class Game(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.lives = 3
        self.width = 600
        self.height = 400
        self.canvas = tk.Canvas(
            self,
            bg="#405DE6",
            width=self.width,
            height=self.height
        )
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.ball = None
        self.paddle = Paddle(self.canvas, self.width / 2, PADDLE_HEIGHT)
        self.items[self.paddle.item] = self.paddle

        for x in range(5, self.width - 5, BRICK_WIDTH):
            self.add_brick(x + BRICK_WIDTH / 2, 50, 2)
            self.add_brick(x + BRICK_WIDTH / 2, 70, 1)
            self.add_brick(x + BRICK_WIDTH / 2, 90, 1)

        self.hud = None
        self.setup_game()
        self.canvas.focus_set()
        self.canvas.bind("<Left>", lambda _: self.paddle.move(-10))
        self.canvas.bind("<Right>", lambda _: self.paddle.move(-10))

    def setup_game(self) -> None:
        self.add_ball()
        self.update_lives_text()
        self.text = self.draw_text(300, 200, "Press Space to start")
        self.canvas.bind("<space>", lambda _: self.start_game())

    def add_ball(self):
        if self.ball is not None:
            self.ball.delete()

        paddle_coords = self.paddle.get_position()
        x = (paddle_coords[0] + paddle_coords[2]) * 0.5
        self.ball = Ball(self.canvas, x, 310)
        self.paddle.ball = self.ball

    def add_brick(self, x, y, hits):
        brick = Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    def draw_text(self, x, y, text, size="40"):
        font = ("Helvetica", size)
        return self.canvas.create_text(x, y, text=text, font=font)

    def update_lives_text(self):
        text = f"Lives: {self.lives}"
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hello, Pong!")
    game = Game(root)
    game.mainloop()
    game.mainloop()
