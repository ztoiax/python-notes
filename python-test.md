# test

## unittest

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

