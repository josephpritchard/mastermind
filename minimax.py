import random
import clear
import setup
import get_pegs as gp

'''
# get user solution and store as user_sol
user_sol = setup.user_sol

guess1 = gp.get_pegs(user_sol, [setup.c[0], setup.c[0], setup.c[1], setup.c[1]])
'''


pool      = setup.all_codes
pool_neg  = []
attempts  = 0

# create buckets dictionary
buckets = dict(bbbb = 0, bbb = 0, bb = 0, b = 0, wwww = 0, www = 0, ww = 0, w = 0, bbww = 0, bwww = 0, nobw = 0, bbw = 0, bww = 0, bw = 0)

def fill_buckets(code, guess):
    global buckets
    g = gp.get_pegs(code, guess)
    match g:
        case (4, 0): buckets['bbbb'] += 1
        case (3, 0): buckets['bbb'] += 1
        case (2, 0): buckets['bb'] += 1
        case (1, 0): buckets['b'] += 1
        case (0, 4): buckets['wwww'] += 1
        case (0, 3): buckets['www'] += 1
        case (0, 2): buckets['ww'] += 1
        case (0, 1): buckets['w'] += 1
        case (2, 2): buckets['bbww'] += 1
        case (1, 3): buckets['bwww'] += 1
        case (0, 0): buckets['nobw'] += 1
        case (2, 1): buckets['bbw'] += 1
        case (1, 2): buckets['bww'] += 1
        case (1, 1): buckets['bw'] += 1
    print("Buckets:", buckets)
    return buckets

'''
# Updated evaluate function
def evaluate2(solution, guess1):
    largest_bucket = 0
    buckets = {}
    largest_bucket_temp = 0
    # Enumerate (and clear) all possible peg outcomes
    def reset_dict():
        largest_bucket_temp = 0


# Compare guess/all_codes
# Add all matching results to pool
def evaluate(solution, guess_var):
    for code in all_codes:
        g = guess(solution, guess_var)
        h = guess(code, guess_var)
        if h != g:
            pool.remove(code)
            pool_neg.append(code)
    print(f"Pool length is: {len(pool)}")
    if attempts <= 4:
        return g[0], random.choice(pool_neg)
    else:
        return g[0], random.choice(pool)


    reset_dict()

    # Assess guess and shrink pool size
    for code in all_codes:
        g = guess(solution, guess1)
        h = guess(code, guess1)
        if h != g:
            pool.remove(code)
            pool_neg.append(code)

    def evaluate2a():
        print("Quarter pool is: ", len(pool) / 4)
        if attempts <= 2:
            q = random.choice(pool_neg)
        else:
            q = random.choice(pool)


    evaluate2a()
    for value in buckets.values():
        if value > largest_bucket_temp:
            largest_bucket = value
    print(f"Largest bucket is: {largest_bucket}")
    if largest_bucket > len(pool) / 8:
        reset_dict()
        evaluate2a()

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


evaluate2(solution, first_guess)

print(f"Starting pool is: {len(all_codes)}")
print(f"Guess #1 is: {first_guess}")
tries[0] = guess(solution, first_guess)
evals[0] = evaluate(solution, first_guess)
print(f"Guess #2 is: {second_guess}")
tries[1] = guess(solution, second_guess)
evals[1] = evaluate(solution, second_guess)
print(f"Guess #3 is: {third_guess}")
tries[2] = guess(solution, third_guess)
evals[2] = evaluate(solution, third_guess)

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

'''
