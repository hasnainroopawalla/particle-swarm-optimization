from search_space import SearchSpace
from functions import basic


def run_pso(search_space: SearchSpace, max_iterations: int) -> None:
    k = 1
    while k <= max_iterations:
        print(f"iteration: {k}, best solution: {search_space.g_best_value}")
        search_space.set_p_best()
        search_space.set_g_best()
        search_space.move_particles()
        k += 1

    print(
        f"\nFINAL SOLUTION: {search_space.g_best_position}, {search_space.g_best_value}"
    )


if __name__ == "__main__":
    search_space = SearchSpace(fitness_function=basic, num_particles=30)
    run_pso(search_space, max_iterations=50)
