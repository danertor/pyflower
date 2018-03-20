import random
from multiprocessing.pool import Pool
from icecream import ic
import multiproc_defs as defs


if __name__ == '__main__':
    pool = Pool()
    to_factor = [random.randint(100000, 50000000) for i in range(20)]
    results = pool.map(defs.prime_factors, to_factor)
    for value, factors in zip(to_factor, results):
        print("The factors of {} are {}".format(value, factors))
