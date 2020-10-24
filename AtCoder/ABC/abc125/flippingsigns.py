import numpy as np

n = int(input())
a = list(map(int, input().split()))
na = np.array(a) # 各要素の絶対値を楽に計算するため、numpyのarray作成
#total = 0

wh = len([i for i in a if i <= 0]) # リストの中のマイナスの要素数を求める

if wh % 2 == 0 : # マイナスの要素数が偶数の場合、全てプラスにできる
    print(sum(np.abs(na))) # リストの絶対値の合計が答え
else : # マイナスの要素数が奇数の場合、1要素だけマイナスとなる
    m = min(np.abs(na)) # 絶対値が最小となる値
    print(sum(np.abs(na)) - 2*m) # リストの絶対値の合計から2m引いた値が答え