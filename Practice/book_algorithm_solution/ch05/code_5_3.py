# Frog問題を緩和を意識した動的計画法で解く

def chmin(a, dst, b):
    if a[dst] > b:
        a[dst] = b

# どちらか
# INF = float("inf")
INF = 1 << 60

if __name__ == "__main__":
    N = int(input())
    h = list(map(int, input().split()))

    dp = [INF] * N
    dp[0] = 0

    for i in range(1, N):
        chmin(dp, i, dp[i - 1] + abs(h[i] - h[i - 1]))
        if i > 1:
            chmin(dp, i, dp[i - 2] + abs(h[i] - h[i - 2]))

    print(dp[N - 1])