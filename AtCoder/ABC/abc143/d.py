# import itertools
from bisect import bisect_left

N = int(input())
L = list(map(int, input().split()))
L.sort()

result = 0
for i in range(N) :
  for j in range(i+1,N) :
    result += bisect_left(L,L[i]+L[j]) - (j+1)

print(result)

# itertoolsでのやり方
# result = 0
# for i in list(itertools.combinations(range(N),3)) :
#   if L[i[0]] < L[i[1]] + L[i[2]] and L[i[1]] < L[i[0]] + L[i[2]] and L[i[2]] < L[i[1]] + L[i[0]] :
#     result += 1

# print(result)