import numpy as np


class Particle:
    def __init__(self) -> None:
        self.position = np.random.uniform(-50, 50, (2,))
        self.velocity = np.array([0.0, 0.0])
        self.p_best_position = self.position
        self.p_best_value = float("inf")

    def move(self):
        self.position = self.position + self.velocity
