from multiprocessing import Process, cpu_count
from threading import Thread
import time
import os

class MultiCPU(Process):
    def run(self):
        print(os.getpid())
        for i in range(200000000):
            pass

class ThreadCPU(Thread):
    def run(self):
        print(os.getpid())
        for i in range(200000000):
            pass

def launch_cpu(p):
    procs = [p() for f in range(cpu_count())]
    t = time.time()
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print('With {}: work took {} seconds'.format(p.__class__, time.time() - t))

if __name__ == '__main__':
    launch_cpu(MultiCPU)
    launch_cpu(ThreadCPU)

