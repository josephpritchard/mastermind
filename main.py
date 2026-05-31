from setup import all_codes, user_sol, c
import pegs
import buckets as b
import pool
import minimax as mm
import random

print("\nColor choices were:", c)
print("\nThere are {} total possible solutions.\n".format(len(all_codes)))

# Function to solve
def solve(pool0):
    # Using only one pool variable
    global pool_master
    # Get next guess
    mm1 = mm.get(pool0)
    # Create new pool of possible solutions
    pool_master = pool.get(pool0, mm1['code'])
    # Check if the pool is equal to 1
    if len(pool_master) == 1:
        print("Guess {}: {}".format(attempts, pool_master[0]))
        print("Solved in {} attempts!".format(attempts))
    else:
        print("Guess {}: {}".format(attempts, mm1['code']))

# Get random code for first guess
r = random.randint(0, len(all_codes) - 1)
print("Guess 1:", all_codes[r])

# Run first guess outside of while loop
pool_master = pool.get(all_codes, all_codes[r])
attempts = 1

# While loop that uses solve function to solve
while len(pool_master) > 1:
    attempts += 1
    solve(pool_master)
