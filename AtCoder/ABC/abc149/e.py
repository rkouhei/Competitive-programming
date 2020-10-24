N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
result = 0
ans = []


# result += A[0] * 2

# if M >= 3 :
#   result += (A[0] + A[1]) * 2
# elif M == 2 :
#   result += (A[0] + A[1])

# r_1 = 0
# l_1 = 2
# r_2 = 1
# l_2 = 1
# if M > 3 :
#   ite = 3
#   while ite < M :
#     if (A[r_1] + A[l_1]) > (A[r_2] + A[l_2]) :
#       result += (A[r_1] + A[l_1]) * 2
#       ite += 2
#       l_1 += 1
#       if l_1 == N :
#         r_1 = 