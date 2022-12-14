# 几何

## 正多边形

- 正多边形外角公式
$$
\frac {180 - (n - 2) \times 180}{n}
$$

```py
from turtle import *


def regular(n, length=100):
    for i in range(n):
        # 边长
        forward(length)
        # 旋转角度
        right(180 - (n - 2) * 180 / n)


# 等边三角形
regular(3)

# 正方形
regular(4)
```

### 星(star)

- 五角星
```py
def star(length=200):
    for i in range(5):
        forward(length)
        right(144)
star()
```

- 九角星
```py
def star1(length=200):
    for i in range(9):
        forward(length)
        right(160)
```

![image](./imgs/star.avif)

- 五角星海龟螺旋

```py
def f():
    speed(1000000)
    for i in range(70):
        right(5)
        star(400 - i * 5)
f()
```

![image](./imgs/star1.avif)

### 正方形(square)

- 画60个正方形, 每次向右旋转5度
```py
def f():
    # 设置速度
    speed(1000000)
    for i in range(60):
        right(5)
        regular(4)

f()
```

![image](./imgs/square.avif)

- 海龟螺旋

```py
def f():
    speed(1000000)
    for i in range(70):
        right(5)
        # 每次边长都会缩小
        regular(4, 400 - i * 5)

f()
```

![image](./imgs/square1.avif)
