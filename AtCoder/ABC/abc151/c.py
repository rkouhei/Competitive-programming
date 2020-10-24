import itertools

def main() :
  N, M = map(int, input().split())
  p = []
  S = []

  for i in range(M) :
    tmp = input().split()
    p.append(int(tmp[0]))
    S.append(tmp[1])

  s = set(p)
  dict = {}
  for i in s :
    dict[i] = 0
  # print(dict)
  w_cnt = 0
  a_cnt = 0
  skip = []
  cnt = 0
  for key, value in itertools.groupby(p) :
    pre_cnt = cnt
    cnt += len(list(value))
    if key in skip :
      continue
    if 'AC' in S[pre_cnt:cnt] :
      ac_index = S[pre_cnt:cnt].index('AC')
      a_cnt += 1
      skip.append(key)
      w_cnt += len(S[pre_cnt:ac_index+pre_cnt])
    
  # for i in range(M) :
    # if p[i] not in skip :
    #   if S[i] == 'WA' :
    #     dict[p[i]] += 1
    #     continue
    #   else :
    #     a_cnt += 1
    #     w_cnt += dict[p[i]]
    #     skip.append(p[i])
    #     continue

  print(a_cnt, w_cnt)

if __name__ == '__main__' :
  main()