import copy

rest = 10**9 + 7
s = input()
n = len(s)
min_num = s.replace('?','0')
min_list = list(map(int, min_num))
min_num = int(min_num)

cnt = 0
x = 10**n - 1
num_index = []
x_index = []

for i in range(-1,-(n+1),-1) :
  if s[i] != '?' :
    num_index.append(i)
  else :
    x_index.append(i)

# print(num_index)
# for i in range(1,len(x_index)+1) :
#   if min_num % 13 == 5 :
#     break
#   else :

flag = False
for i in list(range(18,10**n-1,13)) :
  q = str(i)
  if len(q) < abs(num_index[-1]) :
    continue
  
  for j in num_index :
    if q[j] == s[j] :
      continue
    else :
      flag = True
      break
  
  if flag :
    flag = False
    continue
  cnt += 1

print(cnt%rest)

# for i in list(range(18,1000000,13)) :
#   q = str(i)
#   if len(q) < 4 :
#     continue
#   else :
#     if q[-4] == '2' and q[-1] == '5' :
#       cnt += 1
#       print(q)
# print(cnt)