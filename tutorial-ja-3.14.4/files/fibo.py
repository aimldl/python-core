# fibo.py
#   source: https://docs.python.org/ja/3.14/tutorial/modules.html

def fib(n):
    """nまでのフィボナッチ数を出力する"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """nまでのフィボナッチ数を返す"""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

