def find(index, N) :
  max_cnt = 0
  next_N = L[index]
  if next_N == 1 :
    # print(C[index])
    return C[index]
  next_index = [j for j, x in enumerate(R) if x >= next_N and x < N]
  if not next_index :
    return 1000000000
  if len(next_index) > 1 :
    for k in range(len(next_index)) :
      cnt = 0
      cnt += C[index]
      cnt += find(next_index[k], next_N)
      if max_cnt > cnt or k == 0:
        max_cnt = cnt
  else :
    max_cnt += C[index]
    # tmp = find(next_index[0], next_N)
    # print(next_index[0],tmp)
    max_cnt += find(next_index[0], next_N)
  return max_cnt

N, M = map(int, input().split())
L = []
R = []
C = []
max_cnt = 10
for i in range(M) :
  tmp = list(map(int, input().split()))
  L.append(tmp[0])
  R.append(tmp[1])
  C.append(tmp[2])

index = [i for i, x in enumerate(R) if x == N]
if not index :
  print(-1)
  exit()
if len(index) > 1 :
  for i in range(len(index)) :
    cnt = 0
    cnt = find(index[i], N)
    if max_cnt > cnt or i == 0:
      max_cnt = cnt
else :
  max_cnt = find(index[0],N)

if max_cnt = 1000000000 :
  print(-1)
else :
  print(max_cnt)