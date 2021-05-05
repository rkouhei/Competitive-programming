# 部分和問題を再帰関数を用いる全探索で
def func(i, w, a):
    # base case
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    
    # a[i - 1]を選ばない場合
    if func(i - 1, w, a):
        return True

    # a[i - 1]を選ぶ場合
    if func(i - 1, w - a[i - 1], a):
        return True

    # どちらもfalseの場合
    return False

if __name__ == "__main__":
    N, W = map(int, input().split())
    a  = list(map(int, input().split()))
    
    if func(N, W, a):
        print("Yes")
    else:
        print("No")