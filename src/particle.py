import numpy as np
import random

class Particle:
    def __init__(self) -> None:
        self.position = np.array([(-1) ** (bool(random.getrandbits(1))) * random.random()*50, (-1)**(bool(random.getrandbits(1))) * random.random()*50])# np.random.uniform(-50, 50, (2,))
        self.velocity = np.array([0.0, 0.0])
        self.p_best_position = self.position
        self.p_best_value = float('inf')
        
    def move(self):
        self.position += self.velocity
