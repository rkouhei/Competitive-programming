import time

def main():
    start = time.time()

    H, W = map(int, input().split())
    Px, Py, Qx, Qy = map(int, input().split())
    Px -= 1
    Py -= 1
    Qx -= 1
    Qy -= 1
    maze = []
    for _ in range(H):
        maze.append(list(input()))
    
    flag_list = [[0] * W for i in range(H)]

    cnt = 0
    front = "N"

    while True:
        if Px == Qx and Py == Qy:
            print(cnt)
            exit()

        if front == "N":
            if Py-1 >= 0 and maze[Px][Py-1] == ".":
                # maze[Px][Py-1] = "#"
                flag_list[Px][Py-1] += 1
                Py -= 1
                front = "W"
            elif Px-1 >= 0 and maze[Px-1][Py] == ".":
                # maze[Px-1][Py] = "#"
                flag_list[Px-1][Py] += 1
                Px -= 1
            elif Py+1 < W and maze[Px][Py+1] == ".":
                # maze[Px][Py+1] = "#"
                flag_list[Px][Py+1] += 1
                Py += 1
                front = "E"
            elif Px+1 < H and maze[Px+1][Py] == ".":
                # maze[Px+1][Py] = "#"
                flag_list[Px+1][Py] += 1
                Px += 1
                front = "S"
            else :
                print("-1")
                exit()
        elif front == "W":
            if Px+1 < H and maze[Px+1][Py] == ".":
                # maze[Px][Py-1] = "#"
                flag_list[Px+1][Py] += 1
                Px += 1
                front = "S"
            elif Py-1 >= 0 and maze[Px][Py-1] == ".":
                # maze[Px-1][Py] = "#"
                flag_list[Px][Py-1] += 1
                Py -= 1
            elif Px-1 >= 0 and maze[Px-1][Py] == ".":
                # maze[Px][Py+1] = "#"
                flag_list[Px-1][Py] += 1
                Px -= 1
                front = "N"
            elif Py+1 < W and maze[Px][Py+1] == ".":
                # maze[Px+1][Py] = "#"
                flag_list[Px][Py+1] += 1
                Py += 1
                front = "E"
            else :
                print("-1")
                exit()
        elif front == "E":
            if Px-1 >= 0 and maze[Px-1][Py] == ".":
                # maze[Px][Py-1] = "#"
                flag_list[Px-1][Py] += 1
                Px -= 1
                front = "N"
            elif Py+1 < W and maze[Px][Py+1] == ".":
                # maze[Px-1][Py] = "#"
                flag_list[Px][Py+1] += 1
                Py += 1
            elif Px+1 < H and maze[Px+1][Py] == ".":
                # maze[Px][Py+1] = "#"
                flag_list[Px+1][Py] += 1
                Px += 1
                front = "S"
            elif Py-1 >= 0 and maze[Px][Py-1] == ".":
                # maze[Px+1][Py] = "#"
                flag_list[Px][Py-1] += 1
                Py -= 1
                front = "W"
            else :
                print("-1")
                exit()
        elif front == "S":
            if Py+1 < W and maze[Px][Py+1] == ".":
                # maze[Px][Py-1] = "#"
                flag_list[Px][Py+1] += 1
                Py += 1
                front = "E"
            elif Px+1 < H and maze[Px+1][Py] == ".":
                # maze[Px-1][Py] = "#"
                flag_list[Px+1][Py] += 1
                Px += 1
            elif Py-1 >= 0 and maze[Px][Py-1] == ".":
                # maze[Px][Py+1] = "#"
                flag_list[Px][Py-1] += 1
                Py -= 1
                front = "W"
            elif Px-1 >= 0 and maze[Px-1][Py] == ".":
                # maze[Px+1][Py] = "#"
                flag_list[Px-1][Py] += 1
                Px -= 1
                front = "N"
            else :
                print("-1")
                exit()
        if "30" in "".join(map(str, list(set(sum(flag_list,[]))))):
            print("-1")
            exit()
        cnt += 1
        elapsed_time = time.time() - start
        if elapsed_time > 1800 :
            print("-1")
            exit()


if __name__ == "__main__":
    main()
