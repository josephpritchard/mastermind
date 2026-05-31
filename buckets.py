import random
import clear
import setup
import pegs

# create buckets dictionary
buckets = dict(bbbb = 0, bbb = 0, bb = 0, b = 0, wwww = 0, www = 0, ww = 0, w = 0, bbww = 0, bwww = 0, nobw = 0, bbw = 0, bww = 0, bw = 0)

def find(pegs):
    b = ''
    match pegs:
        case (4, 0): b = 'bbbb'
        case (3, 0): b = 'bbb'
        case (2, 0): b = 'bb'
        case (1, 0): b = 'b'
        case (0, 4): b = 'wwww'
        case (0, 3): b = 'www'
        case (0, 2): b = 'ww'
        case (0, 1): b = 'w'
        case (2, 2): b = 'bbww'
        case (1, 3): b = 'bwww'
        case (0, 0): b = 'nobw'
        case (2, 1): b = 'bbw'
        case (1, 2): b = 'bww'
        case (1, 1): b = 'bw'
    return b



''''
def fill(code, guess):
    g = pegs.get(code, guess)
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
    return g
'''
