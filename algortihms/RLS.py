### Randomized Local Search
import numpy as np

def RLS(dim, evaluation_budget, objective_function, x_init):
    lambda_value = 10
    res = []

    ## Initialization and first evaluation
    res.append(objective_function.evaluate(x_init))

    # Set up the search
    x_current = x_init.copy()
    best_value = res[0]
    ite = 1

    while True:
        for i in range(lambda_value):
            # Define the novel population
            idx_to_flip = np.random.choice(range(dim))
            to_flip = [0]*dim
            to_flip[idx_to_flip] = 1
            x_new = add_list(to_flip, x_current)
            new_value = objective_function.evaluate(x_new)
            res.append(new_value)
            ite += 1
            # Update the running point
            if new_value > best_value:
                x_current = x_new.copy()
            if ite == evaluation_budget:
                return res
    return True



def add_list(list_1,list_2):
    res = []
    for i in range(len(list_1)):
        res.append(1 if list_1[i] != list_2[i] else 0)
    return res

