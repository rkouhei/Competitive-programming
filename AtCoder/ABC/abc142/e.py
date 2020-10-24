N, M = map(int, input().split())
A = []
B = []
C = []

for i in range(M) :
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(list(map(int, input().split())))

for i in range(M) :
  for j in range(M-i)