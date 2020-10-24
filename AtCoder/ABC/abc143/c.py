N = int(input())
S = list(input())

count = 1
result = []
for i in range(N) :
  if i == 0 :
    before = S[i]
    continue
  if before == S[i] :
    count += 1
  else :
    result.append(count)
    count = 1
    before = S[i]

result.append(count)
print(len(result))