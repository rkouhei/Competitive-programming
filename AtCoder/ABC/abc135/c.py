n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
flag = False
for i in range(n) :
  if a[i] > b[i] :
    a[i] -= b[i]
    cnt += b[i]
    b[i] = 0
  elif a[i] == b[i]:
    cnt += b[i]
    b[i] = 0
    a[i] = 0
  else :
    b[i] -= a[i]
    cnt += a[i]
    a[i] = 0
    flag = True

  if flag :
    if a[i+1] > b[i] :
      a[i+1] -= b[i]
      cnt += b[i]
      b[i] = 0
    elif a[i+1] == b[i]:
      cnt += b[i]
      b[i] = 0
      a[i+1] = 0
    else :
      b[i] -= a[i+1]
      cnt += a[i+1]
      a[i+1] = 0
    flag = False

print(cnt)