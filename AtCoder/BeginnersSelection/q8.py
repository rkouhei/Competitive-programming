import sys

n, y = map(int, input().split())
money = 0
a = 0
b = 0
c = 0

for i in range(n+1) :
  for j in range(n-i,-1,-1) :
    a = i
    b = j
    c = n - i - j
    money = 10000*a + 5000*b + 1000*c
    if money == y :
      print(a,b,c)
      sys.exit()

print('-1 -1 -1')