N = int(input())
X = input()
x = int(X, 2)

ans = 0
de = 998244353

if N % 2 == 0 :
  ans = (2 * N) * (x % de) 

print(x)
print (ans)