<!-- vim-markdown-toc GFM -->

* [python](#python)
    * [环境配置](#环境配置)
        * [交互更友好的解释器](#交互更友好的解释器)
        * [pip 包管理器](#pip-包管理器)
        * [pyenv](#pyenv)
        * [常用命令:](#常用命令)
    * [python 慢的原因](#python-慢的原因)
        * [python加速计划](#python加速计划)
    * [import and from](#import-and-from)
    * [if](#if)
        * [assert](#assert)
        * [try, except](#try-except)
        * [PEP 572: 海象运算符(:=)](#pep-572-海象运算符)
        * [三元运算符(Ternary)](#三元运算符ternary)
    * [while, for(循环)](#while-for循环)
        * [enumerate() index的语法糖](#enumerate-index的语法糖)
        * [iter(迭代器)](#iter迭代器)
            * [itertools模块](#itertools模块)
        * [yield(生成器)](#yield生成器)
            * [yield from(递归生成器)](#yield-from递归生成器)
            * [通过send() 唤醒yield, 类似协程](#通过send-唤醒yield-类似协程)
                * [通过yield和send实现角色模型](#通过yield和send实现角色模型)
        * [zip() 迭代多个对象](#zip-迭代多个对象)
    * [match case(模式匹配): 需要python 3.10](#match-case模式匹配-需要python-310)
    * [函数式编程](#函数式编程)
        * [map()](#map)
        * [filter(): 过滤](#filter-过滤)
        * [reduce()](#reduce)
        * [fib(斐波那契)](#fib斐波那契)
            * [循环 while, for](#循环-while-for)
            * [迭代](#迭代)
            * [泛函](#泛函)
            * [tuple(元组)](#tuple元组)
        * [pi(圆周率)](#pi圆周率)
        * [黄金分割](#黄金分割)
        * [树形递归](#树形递归)
        * [平方根](#平方根)
        * [rlist(序列)](#rlist序列)
    * [数据类型](#数据类型)
        * [基本概念](#基本概念)
        * [动态类型](#动态类型)
        * [str(字符串)](#str字符串)
            * [print()](#print)
            * [format()](#format)
            * [4种字符串格式化方法](#4种字符串格式化方法)
            * [string模块](#string模块)
            * [io模块的StringIO, BytesIO](#io模块的stringio-bytesio)
        * [list(列表)](#list列表)
            * [Queue(队列)](#queue队列)
            * [CircularQueue(环形队列)](#circularqueue环形队列)
            * [Deque(双向链表)](#deque双向链表)
            * [array 模块](#array-模块)
            * [bisect(二分排序列表)](#bisect二分排序列表)
            * [headp: 堆](#headp-堆)
                * [优先级队列](#优先级队列)
        * [tuple(元组)](#tuple元组-1)
            * [namedtuple](#namedtuple)
        * [Dictionaries(字典)](#dictionaries字典)
            * [collections模块](#collections模块)
        * [set(集合)](#set集合)
        * [图](#图)
        * [静态类型(static type)](#静态类型static-type)
            * [静态类型检查工具:mypy](#静态类型检查工具mypy)
            * [静态类型检查工具:pytype](#静态类型检查工具pytype)
            * [基本使用](#基本使用)
    * [sorted](#sorted)
    * [def(函数)](#def函数)
        * [闭包(closure)函数](#闭包closure函数)
        * [参数`*argv`, `**kwargs`](#参数argv-kwargs)
        * [内置函数,属性](#内置函数属性)
        * [装饰器(decorator)](#装饰器decorator)
            * [类装饰器](#类装饰器)
        * [functools模块](#functools模块)
    * [class(类)](#class类)
        * [继承](#继承)
        * [多重继承](#多重继承)
        * [@dataclass(简化类的定义)](#dataclass简化类的定义)
        * [元类(metaclass)](#元类metaclass)
        * [内置函数,属性](#内置函数属性-1)
        * [class的内置装饰器](#class的内置装饰器)
        * [@property类装饰器的方法: getattr(), setattr()](#property类装饰器的方法-getattr-setattr)
        * [`__enter__()`, `__exit__()`: 定义with上下文](#__enter__-__exit__-定义with上下文)
        * [`__getitem__` 和 `__class_getitem__`: 定义带[]的调用 `object['arg']`](#__getitem__-和-__class_getitem__-定义带的调用-objectarg)
        * [`__getattribute__`: 当访问不存在的属性时调用](#__getattribute__-当访问不存在的属性时调用)
        * [functools.partialmethod() 只能封装是类里的方法](#functoolspartialmethod-只能封装是类里的方法)
        * [描述器](#描述器)
            * [实现类的参数类型检查](#实现类的参数类型检查)
    * [weakerf(弱引用)](#weakerf弱引用)
    * [file](#file)
        * [readinto()](#readinto)
        * [hdf5](#hdf5)
        * [自定义数据块读写, 而不是行读写](#自定义数据块读写-而不是行读写)
        * [读写压缩文件](#读写压缩文件)
        * [json](#json)
        * [yaml](#yaml)
        * [toml](#toml)
        * [ini](#ini)
        * [pickle](#pickle)
            * [pickletools](#pickletools)
        * [shelve](#shelve)
        * [pathlib](#pathlib)
        * [os](#os)
    * [日志](#日志)
        * [logging](#logging)
        * [loguru](#loguru)
    * [lib(库)](#lib库)
        * [time](#time)
        * [re(正则表达式)](#re正则表达式)
        * [fnmatch(列表匹配)](#fnmatch列表匹配)
        * [Image](#image)
        * [pynput.keyboard(自动输入)](#pynputkeyboard自动输入)
        * [pyautogui(自动化键盘, 鼠标)](#pyautogui自动化键盘-鼠标)
        * [cursesmenu(tui)](#cursesmenutui)
        * [itchat: 微信库](#itchat-微信库)
        * [wxpy: 微信自动化](#wxpy-微信自动化)
        * [pyecharts: python ECharts数据可视化](#pyecharts-python-echarts数据可视化)
        * [hashlib](#hashlib)
        * [pyodide: 把python编译成wasm, 在浏览器上运行](#pyodide-把python编译成wasm-在浏览器上运行)
        * [locust: web自动化压力测试](#locust-web自动化压力测试)
    * [cython](#cython)
    * [mingshe: 语法糖](#mingshe-语法糖)
    * [PEP 20: pythonic(python之禅)](#pep-20-pythonicpython之禅)
    * [test: 测试](#test-测试)
    * [draw: 画图](#draw-画图)
    * [system: 系统编程](#system-系统编程)
    * [concurrency: 进程, 线程, 协程](#concurrency-进程-线程-协程)
    * [scientific computing: 科学计算](#scientific-computing-科学计算)
    * [network: 网络](#network-网络)
    * [spider: 网络爬虫和自动化测试](#spider-网络爬虫和自动化测试)
    * [debug: 调试](#debug-调试)
    * [algorithms: 算法](#algorithms-算法)
    * [Design Pattern: 设计模式](#design-pattern-设计模式)
* [reference article(优秀文章)](#reference-article优秀文章)
* [第三方软件资源](#第三方软件资源)

<!-- vim-markdown-toc -->

# python

- 强类型的动态类型语言

- 编程语言流行排行榜:python在以下排行榜都是第一

    - [TIOBE](https://www.tiobe.com/tiobe-index/)

    - [PYPL](https://pypl.github.io/PYPL.html)

        - 根据Google搜索的排行榜

    - [IEEE](https://spectrum.ieee.org/top-programming-languages/#toggle-gdpr)

    - [O'reilly](https://www.oreilly.com/radar/where-programming-ops-ai-and-the-cloud-are-headed-in-2021/)

- [编程语言benchmarks](https://github.com/kostya/benchmarks)

## 环境配置

### 交互更友好的解释器

- [ptpython](https://github.com/prompt-toolkit/ptpython)比[ipython](https://github.com/ipython/ipython)更好

- [jupyter notebooks](https://github.com/jupyterhub/jupyterhub)
    > 可以显示plot画的图

- [nbterm](https://github.com/davidbrochart/nbterm)
    > 在终端下的jupter notebooks

- [在线jupyter(需要科学上网)](https://colab.research.google.com/notebooks/intro.ipynb#recent=true)

### pip 包管理器

- `pip install pkg` 普通用户的安装路径:

    `~/.local/lib/python3.9`

- `sudo pip install pkg` sudo表示全局的安装路径:

    - 有些模块像`scapy`需要root权限. 有些模块会破坏依赖, 因此不能使用sudo安装

    `/usr/lib/python3.9/`

- 安装过程:

    - 先`build`, 后`install` 两个阶段是分开的, 可以由不同的工具完成

        - 1.`build`: 把源码构建为wheel(.whl文件)

        - 2.`install`: 把wheel解压, 将文件移动到对应的目录

            - pypi有些包, 操作系统提供wheel的下载(可以跳过build), 而有些则需要build

            - wheel的文件小于源代码

            - `--no-binary=:all:` 参数告诉pip即使有wheel文件, 也要下载源码进行本地构建
            ```py

            pip install \
            --no-binary=:all: \
            package
            ```


        ![image](./imgs/pip-install.png)

        [视频:明希 - Python 打包 101](https://www.bilibili.com/video/BV1Db4y1h7Xx/?spm_id_from=333.788.recommend_more_video.0)

- PEP660: editable build backend
    - 修改源代码后不需要构建wheel, 即可使用, 但python程序还需重启(接近热更新)
    ```sh
    pip install -e .
    ```
    - 目前backend使用`pdm` 的代理模式


### pyenv

> 多版本共存或相互隔离

- 安装两个包: `pyenv` `pyenv-virtualenv`

```bash
# 获取可安装的版本
pyenv install --list

# 安装2.7.18版本
pyenv install -v 2.7.18

# 查看当前版本和可选版本
pyenv versions

pyenv global 2.7.18
```

- virtualenv:

    - 能管理纯python库, 但不能管理拓展库

    - 不能管理python本身的编译

    - pip 也是独立的环境

```bash
# 终端1
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv virtualenv 2.7.13 first
pyenv activate first

# 终端2
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv virtualenv system second
pyenv activate second
```

```py
# 删除虚拟环境
pyenv virtualenv-delete first
pyenv virtualenv-delete second
```

![image](./imgs/virtualenv.png)

### 常用命令:

```bash
# 转换json格式
echo '{"1": "123", "2": "321"}' | python -m json.tool

# 共享当前目录下的文件
python -m http.server 8080

# 浏览器查看文档
python -m pydoc -p 1234

# 监控文件变动
python -m pyinotify -v /tmp

# 打开网页
python -m webbrowser -t "http://www.python.org"

# 生成pem, key证书文件
pip install trustme
python -m trustme -i baidu.com
```

## python 慢的原因

> 官方的 python 版本是 cpython

> CPython 会对代码进行一系列的读取、语法分析、解析、编译、解释和执行的操作。

- GIL(Global Interpreter Lock)全局解释器锁:

  - 解决多线程, 异步编程中变量的死锁问题

  - 变量使用引用计数,次数为 0 时则释放内存

  - GIL只影响重cpu的程序, 对于重io的程序是不影响的

  - 当多个线程共享变量, 每次只能一个线程操作变量, 导致并发效率降低

  - PEP554: 子解释器(subinterpreters) 解决GIL锁低并发问题:

    - 每个进程有独立的解释器以及GIL

    - 子解释器: 进程内部也可以有多个独立的解释器以及GIL

        - 子解释器之间的资源通信: 使用`pickle verison 5` 把资源序列化, 然后通过共享内存进行传输

            ![image](./imgs/subinterpreters.png)

            - 全局变量不能被其它子解释器访问

            - 开销: 子解释器的初始化

                - 要把模块导入到另一个命名空间

                - ...

- JIT(Just-in-time):

  - 原理:

    - 1.通过一种中间语言, 将代码拆分成多个块

    - 2.运行时依然使用字节码, JIT并没有提升字节码的运行速度

    - 3.而是分析哪些代码会多次运行, 并标记为热点(hot spots), 最后对这些热点进行优化

  - 缺点:

    - 1.启动时间慢: cpython 本身的启动时间就很慢, 使用了JIT的pypy启动时间还要慢2-3倍

    - 2.动态语言很难优化

        - 比较和转换类型的成本很高，每次读取、写入或引用变量时，都会检查类型

- Cython: 牺牲灵活性, 换取性能

- Jpython: java 实现

  > Jython中的Python线程, 就是Java线程, 由JVM管理

  - [ ] GIL
  - [ ] JIT

  - 有两种执行方式

    - 生成java字节码, 在jvm上执行

    - 生成python字节码, 在jvm上的python解释器上执行

    ![image](./imgs/jython.png)

- Cpython:库是 C 写的

  - [x] GIL:没有使用引用计数
  - [ ] JIT

- [PyPy](https://doc.pypy.org/en/latest/faq.html):比 cpython2.7 版块 3 倍.库是 RPython 写的

  - [x] GIL
  - [x] JIT

- [Pyodide](https://github.com/pyodide/pyodide): 转换成WebAssembly在浏览器运行

- [更多python解释器](https://wiki.python.org/moin/PythonImplementations)

- [Why is Python so slow?](https://medium.com/hackernoon/why-is-python-so-slow-e5074b6fe55b)

- [不同python版本的性能对比](https://hackernoon.com/which-is-the-fastest-version-of-python-2ae7c61a6b2b)

### python加速计划

- [Implementation plan for speeding up CPython](https://github.com/markshannon/faster-cpython/blob/master/plan.md)

    - 微软资助的5人开发团队(包括python之父)

    - 要让cpython提升5倍, 分为4个阶段:

    - (1) 3.10 不再生成运行时代码
    - (2) 3.11 缩小int类型的位数; 提升运算符, 调用和返回的速度; 改进内存布局, 减少内存管理开销; 零开销的异常处理...
    - (3) 3.12 增加JIT
    - (4) 3.13 生成高级机械语言

    ![image](./imgs/faster.png)


    - 最终目标是加几个[执行层(tiers)](https://github.com/markshannon/faster-cpython/blob/master/tiers.md)

        - 程序分为两部分:

            - 热的(经常执行的): 只要执行速度提升, 即使加载慢一些, 消耗多一点内存也是有意义的

            - 冷的(不经常执行的): 只要加载速度提升, 即使执行慢一些, 也是有意义的

        - 冷热并不容易区分开了, 为了解决这一冷热范围的运行时特征(characteristics), 就要加入执行层

        - 目前考虑0-3层, 层数越高, 代码越热:

            - cpython3.9被视为0-1层之间

            - 开始时, 所有代码都是0层, 随着运行时间的增长进入更高层

            - 0层: 更少的磁盘加载到内存的成本, 更少的内存使用

                - 只运行一次和从不运行的代码, 超过1次进入1层

                    - 比如: 加载模块, 异常处理...

            - 越往高层, 有着更多的优化, 对资源的使用限制更少

## import and from

file test:

```py
# 文件test
__all__ = ['a']
a = 1
b = 2
```

- `import` 用法

> 创建新namespace, 只会加载一次

> 注意:import只在函数里有效

file test1:

```py
# 文件test1
import test
print(test.a)
print(test.b)
```

- `from module import name, name1` 用法

> 在当前 `namespace` 引用

> 注意:from不能在`class`, `function`里使用

```py
a = 0
from test import *

# a的值会被覆盖
print(a)

# __all__ = ['a']因为导入文件没有指定b,所以会报错
print(b)

# 此时再导入b
from test import b
print(b)
```

- from导入函数应使用`()` 代替`\`

    ```py
    # 两者一样
    from timeit import timeit, repeat, \
                        main, reindent

    from timeit import (timeit, repeat,
                        main, reindent)
    ```
    - 注意只能在from语句可以使用(), import 则会报错

        ```py
        import timeit, sys,\
                time, re

        # 报错
        import (timeit, sys,
                time, re)
        ```

## if

| 正确写法                       | 错误写法        |
|--------------------------------|-----------------|
| `if not v:` or `if v is None:` | `if v == None:` |
| `if v:`                        | `if v != None:` |

判断变量是否定义: `if 'v' in locals():`

- or 赋值

    ```py
    b = None
    c = None

    # v = 1
    v = b or 1 or c
    ```
    - False, True

    ```py
    age = False
    s = age or 24
    print(s)

    age = True
    s = age or 24
    print(s)
    ```
    输出
    ```
    24
    True
    ```

### assert

```py
x = 1

# 异常
assert x > 1
```

- 自定义异常

```py
class Myerror(Exception):
    def __str__(self):
        return 'define error'

def f():
    raise Myerror()

try:
    f()
except Myerror:
    print('ok')
```

- 加入参数
```py
class Myerror(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status

    def __str__(self):
        return 'define error'

def f():
    raise Myerror('error', 1)

try:
    f()
except Myerror as e:
    print(e.args)
```


### try, except

- 使用`Exception` 捕抓所有异常

    - 这三个异常SystemExit, KeyboardInterrupt, GeneratorExit除外, 如果要捕抓这三个使用`BaseException`

```py
except Exception as e:
```

- 在异常内, 抛出异常
```py
def example():
    try:
        int('N/A')
    except ValueError as e:
        # raise ... from e
        raise RuntimeError('A parsing error occurred') from e

example()
```

- 处理多个异常
```py
try:
    client_obj.get_url(url)
except (URLError, ValueError, SocketTimeout):
    client_obj.remove_url(url)
```

- 对不同的异常, 进行不同的处理
```py
try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url(url)
except SocketTimeout:
    client_obj.handle_url_timeout(url)
```

```py
try:
    f = open(filename)
except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error('File not found')
    elif e.errno == errno.EACCES:
        logger.error('Permission denied')
    else:
        logger.error('Unexpected error: %d', e.errno)
```

### [PEP 572: 海象运算符(:=)](https://www.python.org/dev/peps/pep-0572/)

- 1.运行b函数
- 2.赋值a
- 3.判断a是否为`None`

```py
def b():
    return 'not None'

# 普通写法
a = b()
if (a):
    print(a)

# 海象运算符
if (a := b()):
    print(a)
```

```py
def f(x):
    return x + 1


data = [1, 2, 3]

# 普通写法
results = []
for x in data:
    result = f(x)
    if result:
        results.append(result)

# 普通写法1
results = [
    f(x) for x in data
    if f(x)
]

# 海象运算符
results = [
    y for x in data
    if (y := f(x))
]
```

```py
# f(x)赋值y
stuff = [[y := f(x), x * y] for x in range(3)]
```

### 三元运算符(Ternary)

```py
# False选第一个元素
state = False
array = ('0', '1', '2')[state]
print(array)

# True选第二个元素
state = True
array = ('0', '1', '2')[state]
print(array)
```
输出
```
0
1
```

## while, for(循环)

- python3的 `range` 代替 python2 的`xrange`

- 定义: 起点, 终点, 步进
    ```py
    for i in range(1, 12, 2):
        print(i)

    # 步进为负数, 表示反转(reverse)
    for i in range(12, 1, -2):
        print(i)

    for i in range(10_000, 1_000_001, 20_000):
        print(i)
    ```

- `*` 运算符
    ```py
    for a, *b in ([1, 2], [3, 4, 5]):
        print(a)
        print(b)
    ```
    - 输出
    ```
    1
    [2]

    3
    [4, 5]
    ```

### enumerate() index的语法糖

- 基本使用
    ```py
    list1 = [0, 1, 2]

    # 普通写法. pythonic(这很不python)
    for index in range(len(list1)):
        print(index, n[index])

    # enumerate()语法糖
    for index, n in enumerate(list1):
        print(index, n)
    ```
    输出:
    ```
    0 0
    1 1
    2 2
    ```

- `enumerate(array, 1)` : 第二个参数表示对index + 1

    ```py
    for index, n in enumerate(list1, 1):
        print(index, n)
    ```
    输出:
    ```
    1 0
    2 1
    3 2
    ```

### iter(迭代器)

- iter()

```py
list1 = [0, 1, 2]
it = iter(list1)

next(it) # 0
next(it) # 1
next(it) # 2
next(it) # StopIteration
```

- `__iter__()` 将迭代请求传递给内部的 `_list` 属性
- `__next__()` 返回下一个迭代

- 迭代文件的每一行

```py
# 相当于cat /home/tz/test.py

with open('/home/tz/test.py') as file:
    while True:
        try:
            line = next(file)
            print(line)
        except StopIteration:
            exit(0)
```

- iter() 控制读取大小

```py
import sys

with open('/home/tz/test.py') as file:
    # 每次读10
    for chunk in iter(lambda: file.read(10), ''):
        sys.stdout.write(chunk)
```

- iter() 实现`range()`

```py
class range:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return self

    def __next__(self):
        if self.x <= self.y:
            x = self.x
            self.x += 1
            return x
        else:
            raise StopIteration


a = range(1, 10)
for i in a:
    print(i)
```

#### itertools模块

- [itertools模块代码](https://docs.python.org/3/library/itertools.html#itertools.product)

- islice() 实现切片
    ```py
    from itertools import islice

    # 等同于a[1:6]
    a = range(1, 10)
    for i in islice(a, 1, 6):
        print(i)
    ```

- permutations() 组合所有元素(不包含自身)
    ```py
    from itertools import permutations

    list1 = ['a', 'b', 'c']
    for i in permutations(list1):
        print(i)
    ```
    输出
    ```
    ('a', 'b', 'c')
    ('a', 'c', 'b')
    ('b', 'a', 'c')
    ('b', 'c', 'a')
    ('c', 'a', 'b')
    ('c', 'b', 'a')
    ```

    - 定义组合的数量
    ```py
    from itertools import permutations

    list1 = ['a', 'b', 'c']
    for i in permutations(list1, 2):
        print(i)
    ```
    输出
    ```
    ('a', 'b')
    ('a', 'c')
    ('b', 'a')
    ('b', 'c')
    ('c', 'a')
    ('c', 'b')
    ```

- combinations_with_replacement() 组合所有元素(包含自身)
    ```py
    from itertools import combinations_with_replacement

    list1 = ['a', 'b', 'c']
    for i in combinations_with_replacement(list1, 3):
        print(i)
    ```

<span id="zip_longest"></span>
- zip_longest() 解决两个对象元素不等

    ```py
    from itertools import zip_longest

    # 对象元素不等
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40, 50]

    # 设置填充元素的值为0
    for i in zip_longest(list1, list2, fillvalue=0):
        print(i)
    ```

- chain() 更好的 for x in list1 + list2:
    ```py
    from itertools import chain

    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40]

    for x in chain(list1, list2):
        print(x)
    ```
    输出
    ```
    1
    2
    3
    4
    10
    20
    30
    40
    ```

### yield(生成器)

- 返回一个迭代器, 函数会暂停运行

    - 生成器和普通函数不同, 只能用于迭代操作

- `next()` 或 `__next__()`迭代下一次

```py
def count(start, stop):
    while True:
        yield start
        start += stop

yd = count(10, 1)
yd.__next__()
next(yd)
```

- yield 实现fib
```py
class fib:
    def __init__(self, n):
        self.x, self.y = 0, 1
        self.n = n

    def __iter__(self):
        x, y = self.x, self.y
        while y <= self.n:
            x, y = x + 1, y + x
            yield y


a = fib(10)
for i in a:
    print(i)
```

- yield 实现grep

```py
def grep(pattern, filename):
    with open(filename) as file:
        for line in file.readlines():
            if pattern in line:
                yield line

get_elem = grep('2', '/tmp/test')

# 迭代下一次
get_elem.__next__()
next(get_elem)
```

#### yield from(递归生成器)

```py
from collections import Iterable


def flatten(items):
    for x in items:
        # 如果x是生成器, 就迭代自身
        if isinstance(x, Iterable):
            yield from flatten(x)
        else:
            yield x


list1 = [1, 2, [3, 4, [5, 6], 7], 8]

# 输出 1 2 3 4 5 6 7 8
for x in flatten(list1):
    print(x)
```

#### 通过send() 唤醒yield, 类似协程

> send()函数向yield函数传递值

```py
def f():
    while True:
        n = yield
        print(n)

# test
r = f()

# send之前需要__next__()
r.__next__()
r.send('hello')
r.send('world')
```
输出
```
hello
world
```

- 通过装饰器包一层函数,让它自动__next__()
```py
def wrapper(func):
    def new_func():
        r = func()
        r.__next__()
        return r
    return new_func

# 消费者
@wrapper
def consumer():
    while True:
        # 接送producer
        n = yield
        print(n)

# 生产者
def producer(n):
    r = consumer()
    for i in range(n):
        # 发送给consumer
        r.send(i)

if __name__ == '__main__':
    producer(10)
```

- send()给自己

```py
# 即是生产者也是消费者
@wrapper
def producer():
    while True:
        n = yield
        if n == 0:
            break
        print(n)
        try:
            # 发送给自己
            my = producer()
            my.send(n-1)
        except StopIteration:
            pass

if __name__ == '__main__':
    r = producer()
    r.send(10)
```

- 生产者负责控制步进, 消费者负责print()

```py
# 消费者负责print()
@wrapper
def consumer():
    while True:
        # 接送生产者
        n = yield
        print(n)

# 生产者负责控制步进
@wrapper
def producer():
    while True:
        n = yield
        if n == 0:
            break
        try:
            # 发送给消费者
            r = consumer()
            r.send(n)

            # 发送给自己
            my = producer()
            my.send(n-1)
        except StopIteration:
            pass

if __name__ == '__main__':
    r = producer()
    r.send(10)
```

- yield返回值(生成器)
```py
def f():
    m = None
    while True:
        line = yield m
        m = line.split(',')

# test
r = f()
r.__next__()
r.send('123,321')
```
##### 通过yield和send实现角色模型
```py
from collections import deque

class ActorScheduler:
    def __init__(self):
        # 字典保存actor
        self._actors = {}
        # 使用双向链表保存(actor, msg)
        self._msg_queue = deque()

    # 注册actor
    def new_actor(self, name, actor):
        self._msg_queue.append((actor, None))
        self._actors[name] = actor

    # actor发送给双向链表, 保存(actor, msg)
    def send(self, name, msg):
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                # 发送msg给对应actor. actor函数使用yield作为接收
                actor.send(msg)
            except StopIteration:
                pass


def consumer():
    while True:
        # 接收run方法的send
        n = yield
        print('got:', n)

def producer(sched):
    while True:
        # 接收run方法的send
        n = yield
        # 退出
        if n == 0:
            break
        # 发送给consumer
        sched.send('consumer', n)
        # 发送给自己, 自己也是consumer
        sched.send('producer', n-1)


if __name__ == '__main__':
    sched = ActorScheduler()
    sched.new_actor('consumer', consumer())
    sched.new_actor('producer', producer(sched))

    sched.send('producer', 5)
    sched.run()
```
输出
```
got: 5
got: 4
got: 3
got: 2
got: 1
```

### zip() 迭代多个对象

- 两个index, 迭代两个对象
```py
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

for x, y in zip(list1, list2):
    print(x, y)
```
输出
```
1 10
2 20
3 30
4 40
```

- 只有单个index的时候, 输出元组
```py
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

for i in zip(list1, list2):
    print(i)
```
输出
```
(1, 10)
(2, 20)
(3, 30)
(4, 40)
```

- [itertools.zip_longest() 解决两个对象元素不等的情况](#zip_longest)

## match case(模式匹配): 需要python 3.10

- [PEP634: Specification](https://www.python.org/dev/peps/pep-0634/)

- [PEP635: Motivation and Rationale](https://www.python.org/dev/peps/pep-0635/)

- [视频: 谭啸 - 如何用好 Python 的模式匹配语法](https://www.bilibili.com/video/BV1Nb4y1a7zV?spm_id_from=333.788.dynamic.content.click)

- `switch case`匹配
    ```py
    def http_error(status):
        match status:
            case 400:
                return "Bad request"
            case 401 | 403 | 404:
                return "Not allowed"
            case _:
                return "Something's wrong with the Internet"
    ```

- 参数匹配:
    ```py
    import sys

    match sys.argv[1:]:
        case 'add', k, v:
            print('add', k, v)
        case _:
            print('不合法输入')

    ```
    - 输出
    ```sh
    ./test.py add name tz
    add name tz

    ./test.py abc
    不合法输入
    ```

- 匹配对象:

    - 1.数组
    ```py
    # 以下三种case的语义相同
    match [1, 2 ,3]:
        case x, y, z:
            pass
        case [x, y, z]:
            pass
        case (x, y, z):
            pass

    # _省略单个元素, *_省略后面所有元素
    match [1, 2 ,3]:
        case x, _, _:
            pass
        case x, *_,:
            pass
    ```
    - 2.字典:
    ```py
    # 可以使用**kwargs
    match {'x': x ,'y': y}:
        case {'x': x, 'y': y}:
            pass
        case {'x': x, **kwargs}:
            pass
        case {**kwargs}:
            pass
    ```
    - 3.class:
    ```py
    from dataclasses import dataclass

    class o:
        x: int = 1
        y: int = 1

    class o2:
        __match_args__ = ("x", "y")
        def __init__(self):
            self.x: int = 0
            self.y: int = 0

    @dataclass
    class o2:
        x: int = 0
        y: int = 0

    class o3:
        x: int = 0
        y: int = 0

    def f(subject):
        match subject:
            # 判断subject是不是o类, 以及x, y是否等于1
            case o(x=1, y=1):
                print('1')

            # 需要定义__match_args__ 或者使用@dataclass
            case o2(x, y):
                print('2')

            # object表示duck type(任何class)
            case object(x=x, y=y):
                print('3')

    f(o())
    f(o2())
    f(o3())
    ```
    - 输出
    ```
    1
    2
    3
    ```



- 值匹配:

    - 判断类的值
    ```py
    # o类来自上面例子
    a = o()

    match (1, 1):
        case (a.x, a.y):
            pass

    match (1, 1):
        # case先执行, if后执行
        case (a.x, a.y) if a.x > 0:
            pass
    ```

    - 普通变量的值会被改写
    ```py
    x, y = 0, 0

    match (1, 1):
        # 会改写为1
        case (x, y):
            print(x, y)
    ```
    - 输出
    ```
    1 1
    ```

- 类型匹配:
```py
dict1 = {'x': 1, 'y': 1.1}

match dict1:
    # 判断x是否为int, y是否为float
    case {'x': int(), 'y': float()}:
        pass
```


## 函数式编程

lambda:

```py
def mul_add(f, g):
    def h(x):
        return f(g(x, x), g(x, x))
    return h

def mul_add(f, g):
    return lambda x: f(g(x, x), g(x, x))

# test
test = mul_add(mul, add)
test(12)
```

- 字典的value放入函数.注意字典的value不能放入lambda

```py
def plus(x):
    return x + 1

func_list = {1: abs, 2: plus}

def wrapper(value):
    return func_list[value]

# test
func = wrapper(1)
func(-1)

func = wrapper(2)
func(-1)
```

### map()

- [优秀文档](https://book.pythontips.com/en/latest/map_filter.html)

- 常用写法

```py
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
```
- 使用map

```py
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```
输出
```
[1, 4, 9, 16, 25]
```

- map(函数)

```py
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)
```
输出
```
[0, 0]
[1, 2]
[4, 4]
[9, 6]
[16, 8]
```

### filter(): 过滤

- 返回生成器

- 比`for` 更快

```py
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
```
输出
```
[-5, -4, -3, -2, -1]
```

### reduce()

- 常用写法

```py
fib = 1
list1 = [1, 2, 3, 4]
for num in list1:
    fib = product + num
```

- 使用reduce

```py
from functools import reduce
fib = reduce((lambda x, y: x + y), [1, 2, 3, 4])

number_list = range(0, 11)
fib = reduce((lambda x, y: x + y), number_list)

number_max = reduce(lambda a, b:a if a > b else b, [1, 2, 3, 4])
```

- 用递归实现reduce
```py
def listsum(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        return list1[0] + listsum(list1[1:])

print(listsum([1, 3, 5, 7, 9]))
```

![image](./imgs/reduce.png)

```py
def reduce(f, list1):
    if len(list1) == 1:
        return list1[0]
    else:
        return f(reduce(f, list1[1:]), list1[0])


number_list = range(0, 11)
print(reduce(lambda x, y: x + y, number_list))
print(reduce(lambda x, y: x + y, [1, 3, 5, 7, 9]))
print(reduce(lambda a, b: a if a > b else b, [1, 2, 3, 4]))
```

### fib(斐波那契)

#### 循环 while, for

```py
def fib(n):
    x = n
    while n > 1:
        n = n - 1
        x = x + n
    return x

def fib(n):
    prev, curr = 1, 0
    for _ in range(n):
        prev, curr = curr, prev + curr
    return curr

# test
fib(10)

def fib1(f, n):
    x = n
    while n > 1:
        n = n - 1
        x = f(x, n)
        print(x)
    return x

# test
fib1(add,10)
fib1(mul,10)
```

#### 迭代

```py
def fib2(x, n):
    def iter(x, n, s):
        if n >= x:
            s = iter(x, n - 1, s + n)
        return s
    return iter(x, n - 1, n)

# test
fib2(0,10)

# 自选函数: f

def fib2(f, x, n):
    def iter(f, x, n, s):
        if n >= x:
            s = iter(f, x, n - 1, f(s, n))
        return s
    return iter(f, x, n - 1, n)


# test
fib2(add, 0, 10)
fib2(mul, 1, 5)

# 步进: y

def fib2(f, x, n, y):
    def iter(f, x, n, s):
        if n >= x:
            # 递减
            s = iter(f, x, n-y, f(s, n))
            # 递加
            # s = iter(f, x+y, n, f(s, x))
        return s
    return iter(f, x, n - y, n)

# 累加器
fib2(add, 0, 10, 2)
fib2(lambda x, y: x + y, 0, 10, 1)
fib2(mul, 10, 100, 10)
```

#### 泛函

```py
def sum(n, term, next):
    s, x = 0, 1
    while x <= n:
        s, x = s + term(x), next(x)
    return s

def fib(x):
    def fib_next(x):
        return x + 1
    def fib_term(x):
        return x
    return sum(x, fib_term, fib_next)

fib(100)
```

#### tuple(元组)

```py
def maporder(n):
    return tuple(map(lambda x: x + 10, range(0, n)))

def sumorder(n):
    return sum(map(lambda x: x + 10, range(0, n)))

def mapfib(n):
    return tuple(map(fib, range(2, n + 1)))

def mapfib(n):
    return tuple(x for x in range(1, n + 1))

def sumfib(n):
    return sum(map(fib, range(2, n + 1)))

def sumfib(n):
    return sum(fib(x) for x in range(2, n + 1))

# test
maporder(10)
sumorder(10)
mapfib(10)
sumfib(10)

# odd, even
def exfib(n, culc, f):
    return f(filter(culc, range(1, n)))

def odd(n, f):
    return exfib(n, lambda x: x % 2 != 0, f)

def even(n, f):
    return exfib(n, lambda x: x % 2 == 0, f)

odd(10, tuple)
even(10, sum)
```

### pi(圆周率)

```py
def pi(n):
    s, x = 0, 1
    while x <= n:
        s, x = s + 8 / (x * (x + 2)), x + 4
    return s

def pi(n):
    def pi_sum(s, x, n):
        if n >= x:
            s = pi_sum(s + 8 / (x * (x + 2)), x + 4, n)
        return s
    return pi_sum(0, 1, n)

# test
pi(100)
```

```py
def sum(n, term, next):
    def pi_sum(s, x, n, pi_term, pi_next):
        if n >= x:
            s = pi_sum(s + term(x), next(x), n, pi_term, pi_next)
        return s
    return pi_sum(0, 1, n, pi_term, pi_next)

# pi
def pi(x):
    def pi_next(x):
        return x + 4
    def pi_term(x):
        return 8 / (x * (x + 2))
    return sum(x, pi_term, pi_next)

# test
# 8 / (x * (x + 2))
pi(100)
```

### 黄金分割

```py
def square(x):
    return x * x

def successor(x):
    return x + 1

def near(x, f, g):
    return approx_eq(f(x), g(x))

def approx_eq(x, y, tolerance = 1e-5):
    return abs(x - y) < tolerance

def golden_update(guess):
    return 1 / guess + 1

def golden_test(guess):
    return near(guess, square, successor)

def iter_improve(update, test, guess = 1):
    while not test(guess):
        guess = update(guess)
    return guess

# test
# 1 / guess + 1
iter_improve(golden_update, golden_test)
```

### 树形递归

```py
# 指数增长

def tree(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return tree(n - 2) + tree(n - 1)

# test
tree(6)
```

### 平方根

```py
def square(x):
    return x * x

def average(x, y):
    return (x + y) / 2

def approx_eq(x, y, tolerance = 1e-5):
    return abs(x - y) < tolerance

def iter_improve(update, test, guess = 1):
    while not test(guess):
        guess = update(guess)
    return guess

def sqrt_update(guess, x):
    return average(guess, x / guess)

def square_root(x):
    def update(guess):
        return average(guess, x / guess)
    def test(guess):
        return approx_eq(square(guess), x)
    return iter_improve(update, test)

# test
# ((x / guess) + guess) / 2
square_root(256)
```

牛顿法:

```py
def square(x):
    return x * x

def successor(k):
    return k + 1

def approx_eq(x, y, tolerance = 1e-5):
    return abs(x - y) < tolerance

def approx_derivative(f, x, delta = 1e-5):
    df = f(x + delta) - f(x)
    return df / delta

def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)
    return update

def iter_improve(update, test, guess = 1):
    while not test(guess):
        guess = update(guess)
    return guess

def find_root(f, initial_guess = 10):
    def test(x):
        return approx_eq(f(x), 0)
    return iter_improve(newton_update(f), test, initial_guess)

def square_root(a):
    return find_root(lambda x: square(x) - a)

def logarithm(a, base = 2):
    return find_root(lambda x: pow(base, x) - a)


# test
square_root(16)

logarithm(32, 2)
```

### rlist(序列)

```py
def first(rlist):
    return rlist[0]

def rest(rlist):
    return rlist[1]

# insert
def insert(rlist, x):
    return (rlist,x)

def finsert(rlist, x):
    return (x,rlist)

# lengh
def lengh(rlist):
    n = 0
    while rlist != None:
        rlist, n = rest(rlist), n + 1
    return n

# test
rlist = (1, (1, (2, (2, None))))
lengh(rlist)

# get item
def get(rlist, n):
    while n > 0:
        rlist, n = rest(rlist), n - 1
    return first(rlist)

# test
get(rlist, 2)

# nonone
def nonone(rlist):
    if rest(rlist) == None:
        return first(rlist)
    return rlist

# reverse 反转
def reverse(rlist):
    x, rlist = insert(first(rlist),None), rest(rlist)
    while rlist != None:
        x, rlist = insert(first(rlist),x), rest(rlist)
    return x

# 递归
def test(rlist, x):
    if rlist != None:
       x = test(rest(rlist), (first(rlist),x))
    return x

def reverse(rlist):
    return test(rlist, None)

# test
reverse(rlist)

# insert
def ninsert(rlist, x, n):
    len, y, rerlist = lengh(rlist) - n, None, reverse(rlist)
    while rerlist != None:
        y, rerlist = insert(first(rerlist),y), rest(rerlist)
        len = len - 1
        if len == 0:
            y = insert(x, y)
    return y

# test
ninsert(rlist, 0, 2)

def einsert(rlist, x):
    return ninsert(rlist, x, lengh(rlist))

def einsert(rlist, x):
    x = insert(0, None)
    rerlist = reverse(rlist)
    link(x, rerlist)
    return x

# test
einsert(rlist, 0)
```

元组操作序列:

```py
# count 计算一个值,在序列出现的次数
def count(rlist, x):
    n = 0
    while rlist != None:
        if (x == first(rlist)):
            n = n + 1
        rlist = rest(rlist)
    return n

# bug
def count(rlist, x):
    n = 0
    for i in rlist:
        print(i)
        if i == x:
            n = n + 1
    return n

count(rlist, 1)
```
## 数据类型

- [python所有类型的时间复杂度](https://wiki.python.org/moin/TimeComplexity)

### 基本概念

- 一切皆是对象

  - 每个对象由 `id(地址)` `type(类型)` `value(值)` 组成

    `a is b` 实际上为 `id(a) == id(b)`. `is` 效率高于 `==`

  - `list` `dict` `set` 为**可变数据**,值的修改**不需要创建新对象**
     ```py
     a = [1, [2], 3]
     b = a
     # 由于b引用a, 所以a和b一样
     b[0] = 2

     import copy
     # 浅复制不会复制所有子对象
     b = copy.copy(a)
     # 父对象修改不会影响a
     b [0] = 2
     # 子对象修改会影响a
     b [1][0] = 1

     # 深复制, 两个对象完全不会影响
     b = copy.deepcopy(a)
     ```


  - `int` `str` `tuple` 为**不可变数据**,值的修改**需要创建新对象**

    - `a = 256` `b = 256` 两者 id 相同

      > python 维护一个(0, 256)的常量值, 这范围内的值的变量 id 相同

    - `a = 257` `b = 257` 两者 id 不相同

    - `a = 257` `b = a` 两者 id 相同

    - `str1 = 'string'`

    - `str1.upper()`
        > 此时返回的是一个新字符串对象

- python 访问变量, 函数, 模块时

    - 1.首先会去查locals(), 这是个本地变量字典

    - 2.如果没有就会去查globals(), 全局变量字典

- 类的特殊方法
    ```py
    a, b = 1, 2
    a + b 等同于 a.__add__(b)

    list1 = [1, 2]
    list[0] 等同于 a.__getitem__(0)
    ```

### 动态类型

- 字典的 `key`, `value` 可以是其它类型

  - 注意:

    **key** 不能为 `list`, `set`

  - 错误:

    `lv = {['hello', 'nihao']: 1}`

    `lv = {{'hello', 'nihao'}: 1}`

    ```py
    kv = {1: 'hello', 2: 'nihao'}
    kl = {1: ['hello', 'nihao']}
    kt = {1: ('hello', 'nihao')}
    ks = {1: {'hello', 'nihao'}}

    sv = {'hello': 1, 'nihao': 2}
    tv = {('hello', 'nihao'): 1}
    ```

- `list`, `tuple`, `set` 转 `dict`

  ```py
  dict([(3, 9), (4, 16), (5, 25)])
  dict(([3, 9], [4, 16], [5, 25]))
  dict(({3, 9}, {4, 16}, {5, 25}))
  ```

- `dict` 转 `list`, `tuple`, `set` 只能保留 `key`:

  ```py
  tuple({1: 'a', 2: 'b'})
  list({1: 'a', 2: 'b'})
  set({1: 'a', 2: 'b'})
  ```

- 要想同时保留 `key` `value` 可以利用 list 保存 key,再循环赋值

  ```py
  D = {'a':1, 'c':3, 'b':2}
  D1 = list(D.keys())
  D1.sort()
  s = tuple()
  for i in D1:
    s = s + (i, D[i])
  ```

- 循环赋值

  ```py
  (x for x in range(1,5))
  tuple(x * 2 for x in 'abc')
  [x for x in range(1,5) if x % 2 == 0]
  ['x' * 2 for x in 'abc']
  {x: x * x for x in range(1,5)}
  ```

### str(字符串)

- join() : `list`, `tuple`, `dict` 转 `str`

```py
tuple1 = ('hello', 'world')
' '.join(tuple1)

list1 = ['hello', 'world']
' '.join(list1)

# 只保留key
dict1 = {'hello': 1, 'world': 2}
' '.join(dict1)
```

- strip()

    - rstrip() 只去除右边

    - lstrip() 只去除左边

    ```py
    # 去除空格符号
    '   \t123\n  '.strip()

    '####123####'.strip('#')

    '####123####'.strip('#13')
    ```

- 比较运算

    ```py
    str(10) > str(9) # False
    ```

- startswith()

    > 判断字符串开头

```py
str1 = "my name is tz , age is 24"

x = str1.startswith('my')
print(x)

x = str1.startswith('name')
print(x)

# 查看name是否在第3个字符
x = str1.startswith('name', 3, 20)
print(x)
```
输出
```
True
False
True
```

- int转字符串 比较运算

```py
str(10) > str(9)
False
```

- 字符的utf-8编码

- 变长编码: 一个字符最短是8位, 最长是32位

- 竟然是变长, 那如何区分一个字符的编码长度? 通过高位代表字符的长度

    - 排除长度的位后, 剩余可用的位数为2^7 ; 2^11 ; 2^16 ; 2^21

| First code point | Last code point | Byte 1   | Byte 2   | Byte 3   | Byte 4   |
|------------------|-----------------|----------|----------|----------|----------|
| U+0000           | U+007F          | 0xxxxxxx |          |          |          |
| U+0080           | U+07FF          | 110xxxxx | 10xxxxxx |          |          |
| U+0800           | U+FFFF          | 1110xxxx | 10xxxxxx | 10xxxxxx |          |
| U+10000          | [nb 2]U+10FFFF  | 11110xxx | 10xxxxxx | 10xxxxxx | 10xxxxxx |

```py
def string_to_bytes(s):
    array = bytearray(s, "utf8")
    list1 = [bin(i) for i in array]
    print(list1)

# 中文需要3个字节
chinese = '一'
# 英文需要1个字节
english = 'a'

string_to_bytes(chinese)
string_to_bytes(english)
```
输出
```
['0b11100100', '0b10111000', '0b10000000']
['0b1100001']
```

- ord()查看字符编码

```py
ord('1')
```

#### print()

- sep: 分隔符, end: 末尾字符
```py
print(1, 2, 3, 4) # 1 2 3 4
print(1, 2, 3, 4, sep=',') # 1,2,3,4
print(1, 2, 3, 4, sep=',', end='!!') # 1,2,3,4!!
```

- end 合并为一行
```py
for i in range(3):
    print(i)

for i in range(3):
    print(i, end='')
```
输出
```
0
1
2

012
```

- 类型转换. 使用 `*` 代替join()
```py
list1 = [1, 2, 3, 4]

# join写法
print(','.join(str(i) for i in list1)) # 1,2,3,4

# *写法
print(*list1, sep=',') # 1,2,3,4
```

#### format()

- [格式化输出](https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p03_format_numbers_for_output.html)

- 插入变量
    ```py
    s = 'name: {name} age: {age}'
    s.format(name='tz', age=24)  # name: tz age: 24
    ```
    - vars()
    ```py
    name = 'tz'
    age = 24
    s.format_map(vars())  # name: tz age: 24
    ```

    - format_map() 将变量插入class

    ```py
    class people:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    p = people('tz', 24)
    s.format_map(vars(p))   # name: tz age: 24
    ```

#### 4种字符串格式化方法

```py
name = 'tz'
age = '24'

str1 = 'name %s age %s' % (name, age)
str1 = 'name ' + name + ' ' + 'age ' + age
str1 = f'name {name} age {age}'
str1 = f'name {0} age {1}'.format(name, age)
```

- `format()`

    ```py
    # 对象
    "my name is {a.name} , age is {a.age}".format(a=people())

    # 小数保留
    "{:.2f}".format(3.1415926)
    ```

- 使用`f'{v=}'` 取代 `f"v = {v}"`

    ```py
    pi = 3.14
    print(f'{pi=}')

    pi=3.14
    ```

- [timeit性能对比: 4种字符串格式化方法](./python-debug.md#str)
    - `{}` >  `+` > `%` > `format`

#### string模块

- `Template()` 模板

```py
from string import Template
str1 = Template("name $name age $age")
print(str1.substitute(name = 'tz', age = '24'))
```

#### io模块的StringIO, BytesIO

- 使用操作文件方式, 来操作文本, 二进制字符串

    - StringIO 和 BytesIO 并没有文件描述符
    - 可以用于单元测试

- io.StringIO(): 文本字符串

```py
import io

s = io.StringIO()

# 写入
s.write('Hello World')
# print写入
print('Hello World', file=s)

# 读取
s.getvalue()

# 读取前4个字符
s.read(4)
```

- io.BytesIO(): 文本字符串

    - 不能使用print()写入

```py
import io

s = io.BytesIO()

# 写入
s.write(b'Hello World')
# print写入

# 读取
s.getvalue()
# 读取前4个字符
s.read(4)
```

### list(列表)

- list.append(): 包含类型

- append自身(递归)

```py
# [1, 2, 3, 4, 5]
list1 = list('12345')
list1.append(list1)
```

- 输出:

```py
list1 == list1[5]
['1', '2', '3', '4', '5', [...]]
```

- list.extend() 合并list

```py
# [1, 2, 3, 4, 5]
list1 = list('12345')
# 添加自身
list1.extend(list1)
```

- 输出:

```py
list1
['1', '2', '3', '4', '5', '1', '2', '3', '4', '5']
```

- 语法糖

```py
# [1, 2, 3, 4, 5]
list1 = list('12345')

# 间隔为2
list1[::2]
[1, 3, 5]

# 反向
list1[-2::]
[4, 5]
```

- 切割
    ```py
    a1, a2, a3 = [1, 2, 3]
    a1, a2, a3 = "123"
    ```

- 切割头, 中间, 尾
    ```py
    a1, *a2, a3 = "123456789"
    ```

    - 输出
    ```
    a1
    '1'

    a2
    ['2', '3', '4', '5', '6', '7', '8']

    a3
    '9'
    ```

- 切割头, 尾
    ```py
    list1 = [['name', 'tz', 'zt'], ['age', 24]]
    k, *v = list1

    # 生成字典
    {k:v for k, *v in list1}
    ```
    - 输出
    ```
    k
    ['name', 'tz', 'zt']

    v
    [['age', 24]]

    {k:v for k, *v in list1}
    {'name': ['tz', 'zt'], 'age': [24]}
    ```

- 取出列表内的值
    ```py
    list1 = [1, 2, [3, 4], 5]
    [a, b, [c, d], e] = list1

    # *_表示省略后面
    [a, b, [c, *_], *_] = list1
    ```
    - 输出
    ```
    a
    1

    b
    2

    c
    3
    ```

- 去重, 并保持原有列表顺序

    - 直接set(), 并不能保持原有列表顺序
        ```py
        list1 = [1, 2, 2, 8, 1, 5, 3, 5]

        # set()会自动排序
        set1=set(list1) # {1, 2, 3, 5, 8}
        ```

    - 使用set() 作过滤
    ```py
        def dedupe(data):
            set1 = set()
            for i in data:
                if i not in set1:
                    yield i
                    set1.add(i)


        list1 = [1, 2, 2, 8, 1, 5, 3, 5]
        list(dedupe(list1)) # [1, 2, 8, 5, 3]
        ```

- 挑选列表内的int值

    - compress() 返回生成器: 挑选列表内True的值
    ```py
    from itertools import compress

    list1 = [2, '8', 1, '9', '+', 3]

    # 输出生成器: [True, False, True, False, False, True]
    list2 = [isinstance(i, int) for i in list1]

    # 输出生成器: [2, 1, 3]
    list(compress(list1, list2))
    ```

- 挑选列表内的int值, 字符串内是int的值
    ```py
    def is_int(i):
        try:
            tmp = int(i)
            return True
        except ValueError:
            return False


    list1 = [2, '8', '-', 1, '9', '+', 3]

    # 输出生成器: [2, '8', 1, '9', 3]
    list(filter(is_int, list1))
    ```

#### Queue(队列)

- list实现
```py
class Queue(object):
    def __init__(self, maxsize=0):
        self.list = []
        self.maxsize = maxsize
        self.size = 0

    def put(self, data):
        if self.maxsize <= 0 or self.size < self.maxsize:
            self.size += 1
            self.list.append(data)
        else:
            raise ValueError("size is max")

    def get(self):
        self.size -= 1
        return self.list.pop(0)

    def isempty(self):
        return len(self.list) == 0


q = Queue(maxsize=0)
q.put(1)
q.put(2)
print(q.get())
print(q.get())
print(q.isempty())

q = queue(maxsize=1)
q.put(1)
try:
    q.put(2)
except ValueError:
    print('error')
```

- Queue: FIFO
```py
from queue import Queue

# maxsize 队列限制, 小于或等于0, 表示无限制
s = Queue(maxsize=0)
s.put("1")
s.put("2")
s.put("3")

# 队列长度
s.qsize()

s.get()
s.get()
s.get()

# 队列是否为空
s.empty()
# 队列是否满
s.full()
```

- LifoQueue: LIFO等同于stack
```py
from queue import LifoQueue

s = LifoQueue()
s.put("1")
s.put("2")
s.put("3")

s.get()
s.get()
s.get()
```

- 括号匹配
```py
from queue import LifoQueue

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

def parChecker(str1):
    stack1 = LifoQueue()

    for i in range(len(str1)):
        symbol = str1[i]
        # 如果是左括号
        if symbol in "([{":
            stack1.put(symbol)
        # 如果是右括号
        elif symbol in ")]}":
            top = stack1.get()
            if not matches(top, symbol):
                return False

    if stack1.empty():
        return True
    else:
        return False


print(parChecker("{{([][])}()}"))
print(parChecker("[{()]"))
```

#### CircularQueue(环形队列)
```py
class CircularQueue():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = [None] * maxsize
        # -1表示队列为空
        self.head = self.tail = -1

    def enqueue(self, data):
        if (self.tail + 1) % self.maxsize == self.head:
            print("The circular queue is full\n")

        # 第一次添加元素
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.maxsize
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            print("The circular queue is empty\n")

        # 当队列只剩一个元素时
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.maxsize
            return temp

    def print(self):
        if self.head == -1:
            print("No element in the circular queue")
        else:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


q = CircularQueue(5)

# 加入队列
for i in range(5):
    q.enqueue(i)
q.print()

# 出队列
q.dequeue()
q.print()
```

#### Deque(双向链表)

- Deque 支持FIFO, LIFO

- 两边的元素append()和pop()的时间复杂度是: O(1)

    - 但随机访问的中间元素是: O(n)

- list实现
```py
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def appendright(self, item):
        self.items.append(item)

    def appendleft(self, item):
        self.items.insert(0, item)

    def popleft(self):
        return self.items.pop(0)

    def pop(self):
        return self.items.pop()


d = Deque()
d.appendright(8)
d.appendright(5)
d.appendleft(7)
d.appendleft(10)
print(d.items)

d.popright()
d.popleft()
print(d.items)
```

- deque()

```py
from collections import deque

de = deque([1, 2, 3])

de.append(4)
print(de)

# 左边添加
de.appendleft(0)
print(de)

de.pop()
# 左边移除

de.popleft()
print(de)
```
输出
```
deque([1, 2, 3, 4])
deque([0, 1, 2, 3, 4])
deque([1, 2, 3])
```
- maxlen: 维护一个固定长度, 新的元素会挤掉旧的
```py
de = deque(maxlen=3)
de.append(1)
de.append(2)
de.append(3)

print(de)
de.append(4)
print(de)
```
输出
```
deque([1, 2, 3], maxlen=3)
deque([2, 3, 4], maxlen=3)
```

- 判断一个字符串是否是回文字符串
```py
from collections import deque

def palchecker(str1):
    deque1 = deque()

    for i in str1:
        deque1.appendleft(i)

    while len(deque1) > 1:
        if deque1.pop() != deque1.popleft():
            return False

    return True

print(palchecker("toot"))
print(palchecker("toat"))
```

- [timeit性能对比: list vs deque](./python-debug.md#deque)

    - 但timeit的测试结果是list比deque快1.68倍

#### array 模块

- 连续内存
```py
from array import array

# i 表示int类型
array1 = array('i', range(3))
# d 表示float类型
array1 = array('d', [1.1, 2.2, 3.3])
```

#### bisect(二分排序列表)

- 通过插入并排序的时间复杂度O(n log n), 来维持查找的时间复杂度O(log(n))

```py
import bisect

list1 = [1, 3, 4, 4, 4, 6, 7]

# 查找元素, 返回最右. 时间复杂度O(log(n))
print(bisect.bisect(list1, 4))

# 返回最左
print(bisect.bisect_left(list1, 4))

# 返回最右
print(bisect.bisect_right(list1, 4))

# 插入元素并排序. 时间复杂度O(n log n)
bisect.insort(list1, 5)
print(list1)

# 在从0开始, 在第4个元素插入元素5
bisect.insort_right(list1, 5, 0, 4)
print(list1)
```

#### headp: 堆

- append()和pop()的时间复杂度是: O(log n)

```py
import heapq

q = []
heapq.heappush(q, (1, "a"))
heapq.heappush(q, (3, "b"))
heapq.heappush(q, (2, "c"))

while q:
    print(heapq.heappop(q))
```

- heapify()找到列表里最小的值. 时间复杂度是: O(log n)
```py
list1 = [4, 2, 1, 6, 4, 7, 5]
heapq.heapify(list1)
print(list1)
print(list1[0])
print(heapq.heappop(list1))
```
输出
```
[1, 2, 4, 6, 4, 7, 5]
1
1
```

##### 优先级队列
```py
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self._index = 0

    def push(self, data, priority):
        # 最小的数会先pop, 因此要加负数priority
        heapq.heappush(self.queue, (-priority, self._index, data))
        self._index += 1

    def pop(self):
        # 返回(-3, 1, 'b'), 所以要加[-1]
        return heapq.heappop(self.queue)[-1]


q = PriorityQueue()
q.push('a', 1)
q.push('b', 3)
q.push('c', 2)
q.push('d', 3)

while q.queue:
    print(q.pop())
```

### tuple(元组)

```py
word = "hello Worrld ! in Python"

# 字符串传元组
tuple(word.split())
tuple(w[0] for w in word.split())
tuple(w[0] for w in word.split() if w[0].isupper())
tuple(w[0] for w in word.split() if w[0].islower())

def first(list):
    return list[0]

def iscap(word):
    return word[0].isupper()

def acronym(word, f):
    return tuple(map(f, filter(iscap, word.split())))

def acronym1(word, f):
    return tuple(f(w) for w in word.split() if iscap(w))

# 提取首字母为大写的单词
acronym(word, lambda x: x)

# 提取首字母为大写的字母
acronym(word, lambda x: x[0])

# 转换为小写
acronym(word, lambda x: x[0].lower())
```

```py
def insert(s, x):
    s = s + x
    s = s + ' '
    return s

# insert
def ninsert(n, y, x):
    l, s = 0, ''
    for i in n:
        s = insert(s, i)
        l = l + 1
        if l == y:
            s = insert(s, x)
    return tuple(s.split())

n = ('hello', 'Worrld', '!', 'in', 'Python')
ninsert(n, 3, 'test')
```

- 第一个元素可以比较大小. 列表也一样可以
```py
a = (1, 'a')
b = (2, 'b')
print(a < b)
print(a > b)
```

#### namedtuple

- 可以代替字典, 有着比字典更小的空间

```py
from collections import namedtuple

people = namedtuple('people', ('name', 'age'))

a = people('tz', 24)
print(a.name, a.age)
print(a[0], a[1])

# 字典输出
print(a._asdict())
```
输出
```
tz 24
tz 24
{'name': 'tz', 'age': 24}
```
- 列表输入
```py
from collections import namedtuple

people = namedtuple('people', ('name', 'age'))

# 列表输入
list1 = ['tz', 24]
people._make(list1)
print(list1)
```
输出
```
['tz', 24]
```

- `_replace()` 修改value.  会创建一个新的实例

```py
# 报错: AttributeError: can't set attribute
a.age = 20
```

```py
# 会创建一个新的实例
a = a._replace(age=20)
```

- 定义函数, 输入字典, 将nametuple的实例, 修改字典值
```py
from collections import namedtuple


def replace(dict1):
    return a._replace(**dict1)


people = namedtuple('people', ('name', 'age'))
a = people('tz', 24)

dict1 = {'name': 'tz', 'age': 21}

# 输出: people(name='tz', age=21)
a = replace(dict1)
```


### Dictionaries(字典)

> key不能重复

- `v | b` instead of `{**v, **v1}` instead of  `v.update(b)`

```py
{**a, **b}

# or
a | b
```

- `|=` instead `dict.update()`

```py
a = {**a, **b}

# or
a.update(b)

# or
a |= b
```
- 去重key值. 通过set()作过滤器

    ```py
    def dedupe(data, key=None):
        set1 = set()
        for i in data:
            val = i if key is None else key(i)
            if val not in set1:
                yield i
                set1.add(val)

    dict1 = [{'x': 1, 'y': 2},  {'x': 3, 'y': 4}, {'x': 1, 'y': 2}, {'x': 1, 'y': 3}]

    # 去重key. 提取key值后保存进set
    list(dedupe(dict1, key=lambda d: d['x']))

    # 去重key, value. 转换成tuple后保存进set
    list(dedupe(dict1, key=lambda d: (d['x'], d['y'])))
    ```
    输出
    ```
    [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]
    [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 1, 'y': 3}]
    ```

- 去重文件重复行
    ```py
    with open('/tmp/test', 'r') as file:
        for line in dedupe(file):
            print(line.strip('\n'))
    ```

- 通过转换kv, 去除重复value

```py
test_dict = {'a': 10, 'b': 15, 'c': 20, 'd': 10, 'e': 20}
temp = {val: key for key, val in test_dict.items()}
res = {val: key for key, val in temp.items()}
print(res)
```
输出
```
{'d': 10, 'b': 15, 'e': 20}
```

- zip(): 迭代多个对象

    - 对value进行排序
        ```py
        dict1 = {
                'o': 3,
                'y': 2,
                'x': 1,
                'z': 3
                }

        dict1_zip = zip(dict1.values(), dict1.keys())
        print(sorted(dict1_zip))
        ```
        输出
        ```
        [(1, 'x'), (2, 'y'), (3, 'o'), (3, 'z')]
        ```

    - 两个数组转换为字典
    ```py
    k = ['k1', 'k2']
    v = ['v1', 'v2']
    kv = dict(zip(k,v))

    # 通过切片交换数组, 形成字典
    old_kv = ['k1', 'v1', 'k2', 'v2']
    old_kv1 = ['k10', 'v10', 'k20', 'v20']
    new_kv = dict(zip(old_kv[0::2], old_kv1[0::2]))
    ```
    - 输出
    ```
    kv
    {'k1': 'v1', 'k2': 'v2'}

    new_kv
    {'k1': 'k10', 'k2': 'k20'}
    ```
- 取出字典内的kv
    ```py
    dict1 = {'k1': 'v1', 'k2': 'v2'}
    (k1, v1), (k2, v2) = dict1.items()
    (i1, i2)  = dict1.items()

    # *_表示省略后面
    (k1, v1), *_  = dict1.items()

    # _表示省略
    (i1, _)  = dict1.items()
    ```
    - 输出
    ```
    k1
    'k1'

    v1
    'v1'

    i1
    ('k1', 'v1')

    i2
    ('k2', 'v2')
    ```

- 一个key保存多个value:

    - 字典包字典
        ```py
        dict1 = {
                'a': {'1', '2', '3'},
                'b': {'2', '3', '4'}
                }
        dict1['a']
        ```

    - setdefault():
        ```py
        dict1 = {}
        dict1.setdefault('a', []).append(1)
        dict1.setdefault('a', []).append(2)
        ```

    - defaultdict()
        ```py
        from collections import defaultdict

        d = defaultdict(list)
        d['a'].append(1)
        d['a'].append(2)
        ```

- 集合运算. keys支持集合运算, values不支持, items带keys所以支持
    ```py
    dict1 = {
            'x': 1,
            'y': 2,
            'z': 3
            }

    dict2 = {
            'x': 1,
            'y': 20,
            'o': 3
            }

    # & 交集
    dict1.keys() & dict2.keys()   # {'x', 'y'}
    dict1.items() & dict2.items() # {('x', 1)}

    # - 差集
    dict1.keys() - dict2.keys() # {'z'}
    ```

#### collections模块

- [geeksforgeeks文档](https://www.geeksforgeeks.org/python-collections-module/)

- Counter()

    ```py
    from collections import Counter

    print(Counter(['B','B','A','B','C','A','B',
                   'B','A','C']))
    ```
    输出
    ```
    Counter({'B': 5, 'A': 3, 'C': 2})
    ```

    - 统计命令的次数

        ```py
        from collections import Counter

        cmd = []

        # 将所有命令加入list
        with open('/home/tz/.bash_history', 'r') as f:
            for line in f:
                l = line.split()
                if len(l) > 1:
                    cmd.append(l[0])

        # Counter用dict统计list重复的值, 并按顺序排序
        print(Counter(cmd))
        ```

- defaultdict

    - append()

        ```py
        from collections import defaultdict

        # 定义value为list
        d = defaultdict(list)

        for i in range(5):
            d[i].append(i)

        print(d)
        ```
        输出
        ```
        defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})
        ```

    - 统计

        ```py
        from collections import defaultdict

        # 定义int
        d = defaultdict(int)

        list1 = [1, 2, 3, 4, 2, 4, 1, 2]

        for i in list1:
            d[i] += 1

        print(d)
        ```
        输出
        ```
        defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})
        ```

    - 统计命令的次数

        ```py
        from collections import defaultdict
        cmd = []

        d = defaultdict(str)
        # 将所有命令加入list
        with open('/home/tz/.bash_history', 'r') as f:
            for line in f:
                l = line.split()
                if len(l) > 1:
                    cmd.append(l[0])

        # 定义int
        d = defaultdict(int)

        for i in cmd:
            d[i] += 1

        # 不会按顺序排序
        print(d)
        ```

    - OrderedDict: 双向链表, 新元素会加入末尾, 内存比普通字典大2倍多
        ```py
        from collections import OrderedDict

        d = OrderedDict()
        d['a'] = 1
        d['b'] = 2
        d['c'] = 3

        for key in d:
            print(key, d[key])
        ```
- ChainMap():

```py
from collections import ChainMap

dict1 = {'x': 0, 'y': 1}
dict2 = {'x': 2, 'z': 3}

c = ChainMap(dict1, dict2)

# 只会输出第一个key的值
# 输出: 0
c['x']

# 输出: ['x', 'z', 'y']
list(c.keys())

# 输出: [0, 3, 1]
list(c.values())
```

- new_child() 手动创建
```
c = ChainMap()
c['x'] = 0
c['y'] = 1
c = c.new_child()
c['x'] = 2
c['z'] = 3

# 输出: ChainMap({'x': 2, 'z': 3}, {'x': 0, 'y': 1})
print(c)
```

### set(集合)

- 比list使用更多的内存, 但查询速度更快

- 匹配元素重复2次以上

    ```py
    list1 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    set1 = set([x for x in list1 if list1.count(x) > 1])
    print(set1)
    ```
    输出
    ```
    {'n', 'b'}
    ```

- `intersection()`: 交集

    ```py
    list1 = range(5)
    set1 = set([1, 6])
    print(set1.intersection(list1))
    ```
    输出
    ```
    {1}
    ```

- `intersection()`: 差值

    ```py
    list1 = range(5)
    set1 = set([1, 6])
    print(set1.difference(list1))
    ```
    输出
    ```
    {6}
    ```

### 图

![image](./imgs/dawg.png)
- 减少内存

- DAWG(有向无环图)

    - 共享前缀, 后缀

    - 不能修改

    ```py
    import dawg

    str1 = 'hello world'

    dawg1 = dawg.DAWG('str1')
    ```

- trie只共享前缀

    - `marisa_trie`

        - 不能修改

    ```py
    import marisa_trie
    trie = marisa_trie.Trie('str1')
    ```

    - `datrie`

        - 可以修改

    ```py
    import datrie
    set1 = set('str1')
    datrie1 = datrie.BaseTrie(set1)
    ```

### 静态类型(static type)

#### [静态类型检查工具:mypy](https://github.com/python/mypy)

- 将代码保存文件后, 使用`mypy` 进行静态类型检查
    ```sh
    mypy ./test.py
    # python2
    mypy --py2 ./test.py
    ```

- 以下代码的**报错**是指静态类型检查阶段

```py
def add(x: int, y: int):
    return x + y

# 报错 不是int
add('1', '2')
```

```py
def test(n: int) -> int:
    return n

test(1)

# 报错 输入值不是int
test(1.1)

def test1(n: int) -> int:
    # 报错 返回值不是int
    n = 1.1
    return n

test1(1)
```

```py
from typing import List

def test(names: List[str]) -> None:
    print(names)

names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

test(names)

# 报错 输入值不是list
test('123')
```

#### [静态类型检查工具:pytype](https://github.com/google/pytype)

- 自动生成`pyi`文件

    - 相当于解耦

    - 1.源码:

        ```py
        class o:
            def __init__(self, x):
                self.x = []
        ```


    - 2.生成`pyi`文件. 文件保存在`.pytype/pyi/`下

        ```sh
        pytype test.py
        ```

    - 3.`pyi`文件:

        ```py
        from typing import List

        class o:
            x: List[nothing]
            def __init__(self, x) -> None: ...
        ```

#### 基本使用

- [视频: 丁来强-Python强类型编程最佳实践](https://www.bilibili.com/video/BV185411H7Bc?spm_id_from=333.999.0.0)

- [dropbox 检查400万行代码的过程](https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python)

- 什么时候需要静态类型检查:
    - 1.sdk, 库, 接口给别人的时候
    - 2.大代码量
    - 3.单元测试

- PEP484: 分两个阶段

    - 1.静态检查阶段

    - 2.运行时阶段

- `TYPE_CHECKING` 只在静态检查阶段导入库
    ```py
    from typing import TYPE_CHECKING

    # 静态检查阶段
    if TYPE_CHECKING:
        import requests
    ```

- `[]` 定义类型:
    ```py
    # 定义元组内的类型, 第一个必须是int, 第二个必须是str
    n = tuple[int, str]

    def f() -> n:
        return (1, '1')

    # 报错 第二个元素不是str类型
    def f() -> n:
        return (1, 1)

    # 报错 多出一个元素
    def f() -> n:
        return (1, '1', 1)
    ```

    - `Literal` 定义一组值
    ```py
    from typing import Literal

    # 定义r, w
    mode = Literal['r', 'w']
    def myopen(path: str, m: mode) ->None:
        pass

    # 不报错
    myopen('/tmp/test', 'r')
    # 报错 rb不在mode列表内
    myopen('/tmp/test', 'rb')
    ```

    - `Union` 定义一组类型, 类型可以不同
    ```py
    from typing import Union

    n = Union[int, str]

    # 不会报错
    def f() -> n:
        return 1

    # 不会报错
    def f() -> n:
        return '1'
    ```

    - `TypeVar` 定义一组类型(泛型), 类型必须相同
    ```
    from typing import TypeVar

    n = TypeVar('n', int, str)

    def f(x: n, y: n):
        pass

    # 没有报错
    f(1, 1)

    # 没有报错
    f('1', '1')

    # 报错 两个参数的类型必须相同
    f('1', 1)
    ```
    - `Iterable` 定义迭代器
    ```py
    from typing import TypeVar, Iterable

    n = TypeVar('n', int, float)
    # 定义迭代器
    n1 = Iterable[tuple[n, n]]

    def f(v: n1[n]):
        pass


    # 不会报错
    f(
      ((1, 1), (2, 2))
            )

    # 不会报错
    f(
      ((1, 1.1), (2.1, 2))
            )

    # 报错
    f(
      (1, 1.1)
            )
    ```

    - 类继承`Generic` , 使类下的方法与`TypeVar`相同
    ```py
    from typing import TypeVar, Generic

    # 初始化泛型
    n = TypeVar('n')

    # 继承泛型
    class o(Generic[n]):
        def f(self, x: n):
            pass

    # 定义泛型为int
    a: o[int] = o()

    # 不会报错
    a.f(1)

    # 报错 参数只能是泛型n, 也就是int类型
    a.f('1')
    ```

- `@no_type_check` 关闭静态类型检查:
    ```py
    from typing import no_type_check

    # 不会报错
    @no_type_check
    def f(x: int) -> int:
        return x + 1

    f(1.1)
    ```

- `Final`变量不能修改
    ```py
    from typing import Final

    x: Final = 1

    # 报错, 变量不能修改
    x += 1
    ```

- `@final` 类, 方法不能继承和重写

    - 类
    ```py
    from typing import final

    @final
    class o: pass

    # 报错, 不能继承
    class o1(o): pass

    # 报错, 不能重写
    class o: pass
    ```

    - 方法:
    ```py
    class o:
        @final
        def f(self): pass

        # 报错, 不能重写
        def f(self): pass
    ```

- `@dataclass` 将类变为数据结构
    ```py
    from dataclasses import dataclass

    @dataclass
    class o:
        x: int
        y: int

    a = o(1, 2)
    ```

    ```py
    from dataclasses import dataclass
    from typing import List

    @dataclass
    class o:
        x: int
        y: int

    @dataclass
    class o1:
        mylist: List[o]

    b = o1([o(1, 2), o(3, 4)])
    print(b.mylist)
    # 获取列表中, 第一个o对象中的, 第一个元素
    print(b.mylist[0].x)
    ```

- `Protocol`实现 duck typing(任何class). 不检查类型, 而是检查方法, 属性是否存在
```py
from typing import Protocol, Iterable

class iresource(Protocol):
    def close(self) -> None:
        pass

# 并不需要继承iresource
class resource():
    def close(self) -> None:
        pass

# close所有列表对象
def close_all(r: Iterable[iresource]):
    for i in r:
        i.close()

f = open('/tmp/test')
r = resource()

# 不管是什么class, 都可以close()
close_all([f, r])
```

## sorted

- 找出列表内元素组合的最大值. 通过字符串的比较, 使其变成一个排序问题

    - 普通方法
        ```py
        list1 = [10, 9, 33, 62, 31]
        list2 = [str(i) for i in list1]
        print(''.join(sorted(list2, reverse=True))) # 962333110
        ```
    - 通过cmp_to_key(), 让sorted的key参数(指定排序规则)接受2个值
        ```py
        from functools import cmp_to_key

        # 只能是int(y+x)-int(x+y), 而不能是 int(x+y)-int(x+y)
        list2 = sorted(list2, key=cmp_to_key(lambda x, y:int(y+x)-int(x+y)))
        print(''.join(list2))
        ```

- dict内的value排序

    - lambda方法
        ```py
        users = [
                {'name': 'user0', 'age': 24, 'uid': 1000},
                {'name': 'user1', 'age': 22, 'uid': 1002},
                {'name': 'user2', 'age': 22, 'uid': 1001},
                {'name': 'user3', 'age': 21, 'uid': 1003}
                ]

        # 排序age
        print(sorted(users, key=lambda x: x['age']))
        # 先排序age, 再排序uid
        print(sorted(users, key=lambda x: (x['age'], x['uid'])))
        ```
    - itemgetter()
        ```py
        from operator import itemgetter

        print(sorted(users, key=itemgetter('age')))
        print(sorted(users, key=itemgetter('age', 'uid')))
        ```

- 对dict的val进行分组

    - groupy()
        ```py
        users = [
        {'name': 'user0', 'age': 24, 'scores': 60},
        {'name': 'user1', 'age': 22, 'scores': 100},
        {'name': 'user2', 'age': 22, 'scores': 50},
        {'name': 'user3', 'age': 21, 'scores': 60}
        ]

        from itertools import groupby
        from operator import itemgetter

        # 排序
        users.sort(key=itemgetter('scores'))

        for k, items in groupby(users, key=itemgetter('scores')):
            print(k)
            for i in items:
                print(i)
        ```
        输出
        ```
        50
        {'name': 'user2', 'age': 22, 'scores': 50}
        60
        {'name': 'user0', 'age': 24, 'scores': 60}
        {'name': 'user3', 'age': 21, 'scores': 60}
        100
        {'name': 'user1', 'age': 22, 'scores': 100}
        ```
    - defaultdict()
        ```py
        from collections import defaultdict

        dict1 = defaultdict(list)
        for i in users:
            dict1[i['scores']].append(i)

        for i in dict1[60]:
            print(i)
        ```
        输出
        ```
        {'name': 'user0', 'age': 24, 'scores': 60}
        {'name': 'user3', 'age': 21, 'scores': 60}
        ```

- class内属性排序

    - lambda方法
        ```py
        class User:
        def __init__(self, id):
            self.uid = id

        def __repr__(self):
            return f'{self.uid}'

        users = [User(3), User(2), User(1)]
        sorted(users, key=lambda u: u.uid) # [1 2 3]
        ```
    - itemgetter()
        ```py
        from operator import attrgetter

        sorted(users, key=attrgetter('uid')) # [1 2 3]
        ```

## def(函数)

- 返回多个值

```py
def f():
    return 1, 2, 3

tuple1 = f()
a, b, c = f()
```

- lambda: 匿名函数

```py
# x是自由变量, 运行时绑定, 而不是定义时绑定
x = 10
f = lambda y: x + y

# 30
f(20)
```
- 推导式的自由变量
```py
# 错误, n没有绑定, 在这里会一直等于4
funcs = [lambda x: x+n for n in range(5)]

# 绑定n
funcs = [lambda x, n=n: x+n for n in range(5)]

for f in funcs:
    print(f(0))
```

- [回调函数](https://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p10_carry_extra_state_with_callback_functions.html)
    - 函数, 类, 协程. 三个例子

### 闭包(closure)函数

```py
def closure():
    n = 0

    # 闭包函数
    def func():
        print('n=', n)

    # nonlocal可以修改函数内部变量
    def set_n(value):
        nonlocal n
        n = value

    func.set_n = set_n
    return func


# f = func()
f = closure()
f() # 0

f.set_n(1)
f() # 1
```

### 参数`*argv`, `**kwargs`

- `*argv`: 表示剩下的元组元素

```py
def myFun(arg1, arg2, *argv):
    print ("First argument :", arg1)
    print ("Second argument :", arg2)
    for arg in argv:
        print("Next argument through *argv :", arg)

myFun('Hello', 'Welcome', 'to', 'python')

# 或者
tuple1 = ('Hello', 'Welcome', 'to', 'python')
myFun(*tuple1)
```

- `**kwargs`: 表示剩下的字典kv

```py
def myFun(arg1, arg2, **kwargs):
    print ("First argument :", arg1)
    print ("Second argument :", arg2)
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

myFun('hello', 'tz', name = 'tz', age = '24')

# 或者
dict1 = {'name' : 'tz', 'age' : '24'}
myFun('hello', 'tz', **dict1)
```

### 内置函数,属性

```py
# 普通函数和匿名函数
def a (x, y):
    """This is the module docstring."""
    c = {'a': 1, 'b': 2}
    return x + y

b = lambda x, y: x + y

# dir查看方法
dir(a)
dir(b)

# __doc__返回 """This is the module docstring."""
a.__doc__

# 调用是使用内置的方法__call__()
a.__call__(1, 2)
b.__call__(1, 2)
a(1, 2)
b(1, 2)

# __dict__查看内部使用字典保存a.name, a.age属性变量
def test():
    test.a = 1

# 一开始函数没有运行,此时还没有赋值,结果为空
test.__dict__

# 函数运行后可查看
test()
test.__dict__
```

- inspect.signature(): 获取形式参数
```py
from inspect import signature

def f(x, y, z=1):
    pass

args = signature(f)
print(args) # (x, y, z=1)
print(args.parameters) # OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">), ('z', <Parameter "z=1">)])
print(args.parameters['z'].default) # 1
```

### 装饰器(decorator)

> 输入输出函数

```py
def wrapper(func):
    def newfunc(*args, **kw):
        print("我真的是一个装饰器")
        return func
    return newfunc

@wrapper
def func():
    print("我是原函数")

# @的表达式.个人理解为面向对象遇上函数的表达方法.等同于以下
func = wrapper(func)

# test
# 这里执行的是newfunc
func()
# 执行newfunc后会返回func函数,第二个()就是执行func
func()()

# 再包一层
def wrapper1(func):
    def newfunc(*args, **kw):
        print("我真的是第二个装饰器")
        return func
    return newfunc

def wrapper(func):
    def newfunc(*args, **kw):
        print("我真的是一个装饰器")
        return func
    return newfunc

@wrapper1
@wrapper
def func():
    print("我是原函数")

# 以上等同于
func = wrapper1(wrapper(func))

# test
func()()()
```

- functools.wraps(): 传递参数, 复制元信息(__name__, __doc__)
```py
import time

from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(100000)

# __wrapped__获取原来的函数
origin_func = countdown.__wrapped__
origin_func(10)
```

- 装饰类
```py
def wrapper(cls):
    class newcls:
        def __init__(self):
            self.name = "我真的是一个装饰器"
            self.cls = cls
    return newcls

@wrapper
class cls:
    def __init__(self):
        self.name = "我是原函数"

# test
a = cls()
a.name

b = a.cls()
b.name
```

- 装饰类的方法
```py
from functools import wraps

def wrapper(func):
    @wraps(func)
    def f(*args, **kwargs):
        print('我是装饰器')
        return
    return f


class O:
    @classmethod
    @wrapper
    def f(cls):
        print('in classmethod')

    @staticmethod
    @wrapper
    def f1():
        print('in staticmethod')


# test classmethod
O.f() # 我是装饰器

s = O()

# test staticmethod
s.f1() # 我是装饰器
```

- 根据函数是否存在某参数, 从而执行相应的操作
```py
from functools import wraps
import inspect

def optional_add(func):
    # 查看函数是否存在arg_, 就输出y参数
    if 'arg_y' in inspect.getfullargspec(func).args:
        print('not arg_y')

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@optional_add
def f(x):
    pass

@optional_add
def f1(x, arg_y):
    pass

f1(1, 2)
f(1) # not arg_y
```

#### 类装饰器

- 手动实例化
```py
from functools import wraps

class O:
    # Decorator as an instance method
    def wrapper(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('我是装饰器')
            return func(*args, **kwargs)
        return wrapper

# 实例化
o = O()

@o.wrapper
def f():
    pass

f() # 我是装饰器
```

- 不需要手动实例化
```py
import types
from functools import wraps

class Wrapper:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        print('我是装饰器', self.ncalls)
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

    def f1(self):
        print('我是f1函数')


@Wrapper
def f():
    pass

f()    # 我是装饰器 1
f()    # 我是装饰器 2
f.f1() # 我是f1函数
```

### functools模块

- partial() 封装一个参数

```py
from functools import partial

def p(a, b):
    print(a, b)

p1 = partial(p, b = 3)
p1(2) # 2 3
```

- cmp_to_key()

```py
# 函数转为key,然后进行排序:
from functools import cmp_to_key

def cmp_fun(a, b):
    if a[-1] > b[-1]:
        return 1
    elif a[-1] < b[-1]:
        return -1
    else:
        return 0

list1 = ['9', '2', '7']
l = sorted(list1, key = cmp_to_key(cmp_fun))
print('sorted list :', l)
```

- lru_cache(): 保存最新的调用, 减少内存

```py
from functools import lru_cache

@lru_cache(maxsize = None)
def fib(n):
    if n == 0:
        return n
    return n + fib(n-1)

print([fib(n) for n in range(7)])
print(fib.cache_info())
```
输出
```
[0, 1, 3, 6, 10, 15, 21]
CacheInfo(hits=6, misses=7, maxsize=None, currsize=7)
```

- singledispatch(): 根据输入参数的类型, 使用不同的函数

```py
from functools import singledispatch

@singledispatch
def fun(s):
    print(s)
@fun.register(int)
def _(s):
    print(s * 2)
@fun.register(float)
def _(s):
    print(s - 1)

fun('GeeksforGeeks')
fun(10)
fun(10.0)
```
输出
```
test
20
9.0
```

## class(类)

### 继承

- `__` 私有不能被继承; `_` 可以被继承
```py
class A():
    def __f(self):
        print('in A')


class B(A):
    def __init__(self):
        super().__f()

# 报错
B()
```

- super(): 调用父类方法

    - 通过`__mro__`列表, 从左到右查找基类, 每个方法也只会被调用一次

        - mro列表: 是使用C3(反向广度优先算法)实现


- 查看mro列表
```py
int.__mro__
# (int, object)
```

- 不使用super(), 调用父类方法
```py
class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')

class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')

c = C()
```
输出: 会调用两次Base
```
Base.__init__
A.__init__
Base.__init__
B.__init__
C.__init__
```

- 使用super(), 调用父类方法

```py
class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')

c = C()
```
输出: 只调用一次Base
```py
Base.__init__
B.__init__
A.__init__
C.__init__
```

- 查看mro列表
```py
C.__mro__

# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)
```

### 多重继承

![image](./imgs/inheritance.png)

- 深度优先: M5 -> M3 -> M1 -> M4 -> M1 -> M2
- 广度优先: M5 -> M3 -> M4 -> M1 -> M2
- C3(反向广度优先): M5 -> M4 -> M3 -> M2 -> M1

- python使用的是C3算法

- 如果两个对象之间没有继承关系, 多重继承可以将他们, 关联起来

```py
class A:
    def f(self):
        print(self[0])

# 关联A类, list类
class B(A, list):
    pass

list1 = B()
list1.append(1)
list1.f()
```

### @dataclass(简化类的定义)

```py
from dataclasses import dataclass

@dataclass
class people:
    name: str
    age: int

# 以上等同于
class people:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

example = people('tz', 24)
print(example)
```

- `frozen`: 设置只读, 默认为False
```py
@dataclass(frozen=True)
class people:
    name: str
    age: int
```

```py
@dataclass(frozen=True)
class people:
    name: str
    age: int

    def __post_init__(self):
        self.age = self.age.upper()

example = people('tz')
```


- `field(default_factory=function)`变量赋值为函数返回值

```py
from dataclasses import dataclass, field

def f():
    return 24

@dataclass
class people:
  name: str
  age:  int = field(default_factory=f)

example = people(name = 'tz')
print(example)
```

### 元类(metaclass)

- `type()` 是python默认的元类

```py
a = 1
print(a.__class__)
print(a.__class__.__class__)
```
输出
```
<class 'int'>
<class 'type'>
```

- `type()` 装饰类, 类似与装饰器于函数

    - 三个参数
        - 1.返回类型
        - 2.继承的类, 用元组表示
        - 3.类字典: 类的属性, 方法

    ```py
    # creating a base class
    class Base:
        def myfun(self):
            print("This is inherited method!")

    def f(self):
        print("This is Test class method!")

    # 装饰类
    Test = type('Test', (Base, ), dict(x = 1, my_method=f))

    o = Test()

    o.myfun()

    o.my_method()

    print(o.x)
    ```
- 使用`__new__` 元类代替函数装饰器

    - 装饰器例子

    ```py
    def debugmethods(cls):
        # vars() 字典类型:类的方法, 方法对象
        for key, val in vars(cls).items():
            # callable() 判断对象能否调用, 函数, 类都为True
            if callable(val):
                # setattr() 对类添加属性或方法
                setattr(cls, key, val)
        return cls

    @debugmethods
    class Calc:
        def add(self, x, y):
            return x+y
        def mul(self, x, y):
            return x*y
        def div(self, x, y):
            return x/y

    mycal = Calc()
    print(mycal.add(2, 3))
    print(mycal.mul(5, 2))
    ```

    - 元类例子
    ```py
    def debugmethods(cls):
        for key, val in vars(cls).items():
            if callable(val):
                setattr(cls, key, val)
        return cls

    # 元类
    class Meta(type):
        def __new__(cls, clsname, bases, clsdict):
            obj = super().__new__(cls, clsname, bases, clsdict)
            # 装饰类
            obj = debugmethods(obj)
            return obj

    # 继承元类
    class Base(metaclass=Meta):pass

    # 继承Base
    class Calc(Base):
        def add(self, x, y):
            return x+y

    # 继承Calc
    class Calc_adv(Calc):
        def mul(self, x, y):
            return x*y

    mycal = Calc_adv()
    print(mycal.add(2, 3))
    print(mycal.mul(5, 2))
    ```



### 内置函数,属性

- ` __new__()`创建实例, 并返回实例

    - 在init()之前调用的方法, 可以重写这个方法来控制如何创建实例

- ` __init__()`初始化实例: 将参数传递给已创建的实例


    > 类实例化的内部函数

    ```py
    class cls(object):
        pass

    a = cls.__new__(cls)

    if isinstance(a, cls):
        cls.__new__(a)

    # 以上等同于
    a = cls()
    ```

    - 通过`__new__` 调用实现类实例缓存, 使相同名字的类实例只有一个
        - 缺点: 这个方法每次都会调用__init__
    ```py
    class O:
        # 通过字典缓存
        cache = {}
        def __new__(cls, name):
            if name in cls.cache:
                return cls.cache[name]
            else:
                self = super().__new__(cls)
                cls.cache[name] = self
                return self

        def __init__(self, name):
            print('init')
            self.name = name

    a = O('tz')
    b = O('tz')
    print(a is b) # True
    ```

- `__del__()` destructors(析构函数)

    > 类引用次数为0时,删除资源的内部析构函数

    尽量不要自定义`__del__()`,否则在以下循环引用的例子会导致内存泄漏

    ```py
    class A:
        def __init__(self, b):
            self.b = b

    class B:
        def __init__(self):
            self.a = A(self)
        def __del__(self):
            print("die")

    b = B()
    ```

- `__call__` 像函数那样调用类.class()

    ```py
    class people(object):
        def __init__(self):
            self.name = 'tz'
        def __call__(self):
            print('class call')

    # test
    a = people()
    a()

    # callable()判断能否对象调用, 返回True
    print(callable(a))
    ```


- `__file__`查看模块路径

    ```py
    import re

    re.__file__
    ```

- `__dict__` 查看class的self变量

    > clss的self变量,使用字典保存

    ```py
    class people(object):
        height = 180
        __weight = 100
        def __init__(self):
            self.name = 'tz'
        def age(self, n):
            self.age = n

    a = people()
    a.age(24)

    a.__dict__
    # a.name 等同于a.__dict__['name']
    a.__dict__['name']
    ```

-  `__slots__` 不使用dictionary(字典)保存self变量

    > 每个class的dictionary浪费大量内存, 而__slots__是一种减少内存的方法

    > 注意: 依赖__dict__代码将无法使用

    ```py
    class people(object):
        __slots__ = ['name', 'age']
        def __init__(self):
            self.name = 'tz'
            self.age = 24

    a = people()
    print(a.__slots__)
    ```

- `__str__()` 和 ` __repr__()`

    - `__str__`: 给用户看的. print()或str(), 才会被调用

    ```py
    class people(object):

        def __init__(self, name):
            self.name = name

        def __str__(self):
            return 'in __str__: my name is %s' % self.name

    print(people('tz'))

    # 给用户看的, 不可以直接调用
    people('tz')
    ```
    输出
    ```
    in __str__: my name is tz
    <__main__.people object at 0x7f250de170a0>
    ```

    - `__repr__`: 给开发者看的. 执行print([class_name]), 传入列表, 返回包含字符串的列表

    ```py
    class people(object):

        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return 'in __str__: my name is %s' % self.name

    print(people('tz'))
    print([people('tz')])

    # 给开发者看的, 可以直接调用
    people('tz')
    ```
    输出
    ```
    in __str__: my name is tz
    [in __str__: my name is tz]
    in __str__: my name is tz
    ```

### class的内置装饰器

- @property: 是一个类装饰器

    > 只读

    ```py
    class people(object):
        def __init__(self, name = 'tz'):
            self.name = name

        @property
        def age(self):
            return 24

    # test
    a = people().age
    # 实例化后无法修改
    a.age = 23
    ```

    访问私有变量

    ```py
    class people(object):
        __age = 24

        def __init__(self, name = 'tz'):
            self.name = name

        @property
        def age(self):
            return self.__age

    # test
    people().age
    ```

- @name.setter

    > 可以修改`@property`的属性

    ```py
    class people(object):
        def __init__(self, name = 'tz'):
            self.name = name

        @property
        def age(self):
            return 24

        @age.setter
        def age(self, age):
            # 这里不能是self.age = age
            people.age = age

    a = people()
    a.age
    a.age = 100
    ```

    修改私有变量

    ```py
    class people(object):
        __age = 24
        def __init__(self, name = 'tz'):
            self.name = name

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, age):
        # 这里不能是__age = age
            people.__age = age

    a = people()
    a.age
    a.age = 100
    ```

- @classsmethod

    > 不需要实例化,就能访问方法

    ```py
    # 访问私有变量
    class people(object):
        __height = 180
        def __init__(self, name = 'tz'):
            self.name = name

        @classmethod
        def height(cls):
            return cls.__height

    people().height()

    # 继承
    class new_people(people):
        pass

    new_people.height()
    ```

- @staticmethod

    > 类外的函数, 不需要强制传递self参数, 不能对类造成影响

    ```py
    class people(object):
        def __init__(self, name = 'tz'):
            self.name = name

        def inside(self):
            a = 1
            # 可以修改类的属性
            self.name = 'inside_tz'
            return a

        @staticmethod
        # 不需要传递self参数
        def outside():
            a = 1
            return a

    # test
    a = people()
    a.name
    a.outside()
    a.inside()
    a.name
    ```

    - [实现状态机](https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p19_implements_stateful_objects_or_state_machines.html)

### @property类装饰器的方法: getattr(), setattr()

- getattr(): 字符串调用类的方法
    ```py
    # 例子1
    class A:
        def f(self, x):
            print(x)

    a = A()
    getattr(a, 'f')(0) # Calls a.f(0)

    # 例子2
    list1 = []
    getattr(list1, 'append')(0) # Calls list1.append(0)
    ```
    - operator.methodcaller(): 另一种字符串调用类的方法
        ```py
        import operator

        list1 = []
        operator.methodcaller('append', 0)(list1)
        ```

- setattr()
```py
class people:
    def __init__(self):
       self.name = 'tz'

# 添加age属性
setattr(people, 'age', 24)

# 可以直接调用
people.age
```
### `__enter__()`, `__exit__()`: 定义with上下文

- contextlib.contextmanager() 装饰器
    - `yield` 之前的代码为`__enter__()`
    - `yield` 之后的代码为`__exit__()

```py
from contextlib import contextmanager

@contextmanager
def list_transaction(list1):
    print('start', list1)
    yield list1
    print('end', list1)


list1 = []
with list_transaction(list1) as list_t:
    list_t.append(1)
    list_t.append(2)
```

### `__getitem__` 和 `__class_getitem__`: 定义带[]的调用 `object['arg']`

- `__getitem__` 函数:
    ```py
    class o:
        def __getitem__(self, x):
            print(x)

    class o1(o): pass

    # ()调用__getitem__函数, []表示传入参数
    o()['test']
    o1()['test']
    ```

    - fib例子

        ```py
        class fib:
        def __getitem__(self, n):
            x, y = 1, 1
            for i in range(n):
                x, y = y, x + y
            return x

        print(fib()[7])
        ```

- `__class_getitem__` 函数:
    ```py
    class o:
        # cls表示类, item表示参数
        def __class_getitem__(cls, item):
            print(f"{cls.__name__}[{item.__name__}]")

    class o1(o): pass

    # []调用__class_getitem__函数, 并传入参数
    o1[int]
    ```

### `__getattribute__`: 当访问不存在的属性时调用

- 注意:对`__`开头和结尾的属性并不适用

```py
class people:
    def __init__(self, name):
        self.name = name

o = people('tz')
o.name

# 报错: 不存在age属性
o.age
```

- 使用`__getattribute__`

```py
class people:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, attr):
        # 如果是age, 就返回对应的值
        if attr == 'age':
            return 24

o = people('tz')
o.name
o.age
```

- 装饰器
```py
def new_getattr(cls):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, attr):
        print(attr)
        return attr

    cls.__getattribute__ = new_getattribute
    return cls


@new_getattr
class people:
    pass

o = people()
o.age # age
```

- 代理:

    - 普通写法
    ```py
    class A:
        def f(self):
            pass

        def f1(self, x):
            pass


    class B:
        def __init__(self):
            self._a = a()

        def f(self):
            return self._a.f()

        def f1(self, x):
            return self._a.f1(x)

    b = B()
    b.f()
    b.f1(1)
    ```
    - 使用`__getattr__`

    ```py
    class Proxy:
        def __init__(self, obj):
            self._obj = obj

        def __getattr__(self, name):
            return getattr(self._obj, name)

    a = A()

    b = Proxy(a)
    b.f()  # Calls B.__getattr__('f')
    b.f1(1)
    ```

- 代理列表对象

```py
class ListLike:
    def __init__(self):
        # 列表对象
        self._obj = []

    def __getattr__(self, name):
        # 找不到属性和方法时, 调用列表对象的方法
        return getattr(self._obj, name)

list1 = ListLike()

# 像列表一样append
list1.append(1)

# 报错: 不支持__len__, 需要自行写入
len(list1)
```

### functools.partialmethod() 只能封装是类里的方法

```py
from functools import partialmethod

class Demo:
    def __init__(self):
        self.color = 'black'

    def _color(self, type):
        self.color = type

    set_red = partialmethod(_color, type='red')
    set_blue = partialmethod(_color, type='blue')
    set_green = partialmethod(_color, type='green')


obj = Demo()
print(obj.color)
obj.set_blue()
print(obj.color)
```
输出
```
black
blue
```
### 描述器

- 通过setattr()实现描述器, 将参数转换成属性

```py
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


o = Descriptor('test', a=1, b=2)
o.a = 10
o.b = 20
```

- 实现类型检查器
```py
class Typed(Descriptor):
    # 类型
    expected_type = type(None)

    def __set__(self, instance, value):
        # 判断类型
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)

class Int(Typed):
    expected_type = int
```

- 实现值的判断
```py
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)
```

#### 实现类的参数类型检查

```py
# 描述器
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

# 类型检查
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        # 判断类型
        if not isinstance(value, self.expected_type):
            print(self.expected_type)
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)

# 类型
class Int(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class Str(Typed):
    expected_type = str

class Stock:
    a = Str('a')
    b = Int('b')
    c = Float('c')

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


# 报错: 第二个参数不是int
Stock('tz', 's', 1.1)

# 不报错
Stock('tz', 0, 1.1)
```

- 装饰器写法
```py
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value


# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# 报错: 第二个参数不是int
Stock('tz', 's', 1.1)

# 不报错
Stock('tz', 0, 1.1)
```
## weakerf(弱引用)

- gc(垃圾回收)

    - 对象的引用数变成0时才会被gc, 而循环引用导致条件永远不会成立

```py
class Data:
    def __del__(self):
        print('Data.__del__')

class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Data()
del a # Data.__del__

a = Node()
del a # Data.__del__

# 循环引用没有触发del(在交互模式下运行)
a = Node()
a.add_child(Node())
del a

# 需要手动触发
import gc
gc.collect()
```

- weakref.ref(): 通过弱引用消除循环引用

    - 弱引用就是一个对象指针，它不会增加它的引用计数

```py
# 重新定义方法
    def add_child(self, child):
        self.children.append(child)
        child.parent = weakref.ref(self)
```

## file

| 权限 | 操作
|------|--------------------------------------|
| r    | 只读(不会覆盖文件)                   |
| w    | 只写(如果文件不存在就创建, 覆盖文件) |
| x    | 只写(文件不存在才写入)               |
| r+   | 读写(不会覆盖文件)                   |
| w+   | 读写(如果文件不存在就创建, 覆盖文件) |
| rb+  | 读写二进制文件                       |
| wb+  | 只写二进制文件                       |
| xb   | 只写二进制文件(文件不存在才写入)     |
| a    | 只写追加尾部                         |
| a+   | 读写追加尾部(如果文件不存在就创建)   |

- 写入文件
```py
with open('/tmp/test', 'w') as file:
    data = "123 321 abc ABC"
    file.write(data)

# 使用print()写入
with open('/tmp/test', 'w') as file:
    print('123 321 abc ABC', file=file)
```

- 读取文件
```py
# 指定编码 file = open('/tmp/test', 'r', encoding='utf-8')

# 文件必须存在
file = open('/tmp/test')

# 只能读取一次
print(file.read())
file.close()

# with 能读取多次
with open('/tmp/test') as file:
        data = file.read()
```

- 读取多个文件
```py
# 边读边写,将首字符转为大写
with open('/tmp/test', 'r') as intf, open('/tmp/test1', 'w') as outf:
    for line in intf:
        print([word.capitalize() for word in line.split()], file=outf)

# for 读取
file = ('test', 'test1')
for i in file:
    f = open(i)
    print(f.read())

f.close()
```

- 防止读取错误
```py
# 防止文件不存在, 报错
if not os.path.exists(file):
    os.mknod(file)

# 防止读取空文件
with open(f, 'r') as file:
    try:
        page_dict |= yaml.load(file)
    except:
        pass
```

- 读写二进制文件
```py
# 读取需要解码, 写入需要编码
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))
```

### readinto()

- 和 read() 不同的是, readinto() 填充已存在的缓冲区, 而不是为新对象重新分配内存再返回它们

    - 可以避免大量的内存分配操作

    - 返回实际读取的字节数

- 二进制io, 可以直接读写C结构, 比如array(数组)
```py
import array

nums_write = array.array('i', [1, 2, 3, 4])
with open('/tmp/test.bin', 'wb') as f:
    f.write(nums_write)

nums_read = array.array('i', [0, 0, 0, 0])
with open('/tmp/test.bin', 'rb') as f:
    f.readinto(nums_read)

print(nums_read)
```

- 读取文件到一个数组里
```py
import os.path

def read_into_buffer(filename):
    # 设置缓冲区为文件的大小
    buf = bytearray(os.path.getsize(filename))

    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

# /tmp/file 内容为: 1234567890
array = read_into_buffer('/tmp/file')

# 使用数组切片
print(array[0:5]) # b'12345'
```

- 使用mmap 模块内存映射文件, 实现数组切片
```py
import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

# mmap.ACCESS_COPY 只写内存, 而不会写入文件
file = memory_map('/tmp/file', mmap.ACCESS_COPY)

# 修改第一个字符, 57是字符串9的ascii码
file[0] = 57
print(file[0:5]) # b'92345'
```

### hdf5

- [Quick Start Guide](https://docs.h5py.org/en/latest/quick.html)

- 序列化数组

```py
import numpy as np
import h5py

# 生成一个大数据集
arr = np.random.randn(1000)

# 写入. 数组的名字为arary1
with h5py.File('/tmp/test.hdf5', 'w') as f:
    dset = f.create_dataset("array1", data=arr)

# 读取
with h5py.File('/tmp/test.hdf5', 'r') as f:
    data = f['array1']

    print(min(data))
    print(max(data))
    print(data[:15])
```

- 压缩文件
```py
# 默认压缩等级是4
with h5py.File('/tmp/test.hdf5', 'w') as f:
    dset = f.create_dataset('array1', data=arr1, compression="gzip", compression_opts=9)
```

- 一个文件保存多个数组
```py
import numpy as np
import h5py

arr1 = np.random.randn(1000)
arr2 = np.random.randn(1000)

# 写入两个数组
with h5py.File('/tmp/test.hdf5', 'w') as f:
    dset = f.create_dataset("array1", data=arr1)
    dset = f.create_dataset("array2", data=arr2)

# 读取两个数组
with h5py.File('/tmp/test.hdf5', 'r') as f:
    arr1 = f['array1']
    arr2 = f['array2']

    # 查询arr1大于0的值的位置, 再读取arr2所对应的位置. [:]表示加载到内存
    data = arr2[arr1[:]>0]
```


### 自定义数据块读写, 而不是行读写

- 多个字符串写入

    - 如果两个字符串很小，第一个更好，因为I/O系统调用天生就慢

    - 如果两个字符串很大，第二个更好，因为它避免了创建一个很大的临时结果并且要复制大量的内存块数据

    ```py
    # Version 1
    f.write(str1 + str2)

    # Version 2
    f.write(str1)
    f.write(str2)
    ```
    - 定义写入大小函数

    ```py
    def sample():
        yield 'Is'
        yield 'Chicago'
        yield 'Not'
        yield 'Chicago?'


    def combine(source, maxsize):
        parts = []
        size = 0
        for part in source:
            parts.append(part)
            size += len(part)
            if size > maxsize:
                print('#')
                yield ''.join(parts)
                parts = []
                size = 0
        yield ''.join(parts)


    with open('/tmp/file', 'w') as f:
        for part in combine(sample(), 32768):
            f.write(part)
    ```

- 二进制读

    - functools.partial: 每次被调用时读取固定字节的可调用对象

```py
from functools import partial

# 数据块大小
SIZE = 32

with open('/tmp/file', 'rb') as f:
    records = iter(partial(f.read, SIZE), b'')
    for r in records:
        print(r)
```

### 读写压缩文件
```py
import gzip

# 必须是二进制字符串
data = b'test'

# 写入
with gzip.open('/tmp/file.gz', 'w') as f:
        f.write(data)

# 读取
with gzip.open('/tmp/file.gz', 'r') as f:
        data = f.read()
```

- compresslevel: 设置压缩等级

```py
with gzip.open('/tmp/file.gz', 'w', compresslevel=5) as f:
    f.write(data)
```

### json

- 对变量的转换: 带s的方法loads(), dumps()

- 对文件的读写: 不带s的方法load(), dump()

```py
import json

# loads() str内的dict转json.注意:字符串外层必须是',字典内必须是"
str_dict = '{"a": 1, "b": 2}'
json.loads(str_dict)

# dumps() dict转换json.'' 变成 ""
dict1 = {'a': 1, 'b': 2}
json.dumps(dict1)
json.dumps(dict1, indent = 4, sort_keys=True)

# load() 读取json文件
with open('test.json') as file:
  data = json.load(file)

# dump() 写入json文件
with open('test.json', 'w') as file:
  json.dump(dict1, file)

# ensure_ascii=False(默认使用ascii编码) 防止中文乱码
with open('test.json', 'w') as file:
  json.dump(dict1, file, ensure_ascii=False)
```

- 通过object_hook参数, 将json字典转为对象
```py
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

s = '{"name": "tz", "age": 24}'
data = json.loads(s, object_hook=JSONObject)

# 读取属性
data.name # tz
data.age # 24
```

- 通过object_pairs_hook参数(json只有list, dict), 传递给其他类型

```py
from collections import OrderedDict

s = '{"name": "tz", "age": 24}'

# 创建OrderedDict类型
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data) # OrderedDict([('name', 'tz'), ('age', 24)])
```

- pprint.pprint(): 更好的显示

```py
from pprint import pprint

data = {
        'completed_in': 0.074,
        'max_id': 264043230692245504,
        'max_id_str': '264043230692245504',
        'next_page': '?page=2&max_id=264043230692245504&q=python&rpp=5',
        'page': 1
        }

print(json.dumps(data, indent=4))
# 或者
json_str = json.dumps(data)
pprint(json_str)
```

- 没有代码注入的安全问题

### yaml

> 操作类似json

```py
import yaml

# 读取json文件
with open('test.json') as file:
  data = yaml.load(f)

# 使用utf编码, 写入文件
with open('test.yaml', 'w') as file:
  yaml.dump(dict1, file, allow_unicode=True)
```

- `yaml.load()` 和`pickle.loads()`一样有代码注入的安全问题

    ```py
    print(yaml.load('!!python/tuple [1, 2, 3]'))
    ```

    - 解决方法: 使用`yaml.safe_load()`代替

    ```py
    yaml.safe_load(f)
    ```

### [toml](https://github.com/toml-lang/toml)

### ini

```py
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read("/tmp/ini.ini")
# 查看所有段
cfg.sections()

# 读取installation段的library键字符串值
cfg.get("installation", "library")

# 读取debug段的log_errors键布尔值
cfg.getboolean("debug", "log_errors")

# 读取server段的nworkers键的int值
cfg.getint("server", "nworkers")
```

### pickle

- 安全问题

    - [从零开始python反序列化攻击：pickle原理解析 & 不用reduce的RCE姿势](https://zhuanlan.zhihu.com/p/89132768)

    - [思辨｜浅谈Python的Pickle模块](https://mp.weixin.qq.com/s?src=11&timestamp=1636190790&ver=3420&signature=eUxnKBaczfVeupHnz1AQTW6rKwqztJQovwcukJQGLp1m58IcvKfnyDu-dSLWHJRQkO3yJJE6QbcWa3duD7gEKGdmhRpN1e3HD*kWLmk0DrbeBn0rhB-vz9hl7G7fsqFi&new=1)

    - 数据和指令保存在一起不加区分, 会有代码注入风险, 因此不要对未知来源的数据进行loads(反序列化)


- 序列化对象

    - 通过pickle将数据和命令, 在进程之间进行传输

- `dumps()`序列化, `loads()`反序列化
```py
import pickle, base64

list1 = [1, 2, 3]

# dumps()6个版本
print(pickle.dumps(list1, protocol=0))
print(pickle.dumps(list1, protocol=1))
print(pickle.dumps(list1, protocol=2))
print(pickle.dumps(list1, protocol=3))
print(pickle.dumps(list1, protocol=4))
print(pickle.dumps(list1, protocol=5))

# 使用base64加密
print(base64.b64encode(pickle.dumps(list1, protocol=0)))

# loads可以自动识别版本
print(pickle.loads(b'(lp0\nI1\naI2\naI3\na.'))

```
输出:
```
b'(lp0\nI1\naI2\naI3\na.'
b']q\x00(K\x01K\x02K\x03e.'
b'\x80\x02]q\x00(K\x01K\x02K\x03e.'
b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.'
b'\x80\x05\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.'
b'KGxwMApJMQphSTIKYUkzCmEu'
[1, 2, 3]
```

- `dump()`, `load()`
```py
import pickle

integers = [1, 2, 3, 4, 5]

# 写入
with open('file', 'wb') as file:
    pickle.dump(integers, file)

# 读取
with open('file', 'rb') as file:
    integers = pickle.load(file)
    print(integers)
```

#### pickletools

- `optimize()`: 优化`dumps()`后的序列化对象

```py
import pickle, pickletools

list1 = [1, 2, 3]

list1_pickle = pickle.dumps(list1,protocol=0)
print(list1_pickle)

# 优化
list1_pickle = pickletools.optimize(list1_pickle)
print(list1_pickle)
```
输出
```
b'(lp0\nI1\naI2\naI3\na.'
b'(lI1\naI2\naI3\na.'
```

- `dis()`反编译序列化对象
```py
pickletools.dis(list1_pickle)
```
输出
```
    0: (    MARK
    1: l        LIST       (MARK at 0)
    2: I    INT        1
    5: a    APPEND
    6: I    INT        2
    9: a    APPEND
   10: I    INT        3
   13: a    APPEND
   14: .    STOP
highest protocol among opcodes = 0
```

### shelve

- [shelve与pickle的区别](https://newbedev.com/what-is-the-difference-between-pickle-and-shelve)

    - 在pickle之上并实现一个序列化dict(字典)

```py
import shelve

file = shelve.open('/tmp/data')
a = ['123', '321']

# 写入
file['a'] = a

# 读取
file['a']

# 关闭
file.close()
```

### pathlib

- [你应该使用 pathlib 替代 os.path](https://zhuanlan.zhihu.com/p/87940289)

  > 面向对象

```py
from pathlib import Path
p = Path('/home/tz/notes/python.md')

# 查看当前程序的绝对路径
Path(__file__).parent.absolute()

# 当前目录
Path().absolute()

# 父目录
p.parent
p.parents[0]
p.parents[1]
p.parents[2]

p.cwd().is_dir()

# 文件名
p.name
# 去除拓展名
p.stem
# 只显示拓展名
p.suffix

# 以.为分格符返回列表
Path('my.tar.bz2').suffixes

# 文件属性
p.stat()

# touch
p = Path('/tmp/test')
p.touch()

# 写入文件,会删除文件原有内容
p.write_text('123\n123\n')

# 读取文件
p.read_text()
# 或者
with p.open() as f:
    for line in f:
        print(line)

# ls
for i in p.iterdir():
        print(i)

# 返回PosixPath对象
p = Path('.')
[i for i in p.glob('*')]

# 区分文件和目录
for i in p.glob('*'):
    if i.is_file():
        print('file: ' + i)
    elif i.is_dir():
        print('dir: ' + i)

# find .
for i in p.glob('**/*'):
    print(i)
```

### os

| 方法        | 操作               |
|-------------|--------------------|
| os.fork()   | 创建子进程         |
| os.setsid() | 创建新会话, 并设置子进程为进程组组长 |

```py
import os

# 创建目录
os.mkdir(filepath)

# 创建文件
os.mknod(filepath)

# 创建ipc文件
os.mkfifo(filepath)

# 删除文件
os.unlink(filepath)
```

```py
from os import walk

# 输出文件和目录
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

# 将名为BBB的目录,改名为AAA
for root, dirs, files in os.walk(".", topdown=False):
   for name in dirs:
      if name == 'BBB':
          src = (os.path.join(root, name))
          dst = (os.path.join(root, 'AAA'))
          os.rename(src,dst)
```
## 日志

### logging
```py
import logging

def main():
    # 设置为DEBUG, 也就是输出所有等级
    logging.basicConfig(filename="app.log", level=logging.DEBUG)

    # 5个等级
    logging.critical('log')
    logging.error('log')
    logging.warning('log')
    logging.info('log')
    logging.debug('log')

if __name__ == "__main__":
    main()
```
输出
```
CRITICAL:root:log
ERROR:root:log
WARNING:root:log
INFO:root:log
DEBUG:root:log
```

- 设置
```py
import logging

# 设置等级debug以上才输出
logging.basicConfig(level=logging.DEBUG)

# 禁用等级CRITICAL以下的输出
logging.disable(logging.CRITICAL)

# filemode='w' 覆盖写入; 默认为'a' 追加写入
logging.basicConfig(filename='app.log', filemode='w')

# 默认格式
logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s')

# 修改格式
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')

# 设置时间格式
logging.basicConfig(datefmt='%d-%b-%y %H:%M:%S')
```

- 配置文件
```ini
; /tmp/log.ini

[loggers]
keys=root

[handlers]
keys=defaultHandler

[formatters]
keys=defaultFormatter

[logger_root]
level=INFO
handlers=defaultHandler
qualname=root

[handler_defaultHandler]
class=FileHandler
formatter=defaultFormatter
args=('app.log', 'a')

[formatter_defaultFormatter]
format=%(levelname)s:%(name)s:%(message)s
```

- 读取配置文件
```py
import logging.config
logging.config.fileConfig('/tmp/log.ini')
```

### [loguru](https://github.com/Delgan/loguru)

- [腾讯技术工程: Python 中日志记录新技能](https://zhuanlan.zhihu.com/p/436603775)

- 不需要繁琐的配置

## lib(库)

### time

| time | 符号 |
|------|------|
| 年   | %Y   |
| 月   | %m   |
| 日   | %d   |
| 时   | %H   |
| 分   | %M   |
| 秒   | %S   |

```py
import time

# 年 月 日 时 分 秒
current_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
print(current_time)
```

- 统计函数运行的时间

```py
from time import time, sleep

start = time()
sleep(1)
end = time()
print('%.2f秒' % (end - start))
```

- 计时器
```py
import time

class Timer:
    # time.perf_counter()时间精度最高
    def __init__(self, func=time.perf_counter):
        self.time = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.time += end - self._start
        self._start = None

    def reset(self):
        self.time = 0.0

    @property
    def running(self):
        return self._start is not None

    # with语句
    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()


def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    t = Timer()

    # 不使用with
    t.start()
    countdown(100)
    t.stop()
    print(t.time)

    # with语句
    with t:
        countdown(100)
    print(t.time)
```

### re(正则表达式)

- 注意:判断字符串开头应使用`str.startswith()`, 而不是re

```py
a = '123abc 192.168.1.1 ABC\n1.1.1.1\nabc ABC\n999.999.999.999\n<meta name="user-login" content="ztoiax">'

# findall() 返回列表. 匹配ip地址
re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', a)

# match() 从头匹配. 成功则返回对象, 匹配失败则返回false
aa = re.match('\d{1,3}', a)
# group() 返回匹配后的字符串
ip = aa.group()

# search() 返回第一个符合匹配
aa = re.search('\d+', a)
ip = aa.group()

# group(1)提取
match = re.search(r'"user-login" content="(.*?)"', a)
name = match.group(1)

# sub 替换
# 所有数字替换成0
aa = re.sub('\d','0', a)

# split 拆分
aa = re.split('[\n\b.]',a)
```

- `compile()` 生成对象

```py
pattern = re.compile('\d{1,3}')

# search() 只返回第一个匹配
pattern.search(a).group()

# finall() 返回所有匹配
re.findall(pattern, a)
```

- flags

```py
# re.DOTALL 换行符
re.compile('.*', re.DOTALL)

# re.I 不区分大小写
re.compile('regex', re.I)

# re.VERBOSE 忽略空格等字符,需要'''
re.compile('''\d{1,3}\.
              \d{1,3}\.
              \d{1,3}\.
              \d{1,3}''', re.VERBOSE)

# 多flags
re.compile('.*', re.DOTALL | re.I | re.VERBOSE)
```
- 剪切板匹配并连接在一起

```py
import pyperclip, re
phoneRegex = re.compile(r'something')

text = str(pyperclip.paste())
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
```

### fnmatch(列表匹配)

```py
import fnmatch
import os

pattern = '*py*'
files = os.listdir('.')
print ('Matches :', fnmatch.filter(files, pattern))
```

### Image

```py
from PIL import Image
image = Image.open('/tmp/test.jpg')

# 裁剪
rect = 80, 20, 500, 550
image.crop(rect).show()

# 缩略
size = (128, 128)
# image.thumbnail(size)

# 旋转
image.rotate(180).show()

# 翻转
image.transpose(Image.FLIP_LEFT_RIGHT).show()

# 滤镜
from PIL import ImageFilter
image.filter(ImageFilter.CONTOUR).show()
```
### pynput.keyboard(自动输入)

```py
# 键盘
from pynput.keyboard import Key, Controller

keyboard = Controller()

# 按一下enter
keyboard.press(Key.enter)

# 按住c
keyboard.release('c')


# 鼠标
from pynput.mouse import Button, Controller as MouseController
mouse = MouseController()
```

### pyautogui(自动化键盘, 鼠标)

- 键盘

```py
import pyautogui

# 输入
pyautogui.typewrite('Hello world!')
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

# keyDown()按住, keyUp()送开
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

# 输入Ctrl-C
pyautogui.hotkey('ctrl', 'c')
```

- 鼠标

```py
# 获取分辨率
pyautogui.size()

# 获取鼠标坐标
pyautogui.position()

# 在100, 150位置,点击左键
pyautogui.click(100,150,button='left')

# 在100, 150位置,点击右键
pyautogui.click(100,150,button='right')

# 双击
pyautogui.doubleClick()

# 鼠标滚动
pyautogui.scroll(200)

# 鼠标向右移动100
pyautogui.moveRel(100, 0, duration=0)

# 拖住移动0.25秒
pyautogui.dragRel(100, 0, duration=0.25)

# 鼠标向下移动100
pyautogui.moveRel(0, 100, duration=0)

# 鼠标向左移动100
pyautogui.moveRel(-100, 0, duration=0)

# 鼠标向上移动100
pyautogui.moveRel(0, -100, duration=0)
```

- 图片

```py
# 获取图片, 需要安装scrot
im = pyautogui.screenshot()

# 读取本地图片
pyautogui.locateOnScreen('123.png')

# 获取像素RGB
im.getpixel((0, 0))
```

### cursesmenu(tui)

### [itchat: 微信库](https://github.com/littlecodersh/itchat)

### [wxpy: 微信自动化](https://github.com/youfou/wxpy)

- [官方文档](https://wxpy.readthedocs.io/zh/latest/)

- 好友

```py
from wxpy import *
# 登陆微信
bot = Bot()

# 查看所有好友
bot.friends()

# 查看所有好友信息
bot.friends().stats_text()

# 查找好友
my_friend = bot.friends().search('name')[0]

# 发送信息
my_friend.send('Hello, WeChat!')
# 发送图片
my_friend.send_image('my_picture.png')
# 发送视频
my_friend.send_video('my_video.mov')
# 发送文件
my_friend.send_file('my_file.zip')
# 以动态的方式发送图片
my_friend.send('@img@my_picture.png')('my_picture.jpg')

# 下载好友头像
img = my_friend.get_avatar()
with open('img.png','wb') as file:
     file.write(img)

# 下载所有好友的头像
for friend in bot.friends():
    img = friend.get_avatar()
    with open(f'{friend.name}.png','wb') as file:
         file.write(img)
```

- 群

```py
# 查看群
bot.groups()

# 查找群
group = bot.groups().search('name')[0]

# 查看群主
group.owner

# 查看群友
for i in group:
    print(i)

# 查看好友是否在群里
my_friend in group

# 查看所有公众号
bot.mps()
```
- 统计好友地区分布

```py
# 获取好友信息
friends_stat = bot.friends().stats()

# 统计好友地区分布
friend_list = []
for province, count in friends_stat["province"].items():
    if province != "":
        friend_list.append([province, count])

# 排序
friend_list.sort(key=lambda x: x[1], reverse=True)

# 打印
for item in friend_list[:10]:
     print(item[0], item[1])
```

- 对以上的统计例子, 使用`pyecharts`生成饼图

```py
from pyecharts.charts import Pie
from pyecharts import options as opts

# 生成饼图
(
    Pie()
    .add("", friend_list)
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts())
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("name.html")
)
```

- 统计好友男女数量

```py
for sex, count in friends_stat["sex"].items():
    # 1代表MALE, 2代表FEMALE
    if sex == 1:
        print("MALE %d" % count)
    elif sex == 2:
        print("FEMALE %d" % count)
```

- 对以上的统计例子, 使用`pyecharts`生成饼图

```py
friends_stat = bot.friends().stats()

sex_list = []
for sex, count in friends_stat["sex"].items():
    # 1代表男, 2代表女
    if sex == 1:
        sex_list.append(['男', count])
    elif sex == 2:
        sex_list.append(['女', count])

# 生成饼图
from pyecharts.charts import Pie
from pyecharts import options as opts
(
    Pie()
    .add("", sex_list)
    .set_colors(["blue", "red"])
    .set_global_opts(title_opts=opts.TitleOpts())
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("name.html")
)
```

- 其它功能

```py
# 打印好友, 群公众号信息
@bot.register()
def print_others(msg):
    print(msg)

# 自动回复
@bot.register(mp)
def forward_message(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

# 指定好友, 自动回复
@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)
```

- 图灵机器人自动回复消息

```py
import json
import requests

# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "你的api key"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "123456"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[tuling] " + result["text"]

@bot.register(my_friend)
def reply_my_friend(msg):
    return auto_reply(msg.text)
```

### [pyecharts: python ECharts数据可视化](https://github.com/pyecharts/pyecharts)

- [官方文档](https://gallery.pyecharts.org/#/README)

- Bar(柱形图)
```py
from pyecharts.charts import Bar

bar = Bar()
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

# x轴
bar.add_xaxis(attr)
# y轴
bar.add_yaxis("商家A", v1)
bar.add_yaxis("商家B", v1)

# 生成html
bar.render('name.html')
```

- 链式调用

```py
from pyecharts.charts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

(
    Bar()
    # x轴
    .add_xaxis(attr)
    # y轴
    .add_yaxis("商家A", v1)
    .add_yaxis("商家B", v1)

    # 生成html
    .render('name.html')
)
```

- Line(折线图)

```py
from pyecharts.charts import Line
import pyecharts.options as opts

line = Line()
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

(
    # 设置宽度, 高度
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=attr)
    .add_yaxis(series_name="商品A", y_axis=v1,)
    .add_yaxis(series_name="商品B", y_axis=v2,)
    .render("name.html")
)
```

- 画点, 画线

```py
from pyecharts.charts import Line
import pyecharts.options as opts

line = Line()
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

(
    Line()
    .add_xaxis(xaxis_data=attr)
    .add_yaxis(series_name="商品A", y_axis=v1,
        # MarkPointOpts()高亮最大, 最小点
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ]
        ),
        # 高亮平均点
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .add_yaxis(series_name="商品B", y_axis=v2,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
        ),
        # MarkLineOpts()最高点画线
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
            ]
        ),
    )
    .render("name.html")
)
```
- 图表转换
```py
from pyecharts.charts import Line
import pyecharts.options as opts

line = Line()
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

(
    Line()
    .add_xaxis(xaxis_data=attr)
    .add_yaxis(series_name="商品A", y_axis=v1,
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .add_yaxis(series_name="商品B", y_axis=v2,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
            ]
        ),
    )
    # 图表转换
    .set_global_opts(
        title_opts=opts.TitleOpts(title="标题", subtitle="子标题"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("name.html")
)
```

- Pie(饼图)

```py
from pyecharts.charts import Pie
from pyecharts import options as opts

data = [['小米', 65], ['三星', 83], ['华为', 20], ['苹果', 116], ['魅族', 44], ['VIVO', 96], ['OPPO', 92]]

phones = (
    Pie()
    .add("", data)
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("name.html")
)
```

### hashlib

- 内置库

```py
import hashlib

name = 'tz'

# md5
token = hashlib.md5(name.encode(encoding='UTF-8')).hexdigest()

# sha256
token = hashlib.sha256(name.encode(encoding='UTF-8')).hexdigest()

# sha3_512
token = hashlib.sha3_512(name.encode(encoding='UTF-8')).hexdigest()
```

### [pyodide: 把python编译成wasm, 在浏览器上运行](https://github.com/pyodide/pyodide)

- [阿里技术:复杂推理模型从服务器移植到Web浏览器的理论和实战](https://mp.weixin.qq.com/s?src=11&timestamp=1638685048&ver=3477&signature=36Xs1HetyvAraQhPQIrJnqPsejKyxVfQCG*Lyuz6sHM1K2XwdWN9l8RJtRH1sdE1AJAhNzZ8ubS-zOcGnxOdwFGHpuoibokcOVzpZuBJf1siUc5CHuTESabz-xXPc6Tf&new=1)

### [locust: web自动化压力测试](https://github.com/locustio/locust)

## cython

- [官方文档](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html)

- 编译:

    - file: `helloworld.pyx`

    ```py
    print('hello world')
    ```
    - file: `setup.py`
    ```py
    from setuptools import setup
    from Cython.Build import cythonize
    import numpy

    setup(
        ext_modules = cythonize("helloworld.pyx"),
        include_dirs=[numpy.get_include()]
    )
    ```
    - 编译生成文件: `helloworld.c`, `helloworld.cpython-39-x86_64-linux-gnu.so`
    ```sh
    python setup.py build_ext --inplace
    ```
    - 运行
    ```py
    import helloworld
    ```

- [timeit性能对比: 使用cython vs 不使用](./python-debug.md#cython)

    - 使用cython快1.8倍

    - 使用cython静态类型快16倍

## [mingshe: 语法糖](https://mingshe.aber.sh/)
- `|>` 管道
```py
10 |> range |> list |> print
```

## [PEP 20: pythonic(python之禅)](https://www.python.org/dev/peps/pep-0020/)

```py
import this
```

![image](./imgs/pythonic.png)
![image](./imgs/pythonic1.png)
![image](./imgs/pythonic2.png)

## [test: 测试](./python-test.md)

## [draw: 画图](./python-draw.md)

## [system: 系统编程](./python-system.md)

## [concurrency: 进程, 线程, 协程](./python-concurrency.md)

## [scientific computing: 科学计算](./python-sc.md)

## [network: 网络](./python-network.md)

## [spider: 网络爬虫和自动化测试](./python-spider.md)

## [debug: 调试](./python-debug.md)

## [algorithms: 算法](./python-algorithms.md)

## [Design Pattern: 设计模式](./python-design_pattern.md)

# reference article(优秀文章)

- [python官方文档](https://docs.python.org/)

- [awesome-python-books](https://github.com/Junnplus/awesome-python-books/blob/master/README-ZH_CN.md)

- [CPython-Internals](https://github.com/zpoint/CPython-Internals/blob/master/README_CN.md)

- [Problem Solving with Algorithms and Data Structures using Python: 此书可以在线交互式运行代码](https://runestone.academy/runestone/books/published/pythonds3/index.html)

    - [Problem Solving with Algorithms and Data Structures using Python 中文版](https://github.com/facert/python-data-structure-cn)

- [Python Built-in Functions: 搜索内置函数的用法](https://www.programiz.com/python-programming/methods/built-in)

- [free-python-books](https://github.com/pamoroso/free-python-books)

- [CPython-Internals](https://github.com/zpoint/CPython-Internals/blob/master/README_CN.md)

- [python - 100 天从新手到大师](https://github.com/jackfrued/Python-100-Days)

- [python-cheatsheet](https://github.com/gto76/python-cheatsheet)

- [pandas中文教程](http://joyfulpandas.datawhale.club/Content/index.html)

- [Python/Golang Web 入坑指南](https://python-web-guide.readthedocs.io/zh/latest/)

- [腾讯技术工程: 新潮小众的 Python 最新语法合集](https://zhuanlan.zhihu.com/p/363157743)

# 第三方软件资源

- [Best-of Python: python资源分类](https://github.com/ml-tooling/best-of-python)

- [awesome-python-cn: Python资源大全](https://github.com/jobbole/awesome-python-cn)

- [Awesome Python: python资源分类排行](https://python.libhunt.com/)

- [awesome-jupyter](https://github.com/markusschanta/awesome-jupyter)

- [rich: 可以很容易的在终端输出添加各种颜色和不同风格](https://github.com/willmcgugan/rich)

- [rembg: 一键扣图](https://github.com/danielgatis/rembg)

- [mitmproxy: http抓包](https://github.com/mitmproxy/mitmproxy)
