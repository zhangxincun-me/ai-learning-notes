# 排序算法

> 标签：#算法 #数组 #排序 #模板题 #面试高频

---

## 做题心得

这篇笔记里的代码统一采用**教材版基础写法**：先把算法最朴素、最标准的过程写清楚，再理解优化版本。

- 先掌握排序过程，不急着写工程优化版。
- 教材版代码优先保证步骤清晰、变量含义直观、方便手写。
- 如果只是做题或写业务代码，可以直接用语言内置排序。
- 如果题目要求手写排序，先根据稳定性、空间、最坏复杂度选择算法。
- 如果数据范围很小，可以考虑计数排序、桶排序、基数排序。
- 如果只需要前 `k` 个元素，不一定需要完整排序。

以后新增算法笔记时，模板代码也优先使用教材版基础写法。

---

## 一句话总结

排序算法就是按照指定规则重新排列元素，核心是在时间复杂度、空间复杂度、稳定性和数据特征之间做取舍。

---

## 核心问题

排序解决的是“把一组无序元素变成有序元素”的问题。

常见输入：

- 一个数组 `nums`。
- 一个排序规则，例如升序、降序、按字段排序。
- 有时会给出数据范围，例如元素只在 `0..1000` 内。

常见输出：

- 排好序的新数组。
- 原地修改后的数组。
- 排序后的索引、区间或前 `k` 个元素。

适用场景：

- 需要查找、去重、合并区间、双指针扫描。
- 需要按大小、时间、频率、优先级处理数据。
- 需要把无序问题转化成有序问题。

不适用场景：

- 只需要最大值或最小值，不必完整排序。
- 只需要第 `k` 大或前 `k` 个元素，可以考虑堆或快速选择。
- 数据频繁动态变化时，可能更适合堆、平衡树等结构。

---

## 分类方式

### 1. 比较排序

通过元素之间的大小比较决定顺序。

常见算法：

- 冒泡排序
- 选择排序
- 插入排序
- 希尔排序
- 归并排序
- 快速排序
- 堆排序

比较排序的理论下界是 $O(n \log n)$。

### 2. 非比较排序

利用数据本身的范围、位数或分布进行排序。

常见算法：

- 计数排序
- 桶排序
- 基数排序

非比较排序在特定条件下可以达到 $O(n)$，但通常依赖额外空间和数据范围。

---

## 复杂度速查表

| 算法 | 最好时间 | 平均时间 | 最坏时间 | 空间复杂度 | 稳定性 | 原地性 |
| --- | --- | --- | --- | --- | --- | --- |
| 冒泡排序 | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | 稳定 | 原地 |
| 选择排序 | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | 不稳定 | 原地 |
| 插入排序 | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | 稳定 | 原地 |
| 希尔排序 | 取决于 gap | 取决于 gap | 可到 $O(n^2)$ | $O(1)$ | 不稳定 | 原地 |
| 归并排序 | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | 稳定 | 非原地 |
| 快速排序 | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | 不稳定 | 原地 |
| 堆排序 | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | 不稳定 | 原地 |
| 计数排序 | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | 稳定 | 非原地 |
| 桶排序 | $O(n)$ | $O(n + k)$ | $O(n^2)$ | $O(n + k)$ | 取决于桶内排序 | 非原地 |
| 基数排序 | $O(d(n + k))$ | $O(d(n + k))$ | $O(d(n + k))$ | $O(n + k)$ | 稳定 | 非原地 |

其中：

- `n` 是元素个数。
- `k` 是数据范围或桶数量。
- `d` 是数字位数。

---

## 核心思想

排序的本质是不断消除逆序关系。

常见思路：

- 交换：发现逆序就交换，例如冒泡排序、快速排序。
- 选择：每次选出最小或最大元素，例如选择排序、堆排序。
- 插入：维护一个有序区间，把新元素插入正确位置，例如插入排序。
- 分治：先拆成小问题，再合并或分区，例如归并排序、快速排序。
- 计数：统计每个值出现次数，例如计数排序。
- 分桶：按范围或位数分组处理，例如桶排序、基数排序。

---

## 模板代码

### 1. 冒泡排序

核心思想：相邻元素两两比较，如果顺序错误就交换。每一轮会把当前未排序区间的最大值放到最右边。

```python
def bubble_sort(nums):
    n = len(nums)

    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums
```

记忆：

```text
相邻比较，大的往后冒。
```

---

### 2. 选择排序

核心思想：每一轮从未排序区间中选出最小值，放到当前起点。

```python
def selection_sort(nums):
    n = len(nums)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums
```

记忆：

```text
每轮找最小，放到最前面。
```

---

### 3. 插入排序

核心思想：左边维护一个有序区间，每次把当前元素插入到左边合适的位置。

```python
def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        current = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = current

    return nums
```

注意：

```text
while 条件写 nums[j] > current。
如果写成 >=，相等元素的相对顺序会改变。
```

---

### 4. 希尔排序

核心思想：先按较大的间隔 `gap` 做分组插入排序，再逐步缩小 `gap`，最后做一次普通插入排序。

```python
def shell_sort(nums):
    n = len(nums)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            current = nums[i]
            j = i

            while j >= gap and nums[j - gap] > current:
                nums[j] = nums[j - gap]
                j -= gap

            nums[j] = current

        gap //= 2

    return nums
```

记忆：

```text
先大步调整，再小步插入。
```

---

### 5. 归并排序

核心思想：先递归拆成两半，分别排好序，再合并两个有序数组。

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

注意：

```text
合并时相等先取左边元素，所以归并排序是稳定排序。
```

---

### 6. 快速排序

核心思想：选一个基准值 `pivot`，把比它小的放左边，比它大的放右边，再递归处理左右两段。

下面是教材常见的左右指针写法，也可以理解成“挖坑填数”。

```python
def quick_sort(nums):
    def sort(left, right):
        if left >= right:
            return

        i = left
        j = right
        pivot = nums[left]

        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]

            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]

        nums[i] = pivot
        sort(left, i - 1)
        sort(i + 1, right)

    sort(0, len(nums) - 1)
    return nums
```

过程理解：

```text
1. pivot 先保存 nums[left]，左边出现一个坑。
2. 从右边找小于 pivot 的数，填到左边坑里。
3. 从左边找大于 pivot 的数，填到右边坑里。
4. 指针相遇后，把 pivot 放回相遇位置。
```

注意：

```text
教材版通常选第一个元素做 pivot。
如果数组本来有序，可能退化到 O(n^2)。
随机 pivot、三路快排属于进阶优化，先理解教材版再看。
```

---

### 7. 堆排序

核心思想：先把数组建成大顶堆，再反复把堆顶最大值交换到数组末尾。

```python
def heap_sort(nums):
    n = len(nums)

    def sift_down(index, heap_size):
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < heap_size and nums[left] > nums[largest]:
                largest = left

            if right < heap_size and nums[right] > nums[largest]:
                largest = right

            if largest == index:
                break

            nums[index], nums[largest] = nums[largest], nums[index]
            index = largest

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n)

    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        sift_down(0, end)

    return nums
```

记忆：

```text
先建大顶堆，再把堆顶最大值换到末尾。
```

---

### 8. 计数排序

核心思想：统计每个整数出现次数，再根据次数把元素放回有序位置。

教材版通常假设元素是非负整数。

```python
def counting_sort(nums):
    if not nums:
        return nums

    max_value = max(nums)
    count = [0] * (max_value + 1)

    for num in nums:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        count[num] -= 1
        output[count[num]] = num

    return output
```

注意：

```text
倒序遍历原数组，是为了保持稳定性。
如果有负数，需要整体加偏移量后再计数。
```

---

### 9. 桶排序

核心思想：把数据按范围分到多个桶里，每个桶内部排序，最后按桶顺序合并。

```python
def bucket_sort(nums, bucket_count=10):
    if len(nums) <= 1:
        return nums

    min_value = min(nums)
    max_value = max(nums)

    if min_value == max_value:
        return nums

    buckets = [[] for _ in range(bucket_count)]

    for num in nums:
        index = (num - min_value) * (bucket_count - 1) // (max_value - min_value)
        buckets[index].append(num)

    result = []
    for bucket in buckets:
        insertion_sort(bucket)
        result.extend(bucket)

    return result


def insertion_sort(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = current

    return nums
```

注意：

```text
桶排序是否高效，关键看桶的划分是否均匀。
```

---

### 10. 基数排序

核心思想：按位排序。先按个位排，再按十位排，再按百位排，直到最高位。

教材版通常处理非负整数，并且每一位都使用稳定的计数排序。

```python
def radix_sort(nums):
    if not nums:
        return nums

    max_value = max(nums)
    exp = 1

    while max_value // exp > 0:
        nums = counting_sort_by_digit(nums, exp)
        exp *= 10

    return nums


def counting_sort_by_digit(nums, exp):
    count = [0] * 10

    for num in nums:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    output = [0] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        digit = (num // exp) % 10
        count[digit] -= 1
        output[count[digit]] = num

    return output
```

注意：

```text
每一位排序都必须稳定，否则前面低位排好的顺序会被破坏。
```

---

### 11. Python 内置排序

实际做题或写业务代码时，通常优先使用内置排序。

```python
nums = [3, 1, 4, 2]
nums.sort()

arr = [3, 1, 4, 2]
sorted_arr = sorted(arr)
```

按字段排序：

```python
students = [
    ("Alice", 90, 18),
    ("Bob", 90, 17),
    ("Cindy", 95, 19),
]

students.sort(key=lambda x: (-x[1], x[2]))
```

含义：

```text
先按成绩降序；
成绩相同，再按年龄升序。
```

---

## 常见题型

### 1. 直接排序

要求把数组升序或降序排列。

做法：

- 手写排序：优先写教材版快排、归并排序或堆排序。
- 不要求手写：直接用内置排序。

---

### 2. 按字段排序

例如按频率、时间、分数、区间左端点排序。

```python
intervals = [[2, 4], [1, 3], [5, 6]]
intervals.sort(key=lambda x: x[0])
```

多个字段时用元组：

```python
people = [("Alice", 170), ("Bob", 180), ("Alice", 165)]
people.sort(key=lambda x: (x[0], -x[1]))
```

---

### 3. 排序后双指针

很多数组题排序后可以使用双指针。

常见题：

- 两数之和变体
- 三数之和
- 合并区间
- 最接近的三数之和

---

### 4. 前 k 个元素

不一定需要完整排序。

做法：

- `k` 很小：用堆。
- 需要平均线性时间：用快速选择。
- 数据范围小：用计数。
- 题目不限制：直接排序最简单。

---

### 5. 链表排序

链表排序常用归并排序。

原因：

- 链表不适合随机访问。
- 归并排序只需要断链和合并两个有序链表。
- 可以保持稳定性。

---

### 6. 区间排序

区间题经常先按左端点排序。

```python
intervals = [[2, 6], [1, 3], [8, 10]]
intervals.sort(key=lambda x: x[0])
```

---

## 易错点

- 快排递归边界写错，导致死循环或漏排。
- 快排中 `i`、`j` 移动条件写反。
- 快排保存 `pivot` 后，忘记在相遇位置放回 `pivot`。
- 归并排序合并时相等元素没有先取左边，导致稳定性丢失。
- 插入排序从 `i = 0` 开始虽然不一定错，但教材版通常从 `i = 1` 开始。
- 堆排序建堆应从最后一个非叶子节点 `n // 2 - 1` 开始。
- 计数排序默认非负整数，有负数时要加偏移量。
- 计数排序数据范围太大时，空间消耗会很高。
- 基数排序每一位排序必须稳定。
- `nums.sort()` 返回 `None`，不能写 `nums = nums.sort()`。

---

## 选择建议

面试手写时：

- 通用排序：快速排序。
- 要稳定：归并排序。
- 要最坏时间稳定且原地：堆排序。
- 小数组或基本有序：插入排序。
- 整数范围小：计数排序。

刷题实战时：

- 能用内置排序就用内置排序。
- 题目要求空间 $O(1)$，慎用归并排序。
- 题目强调稳定性，慎用快排、堆排、选择排序。
- 题目只要第 `k` 大，不要急着完整排序。

---

## 相关变形

- 快速选择：基于快排分区思想，用于找第 `k` 大或第 `k` 小。
- 随机快排：随机选择 pivot，降低退化概率。
- 三路快排：把数组分成小于、等于、大于 pivot 三段，适合重复元素很多的情况。
- 外部排序：数据太大无法一次放入内存，常用多路归并。
- 拓扑排序：名字里有排序，但本质是图的依赖顺序，不是比较大小。
- 排序 + 双指针：排序只是前置步骤，核心是利用有序性移动指针。

---

## 记忆口诀

```text
冒泡相邻换，选择找最小；
插入维护序，希尔分组跳；
归并先拆后合，快排左右填坑；
堆排建堆换尾，计数先数后放；
桶排序看分布，基数排序按位走。
```

