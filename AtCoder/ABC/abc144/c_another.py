import numpy as np

N = int(input())
for i in range(int(np.sqrt(N)), 0, -1) :
  if N%i == 0 :
    print(int(N/i)+i-2)
    exit()

print(N-1)