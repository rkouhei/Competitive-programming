# 連結リストを、挿入操作を用いて構築する
# 疑似ノード
class Node:
    def __init__(self, name):
        self.value = name
        self.next = None

# グローバル番兵
# 初期化
nil = Node(None)

# 連結リストの出力
def printList():
    cur = nil.next
    while cur:
        print(cur.value + ", ", end="")
        cur = cur.next

# ノードpの直後にノードvを挿入
# ノードpのデフォルトをNone → insert(v)ではリストの先頭への挿入
def insert(v, p = nil):
    v.next = p.next
    p.next = v

if __name__ == "__main__":
    # 作りたいノードの名前一覧
    names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]

    for name in names:
        node = Node(name)
        insert(node)

        print("step ", end="")
        printList()
        print()
