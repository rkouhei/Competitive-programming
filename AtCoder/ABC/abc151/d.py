H, W = map(int, input().split())
maze = []
for i in range(H) :
  tmp = input().split()
  maze.append(tmp)

m_cnt = 0

def dps(maze, y, x, gy, gx) :
  cnt = 0
  if y == gy and x == gx :
    return [(y,x)]
  maze[y][x] = '#'
  for (n_y, n_x) in [(y+1, x), (y, x+1), (y, x-1), (y-1, x)] :
    if n_y < 0 or n_x < 0 or n_y >= H or n_x >= W :
      continue
    if maze[n_y][n_x] == '#' :
      continue
    cnt = dps(maze, n_y, n_x, gy, gx)
    if cnt :
      return [(y,x)] + cnt

for i in range(H) :
  for j in range(W) :
    for k in range(H) :
      for l in range(W) :
        tmp = len(dps(maze, i, j, k, l))
        print(tmp)
        if tmp > m_cnt :
          m_cnt = tmp

print(m_cnt)