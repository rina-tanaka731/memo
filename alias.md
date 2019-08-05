# ターミナルをちょっといい感じにする（Mac）(多分 Windows でもできる)

## 色をつける

- ホームディレクトリ`.gitconfig`内に記述

```
[color]
    ui = true
```

## エイリアスの設定

- git コマンドを自分で自由に短縮できる
- ホームディレクトリ`.gitconfig`内に記述

```
[alias]
    st = status
    co = checkout
    cm = commit
    gr = log --graph --date-order --all --pretty=format:'%h %Cred%d %Cgreen%ad %Cblue%cn %Creset%s' --date=short
```

## タブ補完で大文字と小文字の区別をしないようにする

- ホームディレクトリ`.inputrc`内に記述

```
set completion-ignore-case on
```
