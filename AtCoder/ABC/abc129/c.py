import math, sys

def combination(n,r) :
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

n, m = map(int, input().split())
a = list()
total = 1

for i in range(m) :
    a.append(int(input()))

for i in range(m+1) :
    if i == 0 :
        nos = a[i] - 1
    elif i == m :
        nos = n - (a[i-1]+1)
    else : 
        nos = (a[i]-1) - (a[i-1]+1)
        if nos < 0 :
            print(0)
            sys.exit()
    
    hoge = 1
    if nos % 2 == 0 : 
        for x in range(1,int(nos/2)+1) :
            if nos - (2+x) <= x+1 :
                hoge += 1
            else :
                hoge += combination(nos-x,x)
    else :
        for x in range(int(nos/2)) :
            hoge += combination(nos-(2+x),x+1)
    print(hoge)
    total *= hoge
    total %= 1000000007

'''
a += 1
rmn = n-a
hoge = 1
if rmn == 2 :
    hoge += 1
else :
    for x in range(int(rmn/2)) :
        hoge += combination(rmn-(2+x),x+1)
total *= hoge
'''
total = total % 1000000007
print(total)

'''
hoge = 1
for i in range(1,11) :
    print(combination(20-i,i))
    hoge += combination(20-i,i)

print(hoge)
'''

'''
4(3)3/2=1

123
13
23

5(4)4/2=2

1 + a-2C1+ a-3C2 + ... a-2Ca(%が0なら+1)

1234
124
134
234
24

100 5 
1
23
45

1
20/2 = 10
1+19C1+18C2+17C3...10C10
1 19 153
'''