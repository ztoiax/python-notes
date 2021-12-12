# test(测试)

## pytest

### 基本使用

- [官方文档](https://docs.pytest.org/en/6.2.x/contents.html)

- pytest不需要加入任何代码

```py
# test.py
class Test:
    def test_one(self):
        assert 0
```

- pytest会自动运行以test开头的类和函数
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

- pytest 参数
```sh
# pdb调试
pytest --trace ./test.py

# pastbin=all 发送所有测试结果到 http://bpaste.net
pytest --pastebin=all ./test.py
# 只发送failed测试结果
pytest --pastebin=failed ./test.py
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

| 测试结果 |
|----------|
| failed   |
| passed   |
| skipped  |
| xfailed  |
| xpassed  |
| error    |

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
