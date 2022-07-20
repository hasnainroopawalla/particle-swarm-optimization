from typing import Callable, List
import numpy as np

from particle import Particle


W = 0.5
C1, C2 = 0.8, 0.9


class SearchSpace:
    def __init__(
        self,
        fitness_function: Callable[[np.ndarray], float],
        target_value: float,
        target_error: float,
        num_particles: int,
    ) -> None:
        self.fitness_function = fitness_function
        self.target_value = target_value
        self.target_error = target_error
        self.num_particles = num_particles
        self.g_best_value: float = float("inf")
        self.g_best_position: np.ndarray = np.random.uniform(-50, 50, (2,))
        self.particles: List[Particle] = [Particle() for _ in range(num_particles)]

    def set_p_best(self) -> None:
        for particle in self.particles:
            fitness_value = self.fitness_function(particle.position)
            if particle.p_best_value > fitness_value:
                particle.p_best_position, particle.p_best_value = (
                    particle.position,
                    fitness_value,
                )

    def set_g_best(self) -> None:
        for particle in self.particles:
            fitness_value = self.fitness_function(particle.position)
            if self.g_best_value > fitness_value:
                self.g_best_position, self.g_best_value = (
                    particle.position,
                    fitness_value,
                )

    def move_particles(self) -> None:
        for particle in self.particles:
            new_velocity = (
                (W * particle.velocity)
                + (C1 * np.random.uniform())
                * (particle.p_best_position - particle.position)
                + (C2 * np.random.uniform())
                * (self.g_best_position - particle.position)
            )
            particle.velocity = new_velocity
            particle.move()
