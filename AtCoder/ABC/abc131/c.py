from fractions import gcd
a, b, c, d = map(int, input().split())

cnt = 0
s = b - a + 1
cd = (c*d) // gcd(c,d)

m1 = int((a-1) // c)
m2 = int(b // c)
cnt += (m2-m1)
#print(cnt)

m1 = int((a-1) // d)
m2 = int(b // d)
cnt += (m2-m1)
#print(cnt)

m1 = int((a-1) // cd)
m2 = int(b // cd)
cnt -= (m2-m1)
#print(cnt)

#print(cnt)
print(s - cnt)