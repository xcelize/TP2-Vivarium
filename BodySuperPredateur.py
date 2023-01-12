import core
from body import Body


class BodySuperPredateur(Body):

    def __init__(self):
        self.params = core.memory("scenario")["SuperPredateur"]["parametres"]
        super().__init__()
        self.color = (255, 255, 255)

