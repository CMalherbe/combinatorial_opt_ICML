# Code for the paper "Optimistic Tree Search Strategies for Black-Box Combinatorial Optimization"



## Dependencies

Dependencies to install the test problems

> pip install ioh


## Run the experiment

You can run all the experiments on a single problem with any given dimensionality:

> sh sun_exp.sh test_problem dim evaluation_budget

Otherwise, you can run each individual algorithm using the following command:

> python main.py test_problem dim algo evaluation_budget random_seed


## Algorithms implemented

1. SA: Simulated Annealing
2. VGA: Vanilla Genetic Algoirthm
3. VEA: Vanilla Evolutionary Algorithm
4. RS: Random Search
5. RLS: Randomized Local Search
6. GHC: Greedy Hill Climber
7. OCTS: the algorithm from the paper

## Test problems

1. LABS: any dimension
2. Ising: any dimension 
3. MIS: any dimension
4. ConcatenatedTrap: any dimension
5. NKL: any dimension
