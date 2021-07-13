# 双方向への自己参照構造体
class Node:
    def __init__(self, name):
        self.value = name
        self.next = None
        self.prev = None
