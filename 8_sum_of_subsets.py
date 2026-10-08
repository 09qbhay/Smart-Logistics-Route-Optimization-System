# Sum of Subsets (Unit 4, backtracking): parcels whose weights add up exactly to vehicle capacity
w = [1, 3, 4, 5]
target = 7
found = []
def solve(i, chosen, total, remaining):
    if total == target:
        found.append(chosen[:]); return
    if i == len(w) or total + remaining < target or total > target:
        return                                         # prune
    chosen.append(w[i])
    solve(i + 1, chosen, total + w[i], remaining - w[i])   # include
    chosen.pop()
    solve(i + 1, chosen, total, remaining - w[i])          # exclude
solve(0, [], 0, sum(w))
print("Weights:", w, "| target:", target)
print("Exact-fit subsets:", found)
