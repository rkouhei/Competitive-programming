S = input()

length = len(S) + 1
ans = [0] * length
flag = False
for x in range(len(S)) :
  if flag :
    if S[x] == '>' :
      continue
    else :
      flag = False
  if S[x] == '<' :
    ans[x+1] = ans[x] + 1
  else :
    if S[x+1] == '>' :
      for y in range(x+1,len(S)) :
        if S[y] == '>' :
          for z in range(x,y+1) :
            ans[z] += 1
          if ans[x] > ans[x+1] + 1 :
            ans[x] -= 1
        else :
          break
      flag = True



# print(ans)
print(sum(ans))

# for x in range(length) :
#   print(ans[x], end='')
#   print(S[x], end='')