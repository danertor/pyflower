import random
from multiprocessing.pool import Pool
import multiproc_defs as defs


if __name__ == '__main__':
    pool = Pool()
    to_factor = [random.randint(100000, 50000000) for i in range(20)]
    results = pool.map_async(defs.prime_factors, to_factor)
    while not results.ready():
        results.wait(timeout=0)
    for value, factors in zip(to_factor, results.get()):
        print("The factors of {} are {}".format(value, factors))
