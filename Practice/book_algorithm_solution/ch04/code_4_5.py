# フィボナッチ数列を求める再帰関数
def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1

    return fibo(N - 1) + fibo(N - 2)