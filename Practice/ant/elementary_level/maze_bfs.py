# abc007-c

def bfs(maze, d, sx, sy, gx, gy, N, M) :
    que = []
    que.append([sx, sy])
    d[sx][sy] = 0
    dx = [1, 0, -1, 0] # x軸の進行方向
    dy = [0, 1, 0, -1] # y軸の進行方向

    while que :
        p = que.pop(0)
        if p[0] == gx and p[1] == gy :
            break
        for i in range(4) :
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if 0 <= nx and nx < N and 0 <= ny and ny < M and maze[nx][ny] != '#' and d[nx][ny] == 1000000 :
                que.append([nx, ny])
                d[nx][ny] = d[p[0]][p[1]] + 1

    return d[gx][gy]

if __name__ == "__main__":
    N, M = map(int, input().split()) # size of maze
    sx, sy = map(int, input().split()) # start
    gx, gy = map(int, input().split()) # goal
    maze = []
    d = [[1000000] * M for i in range(N)] # 各点までの最短距離
    
    # 問題の都合
    sx -= 1
    sy -= 1
    gx -= 1
    gy -= 1
    
    for i in range(N) :
        maze.append(list(input()))
    print(bfs(maze, d, sx, sy, gx, gy, N, M))