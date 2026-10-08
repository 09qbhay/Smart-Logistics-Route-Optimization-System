# N-Queens (Unit 4, backtracking): conflict-free placement (e.g. vehicles in loading bays)
N = 6
cols, sols = [], []
def safe(r, c):
    return all(c != cc and abs(c - cc) != r - rr for rr, cc in enumerate(cols))
def place(r):
    if r == N:
        sols.append(cols[:]); return
    for c in range(N):
        if safe(r, c):
            cols.append(c); place(r + 1); cols.pop()   # backtrack
place(0)
print("N =", N, "| total solutions:", len(sols))
print("First solution (row -> column):", sols[0])
for c in sols[0]:
    print(" ".join("Q" if k == c else "." for k in range(N)))
