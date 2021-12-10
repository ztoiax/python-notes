
<!-- vim-markdown-toc GFM -->

* [并发](#并发)
    * [Thread(线程)](#thread线程)
        * [Lock(线程锁)](#lock线程锁)
        * [RLock(Reentrant Lock)可重入锁](#rlockreentrant-lock可重入锁)
        * [semaphore(信号量)](#semaphore信号量)
        * [Condition(条件)](#condition条件)
        * [threading.Event(事件)](#threadingevent事件)
        * [测试每种锁使用with, 和不使用with](#测试每种锁使用with-和不使用with)
        * [Queue(线程队列)](#queue线程队列)
            * [使用Queue实现Pool(线程池)](#使用queue实现pool线程池)
        * [Barrier](#barrier)
        * [死锁](#死锁)
    * [Process(进程)](#process进程)
        * [共享变量](#共享变量)
        * [Queue(进程队列)](#queue进程队列)
        * [Pipe](#pipe)
        * [Barrier](#barrier-1)
        * [Pool(进程池)](#pool进程池)
        * [concurrent.futures进程, 线程池](#concurrentfutures进程-线程池)
    * [yiled 实现协程](#yiled-实现协程)
    * [asyncio(异步I/O): 协程(Coroutines)](#asyncio异步io-协程coroutines)
        * [基本使用](#基本使用)
        * [从调用function_1到function_3, 一共3次循环](#从调用function_1到function_3-一共3次循环)
        * [协程: 从调用function_1到function_3, 并返回值](#协程-从调用function_1到function_3-并返回值)
        * [asyncio.Task()](#asynciotask)
    * [gevent(异步)](#gevent异步)
        * [`gevent.select.select([], [], [], 2)`: 轮询](#geventselectselect---2-轮询)
        * [与普通的同步阻塞执行对比](#与普通的同步阻塞执行对比)
        * [`gevent.monkey`补丁修改标准库内阻塞的系统调用](#geventmonkey补丁修改标准库内阻塞的系统调用)
        * [gevent.pool.Pool()(gevent池), 能维持数据一致性](#geventpoolpoolgevent池-能维持数据一致性)
        * [gevent.Timeout()](#geventtimeout)
        * [gevent.event.Event(事件)](#geventeventevent事件)
        * [gevent.event.AsyncResult 是Event()的拓展, 允许唤醒后发送值](#geventeventasyncresult-是event的拓展-允许唤醒后发送值)
        * [gevent.queue.Queue(队列)](#geventqueuequeue队列)
            * [gevent与进程通信](#gevent与进程通信)
    * [分布式](#分布式)
        * [Celery](#celery)
        * [Scoop](#scoop)
* [reference](#reference)

<!-- vim-markdown-toc -->
# 并发

- 进程的开销:需要复制内存, 创建进程需要系统调用

    - copy on write(写时复制)技术: 子进程修改时, 再进行内存复制, 减少开销

- 线程的开销:相比于进程不需要复制内存, 但创建线程仍然需要系统调用, 以及分配内存

- 从开销的角度来看, 操作系统所提供的进程和线程并不理想

- 因此一些编程语言有独特的并发控制技术

    - Erlang的"进程":

        - 比操作系统的进程, 线程更轻量

        - 在用户空间创建, 没有系统调用

        - 这个"进程"概念类似于Actor模型的Actor

    - Go的goroutine:

        - 类似于Erlang的进程 [Quora: How are Erlang processes different from Golang goroutines?](https://www.quora.com/How-are-Erlang-processes-different-from-Golang-goroutines)

    - Clojure的STM(Software Transactional Memory)软件事务内存:

        - 类似于关系性数据库的acid事务概念. [Clojure STM - What? Why? How?](https://sw1nn.com/blog/2012/04/11/clojure-stm-what-why-how/)

- 内存模型

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

| 方法                                       | 内容                                     |
| ------------------------------------------ | ----------------------------             |
| threading.currentThread().getName()        | 线程名                                   |
| threading.currentThread().get_ident()      | 线程唯一标识符, 不是线程id               |
| threading.currentThread().get_native_id()  | 线程id                                   |
| threading.currentThread().get_native_id()  | 线程id                                   |
| threading.currentThread().is_alive()       | 是否在运行                               |
| threading.currentThread().isDaemon()       | 是否是守护进程                           |
| threading.current_thread()                 | 返回当前线程对象                         |
| threading.main_thread()                    | 返回主线程对象                           |
| threading.enumerate()                      | 返回所有alive为Trued的线程对象(list类型) |

| 线程方法 | 操作                                                     |
|----------|----------------------------------------------------------|
| start()  | 启动线程, 设置alive为True. 多次启动会异常:RuntimeError   |
| run()    | 启动线程, 设置alive为True. 多次启动会异常:AttributeError |
| join()   | 主线程等待(阻塞)线程结束(alive为False)                   |
| local()  | 只保存当前运行线程的状态, 对其它线程不可见(原理是维护一个字典)                   |

- 基本使用

```py
import threading

# 定义函数, 输出参数, 线程名, 线程id
def func(s):
    print(s)
    print(threading.currentThread().getName())
    print(threading.currentThread().native_id)
    print(f'Daemon: {threading.currentThread().isDaemon()}')
    print(f'alive: {threading.currentThread().is_alive()}')

# 线程绑定函数
t = threading.Thread(target=func, args=('hello tz',))

# 如果需要以守护进程运行则
t.daemon = True

# 开启线程
t.start()

# 等待线程(阻塞主线程)
t.join()
```

- 子类使用进程

```py
import threading
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

- 为了防止出现Lock死锁, 最好设置为每个线程一次只允许获取一个锁

    - 或者使用更高级的锁同步机制 **`RLock(可重入锁)`** 和 **`Semaphore(信号量)`**

- 没有锁:

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

    # 结果不等于0, 并且每次运行的结果都不一样
    print(share)
```

- Lock锁:

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

    # 设置Lock后, 结果为0
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

    性能对比:

    ```
    1.91秒
    0.11秒
    ```

- 使用with语句, 可以防止忘记lock.release()

    ```py
    lock = threading.Lock()
    with lock:
        pass
    ```

### RLock(Reentrant Lock)可重入锁

- 同一线程可以多次 `acquire`,  `release`. 只有最后一次 `release` 状态才会变成 `unlocked`

    - 但一次只有一个线程可以执行

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
| acquire()   | 对信号量减一. 信号量不为1时会执行  |
| release()   | 对信号量加一. 信号量为0时会阻塞    |
| 死锁        | 线程1: 等待信号2; 线程2: 等待信号1 |

- 信号量增加了复杂性, 会影响程序性能, 只适合需要在线程之间引入信号或者限制的程序

```py
import threading
import time
import random

def consumer():
        print("consumer is waiting.")
        # 信号量减1
        semaphore.acquire()
        print("Consumer notify : consumed item number %s " % item)

def producer():
        global item
        time.sleep(1)
        item = random.randint(0, 1000)
        print("producer notify : produced item number %s" % item)
        # 信号量加1
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

| Condition    | 操作                         |
|--------------|------------------------------|
| acquire()    | 获取锁                       |
| release()    | 释放锁                       |
| wait()       | 等待通知                     |
| notify()     | 通知线程(生产者和消费者)     |
| notify_all() | 通知所有线程(生产者和消费者) |

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

- 一个时间间隔器的线程, 每隔一段时间就通知两个消费者线程

```py
import threading
import time

class Timer(threading.Thread):
    def __init__(self, interval):
        self._interval = interval
        threading.Thread.__init__(self)

    def run(self):
        while True:
            # sleep
            time.sleep(self._interval)
            # notify_all通知所有生产者
            with condition:
                condition.notify_all()


def wait_for_tick(condition):
    with condition:
        condition.wait()

# 设置两个消费者
def countdown(n):
    for i in range(n, 0, -1):
        wait_for_tick(condition)
        print('down:', i)

def countup(n):
    for i in range(n):
        wait_for_tick(condition)
        print('up:', i)


if __name__ == '__main__':
    condition = threading.Condition()

    threading.Thread(target=countdown, args=(10,)).start()
    threading.Thread(target=countup, args=(5,)).start()

    # 每隔1秒通知所有消费者
    timer = Timer(1)
    timer.run()
```

### threading.Event(事件)

| 事件    | 操作           |
|---------|----------------|
| set()   | 将信号设置为真 |
| clear() | 将信号设置为假 |
| wait()  | 等待信号       |

- 1.初始的event 对象中的信号被设置为假

- 2.消费者线程等待(阻塞) event 对象，直至信号为真

- 3.生产者线程将 event 对象的信号设置为真后，会唤醒所有等待这个 event 对象的消费者线程

- event对象的一个重要特点是可以唤醒所有等待它的线程

    - 如果只想唤醒单个线程，最好是使用**信号量**或者 **Condition** 对象来替代

- 将conditon的时间间隔器例子改为event
```py
import threading
import time

class Timer(threading.Thread):
    def __init__(self, interval):
        self._interval = interval
        threading.Thread.__init__(self)

    def run(self):
        while True:
            # sleep
            time.sleep(self._interval)
            # 改为set()和clear()
            event.set()
            event.clear()


# 设置两个消费者
def countdown(n):
    for i in range(n, 0, -1):
        # 改为wait()
        event.wait()
        print('down:', i)

def countup(n):
    for i in range(n):
        event.wait()
        print('up:', i)


if __name__ == '__main__':
    event = threading.Event()

    threading.Thread(target=countdown, args=(10,)).start()
    threading.Thread(target=countup, args=(5,)).start()

    # 每隔1秒通知所有消费者
    timer = Timer(1)
    timer.run()
```

### 测试每种锁使用with, 和不使用with

```py
import threading
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

# 使用with语句获取释放锁
def threading_with(lock):
    with lock:
        logging.debug('%s acquired via with' % lock)

# 不使用with语句获取释放锁
def threading_not_with(lock):
    lock.acquire()
    try:
        logging.debug('%s acquired not with' % lock)
    finally:
        lock.release()

if __name__ == '__main__':
    # 测试所有锁机制
    lock_thread = threading.Lock()
    rlock = threading.RLock()
    condition = threading.Condition()
    mutex = threading.Semaphore(1)

    # 把锁放入列表, 逐个测试
    locks = [lock_thread, rlock, condition, mutex]

    # 测试每种锁的with和no_with
    for lock in locks:
       t1 = threading.Thread(target=threading_with, args=(lock,))
       t2 = threading.Thread(target=threading_not_with, args=(lock,))
       t1.start()
       t2.start()
       t1.join()
       t2.join()
       print('\n')
```

### Queue(线程队列)

| Queue       | 操作                                                                  |
|-------------|-----------------------------------------------------------------------|
| put()       | 往queue中放一个item                                                   |
| get()       | 从queue删除一个item，并返回删除的这个item. 可设置时间get(timeout=5.0) |
| task_done() | 每次item被处理的时候需要调用这个方法                                  |
| join()      | 所有item都被处理之前一直阻塞                                          |
| qsize()     | 队列长度                                                              |
| full()      | 队列是否满了                                                          |
| empty()     | 队列是否为空                                                          |

- Queue 对象已经包含了必要的锁

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

- 协调生产者和消费者的退出问题: 生产者在队列中put一个特殊的值，当消费者get到后，就退出

    - 这样的退出方法, 只能有一个消费者, 而且是生产者对消费者的单向退出

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

            # 当get到哨兵就退出
            if item == _sentinel:
                break

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

        # put哨兵, 让消费者退出
        self.queue.put(_sentinel)

if __name__ == '__main__':
    queue = Queue()
    # 设置哨兵值
    _sentinel = object()

    # 这样的退出方法, 只能有一个消费者
    t1 = producer(queue)
    t2 = consumer(queue)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

#### 使用Queue实现Pool(线程池)

- 计算0到100的平方, 并加入到list里

```py
import threading
from queue import Queue
from queue import Empty

def function_square(data):
    global inputs
    inputs.append(data*data)

def pool_thread(q):
    try:
        while True:
            # 接受queue
            elem = q.get_nowait()
            # 计算
            function_square(elem)
    except Empty:
        pass

if __name__ == '__main__':
    inputs = []
    q = Queue()
    threads = []
    for i in range(100):
        # 发送queue
        q.put(i)

    # 4个线程的线程池
    for i in range(4):
        thr = threading.Thread(target=pool_thread, args=(q,))
        thr.start()
        threads.append(thr)

    for i in threads:
        i.join

    print ('Pool    :', inputs)
```

### Barrier

> 多个线程同时执行

```py
import threading
from threading import Barrier, Lock, Thread
from time import time
from datetime import datetime

def test_with_barrier(barrier, lock):
    name = threading.currentThread().getName()
    # 等待两个进程同时wait, 再执行
    barrier.wait()
    with lock:
        print("process %s ----> %s" % (name, datetime.fromtimestamp(time())))

def test_without_barrier():
    name = threading.currentThread().getName()
    print("process %s ----> %s" % (name, datetime.fromtimestamp(time())))

if __name__ == '__main__':
    # 初始化Barrier, 参数2代表两个进程
    barrier = Barrier(2)
    # 初始化锁
    lock = Lock()
    p1=Thread(name='p1 - test_with_barrier', target=test_with_barrier, args=(barrier,lock))
    p2=Thread(name='p2 - test_with_barrier', target=test_with_barrier, args=(barrier,lock))
    p3=Thread(name='p3 - test_without_barrier', target=test_without_barrier)
    p4=Thread(name='p4 - test_without_barrier', target=test_without_barrier)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
```

### 死锁

- 死锁很大一部分是由于线程同时获取多个锁造成的

    - 尽可能保证每一个线程只能同时保持一个锁

看门狗计数器。当线程正常 运行的时候会每隔一段时间重置计数器，在没有发生死锁的情况下，一切都正常进行。一旦发生死锁，由于无法重置计数器导致定时器 超时，这时程序会通过重启自身恢复到正常状态。

- 一种解决方案:为程序中的每一个锁分配一个唯一的id，然后只允许按照升序规则来使用多个锁(可以使用contextmanager实现)

```py
import threading
from contextlib import contextmanager

# @contextmanager实现with语句
@contextmanager
def acquire(*locks):
    # 对锁进行排序. 即使用户以不同顺序获取锁, 最后也可以按顺序获取锁
    locks = sorted(locks, key=lambda x: id(x))

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        for lock in reversed(locks):
            lock.release()


def thread_1():
    with acquire(x_lock, y_lock):
        for _ in range(5):
            print('Thread-1')

def thread_2():
    with acquire(y_lock, x_lock):
        for _ in range(5):
            print('Thread-2')


if __name__ == '__main__':
    # 设置两个Lock
    x_lock = threading.Lock()
    y_lock = threading.Lock()

    t1 = threading.Thread(target=thread_1)
    t2 = threading.Thread(target=thread_2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

## Process(进程)

> 曾经是每个进程一个解释器和GIL, 因此多线程会有GIL的限制, 人们往往就用多进程而不是多线程. 但现如今每个进程内部有多个解释器和GIL, 解决了多线程并发的问题

- 把线程方法,改为进程方法:

    - `threading` -> `multiprocessing`

    - `threading.Thread` -> `multiprocessing.Process`

```py
import multiprocessing
import threading

def func(s):
    print(s)
    print(threading.currentThread().getName())
    # pid
    print(threading.currentThread().native_id)
    print(f'Daemon: {threading.currentThread().isDaemon()}')
    print(f'alive: {threading.currentThread().is_alive()}')

p = multiprocessing.Process(target=func, args=('hello tz',))

p.start()
p.join()
```

| 方法                                    | 操作     |
|-----------------------------------------|----------|
| multiprocessing.current_process().name  | 进程名   |
| multiprocessing.current_process().pid   | pid      |
| multiprocessing.current_process().ident | pid,同上 |
| terminate()                             | 终止进程 |

- 三者相同都是pid:
    - `multiprocessing.current_process().pid`
    - `multiprocessing.current_process().ident`
    - `threading.currentThread().native_id`

```py
import multiprocessing

def func(s):
    print(s)
    print(multiprocessing.current_process().name)
    print(multiprocessing.current_process().pid)
    print(f'alive: {multiprocessing.current_process().is_alive()}')

p = multiprocessing.Process(target=func, args=('hello tz',))

p.start()
p.join()
```

- 子类使用进程

```py
import multiprocessing
class myProcess(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):
        for _ in range(10):
            print(self.name)
            print(self.pid)

t1 = myProcess()
t2 = myProcess()

t1.start()
t2.start()

t1.join()
t2.join()
```

### 共享变量

- 线程共享变量: 线程之间使用同一内存空间, 可以直接使用

```py
import threading

def worker(dictionary, key, item):
   dictionary[key] = item
   print("key = %d value = %d" % (key, item))

if __name__ == '__main__':
    dictionary = dict()
    jobs = [threading.Thread(target=worker, args=(dictionary, i, i*2)) for i in range(10)]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print('Results:', dictionary)
```

- 进程共享变量: 因为进程之间相互独立, 需要使用`Manager()`进行管理

```py
import multiprocessing

def worker(dictionary, key, item):
   dictionary[key] = item
   print("key = %d value = %d" % (key, item))

if __name__ == '__main__':
    # 初始化内存管理器
    mgr = multiprocessing.Manager()
    # 初始化共享变量
    dictionary = mgr.dict()

    jobs = [multiprocessing.Process(target=worker, args=(dictionary, i, i*2)) for i in range(10)]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print('Results:', dictionary)
```

- 线程, 进程性能对比

> 线程比进程快2倍多

```
# 线程
0.000921726227秒

# 进程
0.025198221207秒
```

### Queue(进程队列)

- 相比于线程`from queue import Queue` -> `from multiprocessing import Queue`

    - 进程没有 `queue.task_done()`

- `self.queue.empty()`: 消费者查看queue是否为空

```py
from multiprocessing import Process, Queue
import time

class consumer(Process):
    def __init__(self, queue):
        Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Consumer notify: get item %d by %s\n' % (item, self.name))

class producer(Process):
    def __init__(self, queue):
        Process.__init__(self)
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

### Pipe

| 方法    | 操作 |
|---------|------|
| send()  | 发送 |
| recv()  | 结束 |
| close() | 关闭 |

```py
import multiprocessing

def create_items(pipe):
    output_pipe, _ = pipe
    for item in range(10):
        # 发送pipe1
        output_pipe.send(item)
    output_pipe.close()

def multiply_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            # 接受pipe1
            item = input_pipe.recv()
            # 发送pipe2
            output_pipe.send(item * item)
    except EOFError:
        output_pipe.close()

if __name__== '__main__':
    # 第一个进程管道发出数字
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(target=create_items, args=(pipe_1,))
    process_pipe_1.start()

    # 第二个进程管道接收数字并计算
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(target=multiply_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()
    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            # 接受pipe2
            print(pipe_2[1].recv())
    except EOFError:
        print("End")
```

### Barrier

> 多个进程同时执行

```py
import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def test_with_barrier(barrier, lock):
    name = multiprocessing.current_process().name
    # 等待两个进程同时wait, 再执行
    barrier.wait()
    with lock:
        print("process %s ----> %s" % (name, datetime.fromtimestamp(time())))

def test_without_barrier():
    name = multiprocessing.current_process().name
    print("process %s ----> %s" % (name, datetime.fromtimestamp(time())))

if __name__ == '__main__':
    # 初始化Barrier, 参数2代表两个进程
    barrier = Barrier(2)
    # 初始化锁
    lock = Lock()
    Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(barrier,lock)).start()
    Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(barrier,lock)).start()
    Process(name='p3 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier', target=test_without_barrier).start()
```
- 线程, 进程性能对比

> 线程比进程快14倍

```
# 线程
0.000603914261秒

# 进程
0.008400917053秒
```

### Pool(进程池)

- 进程之间会竞争

- `pool.map()`

```py
import multiprocessing

def function_square(data):
    result = data*data
    return result

if __name__ == '__main__':
    inputs = list(range(100))
    # 初始化4个进程的进程池
    pool = multiprocessing.Pool(processes=4)
    # map()将任务交给进程池执行. 进程之间会竞争
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()
    print ('Pool    :', pool_outputs)
```

- `pool.imap_unordered` 返回生成器

```py
import multiprocessing

def function_square(data):
    result = data*data
    return result

if __name__ == '__main__':
    inputs = list(range(100))
    # 初始化4个进程的进程池
    pool = multiprocessing.Pool(processes=4)
    # pool.imap_unordered()返回生成器
    pool_outputs = pool.imap_unordered(function_square, inputs)
    pool.close()
    pool.join()

    # 打印值
    for i in pool_outputs:
        print(i)
```

- 线程, 进程性能对比

> 线程比进程快16倍

```
# 线程
0.000762224197秒

# 进程
0.012202501297秒
```

### concurrent.futures进程, 线程池

- requests.get url例子
```py
from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_url(url):
    u = requests.get(url)
    return u.content

pool = ThreadPoolExecutor(10)
a = pool.submit(fetch_url, 'http://www.baidu.com')
b = pool.submit(fetch_url, 'http://www.sogou.com')

# result()阻塞进程直到函数返回
print(len(a.result()))
print(len(b.result()))
```


```py
import concurrent.futures
import time

def evaluate_item(x):
        # 计算总和，这里只是为了消耗时间
        result_item = count(x)
        # 打印输入和输出结果
        return result_item

def  count(number) :
        for i in range(0, 10000000):
                i += 1
        return i * number

if __name__ == "__main__":
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # 顺序执行
        start_time = time.time()
        for item in number_list:
                print(evaluate_item(item))
        print("Sequential execution in " + str(time.time() - start_time), "seconds")

        # 线程池执行
        start_time_1 = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                futures = [executor.submit(evaluate_item, item) for item in number_list]
                for future in concurrent.futures.as_completed(futures):
                        print(future.result())
        print ("Thread pool execution in " + str(time.time() - start_time_1), "seconds")

        # 进程池. 不受GIL的限制
        start_time_2 = time.time()
        with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
                # submit()定义进程
                futures = [executor.submit(evaluate_item, item) for item in number_list]
                # as_completed()生成器, 主线程等待线程结束.类似yield
                for future in concurrent.futures.as_completed(futures):
                        # result()执行, 并返回
                        print(future.result())
        print ("Process pool execution in " + str(time.time() - start_time_2), "seconds")
```

## yiled 实现协程

```py
def countdown(n):
    for i in range(n, 0, -1):
        print('down:', i)
        yield

def countup(n):
    for i in range(n):
        print('up:', i)
        yield


from collections import deque

class TaskScheduler:
    def __init__(self):
        # 双向链表
        self._task_queue = deque()

    def new_task(self, task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                # Run until the next yield statement
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                # Generator is no longer executing
                pass

if __name__ == '__main__':
    sched = TaskScheduler()
    sched.new_task(countdown(10))
    sched.new_task(countup(5))
    sched.run()
```

## asyncio(异步I/O): 协程(Coroutines)

> 异步I/O不是多进程, 多线程. 是一种特殊的单线程, 通过中断机制,让线程给人一种并发的感觉

- 重I/O程序, I/O的延迟花费了大量的时间, 在此过程中cpu只能等待(阻塞), 也叫同步

    - cpu请求多个网站时, 发送第一个请求后: 需要等待响应, 才能请求下一个

- 而异步就是不等待I/O, 直接去执行其它任务, 直到I/O响应后, 再通知cpu回来处理(事件驱动)

    - cpu请求多个网站时, 发送第一个请求后: 暂停处理, 直接请求下一个, 第一个网站响应后再通知cpu回来处理

### 基本使用

- 异步的处理过程类似于生成器`yield`

- `async` 定义异步函数. 函数需要`asyncio.run()` 执行

- `await` 表示让cpu去执行其它任务. 必须在 `async` 定义的函数下使用

```py
async def test():
    await func()
```

- `@asyncio.coroutine` 装饰器代替async; `yiled from`代替await.**在python3.8已被弃用**

```py
# 等同于上一个例子
@asyncio.coroutine
def test():
    yield from func()
```

### 从调用function_1到function_3, 一共3次循环

- 非异步:

```py
import time

def function_1():
    print ("function_1 called")
    if time.time() < end_time:
        time.sleep(1)
        function_2()
    else:
        exit(0)

def function_2():
    print ("function_2 called ")
    if time.time() < end_time:
        time.sleep(1)
        function_3()
    else:
        exit(0)

def function_3():
    print ("function_3 called")
    if time.time() < end_time:
        time.sleep(1)
        function_1()
    else:
        exit(0)

if __name__ == '__main__':
    end_time = time.time() + 9.0
    time.sleep(1)
    function_1()
```

- 异步. asyncio.get_event_loop()实现事件循环:

```py
import asyncio

def function_1(end_time, loop):
    print ("function_1 called")
    if (loop.time() + 1.0) < end_time:
        # 1秒后调用function_2
        loop.call_later(1, function_2, end_time, loop)
    else:
        loop.stop()

def function_2(end_time, loop):
    print ("function_2 called ")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_3, end_time, loop)
    else:
        loop.stop()

def function_3(end_time, loop):
    print ("function_3 called")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_1, end_time, loop)
    else:
        loop.stop()

if __name__ == '__main__':
    # 事件循环
    loop = asyncio.get_event_loop()
    # function最长运行时间9秒, 3循环
    end_loop = loop.time() + 9.0
    # 调用function_1
    loop.call_soon(function_1, end_loop, loop)
    # 超时就停止
    loop.run_forever()
    loop.close()
```

### 协程: 从调用function_1到function_3, 并返回值

```py
import asyncio

async def function_1():
    await asyncio.sleep(1)
    print ("function_1 called")
    # 调用function_2, 并返回值
    result = await function_2()
    print(result)
    return("function_1 finish")

async def function_2():
    await asyncio.sleep(1)
    print ("function_2 called")
    result = await function_3()
    print(result)
    return("function_2 finish")

async def function_3():
    await asyncio.sleep(1)
    print ("function_3 called")
    return("function_3 finish")

if __name__ == '__main__':
    # asyncio.run()调用function_1, 并返回值
    result = asyncio.run(function_1())
    print(result)
```

- 上面例子, 改为使用事件循环

```py
if __name__ == '__main__':
    # 定义事件循环
    loop = asyncio.get_event_loop()
    # 调用function_1, 并返回值
    result = loop.run_until_complete(function_1())
    print(result)
```

### asyncio.Task()

```py
import asyncio

async def function_1():
    for i in range(3):
        print("function_1(%s)" % (i))
        await asyncio.sleep(1)

async def function_2():
    for i in range(3):
        print("function_2(%s)" % (i))
        await asyncio.sleep(1)

async def function_3():
    for i in range(3):
        print("function_3(%s)" % (i))
        await asyncio.sleep(1)

if __name__ == "__main__":
    # 定义asyncio.Task列表
    tasks = [asyncio.Task(function_1()),
             asyncio.Task(function_2()),
             asyncio.Task(function_3())]
    loop = asyncio.get_event_loop()
    # 调用task
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
```

## gevent(异步)

- [优秀文档](https://sdiehl.github.io/gevent-tutorial/)

- 并发的核心思想是:一个较大的任务分解成一组子任务,这些子任务异步运行,而不是一个一个的同步运行,两个子任务之间的切换称为上下文切换

| 方法                                | 操作                      |
|-------------------------------------|---------------------------|
| gevent.spawn()                      | 使用gevent执行函数        |
| gevent.joinall()                    | 等待spawn执行的函数结束   |
| gevent.sleep(0)                     | 切换上下文, 由`yield`实现 |
| gevent.select.select([], [], [], 2) | poll(轮询) 2秒            |
| gevent.pool.Pool()                  | 池(不会出现竞争问题)      |

```py
import gevent

def foo():
    print('Running in foo')
    # 异步总时间为1秒
    gevent.sleep(1)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')

# 等待spawn执行的函数结束
gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
```

### `gevent.select.select([], [], [], 2)`: 轮询

```py
import time
import gevent
from gevent import select

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

def gr1():
    print('Started Polling: %s' % tic())
    # poll 2秒
    select.select([], [], [], 2)
    print('Ended Polling: %s' % tic())

def gr2():
    print('Started Polling: %s' % tic())
    select.select([], [], [], 2)
    print('Ended Polling: %s' % tic())

def gr3():
    print("Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)

gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
])
```

### 与普通的同步阻塞执行对比

```py
import gevent

def task(pid):
    # 同步: 每次执行等待时间为0.5秒; 异步: 总时间为0.5秒
    gevent.sleep(0.5)
    print('Task %s done' % pid)

# 同步
def synchronous():
    for i in range(1,10):
        task(i)

# 异步
def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
```

### `gevent.monkey`补丁修改标准库内阻塞的系统调用

| 补丁                  | 补丁类型               |
|-----------------------|------------------------|
| monkey.patch_all()    | 所有系统调用都打上补丁 |
| monkey.patch_socket() | socket补丁             |
| monkey.patch_select() | select补丁             |

```py
import socket
print(socket.socket)

print("After monkey patch")
from gevent import monkey
# patch socket()
monkey.patch_socket()
print(socket.socket)

import select
print(select.select)
# patch select()
monkey.patch_select()
print("After monkey patch")
print(select.select)
```

- `gevent.monkey.patch_socket()` 修改 socket库

- 补丁最好放在最前面

```py
# 打上修改socket的补丁
from gevent import monkey; monkey.patch_socket()

import gevent
import requests

def task(pid):
    r = requests.get('http://www.baidu.com')
    print(f'Process {pid}: {r.status_code}')

def synchronous():
    for i in range(1, 10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(1, 10)]
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
```

### gevent.pool.Pool()(gevent池), 能维持数据一致性

- 与进程Pool对比

```py
from time import time, sleep

def echo(i):
    sleep(0.001)
    return i

# Non Deterministic Process Pool

start = time()
from multiprocessing.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(echo, range(10))]
run2 = [a for a in p.imap_unordered(echo, range(10))]
run3 = [a for a in p.imap_unordered(echo, range(10))]
run4 = [a for a in p.imap_unordered(echo, range(10))]
# 进程之间会竞争, 所以结果不会相同
print(run1 == run2 == run3 == run4)

end = time()
print('%.12f秒' % (end - start))

# Deterministic Gevent Pool

start = time()
from gevent.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(echo, range(10))]
run2 = [a for a in p.imap_unordered(echo, range(10))]
run3 = [a for a in p.imap_unordered(echo, range(10))]
run4 = [a for a in p.imap_unordered(echo, range(10))]
print(run1 == run2 == run3 == run4)

end = time()
print('%.12f秒' % (end - start))
```

- 输出结果

    - 虽然进程池存在一致性问题, 但速度比gevent快20倍

```
False
0.027213811874秒
True
0.066201686859秒
```

### gevent.Timeout()

- 4种timeout的方法

```py
import gevent
from gevent import Timeout

def wait():
    gevent.sleep(2)

# Thread 0

timeout = Timeout(1)
timeout.start()

try:
    gevent.spawn(wait).join()
except Timeout:
    print('Thread 0 timed out')

# Thread 1

timer = Timeout(1).start()
thread1 = gevent.spawn(wait)

try:
    thread1.join(timeout=timer)
except Timeout:
    print('Thread 1 timed out')

# Thread 2

timer = Timeout.start_new(1)
thread2 = gevent.spawn(wait)

try:
    thread2.get(timeout=timer)
except Timeout:
    print('Thread 2 timed out')

# Thread 3

try:
    gevent.with_timeout(1, wait)
except Timeout:
    print('Thread 3 timed out')
```

### gevent.event.Event(事件)

```py
import gevent
from gevent.event import Event

def setter():
    '''After 2 seconds, wake all threads waiting on the value of event'''
    print('A: Hey wait for me, I have to do something')
    gevent.sleep(2)
    print("Ok, I'm done")
    # 发送event
    event.set()

def waiter():
    '''After 2 seconds the get call will unblock'''
    print("I'll wait for you")
    # blocking
    event.wait()
    print("It's about time")

if __name__ == '__main__':
    # 初始化事件
    event = Event()

    gevent.joinall([
        gevent.spawn(setter),

        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter)
    ])
```
### gevent.event.AsyncResult 是Event()的拓展, 允许唤醒后发送值

```py
import gevent
from gevent.event import Event

def setter():
    '''After 2 seconds, wake all threads waiting on the value of event'''
    print('A: Hey wait for me, I have to do something')
    gevent.sleep(2)
    print("Ok, I'm done")

    # 发送event值
    event.set("It's about time")

def waiter():
    '''After 2 seconds the get call will unblock'''
    print("I'll wait for you")

    # blocking
    event.wait()

    # 获取值
    print(event.get())

if __name__ == '__main__':
    # 初始化AsyncResult
    from gevent.event import AsyncResult
    event = AsyncResult()

    gevent.joinall([
        gevent.spawn(setter),

        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter)
    ])
```

### gevent.queue.Queue(队列)

| Queue方法    | 操作        |
|--------------|-------------|
| get()        | 阻塞版get   |
| put()        | 阻塞版put   |
| get_nowait() | 非阻塞版get |
| put_nowait() | 非阻塞版put |

- 非阻塞版get, put

```py
import gevent
from gevent.queue import Queue

def consumer(n):
    # 循环队列
    while not queue.empty():
        # 获取队列值, 队列长度减1
        task = queue.get_nowait()
        print('%s got %s' % (n, task))
        gevent.sleep(0)

    print('%s Quit!' % (n))

def producer():
    for i in range(10):
        # 发送队列值
        queue.put_nowait(i)

if __name__ == '__main__':
    # 初始化Queue
    queue = Queue()

    gevent.joinall([
        gevent.spawn(producer),

        gevent.spawn(consumer, 'function_1'),
        gevent.spawn(consumer, 'function_2'),
        gevent.spawn(consumer, 'function_3'),
    ])
```

- 阻塞版get, put

```py
import gevent
from gevent.queue import Queue, Empty

def consumer(n):
    # 循环队列
    try:
        while True:
            # decrements queue size by 1
            task = queue.get(timeout=1)
            print('%s got %s' % (n, task))
            gevent.sleep(0)
    except Empty:
        print('%s Quit!' % (n))

def producer():
    for i in range(10):
        # 发送队列值
        queue.put(i)
    print('Assigned all work in iteration 1')

    for i in range(10, 20):
        # 第二条队列
        queue.put(i)
    print('Assigned all work in iteration 2')

if __name__ == '__main__':
    # 现在长度
    queue = Queue(maxsize=3)

    gevent.joinall([
        gevent.spawn(producer),

        gevent.spawn(consumer, 'function_1'),
        gevent.spawn(consumer, 'function_2'),
        gevent.spawn(consumer, 'function_3'),
    ])
```

#### gevent与进程通信

```py
import gevent
from multiprocessing import Process, Pipe
from gevent.socket import wait_read, wait_write

# To Process
a, b = Pipe()

# From Process
c, d = Pipe()

def relay():
    for i in range(10):
        msg = b.recv()
        # 发送给d
        c.send(msg + " in " + str(i))

def put_msg():
    for _ in range(10):
        wait_write(a.fileno())
        # 发送给b
        a.send('hi')

def get_msg():
    for _ in range(10):
        wait_read(d.fileno())
        print(d.recv())

if __name__ == '__main__':
    proc = Process(target=relay)
    proc.start()

    g1 = gevent.spawn(get_msg)
    g2 = gevent.spawn(put_msg)
    gevent.joinall([g1, g2], timeout=1)
```

## 分布式

### Celery

> Celery是任务分发器负责发送消息, 需要安装并启动`RabbitMQ`消息队列

- 文件: addTask.py

```py
from celery import Celery
# module名字: addTask. 连接代理的 broker(RabbitMQ)
app = Celery('addTask', broker='amqp://guest:@localhost:5672//')
# 定义任务
@app.task
def add(x, y):
    return x + y
```

- 文件: addTask_main.py
```py
import addTask
if __name__ == '__main__':
    # 调用add
    result = test.add.delay(5,5)
```

```sh
# 启动addTask
celery -A addTask worker --loglevel=info

# 运行. 在celery能看到结果等于10
./addTask_main.py

```
### Scoop

- 性能对比: Scoop.futures.mapReduce() 与 python内置map()

```py
import operator
import time
from scoop import futures

def my_sum(inputData):
    # 延长计算时间, 如果没有延长, 则有可能python内置map()更快
    time.sleep(0.01)
    return sum(inputData)

def CompareMapReduce():
    mapScoopTime = time.time()
    res = futures.mapReduce(
        my_sum,
        operator.add,
        # 相加每个元素[[], [1], [2, 2], [3, 3, 3], [4, 4, 4, 4]...1000]]
        list([a] * a for a in range(1000)),
    )
    # futures.mapReduce()
    mapScoopTime = time.time() - mapScoopTime
    print("futures.map in SCOOP executed in {0:.3f}s with result:{1}".format(
          mapScoopTime, res))

    # python map()
    mapPythonTime = time.time()
    res = sum(map(my_sum, list([a] * a for a in range(1000))))
    mapPythonTime = time.time() - mapPythonTime
    print("map Python executed in: {0:.3f}s with result: {1}".format(
        mapPythonTime, res))

if __name__ == '__main__':
    CompareMapReduce()
```

- Scoop.futures.map快10倍以上

```
futures.map in SCOOP executed in 0.899s with result:332833500
map Python executed in: 10.101s with result: 332833500
```

# reference

- [Python并行编程 中文版](https://python-parallel-programmning-cookbook.readthedocs.io/zh_CN/latest/index.html)
