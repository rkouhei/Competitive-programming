# N = int(input())
# A = list(map(int, input().split()))
H, W = map(int, input().split())

if H == 1 or W == 1 :
  print(1)
  exit()

print(-(-(H * W) // 2))