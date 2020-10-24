import collections

N = int(input())
D = list(map(int, input().split()))
mod = 998244353


if D[0] != 0 :
  print(0)
else :
  D_dict  = collections.Counter(D)
  if D_dict[0] > 1 :
    print(0)
    exit()
  result = 1
  for i in range(1, len(D_dict)) :
    if D_dict[i] == 0 :
      print(0)
      exit()
    else :
      result *= D_dict[i-1]**D_dict[i]
      result = result % mod

  print(result)
  