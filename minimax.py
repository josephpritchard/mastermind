import buckets as b
import pegs
from setup import all_codes

minimax = dict(code = [], size = len(all_codes))

def get(pool):
    global minimax
    buckets1 = b.buckets
    for code in all_codes:
        for k in buckets1.keys():
            buckets1[k] = 0
        buckets2 = 0
        for p in pool:
            p1 = pegs.get(code, p)
            buckets1[p1] += 1
        for v in buckets1.values():
            if v > buckets2:
                buckets2 = v
        if buckets2 < minimax['size']:
            minimax['size'] = buckets2
            minimax['code'] = code
    return minimax
