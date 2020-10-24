a = int(input()) # 500円玉の枚数
b = int(input()) # 100円玉の枚数
c = int(input()) # 50円玉の枚数
x = int(input()) # 目標の合計金額

sum = 0 # 合計金額
count = 0 # 何通りあるか

for q in range(a+1) :
    for w in range (b+1) :
        for e in range(c+1) :
            sum = 500*q + 100*w + 50*e
            if sum == x :
                count += 1
            elif sum > x : # sumが目標金額を超えたらそれ以上のループは意味ない
                break 
            sum = 0

print(count)