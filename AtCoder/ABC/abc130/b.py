n, x = map(int, input().split())
l = list(map(int, input().split()))

d = 0
c = 1
for i in range(1,n+1) :
    d += l[i-1]
    if d <= x :
        c += 1

print(c)