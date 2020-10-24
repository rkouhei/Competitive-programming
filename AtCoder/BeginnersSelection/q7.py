n = int(input())
d = []
cnt = 0
tmp = 0

for i in range(n) :
  d.append(int(input()))

d.sort(reverse=True)

for i in range(n) :
  if tmp == d[i] :
    continue
  tmp = d[i]
  cnt += 1

print(cnt)