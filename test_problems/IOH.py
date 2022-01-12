from ioh import get_problem

class LABS:
    def __init__(self, dim):
        self.name = "LABS"
        self.dim = dim
        self.F = get_problem(18, 1, dim, "PBO")
    def evaluate(self, x):
        return self.F(x)

class IsingRing:
    def __init__(self, dim):
        self.name = "IsingRing"
        self.dim = dim
        self.F = get_problem(19, 1, dim, "PBO")
    def evaluate(self, x):
        return self.F(x)

class MIS:
    def __init__(self, dim):
        self.name = "MIS"
        self.dim = dim
        self.F = get_problem(22, 1, dim, "PBO")
    def evaluate(self, x):
        return self.F(x)

class ConcatenatedTrap:
    def __init__(self, dim):
        self.name = "ConcatenatedTrap"
        self.dim = dim
        self.F = get_problem(24, 1, dim, "PBO")
    def evaluate(self, x):
        return self.F(x)

class NKL:
    def __init__(self, dim):
        self.name = "NKL"
        self.dim = dim
        self.F = get_problem(25, 1, dim, "PBO")
    def evaluate(self, x):
        return self.F(x)
