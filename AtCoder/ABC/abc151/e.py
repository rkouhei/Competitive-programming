import itertools

mod = 10**9 + 7
N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

for i in itertools.combinations(A, K) :
  cnt += abs(max(i)- min(i))
  cnt %= mod

print(cnt)