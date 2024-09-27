
<!-- vim-markdown-toc GFM -->

* [algorithms(算法)](#algorithms算法)
    * [O()：大O标记法](#o大o标记法)
        * [常见语句的复杂度](#常见语句的复杂度)
    * [sort(排序)](#sort排序)
        * [bubble sort(冒泡排序)](#bubble-sort冒泡排序)
            * [comb sort(梳子排序)](#comb-sort梳子排序)
            * [cocktail Sort(混合排序)](#cocktail-sort混合排序)
            * [oddEvenSort](#oddevensort)
        * [insertion sort(插入排序)](#insertion-sort插入排序)
            * [二分插入排序](#二分插入排序)
        * [select sort(选择排序)](#select-sort选择排序)
            * [pancake Sort(煎饼排序)](#pancake-sort煎饼排序)
        * [merge sort(归并排序)](#merge-sort归并排序)
        * [bitonic Sort(双音排序)](#bitonic-sort双音排序)
        * [shell sort(希尔排序)](#shell-sort希尔排序)
        * [quick sort (快速排序)](#quick-sort-快速排序)
            * [0, 1, 2三路快速排序](#0-1-2三路快速排序)
        * [heap sort(堆排序)](#heap-sort堆排序)
            * [使用heapq模块的heapify函数](#使用heapq模块的heapify函数)
        * [bucket sort(桶排序)](#bucket-sort桶排序)
        * [counting sort(计数排序)](#counting-sort计数排序)
        * [radix sort(基数排序)](#radix-sort基数排序)
        * [pigeonhole Sort(范围排序)](#pigeonhole-sort范围排序)
        * [stooge sort](#stooge-sort)
        * [Timsort](#timsort)
        * [煎饼翻转](#煎饼翻转)
    * [search(搜索)](#search搜索)
        * [binary search(二分搜索)](#binary-search二分搜索)
        * [hash tab(hash表)](#hash-tabhash表)
            * [hash函数](#hash函数)
                * [双字母hash函数](#双字母hash函数)
        * [Bloom Filters(布隆过滤器)](#bloom-filters布隆过滤器)
            * [Counting Bloom Filter(计数布隆过滤器)](#counting-bloom-filter计数布隆过滤器)
            * [Cuckoo Filter(布谷鸟过滤器)](#cuckoo-filter布谷鸟过滤器)
        * [匹配查找](#匹配查找)
            * [穷举: O(nm)](#穷举-onm)
            * [Boyer-Moore](#boyer-moore)
            * [kmp(Knuth-Morris-Pratt)](#kmpknuth-morris-pratt)
        * [lcs(Longest Common Subsequence)最长公共子序列](#lcslongest-common-subsequence最长公共子序列)
    * [Linked List(链表)](#linked-list链表)
        * [Linked List(单向链表)](#linked-list单向链表)
            * [单向链表归并排序](#单向链表归并排序)
        * [DoublyList(双向链表)](#doublylist双向链表)
        * [CircularQueue(环形队列)](#circularqueue环形队列)
            * [判断是否为环形队列](#判断是否为环形队列)
            * [LRU缓存](#lru缓存)
        * [skip list(跳表)](#skip-list跳表)
        * [Python 不用堆和树实现按优先级过期的 LRU 缓存: https://death.andgravity.com/lru-cache](#python-不用堆和树实现按优先级过期的-lru-缓存-httpsdeathandgravitycomlru-cache)
        * [Blockchain(区块链)](#blockchain区块链)
    * [缓存清除算法](#缓存清除算法)
    * [graph(图)](#graph图)
        * [遍历有环图](#遍历有环图)
        * [生成树](#生成树)
            * [Prim算法](#prim算法)
            * [Kruskal算法](#kruskal算法)
        * [Dijkstra最短路径算法](#dijkstra最短路径算法)
        * [全排列](#全排列)
        * [走出迷宫](#走出迷宫)
        * [图的应用](#图的应用)
    * [tree(树)](#tree树)
        * [树相关的基础概念：](#树相关的基础概念)
        * [binary tree(二叉树)](#binary-tree二叉树)
            * [遍历树](#遍历树)
                * [dfs](#dfs)
                * [bfs](#bfs)
            * [只遍历左子树](#只遍历左子树)
            * [反转树(invert)](#反转树invert)
            * [计算树的高度](#计算树的高度)
                * [dfs](#dfs-1)
                * [bfs](#bfs-1)
            * [判断是否为平衡二叉树(balanced binary tree)](#判断是否为平衡二叉树balanced-binary-tree)
            * [判断是否为对称二叉树(symmetric binary tree)](#判断是否为对称二叉树symmetric-binary-tree)
            * [判断是否为堂兄弟结点](#判断是否为堂兄弟结点)
        * [full binary tree](#full-binary-tree)
            * [判断是否为full binary tree](#判断是否为full-binary-tree)
        * [完全二叉树(complete binary tree)](#完全二叉树complete-binary-tree)
            * [判断是否为完全二叉树](#判断是否为完全二叉树)
        * [二叉搜索树(binary search tree)](#二叉搜索树binary-search-tree)
            * [输入两个值, 计算他们之间的值](#输入两个值-计算他们之间的值)
            * [判断是否为二叉搜索树](#判断是否为二叉搜索树)
        * [自平衡二叉搜索树(AVL tree)](#自平衡二叉搜索树avl-tree)
        * [红黑树](#红黑树)
        * [字典树(trie tree)](#字典树trie-tree)
        * [2-3树](#2-3树)
        * [B树](#b树)
        * [B+树](#b树-1)
        * [B-link树](#b-link树)
        * [R树](#r树)
        * [LSMTree(日志结构合并树)](#lsmtree日志结构合并树)
    * [递归(rec)](#递归rec)
        * [阶乘](#阶乘)
        * [反转列表](#反转列表)
        * [累加列表里的元素](#累加列表里的元素)
        * [次方](#次方)
        * [汉诺塔](#汉诺塔)
        * [反转正整数](#反转正整数)
        * [集合划分](#集合划分)
        * [整数划分](#整数划分)
        * [最大公约数, 最小公倍数](#最大公约数-最小公倍数)
    * [分治算法](#分治算法)
        * [找到出现最多次数的值](#找到出现最多次数的值)
    * [动态规划](#动态规划)
        * [UnlyNum(丑数)](#unlynum丑数)
        * [进制转换](#进制转换)
        * [最少硬币找零](#最少硬币找零)
        * [完全背包问题](#完全背包问题)
    * [贪心算法](#贪心算法)
        * [背包问题](#背包问题)
        * [钱币找零](#钱币找零)
        * [任务调度](#任务调度)
        * [活动安排](#活动安排)
        * [分数背包](#分数背包)
        * [连续背包](#连续背包)
        * [密度贪心算法](#密度贪心算法)
    * [双指针算法](#双指针算法)
        * [三数之和](#三数之和)
            * [四数之和](#四数之和)
        * [救生艇](#救生艇)
        * [存储水](#存储水)
    * [string(字符串)](#string字符串)
        * [回文字符串](#回文字符串)
        * [中叙, 后叙(逆波兰记法), 前叙表达式](#中叙-后叙逆波兰记法-前叙表达式)
    * [fib(斐波那契)](#fib斐波那契)
        * [循环 while, for](#循环-while-for)
        * [递归](#递归)
        * [迭代](#迭代)
        * [泛函](#泛函)
    * [pi(圆周率)](#pi圆周率)
    * [牛顿法求平方根](#牛顿法求平方根)
    * [密码](#密码)
        * [rsa整数加密](#rsa整数加密)
* [reference](#reference)

<!-- vim-markdown-toc -->

# algorithms(算法)

- [算法可视化](https://visualgo.net/en)

- [算法可视化](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)

## O()：大O标记法

- Big oh (O) : 最坏的情况
- Big Omega (Ω) : 最好的情况
- Big Theta (Θ) : 平均

- n 表示数据量的大小

- 如果n=1000时需要花费1秒

    - O(n)线性复杂度: n = 5000时就需要5秒

    - O(n^2)线性复杂度: n = 5000时就需要25秒

- 大O标记法, 并没告诉我们实际花费的时间, 而是n值(数据量)发生变化时, 所对应的运行时间的变化

    - **复杂度越高并不代表一定更慢**: 同一个问题, 有的O(n^2)的算法可能只需0.1秒, 有的O(n)的算法可能要1秒

| f(n)    | Name                 |
| ------- | -------------------- |
| 1       | Constant(常数)       |
| log n   | Logarithmic(对数)    |
| n       | Linear(线性)         |
| n log n | Log Linear(线性对数) |
| n^2     | Quadratic(平方)      |
| n^3     | Cubic(立方)          |
| 2^n     | Exponential(指数)    |

![image](./imgs/algorithms/Big-O.avif)

- 大O标记法中，常见的时间复杂度有一下几类：

    - 常数阶:复杂度通常用O(1)表示，不是说程序只有一行基础代码运行，它的意思是不管程序的输入是什么程序都会运行一个固定数量的运算，这个数可以是任何常数5、100、200都行，重点是他不会随输入的增长才被统计称 O(1)

    - 多项式阶：很多算法的时间复杂度是 O(n)、O(n2)、O(n3)这样的多项式。

    - 指数阶：指数阶的时间复杂度用O(2n) 、 O(nn) 等表示，这种程序运行效率极差，是程序员写代码一定要避开的大坑。

    - 对数阶：对数阶的程序运行效率较高，通常用O(logn)、 O(n log n) 等表示。

    - 按照时间复杂度从低到高排序：
    ```
    O(1) < O(logn) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)
    ```

### 常见语句的复杂度

- [网管叨bi叨：怎么计算我们自己程序的时间复杂度](https://mp.weixin.qq.com/s/hVzeXSx-0qRSz8QioSoXRg)

- 顺序语句的复杂度

    ```py
    # 计算3个数字的平方和的函数。
    def square_sum(a, b, c):
        sa = a * a
        sb = b * b
        sc = c * c
        total = sa + sb + sc
        return total
    ```

    - 函数中的每个语句都是一个基本运算。每行的时间复杂度为 O(1)。我们把所有语句的时间加起来，它仍然是 O(1)， 记住昂，不是O(3)。

    - O(1)表示程序时常数级的时间复杂度，不管程序的输入是什么程序都会运行数量固定的操作。

- 条件语句的复杂度

    ```py
    if isValid:
        statement1
        statement2
    else:
        statement3
    ```

    - 时间复杂度可以按下面这个公式推导出来：

        ```
        T(n) = Math.max([t(statement1) + t(statement2)], [time(statement3)])
        ```

    - if代码块中的时间复杂度为O( n log n) — 常用编程语言内置排序算法的时间复杂度，else代码块的时间复杂度为O(1)，那么整个代码的时间复杂度为：

        ```
        O([n log n] + [n]) => O(n log n)
        ```

        ```py
        if isValid:
            array.sort()
            return True
        else:
            return False
        ```

- 循环语句的复杂度

    - 线性循环

        - 循环执行 array.length次，所有与输入数据增长而成比例增长的循环都具有线性—常数阶的时间复杂度 O(n)。

            ```py
            for i in range(len(array)):
                statement1
                statement2
            ```


    - 对数循环

        - 对于这个程序，我们无法确定while 以及 i = i*2 语句运行了多少次，这时可以假设运行了x次，每次运行后i的值为2、22、23… 当while 语句的条件不满足即i = n时结束，也就是2x = n ， x = log2n ，它的时间复杂度近似于O(logn )。

        ```py
        def fn(n):
            i = 1
            while i < n:
                i *= 2
        ```

    - 固定次数循环
        - 无聊时固定循环4次还是 100 次时间复杂度都是 O(1)
        ```py
        for i in range(4):
            statement1
            statement2
        ```

    - 嵌套循环
        - 假设循环中的语句都是基础操作，没有对函数的调用，那么这个代码有两层嵌套循环，时间复杂度为O(n2)。
        ```py
        for i in range(n):
            statement1

            for j in range(m):
                statement2
                statement3
        ```

- 循环中有函数调用的时间复杂度

    - 循环中有函数调用，时间复杂度可以用下面这个公式计算：

        ```
        T(n) = n * [ t(fn1()) + n * [ t(fn2()) + n * [ t(fn3()) ] ] ]
        ```

    - 根据 fn1、fn2 和 fn3 函数自身的时间复杂度，整个程序将拥有不同的运行时间。

        - 如果这三个函数它们都是常数阶 O(1)，那么最终的运行时间将为 O(n3)。但是如果只有 fn1 和 fn2 是常数介， fn3 的时间复杂度为 O(n2)，则该程序的运行时间将为 O(n5)。

        ```py
        for i in range(n):
            fn1()
            for j in range(n):
                fn2()
                for k in range(n):
                    fn3()
        ```

- 函数递归调用的时间复杂度

    - O(n): 线性复杂度

        ```py
        def iter(x):
            if x == 0:
                return
            iter(x - 1)
        ```

        - 时间复杂度是`x`的大小O(n)

        - 但递归调用,都会在内存分配一个新的堆栈, 直到调用返回

            - 到最深的递归时, 分配了x个堆栈, 空间复杂度也是O(n)

    - 斐波那切数列的递归调用实现版本，它的时间复杂度为O(2n)
        - 平时写代码时在你不确定程序能执行多少次的时候，最好不要轻易使用递归调用。
        ```py
        def fn(n):
            if n == 1 or n == 2:
                return 1
            return fn(n - 1) + fn(n - 2)
        ```

## sort(排序)

- 是否稳定:

    - 一个排序算法使元素之间, 保留原有的相对位置, 就可以说它是**稳定的**

    - 意义: 如果对学生的成绩进行排序, 一个稳定的排序算法, 可以把成绩相同的学生, 保留原有的字母顺序

- 是否在位(in-place):

    - 是否需要使用额外的空间, 不需要就是**在位的(in-place)**

![image](./imgs/algorithms/bigO_sort.avif)

- [geeksforgeeks: sorting-algorithms](https://www.geeksforgeeks.org/sorting-algorithms/)

- [排序算法](https://big-o.io/)

- [zhihu: 算法实现](https://zhuanlan.zhihu.com/p/49271189)

### bubble sort(冒泡排序)

![image](./imgs/algorithms/bubbleSort.avif)

- 正向:

```py
def bubbleSort(list1):
    length = len(list1) - 1
    for i in range(length, 0, -1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
```

- 反向:

    - 循环:

    ```py
    def bubbleSort(list1):
        length = len(list1)
        for i in range(length):
            for j in range(length-1, i, -1):
                if list1[j-1] > list1[j]:
                    list1[j], list1[j-1] = list1[j-1], list1[j]
    ```

    - 函数式编程:

    ```py
    def iter(list1, i):
        if i <= 0:
            return

        j = i - 1
        if list1[j] > list1[i]:
            list1[j], list1[i] = list1[i], list1[j]

        iter(list1, j)


    def bubbleSort(list1):
        length = len(list1)
        for i in range(1, length):
            iter(list1, i)
    ```

#### comb sort(梳子排序)

- 优化的冒泡算法: 每个元素并不是传统的与后一个元素(i+1)对比, 而是对比不断缩小的长度系数(i+gap)

![image](./imgs/algorithms/combSort.avif)

```py
def getNextGap(gap):
    # 系数为1.3
    gap = gap / 1.3
    if gap < 1:
        return 1
    else:
        return int(gap)


def combSort(list1):
    length = len(list1)
    gap = length

    while gap > 1:
        gap = getNextGap(gap)

        for i in range(0, length-gap):
            # 对比加上系数的元素
            if list1[i] > list1[i + gap]:
                list1[i], list1[i + gap] = list1[i + gap], list1[i]
```

#### cocktail Sort(混合排序)

- 冒泡排序的变种. 先从左到右, 再从右到左

```py
def cocktailSort(list1):
    length = len(list1)
    start = 0
    end = length - 1

    while length > 1:
        # 从左到右
        for i in range(start, end):
            if (list1[i] > list1[i + 1]):
                list1[i], list1[i + 1] = list1[i + 1], list1[i]

        # 从右到左
        for i in range(end-1, start-1, -1):
            if (list1[i] > list1[i + 1]):
                list1[i], list1[i + 1] = list1[i + 1], list1[i]

        start += 1
        end -= 1
        length -= 2
```

#### oddEvenSort

- 冒泡排序的变种. 奇数排序一次, 偶数排序一次

![image](./imgs/algorithms/odd-even-sort.avif)
```py
def oddEvenSort(list1):
    length = len(list1)
    half = length // 2
    while half > 0:
        for i in range(1, length-1, 2):
            if list1[i] > list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]

        for i in range(0, length-1, 2):
            if list1[i] > list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
        half -= 1
```

### insertion sort(插入排序)

![image](./imgs/algorithms/insertionSort.avif)

```py
def insert(list1, j, i):
    tmp = list1.pop(i)
    list1.insert(j, tmp)
```

- 循环:

```py
def sort(list1):
    length = len(list1)
    for i in range(1, length):
        for j in range(i):
            if list1[i] < list1[j]:
                insert(list1, j, i)
```

- 函数式编程:

```py
def iter(list1, j, i):
    if list1[i] < list1[j]:
        insert(list1, j, i)
        return

    if j < i:
        iter(list1, j+1, i)


def sort(list1):
    length = len(list1)
    for i in range(length):
        iter(list1, 0, i)
```

#### 二分插入排序

- 时间复杂度依然是O(n^2)

    - 但比较的复杂度是O(log n)

```py
def insertionSort(list1):
    length = len(list1)
    for i in range(length):
        l = 0
        r = i - 1

        # 二分查找插入的位置
        while l <= r:
            mid = (l + r) // 2
            if list1[mid] <= list1[i]:
                l += 1
            elif list1[mid] >= list1[i]:
                r -= 1

        insert(list1, l, i)
```

### select sort(选择排序)

```py
def selectSort(list1):
    length = len(list1)
    for i in range(length):
        index = i
        for j in range(i+1, length):
            if list1[index] > list1[j]:
                index = j

        list1[i], list1[index] = list1[index], list1[i]
```

#### pancake Sort(煎饼排序)

- 选择排序的变种, 找到最大值, 移动至末尾

![image](./imgs/algorithms/pancakeSort.avif)

```py
# 查询列表内最大值的偏移量
def findMax(list1, length):
    max_index = 0
    for i in range(0, length):
        if list1[i] > list1[max_index]:
            max_index = i
    return max_index


def pancakeSort(list1):
    length = len(list1)
    for i in range(length, 1, -1):
        max_index = findMax(list1, i)

        # 移动至末尾
        if max_index != i - 1:
            list1[0], list1[max_index] = list1[max_index], list1[0]
            list1[0], list1[i-1] = list1[i-1], list1[0]
```

### merge sort(归并排序)

![image](./imgs/algorithms/mergeSort.avif)

- merge sort由冯诺依曼于1945年发明

- 分治算法: 找到最简单的解, 然后将其组合起来

    - 设置一个阈值(也叫递归基): 低于这个值时, 问题就不再分解

        - 大多数情况下是2

    - 分解成多个子集

        - 如果列表的长度是0或1: 低于阈值, 不会分解

        - 如果列表长度大于1: 分解成两个列表


    - 合并子集

        - 对比两个列表的第一个元素, 将小的元素移动(append)到目标列表(result)的末尾

        - 最后将剩余的列表元素, 移动到目标列表末尾

- 时间复杂度是外层的分解 * 内层的合并: O(n log n)

    - 空间复杂度只有内层的合并也就是: O(n)

    - 分解的时间复杂度是O(log n)

    - 合并的时间复杂度是O(n)

```py
def merge(left, right, compare):
    # 目标列表
    result = []

    l = r = 0
    length_left, length_right = len(left), len(right)

    # 对比两个列表的第一个元素, 将小的元素移动到目标列表(result)的末尾
    while l < length_left and r < length_right:
        if compare(left[l], right[r]):
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    # 检查剩余元素
    while l < length_left:
        result.append(left[l])
        l += 1

    while r < length_right:
        result.append(right[r])
        r += 1

    return result


def mergeSort(list1, compare=lambda x, y: x < y):
    length = len(list1)
    if length < 2:
        return list1

    mid = length // 2
    left = mergeSort(list1[:mid], compare)
    right = mergeSort(list1[mid:], compare)
    return merge(left, right, compare)
```
### bitonic Sort(双音排序)

![image](./imgs/algorithms/bitonicSort.avif)

```py
def compAndSwap(list1, i, j, dire):
    if dire==1 and list1[i] > list1[j]\
            or dire==0 and list1[i] < list1[j]:
        list1[i], list1[j] = list1[j], list1[i]


def bitonicMerge(list1, low, length, dire):
    if length > 1:
        mid = length // 2
        for i in range(low, low+mid):
            compAndSwap(list1, i, i+mid, dire)
        bitonicMerge(list1, low, mid, dire)
        bitonicMerge(list1, low+mid, mid, dire)


def bitonic(list1, low, length, dire):
    if length > 1:
          mid = length // 2
          bitonic(list1, low, mid, 1)
          bitonic(list1, low+mid, mid, 0)
          bitonicMerge(list1, low, length, dire)


def bitonicSort(list1):
    up = 1
    bitonic(list1, 0, len(list1), up)


list1 = [3, 7, 4, 8, 6, 2, 1, 5]
bitonicSort(list1)
print(list1)
```


### shell sort(希尔排序)

![image](./imgs/algorithms/shellSort.gif)
```py
def shellSort(list1):
    length = len(list1)
    half = length // 2
    while half > 0:
        for i in range(half, length):
            while i >= half:
                if list1[i-half] > list1[i]:
                    list1[i], list1[i-half] = list1[i-half], list1[i]
                i -= half
        half //= 2
```

- 以上代码是指针是从half到lenght. 现在改为指针从0开始到half

    - 这样的修改是致命的

    ```py
    def shellSort(list1):
        length = len(list1)
        half = length // 2
        while half > 0:
            # 指针改为从0开始移动
            for i in range(0, half):
                while i <= half:
                    if list1[i] > list1[i+half]:
                        list1[i], list1[i+half] = list1[i+half], list1[i]
                    i += 1
            half //= 2

    # 结果不准确
    list1 = [1, 3, 7, 4, 8, 6, 2, 1, 5]
    shellSort(list1)
    print(list1)

    # 偶数个元素时会报错
    list1 = [3, 7, 4, 8, 6, 2, 1, 5]
    shellSort(list1)
    print(list1)
    ```

### quick sort (快速排序)

![image](./imgs/algorithms/quickSort.avif)

- 分治算法

- 选取一个基准元素, 把比这个基准元素小的移动到左边;大的移动到右边. 这样一轮下来, 就确定了这个基准元素的位置

    - 基准元素一般是取第一个元素

```py
def partition(start, end, list1):
    pivot_index = start
    pivot = list1[start]

    while start < end:
        length = len(list1)
        while start < length and list1[start] <= pivot:
            start += 1

        while list1[end] > pivot:
            end -= 1

        if start < end:
            list1[start], list1[end] = list1[end], list1[start]

    list1[end], list1[pivot_index] = list1[pivot_index], list1[end]
    return end

def quick(start, end, list1):
    if start < end:
        p = partition(start, end, list1)
        quick(start, p - 1, list1)
        quick(p + 1, end, list1)

def quickSort(list1):
    quick(0, len(list1) - 1, list1)
```
#### 0, 1, 2三路快速排序
```py
def quickSort(list1):
    i = l = 0
    length = len(list1)
    r = length - 1

    while i <= r:
        if list1[i] < 1:
            list1[i], list1[l] = list1[l], list1[i]
            l += 1
            i += 1
        elif list1[i] > 1:
            list1[i], list1[r] = list1[r], list1[i]
            r -= 1
        else:
            i += 1


list1 = [0, 2, 2, 1, 0, 1]
quickSort(list1)
print(list1)
```

### heap sort(堆排序)

- 将数组看作是完全二叉树

    - 把最大的元素, 移动到最底层; 最小的数移动到最顶层


![image](./imgs/algorithms/heapSort.avif)

```py
def heapify(list1, length, i):
    root = i
    l = 2 * i + 1 # 左节点 = 2*i + 1
    r = 2 * i + 2 # 右节点 = 2*i + 2

    # 查找比root数大的节点
    if l < length and list1[root] < list1[l]:
        root = l

    # 先对比右节点
    if r < length and list1[root] < list1[r]:
        root = r

    # 如果找到比root数大的节点后, 就交换和递归
    if root != i:
        list1[i], list1[root] = list1[root], list1[i]
        heapify(list1, length, root)


def heapSort(list1):
    length = len(list1)
    # 生成堆
    for i in range(length//2-1, -1, -1):
        heapify(list1, length, i)

    # 将第一个值(最大的值), 放到最后面
    for i in range(length-1, 0, -1):
        list1[i], list1[0] = list1[0], list1[i]  # swap
        heapify(list1, i, 0)
```

#### 使用heapq模块的heapify函数
```py
import heapq

def heapSort(list1):
    result = []
    length = len(list1)
    for i in range(length):
        heapq.heapify(list1)
        # pop 第一个值, 也是最小值
        result.append(heapq.heappop(list1))
    return result
```

### bucket sort(桶排序)

- 小数排序

    ![image](./imgs/algorithms/BucketSort.avif)

```py
def bucketSort(list1):
    bucket = []
    num = 10

    # 生成桶
    for _ in range(num):
        bucket.append([])

    # 将每个元素加入桶
    for i in list1:
        # 小数乘以桶数
        index = int(i * num)
        bucket[index].append(i)

    # 对每个桶执行插入排序
    for i in range(num):
        bucket[i] = insertionSort(bucket[i])

    # 将桶内的元素加入列表
    k = 0
    for i in range(num):
        for j in range(len(bucket[i])):
            list1[k] = bucket[i][j]
            k += 1


list1 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucketSort(list1)
print(list1)
```

### counting sort(计数排序)

![image](./imgs/algorithms/CountingSort.avif)

```py
def countingSort(list1):
    # 桶的数量为最大值加1
    size = max(list1) + 1
    count = [0] * size

    # 对桶进行计数
    for i in range(size):
        for j in list1:
            if i == j:
                count[i] += 1

    # 排列
    j = 0
    for i in range(size):
        while count[i] > 0:
            list1[j] = i
            count[i] -= 1
            j += 1
```

### radix sort(基数排序)

![image](./imgs/algorithms/RadixSort.avif)

```py
def countingSort(list1, exp1):
    length = len(list1)

    output = [0] * length
    count = [0] * 10

    # 对个位数相同的元素进行计数
    for i in range(0, length):
        index = list1[i] // exp1
        count[index % 10] += 1

    # 加上前面的计数, 得到累计位置
    for i in range(1, 10):
        count[i] += count[i-1]

    # 对个位数进行排列
    i = length - 1
    while i >= 0:
        index = list1[i] // exp1
        output[count[index % 10] - 1] = list1[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, length):
        list1[i] = output[i]

def radixSort(list1):
    max1 = max(list1)

    # 位
    exp = 1
    while max1 / exp > 0:
        countingSort(list1, exp)
        exp *= 10
```

### pigeonhole Sort(范围排序)

- 类似于计数排序

```py
def pigeonholeSort(list1):
    my_min = min(list1)
    my_max = max(list1)
    size = my_max - my_min + 1

    # 生成桶
    buckets = [0] * size

    # 每个元素的值减去最小值, 分配对应的桶
    for x in list1:
        buckets[x - my_min] += 1

    # 将桶的值返回给列表
    i = 0
    for count in range(size):
        while buckets[count] > 0:
            buckets[count] -= 1
            # 桶值加上最小值
            list1[i] = count + my_min
            i += 1
```

### stooge sort

![image](./imgs/algorithms/stoogeSort.avif)

```py
def stooge(list1, l, r):
    if l >= r:
        return

    # left 对比 right
    if list1[l]>list1[r]:
        list1[l], list1[r] = list1[r], list1[l]

    if r - l + 1 > 2:
        stooge(list1, l, r-1)
        stooge(list1, l+1, r)


def stoogeSort(list1):
    stooge(list1, 0, len(list1)-1)
```

### Timsort

> 是python, java...等默认的排序算法

- tim是python之禅(import this)的作者, 也是高产的python核心开发者

- [Timsort — the fastest sorting algorithm you’ve never heard of](https://hackernoon.com/timsort-the-fastest-sorting-algorithm-youve-never-heard-of-36b28417f399)

- [python中的sort之timsort学习](https://zhuanlan.zhihu.com/p/158972725)
    ![image](./imgs/algorithms/timsort.avif)

- 由`Mergesort`(归并排序) 和 `insertion sort`(插入排序) 两种排序组成

- 1.按顺序扫描元素:

    - 如果扫描的元素是递减的, 则反转扫描的元素

        - 遇到不能递减的元素时, 则对刚才扫描过的元素生成切片(也就是概念run)

        ```
        [4, 2, 1, 3, 5, 7]

        # 扫描并反转
        [1, 2, 4, 3, 5, 7]

        # 生成切片
        1, 2, 4
        ```

    - 如果扫描的元素是递增的, 则不变

- `minrun`概念, 防止合并的切片太短, 太长:

    - 当列表元素的个数小于64时: minrun就是列表长度, 也就是log64等于6

    - 当列表元素的个数大于64时: minrun范围为[32, 64]. 具体选取列表长度的前6位 + 最后2位

    - 切片(run)少于`minrun`时: 使用`insertion sort`.  在元素量少的情况下很快, 但在元素量多时却很慢

- 2.使用归并排序合并切片(和扫描是同步进行的):

    - 将切片放入stack里

    - 当最上面的切片长度**不满足**以下两个条件, 就合并切片:

        - `a > b + c`

        - `b > c`

        ```
        [(1, 2, 4,) (3, 5, 7,)]
        # b == c,  不满足b > c. 合并切片
        [(1, 2, 3, 4, 5, 7,)]
        ```
### 煎饼翻转

- 输入一个数n, 对列表内的前n个元素翻转

```py
def switch(list1):
    l = 0
    r = len(list1) - 1

    while l <= r:
        list1[l], list1[r] = list1[r], list1[l]
        l += 1
        r -= 1

def sort(list1, n):
    tmp = list1[:n]
    switch(tmp)
    return tmp + list1[n:]

list1 = [3, 2, 4, 1]
print(sort(list1, 4))
```

## search(搜索)

### binary search(二分搜索)

- 循环:
```py
def binarySearch(list1, x):
    low = 0
    high = len(list1) - 1

    while low <= high:

        mid = (low + high)//2

        if list1[mid] == x:
            return mid

        elif list1[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


list1 = [3, 4, 5, 6, 7, 8, 9]
result = binarySearch(list1, 5)
print(result)
```

- 函数式编程:
```py
def iter(low, high, n):
    if low >= high:
        return -1

    mid = (high - low) // 2
    if list1[mid] == n:
        return mid
    elif list1[mid] > n:
        iter(low, mid-1, n)
    else:
        iter(mid+1, high, n)


def binarySearch(list1, n):
    return iter(0, len(list1), n)
```

- 递归
```py
def binarySearch(list1, x):
    length = len(list1)
    if length == 0:
        return False
    else:
        mid = length // 2
        if list1[mid] == x:
            return True
        else:
            if list1[mid] > x:
                return binarySearch(list1[:mid], x)
            else:
                return binarySearch(list1[mid+1:], x)
```

### hash tab(hash表)

- 50%的碰撞概率：1.2 * √￣个数
    例子：有100个，只需试12个就可能碰撞

- 链地址法(chaining)

    - 遇到冲突时, 放如链表里

    - 优点:
        - 删除方便

    - 缺点:
        - 需要额外空间

    ![image](./imgs/algorithms/hash_link.avif)

- 开放地址法(open addressing)

    - 遇到冲突时, 寻找下一个空的桶

        - 最简单的方法就是: 按顺序遍历, 直到找到空的桶

    - 优点:
        - 不需要额外的空间

    - 缺点:
        - 桶快填满时, 冲突的几率大大增加, 寻找空桶的时间也增加

        - 删除比链地址法要麻烦

    ![image](./imgs/algorithms/hash_linear.avif)

- 桶越多, 冲突次数越少

    - 没有冲突复杂度为O(1)

    - 完全冲突复杂度为O(n)

    - ruby采用链地址法, 在冲突大于5时, 就增加桶的数量

    - JDK1.8 采用链地址法，针对链表上的数据超过8条的时候，使用了红黑树进行优化

    - python采用开放地址法, 但2/3的桶被填满时, 就增加桶的数量

```py
class Hash:
    def __init__(self, n):
        self.n = n
        # 一个集合代表一个桶. 集合没有重复值
        self.buckets = [set()] * n

    # hash函数
    def _hash(self, x):
        return x % self.n

    def add(self, x):
        self.buckets[self._hash(x)].add(x)

    def remove(self, x):
        self.buckets[self._hash(x)].remove(x)

    def list(self):
        print(self.buckets)


if __name__ == '__main__':
    # 5个桶
    hash = Hash(5)

    # 添加
    hash.add(10)
    hash.add(11)
    hash.add(100)
    hash.add(101)
    hash.list()

    # 删除
    hash.remove(10)
    hash.list()
```
输出
```
[{10, 100}, {11, 101}, set(), set(), set()]
[{100}, {11, 101}, set(), set(), set()]
```

- 保存kv值
```py
class intdict(object):
    def __init__(self, numBuckets):
        self.buckets = []
        self.numBuckets = numBuckets

        # 一个列表代表一个桶
        for _ in range(numBuckets):
            self.buckets.append([])

    def add(self, key, val):
        hashlist = self.buckets[key%self.numBuckets]
        length = len(hashlist)
        for i in range(length):
            # 如果key存在, 就更换key值
            if hashlist[i][0] == key:
                hashlist[i] = (key, val)
                return

        # 如果key不存在, 就添加
        hashlist.append((key, val))

    def get(self, key):
        hashlist = self.buckets[key%self.numBuckets]
        for i in hashlist:
            if i[0] == key:
                return i[1]

    def list(self):
        print(self.buckets)


if __name__ == '__main__':
    # 5个桶
    dict1 = intdict(5)

    # 添加
    for i in range(5):
        dict1.add(i, i)
    dict1.list()

    # 修改
    dict1.add(0, 999)
    dict1.list()

    # 获取
    print(dict1.get(0))
```
输出
```
[[(0, 0)], [(1, 1)], [(2, 2)], [(3, 3)], [(4, 4)]]
[[(0, 999)], [(1, 1)], [(2, 2)], [(3, 3)], [(4, 4)]]
999
```

#### hash函数

- 分组求和法:
    - 1. 电话号码436-555-4601, 分成2位数（43,65,55,46,01）
    - 2. 43 + 65 + 55 + 46 + 01得到 210
    - 3. 210 % 桶数

- 平方取中法:
    - 1. 数44, 先平方, 44^2 = 1936
    - 2. 取中间两个数字 93
    - 3. 93 % 桶数

- 字符串ascii值相加法:
    ```py
    def hash(str1, bucket_num):
        sum = 0
        for i in str1:
            sum += ord(i)

        # 最后相加的值 % 桶数
        return sum % bucket_num
    ```

- 计算桶数:
    - 据统计, 桶数使用率高于2/3时, 冲突率就会很高

    - 因此桶数等于: 字典的个数除以2/3, 最后找到满足这个值的2的n次方(8, 16, 32, 64...)

    - 假设字典个数为676. `676 / 2/3 = 1014`. 满足1014的是2的10次方 = 1024. 因此可以设置桶数为1024

##### 双字母hash函数
- 双字母: aa, ab, ac 

- 个数: `26 ^ 2 = 676`

```py
def hash(key):
    offset = ord('a')
    k1, k2 = key
    return (ord(k2)) - offset + 26 + (ord(k1)) - offset
```

### Bloom Filters(布隆过滤器)

- [介绍](https://llimllib.github.io/bloomfilter-tutorial/zh_CN/)

- [朱小厮的博客：过滤请求绝技 — 布隆过滤器与布谷鸟过滤器]()

- [python实现](https://github.com/jaybaird/python-bloomfilter)

![image](./imgs/algorithms/Bloom-Filter.avif)

- Bitmap 可以看作是一个位数组结构，在这个数组中每一个位置只占有 1 个 bit 的大小，而每个 bit 只有 0 和 1 两种状态。类似于位图（Bitmap）

    - 定义了 K 个不同的哈希函数，当一个元素尝试被 add 加入 Bloom Filter 时，会进行 K 个哈希函数的计算，得到 k 个不同的 bit 索引位置，并将这 k 个 bit 索引位都置为 1，表示插入成功。

    - 检索某个元素，同样经过 K 个不同的哈希函数得到 k 个哈希点位，然后再看看这些点位在对应的 bitmap 索引位上是否都为 1
        - 如果这些点位有任何一个 0，则被检元素一定不存在
        - 如果都是 1，则被检元素很可能存在。

    - 优点：占用空间更少，申请一个 100w 个元素的位数组只占用 1000000Bit/8=125000Byte=125000/1024kb≈122kb 的空间。

    - 缺点：

        - 1.其返回的结果是概率性的

        - 2.删除操作非常困难：一般的直接不允许 remove 移除元素，因为那样的话会把相应的 k 个 bits 位置为 0，而其中很有可能有其他元素执行哈希计算之后也会对应该 bit 位，从而造成更多的误判！如果要删除元素，则使用 Counting Bloom Filter。

#### Counting Bloom Filter(计数布隆过滤器)

- 将布隆过滤器的bitmap更换成数组，当数组某位置被映射一次时就+1，当删除时就-1

#### Cuckoo Filter(布谷鸟过滤器)

- [《Cuckoo Filter：Better Than Bloom》](https://www.cs.cmu.edu/~dga/papers/cuckoo-conext2014.pdf)

- 空间利用率高于布隆：空间上大概能节省 40% 多。布谷鸟过滤器要求位图的长度必须是 2 的指数

- 支持删除操作

- 为啥要取名布谷鸟呢? 有个成语，「鸠占鹊巢」,布谷鸟也是,布谷鸟从来不自己筑巢。它将自己的蛋产在别人的巢里，让别人来帮忙孵化。待小布谷鸟破壳而出之后，因为布谷鸟的体型相对较大，它又将养母的其它孩子（还是蛋）从巢里挤走 —— 从高空摔下夭折了。

    - 一维数组结构，会有两个 hash 算法将新来的元素映射到数组的两个位置。如果两个位置中有一个位置为空，那么就可以将元素直接放进去。但是如果这两个位置都满了，它就不得不「鸠占鹊巢」，随机踢走一个，然后自己霸占了这个位置。

    - 布谷鸟哈希算法会帮这些受害者（被挤走的蛋）寻找其它的窝。因为每一个元素都可以放在两个位置，只要任意一个有空位置，就可以塞进去。所以这个伤心的被挤走的蛋会看看自己的另一个位置有没有空，如果空了，自己挪过去也就皆大欢喜了。但是如果这个位置也被别人占了呢？好，那么它会再来一次「鸠占鹊巢」，将受害者的角色转嫁给别人。然后这个新的受害者还会重复这个过程直到所有的蛋都找到了自己的巢为止。

    - 连续踢来踢去几百次还没有停下来，这时候会严重影响插入效率。这时候布谷鸟哈希会设置一个阈值，当连续占巢行为超出了某个阈值，就认为这个数组已经几乎满了。这时候就需要对它进行扩容，重新放置所有元素。

### 匹配查找

#### 穷举: O(nm)
```py
def find(str1, str2):
    len1, len2 = len(str1), len(str2)
    for i in range(len1 - len2 + 1):
        for j in range(len2):
            if str1[i + j] != str2[j]:
                break
            if j == len2 - 1:
                return i
    return -1


str1 = "abcdef"
str2 = "de"
print(find(str1, str2))
```

#### Boyer-Moore

- 最坏时间复杂度依然是O(nm), 但平均时间复杂度是: O(n)

![image](./imgs/algorithms/Boyer-Moore.avif)

```py
def find(str1, str2):
    len1, len2 = len(str1), len(str2)

    # 对比倒数第一个元素
    i = j = len2 - 1
    while i < len1:
        if str1[i] == str2[j]:
            # 从后向前对比
            if j > 0:
                i -= 1
                j -= 1
            else:
                return i
        # 步长为str2
        else:
            i += len2 - j

    return -1
```

#### kmp(Knuth-Morris-Pratt)

![image](./imgs/algorithms/kmp.avif)

- 时间复杂度: O(n+m)

- 失败函数: O(m)
```py
# 通过位图记录公共子序列
def kmp_fail(str2):
    len2 = len(str2)
    bitmap = [0] * len2
    i = 1
    j = 0
    while i < len2:
        if str2[i] == str2[j]:
            bitmap[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = bitmap[j - 1]
        else:
            i += 1
    return bitmap


str2 = "ded"
kmp_fail(str2)  # [0, 0, 1]
str2 = "dedee"
kmp_fail(str2)  # [0, 0, 1, 2, 0]
str2 = "abcabc"
kmp_fail(str2)  # [0, 0, 0, 1, 2, 3]
```

- 匹配查找函数
```py
def find(str1, str2):
    len1, len2 = len(str1), len(str2)
    # 获取位图
    bitmap = kmp_fail(str2)
    i = 0
    j = 0
    while i < len1:
        if str1[i] == str2[j]:
            if j == len2 - 1:
                return i - len2 + 1
            i += 1
            j += 1
        # 查看是否需要移动子序列
        elif j > 0:
            j = bitmap[j - 1]
        else:
            i += 1
    return -1


str1 = "abcaba,abcabb,abcabc"
str2 = "abcabc"
print(find(str1, str2)) # 14
```

### lcs(Longest Common Subsequence)最长公共子序列

![image](./imgs/algorithms/lcs.avif)

- 动态规划算法

```py
def f(str1, str2):
    len1, len2 = len(str1), len(str2)
    # 二维数组. 横是str2, 纵是str1
    array = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i-1] == str2[j-1]:
                array[i][j] = array[i-1][j-1] + 1
            else:
                array[i][j] = max(array[i][j-1], array[i-1][j])
    return array[len1][len2]


str1 = "abcdef"
str2 = "de"
print(f(str1, str2)) # 2
```

## Linked List(链表)

### Linked List(单向链表)

- 时间复杂度O(n)

实现list(列表)的所有方法, 除了`sort()`

<details><summary>代码实现</summary><p>

---
```py
# 文件: list.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 迭代器
class _ListIter():
    def __init__(self, node):
        self.node = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.node:
            data = self.node.data
            self.node = self.node.next
            return data
        else:
            raise StopIteration


class List:
    def __init__(self, data=None):
        self.head = Node(data)
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return _ListIter(self.head)

    def __repr__(self):
        str1 = '['
        for i in self:
            str1 += f'{i}, '
        str1 = str1.rstrip(', ')
        str1 += ']'
        return str1

    # List[0]
    def __getitem__(self, index):
        assert index >= 0 and index < len(self), 'out of range'
        for i, item in enumerate(self):
            if i == index:
                return item

    # List[0] = 10
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), 'out of range'
        node = self.head
        i = 0
        while node:
            if i == index:
                node.data = value
                return
            i += 1
            node = node.next

    def __mul__(self, n):
        new_link = self.copy()
        for _ in range(n-1):
            new_link.extend(self)
        return new_link

    def index(self, data):
        for index, item in enumerate(self):
            if item == data:
                return index

        raise ValueError("not search index data")

    def count(self, data):
        i = 0
        for item in self:
            if item == data:
                i += 1
        return i

    def _last(self):
        node = self.head
        while node.next:
            node = node.next
        return node

    def extend(self, link):
        new_link = link.copy()
        node = self._last()
        node.next = new_link.head

    def append(self, data):
        if self.head.data is None:
            self.head = Node(data)
            self.size = 1
        else:
            node = self._last()
            node.next = Node(data)
            self.size += 1

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return

        node = self.head
        prev = node
        while node:
            if node.data == data:
                prev.next = node.next
                return
            prev = node
            node = node.next

        raise ValueError("not search delete data")

    def pop(self, index=None):
        assert index >= 0 and index < len(self), 'out of range'
        if index is None:
            index = self.size - 1

        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data

        node = self.head
        i = 0
        prev = node
        while node:
            if i == index:
                prev.next = node.next
                return node.data
            i += 1
            prev = node
            node = node.next

    def insert(self, index, data):
        assert index >= 0 and index < len(self), 'out of range'
        node = self.head
        i = 0
        prev = node
        while node:
            if i == index:
                new_node = Node(data)
                new_node.next = node
                prev.next = new_node
                return
            i += 1
            prev = node
            node = node.next

    def copy(self):
        list = List()
        for item in self:
            list.append(item)
        return list

    def reverse(self):
        node = self.head
        next = self.head.next
        node.next = None
        while next:
            current = next
            next = next.next
            current.next = node
            node = current
        self.head = current
```
---

</p></details>

<details><summary>测试代码</summary><p>

---
```py
import pytest

# 导入上面的代码
from list import List


# 初始化
@pytest.fixture()
def list1():
    list = List()
    for i in range(3):
        list.append(i)
    yield list

def test_size(list1):
    assert 3 == len(list1)

def test_getitem(list1):
    assert 0 == list1[0]

    with pytest.raises(AssertionError, match="out of range"):
        assert 0 == list1[9]

def test_setitem(list1):
    list1[0] = 10
    assert 10 == list1[0]

    with pytest.raises(AssertionError, match="out of range"):
        list1[9] = 10

def test_index(list1):
    assert 1 == list1.index(1)

    with pytest.raises(ValueError, match="not search index data"):
        list1.index(9)

def test_count(list1):
    assert 1 == list1.count(1)
    # 不存在返回0
    assert 0 == list1.count(11)

def test_copy(list1):
    list2 = list1.copy()
    assert id(list2) != id(list1)

def test_iter(capsys, list1):
    def iter(list1):
        for i in list1:
            print(i)

    iter(list1)
    out, err = capsys.readouterr()
    assert out == '0\n1\n2\n'

def test_extend(list1):
    node = List()
    for i in range(3, 6):
        node.append(i)

    list1.extend(node)
    assert list1.__repr__() == '[0, 1, 2, 3, 4, 5]'

def test_remove(list1):
    list1.remove(1)
    assert list1.__repr__() == '[0, 2]'

    with pytest.raises(ValueError, match="not search delete data"):
        list1.remove(9)

def test_pop(list1):
    assert 1 == list1.pop(1)
    assert list1.__repr__() == '[0, 2]'

    with pytest.raises(AssertionError, match="out of range"):
        assert 1 == list1.pop(9)

def test_insert(list1):
    list1.insert(1, 11)
    assert list1.__repr__() == '[0, 11, 1, 2]'

    with pytest.raises(AssertionError, match="out of range"):
        list1.insert(9, 11)

def test_repr(list1):
    assert list1.__repr__() == '[0, 1, 2]'

def test_mul(list1):
    list2 = list1 * 2
    assert list2.__repr__() == '[0, 1, 2, 0, 1, 2]'

def test_reverse(list1):
    list1.reverse()
    assert list1.__repr__() == '[2, 1, 0]'
```
---

</p></details>

#### 单向链表归并排序

```py
def getmid(head):
    one = two = head
    if head is None:
        return one
    while two.next and two.next.next:
        one = one.next
        two = two.next.next
    return one


def sort(head):
    if head is None or head.next is None:
        return head
    mid = getmid(head)
    l = head
    r, mid.next = mid.next, None
    return merge(sort(l), sort(r))


def merge(l, r):
    node0 = Node(0)
    node = node0

    while l and r:
        if l.data > r.data:
            node.next = r
            r = r.next
        else:
            node.next = l
            l = l.next

    if l:
        node.next = l
    if r:
        node.next = r

    return node0.next

link1 = Linkedlist()
link1.add(3)
link1.add(2)
link1.add(5)
link1.add(1)
link1.add(6)

node = sort(link1.head)
while node:
    print(node.data)
    node = node.next
```

### DoublyList(双向链表)

<details><summary>代码实现</summary><p>

---
```py
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class _ListIter():
    def __init__(self, node):
        self.node = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.node:
            data = self.node.data
            self.node = self.node.next
            return data
        else:
            raise StopIteration


class Deque:
    def __init__(self, maxlen=-1):
        self.head = None
        self.tail = None
        self.maxlen = maxlen
        self.size = 0

    def __iter__(self):
        return _ListIter(self.head)

    def __repr__(self):
        str1 = '['
        for i in self:
            str1 += f'{i}, '
        str1 = str1.rstrip(', ')
        str1 += ']'
        return str1

    def _isFull(self):
        if self.maxlen == self.size:
            return True

    def _isEmpry(self):
        if self.head is None:
            return True

    def __len__(self):
        return self.size

    def append(self, data):
        if self._isEmpry():
            self.head = Node(data)
            self.tail = self.head
        else:
            if self._isFull():
                self.popleft()
            node = Node(data)
            self.tail.next, node.prev = node, self.tail
            self.tail = node
        self.size += 1

    def appendleft(self, data):
        if self._isEmpry():
            self.head = Node(data)
            self.tail = self.head
        else:
            if self._isFull():
                self.pop()
            node = Node(data)
            self.head.prev, node.next = node, self.head
            self.head = node
        self.size += 1

    def pop(self):
        assert not self._isEmpry(), 'pop from an empty deque'
        data = self.tail.data
        if self.size > 1:
            self.tail = self.tail.prev
            self.tail.next = None
        # 链表只剩1个的时候
        else:
            self.prev = self.head = None
        self.size -= 1
        return data

    def popleft(self):
        assert not self._isEmpry(), 'pop from an empty deque'
        data = self.head.data
        if self.size > 1:
            self.head = self.head.next
            self.head.prev = None
        # 链表只剩1个的时候
        else:
            self.prev = self.head = None
        self.size -= 1
        return data

    def copy(self):
        new_de = Deque()
        for i in self:
            new_de.append(i)
        return new_de

    def reverse(self):
        node = self.tail.prev
        self.head = self.tail
        while node:
            self.append(node.data)
            node = node.prev
        self.tail = node

    def extend(self, link):
        # 如果是合并自身, 就复制自身
        if link == self:
            link = link.copy()

        for i in link:
            self.append(i)

    def extendleft(self, link):
        # 如果是合并自身, 就复制自身
        if link == self:
            link = link.copy()

        for i in link:
            self.appendleft(i)

    def rotate(self, n=1):
        '''旋转'''
        for _ in range(n):
            self.appendleft(self.pop())

    def clear(self):
        self.tail = self.head = None
        self.size = 0
```
---

</p></details>

<details><summary>测试代码</summary><p>

---
```py
import pytest
# 导入上面的代码
from list import Deque


# 初始化
@pytest.fixture()
def queue():
    de = Deque()
    for i in range(3):
        de.append(i)

    for i in range(3):
        de.appendleft(i)
    yield de

def test_size(queue):
    assert 6 == len(queue)

def test_clear(queue):
    queue.clear()
    assert True == queue._isEmpry()

def test_pop_popleft(queue):
    for i in range(3):
        queue.popleft()
        queue.pop()
    assert True == queue._isEmpry()

def test_extend(queue):
    # 合并自身
    queue.extend(queue)
    assert queue.__repr__() == '[2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2]'

    # 合并其它链表
    de2 = Deque()
    for i in range(3, 6):
        de2.append(i)

    queue.extend(de2)
    assert queue.__repr__() == '[2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2, 3, 4, 5]'

def test_extendleft(queue):
    # 合并自身
    queue.extend(queue)
    assert queue.__repr__() == '[2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2]'

    # 合并其它链表
    de2 = Deque()
    for i in range(3, 6):
        de2.append(i)

    queue.extendleft(de2)
    assert queue.__repr__() == '[5, 4, 3, 2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2]'

def test_rotate(queue):
    de2 = queue
    queue.rotate(len(queue))
    assert de2 == queue

def test_reverse(queue):
    for _ in range(3):
        queue.popleft()
    queue.reverse()
    assert queue.__repr__() == '[2, 1, 0]'

def test_maxlen():
    queue = Deque(maxlen=6)
    for i in range(3):
        queue.append(i)

    for i in range(3):
        queue.appendleft(i)

    # 合并自身
    queue.extend(queue)
    assert queue.__repr__() == '[2, 1, 0, 0, 1, 2]'

    queue.extendleft(queue)
    assert queue.__repr__() == '[2, 1, 0, 0, 1, 2]'

    # 合并其它链表
    de2 = Deque()
    for i in range(3, 6):
        de2.append(i)

    queue.extend(de2)
    assert queue.__repr__() == '[0, 1, 2, 3, 4, 5]'

    queue.extendleft(de2)
    assert queue.__repr__() == '[5, 4, 3, 0, 1, 2]'
```
---

</p></details>

### CircularQueue(环形队列)

> FIFO(先入先出)

![image](./imgs/algorithms/Circular-queue.avif)

- 只需在双向链表的代码实现里, 做些修改

```py
# 保存key, value
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class CircularQueue(object):
    def __init__(self, maxsize=-1):
        self.head = None
        self.tail = self.head
        self.maxsize = maxsize
        self.qsize = 0

    def full(self):
        if self.maxsize == self.qsize:
            return True

    def empry(self):
        if self.head is None:
            return True

    # FI
    def put(self, key, value):
        '''入队'''
        if self.empry():
            self.head = Node(key, value)
            self.tail = self.head
        else:
            # 队列满了, 会自动出队
            if self.full():
                self.get()

            node = Node(key, value)
            self.tail.next, node.prev = node, self.tail
            self.tail = node

            self.tail.next = self.head
            self.head.prev = self.tail
        self.qsize += 1

    # FO
    def get(self):
        '''出队'''
        assert not self.empry(), 'Queue is empry'
        value = self.head.value
        if self.qsize > 1:
            self.head = self.head.next

            self.tail.next = self.head
            self.head.prev = self.tail
        # 链表只剩1个的时候
        else:
            self.prev = self.head = None
        self.qsize -= 1
        return value

    def __repr__(self):
        node = self.head
        str1 = '['
        for _ in range(self.qsize):
            str1 += f'{node.value}, '
            node = node.next
        str1 = str1.rstrip(', ')
        str1 += ']'
        return str1
```

#### 判断是否为环形队列

- 使用快慢双指针: 每次移动快指针都比慢指针快1

- 快指针要追上慢指针, 只需一次遍历, 因此时间复杂度为O(n)

```py
def check(cqueue):
    slow = fast = cqueue.head
    while fast.next:
        fast = fast.next.next
        slow = slow.next

        if id(fast) == id(slow):
            return True
    # 到头就返回False
    return False

if __name__ == '__main__':
    cqueue = CircularQueue()
    for i in range(3):
        cqueue.put(i, i)

    print(check(cqueue)) # True
```

#### LRU缓存

- 利用CircularQueue的FIFO特性, 实现LRU缓存

    - 字典的搜索复杂度为O(1), 适合作为缓存

    - 缓存命中时: 重新put(入队). 实现更新

    - 缓存满时:

        - 队列: get(出队)

        - 字典: 通过Node里的key值定位字典, 实现删除缓存项

```py
class LRUCache(object):
    def __init__(self, maxsize=16):
        # 缓存长度
        self.maxsize = maxsize
        self.cache = {}
        # 队列长度等于缓存长度
        self.queue = CircularQueue(maxsize)

    def full(self):
        return len(self.cache) >= self.maxsize

    def __call__(self, func):
        def wrapper(n):
            cachenode = self.cache.get(n)
            # 命中
            if cachenode is not None:
                self.queue.get()
                self.queue.put(cachenode)
                return cachenode.value
            # miss
            else:
                # 缓存满了, 就删除缓存项, 以及出队get()
                if self.full():
                    lru_node = self.queue.head

                    # key的目的是为了定位字典, 方便cache的删除
                    del self.cache[lru_node.key]

                value = func(n)
                # 如果队列长度满了, 会自动出队get()
                self.queue.put(n, value)
                self.cache[n] = Node(n, value)
                return value
        return wrapper


# 使用fib进行测试
@LRUCache(maxsize=16)
def fib(n):
    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr
    return curr


if __name__ == '__main__':
    for i in range(1, 32):
        print(fib(i))

# 缓存情况
# {1: 1: 1, 2: 2: 2, 3: 3: 3, 4: 4: 5, 5: 5: 8, 6: 6: 13, 7: 7: 21, 8: 8: 34, 9: 9: 55, 10: 10: 89, 11: 11: 144, 12: 12: 233, 13: 13: 377, 14: 14: 610, 15: 15: 987}

# {15: 15: 987, 16: 16: 1597, 17: 17: 2584, 18: 18: 4181, 19: 19: 6765, 20: 20: 10946, 21: 21: 17711, 22: 22: 28657, 23: 23: 46368, 24: 24: 75025, 25: 25: 121393, 26: 26: 196418, 27: 27: 317811, 28: 28: 514229, 29: 29: 832040, 30: 30: 1346269}
```

### skip list(跳表)

### Python 不用堆和树实现按优先级过期的 LRU 缓存: https://death.andgravity.com/lru-cache

### Blockchain(区块链)

## 缓存清除算法

- [ByteByteGo：8 大缓存清除策略](https://mp.weixin.qq.com/s/NfST0edfUthvKDZtzLQSwg)

- 缓存驱逐是从缓存中删除数据，以便在缓存容量达到极限时为新条目腾出空间的过程。这有时会由缓存失效触发，即从缓存中删除不再被视为有效或新鲜的数据。

![image](./imgs/algorithms/8大缓存清除算法.gif)

- LRU（最近最少使用）
    - LRU 驱逐策略首先删除最近访问次数最少的项目。这种方法的原理是，最近访问过的项目在不久的将来更有可能再次被访问。LRU 可以通过哈希表和双链表的组合来实现。

- MRU（最近使用）
    - 与 LRU 相反，MRU 算法首先删除最近使用的项目。在最近访问的项目不太可能很快再次被访问的情况下，这种策略非常有用。不过，由于 MRU 采用了与直觉相反的缓存管理方法，因此并不常用。


- SLRU（分段式 LRU）
    - SLRU 将高速缓存分为两段：缓存段和保护段。新项目最初被放入试用段。如果缓存段中的项目再次被访问，它就会被提升到保护段。从缓存段的 LRU 端开始驱逐，保护段中的项目会被赋予更高的优先级，以留在缓存中。这种方法旨在将 LRU 的优势与保护频繁访问项目的附加层结合起来。

- LFU（最不常用算法）
    - LFU 算法会驱逐访问频率最低的项目。与考虑访问时间的 LRU 不同，LFU 侧重于项目被访问的次数，因此更有利于长期重复访问的项目。LFU 的实现可能比较复杂，因为它需要跟踪访问次数，并有可能动态调整整个缓存。


- FIFO（先进先出）
    - FIFO 是最简单的缓存策略之一，缓存以类似队列的方式运行，先驱逐最旧的项目，而不管其访问模式或频率如何。虽然 FIFO 容易实现，但它并不考虑项目的实际使用情况，因此可能导致缓存性能不理想。

- TTL（生存时间）
    - TTL 并非严格意义上的驱逐算法，它是一种为每个缓存项设定特定生命周期的策略。当 TTL 过期时，该项目将被视为过时项目，并在下次访问缓存时被自动删除或标记为符合驱逐条件。TTL 可与其他驱逐策略结合使用，以管理缓存的新鲜度。

- 双层缓存
    - 在双层缓存策略中，第一层使用内存缓存，第二层使用分布式缓存。第一层通常保存经常使用的数据。

- RR（随机替换）
    - 随机替换算法随机选择一个缓存项并将其驱逐，为新项目腾出空间。这种方法实施起来也很简单，不需要跟踪访问模式或频率。不过，它的简单性也带来了代价，那就是可能纯属偶然地移除使用率高的项目。

## graph(图)

- [图介绍](https://www.section.io/engineering-education/graph-data-structure-python/)

- [10种常用的图算法直观可视化解释](https://cloud.tencent.com/developer/article/1692264)

![image](./imgs/algorithms/graph.avif)

```py
class Node:
    """结点"""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Edge:
    """边"""

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def __repr__(self):
        return self.src.name + "->" + self.dest.name


class WeightEdge(Edge):
    """权重边"""

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return self.src.name + "->" + str(self.weight) + "," + self.dest.name


class Digraph:
    """有向图"""

    def __init__(self):
        self.nodes = []
        # {0: [1, 2], 1: [2, 0], 2: [3, 4], 3: [5, 1], 4: [0], 5: []}
        self.edges = {}

    def addNode(self, node):
        self.nodes.append(node)
        self.edges[node] = []

    def addEdge(self, edge):
        self.edges[edge.src].append(edge.dest)

    def getEdge(self, node):
        return self.edges[node]

    def __repr__(self):
        result = ""
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result = src.name + "->" + dest.name + "\n"
        return result[:-1]


class Graph(Digraph):
    """无向图"""

    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.dest, edge.src)
        Digraph.addEdge(self, rev)


def printPath(path):
    """输入[0, 2, 3, 5]; 输出0->2->3->5"""
    result = ""
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += "->"

    return result


def dfs(graph, start, end, toPrint=False):
    def rec(graph, start, end, path, result, toPrint=False):
        path = path + [start]

        if toPrint:
            print(printPath(path))

        if start == end:
            return path

        for node in graph.getEdge(start):
            if node not in path:
                if result is None or len(path) < len(result):
                    newPath = rec(graph, node, end, path, result, toPrint)

                    if newPath:
                        result = newPath
        return result
    return rec(graph, start, end, [], None, toPrint)


def bfs(graph, start, end, toPrint=False):
    initPath = [start]
    pathQueue = [initPath]

    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print(printPath(tmpPath))

        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath

        for node in graph.getEdge(lastNode):
            if node not in tmpPath:
                newPath = tmpPath + [node]
                pathQueue.append(newPath)


def test_SP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))

    graph = Digraph()
    for i in nodes:
        graph.addNode(i)

    graph.addEdge(Edge(nodes[0], nodes[1]))
    graph.addEdge(Edge(nodes[1], nodes[2]))
    graph.addEdge(Edge(nodes[2], nodes[3]))
    graph.addEdge(Edge(nodes[2], nodes[4]))
    graph.addEdge(Edge(nodes[3], nodes[5]))
    graph.addEdge(Edge(nodes[0], nodes[2]))
    graph.addEdge(Edge(nodes[1], nodes[0]))
    graph.addEdge(Edge(nodes[3], nodes[1]))
    graph.addEdge(Edge(nodes[4], nodes[0]))

    sp = dfs(graph, nodes[0], nodes[5], toPrint=True)
    print(printPath(sp))

    print()

    sp = bfs(graph, nodes[0], nodes[5], toPrint=True)
    print(printPath(sp))


if __name__ == '__main__':
    test_SP()
```

### 遍历有环图

![image](./imgs/algorithms/graph1.avif)

| 节点 | 1 | 2 | 3 | 4 | 5 |
|------|---|---|---|---|---|
| 1    | 0 | 1 | 0 | 1 | 1 |
| 2    | 1 | 0 | 1 | 0 | 0 |
| 3    | 0 | 1 | 0 | 0 | 0 |
| 4    | 1 | 0 | 0 | 0 | 1 |
| 5    | 1 | 0 | 0 | 1 | 0 |

- dfs

```py
def dfs(graph, point):
    def rec(n, sum):
        bitmap[n] = 1
        print(point[n], end='')
        sum += 1
        if sum == len(bitmap):
            return
        for i in range(len(graph)):
            if graph[n][i] == 1 and bitmap[i] == 0:
                rec(i, sum)

    bitmap = [0 for _ in range(len(graph))]
    rec(0, 0)
```

- bfs
```py
from collections import deque


def bfs(graph, point):
    bitmap = [0 for _ in range(len(graph))]
    n = 0
    queue = deque([n])
    bitmap[n] = 1

    while queue:
        head = queue.popleft()
        print(point[head], end="")
        for i in range(len(graph)):
            if graph[head][i] == 1 and bitmap[i] == 0:
                queue.append(i)
                bitmap[i] = 1


if __name__ == "__main__":
    graph = [
        [0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0],
    ]
    point = [1, 2, 3, 4, 5]

    dfs(graph, point) # 12345
    bfs(graph, point) # 12453
```

### 生成树

#### Prim算法

#### Kruskal算法

### Dijkstra最短路径算法

### 全排列

- 输入输出

    输入
    ```
    [1, 2, 3]
    ```
    输出
    ```
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 1, 2]
    [3, 2, 1]
    ```

- dfs
```py
def dfs(list1):
    def iter(i, list2):
        if len(list2) == len(list1):
            print(list2)
        for i in list1:
            if i not in list2:
                list2.append(i)
                iter(i+1, list2)
                list2.pop()
    iter(0, [])

list1 = [1, 2, 3]
dfs(list1)
```

### 走出迷宫

### 图的应用

- [pagerank](https://en.wikipedia.org/wiki/PageRank)

    > 为网页的每个链接分配权重, 测量网页内部连接的相对重要性

## tree(树)

![image](./imgs/algorithms/bigO_link.avif)
![image](./imgs/algorithms/tree_benchmark.avif)

### 树相关的基础概念：

- [爱可生开源社区：第15期：索引设计（索引组织方式 B+ 树）](https://mp.weixin.qq.com/s?__biz=MzU2NzgwMTg0MA==&mid=2247490020&idx=1&sn=f786f4f21595d16b4e55d46cd115d696&chksm=fc96fb7bcbe1726d1b37b154abb07fa66d9f6e05a9b29be626b447143ae4be59f61239739c3c&cur_album_id=1338281900976472064&scene=189#wechat_redirect)

- binary tree(二叉树)

    ![image](./imgs/algorithms/binary_tree.avif)

    - 根节点：6 为根节点，根节点没有父节点，有儿子节点，一般叫做 ROOT 节点；

    - 儿子节点：8 和 4 是 6 的儿子节点，4 是左儿子，8 是右儿子；

    - 父节点：6 是 4 和 8 的父节点，父节点是儿子节点的上层节点；

    - 叶子节点：4 和 5 是叶子节点，叶子节点指的是除根节点外没有儿子的节点；

    - 兄弟节点：8 和 4 互为兄弟节点，因为有共同的父亲 6。10，9，7 三个节点没有兄弟，都只有一个儿子；

    - 层数：一棵树的节点层数。这颗二叉树层数为 6；

    - 高度：自下向上遍历，从叶子节点遍历到根节点所需要的节点数量。叶子节点 5 到根节点遍历 7，9，10，8，6，这棵树的高度为 5；

    - 深度：自上而下遍历，从根节点到叶子节点遍历所需要的节点数量，同样，这棵树的深度也是 5；

    - 高度和深度一般以 0 开始计算，当然也有按照从 1 开始计算的；

    - 平衡因子：某节点的左子树与右子树深度的差值，一般结果为绝对值。

    - 如果任何一个子树不存在，按照 0 处理。比如节点 10 的平衡因子就是 3；

- 平衡二叉树（AVL）

    ![image](./imgs/algorithms/avl_tree.avif)

    - 1.所有左子树的节点都小于其对应的父节点（4，5，6）<（7）；（4）<（5）；（8）< （9）；
    - 2.所有右子树上的节点都大于其对应的父节点（8，9，10）>（7）；（6）>（5）；（10）>（9）；
    - 3.每个节点的平衡因子差值绝对值 <=1；

    - 每个节点都符合以上三个特征。满足这样条件的树叫平衡二叉树（AVL）树。

    - 问：那再次查找节点 5，需要遍历多少次呢？

        - 由于数据是按照顺序组织的，那查找起来非常快，从上往下找：7-5，只需要在左子树上查找，也就是遍历 2 次就找到了 5。
        - 假设要找到叶子节点 10，只需要在右子树上查找，那也最多需要 3 次，7-9-10。
        - 也就说 AVL 树在查找方面性能很好，最坏的情况是找到一个节点需要消耗的次数也就是树的层数， 复杂度为 O(logN)

    - 假设现在有 31 个节点，用 AVL 树表示如图
        ![image](./imgs/algorithms/avl_tree-31个节点.avif)
        - 一棵高度为 4 的 AVL 树，有 5 层共 31 个节点，橙色是 ROOT 节点，蓝色是叶子节点。对 AVL 树的查找来看起来已经很完美了，能不能再优化下？比如，能否把这个节点里存放的 KEY 增加？能否减少树的总层数？那减少纵深只能从横向来想办法，这时候可以考虑用多叉树。

- B 树

    - B 树是一种多叉的 AVL 树。B-Tree 减少了 AVL 数的高度，增加了每个节点的 KEY 数量。

    - B 树的特性：（m 为阶数：结点的孩子个数最大值）
        - 1.树中每个节点最多含有 m 个孩子节点 (m>=2)；
        - 2.除根节点和叶子结点外，其他节点的孩子数量 >=ceil(m / 2)；
        - 3.若根节点不是叶子结点，最少有两个孩子
            - 特殊情况：没有孩子的根结点，即根结点为叶子结点，整棵树只有一个根节点；
        - 4.每个非叶子结点中包含有 n 个关键字信息：(n，P0，K1，P1，K2，P2，......，Kn，Pn) 其中：

            - Ki (i=1...n) 为关键字，且关键字按顺序升序排序 K(i-1)< Ki
            - Pi 为指向儿子节点的指针，且指针 P(i-1) 指向的儿子节点里所有关键字均小于 Ki，但都大于 K(i-1)
            - 关键字的个数 n 必须满足：[ceil(m / 2)-1]<= n <= m-1
            - 如果一个结点有 n 个关键字，那么该结点有 n+1 个分支。这 n+1 个关键字按照递增顺序排列
            - 所有叶子结点都出现在同一层，是所有遍历的终点位置

    - 把上面的个31节点的avl树变为b树

        ![image](./imgs/algorithms/b_tree.avif)

        - 一棵 4 阶 B 树，总共有 11 个节点，节点数比avl树 少了 20 个；层数为 3，比avl树 少了两层
        - 实际应用中，每个最小单元不是 KEY，而一般是按照块（BLOCK）来算：
            - 磁盘文件系统 EXT4 每块 4KB
            - PostgreSQL 是 8KB
            - MySQL InnoDB 是 16KB
            - MySQL NDB  是 32KB

        - 这颗b树每个节点的基本单元是一个磁盘块（BLOCK，默认 4KB），根节点含有一个键值，其他节点含有 3 个键值，每个磁盘块包含对应的键值与数据。

            - 比如现在要读取 KEY 为 31 的记录：
                - 1.先找到根节点磁盘块（1），读入内存。（第一次IO）
                - 2.关键字 31 大于区间（16，），根据指针 P2 找到磁盘块 3，读入内存（第二次 IO）
                - 3.31 大于区间（20，24，28），根据指针 P4 读取磁盘块 11（第三次 IO），在磁盘块 11 中找到 KEY 为 31 的记录，返回结果。
                - 这期间有三次磁盘 IO 的读取。可以明确看到，B 树相对于 AVL 树，减少了树的节点数与树的深度，减少了磁盘 IO。

            - 看到这里其实有一个问题，三次 IO，前两次 IO 其实从磁盘读取了不必要的数据，因为只用比较 KEY，所以非叶子节点对应的 DATA 完全没有必要，如果 DATA 很大，那完全是浪费内存资源。考虑下能否把非叶子节点的 DATA 拿掉？

- B+ 树

    - B+ 树是对 B 树的一个小升级。大部分数据库的索引都是基于 B+ 树存储的。

    - B+ 树最大的几个特点：
        - 1.非叶子节点只保留 KEY，放弃 DATA；
        - 2.KEY 和 DATA一起，在叶子节点，并且保存为一个有序链表（正序，反序，或者双向）；
        - 3.B+ 树的查找与 B 树不同，当某个结点的 KEY 与所查的 KEY 相等时，并不停止查找，而是沿着这个 KEY 左边的指针向下，一直查到该关键字所在的叶子结点为止。

    - 把上面的B 树做一个调整，变为以下 B+ 树
        ![image](./imgs/algorithms/b+tree.avif)
        - 非叶子节点不再包含除了主键外的数据，数据全部放在叶子节点，并且所有叶子节点存放在一个单向链表里，当然也可以双向链表。
        - B+ 树同时具有平衡多叉树和链表的优点，即可兼顾 B 树对范围查找的高效，又可兼顾链表随机写入的高效， 这也是大部分数据库都用 B+ 树来存储索引的原因。

### binary tree(二叉树)

- 列表实现
```py
def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


if __name__ == '__main__':
    r = BinaryTree(0)
    insertLeft(r, 1)
    insertRight(r, 2)
    insertLeft(r, 3)
    insertRight(r, 4)
    print(r)
```
输出
```
[0, [3, [1, [], []], []], [4, [], [2, [], []]]]
```

#### 遍历树

> LIFO

```py
class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.right = TreeNode(3)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(6)
tree.right.left.left = TreeNode(7)
tree.right.left.right = TreeNode(8)
```

![image](./imgs/algorithms/Preorder-Traversal.avif)

![image](./imgs/algorithms/Inorder-Traversal.avif)

![image](./imgs/algorithms/Postorder-Traversal.avif)

##### dfs

```py
def preorder(tree):
    """先序遍历"""
    if tree:
        print(tree.data, end="")
        preorder(tree.left)
        preorder(tree.right)


def inorder(tree):
    """中序遍历"""
    if tree:
        inorder(tree.left)
        print(tree.data, end="")
        inorder(tree.right)


def postorder(tree):
    """后序遍历"""
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.data, end="")


preorder(tree); print()  # 12435786
inorder(tree); print()   # 42175836
postorder(tree); print() # 42785631
```

- 前序的变种, eulerorder(欧拉遍历)

```py
def eulerorder(tree, parent):
    if not tree:
        return

    print(tree.data, end="")
    eulerorder(tree.left, tree)
    eulerorder(tree.right, tree)
    # 比前序遍历多了parent
    if parent:
        print(parent.data, end="")


eulerorder(tree, None) # 124213575853631
```

- stack实现:
```py
def preorder(tree):
    stack = []
    stack.append(tree)
    while len(stack) > 0:
        tail = stack.pop()
        print(tail.data, end='')
        if tail.right: stack.append(tail.right)
        if tail.left: stack.append(tail.left)


def inorder(tree):
    stack = []
    tail = tree
    while stack or tail:
        if tail:
            stack.append(tail)
            tail = tail.left
        else:
            tail = stack.pop()
            print(tail.data, end="")
            tail = tail.right


def postorder(tree):
    stack = []
    out = []
    stack.append(tree)
    while stack:
        tail = stack.pop()
        out.append(tail.data)
        if tail.left: stack.append(tail.left)
        if tail.right: stack.append(tail.right)

    while out:
        print(out.pop(), end="")
```

- 遍历所有结点的路径
```py
def dfs(tree):
    res = []
    str1 = ''
    def iter(tree, res, str1):
        if not tree:
            return
        else:
            str1 += str(tree.data)
            iter(tree.left, res, str1)
            iter(tree.right, res, str1)
        if not tree.left and not tree.right:
            res.append(str1)
    iter(tree, res, str1)
    return res

print(dfs(tree)) # ['124', '1357', '1358', '136']
```

##### bfs
```py
from collections import deque

def bfs(tree):
    if not tree:
        return
    queue = deque([tree])
    while queue:
        head = queue.popleft()
        print(head.data, end='')
        if head.left: queue.append(head.left)
        if head.right: queue.append(head.right)

bfs(tree) # 12345678
```

#### 只遍历左子树

- dfs
```py
def leftView(tree, depth=1, last_depth=0):
    if not tree:
        return last_depth

    if last_depth < depth:
        last_depth = depth
        print(tree.data, end="")

    last_depth = leftView(tree.left, depth + 1, last_depth)
    last_depth = leftView(tree.right, depth + 1, last_depth)
    return last_depth

leftView(tree)
```
- 字典实现
```py
def leftView(tree, depth=1, dict1={}):
    if not tree:
        return

    if depth not in dict1:
        dict1[depth] = tree.data
        print(tree.data, end="")

    leftView(tree.left, depth + 1, dict1)
    leftView(tree.right, depth + 1, dict1)


leftView(tree)
```

- bfs
```py
def leftView(tree):
    if not tree:
        return

    queue = deque()
    queue.append(tree)

    while queue:
        i = 0
        length = len(queue)

        while i < length:
            head = queue.popleft()
            i += 1

            # 第一个入队的是左子树
            if i == 1:
                print(head.data, end="")

            if head.left: queue.append(head.left)
            if head.right: queue.append(head.right)

leftView(tree)
```

#### 反转树(invert)

```py
def swap(tree):
    if not tree:
        return

    tree.left, tree.right = tree.right, tree.left
```


- dfs:

- 递归
```py
def invert(tree):
    if not tree:
        return

    invert(tree.left)
    invert(tree.right)
    swap(tree)
```
- stack实现
```py
def invert(tree):
    if not tree:
        return

    stack = []
    stack.append(tree)

    while stack:
        tail = stack.pop()
        swap(tail)
        if tail.right: stack.append(tail.right)
        if tail.left: stack.append(tail.left)
```

- bfs:

- 迭代
```py
def invert(tree):
    if not tree:
        return

    swap(tree)
    invert(tree.left)
    invert(tree.right)
```

- 队列实现
```py
from collections import deque

def invert(root):
    if not root:
        return

    queue = deque()
    queue.append(root)

    while queue:
        head = queue.popleft()
        tree.left, tree.right = tree.right, tree.left

        swap(head)

        if head.left: queue.append(head.left)
        if head.right: queue.append(head.right)
```

#### 计算树的高度

##### dfs
- 最大高度

```py
def maxDepth(tree):
    if tree is None:
        return 0
    return 1 + max(maxDepth(tree.left), maxDepth(tree.right))

print(maxDepth(tree))
```

- 最小高度
```py
def minDepth(root):
    if not root:
        return 0

    left = minDepth(root.left)
    right = minDepth(root.right)

    if not root.left: return right + 1
    if not root.right: return left + 1

    return min(left, right) + 1

print(minDepth(tree))
```

##### bfs
- 最大高度

```py
from collections import deque

def maxDepth(root):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    height = 0

    while queue:
        length = len(queue)

        while length > 0:
            head = queue.popleft()
            if head.left: queue.append(head.left)
            if head.right: queue.append(head.right)
            length -= 1

        height += 1

    return height

print(maxDepth(tree)) # 4
```

- 最小高度
```py
from collections import deque

def minDepth(root):
    if not root:
        return 0

    queue = deque()
    queue.append((root, 1))

    while queue:
        head, depth = queue.popleft()

        if not head.left and not head.right:
            return depth

        if head.left: queue.append((head.left, depth + 1))
        if head.right: queue.append((head.right, depth + 1))

print(minDepth(tree))
```

#### 判断是否为平衡二叉树(balanced binary tree)

> 左右结点高度不能超过1

![image](./imgs/algorithms/balanced-binary-tree.avif)

```py
def dfs(tree, isBalanced=True):
    if not tree or not isBalanced:
        return 0, isBalanced

    # 左树高度
    left_depth, isBalanced = dfs(tree.left, isBalanced)
    # 左树高度
    right_depth, isBalanced = dfs(tree.right, isBalanced)

    if abs(left_depth - right_depth) > 1:
        isBalanced = False

    return max(left_depth, right_depth) + 1, isBalanced


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.right = TreeNode(2)

print(dfs(tree)) # (3, True)
```

#### 判断是否为对称二叉树(symmetric binary tree)

![image](./imgs/algorithms/symmetric-binary-tree.avif)

- dfs
```py
def dfs(tree):

    def rec(left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        # 判断值是否相等
        return left.data == right.data\
                and rec(left.left, right.right)\
                and rec(left.right, right.left)

    return rec(tree.left, tree.right)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.right = TreeNode(2)
tree.right.right = TreeNode(3)

print(dfs(tree))
```

- bfs
```py
def bfs(tree):
    if not tree:
        return True
    stack = []
    stack.append(tree.left)
    stack.append(tree.right)
    while stack:
        right = stack.pop()
        left = stack.pop()

        # return True
        if not right and not left:
            return True

        # 只存在一个结点的情况下
        elif not right or not left:
            return False

        # 判断值是否相等
        if right.data != left.data:
            return False

        # 左右结点都存在的情况下
        if right.left or left.left or right.right or left.right:
            stack.append(right.left)
            stack.append(left.right)
            stack.append(right.right)
            stack.append(left.left)
    return True


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.right = TreeNode(2)
tree.right.right = TreeNode(3)

print(bfs(tree))
```

#### 判断是否为堂兄弟结点
```py

```

### full binary tree

> 每个结点要么有两个结点, 要么两个结点都是None

#### 判断是否为full binary tree
```py
def isFullTree(root):

    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return (isFullTree(root.left) and isFullTree(root.right))

    return False


root = Node(1)
root.right = Node(3)
root.left = Node(2)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
print(isFullTree(root))
```

### 完全二叉树(complete binary tree)

> 树向左结点倾斜的

#### 判断是否为完全二叉树

```py
# 结点总数
def count_nodes(root):
    if root is None:
        return 0
    return (1 + count_nodes(root.left) + count_nodes(root.right))


def is_complete(root, index, counts):
    if root is None:
        return True

    if index >= counts:
        return False

    return (is_complete(root.left, 2 * index + 1, counts) and
            is_complete(root.right, 2 * index + 2, counts))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(is_complete(root, 0, count_nodes(root)))
```

### 二叉搜索树(binary search tree)

> 左结点小于根结点; 右结点大于根结点

- 递归实现
```py
def insert(tree, data):
    if not tree:
        return TreeNode(data)

    if data < tree.data:
        tree.left = insert(tree.left, data)
    else:
        tree.right = insert(tree.right, data)

    return tree
```

- 循环实现
```py
def insert(tree, data):
    curr = tree
    parent = None

    if not tree:
        return TreeNode(data)

    while curr:
        parent = curr
        if data < curr.data:
            curr = curr.left
        else:
            curr = curr.right

    if data < parent.data:
        parent.left = TreeNode(data)
    else:
        parent.right = TreeNode(data)
    return tree
```

#### 输入两个值, 计算他们之间的值

```py
class dfs():
    def f(self, tree, left, right):
        self.sum = 0

        def rec(tree):
            if tree:
                # 小于left值就跳过
                if tree.data < left:
                    rec(tree.right)
                # 大于right值就跳过
                elif tree.data > right:
                    rec(tree.left)
                else:
                    # 相加
                    self.sum += tree.data
                    rec(tree.right)
                    rec(tree.left)
        rec(tree)
        return self.sum

func = dfs()
print(func.f(tree, 2, 10))
```

#### 判断是否为二叉搜索树

```py
class SearchTree(object):
    def __init__(self, small, large):
        self.small = small
        self.large = large

    def search(self, root, small, large):
        if root is None:
            return True

        # 左结点必须小于root, 右结点必须大于root
        if self.small >= root.val or self.large <= root.val:
            return False

        # 递归自身
        return self.search(root.left, self.small, root.val)

    def excute(self, root):
        return self.search(root, self.small, self.large)


class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Tree(12)
b = Tree(5)
c = Tree(18)
d = Tree(2)
e = Tree(9)
f = Tree(15)
g = Tree(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

m = SearchTree(a.val, c.val)
print(m.excute(c))
print(m.excute(f))
```
输出
```
False
True
```

### 自平衡二叉搜索树(AVL tree)
### 红黑树
### 字典树(trie tree)
### 2-3树
### B树
### B+树
B+ Tree 的一些变体CSB+ Tree、PB+ Tree、Bw Tree 以及吸收了 B+ Tree 和 Radix Tree 优点的 MassTree 等等
### B-link树
### R树
### LSMTree(日志结构合并树)

## 递归(rec)

- python递归深度
```py
import sys

# 查看最大递归深度
print(sys.getrecursionlimit()) # 3000. 也就是2 ^ 3000次方

# 设置最大递归深度为10000
sys.getrecursionlimit(10000)
```

### 阶乘

```py
def factorial(n):
    if n == 0:
        return 1

    return factorial(n - 1) * n


print(factorial(4)) # 24
```

### 反转列表
```py
def reverse(list1, left, right):
    if left < right - 1:
        list1[left], list1[right] = list1[right], list1[left]
        reverse(list1, left + 1, right - 1)


list1 = [1, 2, 3]
reverse(list1, 0, len(list1) - 1)
print(list1) # [3, 2, 1]
```

### 累加列表里的元素
- O(n)
```py
def list_sum(list1, n):
    if n == 0:
        return 0

    return list_sum(list1, n - 1) + list1[n - 1]


list1 = [1, 2, 3]
print(list_sum(list1, len(list1))) # 6
```

- O(n)
```py
def list_sum1(list1, left, right):
    if left == right - 1:
        return list1[left]

    mid = (left + right) // 2
    return list_sum1(list1, left, mid) + list_sum1(list1, mid, right)

list1 = [1, 2, 3]
print(list_sum1(list1, 0, len(list1))) # 6
```

### 次方
- O(n)
```py
def power(x, n):
    if n == 0:
        return 1

    return power(x, n - 1) * x


print(power(2, 8)) # 256
```

- O(log n)
```py
def power1(x, n):
    if n == 0:
        return 1
    else:
        y = power1(x, n//2)
        result = y ** 2
        # n 为单数时, 多乘一次x
        if n % 2 == 1:
            result *= x
        return result


print(power1(2, 7)) # 128
```

### 汉诺塔

- 2的n次方-1
```py
# 方法1
def iter(n):
    if n == 1:
        return 1
    return iter(n-1) * 2 + 1

# 方法2
def iter1(n):
    if n == 1:
        return 2
    return iter1(n-1) * 2

print(iter1(4) - 1)
```

### 反转正整数

```py
def iter(n):
    print(int(n % 10))
    if n > 10:
        iter(n / 10)

# 输入一个正整数
iter(1234)
```

### 集合划分

```py
def f(n, m):
    if m==1 or n==1:
        return 1
    return f(n-1, m-1) + f(n-1, m)
```

### 整数划分

- 假设num是4, maxnum也是4可以划分为5种: 4+0, 1+3, 2+2, 2+1+1, 1+1+1+1

```py
def func(num, maxnum):
    if num < 1 and maxnum < 1:
        return 0
    if num == 1 or maxnum == 1:
        return 1

    if num < maxnum:
        return func(num, num)
    if num == maxnum:
        return func(num, maxnum-1) + 1
    return func(num - maxnum, maxnum) + func(num, maxnum-1)

print(func(4, 4))
```

### 最大公约数, 最小公倍数

- 最大公约数

    - 60 = 2 * 2 * 2 * 3

    - 24 = 2 * 2 * 3 * 5

    - gcd(60, 24) = 2 * 2 * 3 = 12

    - gcd(60, 24) -> gcd(24, 12) -> gcd(12, 0) = 12

```py
def gcd(m, n):
    yu = m % n
    if yu == 0:
        return n

    return gcd(n, yu)


print(gcd(60, 24))
```

- 最小公倍数

    - 60 = 2 * 2 * 2 * 3

    - 24 = 2 * 2 * 3 * 5

    - lcm(60, 24) = (2 * 2 * 3) * 2 * 5 = 120

        - (公共质因子的积)

$$
lcm(m, n) = \frac {m \times n}{gcd(m, n)}
$$

```py
def lcm(m, n):
    return m * n / gcd(m, n)


print(lcm(60, 24)) # 120.0
```



## 分治算法

### 找到出现最多次数的值

- 二分搜索:时间复杂度O(n log n), 递归需要空间复杂度O(n log n)
```py
def func(list1):
    def rec(low, high):
        if low == high:
            return list1[low]
        mid = low + (high-low) // 2
        head = rec(low, mid)
        tail = rec(mid+1, high)

        if head == tail:
            return tail
        head_count = sum(1 for i in range(low, high+1) if list1[i] == head)
        tail_count = sum(1 for i in range(low, high+1) if list1[i] == tail)
        return head if head_count > tail_count else tail
    return rec(0, len(list1)-1)


list1 = [1, 2, 2, 1, 1]
print(func(list1))
```

- 字典实现:时间复杂度:O(n), 空间复杂度:O(n)
```py
def func(list1):
    dict1 = {}
    for i in list1:
        dict1[i] = dict1.get(i, 0) + 1
    return max(dict1.keys(), key=dict1.get)
```

- 抵消: 时间复杂度O(n), 空间复杂度O(1)
```py
def func(list1):
    times = 1
    res = list1[0]
    length = len(list1)

    for i in range(1, length):
        if times == 0:
            times += 1
        elif list1[i] == res:
            times += 1
        else:
            res = list1[i]
            times -= 1
    return res
```

## 动态规划

- [无聊的闪客：你管这破玩意叫动态规划](https://mp.weixin.qq.com/s/_XS3nd-ipnkhYk_5X_ppSQ)

### UnlyNum(丑数)

```py
def unlyNum(n):
    dp = [0] * n
    dp[0] = 1
    p2 = p3 = p5 = 0
    for i in range(1, n):
        dp[i] = min(2*dp[p2], 3*dp[p3], 5*dp[p5])
        if dp[i] == 2*dp[p2]:
            p2 += 1
        if dp[i] == 3*dp[p3]:
            p3 += 1
        if dp[i] == 5*dp[p5]:
            p5 += 1

    return dp[-1]


print(unlyNum(8))
```

### 进制转换
```py
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]


# 16进制
print(toStr(65535, 16))

# 2进制
print(toStr(255, 2))
```

- stack实现
```py
from queue import LifoQueue

def toStr(n, base):
    stack = LifoQueue()
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            stack.put(convertString[n])
        else:
            stack.put(convertString[n % base])
        n = n // base
    res = ""
    while not stack.empty():
        res = res + str(stack.get())
    return res

print(toStr(65535, 16))
print(toStr(255, 2))
```

### 最少硬币找零

- 循环
```py
def coin(list1, n):
    list2 = [0] * (n + 1)

    def f(list1, n, list2):
        for i in range(n + 1):
            coinCount = i
            for j in [c for c in list1 if c <= i]:
                if list2[i - j] + 1 < coinCount:
                    coinCount = list2[i - j] + 1
            list2[i] = coinCount
        return list2[n]
    return f(list1, n, list2)


print(coin([1, 5, 10, 20, 50, 100], 106))
```

- 递归
```py
def coin(list1, n):
    list2 = [0] * (n + 1)

    def f(list1, n, list2):
        if n in list1:
            list2[n] = 1
            return 1
        elif list2[n] > 0:
            return list2[n]
        else:
            minCoins = n
            for i in [c for c in list1 if c <= n]:
                numCoins = 1 + f(list1, n - i, list2)
                if numCoins < minCoins:
                    minCoins = numCoins
                    list2[n] = minCoins
        return minCoins

    return f(list1, n, list2)


print(coin([1, 5, 10, 20, 50, 100], 106))
```

### 完全背包问题

- 二维数组

```py
weight = [1, 3, 2, 5]
value = [200, 240, 140, 150]
max_weight = 5


def bag(weight, value, max_weight):
    weight.insert(0, 0)
    value.insert(0, 0)
    weight_length = len(weight)

    res = []
    for i in range(weight_length):
        res.append([0] * (max_weight + 1))

    for i in range(1, weight_length):
        for j in range(1, max_weight + 1):
            res[i][j] = res[i - 1][j]
            if j >= weight[i]:
                res[i][j] = max(res[i - 1][j], res[i - 1][j - weight[i]] + value[i])
    return res[weight_length - 1][max_weight]


print(bag(weight, value, max_weight)) # 440
```

## 贪心算法

贪心算法本质是: 每一步都做出, 当前情况下的最优选择(局部最优). 但不一定能得出全局最优

### 背包问题

| 商品 | 价值 | 重量 | 性价比 |
|------|------|------|--------|
| A    | 175  | 10   | 17.5   |
| B    | 90   | 9    | 10     |
| C    | 20   | 4    | 5      |
| D    | 50   | 2    | 25     |
| E    | 10   | 1    | 10     |
| F    | 200  | 20   | 10     |

```py
class Item:
    '''商品'''
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    # [<A:175, 10>]
    def __repr__(self):
        return '<' + self.name + ':' + str(self.value) + ', ' + str(self.weight) + '>'


class Select:
    '''贪心算法, 选择函数'''
    def value(item):
        return item.value

    def weight(item):
        return item.weight

    def desity(item):
        ''' 选择性价比 '''
        return item.value / item.weight


def builditems():
    ''' 生成数据 '''
    names = list("ABCDE")
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items = []
    for i in range(len(names)):
        items.append(Item(names[i], values[i], weights[i]))
    # [<A:175, 10>, <B:90, 9>, <C:20, 4>, <D:50, 2>, <E:10, 1>]
    return items


def greedy(items, maxWeight, func):
    '''数据, 背包的重量, 选择函数'''
    itemsCopy = sorted(items, key=func, reverse=True)
    res = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if total_weight + itemsCopy[i].weight <= maxWeight:
            res.append(itemsCopy[i])
            total_value += itemsCopy[i].value
            total_weight += itemsCopy[i].weight
    print('选择顺序:', res)
    print('最后背包的重量', total_weight)
    print('总价值', total_value)
    print()
    return (res, total_value)


if __name__ == '__main__':
    items = builditems()
    greedy(items, 20, Select.value)
    greedy(items, 20, Select.weight)
    greedy(items, 20, Select.desity)
```
输出: 选择性价比, 反而没有选择价值, 选择重量更优
```
选择顺序: [<A:175, 10>, <B:90, 9>, <E:10, 1>]
最后背包的重量 20.0
总价值 275.0

选择顺序: [<A:175, 10>, <B:90, 9>, <E:10, 1>]
最后背包的重量 20.0
总价值 275.0

选择顺序: [<D:50, 2>, <A:175, 10>, <E:10, 1>, <C:20, 4>]
最后背包的重量 17.0
总价值 255.0
```

### 钱币找零

- 从面值最大的钱币开始选

```py
# 数量
count = [4, 1, 2, 1, 1, 3, 5]

# 面值
value = [1, 2, 5, 10, 20, 50, 100]

# 钱
money = 234

def f(count, value, money):
    # 次数
    res = 0
    list1 = []
    # 从面值最大的钱币开始选
    for i in range(len(value)-1, -1, -1):
        num = min(int(money/value[i]), count[i])
        money -= num * value[i]
        res += num
        for j in range(num):
            list1.append(value[i])

    if money == 0:
        return res, list1
    else:
        return -1

print(f(count, value, money)) # (7, [100, 100, 20, 10, 2, 1, 1])
```
### 任务调度
```py
# 每个任务工作的时间
time = [30, 26, 10, 35]

# 机器的数量
num = 3


def f(time, num):
    tmp = [0] * num
    if len(time) < num:
        return max(time)
    else:
        time.sort(reverse=True)
        # 优先分配时间最长的任务
        tmp = time[:num]
        for i in time[num:]:
            # 获取最先完成的任务机器
            minx = tmp.index(min(tmp))
            tmp[minx] += i
    return max(tmp)


print(f(time, num)) # 36
```

### 活动安排
```py
# 每个活动的时间
time = [(3, 5), (1, 4), (5, 7), (0, 6), (6, 10), (8, 11), (12, 14)]


def f(time):
    res = []

    # 选择结束时间最早的活动
    time.sort(key=lambda x: x[1])
    res.append(time[0])
    for i in time[1:]:
        # 活动的开始时间, 必须大于上一个活动的结束时间
        if i[0] >= res[-1][1]:
            res.append(i)

    # 返回活动数量, 活动列表
    return len(res), res


print(f(time)) # (4, [(1, 4), (5, 7), (8, 11), (12, 14)])
```

### 分数背包
### 连续背包
### 密度贪心算法

## 双指针算法

### 三数之和

> 找出三个元素相加等于0的元素

- 穷举: O(n^3)
```py
def threeSum(list1):
    list1.sort()
    length = len(list1)
    res = []
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                if list1[i] + list1[j] + list1[k] == 0:
                    res.append([list1[i], list1[j], list1[k]])
    return res


list1 = [-1, 0, 1]
print(threeSum(list1)) # [[-1, 0, 1]]

list1 = [-1, 0, 1, -2, 2, 3]
print(threeSum(list1)) # [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
```

- 双指针: O(n^2)

    - 判断x+y 是否等于 -z

```py
def threeSum(list1):
    list1.sort()
    length = len(list1)
    res = []
    for i in range(length - 2):
        l, r = i + 1, len(list1) - 1
        while l < r:
            sum = list1[i] + list1[l] + list1[r]
            if sum == 0:
                res.append([list1[i], list1[l], list1[r]])
                l += 1
                r -= 1
            elif sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
    return res
```

#### 四数之和
```py
def fourSum(list1):
    list1.sort()
    length = len(list1)
    res = []
    for i in range(length - 3):
        for j in range(i+1, length - 2):
            l, r = i + 1, len(list1) - 1
            while l < r:
                sum = list1[i] + list1[l] + list1[r] + list1[j]
                if sum == 0:
                    res.append([list1[i], list1[l], list1[r], list1[j]])
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
    return res


list1 = [1, 1, -1, -1]
print(fourSum(list1)) # [[-1, 1, 1, -1]]

list1 = [-1, 0, 1, -2, 2]
print(fourSum(list1)) # [[-2, 1, 2, -1], [-2, 0, 2, 0], [-1, 0, 1, 0]]
```

### 救生艇

输入两个参数: 人重量的列表, 救生艇每次能承载的重量. 求救生艇至少需要多少次, 才能载完所有人?

```py
def f(list1, weight):
    list1.sort()
    l = 0
    r = len(list1) - 1
    res = 0
    while l < r:
        res += 1
        from ipdb import set_trace
        set_trace()
        if list1[l] + list1[r] <= weight:
            l += 1
        r -= 1
    return res

# 每个人的重量
list1 = [1, 2]
# 救生艇能容纳的重量
weight = 3
print(f(list1, weight)) # 1

list1 = [1, 2, 1, 1, 3, 1]
weight = 3
print(f(list1, weight)) # 3
```

### 存储水

![image](./imgs/algorithms/water.avif)

```py
def water(list1):
    l = 0
    r = len(list1) - 1
    lmax = rmax = 0
    res = 0
    while l < r:
        if list1[l] < list1[r]:
            if list1[l] >= lmax:
                lmax = list1[l]
            else:
                res += lmax - list1[l]
            l += 1
        else:
            if list1[r] >= rmax:
                rmax = list1[r]
            else:
                res += rmax - list1[r]
            r -= 1

    return res

# 墙的高度
list1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2]
print(water(list1)) # 6
```

## string(字符串)

### 回文字符串

- dfs
```py
def isPal(str1):
    if len(str1) <= 1:
        return True
    else:
        return str1[0] == str1[-1] and isPal(str1[1:-1])

print(isPal("toot"))
print(isPal("toat"))
```

- bfs
```py
from collections import deque

def isPal(str1):
    deque1 = deque()

    for i in str1:
        deque1.append(i)

    # 前后对比
    while len(deque1) > 1:
        if deque1.pop() != deque1.popleft():
            return False

    return True
```

### 中叙, 后叙(逆波兰记法), 前叙表达式

> stack实现

- 对比
```
# 中叙
a + b

# 后叙
a b +

# 前叙
+ a b
```

- 中叙表达式转后叙, 前叙表达式
```py
from queue import LifoQueue

def to_lisp(str1):
    # 优先级
    dict1 = {}
    dict1["*"] = 3
    dict1["/"] = 3
    dict1["+"] = 2
    dict1["-"] = 2
    dict1["("] = 1

    list1 = str1.split()
    opStack = LifoQueue()
    res = []

    res.append(')')
    res.append(')')
    for object in list1:
        # 操作数
        if object in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or object in "0123456789":
            res.append(object)
        # 括号
        elif object == '(':
            opStack.put(object)
        elif object == ')':
            topToken = opStack.get()
            while topToken != '(':
                res.append(topToken)
                res.append('(')
                topToken = opStack.get()
        # 操作符
        else:
            length = opStack.qsize()-1
            # 先处理优先级高的操作符
            while (not opStack.empty()) and \
               (dict1[opStack.queue[length]] >= dict1[object]):
                  res.append(opStack.get())
                  res.append('(')
                  res.append(')')
            opStack.put(object)

    # 处理剩余操作符
    while not opStack.empty():
        res.append(opStack.get())
        res.append('(')

    # 将后叙表达式转换为前叙, 也就是lisp
    res.reverse()
    return " ".join(res)

if __name__ == '__main__':
    print(to_lisp("1 * 2 + 3 * 4"))
    print(to_lisp("( A + B ) * C - ( D - E ) * ( F + G )"))
```
输出
```
( + ( * 4 3 ) ( * 2 1 ) )
( - ( * ( + G F ( - E D ) ( * C ( + B A ) )
```

- 前叙转中叙(不带括号)
```py
from queue import LifoQueue

# 去除指定字符
def remove_char(str1, tuple1):
    res = []
    a = True
    for i in str1:
        for j in tuple1:
            if i == j:
                a = False
                break
        if a is True:
            res.append(i)
        a = True
    return res

# 前叙转中叙
def lisp_to(str1):
    opStack = LifoQueue()
    # 去除(, ), 空格
    list1 = remove_char(str1, ('(', ')', ' '))
    res = []

    for object in list1:
        if object in "+-*/":
            opStack.put(object)
        else:
            res.append(object)
            if not opStack.empty():
                res.append(opStack.get())

    return " ".join(res)


if __name__ == '__main__':
    str1 = '/ + 7 8 + 3 2'
    str2 = '(/ (+ 7 8) (+ 3 2))'
    str3 = '* 3 / + 7 8 + 3 2'
    print(lisp_to(str1))
    print(lisp_to(str2))
    print(lisp_to(str3))
```
输出
```
7 + 8 / 3 + 2
7 + 8 / 3 + 2
3 * 7 + 8 / 3 + 2
```

- 前叙转中叙(带括号)
```py
from queue import LifoQueue

def lisp_to(str1):
    # 操作符
    opStack = LifoQueue()
    # 操作数
    operandStack = LifoQueue()

    list1 = list(str1)
    res = []

    for object in list1:
        if object in "+-*/":
            opStack.put(object)
        elif object in "0123456789":
            operandStack.put(object)
        elif object == ')':
            if operandStack.qsize() >= 2:
                res.append('(')
                res.append(operandStack.get())
                res.append(opStack.get())
                res.append(operandStack.get())
                res.append(')')
            if not opStack.empty():
                res.append(opStack.get())

    # 添加剩余操作数
    while not operandStack.empty():
        res.append(operandStack.get())

    return " ".join(res)

if __name__ == '__main__':
    str1 = '(/ (+ 7 8) (+ 3 2))'
    str2 = '(* 3 (/ (+ 7 8) (+ 3 2)))'

    # 前叙转中叙
    print(lisp_to(str1))
    print(lisp_to(str2), '=', eval(lisp_to(str2)))
```
输出
```
( 8 + 7 ) / ( 2 + 3 )
( 8 + 7 ) / ( 2 + 3 ) * 3 = 9.0
```

- 运行后叙表达式
```py
from queue import LifoQueue

# 去除指定字符
def remove_char(str1, tuple1):
    res = []
    a = True
    for i in str1:
        for j in tuple1:
            if i == j:
                a = False
                break
        if a is True:
            res.append(i)
        a = True
    return res

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

def lisp_to(str1):
    operandStack = LifoQueue()
    # 去除(, ), 空格
    list1 = remove_char(str1, ('(', ')', ' '))

    for object in list1:
        if object in "0123456789":
            operandStack.put(int(object))
        else:
            operand2 = operandStack.get()
            operand1 = operandStack.get()
            result = doMath(object, operand1, operand2)
            operandStack.put(result)
    return operandStack.get()

if __name__ == '__main__':
    str1 = '7 8 + 3 2 + /'
    str2 = '((7 8 +) (3 2 +) /)'
    print(lisp_to(str1))
    print(lisp_to(str2))
```
输出
```
3.0
3.0
```

## fib(斐波那契)

### 循环 while, for

```py
def fib(n):
    x = n
    while n > 1:
        n = n - 1
        x = x + n
    return x

def fib(n):
    prev, curr = 1, 0
    for _ in range(n):
        prev, curr = curr, prev + curr
    return curr

# test
fib(10)

def fib1(f, n):
    x = n
    while n > 1:
        n = n - 1
        x = f(x, n)
        print(x)
    return x

# test
fib1(add,10)
fib1(mul,10)
```

### 递归

- 有大量的重复计算: O(2^n/2)

```py
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n - 2)
```

- 保存上一个值, 从而减少重复: O(n)
```py
def fib(n):
    if n == 1:
        return (n, 0)
    else:
        (x, y) = fib(n-1)
        return (x + y, x)


print(fib(10)[0])
```

### 迭代

```py
def fib2(x, n):
    def iter(x, n, s):
        if n >= x:
            s = iter(x, n - 1, s + n)
        return s
    return iter(x, n - 1, n)

# test
fib2(0,10)

# 自选函数: f

def fib2(f, x, n):
    def iter(f, x, n, s):
        if n >= x:
            s = iter(f, x, n - 1, f(s, n))
        return s
    return iter(f, x, n - 1, n)


# test
fib2(add, 0, 10)
fib2(mul, 1, 5)

# 步进: y

def fib2(f, x, n, y):
    def iter(f, x, n, s):
        if n >= x:
            # 递减
            s = iter(f, x, n-y, f(s, n))
            # 递加
            # s = iter(f, x+y, n, f(s, x))
        return s
    return iter(f, x, n - y, n)

# 累加器
fib2(add, 0, 10, 2)
fib2(lambda x, y: x + y, 0, 10, 1)
fib2(mul, 10, 100, 10)
```

### 泛函

```py
def sum(n, term, next):
    s, x = 0, 1
    while x <= n:
        s, x = s + term(x), next(x)
    return s

def fib(x):
    def fib_next(x):
        return x + 1
    def fib_term(x):
        return x
    return sum(x, fib_term, fib_next)

fib(100)
```

## pi(圆周率)

```py
def sum(n, pi_term, pi_next):
    def iter(s, x, n):
        if n >= x:
            s = iter(s + pi_term(x), pi_next(x), n)
        return s
    return iter(0, 1, n)


# pi
def pi(x):
    return sum(x, lambda x: 8 / (x * (x + 2)), lambda x: x + 4)

# 8 / (x * (x + 2))
print(pi(3000)) # 3.1409259869971957
```

## 牛顿法求平方根
- 二分
```py
def f(n):
    epsilon = 0.01
    guess = 0.0

    low = 0.0
    high = max(1.0, n)
    mid = (low + high) / 2.0
    while abs(mid ** 2 - n) >= epsilon:
        print(low, high, mid)
        guess += 1
        if mid ** 2 < n:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2.0
    print(mid)
```
- 牛顿法: 比二分效率要高
```py
def f(n):
    epsilon = 0.01
    guess = n / 2.0
    while abs(guess ** 2 - n) >= epsilon:
        guess = guess - (((guess ** 2) - n) / (2 * guess))
    print(guess)
```

## 密码

### rsa整数加密

- [知乎: 如何深入浅出地讲解RSA密码？](https://www.zhihu.com/question/304030251/answer/543201982)

- [Implementing RSA in Python from Scratch (Part 1)](https://sudosecurity.org/blog/implementing-rsa-from-scratch-in-python/)

```py
def eucalg(a, b):
    # 通过扩展欧几里得算法, 求出a的乘法逆元

    # make a the bigger one and b the lesser one
    swapped = False
    # 找出a,b之间更大的数
    if a < b:
        a, b = b, a
        swapped = True
    # ca and cb store current a and b in form of
    # coefficients with initial a and b
    # a' = ca[0] * a + ca[1] * b
    # b' = cb[0] * a + cb[1] * b
    ca = (1, 0)
    cb = (0, 1)
    while b != 0:
        # k denotes how many times number b
        # can be substracted from a
        k = a // b
        # a  <- b
        # b  <- a - b * k
        # ca <- cb
        # cb <- (ca[0] - k * cb[0], ca[1] - k * cb[1])
        a, b, ca, cb = b, a-b*k, cb, (ca[0]-k*cb[0], ca[1]-k*cb[1])
    if swapped:
        return (ca[1], ca[0])
    else:
        return ca

def modpow(msg, ed, n):
    # 快速幂算法. 时间复杂度log n

    # ed密钥的位数
    size = ed.bit_length()

    # calculate the result
    result = 1
    for i in range(size, -1, -1):
        result = (result * result) % n
        if (ed >> i) & 1: result = (result * msg) % n

    return result

def keysgen(p, q):
    n = p * q
    # 求出n互质整数的个数
    lambda_n = (p - 1) * (q - 1)
    # enc必须是小于n, 且不等于p, q的质数
    enc = 35537
    dec = eucalg(enc, lambda_n)[0]
    if dec < 0: dec += lambda_n
        # both private and public key must have n stored with them
    return {'priv': (dec, n), 'pub': (enc, n)}

def numencrypt(msg, pub):
    return modpow(msg, pub[0], pub[1])

def numdecrypt(msg, priv):
    return modpow(msg, priv[0], priv[1])

def test():
    # 生成密钥. 两个参数必须是质数
    keys = keysgen(31337, 31357)
    # 私钥
    priv = keys['priv']
    # 公钥
    pub = keys['pub']

    # msg只能是int类型
    msg = 80087
    # 加密
    enc = numencrypt(msg, pub)
    # 解密
    dec = numdecrypt(enc, priv)

    # 验证
    assert 80087 == dec
```

# reference

- [hackerearth: 数据结构](https://www.hackerearth.com/practice/algorithms/sorting/)

    - 支持数据可视化

- [programiz: 数据结构](https://www.programiz.com/dsa)

- [Problem Solving with Algorithms and Data Structures using Python(英文版, 可在线交互运行代码)](https://runestone.academy/runestone/books/published/pythonds3/index.html)

    - [problem-solving-with-algorithms-and-data-structure-using-python(中文版)](https://github.com/facert/python-data-structure-cn)

- [TheAlgorithms: Python](https://github.com/TheAlgorithms/Python)

- [LeetCode 刷题攻略](https://github.com/youngyangyang04/leetcode-master)
