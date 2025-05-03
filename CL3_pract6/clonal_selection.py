import numpy as np

# Define the objective function (maximize)
def fitness_function(x):
    # Example: Rastrigin function (commonly used for testing optimization)
    return - (10 * len(x) + sum([xi**2 - 10 * np.cos(2 * np.pi * xi) for xi in x]))

# Parameters
population_size = 20
num_generations = 50
clone_factor = 5
mutation_rate = 0.2
dimension = 2
lower_bound = -5.12
upper_bound = 5.12

# Generate initial population
def initialize_population():
    return np.random.uniform(lower_bound, upper_bound, (population_size, dimension))

# Cloning
def clone_population(population, fitnesses):
    num_clones = clone_factor
    clones = []
    for i in range(len(population)):
        for _ in range(num_clones):
            clones.append(np.copy(population[i]))
    return np.array(clones)

# Mutation
def hypermutation(clones):
    for i in range(len(clones)):
        if np.random.rand() < mutation_rate:
            # Gaussian mutation
            clones[i] += np.random.normal(0, 0.5, size=clones[i].shape)
            # Keep within bounds
            clones[i] = np.clip(clones[i], lower_bound, upper_bound)
    return clones

# Selection: choose best unique antibodies
def select_new_population(clones, fitnesses, size):
    sorted_indices = np.argsort(fitnesses)[::-1]  # descending
    selected = []
    seen = set()
    for idx in sorted_indices:
        candidate = tuple(clones[idx])
        if candidate not in seen:
            selected.append(clones[idx])
            seen.add(candidate)
        if len(selected) == size:
            break
    return np.array(selected)

# Main loop
population = initialize_population()

for generation in range(num_generations):
    fitnesses = np.array([fitness_function(ind) for ind in population])

    clones = clone_population(population, fitnesses)
    clones = hypermutation(clones)
    clone_fitnesses = np.array([fitness_function(ind) for ind in clones])

    population = select_new_population(clones, clone_fitnesses, population_size)

    best_fitness = max(clone_fitnesses)
    print(f"Generation {generation+1}: Best Fitness = {best_fitness:.4f}")

# Final Result
best_solution = population[np.argmax([fitness_function(ind) for ind in population])]
print("\nBest Solution Found:", best_solution)
print("Best Fitness:", fitness_function(best_solution))
