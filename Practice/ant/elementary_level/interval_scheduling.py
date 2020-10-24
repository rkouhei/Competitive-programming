# 貪欲法での区間スケジューリング
# 入力は
# 5
# 1 2 4 6 8
# 3 5 7 9 10
# とする

import copy

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

itv = {}

for i in range(N) :
    itv[T[i]] = S[i]

ans = 0
t = 0
itv2 = dict(sorted(itv.items()))

for i in itv2.keys() :
    if t < itv2[i] :
        ans += 1
        t = copy.copy(i)

print(ans)