n, k = map(int, input().split())
s = str(input())

tar = str(s[k-1]).lower()

print(s[0:k-1] + tar + s[k:n+1])