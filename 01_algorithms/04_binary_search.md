# 二分查找

> 标签：#算法 #数组 #查找 #二分查找 #模板题

---

## 做题心得

二分查找最重要的不是记很多模板，而是先判断题目里有没有“单调性”。

- 如果数组已经有序，通常可以二分查找某个值或某个边界。
- 如果答案越大越容易满足，或越小越容易满足，通常可以二分答案。
- 如果题目要求“第一个”“最后一个”“最小可行值”“最大可行值”，多半是在找边界。
- 如果每次二分后不知道该丢掉哪一半，说明单调性还没有想清楚。

---

## 一句话总结

二分查找是在有序或单调的范围里，每次用中点判断答案在哪一半，从而把查找范围不断缩小到目标位置。

---

## 核心问题

二分查找解决的是“在单调范围中快速定位目标或边界”的问题。

常见输入：

- 一个有序数组 `nums`。
- 一个目标值 `target`。
- 一个可能答案范围 `[left, right]`。
- 一个判断函数 `check(x)`，表示当前答案 `x` 是否满足条件。

常见输出：

- 目标值的下标。
- 第一个满足条件的位置。
- 最后一个满足条件的位置。
- 最小可行答案或最大可行答案。
- 如果不存在目标，返回 `-1` 或插入位置。

适用场景：

- 数组或搜索空间有序。
- 判断函数具有单调性。
- 题目要求找边界，而不是找所有结果。
- 暴力枚举答案会超时，但可以快速判断某个答案是否可行。

不适用场景：

- 数据没有顺序，也没有单调性。
- 判断某个答案是否可行的成本太高，二分后仍然无法优化。
- 题目需要返回所有满足条件的元素，而不是某个边界。

---

## 核心思想

二分查找的本质是不断排除不可能的答案。

每次取中点 `mid`，根据 `nums[mid]` 或 `check(mid)` 的结果，确定答案只可能在左半边还是右半边。只要每一步都能安全排除一半，复杂度就能从 $O(n)$ 降到 $O(log n)$。

做题时先问自己四个问题：

1. 搜索范围是什么？
2. 我要找的是具体值，还是某个边界？
3. `mid` 满足条件时，应该保留 `mid` 还是丢掉 `mid`？
4. 循环结束后，答案落在 `left`、`right`，还是需要额外判断？

最容易掌握的写法可以先记两类：

- 查具体值：用闭区间 `[left, right]`，循环条件写 `left <= right`。
- 查边界：用左闭右开区间 `[left, right)`，循环条件写 `left < right`。

---

## 核心操作 / 关键步骤

### 1. 确定单调性

先判断范围能不能被分成两段。

比如在升序数组中找第一个大于等于 `target` 的位置：

```text
小于 target 的位置：不满足
大于等于 target 的位置：满足
```

整个数组会被切成：

```text
False False False True True True
```

二分查找要找的就是第一个 `True`。

---

### 2. 选择区间写法

常用两种写法：

- 闭区间 `[left, right]`：左右端点都可能是答案。
- 左闭右开 `[left, right)`：`left` 可能是答案，`right` 不在搜索范围内。

入门建议：

- 找具体值时，用闭区间。
- 找第一个满足条件的位置时，用左闭右开区间。

这样边界更容易统一。

---

### 3. 写 `mid`

```text
mid = left + (right - left) // 2
```

Python 中 `(left + right) // 2` 也不会整数溢出，但上面的写法是通用习惯。

---

### 4. 收缩范围

收缩范围时最容易出错，关键是看 `mid` 能不能被排除。

- 如果 `mid` 已经不可能是答案，就用 `left = mid + 1` 或 `right = mid - 1`。
- 如果 `mid` 仍然可能是答案，就保留它，用 `right = mid` 或 `left = mid`。

---

## 模板代码

### 查找具体值

适合题目要求“找到 `target` 的下标，找不到返回 `-1`”。

```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

这个模板用的是闭区间 `[left, right]`。

---

### 第一个大于等于目标值的位置

也叫 `lower_bound`，返回第一个满足 `nums[i] >= target` 的下标。

如果所有数都小于 `target`，返回 `len(nums)`。

```python
def lower_bound(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left
```

这个模板用的是左闭右开区间 `[left, right)`。

---

### 第一个大于目标值的位置

也叫 `upper_bound`，返回第一个满足 `nums[i] > target` 的下标。

如果所有数都小于等于 `target`，返回 `len(nums)`。

```python
def upper_bound(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left
```

---

### 查找目标值的左右边界

有重复元素时，普通二分只能找到其中一个位置。要找完整区间，可以用 `lower_bound` 和 `upper_bound`。

```python
def search_range(nums, target):
    left = lower_bound(nums, target)
    right = upper_bound(nums, target) - 1

    if left <= right:
        return [left, right]

    return [-1, -1]
```

例子：

```text
nums = [1, 2, 2, 2, 3]
target = 2
lower_bound = 1
upper_bound = 4
答案区间 = [1, 3]
```

---

### 搜索插入位置

插入位置本质就是第一个大于等于 `target` 的位置。

```python
def search_insert(nums, target):
    return lower_bound(nums, target)
```

---

### 答案二分：找最小可行值

有些题不是在数组里找，而是在答案范围里找。

比如“吃香蕉”问题：速度越快，越容易在规定时间内吃完。所以可以二分最小速度。

```python
def min_eating_speed(piles, h):
    def can_finish(speed):
        hours = 0

        for pile in piles:
            hours += (pile + speed - 1) // speed

        return hours <= h

    left = 1
    right = max(piles)

    while left < right:
        mid = left + (right - left) // 2

        if can_finish(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

这个模板找的是“最小可行值”：

```text
不可行 不可行 不可行 可行 可行 可行
                         ^
                     找第一个可行
```

---

### 答案二分：找最大可行值

如果题目要找最大可行值，可以把 `mid` 写成偏右中点，避免死循环。

```python
def max_feasible(left, right, check):
    while left < right:
        mid = left + (right - left + 1) // 2

        if check(mid):
            left = mid
        else:
            right = mid - 1

    return left
```

这个模板适合这种单调性：

```text
可行 可行 可行 不可行 不可行
             ^
        找最后一个可行
```

---

### 旋转有序数组中查找

旋转有序数组虽然整体不是完全有序，但每次二分后，至少有一半是有序的。

```python
def search_rotated(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

---

## 复杂度

二分查找每次把搜索范围缩小一半。

- 查找具体值：时间复杂度 $O(log n)$，空间复杂度 $O(1)$。
- 查找左右边界：时间复杂度 $O(log n)$，空间复杂度 $O(1)$。
- 答案二分：时间复杂度通常是 $O(log R * check)$，其中 `R` 是答案范围大小，`check` 是每次判断的成本。
- 浮点数二分：通常按固定次数或误差精度控制循环，复杂度和精度要求有关。

---

## 常见题型

### 1. 有序数组查找

题目给一个升序数组，要求找目标值。

做法：

- 找具体下标：用闭区间模板。
- 找插入位置：用 `lower_bound`。

---

### 2. 查找左右边界

数组中有重复元素，要求找目标值第一次和最后一次出现的位置。

做法：

- 第一次出现：`lower_bound(nums, target)`。
- 最后一次出现：`upper_bound(nums, target) - 1`。

---

### 3. 二分答案

题目没有直接给有序数组，但答案本身有单调性。

常见关键词：

- 最小的最大值。
- 最大的最小值。
- 至少需要多少。
- 最多可以多少。
- 能否在规定时间内完成。

做法：

- 先写 `check(mid)`。
- 再判断 `check(mid)` 为真时，应该往左找还是往右找。

---

### 4. 旋转有序数组

数组原本有序，但被旋转过。

做法：

- 每次判断左半边还是右半边有序。
- 如果目标在有序的一半里，就收缩到这一半。
- 否则去另一半。

---

### 5. 峰值问题

题目要求找一个峰值，比如 `nums[i] > nums[i + 1]` 的方向可以判断峰值在哪边。

做法：

- 如果 `nums[mid] < nums[mid + 1]`，右边一定有峰值。
- 否则左边或当前点一定有峰值。

---

## 易错点

- 没有先判断单调性，直接套模板。
- 闭区间和左闭右开区间混用，导致边界错一位。
- `while left <= right` 和 `while left < right` 搞混。
- 找边界时，`mid` 可能是答案，却被 `mid + 1` 或 `mid - 1` 错误丢掉。
- 找最大可行值时没有用偏右中点，导致 `left = mid` 后死循环。
- `lower_bound` 返回的可能是 `len(nums)`，访问数组前要先判断越界。
- 答案二分时，`check(mid)` 写反，导致方向反了。
- 旋转数组有重复值时，普通判断哪一半有序可能失效，需要额外处理相等情况。

---

## 相关变形

- 三分搜索：用于单峰函数或单谷函数，不是普通单调查找。
- 浮点数二分：用于实数答案，通常用误差或固定次数结束。
- 二分答案：在答案空间上二分，不一定有真实数组。
- 指数搜索：先扩大范围，再二分，适合不知道右边界的场景。
- 二叉搜索树查找：利用树的有序性质，本质上也是每次排除一部分范围。

---

## 记忆口诀

```text
先看单调，再定边界；
找值闭区间，找界左闭右开；
mid 能不能丢，是更新边界的关键。
```
