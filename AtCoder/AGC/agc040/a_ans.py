S = input()
N = len(S)

i = 0
ans = 0
c = 0 # 次の値
d = 0 # '>'が開始した箇所の値
j = 0 # '>'が連続する数

while i < N :
  if S[i] == '<' :
    c = c+1
    ans += c
    j = 0
  else :
    j = j+1
    if j > 1 :
      if d >= j :
        ans = ans+j-1
      else :
        ans = ans+j
    elif i == 0 :
      ans = 1
    else :
      d = c
    c = 0
  i += 1

print(ans)