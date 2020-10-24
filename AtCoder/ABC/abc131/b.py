n, l = map(int, input().split())

tst_l = []

for i in range(1, n+1) :
    tmp = l + i - 1
    tst_l.append(tmp)

n_tst = sum(tst_l)

tmp_tst = sum(tst_l[1:n])
ans = n_tst - tmp_tst
ansi = tmp_tst

for i in range(1, n) :
    tmp_tst = 0
    tmp_tst += sum(tst_l[0:i])
    tmp_tst += sum(tst_l[i+1:n])

    near = n_tst - tmp_tst

    if abs(ans) > abs(near) :
        ansi = tmp_tst

print(ansi)