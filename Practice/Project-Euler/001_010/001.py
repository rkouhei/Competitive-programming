# 3と5の倍数を生成
x = list(range(3,1000, 3))
y = list(range(5,1000, 5))

# 結合
x_y = x + y

# 重複する値を除き、合計を算出
print(sum(set(x_y)))