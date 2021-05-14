# 線形探索(最小値を求める)
if __name__ == "__main__":
    N, v = map(int, input().split())
    a  = list(map(int, input().split()))

    min_value = float("inf")
    for i in range(N):
        if a[i] < min_value:
            min_value = a[i]

    print(min_value)