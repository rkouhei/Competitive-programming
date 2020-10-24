S = input()
K = int(input())

flag = False

itr = 0
cnt = 1
len_cnt = []
for x in S :
  if itr == 0 :
    pre = x
    itr += 1
    continue
  now = x
  if pre == now :
    cnt += 1
    itr += 1
    if itr == len(S) :
      len_cnt.append(cnt)
    continue
  if pre != now :
    len_cnt.append(cnt)
    itr+=1
    if itr == len(S) and cnt == 1 :
      len_cnt.append(cnt)
    cnt = 1
    pre = x
    continue

if sum(len_cnt) != len(S) :
  len_cnt.append(1)

if len(len_cnt) == 1 :
  print(int(len_cnt[0] * K / 2))
  exit()

ans = 0
for x in len_cnt :
  if x == 1 :
    continue
  else :
    ans += int(x / 2)

# if S[0] == S[-1] and len_cnt[-1] > 1 and len_cnt[-1] % 2 == 1 and K > 1:
#   ans += 1
if S[0] == S[-1] and len_cnt[-1] % 2 == 1 and len_cnt[0] % 2 == 1 :
  ans += 1
  flag = True

ANS = K * ans
# print (ANS, len_cnt)
if flag :
  ANS -= 1

# if S[0] ==S[-1] and len_cnt[-1] % 2 == 1 and len_cnt[-1] != 1 :
#   ANS -= 1
print(ANS)

# cnt = 0
# flag = False

# if S[0] == S[-1] :
#   cnt += 1
#   flag = True

# for i in range(1,len(S)) :
#   if S[i] == S[i-1] :
#     cnt += 1
#     if i == len(S)-1 and flag :
#       cnt -= 1

# print (K * cnt)

# iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiix