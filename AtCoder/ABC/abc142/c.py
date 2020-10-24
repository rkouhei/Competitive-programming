N = int(input())
A = list(map(int, input().split()))
result = [0 for i in range(N)]

# for i in range(N) :
#   print(A.index(i+1)+1, end="")
#   print(" ", end="")

# for i in range(N) :
#   for j in range(int(N/2)+1) :
#     if A[j] == i+1 :
#       print(j+1, end="")
#       print(" ", end="")
#       break
#     elif A[N-1-j] == i+1 :
#       print(N-j, end="")
#       print(" ", end="")
#       break
  
for i in range(N) :
  result[A[i]-1] = i+1

for i in range(N) :
  print(result[i], end="")
  print(" ", end="")