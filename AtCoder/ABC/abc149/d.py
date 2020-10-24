N, K = map(int, input().split())
R, S, P = map(int, input().split())
dic = {'r': P, 's': R, 'p': S}
ans_dic = {'r': 'p', 's': 'r', 'p': 's'}
T = list(input())

result = 0
ans = []

for t in range(N) :
  if t < K :
    result += dic[T[t]]
    ans.append(ans_dic[T[t]])
  else :
    if ans[t-K] == ans_dic[T[t]] :
      if t+K < N :
        ans.append(T[t+K])
      else :
        continue
    else :
      result += dic[T[t]]
      ans.append(ans_dic[T[t]])

print(result)
