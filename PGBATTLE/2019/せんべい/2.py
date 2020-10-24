N, K = map(int, input().split())
A = list(map(int, input().split()))

time = 0

for i in range(N) :
  if A[i] > K :
    time += (A[i] - K)

print(time)