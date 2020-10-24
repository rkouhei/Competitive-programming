x, y = list(map(int, input().split()))

price = 0
flag = False
if x == 1 :
  price += 300000
  flag = True
elif x == 2 :
  price += 200000
elif x == 3 :
  price += 100000

if y == 1 :
  price += 300000
  if flag :
    price += 400000
elif y == 2 :
  price += 200000
elif y == 3 :
  price += 100000

print(price)