"""
常用算法模板
"""

# =========================
# 并查集 Union Find
# =========================


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

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
        return self.find(a) == self.find(b)


# =========================
# 二叉树 binary tree
# =========================

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def preorder_traversal_iter(root):
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


def preorder_traversal_iter_push(root):
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


def postorder_traversal_iter(root):
    ans = []
    stack = []
    node = root
    last_visited = None

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        peek = stack[-1]

        if peek.right and last_visited is not peek.right:
            node = peek.right
        else:
            ans.append(peek.val)
            last_visited = stack.pop()

    return ans


def postorder_traversal_iter_reverse(root):
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


def max_depth(root):
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return max(left_depth, right_depth) + 1


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
    return 0


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


def has_path_sum(root, target_sum):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target_sum

    remain = target_sum - root.val

    return has_path_sum(root.left, remain) or has_path_sum(root.right, remain)


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


def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left or right


def is_valid_bst(root):
    def dfs(node, low, high):
        if not node:
            return True

        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False

        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, None, None)


def search_bst(root, val):
    while root:
        if root.val == val:
            return root
        if val < root.val:
            root = root.left
        else:
            root = root.right
    return None


def build_tree(preorder, inorder):
    if not preorder:
        return None

    index = {value: i for i, value in enumerate(inorder)}

    def dfs(pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right:
            return None

        root_value = preorder[pre_left]
        root = TreeNode(root_value)

        root_index = index[root_value]
        left_size = root_index - in_left

        root.left = dfs(pre_left + 1, pre_left + left_size, in_left, root_index - 1)
        root.right = dfs(pre_left + left_size + 1, pre_right, root_index + 1, in_right)

        return root

    return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
