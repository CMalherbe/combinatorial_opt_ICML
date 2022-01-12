### Random Search
import numpy as np
import pdb

def RS(dim, evaluation_budget, objective_function, x_init):

    res = [objective_function.evaluate(x_init)]

    for _ in range(evaluation_budget - 1):
        # Sample a point 
        x_new = list(np.random.choice([0,1], size=dim, replace=True))
        # Evaluate the objective_function
        new_eval = objective_function.evaluate(x_new)
        # Save the new_value
        res.append(new_eval)

    return res


