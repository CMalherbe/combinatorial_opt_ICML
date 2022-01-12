# Numerical experiments for the paper Optimistic Tree Search Strategies for Black-Box Combinatorial Optimization



## To install

Dependencies to install the test problems

> pip install ioh


## Run the experiment

First activate the virtualenv

> . venv/bin/activate

Then, you can run all the experiments for a single problem with given dimensionality:

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

1. MAXSAT: dim 28/43/60
2. LABS: any dimension
3. Ising: any dimension Ring/Torus/Triangular
4. MIS: any dimension
5. ConcatenatedTrap: any dimension
6. NKL: any dimension
