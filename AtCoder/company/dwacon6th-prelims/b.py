N = int(input())
x = list(map(int, input().split()))
mod = 10**9 + 7

p = [1,1]
q = [1,1]
res = 0
an = 0

for j in range(1,N+1) :
  q.append((q[-1]*j)%mod)
  p.append((p[-1]*(N-j))%mod)

for i in range(1,N) :
  res = (res*i+q[i])%mod
  an = (an+(x[i]-x[i-1])*res*p[N-i])%mod

print(p)
print(q)

# s = []
# for i in range(N-1) :
#   tmp = []
#   for j in range(i+1, N) :
#     tmp.append(x[j]-x[i])
#   s.append(tmp)

# s.reverse()
# result = 0
# for i in s :
#   result *= len(i)
#   result += sum(i)
#   result %= mod

# print(result)
