N = int(input())

flag = False

for i in range(1,10) :
  if int(N/i) < 10 and N%i == 0:
    print('Yes')
    exit()

print('No')