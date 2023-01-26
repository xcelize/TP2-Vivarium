from pygame import Vector2
import random
from BodyHerbivore import BodyHerbivore
from Item import Item
from agent import Agent
from body import Body


class CarnivoreBody:
    pass


class Herbivore(Agent):

    def __init__(self, body):
        super().__init__(body)

    def filtrePerception(self):
        manger = []
        danger = []
        for i in self.body.fustrum.perception_list:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, Item) and not isinstance(i, BodyHerbivore) and not i.mort:
                manger.append(i)
            if isinstance(i, CarnivoreBody):
                danger.append(i)
        return manger, danger