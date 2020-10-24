n = int(input())
card = list(map(int, input().split()))
alice = 0
bob = 0
diff = 0

for x in range(n) :
    if x % 2 == 0 :
        alice += max(card)
    else :
        bob += max(card)
    card.remove(max(card))

diff = abs(alice - bob)
print(diff)