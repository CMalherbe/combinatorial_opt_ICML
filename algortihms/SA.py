### Random Search
import numpy as np

def SA(dim, evaluation_budget, objective_function, x_init):
    # Set the initial temperature and variables
    res = []
    T = 1
    annealing_rate = (0.000001)**(1/float(evaluation_budget))
    T_min = 0.00001#max(0.9**evaluation_budget, 0.00001)
    #cool = lambda T: (0.000001)**(1/float(evaluation_budget))*T#T: np.exp(Tfactor/budget)*T#(0.000001)**(1/float(budget))*T#0.9 * T#

    # Set initial condition and evaluate objective
    #x_init = list(np.random.choice([0,1], size=dim, replace=True))
    x_current   = x_init.copy()
    old_obj = objective_function.evaluate(x_init)
    best_obj = old_obj
    res.append(old_obj)

    # Sample all the random variables at the beginning
    idx_to_flip = np.random.choice(range(dim), evaluation_budget)
    uniforms = np.random.rand(evaluation_budget)

    # Run simulated annealing
    for i in range(evaluation_budget-1):
	    # Decrease T according to cooling schedule
        T = T * annealing_rate#cool(T)
        x_new = x_current.copy()
        #idx_to_flip = np.random.choice(range(dim))
        x_new[idx_to_flip[i]] = int(1 - x_new[idx_to_flip[i]])

        # Evaluate objective function
        new_obj = objective_function.evaluate(x_new)
        res.append(new_obj)

        # Update current solution iterate
        Temperature = max(T, T_min)
        if (new_obj > old_obj) or (uniforms[i] < np.exp( (new_obj - old_obj)/( Temperature * (abs(np.mean(res)) +0.00001) ))):
            x_current = x_new.copy()
            old_obj = new_obj

        # Update best solution
        if new_obj > best_obj:
            best_obj = new_obj

    return res

def add_list(list_1,list_2):
    res = []
    for i in range(len(list_1)):
        res.append(1 if list_1[i] != list_2[i] else 0)
    return res
