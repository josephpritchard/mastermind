import setup
import get_pegs as gp
import minimax as mm

'''
# get user solution and store as user_sol
user_sol = setup.user_sol

# return peg count from first guess as (b#, w#)
guess1 = gp.get_pegs(user_sol, setup.guess1)
'''
reset_buckets = mm.buckets
mm.fill_buckets(setup.user_sol, setup.guess1)
print("reset_buckets is:", reset_buckets)
