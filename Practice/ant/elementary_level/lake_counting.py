def dfs(x, y) :
    field[x][y] = '.'

    for dx in range(-1, 2) :
        for dy in range(-1, 2) :
            nx = x + dx
            ny = y + dy

            if (0 <= nx and nx < n and 0 <= ny and ny < m and field[nx][ny] == 'W') :
                dfs(nx, ny)

    return


if __name__ == "__main__":
    n, m = map(int, input().split())
    field = []
    for i in range(n) :
        field.append(list(input()))

    res = 0 # 水たまりの数
    for i in range(n) :
        for j in range(m) :
            if field[i][j] == 'W' :
                dfs(i, j)
                res += 1

    print(res)