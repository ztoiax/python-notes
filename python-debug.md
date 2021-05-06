# debug(调试)

## time

- 统计函数运行的时间

```py
from time import time, sleep

start = time()
sleep(1)
end = time()
print('%.2f秒' % (end - start))
```

## timeit

- timeit 统计函数执行的总时间

    - 单位微妙

    - 默认执行100万次

```py
from timeit import timeit

mysetup = 'from math import sqrt'

def mycode():
    sqrt(3)

# test
timeit(setup = mysetup,        # 执行函数的预设
               stmt = mycode,  # 执行函数
               number = 10000) # 执行次数
```

- Timer 生成对象

```py
from timeit import Timer

def mycode():
    sqrt(3)

t = Timer("sqrt(3)", "from math import sqrt")

# 执行10000次
t.timeit(number=10000)
```

- 直接初始化 比 函数初始化要快3倍以上
    ```py
    timeit('a=tuple()')
    timeit('a=()')
    ```
    输出:
    ```
    0.0321451320005508
    0.009014002999720105
    ```
- 3种字符串格式化对比

    > 区别不大

    ```py
    a = '123'
    b = '321'
    print('timeit test {} {}'.format(a,b))
    ```

    ```py
    a = '123'
    b = '321'
    print(f'timeit test {a} {b}')
    ```

    ```py
    a = '123'
    b = '321'
    print('timeit test' + a + b)
    ```
    测试:
    ```py
    timeit('import test')
    timeit('import test1')
    timeit('import test2')
    ```
    输出:
    ```
    0.07623226299995167
    0.076570758999992
    0.07589723899997125
    ```

- 列表,元组,集合添加元素性能对比:
    > 列表 快于 集合 快于 元组

    ```py
    def list_test():
        list1 = []
        for i in range(10):
            list1.append(i)

    def tuple_test():
        tuple1 = ()
        for i in range(10):
            tuple1 += (i,)

    def set_test():
        set1 = set()
        for i in range(10):
            set1.add(i)

    timeit(stmt = list_test, number = 10000)
    timeit(stmt = tuple_test, number = 10000)
    timeit(stmt = set_test, number = 10000)
    ```
    输出:
    ```
    0.005410605000179203
    0.007548831999883987
    0.006166948000100092
    ```

- 字典的key, 列表的值.相同情况下的循环对比

    > 区别不大

    ```py
    list1 = ['linux', 'xueshu', 'library', 'social', 'waiguosocial', 'video', 'shop', 'search', 'wiki', 'network']

    dict1 = {'linux': 'linux', 'xueshu': 'xueshu', 'library': 'library', 'social': 'social', 'waiguosocial': 'waiguosocial', 'video': 'video', 'shop': 'shop', 'search': 'search', 'wiki': 'wiki', 'network': 'network'}

    def list_test():
        for i in list1:
            print(i)

    def dict_test():
        for i in dict1:
            print(i)

    timeit(stmt = list_test, number = 10000)
    timeit(stmt = dict_test, number = 10000)
    ```

- 对比3种方法获取字典值: if, get(), try

    > 区别不大

    测试文件:test.py
    ```py
    # file test.py

    key = 'a'
    if key in items:
        v = items[key]
    else:
        v = None
    ```
    测试文件:test1.py
    ```py
    # file test1.py
    v = items.get(key)
    ```
    测试文件:test2.py
    ```py
    # file test2.py

    items = {'a': 1, 'b': 2, 'c': 3}
    key = 'n'
    try:
        v = items[key]
    except KeyError:
        v = None
    ```

    测试:
    ```py
    items = {'a': 1, 'b': 2, 'c': 3}
    key = 'a'
    timeit('import test')
    timeit('import test1')
    timeit('import test2')
    ```
    输出:
    ```
    0.07695441999931063
    0.07400108000001637
    0.07423666900012904
    ```

    把key换成字典之外的值
    ```py
    key = 'n'
    ```
    输出:
    ```
    0.07498021500032337
    0.07673525599966524
    0.07963845299946115
    ```

- from 导入比import 导入要快

    > 如果使用math.sqrt(), 解释器首先需要找到math模块,再去找对应的sqrt()方法

    - sqrt() 比 math.sqrt() 快1.5到2倍

    ```py
    timeit('math.sqrt(9)', 'import math')
    timeit('sqrt(9)', 'from math import sqrt')
    ```
    输出:
    ```
    0.06219652999971004
    0.030946962999678362
    ```

## 面向对象的性能损耗

- 单独使用字典赋值比对象内部赋值快3倍, 而使用`__slots__` 快15%

    测试文件test.py:
    ```py
    # file test.py
    class test():
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
    ```
    测试文件test1.py:
    ```py
    # file test1.py
    class test1():
        __slots__ = ['a', 'b', 'c']
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
    ```

    测试:
    ```py
    timeit("r = test(1, 2, 3)", 'from test import test')
    timeit("r = test1(1, 2, 3)", 'from test1 import test1')
    timeit("r = {'a': 1, 'b': 2, 'c': 3}")
    ```
    输出:
    ```
    0.2395006189999549
    0.20651085099962074
    0.07340252900030464
    ```

- 值计算对比

    > 对象内部的字典快于 __slot__() 和 直接字典计算

    ```py
    # test.py
    code = 'r.a * r.b * r.c'
    setup = '''
    from test import test
    r = test(1, 2, 3)'''

    timeit(setup=setup, stmt=code)

    # test1.py
    code = 'r.a * r.b * r.c'
    setup = '''
    from test1 import test1
    r = test1(1, 2, 3)'''

    timeit(setup=setup, stmt=code)

    # test2.py
    timeit("r['a'] * r['b'] * r['c']", "r = {'a': 1, 'b': 2, 'c': 3}")
    ```
    输出:
    ```
    0.08434765600009086
    0.10209759400004259
    0.10072487599995839
    ```

## cProfile

```py
import cProfile

a = []
def test():
    for i in range(10000):
        a.append(i)

cProfile.run('test()')
```
输出:能看到一共1004个函数,以及每个函数的执行次数
```
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.000    0.000 <stdin>:2(test)
    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
 1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

- pstat

    > 查看执行时间

```py
import pstat

profiler = cProfile.Profile()
profiler.enable()
test()              #测试函数
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('ncalls')
stats.print_stats()
```


## [Scalene](https://github.com/emeryberger/scalene)

> 适用于 Python 的高性能，高精度 CPU 和内存分析器

> 注意: gpu的分析,只支持nvidia

```py
import psutil
from subprocess import PIPE
p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
p.name()
```

## [pysnooper](https://github.com/cool-RR/PySnooper)

## [vardbg](https://github.com/CCExtractor/vardbg)
