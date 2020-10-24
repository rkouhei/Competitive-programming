N = int(input())
a = list(map(int, input().split()))

cnt = 0
num = 1
for i in range(N) :
  if a[i] == cnt+1 :
    cnt += 1

if cnt == 0 :
  print(-1)
else :
  print(N-cnt)