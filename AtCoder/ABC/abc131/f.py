n = int(input())
X = [[],[],[]]
Y = [[],[],[]]
INF = 10**18

for i in range(n) :
    x,y,d = input().split()
    x,y = int(x), int(y)
    if d == 'L' :
        X[-1].append(x)
        Y[0].append(y)
    elif d == 'R' :
        X[1].append(x)
        Y[0].append(y)
    elif d == 'U' :
        X[0].append(x)
        Y[1].append(y)
    else :
        X[0].append(x)
        Y[-1].append(y)

#print(X)
#print(Y)

for i in [-1,0,1] :
    X[i] = [min(X[i] + [INF]), max(X[i] + [-INF])]
    Y[i] = [min(Y[i] + [INF]), max(Y[i] + [-INF])]

#print(X)
#print(Y)
