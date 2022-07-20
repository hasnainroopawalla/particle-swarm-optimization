from search_space import SearchSpace
from functions import basic

def error_criteria_attained(g_best_value, target_value, target_error):
    return abs(g_best_value - target_value) <= target_error

k = 0
MAX_ITERATIONS = 50

search_space = SearchSpace(fitness_function=basic, target_value=1, target_error=1e-6, num_particles=30)

while k <  MAX_ITERATIONS:
    search_space.set_p_best()
    search_space.set_g_best()

    if error_criteria_attained(search_space.g_best_value, search_space.target_value, search_space.target_error): 
        break
    
    search_space.move_particles()
    k += 1
    
print(f'Iterations: {k}, Best Solution: {search_space.g_best_position}')