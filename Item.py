import core
import random
from pygame import Vector2


class Item(object):

    def __init__(self):
        self.mass = 10
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.color = (65, 65, 65)
        self.mort = False;

    def show(self):
        core.Draw.circle(self.color, self.position, self.mass)