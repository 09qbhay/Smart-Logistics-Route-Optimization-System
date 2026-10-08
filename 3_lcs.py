# Longest Common Subsequence (Unit 3): common stops, in order, between two route plans
r1 = ["S1", "S2", "S3", "S4", "S2", "S5"]
r2 = ["S2", "S4", "S3", "S5", "S2"]
m, n = len(r1), len(r2)
L = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if r1[i-1] == r2[j-1]:
            L[i][j] = L[i-1][j-1] + 1
        else:
            L[i][j] = max(L[i-1][j], L[i][j-1])
i, j, out = m, n, []
while i > 0 and j > 0:                # traceback
    if r1[i-1] == r2[j-1]:
        out.append(r1[i-1]); i -= 1; j -= 1
    elif L[i-1][j] >= L[i][j-1]:
        i -= 1
    else:
        j -= 1
print("Route 1:", r1)
print("Route 2:", r2)
print("LCS length:", L[m][n], "| common stops in order:", out[::-1])
