if __name__ == "__main__":
    # フィボナッチ数列をfor文による反復で求める
    F = [0] * 50
    F[0] = 0
    F[1] = 1
    for N in range(2, 50):
        F[N] = F[N - 1] + F[N-2]
        print(str(N) + "項目: " + str(F[N]))