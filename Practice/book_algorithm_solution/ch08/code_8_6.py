# 削除操作も可能にした双方向連結リスト
# 疑似ノード
class Node:
    def __init__(self, name):
        self.value = name
        self.next = None
        self.prev = None

# グローバル番兵
# 初期化
nil = Node(None)


# 連結リストの出力
def printList():
    cur = nil.next
    while cur:
        print(cur.value + ", ", end="")
        cur = cur.next
    print()

# ノードpの直後にノードvを挿入
def insert(v, p = nil):
    v.next = p.next
    if p.next != None:
        p.next.prev = v
    p.next = v
    v.prev = p

# ノードvの削除
def erase(v):
    if v == nil:
        return
    v.prev.next = v.next
    v.next.prev = v.prev

if __name__ == "__main__":
    # 作りたいノードの名前一覧
    names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]

    for name in names:
        node = Node(name)
        insert(node)

        if name == "watanabe":
            w = node

    print("before ", end="")
    printList()

    erase(w)
    print("after ", end="")
    printList()
