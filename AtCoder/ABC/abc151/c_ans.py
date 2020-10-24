n, m = map(int, input().split())

p = [0]*(n+1)
q = [False]*(n+1)

for _ in range(m) :
  v,s = input().split()
  v = int(v)
  if q[v] : continue
  if s[0] == 'A' : q[v] = True
  else : p[v] += 1

print(sum(q), sum(p[i] for i in range(n+1) if q[i]))