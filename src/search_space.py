from typing import List
import numpy as np
import random

from particle import Particle

W = 0.5
c1, c2 = 0.8, 0.9

class SearchSpace:
    def __init__(self, fitness_function, target_value, target_error, num_particles) -> None:
        self.target_value = target_value
        self.target_error = target_error
        self.num_particles = num_particles
        self.g_best_value = float('inf')
        self.g_best_position = np.array([random.random()*50, random.random()*50])
        self.particles: List[Particle] = [Particle() for _ in range(num_particles)]
        self.fitness_function = fitness_function
        
    def set_p_best(self):
        for particle in self.particles:
            fitness_value = self.fitness_function(particle.position)
            if  particle.p_best_value > fitness_value:
                particle.p_best_position, particle.p_best_value = particle.position, fitness_value
    
    def set_g_best(self):
        for particle in self.particles:
            fitness_value = self.fitness_function(particle.position)
            if self.g_best_value > fitness_value:
                self.g_best_position, self.g_best_value = particle.position, fitness_value
        print(self.g_best_value)
    def move_particles(self):
        for particle in self.particles:
            new_velocity = (W * particle.velocity) + \
                           (c1 * np.random.uniform()) * (particle.p_best_position - particle.position) + \
                           (c2 * np.random.uniform()) * (self.g_best_position - particle.position)
            particle.velocity = new_velocity
            particle.move()
            