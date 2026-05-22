# 二叉树

> 标签：#算法 #数据结构 #模板题 #二叉树 #DFS #BFS

---

## 做题心得

二叉树题不要急着写代码，先判断这是“遍历整棵树”还是“从子树收集答案”。

- 如果题目要求按某种顺序访问节点，多半是遍历问题，用前序、中序、后序或层序。
- 如果题目要求高度、直径、平衡性、最大路径和，多半是子树问题，用后序递归更自然。
- 如果题目要求一条路径，记得递归进入时加入节点，递归退出时回溯删除节点。

---

## 一句话总结

二叉树算法的本质是围绕“当前节点、左子树、右子树”做递归或遍历，常用 DFS 处理深度、路径和结构判断，常用 BFS 处理层序、最短层数和按层统计。

---

## 核心问题

二叉树解决的是树形结构中的节点访问、信息统计、路径搜索和结构判断问题。

常见输入：

- `root`：二叉树根节点。
- `p`、`q`：树中的某两个目标节点。
- `target_sum`：路径和目标值。
- `preorder`、`inorder`、`postorder`：遍历序列。

常见输出：

- 遍历结果。
- 树的高度、深度、直径、节点数量。
- 是否满足某种性质。
- 某条路径、所有路径或最近公共祖先。
- 重建后的二叉树。

适用场景：

- 问题天然可以拆成左子树和右子树两个子问题。
- 当前节点的答案依赖左右子树的答案。
- 需要按层访问节点。
- 需要在树上搜索某个目标或路径。

不适用场景：

- 数据本质不是树，而是一般图，需要处理环和访问状态。
- 题目要求动态区间查询，通常更适合线段树或树状数组。
- 题目只和数组排序、哈希计数有关，没必要强行转成树。

---

## 核心思想

二叉树是最典型的递归结构。

对任意一个节点 `root` 来说，它的左右孩子又分别是一棵二叉树。所以二叉树题经常可以写成：

```text
处理当前节点
处理左子树
处理右子树
```

或者：

```text
拿到左子树答案
拿到右子树答案
合并成当前节点答案
```

做题时可以先问自己三个问题：

1. 当前节点要做什么？
2. 左子树和右子树需要返回什么信息？
3. 当前节点需要把什么信息返回给父节点？

这三个问题想清楚，递归函数的参数、返回值和终止条件通常就清楚了。

---

## 核心操作 / 关键步骤

### 1. 定义节点

二叉树节点通常包含三个部分：节点值、左孩子、右孩子。

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

### 2. DFS：深度优先遍历

DFS 会沿着一条路径一直走到底，再回到上一个分叉点继续搜索。

三种常见顺序：

- 前序：根 -> 左 -> 右。
- 中序：左 -> 根 -> 右。
- 后序：左 -> 右 -> 根。

区别只在于“处理当前节点”的位置。

```python
def dfs(root):
    if not root:
        return

    # 前序位置：进入节点时处理
    dfs(root.left)
    # 中序位置：左子树处理完后处理
    dfs(root.right)
    # 后序位置：左右子树都处理完后处理
```

---

### 3. BFS：广度优先遍历

BFS 按层访问节点，适合层序遍历、最小深度、每层最大值、右视图等题型。

核心是队列：

```text
根节点入队
每次取出当前层所有节点
把下一层节点加入队列
```

---

### 4. 递归返回值

很多二叉树题的关键不在“访问节点”，而在“子树向父节点返回什么”。

比如求最大深度：

```text
当前树的最大深度 = max(左子树最大深度, 右子树最大深度) + 1
```

比如判断是否平衡：

```text
当前树是否平衡，依赖左子树高度、右子树高度，以及左右子树本身是否平衡
```

这种题通常用后序遍历，因为必须先知道左右子树的答案，才能处理当前节点。

---

## 模板代码

### 基础节点模板

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

### 前序遍历

```python
def preorder_traversal(root):
    ans = []

    def dfs(node):
        if not node:
            return

        ans.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ans
```

---

### 中序遍历

中序遍历在二叉搜索树中很常用，因为二叉搜索树的中序遍历结果是升序。

```python
def inorder_traversal(root):
    ans = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        ans.append(node.val)
        dfs(node.right)

    dfs(root)
    return ans
```

---

### 后序遍历

后序遍历适合“先拿子树信息，再处理当前节点”的问题。

```python
def postorder_traversal(root):
    ans = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        dfs(node.right)
        ans.append(node.val)

    dfs(root)
    return ans
```

---

### 前序遍历（非递归）

非递归遍历的核心是用栈模拟递归调用栈。

前序遍历顺序是 `根 -> 左 -> 右`。因为栈是后进先出，所以要先把右孩子入栈，再把左孩子入栈。

```python
def preorder_traversal_iter(root):
    if not root:
        return []

    ans = []
    stack = [root]

    while stack:
        node = stack.pop()
        ans.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return ans
```

---

### 中序遍历（非递归）

中序遍历顺序是 `左 -> 根 -> 右`。

思路是：先一路向左走到底，把沿途节点压栈；走不动时弹出栈顶节点处理，再去它的右子树。

```python
def inorder_traversal_iter(root):
    ans = []
    stack = []
    node = root

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        ans.append(node.val)
        node = node.right

    return ans
```

---

### 后序遍历（非递归）

后序遍历顺序是 `左 -> 右 -> 根`。

可以先按 `根 -> 右 -> 左` 的顺序遍历，最后把结果反转，就得到后序遍历。

```python
def postorder_traversal_iter(root):
    if not root:
        return []

    ans = []
    stack = [root]

    while stack:
        node = stack.pop()
        ans.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return ans[::-1]
```

---

### 层序遍历

```python
from collections import deque


def level_order(root):
    if not root:
        return []

    ans = []
    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        ans.append(level)

    return ans
```

---

### 最大深度

```python
def max_depth(root):
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return max(left_depth, right_depth) + 1
```

---

### 最小深度

最小深度适合用 BFS，第一次遇到叶子节点时就是答案。

```python
from collections import deque


def min_depth(root):
    if not root:
        return 0

    queue = deque([(root, 1)])

    while queue:
        node, depth = queue.popleft()

        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
```

---

### 判断平衡二叉树

如果某棵子树已经不平衡，就返回 `-1`，避免重复计算高度。

```python
def is_balanced(root):
    def height(node):
        if not node:
            return 0

        left_height = height(node.left)
        if left_height == -1:
            return -1

        right_height = height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return height(root) != -1
```

---

### 路径总和

判断是否存在一条从根节点到叶子节点的路径，使路径和等于目标值。

```python
def has_path_sum(root, target_sum):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target_sum

    remain = target_sum - root.val

    return (
        has_path_sum(root.left, remain)
        or has_path_sum(root.right, remain)
    )
```

---

### 收集所有路径

这类题要注意回溯：递归进入时 `append`，递归退出时 `pop`。

```python
def path_sum(root, target_sum):
    ans = []
    path = []

    def dfs(node, remain):
        if not node:
            return

        path.append(node.val)
        remain -= node.val

        if not node.left and not node.right and remain == 0:
            ans.append(path[:])

        dfs(node.left, remain)
        dfs(node.right, remain)
        path.pop()

    dfs(root, target_sum)
    return ans
```

---

### 最近公共祖先

普通二叉树的最近公共祖先，核心是看 `p` 和 `q` 分别落在哪个子树里。

```python
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left or right
```

---

### 判断二叉搜索树

二叉搜索树不能只比较父子节点，必须给每个节点维护合法取值范围。

```python
def is_valid_bst(root):
    def dfs(node, low, high):
        if not node:
            return True

        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False

        return (
            dfs(node.left, low, node.val)
            and dfs(node.right, node.val, high)
        )

    return dfs(root, None, None)
```

---

### 二叉搜索树查找

利用二叉搜索树“左小右大”的性质，可以像二分查找一样缩小范围。

```python
def search_bst(root, val):
    while root:
        if root.val == val:
            return root
        if val < root.val:
            root = root.left
        else:
            root = root.right

    return None
```

---

### 根据前序和中序构造二叉树

前序遍历的第一个值是根节点，中序遍历中根节点左边是左子树，右边是右子树。

```python
def build_tree(preorder, inorder):
    index = {value: i for i, value in enumerate(inorder)}

    def dfs(pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right:
            return None

        root_value = preorder[pre_left]
        root = TreeNode(root_value)

        root_index = index[root_value]
        left_size = root_index - in_left

        root.left = dfs(
            pre_left + 1,
            pre_left + left_size,
            in_left,
            root_index - 1,
        )
        root.right = dfs(
            pre_left + left_size + 1,
            pre_right,
            root_index + 1,
            in_right,
        )

        return root

    return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
```

这个模板默认树中没有重复值。如果有重复值，就不能只用哈希表记录一个下标。

---

## 复杂度

二叉树题通常设节点数量为 `n`，树高为 `h`，最大层宽为 `w`。

- DFS 遍历：时间复杂度 $O(n)$，空间复杂度 $O(h)$。
- BFS 遍历：时间复杂度 $O(n)$，空间复杂度 $O(w)$。
- 平衡树中 `h = log n`，递归空间接近 $O(log n)$。
- 链状树中 `h = n`，递归空间会退化到 $O(n)$。
- 构造二叉树：使用哈希表定位中序下标后，时间复杂度 $O(n)$，空间复杂度 $O(n)$。

---

## 常见题型

### 1. 遍历类

题目要求输出节点访问顺序。

常见形式：

- 前序遍历。
- 中序遍历。
- 后序遍历。
- 层序遍历。
- 锯齿形层序遍历。

做法：明确处理当前节点的位置。

---

### 2. 深度 / 高度类

题目要求树的最大深度、最小深度、是否平衡、直径等。

做法：大多用后序递归，让子树先返回高度，再合并答案。

---

### 3. 路径类

题目要求找根到叶子的路径、路径和、所有满足条件的路径。

做法：

- 只判断是否存在：递归返回布尔值。
- 要收集所有路径：使用 `path` 记录当前路径，并在递归结束时回溯。
- 路径不一定从根开始：通常需要在每个节点重新开一条路径，或用前缀和优化。

---

### 4. 最近公共祖先

题目要求找到两个节点的最低共同父节点。

做法：

- 普通二叉树：左右子树分别搜索，左右都有结果则当前节点是答案。
- 二叉搜索树：利用 `p`、`q` 和当前节点值的大小关系决定往左还是往右。

---

### 5. 二叉搜索树

题目围绕 BST 的性质展开。

常见形式：

- 验证二叉搜索树。
- 搜索某个值。
- 插入或删除节点。
- 第 `k` 小元素。
- 把有序数组转换成平衡 BST。

做法：优先想中序遍历和取值范围。

---

### 6. 构造 / 序列化

题目给遍历序列或字符串，要求还原二叉树。

做法：

- 前序 + 中序：前序确定根，中序划分左右子树。
- 中序 + 后序：后序确定根，中序划分左右子树。
- 序列化：空节点也要记录，否则结构会丢失。

---

### 7. 树形 DP

题目要求在树上做选择，并且父子节点之间有约束。

常见形式：

- 打家劫舍 III。
- 二叉树中的最大路径和。
- 监控二叉树。

做法：定义每个节点返回多个状态，比如“选当前节点”和“不选当前节点”。

---

## 易错点

- 忘记处理空树：`root is None` 时通常要立刻返回。
- 混淆深度和高度：深度通常从根往下数，高度通常从当前节点往下数。
- 最小深度不能直接写成 `min(left, right) + 1`，因为只有一个孩子时，空孩子不能算成深度 `0` 的有效路径。
- 判断 BST 不能只比较当前节点和左右孩子，要用上下界限制整棵子树。
- 收集路径时忘记 `path.pop()`，会导致不同路径互相污染。
- `ans.append(path)` 会保存同一个列表引用，应该写 `ans.append(path[:])`。
- 非递归前序遍历要先压右孩子再压左孩子，否则访问顺序会变成 `根 -> 右 -> 左`。
- 非递归后序遍历如果用反转法，要先得到 `根 -> 右 -> 左`，再反转成 `左 -> 右 -> 根`。
- 构造二叉树时左右区间边界容易写错，要先算左子树大小。
- Python 递归深度有限，极端链状树可能需要改成迭代写法或调整递归深度。

---

## 相关变形

- N 叉树：一个节点有多个孩子，DFS 和 BFS 思想不变。
- 二叉搜索树：在二叉树基础上增加左小右大的有序性质。
- 字典树 Trie：用树结构存字符串前缀。
- 堆：常用数组表示的完全二叉树。
- 线段树：用于区间查询和区间更新的树形结构。

---

## 记忆口诀

```text
先想当前节点，再问左右子树；遍历看位置，答案靠返回。
```
