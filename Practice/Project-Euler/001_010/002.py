# フィボナッチ数列
fib = [1, 2]
next = 2

# ストップ
STOP = 4000000

# 合計
sum_fib = 2

while fib[-1] <= STOP :
    fib.append(fib[next-2]+fib[next-1])
    next += 1
    if fib[-1] % 2 == 0 :
        sum_fib += fib[-1]

print(sum_fib)