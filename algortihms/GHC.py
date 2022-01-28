### Greedy Hill-Climber
import numpy as np
import pdb

def GHC(dim, evaluation_budget, objective_function, x_init):

    ## Initialization and first evaluation
    res = [objective_function.evaluate(x_init)]

    # Save the current point and start the loop
    x_current = x_init.copy()

    for i in range(evaluation_budget - 1):
        x_new = x_current.copy()
        idx_rdm = i % dim
        x_new[idx_rdm] = 1 if x_current[idx_rdm] == 0 else 0
        res.append(objective_function.evaluate(x_new))

        if res[-1] > res[-2]:
            x_current = x_new.copy()

    return res


