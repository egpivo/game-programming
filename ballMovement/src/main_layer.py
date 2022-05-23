from collections import defaultdict

import cocos
import cocos.collision_model as cm
from actor import Actor
from pyglet.window import key

BALL_POSITIONS = [
    (100, 100), (70, 100), (540, 380), (540, 100), (100, 380)
]


class MainLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self) -> None:
        super(MainLayer, self).__init__()

        self.player = Actor(320, 250, (0, 0, 255))
        self.add(self.player)

        for position in BALL_POSITIONS:
            self.add(Actor(position[0], position[1], (255, 255, 0)))

        cell = self.player.width * 1.25
        self.collman = cm.CollisionManagerGrid(0, 640, 0, 480, cell, cell)

        self.speed = 1000
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def on_key_press(self, k: int, m: int) -> None:
        self.pressed[k] = 1

    def on_key_release(self, k: int, m: int) -> None:
        self.pressed[k] = 0

    def update(self, dt: float) -> None:
        self.collman.clear()

        for _, node in self.children:
            self.collman.add(node)
        for sentinel in self.collman.iter_colliding(self.player):
            self.remove(sentinel)

        x = self.pressed[key.RIGHT] - self.pressed[key.LEFT]
        y = self.pressed[key.UP] - self.pressed[key.DOWN]
        if x != 0 or y != 0:
            position = self.player.position
            new_x = position[0] + self.speed * x * dt
            new_y = position[1] + self.speed * y * dt
            self.player.position = (new_x, new_y)
            self.player.cshape.center = self.player.position


if __name__ == '__main__':
    cocos.director.director.init(caption="Ball Movement")
    layer = MainLayer()
    scene = cocos.scene.Scene(layer)
    cocos.director.director.run(scene)
