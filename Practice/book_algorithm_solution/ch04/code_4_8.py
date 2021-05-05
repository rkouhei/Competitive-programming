# fibo(N)の答えをメモ化
memo = [-1] * 50

def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1

    if memo[N] != -1:
        return memo[N]

    memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]

if __name__ == "__main__":
    fibo(49)

    for N in range(2, 50):
        print(str(N) + "項目: " + str(memo[N]))