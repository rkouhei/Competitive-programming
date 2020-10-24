def main():
    N = int(input())
    cnt = 0
    for _ in range(N):
        A = input()
        if A == "WA" or A == "-":
            cnt += 1
    print(cnt * 5)

if __name__ == "__main__":
    main()