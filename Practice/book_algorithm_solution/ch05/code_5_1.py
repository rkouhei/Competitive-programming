# Frog問題を動的計画法で解く

# どちらか
# INF = float("inf")
INF = 1 << 60

if __name__ == "__main__":
    N = int(input())
    h = list(map(int, input().split()))

    dp = [INF] * N
    dp[0] = 0

    for i in range(1, N):
        if i == 1:
            dp[i] = abs(h[i] - h[i - 1])
        else:
            dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))

    print(dp[N - 1])