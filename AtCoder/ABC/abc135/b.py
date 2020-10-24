n = int(input())
p = list(map(int, input().split()))

# x = range(1,n+1)

cnt = 0
for i in range(1,n+1) :
  if p[i-1] == i :
    continue
  else :
    cnt += 1

if cnt == 2 or cnt == 0 :
  print('YES')
else : 
  print('NO')