# フィボナッチ数列を求める過程での再帰呼び出しの様子
def fibo(N):
    print("fibo(" + str(N) + ") を呼び出しました")

    if N == 0:
        return 0
    elif N == 1:
        return 1

    result = fibo(N - 1) + fibo(N - 2)
    print(str(N) + "項目 = " + str(result))

    return result

if __name__ == "__main__":
    fibo(6)