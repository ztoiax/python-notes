# 科学计算

## numpy

- [官方文档](https://numpy.org/doc/stable/user/quickstart.html)

- 速度比函数对数组内的每个元素进行处理, 快上百倍

- 但内存比list大

> 默认数据类型是 `float64`

```py
import numpy as np

# zeros() 创建3行2列数组,全0的数组
a = np.zeros((3, 2))

# astype 对现有转换数据类型
a.astype(int)

# 或者 dtype 指定数据类型
a = np.zeros((3, 2), dtype=np.int32)

# random.rand() 创建3行2列的随机数组
np.random.rand(3, 2)

# shape 获取数组行列
a.shape

# arange()创建0到8的数组
np.arange(0, 9)

# arange()创建0到9的数组
np.arange(10)

# arange() 每个元素 * 2
np.arange(10) * 2

# arange() 每个元素平方
np.arange(10) ** 2


# linspace() 创建有步进的数组
np.linspace(0, 9, 4)
np.linspace(0, 1, 5)

# r_ 自定义数组.把0放在中间
np.r_[1:5,0,6:10]

# array()自定义数组

# 1行2列
np.array([2, 4])

# 3行1列
np.array([[10], [20], [30]])

# 配合arange()
np.array([np.arange(1, 9),
          np.arange(0, 8)])
```

- 计算

```py
a = np.arange(10)

# 左右交换
np.append(a[4:],a[:4])

# 或者
b = int(a.size / 2)
np.append(a[b:],a[:b])

# 或者使用split()
b, c = np.split(a, 2)
np.append(c, b)

# 左右交换后,分别翻转
np.append(a[b::-1], a[9:b:-1])

# 以步进为2,左右交换后,分别翻转
np.append(a[b::-1][::2], a[9:b:-1][::2])
```

- 维度变换

```py
a= np.array([[ 0,  1,  2,  3],
               [10, 11, 12, 13],
               [20, 21, 22, 23],
               [30, 31, 32, 33],
               [40, 41, 42, 43]])

# 转换为单行单维
a.ravel()
np.hstack(a)

# 转换成2行
a.reshape(2,-1)
# 或者手动转换,并重新赋值
a.resize((2,10))

# 行列交换
a.T

# column_stack()列表类型转数组,并进行同维度的合并
a = [[0,0],[1,1],[2,2]]
b = [[9,9],[8,8],[7,7]]
np.column_stack((a,b))
# 或者
np.c_[a, b]
```

- 以数组i,j的行列分布,获取数组a值

```py
a = np.arange(10)
i = np.array([0,1])
j = np.array([[0],[1]])
a[i]
a[j]
a[l]

# 以i为行, j为列截取数组b(像截图一样)
b = np.arange(12).reshape(3,4)
l = (i, j)
b[l]

i = np.array([[0, 1],[1, 2]])
j = np.array([[2, 1],[3, 3]])
b[:,i]
b[:,j]
```

```py
a = np.arange(2, 4)
b = np.arange(3, 5)
```

- a + b

    ```py
    [2, 3]
      +
    [3, 4]
      =
    [5, 7]
    ```

- np.dot(a, b)

    ```py
    ??
    ```

- np.sum()

    ```py
    a = np.array([np.arange(1, 9),
              np.arange(0, 8)])

    # axis=0 行相加
    a.sum(axis=0)

    # axis=1 列相加
    a.sum(axis=1)
    ```

- 不同尺寸也能计算

    > 自动扩展相同尺寸

    - a + b

    ```py
    a = np.array([2, 4])
    b = np.array([[10], [20], [30]])
    ```

    ```py
    [2, 4] + [10, 10] = [12, 14]
    [2, 4] + [20, 20] = [22, 24]
    [2, 4] + [30, 30] = [32, 34]
    ```
#### numpy 处理图片

- [Image Processing with Numpy](https://www.degeneratestate.org/posts/2016/Oct/23/image-processing-with-numpy/)

```py
import numpy as np
from PIL import Image

# 打开图片并转换数组
image = np.array(Image.open('/tmp/test.jpg'))
image.shape

# 提取红色
image_red = image[:,:,0]
# 显示
Image.fromarray(image_blue).show()
```

- 合并图片

```py
image1 = Image.open('/home/tz/1.jpg')
image2 = Image.open('/home/tz/2.jpg')

# 裁剪为800 * 600
rect = 0, 0, 600, 800
image1 = image1.crop(rect)
image2 = image2.crop(rect)
image1 = np.array(image1)
image2 = np.array(image2)

# 合并
image_merge = image1 * 0.5 + image2 * 0.5
# 转换整数
image_merge = image_merge.astype(np.uint8)

image.fromarray(image_merge).show()
```

