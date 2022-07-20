import numpy as np


class Particle:
    def __init__(self) -> None:
        self.position: np.ndarray = np.random.uniform(-50, 50, (2,))
        self.velocity: np.ndarray = np.array([0.0, 0.0])
        self.p_best_position: np.ndarray = self.position
        self.p_best_value: float = float("inf")

    def move(self) -> None:
        self.position = self.position + self.velocity
