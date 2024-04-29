---
blogpost: true
date: 2024-02-10 # YYYY-MM-DD
category: technical
tags: Sphinx, Github Pages
language: ja
---

# Sphinx＋Github Pagesで個人ページ作成

```{Attention}
以下は個人的備忘録としての側面が強いため，解説記事としては不足が多いです．また，書いた人間はいわゆるIT業界で働いているわけではなく，技術系ブログを書いた経験もなく，プログラミングはなるべくやりたくないと考えています．
```

細かい設定はさておき，このウェブサイト風のものを再現したいだけのときは，[ここ](#flow)から先のみ見ればよい．

## 動機
Github Pagesで個人ページを作成する際，Markdown＋Jekyllで作成するのが簡便である．検索しても多くの場合その情報が出てくる．また，そもそもGithub PagesではデフォルトでJekyllをサポートしている．しかしここではSphinxのみを使用する．その理由は以下の3点である．
- Jekyllがよくわからなかった
- Sphinxを勉強したかった（結局Sphinxもよくわからなかった）
- Dockerを勉強したかった（後述するがSphinxはsphinx-docコンテナを使用したが当然よくわからなかった）

上記のように，よくわからなかったのでSphinxそのものの解説はここでは書かない．

なお，Sphinxはそもそも個人ページというよりは公式ドキュメントやマニュアル向けの色が強い．なので使用目的がずれているという指摘はごもっともかもしれないがそれは置いておく．

ほかにはHugoという選択肢もあるようで，これはこれで簡単そうで気になるがこれから検討ということにしておく．

## 導入
Dockerを使用する．Docker Hubからイメージsphinxdoc/sphinxをpullする．いろいろライブラリを追加したいため最終的にはDockerfileでイメージを作成するが，一応書いておく．
```bash
docker pull sphinxdoc/sphinx
```
検索すると，様々な先駆者たちが工夫を凝らしたSphinxのイメージが見つかるが，これもよくわからない．試したいくらいの人はまずはsphinxdoc/sphinxで，何か追加したくなったら自分でDockerfileを書き，それでも足りなかったら先駆者たちのを参照すればよいと思われる．

(basicspdoc)=
### sphinxdocの基本コマンド
作業ディレクトリ直下にいるとする．また，後でDockerfileを書いてイメージを作るが，そのとき`sphinxdoc/sphinx`の部分はそのコンテナ名もしくはIDにする．なおこのページは後述のABlogを使用するため以下のコマンドでは生成していないが，一応書いておく．
- プロジェクトの生成
```bash
docker run -it --rm -v $PWD:/docs sphinxdoc/sphinx sphinx-quickstart
```

プロジェクト名など聞かれるので適宜入力する．
```{Note}
ここで，quickstartしたときにソースと同じ階層にビルド先を置くか（デフォルト），ソースとビルド先を別にするか選ぶことができる．
```

- htmlの生成
```bash
docker run --rm -v $PWD:/docs sphinxdoc/sphinx make html
```
もしくは,
```bash
docker run --rm -v $PWD:/docs sphinxdoc/sphinx sphinx-build -b html sourcedir builddir
```
sourcedirはソースファイル置き場，builddirはビルドしたhtmlなどの置き場．

makeコマンドが基本は手軽だが，ソースディレクトリやビルドディレクトリをデフォルトでないところにしたいなど，いろいろいじりたい場合はsphinx-buildで直接指定したほうが楽かもしれない．sphinx-quickstartで生成されたmake.batをいじればそれもmakeでできるのかもしれないがよくわからなかった．

またDockerよくわからないので一応書いておくと，プロジェクトの生成で書いているがhtml生成では書いていないオプション`-it`はinputの`-i` とttyの `-t` をあわせたものである．要はターミナルとかに何か入力する必要があるから書くオプションである．実際にプロジェクトの生成をすると，プロジェクト名とか言語設定など入力を求められる．

以下，イメージのしやすさのためsphinx-quickstart時点での作業ディレクトリ構成を示しておく．ただしこれは`make html`した場合である．
- ソースとビルド先を別ディレクトリにしたとき
```
.
├── Makefile
├── build
│   ├── doctrees
│   └── html
├── make.bat
└── source
    ├── _static
    ├── _templates
    ├── conf.py
    └── index.rst
```
- ソースと同じ階層にビルド先があるとき（デフォルト）
```
.
├── Makefile
├── _build
├── _static
├── _templates
├── conf.py
├── index.rst
└── make.bat
```

### 各種設定
個人的に最低限必須と感じられる設定についてまとめる．一般に，「最低限必須と感じられる」ことは時間とともに増えていくとされている．
#### Jekyll無効化
Github PagesはデフォルトでJekyllをサポートしているため，何もせずSphinxで作成したプロジェクトをpushしてもアンダースコアで始まるファイル等は無視されるらしい．するとウェブページのようなものは表示されるがCSSとかが完全に無視された状態になるらしい．[参考](https://nikkie-ftnext.hatenablog.com/entry/do-you-know-sphinx-ext-githubpages#Sphinx%E3%81%A8GitHub-Pages%E3%82%92%E4%B8%80%E7%B7%92%E3%81%AB%E4%BD%BF%E3%81%86%E3%81%A8%E3%81%8D%E3%81%AE%E8%90%BD%E3%81%A8%E3%81%97%E7%A9%B4)．

そこで.nojekyllというファイルを作成すればこれを回避できるらしい．Sphinxはデフォルトでこれをサポートしている．

具体的には，conf.pyの`extentions`に以下を追記．
```Python
extensions = [
# ... 
 "sphinx.ext.githubpages",
# ...
]
```

#### テーマのインストール
好みのテーマをインストールする．[次節](#settingtheme)参照．

#### 自動ビルド（失敗）
やりたかったができなかった．
```{error}
Dockerfileでsphinx-autobuildをインストールし，ビルドしてhttp://127.0.0.1:8000/にアクセスしても接続できない．適当に検索した情報では原因を突き止めきれず．必須ではないので諦めた．要再確認．
```

#### Markdown対応
Dockerfileでmyst-parserをインストール．
```Dockerfile
RUN python3 -m pip install myst-parser
```
conf.pyに以下を追記．
```Python
extensions = [
# ... 
 "myst_parser",
# ...
]
myst_include = ["*.md"]
```
reSTをもう使わない，Markdown一本で突き進む場合は以下を追記（ここではやっていない）．
```Python
source_suffix = [".rst", ".md"]
```
数式などでいろいろ凝りたい場合は拡張機能を入れることで簡単に解決するかもしれない．[ここ](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-amsmath)を確認してconf.pyに`myst_enable_extensions = ["my_extension"]`で随時追加していく．

(ablog)=
#### ABlogの導入
PyDataテーマはABlogをサポートしているらしいので，インストールしておく．日本語の情報として[ここ](https://water2litter.net/pisco/doc/ablog_start.html)などを参照．
```Dockerfile
RUN python3 -m pip install ablog
```
conf.pyに以下を追記．
```Python
extensions = [
# ... 
 "ablog",
# ...
]
```

#### sphinx-desginの導入
今回使用するPyDataテーマにはいろいろなデザインの何かが仕込まれている．デザインにはまったく興味がないので何も説明できないが，[公式ドキュメント](https://pydata-sphinx-theme.readthedocs.io/en/latest/)を見ていろいろ試すと楽しいのかもしれない．試すには追加で該当パッケージをインストールする必要があるが，sphinx-designを入れておけばだいたい大丈夫と思われる．
```Dockerfile
RUN python3 -m pip install sphinx-design
```
conf.pyに以下を追記．
```Python
extensions = [
# ... 
 "sphinx_design",
# ...
]
```

#### mermaidを使えるようにする
便利．使う可能性が高いので該当パッケージを入れておく．
```Dockerfile
RUN python3 -m pip install sphinxcontrib.mermaid
```
conf.pyに以下を追記．
```Python
extensions = [
# ... 
 "sphinxcontrib.mermaid",
# ...
]
```

#### コードブロックのコピーボタン
```Dockerfile
RUN python3 -m pip install sphinx-copybutton
```
conf.pyに以下を追記．
```Python
extensions = [
# ... 
 "sphinx_copybutton",
# ...
]
```

(dockerfile)=
### 最終的なDockerfile
前項までを踏まえて以下のようなDockerfileでイメージを作成する．
```Dockerfile
FROM sphinxdoc/sphinx

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install pydata-sphinx-theme
RUN python3 -m pip install sphinx-autobuild
RUN python3 -m pip install myst-parser
RUN python3 -m pip install ablog
RUN python3 -m pip install sphinx-design
RUN python3 -m pip install sphinxcontrib.mermaid
RUN python3 -m pip install sphinx-copybutton
```

RUNが続くところはrequirements.txtでやっていればかっこいいらしいが，まあいいかという精神でベタ書きしている．また厳密にはLABELだのENVだの書くべきらしい．

(settingtheme)=
## テーマの設定
Sphinxに元から入っているテーマ（[Sphinx Themes Gallery](https://sphinx-themes.org/)でdefaultとかbuiltinとか書かれているもの）を使用したければ，conf.pyの`html_theme`の部分を使用テーマの名前に書き換えるだけでよい．

今回は，builtinではない[PyDataテーマ](https://pydata-sphinx-theme.readthedocs.io/en/latest/)を使用するのでそれを[前節](#dockerfile)に書いたようにインストールしている必要がある．
```Dockerfile
RUN python3 -m pip install pydata-sphinx-theme
```

conf.pyに以下を記述．
```Python
html_theme = 'pydata_sphinx_theme'
```

少しいじってみた限り，PyDataテーマは個人的にはリッチすぎて使いこなせてない気もするが，他によさそうなものが見つからないのでこれで進める．

どうでもいいが，PyDataテーマのドキュメント自体はJekyll製のように思われる（たぶん）．conf.pyの`extentions`に`"sphinx.ext.githubpages"`がないし，リポジトリのdocs以下を見ると普通にMarkdownファイルが置いてある．よくわからないが，Sphinxはスタイル関連ファイルの作成にのみ使ったということか？

(mypage)=
## ABlogで個人ページ風にする

### ABlogの基本コマンド
PyDataテーマではABlog専用のコマンドを使用しなくとも，通常のコマンドでビルドするだけでブログ的なものを作ることができるようだがよくわからなかった．

ここではABlog専用のコマンドでやっていく．基本的には以下の2つ．
- プロジェクトの生成
```bash
docker run -it --rm -v $PWD:/docs mysphinx ablog start
```

プロジェクト名など聞かれるので適宜入力する．

- htmlの生成
```bash
docker run --rm -v $PWD:/docs mysphinx ablog build
```
もしくは，
```bash
docker run --rm -v $PWD:/docs mysphinx ablog build -s sourcedir -w builddir
```
[sphinxdocの基本コマンド](#basicspdoc)と同様，ソースディレクトリとビルドディレクトリをデフォルトでないところに設定できる．

### 一覧ページの設定
通常のブログのように，全記事の一覧ページが作成される．デフォルトではビルド先に`blog`というディレクトリのindex.htmlである．変更したい場合はconf.pyで以下のように変える．
```Python
# blog_path = "blog"
blog_path = "posts"
```
なおここではデフォルトの`blog`のままとする．

一覧ページのリンクをトップページのヘッダ（ナビゲーションバー？）に置きたいとする．これは，こちらがMarkdownやreSTのソースからSphinxビルドで出したものではないため，外部リンクとして書くほかないような気がする．index.rstに`toctree`とか書いてある部分があり，ここに書いた文書をリストアップしておくのが基本的な書き方として想定されているが，PyDataテーマではあくまでソースディレクトリ内にあるものが`toctree`には入れられるように思われる．そこで普通に外部リンクとして扱う．conf.pyで以下のように書く．
```Python
html_theme_options = {
# ...
  "external_links": [
      {
          "url": "./blog/index.html",
          "name": "Posts",
      }
  ],
# ...
}
```

reST形式のトップページの本文中でリンクを書きたいときは次のようにする．

```rst
`Link to posts <blog/index.html>`_
```
PyDataテーマの公式ドキュメントではわざわざ[ボタンなんかをこしらえている](https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/ablog.html)．

(flow)=
## 最終的な作業フロー
### 初回のみ
#### Dockerイメージ作成
Dockerfileがあるところで以下を実行．
```bash
docker build -t mysphinx .
```
`mysphinx`は好きな名前に．
#### プロジェクト作成
作業ディレクトリ直下で以下を実行．
```bash
docker run -it --rm -v $PWD:/docs mysphinx ablog start
```

(changeouputdir)=
#### ビルド先をdocsに変更
作業ディレクトリ直下で以下を実行．
```bash
mkdir docs
```

#### ソース置き場をsrcに変更
作業ディレクトリ直下で以下を実行．
```bash
mkdir src
```

#### index.rstとconf.pyを移動
作業ディレクトリ直下で以下を実行．
```bash
mv index.rst ./src
mv conf.py ./src
```
もとのビルド先_websiteやその他サンプルファイルも適宜削除．
#### 見た目を整える
[テーマの設定](#settingtheme)や[個人ページ風にする](#mypage)で書いたようなことに加え，ナビゲーションバー，サイドバーなどややこしいことが多くある．そこは各自よいようにやっておく．

#### Git初期化
あなたのGithubリポジトリのURLをyourURLとして，以下を実行．
```bash
git init
git add .
git commit -m "yaruzo"
git remote add origin yourURL
git push -u origin main
```

```{Note}
通常，HTTPSがSSHか選べる．HTTPSにした場合，Githubのアカウントとパスワードの入力を求められるが，パスワードといってもアクセストークンに最近なったらしい．そしてpushのたびに（たぶん）毎回入力が求められる．アクセストークンにはfine-grainedなんたらとPersonal access token(classic)みたいなのと2種類ある．前者は要は権限をいろいろ細かく設定でき，後者も権限をいろいろ設定できるがfine-grainedよりは一括で選択などができるものになっている（たぶん）．

SSHにした場合，いったん鍵の設定をしておけば毎回パスワードの入力などは不要．
```
### 文書作成
書いたらsrcに入れる．タグを入れないとABlogに記事と認識されないので以下のように入れる．なおindex.rst以外基本的にMarkdownで書くとしているのでMarkdownのもの．
```
---
blogpost: true
date: YYYY-MM-DD
author: author1
location: World
category: Theory
tags: tag1,tag2
language: English
---
```

一応，reSTは以下．
```rst
.. post:: YYYY-MM-DD
   :tags: tag1,tag2
   :category: Theory
   :author: author1
   :location: World
   :language: English
```
 以下でもよいらしい．
 ```rst
:blogpost: true
:date: YYYY-MM-DD
:author: author1
:location: World
:category: Theory
:tags: tag1,tag2
:language: English
```
### ビルドする
作業ディレクトリ直下で以下を実行．
```bash
docker run --rm -v $PWD:/docs mysphinx ablog build -s src -w docs
```

### pushする
作業ディレクトリ直下で以下を実行．
```bash
git add .
git commit -m "yattazo"
git push
```
