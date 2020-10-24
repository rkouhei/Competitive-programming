n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(n-2) :
  for j in range(i+1,n-1) :
    for k in range(j+1,n) :
      length = a[i] + a[j] + a[k]
      max_num = max(a[i],a[j],a[k])
      rest = length - max_num
      if max_num < rest :
        ans = max(ans,length)

print(ans)