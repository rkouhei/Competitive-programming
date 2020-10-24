i = int(input())
j = [int(x) for x in input().split()]
count = 0
flag = False

while True :
    for y in range(i) :
        if j[y] % 2 != 0 :
            flag = True
        else :
            j[y] /= 2
    if flag :
    	break
    count += 1

print(count)
