from pygame import Vector2
import random

from BodySuperPredateur import BodySuperPredateur
from BodyCarnivore import BodyCarnivore
from BodyHerbivore import BodyHerbivore
from agent import Agent


class Carnivore(Agent):
    def __init__(self, body):
        super().__init__(body)

    def filtrePerception(self):
        manger = []
        danger = []
        for i in self.body.fustrum.perception_list:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, BodyHerbivore) and not isinstance(i, BodyCarnivore) and not i.mort:
                manger.append(i)
            if isinstance(i, BodySuperPredateur):
                danger.append(i)
        return manger, danger