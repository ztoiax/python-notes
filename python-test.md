
<!-- mtoc-start -->

* [test(测试)](#test测试)
  * [pytest](#pytest)
    * [基本使用](#基本使用)
    * [6种测试结果](#6种测试结果)
    * [fixture](#fixture)
    * [临时文件tmpdir, tmpfactory](#临时文件tmpdir-tmpfactory)
    * [capsys获取stdout, stderr](#capsys获取stdout-stderr)
      * [recwarn 读取warnings模块](#recwarn-读取warnings模块)
    * [插件](#插件)
    * [配置文件](#配置文件)
      * [pytest.ini](#pytestini)
      * [tox 测试多个python版本](#tox-测试多个python版本)
    * [jenkins(持续集成)](#jenkins持续集成)
  * [unittest](#unittest)
    * [基本使用](#基本使用-1)
    * [patch](#patch)
    * [mock](#mock)
    * [@mock.path()](#mockpath)

<!-- mtoc-end -->

# test(测试)

## pytest

### 基本使用

- [官方文档](https://docs.pytest.org/en/6.2.x/contents.html)

- pytest不需要加入任何代码

| pytest参数        | 操作                                 |
|-------------------|--------------------------------------|
| -x                | 遇到第1个failed就退出                |
| --maxfail=2       | 自定义failed退出的次数               |
| -s                | 输出print()的内容                    |
| -l                | 输出堆栈跟踪                         |
| --trace           | pdb调试                              |
| --pastebin=all    | 发送所有测试结果到 http://bpaste.net |
| --pastebin=failed | 只发送failed测试结果                 |
| --setup-show      | 回溯fixture的执行过程                |
| --cache-show      | 查看缓存                             |
| --lf              | 运行上一次failed的测试               |

```py
# test.py
class Test:
    def test_one(self):
        assert 0
```

- pytest会根据以下规则自动运行

| 文件                   | 类    | 函数   |
|------------------------|-------|--------|
| test_*.py or *_test.py | Test* | test_* |

```sh
pytest ./test.py
```

- 指定运行测试类和函数
```py
class Test:
    def test_one(self):
        assert 0

class Test1:
    def test_two(self):
        assert 0
```

```sh
# 只测试Test1类
pytest ./test.py::Test1

# 只测试Test1类的test_two函数
pytest ./test.py::Test1::test_two
```

- @pytest.mark.name 标记

    - 标记名字可以自定义

```py
# 标记为a
@pytest.mark.a
def test_1():
    assert 0

@pytest.mark.c
def test_2():
    assert 0

# 标记为a和b
@pytest.mark.b
@pytest.mark.a
def test_3():
    assert 0
```

```sh
# 运行标记a. 只运行test_1和test_3
pytest -m a ./test.py

# 运行标记a. 只运行test_3
pytest -m b ./test.py

# 运行标记b和c
pytest -m 'b or c' ./test.py
```

- 输入测试参数
```py
# 输入两个参数
@pytest.mark.parametrize('x, y',
        [(0, 0), (1, 1)])
def test_1(x, y):
    assert 0 == x + y
```
```py
xy = [(0, 0), (1, 1)]

@pytest.mark.parametrize('x, y', xy)
def test_1(x, y):
    assert 0 == x + y
```

- 装饰类, 可以将输入参数传递给的所有方法
```py
@pytest.mark.parametrize('x, y',
        [(0, 0), (1, 1)])
class Test():
    def test_1(self, x, y):
        assert 0 == x + y

    def test_2(self, x, y):
        assert 0 == x + y
```


- 跳过测试
```py
import pytest
import os

# 跳过
@pytest.mark.skip
def test_1():
    assert 0

# 如果不是unix就跳过
@pytest.mark.skipif(os.name!='posix',
        reason='Not supported on Unix')
def test_2():
    assert 0
```

- `@pytest.mark.xfail`捕抓异常
```py
import pytest

@pytest.mark.xfail(raises=ValueError)
def test():
    raise ValueError("Exception 123 raised")
```

- `pytest.raises` 捕抓异常和异常参数

```py
import pytest

def f():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        f()
```

### 6种测试结果

| 测试结果 | 内容                   |
|----------|------------------------|
| failed   | 失败                   |
| passed   | 通过                   |
| skipped  | 跳过                   |
| xfailed  | 预期失败               |
| xpassed  | 预期失败, 但成功       |
| error    | 测试以外的代码出现异常 |

```py
import pytest


@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass
```

```sh
pytest ./test.py
```
输出
```
...省略
======================================== short test summary info =========================================
FAILED test.py::test_fail - assert 0
ERROR test.py::test_error - assert 0
================= 1 failed, 1 passed, 1 skipped, 1 xfailed, 1 xpassed, 1 error in 0.10s ==================
```

- `pytest -r ` 加以下参数. 指定最后部分显示

| r后面的参数 | 最后部分只显示        |
|-------------|-----------------------|
| f           | failed                |
| E           | error                 |
| s           | skipped               |
| x           | xfailed               |
| X           | xpassed               |
| p           | passed                |
| P           | passed with output    |
| a           | all except pP         |
| A           | all                   |
| N           | none (不显示任何内容) |

```sh
pytest -ra ./test.py
```
输出
```
...省略
======================================== short test summary info =========================================
SKIPPED [1] test.py:23: skipping this test
XFAIL test.py::test_xfail
  reason: xfailing this test
XPASS test.py::test_xpass always xfail
ERROR test.py::test_error - assert 0
FAILED test.py::test_fail - assert 0
================= 1 failed, 1 passed, 1 skipped, 1 xfailed, 1 xpassed, 1 error in 0.11s ==================

```

### fixture

> fixture表示测试前的预备工作, 比方说检索测试数据等...

- 使用fixture传递参数
```py
# 在测试函数运行前, 先运行x()
import pytest

# 传递x函数给test_1
@pytest.fixture()
def x():
    return 10

def test_1(x):
    assert 0 == x
```

- 使用request传递参数, request是pytest的内建函数之一
```py
n = [0, 1]

# 将n传递给x函数
@pytest.fixture(params=n)
def x(request):
    # return n
    return request.param

def test_1(x):
    assert 0 == x
```

- yield 上面的语句为setup(测试前运行), 下面的语句为teardown(测试后运行)
```py
@pytest.fixture()
def x():
    # setup
    print('setup')
    yield 10
    # teardown
    print('teardown')

def test_1(x):
    assert 0 == x
```

- 回溯fixture的执行过程

```sh
pytest --setup-show ./test.py
```

- 作用范围: 默认是函数范围

| 名称     | 作用范围 |
|----------|----------|
| function | 函数     |
| class    | 类       |
| module   | 模块     |
| session  | 会话     |

```py
# 设置作用范围为module
@pytest.fixture(scope='module')
```


### 临时文件tmpdir, tmpfactory

- 文件和目录会在, 测试开始时创建, 测试结束后删除

- `tmpdir` 的范围是函数级别

- `tmpfactory` 的范围是会话级别

```py
def test_tmpdir(tmpdir):
    # 新建名为file_a的文件
    file_a = tmpdir.join('file_a')

    # 新建名为dir的目录
    dir = tmpdir.mkdir('dir')

    # 在dir目录下新建名为file_b的文件
    file_b = dir.join('file_b')

    # 写入内容
    file_b.write('test')

    # 测试
    assert file_b.read() == 'test'
```

### capsys获取stdout, stderr

- stdout
```py
def f():
    print('hello world')


def test_capsys(capsys):
    f()
    # 读取stdout, stderr
    out, err = capsys.readouterr()

    # 需要加上换行符\n
    assert out == 'hello world\n'
    assert err == ''
```

- stderr
```py
import sys

def f():
    print('hello world', file=sys.stderr)
```

#### recwarn 读取warnings模块

```py
import warnings


def f():
    warnings.warn('warn')


def test_recwarn(recwarn):
    f()
    w = recwarn.pop()
    assert str(w.message) == 'warn'
```

### 插件

- [插件汇总](https://docs.pytest.org/en/latest/reference/plugin_list.html)

- pytest-cov: 代码的覆盖率
```py
# 指定当前目录
pytest --cov=. test.py

# 生成覆盖率的html文件
pytest --cov=. --cov-report=html test.py
```

- pytest-xdist: 并行测试
```py
pytest -n auto test.py
```

- pytest-timeout: 设置限制时间
```py
# 0.5秒
pytest --timeout=0.5 test.py
```

- pytest-html: 生成html测试报告

```py
pytest --html=report.html test.py
```

- pytest-sugar: 显示进度条

- pytest-emoji: emoji
```py
pytest --emoji test.py
```

### 配置文件

#### pytest.ini

- 设置默认参数
```
[pytest]
; 设置默认参数--emoji
addopts = --emoji
```


- 修改搜索规则
```ini
[pytest]
; class
python_classes = *Test Test* *Suite

; file
python_files = *test_ test_*

; function
python_functions = *test_ test_*
```

- `__init__.py` 解决文件名冲突

a, b两个目录下的测试文件是同名的
```
.
├── a
│   └── test.py
└── b
    └── test.py
```

加入`__init__.py` 可解决报错
```
.
├── a
│   ├── __init__.py
│   └── test.py
└── b
    ├── __init__.py
    └── test.py
```

#### tox 测试多个python版本

- `tox.ini`
```ini
[tox]
; python2.7, python3.9
envlist = py27, py39

[testenv]
deps=pytest
commands=pytest
```

### jenkins(持续集成)


## unittest

### 基本使用

| assert方法                          | 操作                    |
|-------------------------------------|-------------------------|
| assertEqual(a, b)                   | a == b                  |
| assertTrue(x)                       | bool(x) is True         |
| assertFalse(x)                      | bool(x) is False        |
| assertIs(a, b)                      | a is b                  |
| assertIsNone(x)                     | x is None               |
| assertIn(a, b)                      | a in b                  |
| assertIsInstance(a, b)              | isinstance(a, b)        |
| assertRaises(ValueError, func, arg) | 执行func(arg)抛出ValueError |

| 测试结果 | 内容                                   |
|----------|----------------------------------------|
| OK       | 所有测试通过                           |
| FAIL     | 未通过. 抛出`AssertionError`异常       |
| ERROR    | 未通过. 抛出`AssertionError`以外的异常 |

- OK
    ```py
    import unittest

    # 继承unittest.TestCase
    class Test(unittest.TestCase):

        def test(self):
            self.assertTrue(True)

    if __name__ == '__main__':
        # 会自动运行以test开头的函数
        unittest.main()
    ```
    输出
    ```
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    ```
    `-v`参数, 表示详细输出
    ```
    test (__main__.Test) ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    ```

- FAIL
    ```py
    import unittest

    class Test(unittest.TestCase):

        def test(self):
            # 改为False, 让测试Fail
            self.assertTrue(False)

    if __name__ == '__main__':
        unittest.main()
    ```
    输出
    ```
    F
    ======================================================================
    FAIL: test (__main__.Test)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/tz/test.py", line 8, in test
        self.assertTrue(False)
    AssertionError: False is not true

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    FAILED (failures=1)
    ```

- error
    ```py
    import unittest

    class Test(unittest.TestCase):

        def test(self):
            # 输入一个不存在的函数, 让测试error
            self.assertTrue(f)

    if __name__ == '__main__':
        unittest.main()
    ```
    输出
    ```
    E
    ======================================================================
    ERROR: test (__main__.Test)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/tz/./test.py", line 7, in test
        self.assertTrue(f)
    NameError: name 'f' is not defined

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    FAILED (errors=1)
    ```

- 跳过测试
```
import os

class Tests(unittest.TestCase):
    # 跳过测试
    @unittest.skip('skipped test')
    def test_1(self):
        pass

    # 如果是unix系统, 就跳过测试
    @unittest.skipIf(os.name=='posix', 'Not supported on Unix')
    def test_2(self):
        import winreg

    # 预期失败
    @unittest.expectedFailure
    def test_4(self):
        self.assertEqual(2+2, 5)

if __name__ == '__main__':
    unittest.main()
```


### patch

- 测试标准输出. 也就是print()的结果

```py
from io import StringIO
import unittest
from unittest.mock import patch

def f(n):
    print(n)

class Test(unittest.TestCase):
    def test_stdout(self):
        n = 1

        # 使用 StringIO 对象来代替 sys.stdout
        with patch('sys.stdout', new=StringIO()) as out:
            f(n)
            expect_output = f'{n}\n'
            self.assertEqual(out.getvalue(), expect_output)


if __name__ == '__main__':
    unittest.main()
```


### mock
??
```py
from unittest import mock
import requests
import unittest

def get(self):
    r = requests.get('https://www.baidu.com/')
    return r.status

class test(unittest.TestCase):

    def test_success(self):
        success = mock.Mock(return_value='200')
        get = success
        self.assertEqual(get(), '200')

    def test_fail(self):
        fail = mock.Mock(return_value='403')
        get = fail
        self.assertEqual(get(), '403')

if __name__ == "__main__":
    unittest.main()
```

### @mock.path()

- 1.使用flask创建登陆网站

```py
from flask import Flask, jsonify, request
import time, hashlib

app = Flask(__name__)

login_html = '''
<html>
    <head>
        <title>弹窗test</title>
    </head>
    <body>
    <form action="/doLogin" method="post">
    Account: <input type="text" name="account"/><br>
    Password: <input type="text" name="password"/><br>
    <input type="submit" value="Submit"/>
    <input type="reset" value="Reset"/>
    </form>
    </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login_index():
    return login_html

@app.route('/doLogin', methods=['GET', 'POST'])
def do_login():
    if request.method == 'POST':
        account = request.form['account']
        password = request.form['password']

    # 帐号和密码
    if account == 'test' and password == '123':
        timestamp = time.time()

        # 加入time保证每次生成的hash都不一样
        str0 = account + password + str(timestamp)

        # hashlib.md5()生成hash
        token = hashlib.md5(str0.encode(encoding='UTF-8')).hexdigest()
        json = [
                {'token': token, 'user_id': 101}
                ];
        # 返回json格式的登陆信息
        return jsonify({'data': json, 'result': True, 'errorMsg': ''})
    else:
        return jsonify({'data': [], 'result': False, 'errorMsg': 'error'})

if __name__ == "__main__":
    app.run(debug=True)
```

- ??2.测试
```py
import requests

class login(object):
    def __init(self):
        selr.url = 'http://127.0.0.1:5000/doLogin'
        selr.data = {'account': 'test', 'password': '123'}

    def dologin(self):
        res = requests.post(self.url, data = self.data)
        return res.text


class test(unittest.TestCase):
    @mock.patch('login.dologin')
    def test_login(self, mock_opt):
        # 登陆成功的token
        json = [
                {'token': "8a171c99252ffccdd9ccb1e1cc8370bf", 'user_id': 101}
                ];
        json_result = {'data': json, 'result': True, 'errorMsg': ''}
        mock_opt.return_value = json_result
        self.assertEqual(login.dologin(), json_result)

if __name__ == "__main__":
    unittest.main()
```
