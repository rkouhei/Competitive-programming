import fractions

n = int(input())
a = list(map(int, input().split()))

gcdl = [0]
gcdr = [0]

for i in range(n-1) :
    gcdl.append(fractions.gcd(gcdl[i], a[i]))
    gcdr.append(fractions.gcd(gcdr[i], a[-(i+1)]))
gcdr = gcdr[::-1]

ans = []
for i in range(n) :
    ans.append(fractions.gcd(gcdl[i], gcdr[i]))

print(max(ans))