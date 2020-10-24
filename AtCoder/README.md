# AtCoderContest
## ディレクトリ構成
- ABC (AtCoder Beginner Contest)
- AGC (AtCoder Grand Contest)
- company (company's contest)
- Beginners Selection
  - URL : https://qiita.com/drken/items/fd4e5e3630d0f5859067

## cliのみでテスト、提出する方法
### コンテスト用のディレクトリ作成
```
$ acc new [contest ID]
```

### テストケースを試す
```
$ oj t -c "python3 a.py" -d tests/
```

### コードの提出
```
$ acc submit a.py
```

pythonは2系と3系の実行環境が存在するため、提出するファイルにはshebangをつける
```
#!/usr/bin/env python3
```

## accとojのセットアップ
まずは以下のコマンドを実行
```
$ pip3 install online-judge-tools
$ npm install -g atcoder-cli
```

インストールの確認
```
$ acc -h
$ oj -h
```

accとojの連携確認(availableならOK)
```
$ acc check-oj
```

accとojでログイン
```
$ acc login 
$ oj login https://atcoder.jp/
```

accで全問のテストケースを入手するように変更
```
$ acc config default-task-choice all
```