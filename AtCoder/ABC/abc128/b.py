n = int(input())

q=[input().split()+[i]for i in range(n)]
for i in range(n):
    q[i][1]=int(q[i][1])
p=sorted(sorted( q ,key=lambda x:x[1],reverse=1),key=lambda x:x[0])
for s,t,r in p:
    print(r+1)

""" 自作の間違えコード
s = []
p = []

for i in range(n) :
    a, b = input().split()
    s.append(a)
    p.append(b)

r = [0]

for i in range(1, n-1) :
    for a in range(i+1) :
        if s[a] > s[i+1] :
            x = s[a]
            s[a] = s[i+1]
            s[i+1] = x
            y = p[a]
            p[a] = p[i+1]
            p[i+1] = y
"""