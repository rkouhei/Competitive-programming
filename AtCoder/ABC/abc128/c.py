from numpy import *
n , m = map(int, input().split())
l = []

for i in range(m) :
    *a, = map(int, input().split())
    l.append(a[1:])
*p, = map(int, input().split())


ans = 0
for t in range(2**n) :
    tmp = array([t>>s&1 for s in range(n)])
    if p == [sum(tmp[array(i)-1])%2 for i in l] :
        ans+=1

print(ans)