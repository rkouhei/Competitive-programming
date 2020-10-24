# N = int(input())
# K = list(map(int, input().split()))
# N, M = map(int, input().split())

S = list(input())

# print(int(''.join(S)) / 2019)
# print(int(''.join(S)) % 2019)

cnt = 0

# for i in range(0,len(S)-3) :
#     for j in range(i+3, len(S)) :
#         # print(int(''.join(S[i:j+1])))
#         res = int(''.join(S[i:j+1]))
#         if res % 2019 == 0 :
#             cnt += 1
#             print(S[i:j+1])

# for i in range(0,len(S)-3) :
#     amari = int(''.join(S[i:i+3]))
#     for j in range(i+3, len(S)) :
#         amari = ((amari * 10) + int(S[j])) % 2019
#         if amari == 0 :
#             cnt += 1

# for i in range(len(S)) :

print(cnt)