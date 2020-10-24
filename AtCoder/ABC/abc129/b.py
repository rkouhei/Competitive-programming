n = int(input())
w = list(map(int, input().split()))

s1 = sum(w[0:1])
s2 = sum(w[1:n])
top = abs(s1-s2)

for i in range(2,n) :
    s1 = sum(w[0:i])
    s2 = sum(w[i:n])
    wsum = abs(s1-s2)
    if top > wsum :
        top = wsum

print(top)