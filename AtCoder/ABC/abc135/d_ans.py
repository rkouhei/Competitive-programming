mod = 10**9 + 7
s = input()
n = len(s)

dp = [[0]*13 for i in range(n+1)]
dp [0][0] = 1

for i in range(n) :
  for j in range(13) :
    for k in range(10) :
      x = (10*j+k) % 13
      dp[i+1][x] = (dp[i+1][x] + (1 if s[i] == '?' or s[i] == str(k) else 0) * dp[i][j]) % mod

print(dp[n][5])