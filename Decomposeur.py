from agent import Agent
from body import Body

class Decomposeur(Agent):
    def __init__(self, body):
        super().__init__(body)

    def filtrePerception(self):
        manger = []
        danger = []
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, Body) and i.mort:
                manger.append(i)
        return manger, danger