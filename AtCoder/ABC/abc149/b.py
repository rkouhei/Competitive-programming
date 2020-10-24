A, B, K = map(int, input().split())

# t = -(-K // 2)
# a = K // 2

# result1 = A-t
# result2 = B-a

# if result1 < 0 :
#   result1 = 0
# if result2 < 0 :
#   result2 = 0

# print(result1, result2)

if A < K :
  K = K - A
  A = 0
else :
  A = A - K
  K = 0

if B < K :
  B = 0
else :
  B = B - K

print(A,B)