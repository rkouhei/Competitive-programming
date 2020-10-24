# 辞書順最小の問題
# 入力は
# 6
# ACDBCB
# とする

N = int(input())
S = input()
T = ''

l = 0
r = N - 1

while l <= r :
    left = False
    for i in range(r) :
        if S[l + i] < S[r - i] :
            left = True
            break
        elif S[l + i] > S[r - i] :
            left = False
            break
    
    if left :
        T += S[l]
        l += 1
    else :
        T += S[r]
        r -= 1

print(T)