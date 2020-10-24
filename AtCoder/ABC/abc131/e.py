import numpy as np

n, m = map(int, input().split())
s = list(map(int, input().split()))
t = np.array(list(map(int, input().split())))

mod = 10**9 + 7
dp = np.ones(m+1, dtype='int64')

for i in s:
    #print(dp, end='')
    #print(dp[:-1],(i == t))
    #print((dp[:-1] * (i == t)))
    dp[1:] = ((dp[:-1] * (i == t)).cumsum() + dp[1:]) % mod
    print(dp)
print(dp[-1])