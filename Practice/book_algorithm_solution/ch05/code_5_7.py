# ナップサック問題に対する動的計画法
import pprint

def chmax(a, dst1, dst2, b): # aはリスト dstはその添字
    if a[dst1][dst2] < b:
        a[dst1][dst2] = b


if __name__ == "__main__":
    N, W = map(int, input().split())
    weight = []
    value = []
    for i in range(N):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)

    dp = [[0] * (W + 1) for i in range(N + 1)]

    for i in range(N):
        for w in range(W+1):
            # i番目を選ぶ場合
            if w - weight[i] >= 0:
                chmax(dp, i + 1, w, dp[i][w - weight[i]] + value[i])

            # i番目を選ばない場合
            chmax(dp, i + 1, w, dp[i][w])

    print(dp[N][W])