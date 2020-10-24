L = int(input())
n = int(input())
x = list(map(int, input().split()))

min = 0
max = 0
for i in range(n) :
    # 最小の場合
    minL_i = x[i] if x[i] < L - x[i] else L - x[i]
    min = min if min > minL_i else minL_i
    # 最大の場合
    maxL_i = x[i] if x[i] > L - x[i] else L - x[i]
    max = max if max > maxL_i else maxL_i

print(min, max)