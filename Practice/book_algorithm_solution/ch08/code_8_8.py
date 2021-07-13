# ハッシュテーブルの挿入・削除・検索クエリ処理
if __name__ == "__main__":
    a = set(1, 2)
    x = 3
    
    # 要素xの挿入
    a.add(x)

    # 要素xの削除
    a.remove(x)

    # 要素xの検索
    if x in a:
        print("x in a")
