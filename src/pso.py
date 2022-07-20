from search_space import SearchSpace
from functions import basic


MAX_ITERATIONS = 50

search_space = SearchSpace(
    fitness_function=basic, target_value=1, target_error=1e-6, num_particles=30
)

k = 0
while k < MAX_ITERATIONS:
    search_space.set_p_best()
    search_space.set_g_best()

    if (
        abs(search_space.g_best_value - search_space.target_value)
        <= search_space.target_error
    ):
        break

    search_space.move_particles()
    k += 1

print(
    f"Iterations: {k}, Best Solution: {search_space.g_best_position}, Value: {search_space.g_best_value}"
)
