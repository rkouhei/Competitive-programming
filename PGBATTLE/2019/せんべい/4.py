def func1(lst, value) :
  return [i for i, x in enumerate(lst) if x == value]

N, M = map(int, input().split())

A = []
B = []
for i in range(M) :
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

result = [0 for i in range(N)]
player = 0
person = 0
turn = 0

for j in range(N) :
  person = j+1
  turn = 0
  for i in range(3) :
    x = func1(A,person)
    if len(x) > 1 :
      break
    else :
      turn += 1
      person = B[x[0]]
    if person == 0 :
      result[player] += 1
    # if A[i] == person :
    #   turn += 1
    #   person = B[i]
    # if turn > 3 :
    #   break
    # if person == 0 :
    #   result[player] += 1

for i in range(N) :
  if result[i] == 1 :
    print("Yes")
  else :
    print("No")