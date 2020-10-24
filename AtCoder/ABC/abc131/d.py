import numpy as np
import sys
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
arr = sorted(a, key = lambda x:x[1])
#print(arr)
#arr = np.array(a)
#arr_sort = np.sort(arr, axis=0)
#print(arr_sort)

tmp = 0
for i in range(n) :
    tmp += arr[i][0]
    if tmp > arr[i][1] :
        print('No')
        sys.exit()

print('Yes')