a, b, t = map(int, input().split())

time = 0
biscuit = 0

time +=  a
while time < t + 0.5 :
    biscuit += b
    time += a

print(biscuit)