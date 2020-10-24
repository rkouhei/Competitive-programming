n = int(input())
u = v = w = []
for i in range(n-1) :
    u, v, w = list(map(int, input().split()))

print(u,v,w)
'''
ans = [0]*n
print(ans)
for i in range(n) :
    if uvw[i][2] % 2 == 0 :
        ans[uvw[i][0]-1] = 1
        ans[uvw[i][1]-1] = 1
    else :
        ans[uvw[i][0]-1] = 0
        ans[uvw[i][1]-1] = 0

print(ans)
'''