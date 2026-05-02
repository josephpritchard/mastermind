import random

colors = [
    "red",
    "blue",
    "yellow",
    "green",
    "black",
    "white"
]

guesses = {}
solution = []

for i in range(4):
    solution.append(random.choice(colors))
print(f"Solution is: {solution}")

def guess(num):
    guess_temp = []
    for i in range(4):
        guess_temp.append(random.choice(colors))
    guesses[num] = guess_temp
    return guess_temp

g = guess(1)
print(f"Guess 1 is {g}")

class Solver:
    def __init__(self):
        self.Count = int(0)
        self.InSolution = []
        self.NotInSolution = []
        self.Solved = bool(False)
        self.Points = 10 - self.Count
        self.A = { "Right": [], "Wrong": [] }
        self.B = { "Right": [], "Wrong": [] }
        self.C = { "Right": [], "Wrong": [] }
        self.D = { "Right": [], "Wrong": [] }

    
    def right_wrong(self, num, color, rw):
        match num:
            case 0: self.A[rw].append(color)
            case 1: self.B[rw].append(color)
            case 2: self.C[rw].append(color)
            case 3: self.D[rw].append(color)
            case _: print("Error with right_wrong method match case.")

solver = Solver()

def compare(num):
    solver.Count = num
    for i in range(4):
        print(i)
        if g[i] == solution[i]:
            solver.right_wrong(i, g[i], "Right")
        if g[i] != solution[i]:
            solver.right_wrong(i, g[i], "Wrong")
        if g[i] in solution:
            solver.InSolution.append(g[i])
        else:
            solver.NotInSolution.append(g[i])
    print(solver.A)
    print(solver.B)
    print(solver.C)
    print(solver.D)
    print(solver.InSolution)
    print(solver.NotInSolution)
compare(1)