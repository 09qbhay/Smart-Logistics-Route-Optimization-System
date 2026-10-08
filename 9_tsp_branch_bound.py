# Branch and Bound - TSP (Unit 4): cheapest delivery tour using cost-matrix reduction
import heapq, itertools
INF = float("inf")
M = [[INF, 20, 30, 10, 11],
     [15, INF, 16, 4, 2],
     [3, 5, INF, 2, 4],
     [19, 6, 18, INF, 3],
     [16, 4, 7, 16, INF]]
N = len(M)

def reduce(m):                        # row then column reduction, returns reduction cost
    cost = 0
    for i in range(N):
        r = min(m[i])
        if 0 < r < INF:
            cost += r; m[i] = [x - r for x in m[i]]
    for j in range(N):
        c = min(m[i][j] for i in range(N))
        if 0 < c < INF:
            cost += c
            for i in range(N):
                m[i][j] -= c
    return cost

root = [row[:] for row in M]
root_cost = reduce(root)
print("Root lower bound (after reduction):", root_cost)
tick = itertools.count()
heap = [(root_cost, next(tick), [0], root)]
expanded = 0
while heap:
    cost, _, path, m = heapq.heappop(heap)             # least-cost live node
    if len(path) == N:
        print("Optimal tour:", " -> ".join(map(str, path + [0])), "| cost:", cost)
        break
    expanded += 1
    i = path[-1]
    for j in range(N):
        if j not in path:
            c = [row[:] for row in m]
            for k in range(N):
                c[i][k] = INF; c[k][j] = INF
            c[j][0] = INF
            child = cost + m[i][j] + reduce(c)
            if len(path) == 1:
                print("  child node", j, "cost", child)
            heapq.heappush(heap, (child, next(tick), path + [j], c))
print("Nodes expanded:", expanded, "| brute-force tours would be", len(list(itertools.permutations(range(1, N)))))
best = min(sum(M[a][b] for a, b in zip((0,) + p, p + (0,))) for p in itertools.permutations(range(1, N)))
print("Brute-force check, minimum cost:", best)
