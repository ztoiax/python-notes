# OSI 7层

> 本文采用自顶向下的讲解

![image](./Pictures/net-kernel/osi.avif)

![image](./Pictures/net-kernel/osi1.avif)

## 应用层

### HTTP

- [mozilla文档](https://developer.mozilla.org/zh-CN/docs/Web/HTTP)

- [视频：2分钟了解 HTTP Verbs](https://www.bilibili.com/video/BV1DS4y187Ux)
    - 安全性：`GET`
    - 幂等性：`GET`、`DELETE`
    - 缓存性：`GET`、`POST`、`PATCH`

- [腾讯技术工程：了解 HTTP 看这一篇就够](https://cloud.tencent.com/developer/article/2083715)

- [技术蛋老师视频：HTTP/1.1，HTTP/2和HTTP/3的区别](https://www.bilibili.com/video/BV1vv4y1U77y)

![image](./Pictures/net-kernel/http.avif)

#### 状态码

- `1xx`：
    - `101 Switching Protocol`： 协议转换，比方说升级为`websocket`

- `2xx`：

    - `200 OK`

    - `201 Created`：成功创建资源，一般用于`POST`、`PUT`

    - `204 No Content`：没有body

    - `206 Partial Content`：分块下载和断点续传，在客户端发送“范围请求”、要求获取资源的部分数据时出现，它与 200 一样，也是服务器成功处理了请求，但 body 里的数据不是资源的全部，而是其中的一部分。

        - `Accept-Ranges` （它的值不为“none”），那么表示该服务器支持范围请求。

        - 还会伴随着头字段`Content-Range`，表示响应报文里 body 数据的具体范围，供客户端确认，例如`Content-Range：bytes 0-99/2000`，意思是此次获取的是总计 2000 个字节的前 100 个字节。

        ```sh
        curl http://www.example.com -i -H "Range: bytes=0-50, 100-150"
        ```

- `3××`：

    - `301 Moved Permanently`：“永久重定向”，含义是此次请求的资源已经不存在了，需要改用改用新的 URI 再次访问。

    - `302 Found`：“临时重定向”，意思是请求的资源还在，但需要暂时用另一个 URI 来访问。

        - 例子：访问`www.bing.com` 会出现`302`，重定向到`cn.bing.com`

    - `304 Not Modified`：它用于 `If-Modified-Since` 和`If-None-Match` 请求，表示资源未修改，用于缓存控制。它不具有通常的跳转含义，但可以理解成“重定向已到缓存的文件”（即“缓存重定向”）。

#### Cache

- [腾讯技术工程：彻底弄懂浏览器缓存策略](https://cloud.tencent.com/developer/article/1660735)

    ![image](./Pictures/net-kernel/cache.avif)

- `Cache-Control: `：

    - `private`：只能浏览器缓存，代理服务器不能缓存

    - `no-cache`：浏览器可以缓存，但每次都需要向服务器确认；代理服务器不能缓存

    - `no-store`：不能缓存

    - `max-age=604800`：可以缓存；根据`Date: ` 字段的时间算起，604800秒后过期。

    - `Expires: Tue, 28 Feb 2022 22:22:22 GMT`：过期时间

    - `Expires` 和 `max-age`同时存在优先使用`max-age`

- `Last-Modified`(Response Header)与`If-Modified-Since`(Request Header)是一对报文头：

    - 当带着If-Modified-Since头访问服务器请求资源时，服务器会检查Last-Modified，如果Last-Modified的时间早于或等于If-Modified-Since则会返回一个不带主体的304响应，否则将重新返回资源。

    - 注意：在 Chrome 的 devtools中勾选 `Disable cache` 选项后，发送的请求会去掉If-Modified-Since这个 Header。

- `ETag`(Response Header)与`If-None-Match`(Request Header)是一对报文头：

    - 一致时返回不带实体的304，不然就是带有所请求资源实体的200响应

- `ETag` 和 `Last-Modified`同时存在优先使用`ETag`

- `X-Cache-Lookup:`：

    - `Hit From MemCache`：命中CDN节点的内存
    - `Hit From Disktank`：命中CDN节点的硬盘
    - `Hit From Upstream`：没有命中

- 缓存位置：

    - 优先级：Service Worker -> Memory Cache -> Disk Cache -> Push Cache

    - Chrome 的DevTools Network可以看到`Memory Cache`（內存缓存）和`Disk Cache`（硬盘缓存）

#### Cookie

- [技术蛋老师视频：cookie、localStorage 和 sessionStorage的区别及应用实例 - JavaScript前端Web工程师](https://www.bilibili.com/video/BV1SL4y1i7ZL)

- [技术蛋老师视频：Cookie、Session、Token究竟区别在哪？如何进行身份认证，保持用户登录状态？](https://www.bilibili.com/video/BV1ob4y1Y7Ep)

- 过期时间：

    - `Expires`：绝对时间

    - `max-age`：相对时间，单位为秒。

    - `Expires` 和 `max-age` 同时存在时优先使用`max-age`。

        - 如果服务器不设置`max-age`、`Expries`或者字段值为0指不能缓存cookie，但在会话期间是可用的，浏览器会话关闭之前可以用cookie记录用户的信息。

- 作用域：

    - `Domain`和`Path`指定了 Cookie 所属的域名和路径，浏览器在发送 Cookie 前会从 URI 中提取出 host 和 path 部分，对比 Cookie 的属性。如果不满足条件，就不会在请求头里发送 Cookie。

        - Domain=mozilla.org，则 Cookie 也包含在子域名中（如developer.mozilla.org）

        - Path (“/”) 作为路径分隔符，并且子路径也会被匹配

- 安全性

    - `HttpOnly`表示此 Cookie 只能通过浏览器 HTTP 协议传输，禁止其他方式访问。这也是预防“跨站脚本”（XSS）攻击的有效手段。

    - `SameSite`可以防范“跨站请求伪造”（XSRF）攻击

        - SameSite = strict表示禁止cookie在跳转链接时跨域传输

        - SameSite = lax稍微宽松一点，允许在GET、HEAD等安全请求方式中跨域携带。

            - 如果没有设置 SameSite 属性，则将 cookie 视为 Lax

        - 默认值为none，表示不限制cookie的携带和传输。

            - 必须设置 `Secure` 属性

    - `Secure`表示这个cookie仅能用HTTPS协议加密传输，明文的HTTP协议会禁止发送。但Cookie本身不是加密的，浏览器里还是以明文的形式存在。

#### HTTP1.1 keepalive


- http短连接
    ![image](./Pictures/net-kernel/http_short_connect.avif)

- http keepalive（长连接）
    ![image](./Pictures/net-kernel/http_keepalive.avif)

#### HTTP2

- [李银城：从Chrome源码看HTTP/2](https://zhuanlan.zhihu.com/p/34662800)

##### HPACK（头部压缩）

- 客户端和服务器各自维护一份“索引表”，压缩和解压缩就是查表和更新表的操作。还釆用哈夫曼编码来压缩整数和字符串。

    ![image](./Pictures/net-kernel/HAPCK.avif)

- 新增的头字段或者值保存在动态表（Dynamic Table）里，它添加在静态表后面，结构相同，但会在编码解码的时候随时更新。

    - 比如说，第一次发送请求时的“user-agent”字段长是一百多个字节，用哈夫曼压缩编码发送之后，客户端和服务器都更新自己的动态表，添加一个新的索引号“65”。那么下一次发送的时候就不用再重复发那么多字节了，只要用一个字节发送编号就好。

    ![image](./Pictures/net-kernel/HPACK-Dynamic-Table.avif)

#### HTTP3(Quic)

- [腾讯技术工程：HTTP/3 原理实战](https://cloud.tencent.com/developer/article/1634011)

    - 讲述了QUIC的优点，比另外两篇文章要好一些[《一文读懂 HTTP/1HTTP/2HTTP/3》](https://cloud.tencent.com/developer/article/1580468)和[科普：QUIC 协议原理分析](https://cloud.tencent.com/developer/article/1017235)

- [交互式解释Quic每个步骤](https://quic.xargs.org/)

#### tls

- [技术蛋老师视频：HTTPS是什么？加密原理和证书。SSL/TLS握手过程](https://www.bilibili.com/video/BV1KY411x7Jp)

- [李银城：https连接的前几毫秒发生了什么](https://www.rrfed.com/2017/02/03/https/)

#### 合并请求 vs 并行请求

- [《React进阶之路》作者：合并HTTP请求 vs 并行HTTP请求，到底谁更快？](https://segmentfault.com/a/1190000015665465)

- [腾讯技术工程：HTTP 请求之合并与拆分技术详解](https://cloud.tencent.com/developer/article/1837260)

    - 拆分的多个小请求耗时仍大于合并的请求

### WebSocket

- [ruanyifeng:WebSocket 教程](https://www.ruanyifeng.com/blog/2017/05/websocket.html)

    ![image](./Pictures/net-kernel/websocket.avif)

- 与http的区别

    - 全双工：服务端可以主动向客户端发送数据；不像http客户端发送request，服务端response

    - 不需要发送http header

### DNS

![image](./Pictures/net-kernel/dns.avif)

- 域名可以对应多个ip地址，从而实现负载均衡

    - 第1种方法：域名解析可以返回多个 IP 地址，客户端收到多个 IP 地址后，就可以自己使用轮询算法依次向服务器发起请求，实现负载均衡。

    - 第2种方法：域名解析可以配置内部的策略，返回离客户端最近的主机，或者返回当前服务质量最好的主机，这样在 DNS 端把请求分发到不同的服务器，实现负载均衡。

- [李银城：从Chrome源码看DNS解析过程](https://www.rrfed.com/2018/01/01/chrome-dns-resolve/)

### FTP

![image](./Pictures/net-kernel/ftp.avif)

- 最常用的配置是`passive`。如果是`active`防火墙起不到保护作用。

### 数字签名和数字证书

- [ruanyifeng：数字签名是什么？](https://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html)

- 数字签名：的原理其实很简单，就是把公钥私钥的用法反过来，之前是公钥加密、私钥解密，现在是私钥加密、公钥解密。但又因为非对称加密效率太低，所以私钥只加密原文的摘要，这样运算量就小的多，而且得到的数字签名也很小，方便保管和传输。

- 数字证书和CA：因为公钥是任何人都可以发布的，所以我们需要引入第三方来保证公钥的可信度，这个“第三方”就是我们常说的 CA（Certificate Authority，证书认证机构）。小一点的 CA 可以让大 CA 签名认证，但链条的最后，也就是 Root CA

### 密钥算法

- [视频：【不懂数学没关系】DH算法 | 迪菲-赫尔曼Diffie–Hellman 密钥交换](https://www.bilibili.com/video/BV1sY4y1p78s)

- [视频：数学不好也能听懂的算法 - RSA加密和解密原理和过程](https://www.bilibili.com/video/BV1XP4y1A7Ui)

- [视频（奇乐编程学院）：探秘公钥加密算法 RSA](https://www.bilibili.com/video/BV14y4y1272w)

    > 对比上一个rsa视频，对欧拉函数有进一步介绍

- [视频：公钥加密技术ECC椭圆曲线加密算法原理](https://www.bilibili.com/video/BV1BY411M74G)

### tls

- [交互式解释tls1.3每个步骤](https://tls13.xargs.org/)

![image](./Pictures/net-kernel/tls1.2.avif)

![image](./Pictures/net-kernel/tls1.3.avif)

## Session layer（会话层）

- [Session and Presentation layers in the OSI model](https://www.ictshore.com/free-ccna-course/session-and-presentation-layers/)

> 定义数据的重传、重排。tcp已经包含了这些功能，所以一般用于udp；为音视频、实时流（real-time-streams）提供服务。

### RTP

> VoIP技术基于rtp协议。rtp基于udp之上实现了重排、计时的功能

- header

    ![image](./Pictures/net-kernel/UDP_RTP_header.avif)

    - `Sequence number`：可以重排，但不能重传

## 传输层

- 三种端口

| 端口类型             | 端口范围    | 内容                         |
|----------------------|-------------|------------------------------|
| Well-known(已知端口) | 0-1023      | HTTP FTP DNS 等              |
| Reserved(保留端口)   | 1024-49151  | 分配给服务端。需要从IANA购买 |
| Dynamic(动态端口)    | 49152-65535 | 分配给客户端                 |

### TCP

- [详解tcp1](https://codeburst.io/understanding-tcp-internals-step-by-step-for-software-engineers-system-designers-part-1-df0c10b86449)

- [详解tcp2](https://codeburst.io/understanding-tcp-internals-step-by-step-for-software-engineers-system-designers-part-2-8557c06c2f7b)

- [tcp 带图详解](https://www.ictshore.com/free-ccna-course/transmission-control-protocol-advanced/)

- [腾讯技术工程：彻底弄懂TCP协议：从三次握手说起](https://cloud.tencent.com/developer/article/1687824)

- [详解的 tcp 连接,丢包后的处理,keepalive,tcp window probes 丢包](https://blog.cloudflare.com/when-tcp-sockets-refuse-to-die/)

- [李银城：WebSocket与TCP/IP](https://www.rrfed.com/2017/05/20/websocket-and-tcp-ip/)

#### header(头部)

![image](./Pictures/net-kernel/TCP_header.avif)

- 数据偏移（Data Offset）：该字段长 4 位，单位为 4 字节。表示为 TCP header的长度。所以 TCP 首部长度最多为 60 字节。

- flags

    | flags | 内容                                                                                             |
    |-------|--------------------------------------------------------------------------------------------------|
    | CWR   | 用于 IP 首部的 ECN 字段。ECE 为 1 时，则通知对方已将拥塞窗口缩小。                               |
    | ECE   | 在收到数据包的 IP 首部中 ECN 为 1 时将 TCP 首部中的 ECE 设置为 1，表示从对方到这边的网络有拥塞。 |
    | URG   | 紧急模式                                                                                         |
    | ACK   | 确认                                                                                             |
    | PSH   | 推送，接收方应尽快给应用程序传送这个数据。没用到                                                 |
    | RST   | 该位为 1 表示 TCP 连接中出现异常必须强制断开连接。                                               |
    | SYN   | 初始化一个连接的同步序列号                                                                       |
    | FIN   | 该位为 1 表示今后不会有数据发送，希望断开连接。                                                  |

- 窗口大小（Window）： 该字段长度位 16 位，即 TCP 数据包长度为 65535字节（大概64KB）。可以通过 Options 字段的 WSOPT 选项扩展到 1GB。

    - TCP 窗口扩大因子：`option-kind` 为 3，`option-length` 为 3 个字节，`option-data` 取值范围 0-14。窗口扩大因子用来扩大 TCP 窗口，可把原来 16bit 的窗口，扩大为 31bit。

- TCP Options：

    - SACK_Permitted：只允许在前两次 TCP 握手的设置，表示两方是否支持 SACK。

    - SACK(选择性确认)。该选项参数告诉对方已经接收到并缓存的不连续的数据块，发送方可根据此信息检查究竟是哪些块丢失，从而发送相应的数据块。受 TCP 包长度限制，TCP 包头最多包含四组 SACK 字段。


    - TSOPT：对应linux内核参数`tcp_timestamps`（默认启用）

        - `tcp_timestamps`：每个 TCP 数据包都会携带一个timestamps（时间戳），用于检测延迟和丢失的数据，计算`RTT`。

            ```sh
            # 查看是否启用，1表示启用（默认启用）
            sysctl net.ipv4.tcp_timestamps
            net.ipv4.tcp_timestamps = 1
            ```

    - RTTM（RTT 测量）：发送方在 TSval 处放置一个时间戳，接收方则会把这个时间通过 TSecr 返回来。因为接收端并不会处理这个 TSval 而只是直接从 TSecr 返回来，因此不需要双方时钟同步。这个时间戳一般是一个单调增的值，[RFC1323] 建议这个时间戳每秒至少增加 1。

        - 第一次握手初始 SYN 包中因为发送方没有对方时间戳的信息，因此 TSecr 会以 0 填充，TSval 则填充自己的时间戳信息。

    - PAWS（防回绕序列号）：PAWS 假设接收到的每个 TCP 包中的 TSval 都是随时间单调增的，基本思想就是如果接收到的一个 TCP 包中的 TSval 小于刚刚在这个连接上接收到的报文的 TSval，则可以认为这个报文是一个旧的重复包而丢掉。

- [MTU and TCP MSS](https://www.imperva.com/blog/mtu-mss-explained/)

    ![image](./Pictures/net-kernel/MTU.avif)

    - [小林coding：既然 IP 层会分片，为什么 TCP 层还需要 MSS 呢？](https://www.xiaolincoding.com/network/3_tcp/tcp_interview.html#%E6%97%A2%E7%84%B6-ip-%E5%B1%82%E4%BC%9A%E5%88%86%E7%89%87-%E4%B8%BA%E4%BB%80%E4%B9%88-tcp-%E5%B1%82%E8%BF%98%E9%9C%80%E8%A6%81-mss-%E5%91%A2)

        - 如果一个 IP 分片丢失，整个 IP 报文的所有分片都得重传。经过 TCP 层分片后，如果一个 TCP 分片丢失后，进行重发时也是以 MSS 为单位，而不用重传所有的分片

##### Header Compression(头部压缩)

- 此功能用于路由器和卫星连接

- 路由器接受到的包，如果有相同的源、目的ip和源、目的端口的时候。对头部的ip字段和端口字段进行压缩（使用hash id），而不会压缩其它字段。然后转发到下一个路由器，下一个路由器接受到后进行解压缩。

    - 40bytes的header压缩后的只有4bytes

    ![image](./Pictures/net-kernel/TCP_header_compression.avif)

#### TCP 连接

- [tcp 三次握手,四次挥手 in wireshark](https://github.com/zqjflash/tcp-ip-protocol)

- [腾讯技术工程：深入理解 Linux 的 TCP 三次握手（源码解析）](https://aijishu.com/a/1060000000343326)

- [腾讯技术工程：彻底弄懂 TCP 协议：从三次握手说起](https://cloud.tencent.com/developer/article/1687824)

- TCP 协议规范：不对 ACK 进行 ACK

- tcp建立连接；关闭连接

    ![image](./Pictures/net-kernel/TCP_States_in_a_connection.avif)
    ![image](./Pictures/net-kernel/TCP_States_in_a_connection1.avif)

    - 三次握手：

        > 目的是初始化序列号

        - 1.client 端首先发送一个 SYN 包告诉 Server 端我的初始序列号是 X
        - 2.Server 端收到 SYN 包后回复给 client 一个 ACK 确认包，告诉 client 说我收到了；接着 Server 端也需要告诉 client 端自己的初始序列号，于是 Server 也发送一个 SYN 包告诉 client 我的初始序列号是 Y
        - 3.Client 收到后，回复 Server 一个 ACK 确认包说我知道了。

    - 四次挥手：TCP 是全双工的，需要 Peer 两端分别各自拆除自己通向 Peer 对端的方向的通信信道。这样需要四次挥手来分别拆除通信信道

        - 四次挥手变三次挥手：如果 Server 在收到 Client 的 FIN 包后，在也没数据需要发送给 Client 了，那么对 Client 的 ACK 包和 Server 自己的 FIN 包就可以合并成为一个包发送过去

    - client和server同时连接

        ![image](./Pictures/net-kernel/TCP_handshake.avif)

    - client和server同时关闭连接

        ![image](./Pictures/net-kernel/TCP_Simultaneous_close.avif)

    - `RST`flag直接进入CLOSED状态

        ![image](./Pictures/net-kernel/TCP_Reset_connection.avif)

        - 第1种情况：server端发送`RST` 后进入`CLOSED`；client端接受`RST` 也进入`CLOSED`

        - 第2种情况：server端发送`RST` 后进入`CLOSED`；但`RST` 丢包了，client端仍在发送数据，但接受不到`ACK` ，超时后进入`CLOSED`

            - 一方发了RST以后，连接一定会终止么?

                ![image](./Pictures/net-kernel/TCP_rst.avif)

                - 不一定会终止，需要看这个RST的Seq是否在接收方的接收窗口之内，Seq号较小的情况下不是一个合法的RST被Linux内核无视了。

- [小林coding：为什么是三次握手？不是两次、四次？](https://www.xiaolincoding.com/network/3_tcp/tcp_interview.html#%E4%B8%BA%E4%BB%80%E4%B9%88%E6%98%AF%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B-%E4%B8%8D%E6%98%AF%E4%B8%A4%E6%AC%A1%E3%80%81%E5%9B%9B%E6%AC%A1)

    - 防止历史连接：client发送syn，但出现故障重启后发送新的syn后；如果server响应了旧的syn，client收到后发送`RST` 就可以终止了历史连接。

        ![image](./Pictures/net-kernel/TCP_handshake_why.avif)

    - 两次握手的两种问题：

        - client发送syn，但出现故障重启后发送新的syn后；server响应了旧的syn就进入ESTABLISHED状态后：server就建立了历史连接，开始向client发送数据，直到收到client的`RST` 才关闭连接。之前的数据就白白发送了。

            ![image](./Pictures/net-kernel/TCP_handshake_why1.avif)

        - 如果client发送的syn网络拥塞，超时后client重发了syn；server响应了旧的syn就进入ESTABLISHED状态后：server收到重发的syn，分配连接造成资源浪费。

- [小林coding：为什么每次建立 TCP 连接时，初始化的序列号都要求不一样呢？](https://www.xiaolincoding.com/network/3_tcp/tcp_interview.html#%E4%B8%BA%E4%BB%80%E4%B9%88%E6%AF%8F%E6%AC%A1%E5%BB%BA%E7%AB%8B-tcp-%E8%BF%9E%E6%8E%A5%E6%97%B6-%E5%88%9D%E5%A7%8B%E5%8C%96%E7%9A%84%E5%BA%8F%E5%88%97%E5%8F%B7%E9%83%BD%E8%A6%81%E6%B1%82%E4%B8%8D%E4%B8%80%E6%A0%B7%E5%91%A2)

    - 防止接受历史包：如果连接中断，但发送的包还在网络中；而重新建立的连接之后，会收到了旧的包，由于ISN（序列号）一致，server会响应了旧的包，造成数据混乱

            ![image](./Pictures/net-kernel/TCP_isn_different.avif)


    - `ISN` Initial Sequence Number（初始序列号）随机生成算法：`ISN = M + F`

        - M 是一个计时器，这个计时器每隔 4 微秒加 1。溢出后从0开始。

        - F 是一个 Hash 算法，根据源 IP、目的 IP、源端口、目的端口生成一个随机数值。要保证 Hash 算法不能被外部轻易推算得出，用 MD5 算法是一个比较好的选择。

        - 防止攻击者猜测出`ISN`，攻击者如果知道`ISM` 可以伪造并发送`RST` 关闭连接

- [小林coding：灵魂拷问 TCP ，你要投降了吗？](https://cloud.tencent.com/developer/article/2141541)

    ```sh
    # client发送syn后，未收到syn、ack的重发次数（默认为6次）（重试间隔为1s, 3s, 7s, 15s, 31s, 63s ）超过重发次数后，直接进入CLOSED状态
    sysctl net.ipv4.tcp_syn_retries
    net.ipv4.tcp_syn_retries = 6

    # server发送syn、ack后，未受到ack的重发次数（默认为5次）（重试间隔为1s, 3s, 7s, 15s, 31s）超过重发次数后，直接进入CLOSED状态
    sysctl net.ipv4.tcp_synack_retries
    net.ipv4.tcp_synack_retries = 5

    # 第三次握手丢失后server端进入CLOSED、client端进入ESTABLISHED状态后发数据的重传次数；又或者两端都是ESTABLISHED状态的重发次数。（默认为15次）一共924.6秒，也就是15.4分钟
    sysctl net.ipv4.tcp_retries2
    net.ipv4.tcp_retries2 = 15

    # 第一、二、三、四次挥手的重发次数。超过重发次数后，直接进入CLOSED状态
    sysctl net.ipv4.tcp_orphan_retries
    net.ipv4.tcp_orphan_retries = 0
    ```

- `TIME_WAIT` 相关：

    ```sh
    # tcp关闭连接后保持TIME_WAIT时间。目的是防止丢失Fin包，如果没有接受到ack会再次发送fin包（默认为60秒）
    sysctl net.ipv4.tcp_fin_timeout
    net.ipv4.tcp_fin_timeout = 60

    # TIME_WAIT的最大并发数量。超过这个值时，系统就会将后面的 TIME_WAIT 连接状态重置
    sysctl net.ipv4.tcp_max_tw_buckets
    net.ipv4.tcp_max_tw_buckets = 32768
    ```

    - 为什么要等待2MSL？如果直接`CLOSED` 如果对方没有收到ack，那么会再次收到第三次挥手的fin后，可以重发，并再次重置2MSL定时器。

        > MSL：报文段最大生存时间，它是任何报文段被丢弃前在网络内的最长时间。

        - MSL 与 TTL 的区别： MSL 的单位是时间，而 TTL 是经过路由跳数。所以 MSL 应该要大于等于 TTL 消耗为 0 的时间，以确保报文已被自然消亡。

            - TTL 的值一般是 64，Linux 将 MSL 设置为 30 秒

            ```sh
            sysctl net.ipv4.ip_default_ttl
            net.ipv4.ip_default_ttl = 64
            ```

        ![image](./Pictures/net-kernel/TCP_TIME-WAIT_2msl.avif)

    - 为什么是主动关闭方才会有`TIME_WAIT` 状态：主动关闭方在发送完 ACK 就走了的话，如果最后发送的 ACK 在路由过程中丢掉了，最后没能到被动关闭方，这个时候被动关闭方没收到自己 FIN 的 ACK 就不能关闭连接，接着被动关闭方会超时重发 FIN 包，但是这个时候已经没有对端会给该 FIN 回 ACK，被动关闭方就无法正常关闭连接了

        ![image](./Pictures/net-kernel/TCP_TIME-WAIT_2msl1.avif)

    - `TIME_WAIT`消耗的 Client 的端口的解决方法：

        - 1.`tcp_tw_reuse` 和 `tcp_timestamps`（默认启用）对应tcp header的options的`TSOPT`

            - `tcp_tw_reuse`：调用 connect() 函数时，内核会随机找一个 TIME_WAIT 状态超过 1 秒的连接给新的连接复用

                ```sh
                # 查看是否启用，2表示启用
                sysctl net.ipv4.tcp_tw_reuse
                net.ipv4.tcp_tw_reuse = 2
                ```
            - `tcp_timestamps`重复的数据包会因为时间戳过期被自然丢弃。

                - 一共 8 个字节表示时间戳，其中第一个 4 字节字段用来保存发送该数据包的时间，第二个 4 字节字段用来保存最近一次接收对方发送到达数据的时间。

                ```sh
                sysctl net.ipv4.tcp_timestamps
                net.ipv4.tcp_timestamps = 1
                ```

        - 2.内核收到 RST 将会产生一个错误并终止该连接。我们可以利用 RST 包来终止掉处于 TIME_WAIT 状态的连接，其实这就是所谓的 RST 攻击了。以下为三个步骤

            - 1.client：利用 `IP_TRANSPARENT` 这个 socket 选项，它可以 bind 不属于本地的地址，因此可以从任意机器绑定 Client 地址以及端口 port1，然后向 Server 发起一个连接Server
            - 2.server：收到了窗口外的包于是响应一个 ACK，这个 ACK 包会路由到 Client 处
            - 3.client：这个时候 99% 的可能 Client 已经释放连接 connect1 了，这个时候 Client 收到这个 ACK 包，会发送一个 RST 包，server 收到 RST 包然后就释放连接 connect1 提前终止 TIME_WAIT 状态了

    - [小林coding：服务器出现大量 TIME_WAIT 状态的原因有哪些？](https://www.xiaolincoding.com/network/3_tcp/tcp_interview.html#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%87%BA%E7%8E%B0%E5%A4%A7%E9%87%8F-time-wait-%E7%8A%B6%E6%80%81%E7%9A%84%E5%8E%9F%E5%9B%A0%E6%9C%89%E5%93%AA%E4%BA%9B)

        - HTTP/1.1长连接：client请求数量超过server指定的最大长连接个数（比如 nginx 配置中的 `keepalive_requests` 参数），那么server会主动断开这个连接，此时服务器上就会出现大量的TIME_WAIT 状态。解决方式：调大最大长连接个数。

        - nginx（在服务器上跑）与后端进行大量的短连接请求，由于nginx 会主动挂断这个连接，在server上就会出现大量的 TIME_WAIT 状态。解决方式：使用长连接

        - client在超时时间内没有新的数据发送，那么server会主动挂断这个连接，在server上就会出现 TIME_WAIT 状态。

        - server进程挂掉了，会出现大量的 TIME_WAIT 状态。

            - TCP 的连接信息是由内核维护的，所以当服务端的进程崩溃后，内核需要回收该进程的所有 TCP 连接资源，于是内核会发送第一次挥手 FIN 报文，后续的挥手过程也都是在内核完成，并不需要进程的参与，所以即使服务端的进程退出了，还是能与客户端完成 TCP 四次挥手的过程。

- TCP端口、连接问题？

    - TCP有多少端口可以使用？

        - `bind(0)`系统调用当参数为0时：Linux内核随机分配一个端口号，Linux内核会在 net.ipv4.ip_local_port_range 系统参数指定的范围内，随机分配一个没有被占用的端口。

        - 但`bind(0)` 不能绑定TIME_WAIT状态，也就是内核参数`net.ipv4.tcp_tw_reuse`

            - 解决方法：`bind()`指定端口

        ![image](./Pictures/net-kernel/TCP_bind(0).avif)

        ```sh
        sysctl net.ipv4.ip_local_port_range
        net.ipv4.ip_local_port_range = 32768	60999
        ```

    - tcp和udp可以绑定同一个端口吗？

        - 可以。sever端的tcp和udp的都可以同时拥有80端口

            ![image](./Pictures/net-kernel/port.avif)

    - 文件描述符限制：每个 TCP 连接都是一个文件，如果文件描述符被占满了，会发生 too many open files。
        - 系统级：当前系统可打开的最大数量：`cat /proc/sys/fs/file-max`
        - 用户级：指定用户可打开的最大数量：`ulimit -n`
        - 进程级：单个进程可打开的最大数量：`cat /proc/sys/fs/nr_open`

#### 队列

- `backlog队列`：

    - 当网卡接收数据包的速度大于内核处理的速度时，`backlog队列` 会保存这些数据包，等待软中断处理

    - 队列大小 × 中断频率 = packets per second

    - 可以通过 `/proc/net/softnet_stat` 的第二列来验证, 如果第二列有计数, 则说明出现过 backlog 不足导致丢包

    ```sh
    # 查看backlog队列大小
    sysctl net.core.netdev_max_backlog
    net.core.netdev_max_backlog = 1000
    ```

- syn半连接队列、accept全连接队列：

    ![image](./Pictures/net-kernel/TCP_queue.avif)
    ![image](./Pictures/net-kernel/TCP_queue1.avif)

    - SYN 半连接队列：Server 端收到 Client 的 SYN 包并回复 SYN,ACK 包后，该连接的信息就会被移到accept队列。超过队列长度后Server 会丢弃新来的 SYN 包

        ```sh
        sysctl net.ipv4.tcp_max_syn_backlog
        net.ipv4.tcp_max_syn_backlog = 512

        # 如果是启用了tcp_syncookies。绕过syn队列也就是tcp_max_syn_backlog设置的值也会被忽略，server端生成cookie，在第二次握手返回client
        sysctl net.ipv4.tcp_syncookies
        net.ipv4.tcp_syncookies = 1
        ```

        - `SYN flood` 攻击原理：短时间内伪造大量不同ip地址并向server端发送syn，但不发送最后一次握手的ack；从而让server端一直处于`SYN_RCVD` 状态，占满`tcp_max_syn_backlog` 队列，并不断超时重发syn ack
            - 解决方法：

                - 增大`netdev_max_backlog`
                - 增大`net.ipv4.tcp_max_syn_backlog`
                - 开启`net.ipv4.tcp_syncookies`
                - 增大`net.core.somaxconn`
                - 减少`net.ipv4.tcp_synack_retries`（默认为5次）

    - accept 全连接队列： Server 端收到第三次握手的ACK包后，就会将连接信息从SYN 半连接队列移到此队列（此时三次握手已经完成）。`accept()`socket 接口，从「Accept 队列」取出连接对象，返回用于传输的 socket 的文件描述符

        ```sh
        sysctl net.core.somaxconn
        net.core.somaxconn = 4096
        ```

        - 队列满了后根据`tcp_abort_on_overflow` 值做出行动：

            - 值为1时：server 在收到 SYN_ACK 的 ACK 包后，协议栈会丢弃该连接并回复 RST 包给对端，这个是 Client 会出现 (connection reset by peer) 错误。

            - 值为0时：server 在收到第三次握手的ACK包后，直接丢弃该 ACK 包。 Client 认为连接已经建立了，一直在等 Server 的数据，直到超时出现 read timeout 错误。

            ```sh
            sysctl net.ipv4.tcp_abort_on_overflow
            net.ipv4.tcp_abort_on_overflow = 0
            ```

#### 延迟ACK

- 1.收到多个seq，返回一个ack

- 2.ACK 在收到数据后并不马上回复，而是延迟一段可以接受的时间，目的是返回ack+数据，而不是单独返回一个ack，从而提高网络利用率

#### 重传与RTT、RTO

> RTT(Round Trip Time)：一个数据包从发出去到回来的时间

> RTO(Retransmission TimeOut)：重传时间

- RTT计算算法：

    - [ ] RFC793算法：

        - 1. 首先采样计算RTT值，会有以下图片的问题

            ![image](./Pictures/net-kernel/rto.avif)

        - 2.然后计算平滑的RTT，称为Smoothed Round Trip Time (SRTT)：SRTT = ( ALPHA * SRTT ) + ((1-ALPHA) * RTT)
            - ALPHA（加权移动平均）：取值在 0.8 到 0.9 之间

        - 3.RTO = min[UBOUND,max[LBOUND,(BETA*SRTT)]]
            - UBOUND 是 RTO 值的上限（可以定义为 1 分钟）
            - LBOUND 是 RTO 值的下限（可以定义为 1 秒）
            - BETA：取值在 1.3 到 2.0 之间

    - [ ] Karn/Partridge 算法解决RTT采样问题：当出现超时重传，接收到重传数据的确认信息时不更新 RTT

        - 问题：如果在某一时间，网络闪动，突然变慢了，产生了比较大的延时，这个延时导致要重转所有的包（因为之前的 RTO 很小），于是，因为重转的不算，所以，RTO 就不会被更新

    - [x] Jacobson / Karels算法解决以上问题（今天的tcp算法）：除了考虑每两次测量值的偏差之外，其变化率也应该考虑在内

- RTO定时器：

    - [ ] 为 TCP 中的每一个数据包维护一个定时器，在这个定时器到期前没收到确认，则进行重传。 这种方案将会有非常多的定时器，会带来巨大内存开销和调度开销。

    - [x] RFC2988以连接来确定定时器
        - 1.每一次发送包（包含重传的包）时如果定时器没有启动，则开启定时器

- Fast Retransmit(快速重传) 的算法：

    - 连续收到三个相同确认号的ack，立刻重传，而不需要等待定时器

- SACK：它允许设备单独确认段(segments)，从而只重传丢失的段

    ![image](./Pictures/net-kernel/TCP_SACK_vs_normale_ACK.avif)

- 伪重传（不必要的重传）机制：

    - DSACK：发送端接受到DSACK时，判断是发送端的包丢失了？还是接收端的 ACK 丢失了？

        - 发送端重传了一个包，发现并没有 D-SACK 那个包，那么就是发送的数据包丢了；否则就是接收端的 ACK 丢了，或者是发送的包延迟到达了

        - 发送端可以判断自己的 RTO 是不是有点小，导致过早重传

    - Eifel 检测算法 [RFC3522]：利用了 TCP 的 TSOPT 来检测伪重传。

        - 比仅采用 DSACK 更早检测到伪重传行为，因为它判断伪重传的 ACK 是在启动丢失恢复之前生成的。相反， DSACK 只有在重复报文段到达接收端后才能发送，并且在 DSACK 返回至发送端后才能有所响应。

    - F-RTO：只检测由重传计时器超时引发的伪重传

#### Tcp keepalive

- 在空闲时，TCP 向对方发送空数据的 ack keepalive 探测包，如果没有响应，socket 关闭。

- TCP keepalive 进程在发送第一个 keepalive 之前要等待两个小时（默认值 7200 秒），然后每隔 75 秒重新发送一次。只要 TCP/IP socket 通信正在进行并处于活动状态，就不需要 keepalive。

- socket接口需要设置`SO_KEEPALIVE`

![image](./Pictures/net-kernel/TCP_keepalive.avif)
![image](./Pictures/net-kernel/TCP_keepalive1.avif)

```bash
# 在最后一个 data packet（空 ACK 不算 data）之后,多长时间开始发送keepalive
sysctl net.ipv4.tcp_keepalive_time
net.ipv4.tcp_keepalive_time = 7200

# 发送探测包的时间间隔.在此期间,连接上的任何传输内容,都不影响keepalive的发送
sysctl net.ipv4.tcp_keepalive_intvl
net.ipv4.tcp_keepalive_intvl = 75

# 最大失败次数
sysctl net.ipv4.tcp_keepalive_probes
net.ipv4.tcp_keepalive_probes = 9
```

#### TCP Fast Open

> 需要client和server端同时支持

- [What is TCP Fast Open?](https://www.keycdn.com/support/tcp-fast-open)

- [lwm:TCP Fast Open: expediting web services](https://lwn.net/Articles/508865/)

- 初始阶段比传统三次握手多了请求`cookie`

    ![image](./Pictures/net-kernel/TCP_fast_open.avif)

    - `cookie` 根据client的ip生成

- 之后的阶段

    ![image](./Pictures/net-kernel/TCP_fast_open1.avif)

    - client端：首次syn包含`cookie` 和数据

    - server端：根据client的ip验证`cookie`

        - cookie有效：立即传送数据，不需要等待cilent端的第三次握手的ack

        - cookie无效：server端丢弃client的数据，对client的syn返回一个syn，ack。也就是回到传统三次握手

    - 配合tls1.3的话，tcp三次握手可以与tls1.3同时进行

```sh
# 查看是否开启tcp fast open（linux默认情况下是开启的）。返回0表示没有开启、1表示客户端开启、2表示服务端开启、3表示客户端服务端都开启
cat /proc/sys/net/ipv4/tcp_fastopen

# 永久启用
echo "net.ipv4.tcp_fastopen=3" > /etc/sysctl.d/30-tcp_fastopen.conf
```
##### nginx支持

编译时加入`-DTCP_FASTOPEN=23`

- 开启
```nginx
listen 80 fastopen=256
```

#### TCP window(窗口，流量控制)

- rwnd（接收端窗口）：接收端告诉发送端自己还有多少缓冲区可以接收数据。

- 发送端其发送缓存内的数据都可以分为 4 类：

    ![image](./Pictures/net-kernel/TCP_window_category.avif)

    - 1.已经发送并得到接收端 ACK 的
    - 2.已经发送但还未收到接收端 ACK 的
    - 3.未发送但允许发送的 (接收方还有空间)
    - 4.未发送且不允许发送 (接收方没空间了)

    - 窗口变化：收到 36 的 ACK 后，窗口向后滑动 5 个 byte：
        ![image](./Pictures/net-kernel/TCP_window_category1.avif)
        ![image](./Pictures/net-kernel/TCP_window_category2.avif)

- 窗口变0过程：

    ![image](./Pictures/net-kernel/TCP_window_reduce.avif)

    - 当接收端通知一个 zero 窗口的时候，发送端的发送窗口也变成了 0，也就是发送端不能发数据了。

    - 发送端在窗口变成 0 后，会发 ZWP（Zero Window Probe） 的包给接收方，来探测目前接收端的窗口大小，一般这个值会设置成 3 次，每次大约 30-60 秒

        - 如果 3 次过后还是 0 的话，有的 TCP 实现就会发 RST 掉这个连接。

        - DDoS 攻击点：攻击者可以在和 Server 建立好连接后，就向 Server 通告一个 0 窗口，然后 Server 端就只能等待进行 ZWP，于是攻击者会并发大量的这样的请求，把 Server 端的资源耗尽。

- 接收端的窗口被填满，然后接收处理完几个字节，腾出几个字节的窗口后，通知发送端，这个时候发送端马上就发送几个字节给接收端吗？

    - 在接收端解决方案（David D Clark’s方案）：如果收到的数据导致 window size 小于某个值，就 ACK 一个 0 窗口，等到接收端处理了一些数据后 windows size 大于等于了 MSS，或者 buffer 有一半为空，就可以通告一个非 0 窗口。

    - 在发送端解决方案（Nagle’s algorithm）：
        - 1.如果包长度达到 MSS ，则允许发送
        - 2.如果该包含有 FIN ，则允许发送
        - 3.设置了 TCP_NODELAY 选项，则允许发送
        - 4.设置 TCP_CORK 选项时，若所有发出去的小数据包（包长度小于 MSS）均被确认，则允许发送
            - Nagle 算法并不禁止发送小的数据包 (超时时间内)，而是避免发送大量小的数据包。
        - 5.上述条件都未满足，但发生了超时（一般为 200ms ），则立即发送

#### TCP congestion control(拥塞算法)

- [腾讯技术工程：TCP 拥塞控制算法简介](https://cloud.tencent.com/developer/article/1401283)

- [TCP 流量控制、拥塞控制](https://zhuanlan.zhihu.com/p/37379780)

- [腾讯技术工程：TCP 拥塞控制详解](https://cloud.tencent.com/developer/article/1636214)

- 拥塞算法依赖于一个拥塞窗口 `cwnd`（以包为单位，因此乘以MSS）

    - Linux 3.0 后采用了 Google 的论文[《An Argument for Increasing TCP’s Initial Congestion Window》](https://static.googleusercontent.com/media/research.google.com/zh-CN//pubs/archive/36640.pdf)的建议——把 cwnd 初始化成了 10 个 MSS。

- `swnd`（滑动窗口） = min(rwnd, cwnd)

- BSD初始版本的Reno算法：

    ![image](./Pictures/net-kernel/TCP_congestion_reno.avif)

    - Slow Start（慢热启动算法）

        - 每当收到一个 ACK，cwnd = cwnd + 1; 呈线性上升

        - 每当过了一个 RTT，cwnd = cwnd * 2; 呈指数上升

        - 有一个慢启动门限 ssthresh（一般为65535 bytes）。 当 cwnd >= ssthresh 时进入拥塞避免算法

    - Congestion Avoidance（拥塞避免算法）

        - 每收到一个 ACK，cwnd = cwnd + 1 / cwnd; 呈线性上升

        - 出现 RTO 超时重传数据包时：
            - 1.ssthresh 的值为当前 cwnd 值的 1/2
            - 2.reset 自己的 cwnd 值为 1
            - 3.然后重新进入慢启动过程

        - 出现收到 3 个 duplicate ACK 进行重传数据包时：进入快速重传

    - Fast Retransimit（快速重传）

        > 表明网络只是轻微拥堵

        - 1.调整门限 ssthresh 的值为当前 cwnd 值的 1/2
        - 2.将 cwnd 值设置为新的 ssthresh 的值
        - 3.重新进入拥塞避免阶段

    - Fast Recovery（快速恢复算法）

        > 快速恢复的思想是 “数据包守恒” 原则：即带宽不变的情况下，在网络同一时刻能容纳数据包数量是恒定的。当 “老” 数据包离开了网络后，就能向网络中发送一个 “新” 的数据包。既然已经收到了 3 个duplicated ACK，那么就是说可以在发送 3 个分段了。

        ![image](./Pictures/net-kernel/TCP_Conservation.avif)

        - 在进入快速恢复前：sshthresh = cwnd / 2，cwnd = sshthresh

        - 1.cwnd = cwnd + 3，重传 Duplicated ACKs 指定的数据包
        - 2.如果再收到 duplicated Acks：cwnd = cwnd + 1
        - 3.如果收到新的 ACK，而非 duplicated Ack，进入拥塞避免状态

- [ ] Linux rate halving 算法的快速恢复（已弃用）：

    - 1.sshthresh = cwnd / 2，cwnd不变
    - 2.每收到两个 ACK（不管是否重复）：cwnd = cwnd - 1
    - 3.新窗口值取 cwnd = MIN(cwnd, inflight+1)
        - inflight：发送了但还未收到的 Ack 的包
    - 4.直到退出快速恢复状态，cwnd = MIN(cwnd, ssthresh)

    - 优点：在快速恢复期间，取消窗口陡降过程，可以更平滑的发送数据
    - 缺点：降窗策略没有考虑 PIPE 的容量特征，考虑一下两点：
        - 如果快速恢复没有完成，窗口将持续下降下去
        - 如果一次性 ACK/SACK 了大量数据，in_flight 会陡然减少，窗口还是会陡降，这不符合算法预期。

- [ ] Linux 2.6版本Cubic 算法（已弃用）：

    ![image](./Pictures/net-kernel/TCP_congestion_cubic.avif)

    - CWND 的增长和 RTT 长短无关，即不是每次 ACK 后就去增大 CWND，而是让 CWND 增长的三次函数跟时间相关，不管 RTT 多大，一定时间后 CWND 一定增长到某个值，从而让网络更公平，RTT 小的连接不能挤占 RTT 大的连接的资源。

- [x] Linux最新的快速恢复算法PRR(Proportional Rate Reduction)：

    - 1.在快速恢复过程中，拥塞窗口非常平滑地向 ssthresh 收敛
    - 2.在快速恢复结束后，拥塞窗口处在 ssthresh 附近

- New Reno 算法：慢启动算法、拥塞避免算法、快速重传算法和 prr 算法

    ![image](./Pictures/net-kernel/TCP_congestion_newreno.avif)

- BDP(Bandwidth and Delay Product)：带宽 (单位 bps) 和延迟 (单位 s) 的乘积，单位是 bit

    ![image](./Pictures/net-kernel/TCP_congestion_bdp.avif)

- BBR:以时间窗口内的最大带宽 max_bw 和最小 RTT min_rtt，并以此计算发送速率和cwnd

    - [常见 TCP 拥塞避免算法浏览（下）](https://zhuanlan.zhihu.com/p/142835569)

- TCP Westwood 算法简称 TCPW：和 bbr 算法类似是基于带宽估计的一种拥塞控制算法。TCPW 采用和 Reno 相同的慢启动算法、拥塞避免算法。区别在于当检测到丢包时，根据带宽值来设置拥塞窗口、慢启动阈值。

```sh
# 查看拥塞算法（我这里为bbr）
sysctl net.ipv4.tcp_congestion_control
net.ipv4.tcp_congestion_control = bbr
```

- 同一网络下TCP对比UDP：

    ![image](./Pictures/net-kernel/TCP_vs_UDP.avif)

    - tcp每次进入拥塞后带宽会减少（图片上的tcp山峰）；而udp则不会，所以最后只剩下udp的带宽。

    - 在LAN（局域网）下不会有这类问题。但WAN则不同，因此需要设置`Qos`的规则控制udp带宽

### buffer（缓冲）

- socket buffer 也就是内核源码中常见的 skb 数据结构

- 内核为每条tcp分配buffer

- 如果sql查询的过大超过buffer会很慢，通过加大buffer可以减少查询时间

    - buffer 不是越大越好,过大的 buffer 容易影响拥塞控制算法对延迟的估测

```bash
# 值为1时：内核自动调整buffer（默认启用）
sysctl net.ipv4.tcp_moderate_rcvbu

# 发送端buffer。对应socket代码SO_RCVBUF（最好不要设置，让系统自动调整）
sysctl net.ipv4.tcp_rmem
net.ipv4.tcp_rmem = 4096 131072 6291456

# 接收端buffer。对应socket代码SO_SNDBUF（最好不要设置，让系统自动调整）
sysctl net.ipv4.tcp_wmem
net.ipv4.tcp_wmem = 4096 16384 4194304
```

| 列数                  | 内容                                           |
| --------------------- | ---------------------------------------------- |
| 最小包缓冲            | 用于系统内存紧张时保证最低限度的连接建立       |
| 默认包缓冲            | 此数值将会覆盖全局参数 `net.core.rmem_default` |
| 最大包缓冲            | 此数值 不覆盖 全局参数 `net.core.rmem_max`     |

`net.core.rmem` & `net.core.wmem` 为全局配置

### UDP

- header(头部)

    ![image](./Pictures/net-kernel/UDP_header.avif)

    - `source port` 和 `checksum` 是可选域（fields）

    - udp的header比tcp的header要小；因此单个段（segment）可以更大/

- udp不可靠，也无法重排段（segment）

### KCP

- [](https://cloud.tencent.com/developer/article/1148654)
## Network Layer（网络层）

- [traceroute and ttl](https://netbeez.net/blog/traceroute/)

## Data Link layer(数据链路层)

- [The Data Link layer of the OSI model](https://www.ictshore.com/free-ccna-course/data-link-layer/)

### 802.11 frame

- header

    ![image](./Pictures/net-kernel/802_11_Frame.avif)

## MTU

- [Troubleshooting MTU Issues](https://netbeez.net/blog/troubleshooting-mtu-issues/)

| Packet Size | Interface MTU | DF option (IP header) | Layer 2 interface (switched) | Layer 3 interface (routed) |
|-------------|---------------|-----------------------|------------------------------|----------------------------|
| <= 1500     | 1500          | 0 (unset)             | Pass                         | Pass                       |
| <= 1500     | 1500          | 1 (set)               | Pass                         | Pass                       |
| >= 1500     | 1500          | 0 (unset)             | Discard                      | Fragment                   |
| >= 1500     | 1500          | 1 (set)               | Discard                      | Discard and Notify         |

## 包的拆分与合并TSO、GSO、LRO、GRO

- 拆分

    ![image](./Pictures/net-kernel/TSO-GSO-off.avif)
    ![image](./Pictures/net-kernel/TSO.avif)
    ![image](./Pictures/net-kernel/GSO.avif)

- 合并

    ![image](./Pictures/net-kernel/LRO-GRO-off.avif)
    ![image](./Pictures/net-kernel/LRO.avif)
    ![image](./Pictures/net-kernel/GRO.avif)

```sh
# 查看是否开启
ethtool -k eth0

tcp-segmentation-offload: on # TSO
generic-segmentation-offload: on # GSO

large-receive-offload: on # LRO
generic-receive-offload: on # GRO
```

```sh
# 开启TSO
sudo ethtool -K eth0 tso on
```

# 内核网络协议栈

- TCP 相关配置在 `/proc/sys/net/ipv4/` ，但 Linux 的 TCP 协议栈不分 IPV4/IPV6，所有 ipv4.tcp 的设置将同时影响 V6 的 TCP 连接

## sysctl

- [sysctl-ArchWiki](https://wiki.archlinux.org/index.php/sysctl#Improving_performance)

- [linux sysctl net 字段 文档](https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt)
- [linux sysctl 每个字段文档](https://sysctl-explorer.net/)
- [linux net.netfilter 文档](https://www.kernel.org/doc/Documentation/networking/nf_conntrack-sysctl.txt)

sysctl 在运行时检查和更改内核参数的工具,在`procfs文件系统`(也就是`/proc`路径)中实现的

- 基本用法：

```sh
# 以下两条命令相同，重启后失效，如需持久化需配置 /etc/sysctl.conf
echo bar > /proc/sys/net/foo
sysctl -w net.foo=bar

# 写入/etc/sysctl.conf的配置，需要以下命令进行加载
sysctl --system

# 查看所有配置
sysctl --all
```

## /proc/net/softnet_stat

记录了一些内核网络栈的状态:

| 列数 | 内容                                                                                               |
| ---- | -------------------------------------------------------------------------------------------------- |
| 1    | processed 网络帧的计数                                                                             |
| 2    | dropped 计数也就是因 input_pkt_queue 不能处理导致的丢包数（和 ring buffer 满导致的丢包是两个问题） |
| 3    | NAPI 中由于 budget 或 time limit 用完而退出 net_rx_action 循环的次数                               |
| 8    | 没有意义因此全是 0                                                                                 |
| 9    | CPU 为了发送包而获取锁的时候有冲突的次数                                                           |
| 10   | CPU 被其他 CPU 唤醒来处理 backlog 数据的次数                                                       |
| 11   | 触发 flow_limit 限制的次数                                                                         |

```bash
cat /proc/net/softnet_stat                                                                         ─
00000f0f 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
000007f2 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
00000ffb 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
00006d1b 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
0000102f 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
00000777 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
0000be12 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
00006447 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
0000b33e 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
000083b6 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
0000bd5f 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
00008710 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
```

## 网络优化，有争议

```bash
# 回环接口的缓冲区大小
net.core.netdev_max_backlog = 16384

# 连接数上限
net.core.somaxconn = 8192

net.core.rmem_default = 1048576
net.core.rmem_max = 16777216
net.core.wmem_default = 1048576
net.core.wmem_max = 16777216
net.core.optmem_max = 65536
net.ipv4.tcp_rmem = 4096 1048576 2097152
net.ipv4.tcp_wmem = 4096 65536 16777216
net.ipv4.udp_rmem_min = 8192
net.ipv4.udp_wmem_min = 8192

# tcp-fast-open是tcp拓展，允许在tcp syn第一次握手期间建立连接,交换数据,减少握手的网络延迟
net.ipv4.tcp_fastopen = 3

# 最大传输单元（MTU）越长，性能越好，但可靠性越差。
net.ipv4.tcp_mtu_probing = 1
```

防止 ddos 攻击:

```bash
# tcp syn等待ack的最大队列长度
net.ipv4.tcp_max_syn_backlog = 8192

# TIME_WAIT状态下的最大套接字数
net.ipv4.tcp_max_tw_buckets = 2000000

# fin 秒数
net.ipv4.tcp_fin_timeout = 10

# 有助于抵御SYN flood攻击
net.ipv4.tcp_syncookies = 1

# 启用rp_filter(反向路径过滤)，内核将对所有接口收到的数据包进行源验证，可以防止攻击者使用IP欺骗
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.all.rp_filter = 1

# 禁止 icmp 重定向接受
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.all.secure_redirects = 0
net.ipv4.conf.default.secure_redirects = 0
net.ipv6.conf.all.accept_redirects = 0
net.ipv6.conf.default.accept_redirects = 0

# 在非路由上禁止 icmp 重定向发送
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.send_redirects = 0

# 忽略 icmp echo 请求
net.ipv4.icmp_echo_ignore_all = 1
net.ipv6.icmp.echo_ignore_all = 1
```

Tcp keepalive

```bash
# 设置为等待一分钟
net.ipv4.tcp_keepalive_time = 60
net.ipv4.tcp_keepalive_intvl = 10
net.ipv4.tcp_keepalive_probes = 6
```

关闭 tcp 慢启动:

- 因为 http1.1 采用多连接和域名分片,当一些连接闲置时,连接的网速会下降

- 以及 web 服务器的流量是间歇性

```bash
net.ipv4.tcp_slow_start_after_idle = 0
```

# reference

- [Linux 网络调优：内核网络栈参数篇(这篇文章非常好，可语文表达不太清晰)](https://www.starduster.me/2020/03/02/linux-network-tuning-kernel-parameter/#Linux_ingress)
