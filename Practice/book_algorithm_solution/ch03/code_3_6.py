# 部分和問題に対するビットを用いる全探索

if __name__ == "__main__":
    N, W = map(int, input().split())
    a  = list(map(int, input().split()))

    exist = False
    for bit in range(2**N):
        sum = 0
        for i in range(N):
            if bit & (1 << i):
                sum += a[i]
        
        if sum == W:
            exist = True

    if exist:
        print("Yes")
    else:
        print("No")