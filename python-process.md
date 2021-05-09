# 进程, 线程, 异步I/O

| 内存模型       | 概念                   | 数据一致性                                             |
|----------------|------------------------|--------------------------------------------------------|
| 共享内存模型   | 多处理器共享同一内存   | 数据只有一份, 通过锁, 信号量解决处理器之间的缓存一致性 |
| 分布式内存模型 | 每个处理器有独立的内存 | 数据需要分发到每个处理器的内存                         |

- 需要频繁通讯的任务: 应由同一个处理器处理

- [如何评估并行程序的性能](https://python-parallel-programmning-cookbook.readthedocs.io/zh_CN/latest/chapter1/06_How_to_evaluate_the_performance_of_a_parallel_program.html)

## Thread(线程)

- 包含: 程序计数器，寄存器和栈

- 和同一进程的其它线程共享资源: 文件描述符(句柄), 内存空间

- 状态: ready, running, blocked


- class:
    ```py
    class threading.Thread(group=None,
                           target=None,
                           name=None,
                           args=(),
                           kwargs={})
    ```
    | 参数   | 内容                                         |
    |--------|----------------------------------------------|
    | group  | 一般设置为 None ，这是为以后的一些特性预留的 |
    | target | 线程的执行函数                               |
    | name   | 线程名: 默认会分配一个唯一名字 Thread-N      |
    | args   | 函数参数: 类型为tuple                        |
    | kwargs | 函数参数: 类型为dict                         |

| 方法                                | 内容                       |
|-------------------------------------|----------------------------|
| threading.currentThread().getName() | 线程名                     |
| thread.get_ident()                  | 线程唯一标识符, 不是线程id |
| threading.get_native_id()           | 线程id                     |
| threading.current_thread()          | 返回当前线程对象           |
| threading.main_thread()             | 返回主线程对象             |
| threading.enumerate()               | 返回所有线程对象(list类型) |

- 基本使用

```py
import threading

# 定义函数, 输出参数, 线程名, 线程id
def func(s):
    print(s)
    print(threading.currentThread().getName())
    print(threading.currentThread().native_id)

# 线程绑定函数
t = threading.Thread(target=func, args=('hello tz',))

# 开启线程
t.start()

# 等待线程(阻塞主线程)
t.join()
```

- 继承`threading.Thread`类

```py
# 定义自己的线程类
class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for _ in range(10):
            print(self.getName())
            print(self.native_id)

t1 = myThread()
t2 = myThread()

t1.start()
t2.start()

t1.join()
t2.join()
```

### Lock(线程锁)

- 通过Lock, 让线程同步执行共享资源

- Lock有两种状态: `unlocked`, `locked`

| Lock的方法 | 操作                                                                          |
|------------|-------------------------------------------------------------------------------|
| acquire()  | 获取锁: 状态从unlocked -> locked. 如果状态是locked: 则等待另一个线程relaese() |
| release()  | 释放锁: 状态从locked -> unlocked. 如果状态是unlocked: 则RuntimError           |
| locked()   | 状态为locked时, 返回true                                                      |

- 没有锁

```py
import threading

def increment():
    global share
    for _ in range(count):
        share += 1

def decrement():
    global share
    for _ in range(count):
        share -= 1

if __name__ == '__main__':
    # 共享变量
    share = 0

    # 这个数要大
    count = 1000000

    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=decrement)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    #  查看是否为0. 多运行几次
    print(share)
```

- 有锁

```py
import threading

def increment():
    global lock
    global share
    for _ in range(count):
        # 获取锁
        lock.acquire()
        share += 1
        # 释放锁
        lock.release()

def decrement():
    global lock
    global share
    for _ in range(count):
        lock.acquire()
        share -= 1
        lock.release()

if __name__ == '__main__':
    share = 0
    count = 1000000

    # 定义锁
    lock = threading.Lock()

    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=decrement)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 查看是否为0
    print(share)
```

- 将上面例子的代码修改为:只获取,释放一次锁

源代码:

```py
for _ in range(count):
    # 获取锁
    lock.acquire()
    share += 1
    # 释放锁
    lock.release()
```

修改为:

``` py
# 获取锁
lock.acquire()
for _ in range(count):
    share += 1
# 释放锁
lock.release()
```

结果对比:

```
1.91秒
0.11秒
```

### RLock(Reentrant Lock)

> 递归锁: 同一线程可以多次 `acquire`,  `release`. 只有最后一次 `release` 状态才会变成 `unlocked`

```py
import threading
from time import time

def exec(i):
    global share
    # 递归获取锁
    lock.acquire()
    share += i
    # 递归获取锁
    lock.release()

def crement(func):
    global lock
    for _ in range(count):
        # 获取锁
        lock.acquire()
        eval(func)
        # 释放锁
        lock.release()

if __name__ == '__main__':
    share = 0
    count = 1000000

    # 定义锁
    lock = threading.RLock()

    # increment
    t1 = threading.Thread(target=crement, args=('exec(1)', ))
    # decrement
    t2 = threading.Thread(target=crement, args=('exec(-1)', ))

    start = time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time()

    # 查看是否为0
    print(share)
    # 执行时间
    print('%.2f秒' % (end - start))
```

- 执行时间
```
13.03秒
```

### semaphore(信号量)

| 信号量      | 操作                               |
|-------------|------------------------------------|
| acquire()   | 对信号量减一                       |
| release()   | 对信号量加一                       |
| 信号量为0时 | 就会阻塞acquire()                  |
| 死锁        | 线程1: 等待信号2; 线程2: 等待信号1 |

```py
import threading
import time
import random

def consumer():
        print("consumer is waiting.")
        # 信号量加1
        semaphore.acquire()
        print("Consumer notify : consumed item number %s " % item)

def producer():
        global item
        time.sleep(1)
        item = random.randint(0, 1000)
        print("producer notify : produced item number %s" % item)
        # 信号量减1
        semaphore.release()

if __name__ == '__main__':
    # 初始化信号量为0
    semaphore = threading.Semaphore(0)

    for _ in range (5):
            t1 = threading.Thread(target=producer)
            t2 = threading.Thread(target=consumer)
            t1.start()
            t2.start()
            t1.join()
            t2.join()
```
### Condition(条件)

| Condition | 操作       |
|-----------|------------|
| acquire() | 获取锁     |
| wait()    | 等待通知   |
| notify()  | 通知生产者 |
| release() | 释放锁     |

```py
from threading import Thread, Condition
import time

class consumer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for _ in range(10):
            global condition
            condition.acquire()
            # 当等于0, 消费者进入等待
            if len(item) == 0:
                condition.wait()
            item.pop()
            print("Consumer notify : item lengh %d\n" % (len(item)))
            condition.notify()
            condition.release()
            # 消费者等待的时间要比生产者长
            time.sleep(2)

class producer(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(10):
            global condition
            global item
            condition.acquire()
            # 当等于5, 生产者进入等待
            if len(item) == 5:
                condition.wait()
            item.append(1)
            print("Producer notify : item lengh %d" % (len(item)))
            condition.notify()
            condition.release()
            time.sleep(1)

if __name__ == '__main__':
    condition = Condition()
    item = []
    producer = producer()
    consumer = consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
```

- 3个线程, 按顺序打印ABC

```py
from threading import Thread, Condition

condition = Condition()
current = "A"


class ThreadA(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != "A":
                    condition.wait()
                print("A")
                current = "B"
                condition.notify_all()


class ThreadB(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != "B":
                    condition.wait()
                print("B")
                current = "C"
                condition.notify_all()


class ThreadC(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != "C":
                    condition.wait()
                print("C")
                current = "A"
                condition.notify_all()


if __name__ == '__main__':
    a = ThreadA()
    b = ThreadB()
    c = ThreadC()

    a.start()
    b.start()
    c.start()

    a.join()
    b.join()
    c.join()
```

### Event(事件)

| 事件    | 操作     |
|---------|----------|
| set()   | 发送信号 |
| clear() | 发送信号 |
| wait()  | 等待信号 |

```py
import time
from threading import Thread, Event

class consumer(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.event = event

    def run(self):
        for _ in range(5):
            # 等待信号
            self.event.wait()
            print('Consumer notify : get i number %d\n' % (i))

class producer(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.event = event

    def run(self):
        global i
        for i in range(5):
            print('Producer notify : event set i number %d' % (i))
            # 发送信号
            self.event.set()
            print('Producer notify : event cleared')
            # 阻塞
            self.event.clear()
            # 防止在发送i之前, 进入下一轮循环
            time.sleep(1)

if __name__ == '__main__':
    event = Event()
    t1 = producer(event)
    t2 = consumer(event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

### with

```py
import threading
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

def threading_with(statement):
    with statement:
        logging.debug('%s acquired via with' % statement)

def threading_not_with(statement):
    statement.acquire()
    try:
        logging.debug('%s acquired directly' % statement )
    finally:
        statement.release()

if __name__ == '__main__':
    # let's create a test battery
    lock = threading.Lock()
    rlock = threading.RLock()
    condition = threading.Condition()
    mutex = threading.Semaphore(1)
    threading_synchronization_list = [lock, rlock, condition, mutex]
    # in the for cycle we call the threading_with e threading_no_with function
    for statement in threading_synchronization_list :
       t1 = threading.Thread(target=threading_with, args=(statement,))
       t2 = threading.Thread(target=threading_not_with, args=(statement,))
       t1.start()
       t2.start()
       t1.join()
       t2.join()
```

### Queue

| Queue       | 操作                                      |
|-------------|-------------------------------------------|
| put()       | 往queue中放一个item                       |
| get()       | 从queue删除一个item，并返回删除的这个item |
| task_done() | 每次item被处理的时候需要调用这个方法      |
| join()      | 所有item都被处理之前一直阻塞              |

```py
from threading import Thread
from queue import Queue
import time

class consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Consumer notify: get item %d by %s\n' % (item, self.name))
            self.queue.task_done()

class producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(10):
            item = i
            self.queue.put(item)
            print('Producer notify: item number %d by %s' % (item, self.name))
            time.sleep(1)

if __name__ == '__main__':
    queue = Queue()
    t1 = producer(queue)
    t2 = consumer(queue)
    t3 = consumer(queue)
    t4 = consumer(queue)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
```

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
