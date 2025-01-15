
<!-- mtoc-start -->

* [设计模式](#设计模式)
  * [访问者模式](#访问者模式)
  * [发布/订阅模式(交换机)](#发布订阅模式交换机)
  * [洋芋编程：计算机网络中的设计模式](#洋芋编程计算机网络中的设计模式)
* [reference](#reference)

<!-- mtoc-end -->

# 设计模式

## 访问者模式

- 访问者模式严重依赖递归

- 运算类
```py
class Number:
    def __init__(self, value):
        self.value = value

class Operator:
    def __init__(self, left, right):
        self.left = left
        self.right = right

# 运算类
class Add(Operator):
    pass

class Mul(Operator):
    pass


# eval处理
class NodeVisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))

# 封装类
class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

t1 = Add(Number(1), Number(2))
t2 = Mul(t1, Number(3))

e = Evaluator()
print(e.visit(t2)) # 9
```
- 封装成stack
```py
class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def visit_Number(self, node):
        self.instructions.append(('PUSH', node.value))

    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))

    def visit_Add(self, node):
        self.binop(node, 'ADD')

    def visit_Mul(self, node):
        self.binop(node, 'MUL')


t1 = Add(Number(1), Number(2))
t2 = Mul(t1, Number(3))

e = StackCode()
print(e.generate_code(t2))
# [('PUSH', 1), ('PUSH', 2), ('ADD',), ('PUSH', 3), ('MUL',)]
```

## 发布/订阅模式(交换机)
```py
from collections import defaultdict

# 任务类
class Task:
    def send(self, msg):
        print(msg)


# 交换机类
class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    # 有多少个task就send多少次
    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# 交换机类的字典
_exchanges = defaultdict(Exchange)

def get_exchange(name):
    return(_exchanges[name])


if __name__ == '__main__':
    task_a = Task()
    task_b = Task()

    # 生成名为tz的交换机
    exc = get_exchange('tz')

    # 连接交换机(订阅)
    exc.attach(task_a)
    exc.attach(task_b)

    # 执行
    exc.send('msg1')
    exc.send('msg2')

    # 取消连接(解绑)
    exc.detach(task_a)
    exc.detach(task_b)
```
输出
```
msg1
msg1
msg2
msg2
```

- 使用contextmanager实现with语句, 防止用户忘记detach
```py
from collections import defaultdict
from contextlib import contextmanager

# 任务类
class Task:
    def send(self, msg):
        print(msg)


# 交换机类
class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    # 添加with语句, 防止用户忘记detach
    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    # 执行task的方法
    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# 交换机类的字典
_exchanges = defaultdict(Exchange)

def get_exchange(name):
    return(_exchanges[name])


if __name__ == '__main__':
    task_a = Task()
    task_b = Task()

    # 生成名为tz的交换机
    exc = get_exchange('tz')

    # 订阅(绑定)两个任务
    with exc.subscribe(task_a, task_b):
        exc.send('msg1')
        exc.send('msg2')
```


- 对Task类加入统计send的次数
```py
class Task:
    def __init__(self):
        # 统计发了多少次send
        self.count = 0

    def send(self, msg):
        self.count += 1
        print('msg[{}]: {!r}'.format(self.count, msg))
```

## [洋芋编程：计算机网络中的设计模式](https://mp.weixin.qq.com/s/AzzEkjVcSiBcOR4F-b6YjA)

# reference

- [美团技术团队：设计模式二三事](https://tech.meituan.com/2022/03/10/interesting-talk-about-design-patterns.html)
