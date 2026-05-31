from setup import user_sol
import pegs

def get(pool, guess):
    pool1 = []
    pegs1 = pegs.get(user_sol, guess)
    for p in pool:
        p1 = pegs.get(p, guess)
        if p1 == pegs1:
            pool1.append(p)
    return pool1
