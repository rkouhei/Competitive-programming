import collections

N = int(input())
# K = list(map(int, input().split()))
# S, W = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cnt = 0

D = []

for i in range(N):
    D.append(B[C[i]-1])

A_c = collections.Counter(A)
D_c = collections.Counter(D)

for i in range(1, N+1):
    cnt += (A_c[i] * D_c[i])

# for i in range(1, N+1):
#     if i not in B:
#         continue
#     # if B[i] in B[:i]:
#     #     cnt += memo[B.index(B[i])]
#     #     continue
#     tmp = A.count(i) * C.count(B.index(i)+1)
#     b_len = len([j for j, x in enumerate(B) if x == i])
#     cnt += (tmp * b_len)

# memo = [0] * (N+1)

# for i in range(N):
    # if A[i] in A[:i]:
    #     cnt += memo[A.index(A[i])]
    #     continue
#     tmp = 0
#     for j in range(N):
#         if A[i] == B[j]:
#             tmp += C.count(j+1)
#     cnt += tmp
#     memo.append(tmp)

print(cnt)