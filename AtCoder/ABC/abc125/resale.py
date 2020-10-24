n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

est = 0

for a in range(n) :
    x = v[a] - c[a]
    if x > 0 :
        est += x

print(est)