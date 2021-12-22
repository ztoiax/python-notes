
<!-- vim-markdown-toc GFM -->

* [系统编程](#系统编程)
    * [命令行相关](#命令行相关)
        * [typer](#typer)
        * [click](#click)
        * [prompt_toolkit](#prompt_toolkit)
        * [shovel: 像普通命令那样使用](#shovel-像普通命令那样使用)
    * [参数解析](#参数解析)
        * [argparse](#argparse)
        * [optparse(参数)](#optparse参数)
    * [shell](#shell)
        * [subprocess](#subprocess)
            * [Popen](#popen)
                * [asyncio(异步)](#asyncio异步)
                * [gevent](#gevent)
            * [clipboard](#clipboard)
            * [安全问题:代码注入](#安全问题代码注入)
    * [性能监控](#性能监控)
        * [psutil](#psutil)
    * [监控文件](#监控文件)
        * [pyinotify](#pyinotify)
    * [限制cpu, 内存](#限制cpu-内存)

<!-- vim-markdown-toc -->
# 系统编程

## 命令行相关

### [typer](https://github.com/tiangolo/typer)

> 快速构建命令行的帮助信息, 针对函数

### [click](https://github.com/pallets/click)

> 快速构建命令行的帮助信息, 针对变量. 执行完@click.command()的函数后会自动退出

- [官方文档](https://click.palletsprojects.com/en/7.x/)

- 打开编辑器,并输出编辑器的输入

```py
import click

message = click.edit()
print(message, end='')
```

- 账号, 密码输入

```py
import click

@click.command()
@click.option("--account", prompt="Account", help="The person to greet.")
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def main(account, password):
    print(f'account:{account}')
    print(f'password:{password}')

main()
```

### [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)

    > 打造像ipython, mycli的交互REPL


### [shovel: 像普通命令那样使用](https://github.com/seomoz/shovel)

- 保存至`/home/tz/.shovel.py`
```py
from shovel import task

@task
def hello():
    print('hello')

@task
def f(x, y):
    print(x, y)
```

- 在终端下运行

```sh
# 调用hello函数
shovel hello

# 调用f函数, 并输入参数
shovel f 1 2
```


## 参数解析

### argparse

- [文档](https://zetcode.com/python/argparse/)

```py
import argparse
parser = argparse.ArgumentParser()

# 如果有-o, --output参数,有则为true
# 注意: 必须要有参数-o
parser.add_argument('-o', '--output', action='store_true', help="shows output")

# 自定义属性now
parser.add_argument('-a', '--add', dest='now', action='store_true', help="shows output")

# required赋值
parser.add_argument('--name', required=True)

# type定义类型
parser.add_argument('-n', type=int, required=True)

# default
parser.add_argument('-e', type=int, default=2, help="defines the exponent value")

# append 多个重复参数
parser.add_argument('-n', '--name', dest='names', action='append')

args = parser.parse_args()
print(args)

# 如果有-o, --output参数,就执行
if args.output:
    print("This is some output")
    print(f'Hello {args.name}')

# 如果没有-o, --output参数,就执行
if not args.output:
    print("This is some output")
    print(f'Hello {args.name}')

if args.now:
    print("This is add")
```

### optparse(参数)

> 允许未add的参数

`argparse` 模块如果遇上没有`add_argument`的参数会报错`error: unrecognized arguments`

`optparse` 这不会有这个问题:

```py
from optparse import OptionParser
parser = OptionParser()
parser.add_option('-n', '--nmap', action='store_true',
                  help="nmap mode")

# positional是没有add_option的其他参数
args, positional = parser.parse_args()
```

## shell

### subprocess

- 返回值:

    - subprocess.call 返回$?(是否执行成功)

    - subprocess.check_output 返回 str

        - 如果报错则出现subprocess.CalledProcessError

    - subprocess.run 返回对象(subprocess.CompletedProcess)

    - subprocess.Popen 返回对象(subprocess.Popen)

    - 更建议使用 run, Popen

```py
# 默认以列表类型运行
subprocess.call(['echo', '123'])

# shell = True 以字符串类型执行
subprocess.call('echo 123', shell = True)

# 不显示命令执行的输出
subprocess.call('echo 123', shell = True, stdout=subprocess.PIPE):

# check_output 获取stdout
output = subprocess.check_output('echo 123', shell=True)

# 将二进制的输出结果转换为str
output = output.decode('utf-8')
# 或者
# universal_newlines=True 将输出转换为str
output = subprocess.check_output('echo 123', shell=True, universal_newlines=True)
output.rstrip() # 去除换行符\n

# 获取标准stdout, stderr, return code
output = subprocess.run('echo 123', shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output.stdout
output.stderr
output.returncode
```

#### Popen

- [Popen](https://queirozf.com/entries/python-3-subprocess-examples)

```py
from subprocess import Popen
# 在后台以子进程运行
p = Popen(["ls","-l"])

# wait()则会阻塞,等待并获取返回值.也就是wait()后才能获取returncode
p.wait()

# pid返回子进程pid
p.pid

# terminate()终止运行
p.terminate()

# 获取stdout, error.注意:必须stdout=subprocess.PIPE,不然output为空
p = Popen("echo 123",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
output, error = p.communicate()

# 重定向输入输出
test = '/tmp/test'
file = open(test,'w+')
# stdout=file.重定向输出
p = Popen("echo 123",shell=True, stdout=file, stderr=subprocess.PIPE, universal_newlines=True)

# p2 stdin=p1.stdout.重定向输出

# PIPE ls -lha | grep foo bar
from subprocess import Popen,PIPE
p1 = Popen(["ls","-lha"], stdout=PIPE)
p2 = Popen(["grep", "foo bar"], stdin=p1.stdout, stdout=PIPE)
p1.stdout.close()
```

##### asyncio(异步)

```py
import asyncio

async def command(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()
    return stdout.decode().strip()
```

- 执行命令

```py
asyncio.run(command('ls /tmp'))
```

- loop执行命令

```py
loop = asyncio.get_event_loop()

# Gather uname and date commands
commands = asyncio.gather(command('uname'), command('date'))

# Run the commands
uname, date = loop.run_until_complete(commands)

# Print a report
print('uname: {}, date: {}'.format(uname, date))
loop.close()
```

- stdin, stdout通信

```py
import asyncio

async def echo(msg):
    # Run an echo subprocess
    process = await asyncio.create_subprocess_exec(
        'cat',
        # stdin must a pipe to be accessible as process.stdin
        stdin=asyncio.subprocess.PIPE,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE)

    # Write message
    print('Writing {!r} ...'.format(msg))
    process.stdin.write(msg.encode() + b'\n')

    # Read reply
    data = await process.stdout.readline()
    reply = data.decode().strip()
    print('Received {!r}'.format(reply))

    # Stop the subprocess
    process.terminate()
    code = await process.wait()
    print('Terminated with code {}'.format(code))


loop = asyncio.get_event_loop()
loop.run_until_complete(echo('hello!'))
loop.close()
```
##### gevent
```py
import gevent
from gevent.subprocess import Popen, PIPE

def cron():
    while True:
        print("cron")
        gevent.sleep(0.2)

g = gevent.spawn(cron)
sub = Popen(['sleep 1; uname'], stdout=PIPE, shell=True)
out, err = sub.communicate()
g.kill()
print(out.rstrip())
```

#### clipboard

- 相当于 `pyperclip` 模块

```py
def getClipboard():
    cmd = 'xclip -selection clipboard -o'
    output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
    return output

def setClipboard(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

setClipboard('data'.encode())
```

#### 安全问题:代码注入

- [Python中的10个常见安全问题](https://medium.com/hackernoon/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03)

- ping例子
```py
import subprocess, sys, re

address = sys.argv[1]

# 匹配是否为ip地址
if not re.match("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", address):
    print('error')
    exit(1)

print(address)
subprocess.call("/bin/ping -c 3 '{0}'".format (address), shell = True)
```

- 注入代码

```sh
 ./test.py "127.0.0.1';/bin/cat /etc/passwd;'"
```

- 解决方法: 使用`shlex` 模块

    - 该模块只适用与unix

```py
import subprocess, sys, re
import shlex

address = sys.argv[1]

# shlex.quote()
address = shlex.quote(address)

# 匹配是否为ip地址
if not re.match("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", address):
    print('error')
    exit(1)

print(address)
subprocess.call("/bin/ping -c 3 '{0}'".format (address), shell = True)
```

## 性能监控

### [psutil](https://github.com/giampaolo/psutil)

- [官方文档](https://psutil.readthedocs.io/en/latest/)

psutil.Popen:

```py
import psutil
from subprocess import PIPE
p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
p.name()
p.communicate()
p.wait(timeout=2)
```

bytes2human():

```py
def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n
```

```py
# 统计time_wait的连接
cons =psutil.net_connections()
len([c for c in cons if c.status == 'TIME_WATI'])
```

## 监控文件

### pyinotify

- [官方文档](https://github.com/seb-m/pyinotify/wiki)

- [Events-types(mask)](https://github.com/seb-m/pyinotify/wiki/Events-types)
```py
import pyinotify

wm = pyinotify.WatchManager()

# mask = delete, create
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE

# 自定义类
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print("Creating: ", event.pathname)

    def process_IN_DELETE(self, event):
        print("Deleting: ", event.pathname)

# handler可单独call: handler(new_event)
handler = EventHandler()

notifier = pyinotify.Notifier(wm, handler)
# 不使用自定义类
notifier = pyinotify.Notifier(wm)

# timeout周期性监控
# notifier = pyinotify.Notifier(wm, handler, timeout=10)

# wdd 所有监控的路径: 字典类型
# rec 是否递归
wdd = wm.add_watch('/tmp', mask, rec=True)
wdd = wm.add_watch('/tmp', pyinotify.ALL_EVENTS, rec=True)

# 取消某个监控路径
wm.rm_watch(wdd['/tmp/dir'])
wm.rm_watch(wdd['/tmp/dir'], rec=True)

# 开始轮询
notifier.loop()
```

开启新线程:

```py
notifier = pyinotify.ThreadedNotifier(wm, EventHandler())
notifier.start()
# 关闭
notifier.stop()
```

异步:

```py
notifier = pyinotify.AsyncNotifier(wm, EventHandler())
wdd = wm.add_watch('/tmp', mask, rec=True)
import asyncore
asyncore.loop()
```

## 限制cpu, 内存
```py
import signal
import resource

def func(signo, frame):
    print("Time's up!")
    raise SystemExit(1)

def set_max_runtime(seconds):
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    # 限制cpu时间
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    # 超过限制就发送信号, 并执行func函数
    signal.signal(signal.SIGXCPU, func)

if __name__ == '__main__':
    set_max_runtime(15)
    while True:
        pass
```
