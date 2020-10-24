# N = int(input())
# K = list(map(int, input().split()))
A, B, C, D = map(int, input().split())

T = -(-A // D)
AO = -(-C // B)

if T >= AO :
    print('Yes')
else :
    print('No')