# 整数bitの表す部分集合にi番目の要素が含まれるか？

if __name__ == "__main__":
    i = int(input())
    bit = int(input(), 2)

    print(bit)

    if bit & (1 << i):
        print("含まれる")
    else:
        print("含まない")