from functools import lru_cache # 引数に紐づけて関数の結果をキャッシュできるモジュールー＞同じ引数で関数が呼び出された時２買い目以降は関数の呼び他しを行わず、保存しておいた戻り値を使うようになる
#＠高階関数
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print([fib(n) for n in range(16)])
