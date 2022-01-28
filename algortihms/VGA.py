### Genetic Algorithm
import numpy as np

def VGA(dim, evaluation_budget, objective_function, x_init):
    # Hyper-parameters
    lambda_value = 30
    ite = 0
    all_x = []
    res = []
    proba_cross = 0.37

    # Create the first population
    for i in range(lambda_value):
        x_new = np.random.choice([0,1], size=dim, replace=True)
        all_x.append(x_new)
        new_value = objective_function.evaluate(x_new.tolist())
        ite += 1
        res.append(new_value)

    while True:
        # Roulette wheel selection
        values = np.array(res) - np.min(res) + 0.001
        idx = np.random.choice(range(len(res)), size=lambda_value, replace=True, p = values/sum(values))
        pop_x = [all_x[i] for i in idx]

        # Crossover phase:
        x_sample = crossover(pop_x, proba_cross)

        # Mutation phase
        for i in range(len(pop_x)):
            mutation = np.random.choice([0,1], size=dim, replace=True, p=[1-float(2/dim), float(2/dim)])
            x_new = add_list(x_sample[i], mutation)
            all_x.append(x_new.copy())
            res.append(objective_function.evaluate(x_new))
            ite += 1
            if ite == evaluation_budget:
                return res

    return True




def crossover(pop_x, proba_cross):
    ## Crossover operation
    new_pop = pop_x.copy()
    for i in range(int(len(new_pop)/2)):
        if np.random.rand(1)<proba_cross:
            new_pop[i], new_pop[5 + i] = offspring(new_pop[i], new_pop[5 + i])
    return new_pop

def offspring(x_1, x_2):
    x_1_new = x_1.copy()
    x_2_new = x_2.copy()
    idx = np.random.choice(range(len(x_1_new)))
    x_1 = list(x_1_new[:idx]) + list(x_2_new[idx:])
    x_2 = list(x_2_new[:idx]) + list(x_1_new[idx:])
    return x_1, x_2 

def add_list(list_1,list_2):
    res = []
    for i in range(len(list_1)):
        res.append(1 if list_1[i] != list_2[i] else 0)
    return res
