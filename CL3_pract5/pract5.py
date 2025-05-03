import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from deap import base, creator, tools, algorithms
import random
import warnings

# Suppress warnings from MLPRegressor
warnings.filterwarnings("ignore")

# ------------------------------
# 🥥 Step 1: Prepare Sample Data
# (Replace with real spray drying coconut milk data)
# ------------------------------
X = np.random.rand(100, 5)  # 5 input features
y = np.random.rand(100)     # 1 target output

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ------------------------------
# ⚙️ Step 2: Setup Genetic Algorithm with DEAP
# ------------------------------

# Define fitness (minimize MSE)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Genetic representation: [neurons_layer1, neurons_layer2, learning_rate, activation_function_index]
toolbox.register("neurons_layer1", lambda: random.randint(10, 150))
toolbox.register("neurons_layer2", lambda: random.randint(10, 100))
toolbox.register("learning_rate", lambda: round(random.uniform(0.0005, 0.05), 5))
toolbox.register("activation", lambda: random.randint(0, 2))  # 0: relu, 1: tanh, 2: logistic

toolbox.register("individual", tools.initCycle, creator.Individual,
                 (toolbox.neurons_layer1, toolbox.neurons_layer2,
                  toolbox.learning_rate, toolbox.activation), n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Activation index map
activation_map = {0: 'relu', 1: 'tanh', 2: 'logistic'}

# ------------------------------
# 🧠 Step 3: Fitness Function - Train and Evaluate Neural Network
# ------------------------------
def evaluate(ind):
    n1, n2, lr, act_idx = ind
    activation = activation_map[act_idx]

    model = MLPRegressor(hidden_layer_sizes=(int(n1), int(n2)),
                         learning_rate_init=lr,
                         activation=activation,
                         max_iter=300,
                         solver='adam',
                         random_state=42)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return (mse,)

toolbox.register("evaluate", evaluate)

# Crossover, mutation, selection
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=10, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Bound checking after mutation
def check_bounds(ind):
    ind[0] = int(np.clip(ind[0], 10, 150))    # neurons_layer1
    ind[1] = int(np.clip(ind[1], 10, 100))    # neurons_layer2
    ind[2] = round(float(np.clip(ind[2], 0.0005, 0.05)), 5)  # learning_rate
    ind[3] = int(np.clip(ind[3], 0, 2))       # activation
    return ind

# ------------------------------
# 🚀 Step 4: Run the Genetic Algorithm
# ------------------------------
def run_genetic_nn_optimization():
    random.seed(42)
    population = toolbox.population(n=10)  # Small population for demo; increase for better results
    NGEN = 10

    for gen in range(NGEN):
        # Genetic operations
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.2)

        # Bound check
        for ind in offspring:
            check_bounds(ind)

        # Evaluate fitness
        fits = list(map(toolbox.evaluate, offspring))
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit

        # Select next generation
        population = toolbox.select(offspring, k=len(population))

        # Track best result
        best = tools.selBest(population, k=1)[0]
        print(f"Generation {gen+1}: Best MSE = {best.fitness.values[0]:.4f}")

    # Print final best individual
    best = tools.selBest(population, k=1)[0]
    print("\n🎯 Best Parameters Found:")
    print(f"Hidden Layers: ({best[0]}, {best[1]})")
    print(f"Learning Rate: {best[2]}")
    print(f"Activation Function: {activation_map[best[3]]}")
    print(f"Final MSE: {best.fitness.values[0]:.4f}")

# ------------------------------
# 🔁 Step 5: Execute
# ------------------------------
run_genetic_nn_optimization()
