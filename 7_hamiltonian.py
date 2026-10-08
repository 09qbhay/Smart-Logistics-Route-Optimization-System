# Hamiltonian Cycle (Unit 4, backtracking): route visiting every stop once and returning to depot
g = [[0, 1, 0, 1, 0],
     [1, 0, 1, 1, 1],
     [0, 1, 0, 0, 1],
     [1, 1, 0, 0, 1],
     [0, 1, 1, 1, 0]]
V = len(g)
path = [0]
def ok(v, pos):
    return g[path[pos-1]][v] == 1 and v not in path
def solve(pos):
    if pos == V:
        return g[path[-1]][path[0]] == 1
    for v in range(1, V):
        if ok(v, pos):
            path.append(v)
            if solve(pos + 1):
                return True
            path.pop()                                 # backtrack
    return False
if solve(1):
    print("Hamiltonian cycle:", " -> ".join(map(str, path + [path[0]])))
else:
    print("No Hamiltonian cycle")
