import random
from pygame import Vector2
import core
from body import Body


class Agent(object):
    def __init__(self, body):
        self.body = body
        self.uuid = random.randint(100000, 999999999)
        self.coeff = 0.06

    def update(self):
        manger, danger = self.filtrePerception()
        if len(danger) > 0:
            target = self.body.position - danger[0].position
            target.scale_to_length(1 / target.length() ** 2)
            target.scale_to_length(target.length() * (self.coeff + self.body.mass))
            self.body.acc = self.body.acc + target
        elif len(manger) > 0:
            target = manger[0].position - self.body.position
            target.scale_to_length(target.length() * self.coeff)
            self.body.acc += target
        else:
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
            while target.length() == 0:
                target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
            target.scale_to_length(target.length() * self.coeff)
            self.body.acc += target

    def show(self):
        self.body.show()
