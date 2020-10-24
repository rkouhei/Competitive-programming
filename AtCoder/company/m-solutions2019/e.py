q = int(input())
s = 1

for i in range(q) :
    x, d, n = map(int, input().split())
    ap = (range(x,x+(n-1)*d+1,d))
    for y in range(1, int(n/2)+1) :
        s *= ap[y-1]
        s *= ap[-y]
        s %= 1000003
    if n % 2 != 0 :
        s *= ap[int(n/2)]
        s %= 1000003
    print(s)
    s = 1