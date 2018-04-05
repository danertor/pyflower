import asyncio
import random

@asyncio.coroutine
def random_sleep(counter):
    delay = random.random() * 5
    print("{} sleeps for {:.2f} seconds".format(counter, delay))
    yield from asyncio.sleep(delay)
    print("{} awakens".format(counter))


@asyncio.coroutine
def five_sleepers():
    print("Creating five tasks")
    tasks = [asyncio.async(random_sleep(i)) for i in range(5)] # async don't execute the coroutine code yet.
    print("Sleeping after starting five tasks")
    yield from asyncio.sleep(2)
    print("Waking and waiting for five tasks")
    yield from asyncio.wait(tasks)

# the future is five_sleepers. We create an event loop and instructs to run the future until it is finished.
asyncio.get_event_loop().run_until_complete(five_sleepers())
# after the future has finished, the loop will exit.
print("Done five tasks")
