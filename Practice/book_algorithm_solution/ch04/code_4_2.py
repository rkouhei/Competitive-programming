# 1からNまでの総和を再帰を用いて計算(printあり)
def func(N):
    print("func(" + str(N) + ") を呼び出しました")

    if N == 0:
        return 0
    
    result = N + func(N - 1)
    print(str(N) + "までの和 = " + str(result))

    return result

if __name__ == "__main__":
    func(5)