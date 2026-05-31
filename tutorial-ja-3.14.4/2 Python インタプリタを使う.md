# [2. Python インタプリタを使う](https://docs.python.org/ja/3.14/tutorial/interpreter.html)

```
python3.14
```

Bad example

```
aimldl@my-MacBookAir % python
zsh: command not found: python
aimldl@my-MacBookAir %
```

Good example
```
aimldl@my-MacBookAir % python3
  ...
```  

## [2.1. インタプリタを起動する](https://docs.python.org/ja/3.14/tutorial/interpreter.html#invoking-the-interpreter)

```
python3 < filename
```
* ファイル名を引数に指定するか、python3 < filename のように標準入力ファイルとして指定すると、インタプリタはファイルから スクリプト を読み込んで実行します。
* インタプリタは Unix シェルと同じように使えます。標準入力が端末に接続された状態では、コマンドを対話的に読み込んで実行します。

```
python -c command [arg] ...
```

* インタプリタを python -c command [arg] ... のように起動する方法もあります。この形式では、シェルの -c オプションと同じように、 command に指定した文を実行します。 Python 文には、スペースなどのシェルにとって特殊な意味をもつ文字がしばしば含まれるので、 command 全体をクォート(訳注: ')で囲っておいたほうが良いでしょう。

Python のモジュールには、スクリプトとしても便利に使えるものがあります。 python -m module [arg] ... のように起動すると、 module のソースファイルを、フルパスを指定して起動したかのように実行できます。

### [2.1.2. 対話モード](https://docs.python.org/ja/3.14/tutorial/interpreter.html#interactive-mode)

```
aimldl@my-MacBookAir % python3
Python 3.9.6 (default, Apr  7 2026, 02:38:40) 
[Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

```
>>> exit()
aimldl@my-MacBookAir %
```
