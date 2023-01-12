import core
from body import Body


class BodyHerbivore(Body):
    def __init__(self):
        self.params = self.params = core.memory("scenario")["Herbivore"]["parametres"]
        super().__init__()
        self.color = (188, 197, 0)
