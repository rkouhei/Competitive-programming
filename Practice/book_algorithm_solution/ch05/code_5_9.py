# 区間ごとに分割する方法を最適化する
INF = float("inf")

def chmin(a, i, b):
    if a[i] > b:
        a = b

if __name__ == "__main__":
    N = int(input())
    c = []
    for i in range(N + 1):
        c.append(list(map(int, input().split())))
    
    dp = [INF] * (N + 1)
    dp[0] = 0

    for i in range(N + 1):
        for j in range(i):
            chmin(dp, i, dp[j] + c[j][i])

    print(dp[N])