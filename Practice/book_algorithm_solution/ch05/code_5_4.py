# Frog問題を「配る遷移形式」で解く

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

    for i in range(0, N):
        if (i + 1) < N:
            chmin(dp, (i + 1), dp[i] + abs(h[i] - h[i + 1]))
        if (i + 2) < N:
            chmin(dp, (i + 2), dp[i] + abs(h[i] - h[i + 2]))

    print(dp[N - 1])