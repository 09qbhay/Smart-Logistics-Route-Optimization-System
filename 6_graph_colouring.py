# Graph Colouring (Unit 4, backtracking): deliveries with overlapping time windows get different slots
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
V, m = 5, 3
adj = [[0] * V for _ in range(V)]
for a, b in edges:
    adj[a][b] = adj[b][a] = 1
colour = [0] * V
def solve(v):
    if v == V:
        return True
    for c in range(1, m + 1):
        if all(not (adj[v][u] and colour[u] == c) for u in range(V)):
            colour[v] = c
            if solve(v + 1):
                return True
            colour[v] = 0                              # backtrack
    return False
if solve(0):
    for v in range(V):
        print("Delivery D%d -> Slot %d" % (v, colour[v]))
else:
    print("No colouring with", m, "slots")
