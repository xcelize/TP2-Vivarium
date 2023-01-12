import core
from body import Body


class BodyCarnivore(Body):

    def __init__(self):
        self.params = self.params = core.memory("scenario")["Carnivore"]["parametres"]
        super().__init__()
        self.color = (255, 252, 0)

