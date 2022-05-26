from collections import defaultdict

import cocos.euclid as eu
from pyglet.window import key

from .actor import Actor


class PlayerCannon(Actor):
    KEYS_PRESSED = defaultdict(int)

    def __init__(self, x: float, y: float) -> None:
        super(PlayerCannon, self).__init__("image/cannon.png", x, y)
        self.spped = eu.Vector2(200, 0)
        self.position = eu.Vector2(x, y)

    def update(self, elapsed: float) -> None:
        pressed = self.KEYS_PRESSED
        movement = pressed[key.RIGHT] - pressed[key.LEFT]
        w = self.width * 0.5

        if movement != 0 and w <= self.x <= self.parent.width - w:
            self.move(self.speed * movement * elapsed)

    def collide(self, other):
        other.kill()
        self.kill()
