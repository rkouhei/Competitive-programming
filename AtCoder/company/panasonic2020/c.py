# N = int(input())
# A = list(map(int, input().split()))
a, b, c = map(int, input().split())

# AB = 2 * np.sqrt(a*b)

# ans = (a + b + AB) - c
ans = (a ** 2) + (b ** 2) + (c ** 2) - 2*(a*b + b*c + a*c)
# ans2 = ((a - c) ** 2) + (b * (b - 2*c - 2*a))
# print(ans, ans2)

if ans > 0 :
  print('Yes')
else :
  print('No')