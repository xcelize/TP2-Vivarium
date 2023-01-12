import random
from pygame import Vector2
import core
from body import Body


class Agent(object):
    def __init__(self, body):
        self.body = body
        self.uuid = random.randint(100000, 999999999)
        self.coeff = 0.06

    def filtrePerception(self):
        pass

    def update(self):
        pass

    def show(self):
        self.body.show()
