# Matrix Chain Multiplication (Unit 3): cheapest order to combine chained cost matrices
p = [30, 35, 15, 5, 10, 20, 25]       # matrix Ai has size p[i-1] x p[i]
n = len(p) - 1
m = [[0] * (n + 1) for _ in range(n + 1)]
s = [[0] * (n + 1) for _ in range(n + 1)]
for length in range(2, n + 1):
    for i in range(1, n - length + 2):
        j = i + length - 1
        m[i][j] = float("inf")
        for k in range(i, j):
            cost = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
            if cost < m[i][j]:
                m[i][j], s[i][j] = cost, k

def paren(i, j):
    if i == j:
        return "A%d" % i
    return "(" + paren(i, s[i][j]) + paren(s[i][j] + 1, j) + ")"

print("Dimensions:", p)
print("Minimum multiplications:", m[1][n])
print("Best order:", paren(1, n))
