import time
from threads_temperatures import CITIES, TempGetter


threads = [TempGetter(c) for c in CITIES]
start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
    # print(thread.__dict__)
    print("it is {0.temperature:.0f}°C in {0.city}".format(thread))

print("Got {} temps in {} seconds".format(len(threads), time.time() - start))
