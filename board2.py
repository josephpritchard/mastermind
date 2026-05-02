import random

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

solution = [ c[1], c[5], c[3], c[2] ]

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


candidate_pool  = all_codes
# Compare guess/all_codes
# Add all matching results to candidate_pool
def evaluate(solution, guess_list):
    for code in all_codes:
        g = guess(solution, guess_list)
        h = guess(code, guess_list)
        if h[0] != g[0]:
            candidate_pool.remove(code)
    print(f"Pool length is: {len(candidate_pool)}")
    print(f"g is {g}")
    print(f"h is {h}")
    return g[0], random.choice(candidate_pool)


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
tries[0] = guess(solution, first_guess)
evals[0] = evaluate(solution, first_guess)
tries[1] = guess(solution, second_guess)
evals[1] = evaluate(solution, second_guess)
tries[2] = guess(solution, third_guess)
evals[2] = evaluate(solution, third_guess)

num = 2
attempts = 3
while True:
    if len(candidate_pool) > 1:
        num += 1
        attempts += 1
        tries[num] = guess(solution, evals[num-1][1])
        if tries[num][0] == 4:
            print(f"Solution is: {solution}")
            print(f"Solution was found in {attempts} attempts.")
            break
        else:
            evals[num] = evaluate(solution, evals[num-1][1])
            print(tries[num])
            print(evals[num])
    else:
        print(f"Solution is: {solution}")
        print(f"Solution was found in {attempts} attempts.")
        break
