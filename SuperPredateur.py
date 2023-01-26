import random

from pygame import Vector2

from BodySuperPredateur import BodySuperPredateur
from agent import Agent
from body import Body


class SuperPredateur(Agent):
    def __init__(self, body):
        super().__init__(body)

    def filtrePerception(self):
        manger = []
        danger = []
        for i in self.body.fustrum.perception_list:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, Body) and not isinstance(i, BodySuperPredateur) and not i.mort:
                manger.append(i)
        return manger, danger