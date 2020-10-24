import decimal
n, k = map(int, input().split())

cnt = 0
sumcl = []

for i in range(1,n+1) :
    pro = i
    while True :
        if pro < k :
            pro *= 2
            cnt += 1
        else :
            if i == 1 :
                top = cnt
                sumcl.append(1)
            else :
                sumcl.append(2**(top-cnt))
            cnt = 0
            break


print(decimal.Decimal(sum(sumcl)/(n*(2**top))))