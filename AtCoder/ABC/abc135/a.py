a, b = map(int, input().split())

c = abs(a-b)

if c % 2 == 0 :
  x = abs((a**2 - b**2)/(2*b - 2*a))
  print(int(x))
else :
  print('IMPOSSIBLE')