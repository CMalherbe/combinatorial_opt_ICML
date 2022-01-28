### Evolutionary Strategy
import numpy as np

def VEA(dim, evaluation_budget, objective_function, x_init):
    lambda_value = 10

    ## Initialization and first evaluation
    res = []
    res.append(objective_function.evaluate(x_init))

    # Set up the search
    x_current = x_init.copy()
    best_value = res[0]
    ite = 1

    while True:
        x_static = x_current.copy()
        for i in range(lambda_value):
            # Define the novel population
            to_flip = list(np.random.choice([0,1], size=dim, replace=True, p=[1-float(1/dim), float(1/dim)]))
            x_new = add_list(to_flip, x_static)
            new_value = objective_function.evaluate(x_new)
            res.append(new_value)
            ite += 1
            # Update the running point
            if new_value > best_value:
                x_current = x_new.copy()
                best_value = new_value
            if ite == evaluation_budget:
                return res
    return True



def add_list(list_1,list_2):
    res = []
    for i in range(len(list_1)):
        res.append(1 if list_1[i] != list_2[i] else 0)
    return res

