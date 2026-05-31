# Function to compare guess/user_sol and return peg counts
def get(user_sol, guess):
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
    # Make pegs a list and match to bucket
    pegs = [black_pegs, white_pegs]
    bucket = ''
    match pegs:
            case (4, 0): bucket = 'bbbb'
            case (3, 0): bucket = 'bbb'
            case (2, 0): bucket = 'bb'
            case (1, 0): bucket = 'b'
            case (0, 4): bucket = 'wwww'
            case (0, 3): bucket = 'www'
            case (0, 2): bucket = 'ww'
            case (0, 1): bucket = 'w'
            case (2, 2): bucket = 'bbww'
            case (1, 3): bucket = 'bwww'
            case (0, 0): bucket = 'nobw'
            case (2, 1): bucket = 'bbw'
            case (1, 2): bucket = 'bww'
            case (1, 1): bucket = 'bw'
    return bucket
