s = str(input())

yy = int(s[0:2])
mm = int(s[2:4])

mf1 = False
mf2 = False

if 0 < yy < 13 :
    mf1 = True
if 0 < mm < 13 :
    mf2 = True

if mf1 and mf2 :
    print('AMBIGUOUS')
elif mf1 and not mf2 :
    print('MMYY')
elif not mf1 and mf2 :
    print('YYMM')
elif not mf1 and not mf2 :
    print('NA')