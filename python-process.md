# 进程, 线程, 异步I/O

## asyncio(异步I/O): 协程(Coroutines)

> 异步I/O不是多进程, 多线程. 是一种特殊的单线程, 通过中断机制,让线程给人一种并发的感觉

- 重I/O程序, I/O的延迟花费了大量的时间, 在此过程中cpu只能等待(阻塞), 也叫同步

    - cpu请求多个网站时, 发送第一个请求后: 需要等待响应, 才能请求下一个

- 而异步就是不等待I/O, 直接去执行其它任务, 直到I/O响应后, 再通知cpu回来处理(事件驱动)

    - cpu请求多个网站时, 发送第一个请求后: 暂停处理, 直接请求下一个, 第一个网站响应后再通知cpu回来处理

### 基本使用

- 异步的处理过程类似于生成器

- `async` 定义异步函数. 函数需要`asyncio.run()` 执行

- `await` 表示让cpu去执行其它任务. 必须在 `async` 定义的函数下使用

```py
async def test():
    await func()
```

- `@asyncio.coroutine` 装饰器, 代替async, await

```py
# 等同于上一个例子
@asyncio.coroutine
def test():
    yield from func()
```

# reference

- [Python并行编程 中文版](https://python-parallel-programmning-cookbook.readthedocs.io/zh_CN/latest/index.html)
