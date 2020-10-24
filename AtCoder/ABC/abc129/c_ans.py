n, m = map(int, input().split())
mod = 10**9 + 7

arrs = set([int(input()) for _ in range(m)])
anss = [0, 1]

for i in range(1, n+1) :
    if i in arrs :
        anss.append(0)
    else :
        anss.append((anss[-2] + anss[-1]) % mod)
print(anss)

print(anss[-1] % mod)