S = input()
# K = list(map(int, input().split()))
# S, W = map(int, input().split())

# S = S.replace('9', '6')

S = S.translate(str.maketrans({'9': '6', '6': '9'}))
S = list(S)
S.reverse()
S = ''.join(S)

print(S)