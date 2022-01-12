### Random Search
import numpy as np


def OCTS(dim, evaluation_budget, objective_function, x_init):

    ## Define the structures used in the algorithm
    TS = dict()
    for L in range(1, dim):
        TS[L] = dict()

    ## Init
    res = []
    left_init = add_list(x_init, get_x_value(1,0,dim))
    right_init = add_list(x_init, get_x_value(1,1,dim))
    left_value = objective_function.evaluate(left_init)
    right_value = objective_function.evaluate(right_init)
    res.append(left_value)
    res.append(right_value)
    ite = 2
    TS[1][0] = left_value
    TS[1][1] = right_value


    while ite < evaluation_budget:
        # Get the pareto nodes
        v_max = -np.inf
        pareto_nodes = []
        for L in range(1, dim):
            if TS[L]:
                idx_max =  max(TS[L], key=TS[L].get)
                value = TS[L][idx_max]
                if value >= v_max:
                    v_max = value
                    pareto_nodes.append((L, idx_max))
        #pdb.set_trace()
        # Evaluate the pareto nodes
        for (L,i) in pareto_nodes:
            # Evaluate right children
            x_new = add_list(x_init, get_x_value(L+1, 2*i+1, dim))
            right_value = objective_function.evaluate(x_new)
            res.append(right_value)
            ite +=1 
            if L < dim-1:
                TS[L+1][2*i] = TS[L][i]
                TS[L+1][2*i+1] = right_value
            del TS[L][i]

            if ite == evaluation_budget:
                return res

    return True




def add_list(list_1,list_2):
    res = []
    for i in range(len(list_1)):
        res.append(1 if list_1[i] != list_2[i] else 0)
    return res


def get_x_value(l,i,dim):
    binary_representation = format(i, 'b').zfill(l) + "0"*(dim - l) 
    return [int(i) for i in binary_representation]
