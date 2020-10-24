def factorization(n):
  arr = []
  temp = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if temp%i==0:
      cnt=0
      while temp%i==0:
        cnt+=1
        temp //= i
      for j in range(cnt) :
        arr.append(i)

  if temp!=1:
    arr.append(temp)

  if arr==[]:
    arr.append(n)

  return arr

N = int(input())
fact = factorization(N)
fact.sort()

# print(fact)

while len(fact) > 4 :
  a = fact.pop(0)
  b = fact.pop(0)
  fact.append(a*b)
  fact.sort()

if len(fact) == 4 :
  x = fact.pop(0) * fact.pop(-1)
  y = fact.pop(0) * fact.pop(-1)
  fact.append(x)
  fact.append(y)
elif len(fact) == 3 :
  x = fact.pop(0) * fact.pop(-1)
  fact.append(x)

# print(fact)
if len(fact) == 1 :
  print(fact[0]-1)
else :
  print(fact[0]+fact[1]-2)