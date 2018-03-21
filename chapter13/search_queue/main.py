from loads import search


if __name__ == '__main__':
    from multiprocessing import Process, Queue, cpu_count
    from pathlib import Path
    cpus = cpu_count()
    pathnames = [f for f in Path('.').glob('*.py') if f.is_file]
    print(pathnames)
    paths = [pathnames[i::cpus] for i in range(cpus)]
    query_queues = [Queue() for p in range(cpus)]
    results_queue = Queue()

    search_procs = [
        Process(target=search, args=(p, q, results_queue))
        for p, q in zip(paths, query_queues)
        ]
    for proc in search_procs: proc.start()

    for q in query_queues:
        q.put("def")
        q.put(None)  # Signal process termination

    for i in range(cpus):
        for match in results_queue.get():
            print(match)

    for proc in search_procs: proc.join()

