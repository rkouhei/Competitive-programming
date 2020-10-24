X = int(input())

while True :
  for x in range(2, int(X**0.5)+1) :
    if X % x == 0 :
      X += 1
      break
  else : break
  
print(X)