N = int(input())
s = []
t = []
for i in range(N) :
  tmp = input().split()
  s.append(tmp[0])
  t.append(int(tmp[1]))
X = input()

num = s.index(X) + 1

if N > num :
  print(sum(t[num:]))
else :
  print(0)