import math

dp = [[0] * 31 for i in range(31)]

def find_kth(A, B, K):
    if A == 0:
        return 'b' * B
    if B == 0:
        return 'a' * A
    if K <= dp[A-1][B]:
        return 'a' + find_kth(A-1, B, K)
    else:
        return 'b' + find_kth(A, B-1, K-dp[A-1][B])

if __name__ == "__main__":
    A, B, K = map(int, input().split())

    dp[0][0] = 1

    for i in range(A+1):
        for j in range(B+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    
    print(find_kth(A, B, K))