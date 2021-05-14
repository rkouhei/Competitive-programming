# 線形探索(添字を取得)
if __name__ == "__main__":
    N, v = map(int, input().split())
    a  = list(map(int, input().split()))

    found_id = -1
    for i in range(N):
        if a[i] == v:
            found_id = i
            break

    print(found_id)