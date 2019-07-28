# いちからSpring Bootプロジェクトを作成する方法（@IntelliJ）
* 環境
    * Java（自宅では12を使用）
    * IntelliJ（無料版で問題なし） 

* プラグインの導入
    *  IntelliJのトップ（Welcome to IntelliJ IDEA）を開く
        * 別のプロジェクトを開いている場合は、File -> Close Project で閉じる
    * 右下 Configure -> Prugins を開く
    * Marketplace から**Spring Assistant**を検索で探し、Install
    * IntelliJ をリスタート

* プロジェクト作成１
    * Create New Projectを選択
    * 左側に先ほどインストールした**Spring Assistant**があるので選択
    * Project SDK でJavaのバージョンを選択
    * Spring Initializr server はDefaultのままでOK
        * 他のを選ぶとどうなるか不明なので、各自調べてください

* プロジェクト作成２
    * Project Type -> Gradle Project
    * Langage -> Java
    * Package -> Jar
    * Java version -> SDKで選択したJavaのバージョンと揃えると思われる

* プロジェクト作成３
    * 依存関係を追加（以下おすすめ）
        * Spring Boot DevTools
        * Spring Web Starter
        * Spring Web Service
        * Tymeleaf
    * いろんな選択肢があるので、ぜひ調べて使ってみてください

* ブラウザで見る
    * Application.javaは自動的に作成されるので、Controllerを作る必要あり
    * HTMLファイルは、resources内に「templates」ディレクトリを作成し、その中に入れる
    * resources/application.propaties へ`server.port = 3000`のように適当な番号を追記すると、デフォルトの8080から[localhost:3000](localhost:3000)に変更できる
    
