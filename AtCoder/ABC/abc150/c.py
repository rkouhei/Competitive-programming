from itertools import *

N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

result = list(permutations(range(1,N+1)))
print(abs(result.index(P)-result.index(Q)))

# def fact(n) :
#   f = 1 
#   for i in range(1,n+1) :
#     f *= i
#   return f

# N = int(input())
# P = list(map(int,input().split()))
# Q = list(map(int,input().split()))

# all = fact(N)

# p_result = 1
# cnt = 1
# tmp = N
# for i in range(N-2) :
#   p_result += (all / tmp) * abs(P[i]-cnt)
#   tmp -= 1
#   all = fact()


# print(p_result)