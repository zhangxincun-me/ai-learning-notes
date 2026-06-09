"""
常用算法模板。

这个文件把可复用的算法都整理成类：
- UnionFind：并查集模板。
- TreeNode：二叉树节点。
- BinaryTreeAlgorithms：二叉树常用算法模板。
- SortAlgorithms：常用排序算法模板。
"""

from collections import deque

# =========================
# 并查集 Union Find
# =========================


class UnionFind:
    """并查集：用于维护集合合并和连通性查询。"""

    def __init__(self, n):
        # parent[i] 表示节点 i 的父节点，初始时每个节点都是自己的父节点。
        self.parent = [i for i in range(n)]
        # rank 用来近似表示树的高度，合并时尽量把矮树接到高树下面。
        self.rank = [1] * n
        # count 表示当前连通分量数量。
        self.count = n

    def find(self, x):
        """查找 x 所在集合的根节点，并进行路径压缩。"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        """合并 a 和 b 所在的集合；如果本来已经连通，返回 False。"""
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        # 按秩合并：让高度更小的树接到高度更大的树下面。
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        self.count -= 1
        return True

    def connected(self, a, b):
        """判断 a 和 b 是否属于同一个集合。"""
        return self.find(a) == self.find(b)


# =========================
# 二叉树 Binary Tree
# =========================


class TreeNode:
    """二叉树节点。"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeAlgorithms:
    """
    二叉树常用算法模板。

    使用时可以：
    tree = BinaryTreeAlgorithms()
    root = TreeNode(1)
    tree.preorder_traversal(root)
    """

    def preorder_traversal(self, root):
        """前序遍历：根 -> 左 -> 右。"""
        ans = []

        def dfs(node):
            if not node:
                return

            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans

    def inorder_traversal(self, root):
        """中序遍历：左 -> 根 -> 右。"""
        ans = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return ans

    def postorder_traversal(self, root):
        """后序遍历：左 -> 右 -> 根。"""
        ans = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)

        dfs(root)
        return ans

    def preorder_traversal_iter(self, root):
        """前序遍历的迭代写法：用栈模拟递归过程。"""
        ans = []
        stack = []
        node = root

        while node or stack:
            while node:
                ans.append(node.val)
                stack.append(node)
                node = node.left

            node = stack.pop()
            node = node.right

        return ans

    def preorder_traversal_iter_push(self, root):
        """前序遍历的迭代写法：先压右孩子，再压左孩子。"""
        if not root:
            return []

        ans = []
        stack = [root]

        while stack:
            node = stack.pop()
            ans.append(node.val)

            # 栈是后进先出，所以先放右孩子，保证左孩子先被访问。
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ans

    def inorder_traversal_iter(self, root):
        """中序遍历的迭代写法：一路向左入栈，再回溯访问根节点。"""
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

    def postorder_traversal_iter(self, root):
        """后序遍历的迭代写法：用 last_visited 记录上一次访问的节点。"""
        ans = []
        stack = []
        node = root
        last_visited = None

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            peek = stack[-1]

            # 如果右子树存在且还没访问过，先转向右子树。
            if peek.right and last_visited is not peek.right:
                node = peek.right
            else:
                ans.append(peek.val)
                last_visited = stack.pop()

        return ans

    def postorder_traversal_iter_reverse(self, root):
        """后序遍历的简化迭代写法：根右左遍历后反转。"""
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

    def level_order(self, root):
        """层序遍历：按层从左到右访问节点。"""
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

    def max_depth(self, root):
        """二叉树最大深度：根节点到最远叶子节点的节点数。"""
        if not root:
            return 0

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        return max(left_depth, right_depth) + 1

    def min_depth(self, root):
        """二叉树最小深度：根节点到最近叶子节点的节点数。"""
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            # BFS 第一次遇到叶子节点时，就是最小深度。
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0

    def is_balanced(self, root):
        """判断是否为平衡二叉树：任意节点左右子树高度差不超过 1。"""

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

    def has_path_sum(self, root, target_sum):
        """判断是否存在一条根到叶子的路径，使路径和等于 target_sum。"""
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == target_sum

        remain = target_sum - root.val

        return self.has_path_sum(root.left, remain) or self.has_path_sum(
            root.right, remain
        )

    def path_sum(self, root, target_sum):
        """返回所有路径和等于 target_sum 的根到叶子路径。"""
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

    def lowest_common_ancestor(self, root, p, q):
        """查找普通二叉树中 p 和 q 的最近公共祖先。"""
        if not root or root == p or root == q:
            return root

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root

        return left or right

    def is_valid_bst(self, root):
        """判断一棵二叉树是否为合法二叉搜索树。"""

        def dfs(node, low, high):
            if not node:
                return True

            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, None, None)

    def search_bst(self, root, val):
        """在二叉搜索树中查找值为 val 的节点。"""
        while root:
            if root.val == val:
                return root
            if val < root.val:
                root = root.left
            else:
                root = root.right

        return None

    def build_tree(self, preorder, inorder):
        """根据前序遍历和中序遍历结果重建二叉树。"""
        if not preorder:
            return None

        # 用哈希表记录中序遍历中每个值的位置，避免递归中反复查找。
        index = {value: i for i, value in enumerate(inorder)}

        def dfs(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            root_value = preorder[pre_left]
            root = TreeNode(root_value)

            root_index = index[root_value]
            left_size = root_index - in_left

            root.left = dfs(pre_left + 1, pre_left + left_size, in_left, root_index - 1)
            root.right = dfs(
                pre_left + left_size + 1, pre_right, root_index + 1, in_right
            )

            return root

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)


# =========================
# 排序 Sorting
# =========================


class SortAlgorithms:
    """常用排序算法模板：统一使用教材版基础写法。"""

    def bubble_sort(self, nums):
        """冒泡排序：相邻元素两两比较，大的元素逐步冒到右边。"""
        n = len(nums)

        for i in range(n - 1):
            for j in range(0, n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums

    def selection_sort(self, nums):
        """选择排序：每一轮从未排序区间中选出最小值，放到当前起点。"""
        n = len(nums)

        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j

            nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums

    def insertion_sort(self, nums):
        """插入排序：左边维护有序区间，把当前元素插入到合适位置。"""
        n = len(nums)

        for i in range(1, n):
            current = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > current:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = current

        return nums

    def shell_sort(self, nums):
        """希尔排序：按 gap 分组做插入排序，再逐步缩小 gap。"""
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

    def merge_sort(self, nums):
        """归并排序：先递归拆成两半，再合并两个有序数组。"""
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self._merge(left, right)

    def _merge(self, left, right):
        """合并两个有序数组。"""
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

    def quick_sort(self, nums):
        """快速排序：教材版左右指针写法。"""

        def sort(left, right):
            if left >= right:
                return

            i = left
            j = right
            pivot = nums[left]

            # 从右边找小于 pivot 的数，从左边找大于 pivot 的数。
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

    def heap_sort(self, nums):
        """堆排序：先建大顶堆，再反复把堆顶最大值放到末尾。"""
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

    def counting_sort(self, nums):
        """计数排序：教材版默认元素都是非负整数。"""
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

    def bucket_sort(self, nums, bucket_count=10):
        """桶排序：按范围分桶，桶内使用插入排序。"""
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
            self.insertion_sort(bucket)
            result.extend(bucket)

        return result

    def radix_sort(self, nums):
        """基数排序：教材版默认元素都是非负整数。"""
        if not nums:
            return nums

        max_value = max(nums)
        exp = 1

        while max_value // exp > 0:
            nums = self._counting_sort_by_digit(nums, exp)
            exp *= 10

        return nums

    def _counting_sort_by_digit(self, nums, exp):
        """按某一位数字做稳定计数排序。"""
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


























