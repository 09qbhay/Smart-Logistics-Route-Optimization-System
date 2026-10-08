# Resource Allocation (Unit 3, multistage DP): share W vehicle units among delivery zones
zones = ["Zone A", "Zone B", "Zone C"]
profit = [[0, 3, 5, 6, 7, 8],      # profit[zone][units given]
          [0, 2, 5, 7, 8, 9],
          [0, 4, 6, 7, 8, 8]]
W, n = 5, len(zones)
f = [[0] * (W + 1) for _ in range(n + 1)]
pick = [[0] * (W + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(W + 1):
        best = -1
        for x in range(j + 1):
            v = profit[i-1][x] + f[i-1][j - x]
            if v > best:
                best, pick[i][j] = v, x
        f[i][j] = best

print("f[stage][units]:")
for i, row in enumerate(f):
    print(i, row)
j, alloc = W, []
for i in range(n, 0, -1):
    alloc.append(pick[i][j]); j -= pick[i][j]
print("Best total benefit:", f[n][W])
for z, a in zip(zones, alloc[::-1]):
    print(z, "->", a, "vehicle units")
