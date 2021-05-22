# 緩和処理関数
def chmin(a, dst, b): # Cと違い参照渡しできるのはmutableなオブジェクトだけ
    if a[dst] > b:
        a[dst] = b

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = 3

    chmin(a, 4, b)
    print(a)