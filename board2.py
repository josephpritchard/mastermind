import random
import os
import time

c = [
        "red",
        "blue",
        "yellow",
        "green",
        "black",
        "white"
        ]

# Create and fill all_codes list with numbers
all_codes = []
for i in range(len(c)):
    for j in range(len(c)):
        for k in range(len(c)):
            for l in range(len(c)):
                code = [c[i], c[j], c[k], c[l]]
                all_codes.append(code)

os.system('clear')
print("= = = = = = = = = = =")
time.sleep(1)
print("= = W E L C O M E = =")
time.sleep(1)
print("= = = = T   O = = = =")
time.sleep(1)
print(" M A S T E R M I N D")
time.sleep(1)
print("= = S O L  V E R = =")
time.sleep(1)
print("= = = = = = = = = = =")
time.sleep(2)

def get_input():
    os.system('clear')
    print("Enter a four-color code and the program will solve it.")
    print("The possible choices are the following colors:")
    print(c)
    sol = []
    for i in range(4):
        while True:
            print(f"Enter color #{i+1}: ")
            a = input().strip().lower()
            if a in c:
                sol.append(a)
                break
            else:
                print(f"Invalid input: {a}")
                print("Please try again.")
    return sol

solution = get_input()
print(f"Your code is: {solution}")

# Function to compare guess/solution and return peg counts
def guess(solution, guess):
    marked = [ None, None, None, None ]
    black_pegs = 0
    white_pegs = 0

    for i in range(4):
        # Check for black pegs and add to marked
        if guess[i] == solution[i]:
            black_pegs += 1
            marked[i] = "Marked"
            # Check for white pegs and add to marked            
            if guess[i] in solution:
                for j in range(4):
                    if guess[i] == solution[j]:
                        if marked[j] == None:
                            white_pegs += 1
                            marked[j] = "Marked"
    return black_pegs, white_pegs

pool      = all_codes
pool_neg  = []
attempts = 0

# Compare guess/all_codes
# Add all matching results to pool
def evaluate(solution, guess_list):
    for code in all_codes:
        g = guess(solution, guess_list)
        h = guess(code, guess_list)
        if h[0] != g[0]:
            pool.remove(code)
            pool_neg.append(code)
    print(f"Pool length is: {len(pool)}")
    if attempts <= 4:
        return g[0], random.choice(pool_neg)
    else:
        return g[0], random.choice(pool)

first_guess     = [ c[0], c[0], c[1], c[1] ]
second_guess    = [ c[2], c[2], c[3], c[3] ]
third_guess     = [ c[4], c[4], c[5], c[5] ]
tries = [ 
         None, None, None, None, None, None,
         None, None, None, None, None, None,
         None, None, None, None, None, None 
         ]
evals = [ 
         None, None, None, None, None, None,
         None, None, None, None, None, None,
         None, None, None, None, None, None 
         ]


print(f"Starting pool is: {len(all_codes)}")
print(f"Guess #1 is: {first_guess}")
tries[0] = guess(solution, first_guess)
evals[0] = evaluate(solution, first_guess)
print(f"Guess #2 is: {second_guess}")
tries[1] = guess(solution, second_guess)
evals[1] = evaluate(solution, second_guess)
'''print(f"Guess #3 is: {third_guess}")
tries[2] = guess(solution, third_guess)
evals[2] = evaluate(solution, third_guess)
'''

num = 1
attempts = 2
while True:
    if len(pool) > 1:
        num += 1
        attempts += 1
        print(f"Guess #{attempts} is: {evals[num-1][1]}")
        tries[num] = guess(solution, evals[num-1][1])
        if tries[num][0] == 4:
            print(f"Solution is: {solution}")
            print(f"Solution was found in {attempts} attempts.")
            break
        else:
            evals[num] = evaluate(solution, evals[num-1][1])
    else:
        num += 1
        attempts += 1
        print(f"Guess #{attempts} is: {evals[num-1][1]}")
        print(f"Solution is: {solution}")
        print(f"Solution was found in {attempts} attempts.")
        break
