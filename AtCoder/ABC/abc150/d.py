N, M = map(int, input().split())
a = list(map(int, input().split()))

a = list(set(a))
l = []
for i in range(len(a)) :
  tmp = int(a[i] * 1.5)
  x = range(tmp,M,a[i])
  l.append(x)

res = set(l[0])
for i in range(1,len(a)) :
  res = set(res) & set(l[i])

print(len(res))