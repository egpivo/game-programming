from collections import defaultdict

import cocos
import cocos.collision_model as cm
import cocos.euclid as eu
from pyglet.window import key


class Actor(cocos.sprite.Sprite):
    def __init__(self, x: float, y: float, color: str) -> None:
        super(Actor, self).__init__("asset/ball.png", color=color)

        self.position = position = eu.Vector2(x, y)
        self.cshape = cm.CircleShape(position, self.width / 2)
