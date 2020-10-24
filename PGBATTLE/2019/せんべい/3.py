N, M = map(int, input().split())
A, B, C = map(int, input().split())

legs = 0

for i in range(N) :
  for j in range(N-i) :
    legs = (A*i) + (B*j) + (C*(N-i-j))
    if legs == M :
      print(i,j,N-i-j)
      exit()

print("-1 -1 -1")

# while True :
#   result[2] += 1
#   legs += C
#   if (result[2] - 1) > result[1] :
#     result[2] -= 2
#     result[1] += 1
#     legs -= C
#     legs += B
#   if (result[1] - 1) > result[0] :
#     result[1] -= 2
#     result[0] += 1
#     legs -= B
#     legs += A
#   if legs == M  and sum(result) == N :
#     break
#   if result[0] > N :
#     flag = True
#     break
#   print(result)

# a_p = 0
# b_p = 1
# c_p = 2

# if A > B :
#   a_p, b_p = b_p, a_p
# if A > C :
#   a_p, c_p = c_p, a_p
# if B > C :
#   b_p, c_p = c_p, b_p



# aflag = True
# bflag = True
# cflag = True

# while aflag and bflag and cflag :
#   if legs < M and cflag:
#     legs += C
#     result[2] += 1
#     if legs > M :
#       legs -= C
#       result[2] -= 1
#       cflag = False
#     continue
#   if legs < M and bflag:
#     legs += B
#     result[1] += 1
#     if legs > M :
#       if result[2] > 0 :
#         result
#       legs -= B
#       result[1] -= 1
#       bflag = False
#     continue
#   if legs < M and aflag:
#     legs += A
#     result[0] += 1
#     if legs > M :
#       legs -= A
#       result[0] -= 1
#       aflag = False
#     continue