def dfs(i, sum) :
    if i == n : return sum == k
    if dfs(i + 1, sum) : return True
    if dfs(i + 1, sum + a[i]) : return True
    return False

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    if dfs(0, 0) : print('Yes')
    else : print('No')