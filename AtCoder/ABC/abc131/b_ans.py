n, l = map(int, input().split())
tst_l = []
taste = 0

for i in range(1,n+1) :
    taste += l+i-1
    tst_l.append(l+i-1)
print(taste-min(tst_l, key=abs))