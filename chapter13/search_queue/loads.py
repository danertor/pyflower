def search(paths, query_q, results_q):
    lines = []
    for path in paths:
        lines.extend(l.strip() for l in path.open())
    query = query_q.get()
    while query:
        results_q.put([l for l in lines if query in l])
        query = query_q.get()
        