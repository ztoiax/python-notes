# Network

## IPy

> 解析ip地址

- 列出网段内的所有ip

```py
from IPy import IP
ip = IP('192.168.1.0/24')

for i in ip:
    print(i)
```

## telnetlib

> 端口搜索

```py
from telnetlib import Telnet
ip = '192.168.1.221'

for port in range(65535):
    try:
       if Telnet(ip, port, timeout=1):
            print(f'{port}  success')
    except ConnectionRefusedError:
        print(f'{port}  fail')
        pass
```

## paramiko(ssh)

- 执行命令

```py
import paramiko

def exec(ip, cmd):
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, 22, 'root')

        stdin, stdout, stderr = client.exec_command(cmd)
        # stdout类似文件类
        print(stdout.read().decode())

centos7='192.168.100.208'
exec(centos7, 'ls -l')
```

- sftp文件操作

```py
import paramiko

def sftp(ip):
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, 22, 'root')

        with client.open_sftp() as ftp:
            # 上传文件
            ftp.put('/tmp/test', '/tmp/test')
            # 修改权限
            ftp.chmod('/tmp/test', 0o755)
            # 改名
            ftp.rename('/tmp/test', '/tmp/rename')
            # 下载回来
            ftp.get('/tmp/rename', '/tmp/rename')

centos7='192.168.100.208'
sftp(centos7)
```

## [scapy](https://github.com/secdev/scapy)

- [官方文档](https://scapy.readthedocs.io/en/latest/)

- 注意:发送数据需要`root`权限

- `_` 代表上一个包

### 基本使用

```py
from scapy import *

# 查看所有命令
ls()

# 设置layout
explore()

# 查看IP包
ls(IP)

# 设置数据包. 注意: 数据包的网络层从左到右递增, 以 / 进行区分
pkt = Ether()/IP(dst="www.baidu.com")/TCP(dport=80)/"GET /index.html HTTP/1.0 \n\n"

# show() 查看包
pkt.show()

# hexdump 以16进制显示
hexdump(pkt)

# 二进制显示
raw(pkt)

# 查看包内各个层的数据. 注意: 下层包是包含上层包的数据. 也就是说: Ether层包含IP层包含TCP层的数据
Raw(raw(pkt))
TCP(raw(pkt))
IP(raw(pkt))
Ether(raw(pkt))
```

- 读取, 写入tcpdump , wireshark抓取的`pcap`文件

```py
# tcpdump抓包
sudo tcpdump -ni eth0 -w packet.pcap

# rdpcap() 读取pcap文件
pkt = rdpcap("packet.pcap")

# wrpcap() 写入pcap文件
wrpcap("temp.cap",pkts)
```

- 保存当前变量
```py
# 查看当前变量
dir()

# 保存文件
save_session("session.scapy")

# 加载文件
load_session("session.scapy")
```

- 保存pdf文件, 需要 `pyx` 模块
```
??
pkt.pdfdump(layer_shift=1)
pkt.psdump("/tmp/isakmp_pkt.eps",layer_shift=1)
```

- 利用元组, 列表快速设置数据包

```py
# 定义ip包
a=IP(dst="www.baidu.com",ttl=[1,2,(5,9)])

# 定义tcp包
c=TCP(dport=[80,443])

# 查看一共多少个包
[p for p in a/c]

# send() 发送
pkt=send(Ether()/a/c, return_packets=True)

# show() 查看
pkt.show()
```

### sr(send and receive)

> send()   : 只发送
> sr1()    : 发送并接受
> sr()     : 发送并接受(包含Unanswered)
> srloop() : 循环发送并接受

```py
# ip 扫描
ans, unans = sr(IP(dst="192.168.1.1",proto=(0,255))/"SCAPY",retry=2)

# arp 扫描
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"),timeout=2)
ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )

# 对网段进行端口扫描
ans, unans = sr( IP(dst="192.168.1.*")/TCP(dport=80,flags="S") )
ans.summary( lambda s,r : r.sprintf("%IP.src% is alive") )

# 端口扫描
res, unans = sr( IP(dst="target")/TCP(flags="S", dport=(1,1024)) )
res.nsummary( lfilter=lambda s,r: (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)) )

# 发送tcp syn(也就是第一次握手)
sr(IP(dst="www.baidu.com")/TCP(sport=RandShort(),dport=[80,443],flags="S"))

# 循环发送接受
srloop(IP(dst="www.baidu.com")/TCP(sport=RandShort(),dport=[80,443],flags="S"))

# _代表上一个包
_

# 赋值
answer, unanswer = _

# 查看返回值
answer.summary()
```

配合`tcpdump`抓包:

    ```sh
    tcpdump -ni enp27s0 dst www.baidu.com and "tcp[tcpflags] & (tcp-syn) != 0"
    ```

    ![image](./imgs/tcp_syn.gif)

- tcp traceroute
```py
ans, unans = sr(IP(dst="www.bilibili.com", ttl=(4,10),id=RandShort())/TCP(flags=0x2))

for snd,rcv in ans:
    print(snd.ttl, rcv.src, isinstance(rcv.payload, TCP))
```

### DNS(需要root用户)

| 属性 | 操作 |
|------|------|
| ra   | 递归 |

```py
from scapy.all import *

dns = '114.114.114.114'
d = DNS(rd = 1,qd=DNSQR(qname='www.baidu.com'))
packet = sr1(IP(dst=dns)/UDP()/d)
packet[DNS].show()
```

可以搭配 [dnspeep](https://github.com/jvns/dnspeep)进行dns监控

### snipp 抓包, 类似tcpdump

```py
sniff(filter="icmp and host 192.168.1.1", count=2)

# 查看刚才抓的包
pkt = _
pkt.summary()

# 抓取所有包
sniff(prn=lambda x: x.summary())

# 显示所有包
sniff(prn=lambda x: x.show())

# 显示网卡
sniff(prn=lambda x: x.sniffed_on+": "+x.summary())

# 显示指定端口, 输出源和目录端口,tcp flag, payload(数据段)
sniff(filter="tcp and ( port 80 or port 443 )",
 prn=lambda x: x.sprintf("%IP.src%:%TCP.sport% -> %IP.dst%:%TCP.dport%  %2s,TCP.flags% : %TCP.payload%"))

# 只显示源和目标ip, 应用层文本
sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
```

- 异步

```py
t = AsyncSniffer()
t.start()
results = t.stop()
```

- tcp连接, 以及http请求

```py
s=socket.socket()
s.connect(("127.0.0.1", 80))
ss=StreamSocket(s,Raw)
ss.sr1(Raw("GET /\r\n"))
```

### 其它命令

```py
traceroute(["www.yahoo.com","www.altavista.com","www.wisenut.com","www.copernic.com"],maxttl=20)

res, unans = traceroute(["www.microsoft.com","www.cisco.com"],dport=[80,443],maxttl=20,retry=-2)
# 使用imagemagick生成图片
res.graph()
# 保存svg图片
res.graph(target="> /tmp/graph.svg") 
# 3d图形
res.trace3D()

# 路由表
conf.route
conf.route.add(net="0.0.0.0/0",gw="192.168.8.1")
conf.route.delt(net="0.0.0.0/0",gw="192.168.8.1")
conf.route.resync()
```

### 自定义数据包

- XByteField()   : 1 byte的整型
- ShortField()   : 2 byte的整型
- IntEnumField() : 类似dict

- scapy的UDP数据包

```py
ls(UDP)

class UDP(Packet):
    name = "UDP"
    fields_desc = [ ShortEnumField("sport", 53, UDP_SERVICES),
                    ShortEnumField("dport", 53, UDP_SERVICES),
                    ShortField("len", None),
                    XShortField("chksum", None), ]
```

- 自定义数据包

```py
# 定义test1, 2, 3字段, 并分配默认值1, 2, 3

class Test(Packet):
    name = "Test packet"
    fields_desc = [ XByteField("test1", 1),
                    ShortField("test2", 2),
                    IntEnumField("test3" , 3 ,
                      { 1: "happy", 2: "cool" , 3: "angry" } ) ]

# 查看数据包
ls(Test)

# 设置数据包
def make_test(x, y, z):
    return Ether()/IP()/Test(test1=x,test2=y,test3=z)

# test3如果大于3, 就是值等于参数, 不会报错
make_test(42, 666, 3)
make_test(42, 666, 4)
```

## requests

- [官方文档](https://requests.readthedocs.io/en/master/)

| 属性方法          | 内容                         |
|-------------------|------------------------------|
| r.headers         | 响应报文                     |
| r.request.headers | 请求报文                     |
| r.content         | byte类型的text(可以decode()) |
| r.text            | str类型的text(中文为unicode) |
| r.json()          | 如果text是json,查看text      |
| r.cookies         | cookies                      |

```py
import requests

# get
r = requests.get('https://www.baidu.com/')

# params 设置参数
p = {'s?wd': '123'}
r = requests.get('https://www.baidu.com/', params=p)

# headers 设置请求头部
url = 'https://www.baidu.com/'
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/90.0.4430.85 Safari/537.36'}

r = requests.get(url=url, headers=headers)
r.request.headers

# post方法的测试网站
url = 'https://httpbin.org/post'

# dict
data1 = {'test': [1, 2]}
# or
data1 = [('test', 1), ('test', 2)]

# 参数data,但实际上是form
r = requests.post(url, data = data1)

# post muti file
# 建议使用二进制模式打开文件
url = 'https://httpbin.org/post'
multiple_files = [
     ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
     ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
 r = requests.post(url, files=multiple_files)
 r.text

# cookies
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.json()

# session
s = requests.Session()
r = s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r.json()

# 确认session是否关闭
with requests.Session() as s:
    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')

# stream=True时只下载响应头,和保持链接.因此需要使用with关闭链接
with requests.get('https://httpbin.org/get', stream=True) as r:
    # Do things with the response here.

# hook
def print_url(r, *args, **kwargs):
    print(r.url)

requests.get('https://httpbin.org/', hooks={'response': print_url})

# hook multpie
def record_hook(r, *args, **kwargs):
    r.hook_called = 'my name is tz'
    return r

r = requests.get('https://httpbin.org/', hooks={'response': [print_url, record_hook]})
r.hook_called

# session hook
s = requests.Session()
s.hooks['response'].append(print_url)
s.get('https://httpbin.org/')

# proxy
proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

requests.get('http://example.org', proxies=proxies)
```

## httpx

> 语法类似`requests`.支持同步, 异步, HTTP2

- [官方文档](https://www.python-httpx.org/)

- 向同一主机发出多个请求时，客户端将重用底层TCP连接(HTTP keep-alive)，而不是为每个请求重新创建一个

- 默认 `encoding` 为 `utf-8`, 而requests的 `encoding` 为 `ISO-8859-1`

```py
import httpx
import asyncio

# async

async with httpx.AsyncClient() as client:
    r = await client.get(url)

# unix domain socket
transport = httpx.HTTPTransport(uds="/var/run/docker.sock")
client = httpx.Client(transport=transport)
response = client.get("http://docker/info")
response.json()

# http2
client = httpx.AsyncClient(http2=True)
r = await client.get(url)
r.http_version
```

- log

```py
# test.py
import httpx

url = 'https://www.baidu.com'

with httpx.Client() as client:
    r = client.get(url)
```

```bash
HTTPX_LOG_LEVEL=debug python3 test.py
DEBUG [2021-03-27 11:45:16] httpx._client - HTTP Request: GET http://www.baidu.com "HTTP/1.1 200 OK"
```

```bash
HTTPX_LOG_LEVEL=trace python3 test.py
TRACE [2021-03-27 11:47:18] httpx._config - load_ssl_context verify=True cert=None trust_env=True http2=False
TRACE [2021-03-27 11:47:18] httpx._config - load_verify_locations cafile=/home/tz/.local/lib/python3.9/site-packages/certifi/cacert.pem
...
```

### httpx vs aiohttp

- [reference](https://gist.github.com/imbolc/15cab07811c32e7d50cc12f380f7f62f)

- 代码:双线程, 10个链接

```py
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse
import httpx
import aiohttp


HOST, PORT = "localhost", 8000
URL = f"http://{HOST}:{PORT}/"


async def index(request):
    return PlainTextResponse("world")


async def aiohttp_single(request):
    async with aiohttp.ClientSession() as client:
        async with client.get(URL) as r:
            return _response(await r.text())


async def aiohttp_session(request):
    async with aiohttp_session.get(URL) as r:
        return _response(await r.text())


async def httpx_single(request):
    async with httpx.AsyncClient() as client:
        r = await client.get(URL)
        return _response(r.text)


async def httpx_session(request):
    r = await httpx_session.get(URL)
    return _response(r.text)


async def httpx_single_http2(request):
    async with httpx.AsyncClient(http2=True) as client:
        r = await client.get(URL)
        return _response(r.text)


async def httpx_session_http2(request):
    r = await httpx_session_http2.get(URL)
    return _response(r.text)


def _response(name):
    return PlainTextResponse("Hello, " + name)


routes = [
    Route("/", endpoint=index),
    Route("/aiohttp/single", endpoint=aiohttp_single),
    Route("/aiohttp/session", endpoint=aiohttp_session),
    Route("/httpx/single", endpoint=httpx_single),
    Route("/httpx/session", endpoint=httpx_session),
    Route("/httpx/single/http2", endpoint=httpx_single_http2),
    Route("/httpx/session/http2", endpoint=httpx_session_http2),
]


async def on_startup():
    global aiohttp_session, httpx_session, httpx_session_http2
    aiohttp_session = aiohttp.ClientSession()
    httpx_session = httpx.AsyncClient()
    httpx_session_http2 = httpx.AsyncClient(http2=True)


app = Starlette(debug=True, routes=routes, on_startup=[on_startup])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
```

- 测试:

```sh
# single
wrk http://localhost:8000/aiohttp/single
wrk http://localhost:8000/httpx/single

# single http2
wrk http://localhost:8000/aiohttp/single/http2
wrk http://localhost:8000/httpx/single/http2

# session
wrk http://localhost:8000/aiohttp/session
wrk http://localhost:8000/httpx/session
```

- 结果:三个测试,都是`aiohttp`更快
