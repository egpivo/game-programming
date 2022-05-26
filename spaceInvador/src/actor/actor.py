import cocos.collision_model as cm
import cocos.euclid as eu
import cocos.sprite


class Actor(cocos.sprite.Sprite):
    def __init__(self, image: str, x: float, y: float) -> None:
        super(Actor, self).__init__(image)

        self.position = eu.Vector2(x, y)
        self.cshape = cm.AARectShape(
            self.position,
            self.width / 2,
            self.height / 2
        )

    def move(self, offset: float) -> None:
        self.position += offset
        self.cshape.center += offset

    def update(self, elapse: float) -> None:
        pass

    def collide(self, other):
        pass
