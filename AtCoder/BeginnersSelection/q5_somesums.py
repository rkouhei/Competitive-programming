n, a, b = map(int, input().split()) # 数字を取得

sum = 0 # 各桁の和の合計
total = 0 # a <= sum <= b となる数字の合計

for x in range(a, n+1) :
    va = x # 待避
    while True :
        if va == 0 :
            break
        else :
            sum += va % 10
            va = va // 10
    if a <= sum and sum <= b :
        total += x
    sum = 0

print(total)