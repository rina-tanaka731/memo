# 登録フォームに履歴書の添付欄を追加しようと思ったら、想像の 100 倍大変だった話

## 事の始まり

職務経歴書の添付欄があったので、同じようにすれば履歴書も添付できるやろ〜と甘く見ていた。2 日で終わると思っていたのに 1 週間かかった。そんなたわいもない話。

## 添付欄の追加（HTML, CSS, JavaScript）

フォームの追加はみなさんご存知のあれ（どれ）  
ファイル選択ボタンを押すと、画像がアップロードされるやつ

## メールにきちんと添付されるかな（Perl）

なんで Perl やねん…と悪態をつきながら毎日作業していた  
（というのは半分冗談で、後半完全に楽しんでた）  
なんとなく読めるようになったし、サブルーチンの作り方とかライブラリのインポート方法とかも分かるようになった（今後も役に立てばいいなあ）

### 問題 その１

- 配列だと思っていた変数が、配列じゃなかった
- 画像を２つ添付すると、画像が１つにされて壊れている
- ２つの場合は zip 形式にして添付しよう

### 問題 その２

- 文字化け地獄
- zip 化した際に、ファイル名が日本語名だと壊れる
- 濁音、撥音のとき壊れる
- ファイル名を「さんぷる」としたことで発見した（たぶん私は天才なんだと思う）
- 合成文字が原因
- 文字コード問題はそろそろ滅びてほしい

### 問題 その３

- null なのか、空文字なのか
- ログファイルを無理矢理作って確認したよ！
