from notepad import Note, Notebook
import string
import random as rd
import time
from functools import wraps


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
               (function.func_name, str(t1 - t0))
               )
        return result

    return function_timer


@fn_timer
def start_test():
    print([note.memo for note in n.search(words[rd.randint(0, N)])])
    print([note.memo for note in n.search(words[rd.randint(0, N)])])
    print([note.memo for note in n.search(words[rd.randint(0, N)])])


if __name__ == "__main__":
    N = 10000
    seed = 1
    words = []
    n = Notebook()
    rd.seed(seed)
    for i in xrange(N):
        word = ''.join(rd.choice(string.ascii_uppercase) for _ in xrange(10))
        words.append(word)
        n.new_note(word)
    start_test()

