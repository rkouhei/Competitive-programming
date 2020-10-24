S = input()
P = 2019
ans = 0
count = [1] + [0] * 2018
u = 0

for i, s in enumerate(reversed(S)):
    u = (int(s) * pow(10, i, P) + u) % P
    ans += count[u]
    count[u] += 1

print(ans)