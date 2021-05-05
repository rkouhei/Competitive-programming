import math

def calc_dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2))

N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

minimum_dist = 100000000.0

for i in range(N):
    for j in range(i+1, N):
        dist_i_j = calc_dist(x[i], y[i], x[j], y[j])

        if dist_i_j < minimum_dist:
            minimum_dist = dist_i_j

print(minimum_dist)