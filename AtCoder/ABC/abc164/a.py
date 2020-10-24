# N = int(input())
# K = list(map(int, input().split()))
S, W = map(int, input().split())

if W >= S : 
    print('unsafe')
else :
    print('safe')