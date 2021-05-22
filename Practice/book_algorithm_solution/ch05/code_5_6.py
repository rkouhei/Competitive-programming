# Frog問題を「メモ化再帰」で解く

# グローバル変数
h = [] # 高さリスト
dp = [] # メモ

# どちらか
# INF = float("inf")
INF = 1 << 60

# ミュータブル非対応
def chmin(a, b):
    if a > b:
        return b
    return a

def rec(i):
    if dp[i] < INF:
        return dp[i]

    if i == 0:
        return 0

    res = INF

    # 足場 i - 1
    res = chmin(res, rec(i - 1) + abs(h[i] - h[i - 1]))

    # 足場 i - 2
    if i > 1:
        res = chmin(res, rec(i - 2) + abs(h[i] - h[i - 2]))

    dp[i] = res # メモ化
    return res

if __name__ == "__main__":
    N = int(input())
    h = list(map(int, input().split()))

    dp = [INF] * N

    rec(N - 1)
    print(dp[N - 1])