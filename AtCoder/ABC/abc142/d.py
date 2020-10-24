def common_divisor(a,b) :
  i = 1
  table = []
  while i*i <= a and i*i <= b :
    if a%i == 0 and b%i == 0:
      table.append(i)
      if b%(a//i) == 0 :
        table.append(a//i)
    i += 1
  table.sort()
  return list(set(table))

def com_gcd(a,b) :
  while b != 0:
    a, b = b, a % b
  if a == 1 :
    return True
  else :
    return False


A, B = map(int, input().split())
c_div = common_divisor(A,B)
if len(c_div) == 1 :
  print(1)
  exit()

if c_div[1] == 2 :
  for i in range(len(c_div),3,-1) :
    if c_div[i-1] % 2 == 0 :
      c_div.pop(i-1)

for i in range(1,len(c_div)) :
  flag = True
  for j in range(i) :
    flag = com_gcd(c_div[i],c_div[j])
  if not flag :
    c_div.pop(i)

print(len(c_div))