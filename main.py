import core
import random
from pygame.math import Vector2

from BodyCarnivore import BodyCarnivore
from BodyHerbivore import BodyHerbivore
from BodySuperPredateur import BodySuperPredateur
from Carnivore import Carnivore
from Decomposeur import Decomposeur
from Herbivore import Herbivore
from agent import Agent
from SuperPredateur import SuperPredateur
from Item import Item
from body import Body

import json


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    f = open('scenario.json')
    data = json.load(f)
    core.memory('scenario', data)
    reset()

    print("Setup END-----------")


def computePerception(agent):
    agent.body.fustrum.perception_list = []
    for b in core.memory("agents"):
        if agent.uuid != b.uuid and agent.body.fustrum.inside(b.body):
            agent.body.fustrum.perception_list.append(b.body)

    for i in core.memory("items"):
        if agent.body.fustrum.inside(i):
            agent.body.fustrum.perception_list.append(i)




def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()


def updateEnv():
    for a in core.memory("agents"):
        for c in core.memory("agents"):
            if c.uuid != a.uuid:
                if isinstance(a, SuperPredateur) and isinstance(c, Carnivore) and a.body.position.distance_to(
                        c.body.position) <= a.body.mass:
                    c.body.mort = True
                    a.body.niveau_faim -= 20
                    if a.body.niveau_faim < 0:
                        a.body.niveau_faim = 0

                if isinstance(a, Decomposeur) and c.body.dead and a.body.position.distance_to(
                        c.body.position) <= a.body.mass:
                    core.memory("agents").remove(c)
                    a.body.niveau_faim -= 20
                    if a.body.niveau_faim < 0:
                        a.body.niveau_faim = 0

                if isinstance(a, Carnivore) and isinstance(c, Herbivore) and a.body.position.distance_to(
                        c.body.position) <= a.body.mass:
                    core.memory("agents").remove(c)
                    a.body.niveau_faim -= 20
                    if a.body.niveau_faim < 0:
                        a.body.niveau_faim = 0


def reset():
    core.memory("agents", [])
    core.memory("items", [])

    for i in range(0, core.memory("scenario")["SuperPredateur"]["nb"]):
        core.memory("agents").append(SuperPredateur(BodySuperPredateur()))

    for i in range(0, core.memory("scenario")["Carnivore"]["nb"]):
        core.memory("agents").append(Carnivore(BodyCarnivore()))

    for i in range(0, core.memory("scenario")["Herbivore"]["nb"]):
        core.memory("agents").append(Herbivore(BodyHerbivore()))

    for i in range(0, 5):
        core.memory("items").append(Item())

    # TODO: Add other items


def run():
    if core.getKeyPressList('r'):
        reset()
    core.cleanScreen()

    # Display
    for agent in core.memory("agents"):
        agent.show()

    for item in core.memory("items"):
        item.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    updateEnv()


core.main(setup, run)