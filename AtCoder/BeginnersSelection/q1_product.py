# aとbを受け取り代入
a, b = map(int, input().split())
# 積を計算
c = a * b
# 偶数か奇数か判定
if c % 2 == 0 :
    print("Even")
else :
    print("Odd")