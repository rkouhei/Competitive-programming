n = list(map(int, input().split()))

tsum = min(n)
n.remove(min(n))
tsum += min(n)

print(tsum)