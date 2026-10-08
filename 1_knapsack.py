# 0/1 Knapsack (Unit 3): choose parcels for one vehicle. weight = parcel weight, value = priority
names = ["P1", "P2", "P3", "P4"]
wt, val, W = [1, 3, 4, 5], [1, 4, 5, 7], 7
n = len(wt)
c = [[0] * (W + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(W + 1):
        if wt[i-1] > w:
            c[i][w] = c[i-1][w]
        else:
            c[i][w] = max(c[i-1][w], val[i-1] + c[i-1][w - wt[i-1]])

print("DP table (rows = parcels, columns = capacity 0..%d)" % W)
for i, row in enumerate(c):
    print("P%d" % i if i else "--", row)

chosen, w = [], W                     # traceback
for i in range(n, 0, -1):
    if c[i][w] != c[i-1][w]:
        chosen.append(names[i-1]); w -= wt[i-1]
print("DP best value:", c[n][W], "| parcels:", chosen[::-1])

tw = tv = 0; gp = []                  # greedy (value/weight) for comparison
for i in sorted(range(n), key=lambda i: -val[i] / wt[i]):
    if tw + wt[i] <= W:
        tw += wt[i]; tv += val[i]; gp.append(names[i])
print("Greedy value :", tv, "| parcels:", gp)
