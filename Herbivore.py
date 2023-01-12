from pygame import Vector2
import random
from BodyHerbivore import BodyHerbivore
from Item import Item
from agent import Agent
from body import Body


class Herbivore(Agent):

    def __init__(self, body):
        super().__init__(body)

    def filtrePerception(self):
        manger = []
        for i in self.body.fustrum.perception_list:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, Item) and not isinstance(i, BodyHerbivore) and not i.mort:
                manger.append(i)
        return manger
    def update(self):
        manger = self.filtrePerception()
        if len(manger) > 0:
            target = manger[0].position - self.body.position
            target.scale_to_length(target.length() * self.coeff)
            self.body.acc += target
        else:
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
            while target.length() == 0:
                target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
            target.scale_to_length(target.length() * self.coeff)
            self.body.acc += target