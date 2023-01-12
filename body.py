import random

import pygame.time
from pygame import Vector2

import core
from fustrum import Fustrum
from time import time


class Body(object):

    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.vitesse = Vector2(random.uniform(-5,5),random.uniform(-5,5))
        self.color = (255, 255, 255)
        self.vMax = 2
        self.accMax = 10
        self.mass = 10
        self.last_params_update = pygame.time.get_ticks()
        self.birthday = time()
        self.esperance = time()
        self.fustrum = Fustrum(150, self)
        self.acc = Vector2()
        self.niveau_faim = random.randint(self.params["faimMax"][0], self.params["faimMax"][1])
        self.max_faim = self.params["faimMax"][1]
        self.mort = False
        self.niveau_fatigue = random.randint(self.params["fatigueMax"][0], self.params["fatigueMax"][1])
        self.max_fatigue = self.params["fatigueMax"][1]
        self.sleeping = False

    def update(self):
        if self.mort:
            return

            # Déplacements seulement si on ne dort pas
        if not self.sleeping:
            if self.acc.length() > self.accMax:
                self.acc.scale_to_length(self.accMax)

            self.vitesse += self.acc
            if self.vitesse.length() > self.vMax:
                self.vitesse.scale_to_length(self.vMax)
            self.acc = Vector2(0, 0)
            self.position += self.vitesse

            self.edge()
        if (pygame.time.get_ticks() - self.last_params_update) > 1000:
            self.last_params_update = pygame.time.get_ticks()

            if self.niveau_faim < self.max_faim:
                self.niveau_faim += 1
                if self.niveau_faim == self.max_faim:
                    self.mort = True
                    return

            if not self.sleeping:
                if self.niveau_fatigue < self.max_fatigue:
                    self.niveau_fatigue += 1
                    if self.niveau_fatigue == self.max_fatigue:
                        self.sleeping = True
            else:
                if self.niveau_fatigue > 0:
                    self.niveau_fatigue -= 1
                    if self.niveau_fatigue == 0:
                        self.sleeping = False
    def show(self):
        core.Draw.circle(self.color, self.position, self.mass)

    def edge(self):
        if self.position.x <= self.mass:
            self.vitesse.x *= -1
        if self.position.x + self.mass >= core.WINDOW_SIZE[0]:
            self.vitesse.x *= -1
        if self.position.y <= self.mass:
            self.vitesse.y *= -1
        if self.position.y + self.mass >= core.WINDOW_SIZE[1]:
            self.vitesse.y *= -1
