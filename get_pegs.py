# Function to compare guess/user_sol and return peg counts
def get_pegs(user_sol, guess):
    black_pegs = 0
    white_pegs = 0

    # these could be used for easy mode
    g_marked = [ None, None, None, None ]
    s_marked = [ None, None, None, None ]

    # Check for black pegs and add to marked
    for i in range(4):
        if guess[i] == user_sol[i]:
            black_pegs += 1
            g_marked[i] = s_marked[i] = "b"

    # Check for white pegs and add to marked
    for i in range(4):
        if g_marked[i] == None and guess[i] in user_sol:
            for j in range(4):
                if guess[i] == user_sol[j] and s_marked[j] == None:
                    white_pegs += 1
                    g_marked[i] = s_marked[j] = "w"
                    break

    # return peg counts
    return black_pegs, white_pegs
