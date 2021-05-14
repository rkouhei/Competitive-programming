# 線形探索(ペア和の最小値を求める)
if __name__ == "__main__":
    N, K = map(int, input().split())
    a  = list(map(int, input().split()))
    b  = list(map(int, input().split()))

    min_value = float("inf")
    for i in range(N):
        for j in range(N):
            if (a[i] + b[i]) < K:
                continue

            if (a[i] + b[i]) < min_value:
                min_value = a[i] + b[i]

    print(min_value)