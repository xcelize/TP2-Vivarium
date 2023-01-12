import core
from body import Body


class BodyDecomposeur(Body):
    def __init__(self):
        self.params = self.params = core.memory("scenario")["Decomposeur"]["parametres"]
        super().__init__()
        self.color = (36, 65, 80)