N, K, M = map(int, input().split())
A = list(map(int, input().split()))

must = (M * N) - sum(A)
if must < 0 : must = 0

if must > K :
  print(-1)
else :
  print(must)