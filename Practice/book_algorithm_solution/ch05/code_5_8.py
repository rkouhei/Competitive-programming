import pprint

# 編集距離を動的計画法を用いて求める
INF = float("inf")

def chmin(a, i, j, b):
    if a[i][j] > b:
        a[i][j] = b

if __name__ == "__main__":
    S, T = map(str, input().split())

    dp = [[INF] * (len(T) + 1) for i in range(len(S) + 1)]
    dp[0][0] = 0

    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            # 変更操作
            if i > 0 and j > 0:
                if S[i - 1] == T[j - 1]:
                    chmin(dp, i, j, dp[i - 1][j - 1])
                else:
                    chmin(dp, i, j, dp[i - 1][j - 1] + 1)

            # 削除操作
            if i > 0:
                chmin(dp, i, j, dp[i - 1][j] + 1)

            # 挿入操作
            if j > 0:
                chmin(dp, i, j, dp[i][j - 1] + 1)

            pprint.pprint(dp)
            print()
    
    print(dp[len(S)][len(T)])