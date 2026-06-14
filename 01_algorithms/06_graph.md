# 图算法

> 标签：#算法 #数据结构 #图 #DFS #BFS #最短路径 #最小生成树 #拓扑排序

---

## 做题心得

图题最容易乱，是因为图不像树那样天然有根，也不一定没有环。写代码前先把三个问题想清楚：

- 这是无向图还是有向图？
- 边有没有权值？权值有没有负数？
- 需要处理的是遍历、连通性、最短路径、生成树，还是依赖关系？

常用判断：

- 只要求访问所有点或判断能不能到达，优先想 DFS / BFS。
- 无权图最短路径，优先想 BFS。
- 非负权最短路径，优先想 Dijkstra。
- 可能有负权边，优先想 Bellman-Ford；多源最短路径想 Floyd。
- 无向连通网的最低总代价，想最小生成树：Prim 或 Kruskal。
- 有向无环图的先后顺序，想拓扑排序。
- 工程活动最早/最晚开始时间，想 AOE 网和关键路径。

图算法里 `visited`、`dist`、`indegree`、`parent` 这些数组很关键，变量含义想清楚，代码就不容易散。

---

## 一句话总结

图算法解决的是“点和边组成的关系网络”中的访问、连通、路径、代价、依赖顺序和关键活动问题。

---

## 核心问题

图可以表示任意对象之间的关系。

常见输入：

- 顶点数 `n`。
- 边列表 `edges`，例如 `(u, v)` 或 `(u, v, w)`。
- 有向 / 无向、带权 / 不带权的信息。
- 起点 `start`、终点 `target`。

常见输出：

- 遍历序列。
- 是否连通、连通分量数量。
- 从一个点到另一个点的路径或最短距离。
- 最小生成树的边和权值总和。
- 拓扑序列。
- 关键路径和关键活动。

适用场景：

- 地图、道路、网络路由。
- 课程先修关系、任务依赖。
- 社交网络、推荐关系。
- 数据结构课本中的网、AOV 网、AOE 网。
- 搜索、路径规划、连通性判断。

不适用场景：

- 数据天然是线性顺序，数组、链表、栈、队列更简单。
- 数据天然是父子层级且无环，树算法更直接。
- 只需要集合合并和连通性查询，并查集可能更轻。

---

## 基本概念

### 1. 图的定义

图记作：

```text
G = (V, E)
```

- `V`：顶点集合，也叫结点集合。
- `E`：边集合，表示顶点之间的关系。

如果一条边没有方向，叫无向边，例如 `(u, v)`。

如果一条边有方向，叫有向边，也叫弧，例如 `<u, v>`，表示从 `u` 指向 `v`。

### 2. 图的分类

按方向分：

- 无向图：边没有方向。
- 有向图：边有方向。

按权值分：

- 无权图：边只表示是否相连。
- 带权图 / 网：边上带有权值，例如距离、费用、时间。

按边的多少分：

- 稀疏图：边比较少，常用邻接表。
- 稠密图：边比较多，常用邻接矩阵。

常见特殊图：

- 完全图：任意两个顶点之间都有边。
- 连通图：无向图中任意两个顶点都有路径相通。
- 强连通图：有向图中任意两个顶点 `u`、`v`，`u` 能到 `v`，`v` 也能到 `u`。
- DAG：有向无环图，常用于拓扑排序。
- 生成树：包含图中全部顶点、且边数为 `n - 1` 的连通无环子图。

### 3. 度

无向图：

- 顶点的度：与该顶点相连的边数。
- 所有顶点度数之和等于边数的两倍。

```text
sum(degree) = 2 * |E|
```

有向图：

- 入度：指向该顶点的边数。
- 出度：从该顶点指出去的边数。
- 所有顶点入度之和 = 所有顶点出度之和 = 边数。

```text
sum(indegree) = sum(outdegree) = |E|
```

### 4. 路径、回路、连通

- 路径：顶点序列 `v0, v1, ..., vk`，相邻顶点之间都有边。
- 路径长度：无权图中通常指边数，带权图中通常指权值和。
- 简单路径：路径中顶点不重复。
- 回路 / 环：起点和终点相同的路径。
- 简单回路：除起点终点外，其余顶点不重复。
- 连通分量：无向图中的极大连通子图。
- 强连通分量：有向图中的极大强连通子图。

---

## 存储结构

### 1. 邻接矩阵

用二维数组 `graph[i][j]` 表示 `i` 到 `j` 是否有边，或边的权值。

无权图：

```text
graph[i][j] = 1 表示有边
graph[i][j] = 0 表示无边
```

带权图：

```text
graph[i][j] = w   表示边权
graph[i][j] = INF 表示无边
```

特点：

- 判断两点是否相邻很快：$O(1)$。
- 枚举一个点的所有邻居较慢：$O(n)$。
- 空间复杂度固定：$O(n^2)$。
- 更适合稠密图。

```python
def build_matrix(n, edges, directed=False, weighted=False):
    if weighted:
        INF = float("inf")
        graph = [[INF] * n for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0

        for u, v, w in edges:
            graph[u][v] = w
            if not directed:
                graph[v][u] = w
    else:
        graph = [[0] * n for _ in range(n)]

        for u, v in edges:
            graph[u][v] = 1
            if not directed:
                graph[v][u] = 1

    return graph
```

对应类写法：

```python
class AdjacencyMatrixGraph:
    def __init__(self, n, directed=False, weighted=False):
        self.n = n
        self.directed = directed
        self.weighted = weighted
        self.INF = float("inf")

        if weighted:
            self.matrix = [[self.INF] * n for _ in range(n)]
            for i in range(n):
                self.matrix[i][i] = 0
        else:
            self.matrix = [[0] * n for _ in range(n)]

    def add_edge(self, u, v, w=1):
        value = w if self.weighted else 1
        self.matrix[u][v] = value

        if not self.directed:
            self.matrix[v][u] = value

    def has_edge(self, u, v):
        if u == v:
            return False

        if self.weighted:
            return self.matrix[u][v] != self.INF

        return self.matrix[u][v] == 1

    def neighbors(self, u):
        result = []

        for v in range(self.n):
            if self.has_edge(u, v):
                if self.weighted:
                    result.append((v, self.matrix[u][v]))
                else:
                    result.append(v)

        return result
```

### 2. 邻接表

用列表保存每个顶点的所有邻居。

无权图：

```python
def build_adj_list(n, edges, directed=False):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)

    return graph
```

带权图：

```python
def build_weighted_adj_list(n, edges, directed=False):
    graph = [[] for _ in range(n)]

    for u, v, w in edges:
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))

    return graph
```

对应类写法：

```python
class AdjacencyListGraph:
    def __init__(self, n, directed=False, weighted=False):
        self.n = n
        self.directed = directed
        self.weighted = weighted
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, w=1):
        if self.weighted:
            self.graph[u].append((v, w))
            if not self.directed:
                self.graph[v].append((u, w))
        else:
            self.graph[u].append(v)
            if not self.directed:
                self.graph[v].append(u)

    def has_edge(self, u, v):
        if self.weighted:
            for to, _ in self.graph[u]:
                if to == v:
                    return True
            return False

        return v in self.graph[u]

    def neighbors(self, u):
        return self.graph[u]
```

特点：

- 枚举邻居很快。
- 空间复杂度：$O(n + e)$。
- 判断两点是否直接相邻通常要扫描邻接表。
- 更适合稀疏图。

### 3. 存储结构对比

| 存储方式 | 空间复杂度 | 判断是否有边 | 枚举邻居 | 适合场景 |
| --- | --- | --- | --- | --- |
| 邻接矩阵 | $O(n^2)$ | $O(1)$ | $O(n)$ | 稠密图、Floyd |
| 邻接表 | $O(n + e)$ | $O(degree)$ | $O(degree)$ | 稀疏图、DFS、BFS |

学习和做题时，优先掌握这两种存储结构就够了。后面的 Kruskal、Bellman-Ford 会直接使用题目给出的 `edges` 边列表作为输入，不再把它单独当作一种存储结构讲。

如果用上面的类来建图：

- 需要邻接矩阵算法时，传入 `matrix_graph.matrix`。
- 需要邻接表算法时，传入 `list_graph.graph`。

---

## 图的遍历

图的遍历就是从某个顶点出发，按某种规则访问所有能到达的顶点。

图和树最大的区别：

- 图可能有环。
- 一个顶点可能被多条路径到达。
- 所以必须用 `visited` 防止重复访问。

### 1. DFS 深度优先搜索

核心思想：

```text
从当前点出发，能往深处走就继续走；走不动再回溯。
```

递归版：

```python
def dfs(graph, start):
    n = len(graph)
    visited = [False] * n
    order = []

    def visit(u):
        visited[u] = True
        order.append(u)

        for v in graph[u]:
            if not visited[v]:
                visit(v)

    visit(start)
    return order
```

非递归版：

```python
def dfs_iterative(graph, start):
    n = len(graph)
    visited = [False] * n
    order = []
    stack = [start]

    while stack:
        u = stack.pop()

        if visited[u]:
            continue

        visited[u] = True
        order.append(u)

        for v in reversed(graph[u]):
            if not visited[v]:
                stack.append(v)

    return order
```

复杂度：

- 邻接表：$O(n + e)$。
- 邻接矩阵：$O(n^2)$。

### 2. BFS 广度优先搜索

核心思想：

```text
从起点开始，一层一层向外扩展。
```

BFS 使用队列。

```python
from collections import deque


def bfs(graph, start):
    n = len(graph)
    visited = [False] * n
    order = []
    queue = deque([start])
    visited[start] = True

    while queue:
        u = queue.popleft()
        order.append(u)

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return order
```

复杂度：

- 邻接表：$O(n + e)$。
- 邻接矩阵：$O(n^2)$。

### 3. 遍历非连通图

如果图不连通，只从一个起点出发不能访问全部顶点。

```python
def traverse_all(graph):
    n = len(graph)
    visited = [False] * n
    components = []

    def dfs(u, component):
        visited[u] = True
        component.append(u)

        for v in graph[u]:
            if not visited[v]:
                dfs(v, component)

    for i in range(n):
        if not visited[i]:
            component = []
            dfs(i, component)
            components.append(component)

    return components
```

这个模板可以求无向图的连通分量。

### 4. BFS 求无权图最短路径

无权图中，每条边长度都可以看作 `1`。BFS 第一次到达某个点时，经过的边数就是最短距离。

```python
from collections import deque


def shortest_path_unweighted(graph, start):
    n = len(graph)
    dist = [-1] * n
    parent = [-1] * n
    queue = deque([start])
    dist[start] = 0

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)

    return dist, parent
```

还原路径：

```python
def restore_path(parent, start, target):
    path = []
    cur = target

    while cur != -1:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]

    if not path or path[-1] != start:
        return []

    path.reverse()
    return path
```

---

## 连通性和环

### 1. 无向图连通性

判断无向图是否连通：

```python
def is_connected(graph):
    n = len(graph)
    if n == 0:
        return True

    visited = [False] * n

    def dfs(u):
        visited[u] = True

        for v in graph[u]:
            if not visited[v]:
                dfs(v)

    dfs(0)
    return all(visited)
```

### 2. 无向图判环

DFS 时，如果遇到已经访问过的邻居，且这个邻居不是父节点，说明有环。

```python
def has_cycle_undirected(graph):
    n = len(graph)
    visited = [False] * n

    def dfs(u, parent):
        visited[u] = True

        for v in graph[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True

        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True

    return False
```

### 3. 有向图判环

有向图常用三色标记：

- `0`：未访问。
- `1`：正在访问，位于当前递归栈中。
- `2`：已经访问完成。

如果从当前点走到状态为 `1` 的点，说明存在环。

```python
def has_cycle_directed(graph):
    n = len(graph)
    state = [0] * n

    def dfs(u):
        state[u] = 1

        for v in graph[u]:
            if state[v] == 0:
                if dfs(v):
                    return True
            elif state[v] == 1:
                return True

        state[u] = 2
        return False

    for i in range(n):
        if state[i] == 0:
            if dfs(i):
                return True

    return False
```

---

## 最小生成树

最小生成树用于无向连通带权图。

目标：

```text
选出 n - 1 条边，连接所有顶点，并让边权总和最小。
```

注意：

- 最小生成树一定没有环。
- 最小生成树边数一定是 `n - 1`。
- 图不连通时不存在包含所有顶点的生成树，只能得到生成森林。

### 1. Prim 算法

核心思想：

```text
从一个顶点集合开始，每次选一条连接集合内外的最小边。
```

适合邻接矩阵，也适合稠密图。

教材版邻接矩阵写法：

```python
def prim(matrix):
    n = len(matrix)
    if n == 0:
        return 0, []

    INF = float("inf")
    visited = [False] * n
    low_cost = [INF] * n
    parent = [-1] * n

    low_cost[0] = 0
    total = 0

    for _ in range(n):
        u = -1
        min_cost = INF

        for i in range(n):
            if not visited[i] and low_cost[i] < min_cost:
                min_cost = low_cost[i]
                u = i

        if u == -1:
            return None

        visited[u] = True
        total += min_cost

        for v in range(n):
            if not visited[v] and matrix[u][v] < low_cost[v]:
                low_cost[v] = matrix[u][v]
                parent[v] = u

    mst_edges = []
    for v in range(1, n):
        mst_edges.append((parent[v], v, low_cost[v]))

    return total, mst_edges
```

复杂度：

- 邻接矩阵教材版：$O(n^2)$。
- 堆优化邻接表：$O(e \log n)$。

### 2. Kruskal 算法

核心思想：

```text
把所有边按权值从小到大排序，每次选不会形成环的边。
```

适合直接对边列表排序，常用于稀疏图。

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        self.parent[root_b] = root_a
        return True


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    total = 0
    mst_edges = []

    for u, v, w in edges:
        if uf.union(u, v):
            total += w
            mst_edges.append((u, v, w))

            if len(mst_edges) == n - 1:
                break

    if len(mst_edges) != n - 1:
        return None

    return total, mst_edges
```

复杂度：

- 排序：$O(e \log e)$。
- 并查集操作近似 $O(1)$。
- 总复杂度：$O(e \log e)$。

### 3. Prim 和 Kruskal 对比

| 算法 | 核心选择 | 常用表示 | 适合图 | 判环方式 |
| --- | --- | --- | --- | --- |
| Prim | 每次选离当前顶点集合最近的点 | 邻接矩阵 / 邻接表 | 稠密图 | 不需要显式判环 |
| Kruskal | 每次选当前最小且不成环的边 | 边列表 | 稀疏图 | 并查集 |

---

## 最短路径

最短路径分为：

- 单源最短路径：从一个起点到其他所有点。
- 单源单终点最短路径：从一个起点到一个终点。
- 多源最短路径：任意两点之间的最短路径。

选择算法时先看边权：

| 场景 | 推荐算法 |
| --- | --- |
| 无权图 | BFS |
| 非负权图 | Dijkstra |
| 有负权边 | Bellman-Ford |
| 任意两点最短路径 | Floyd |
| DAG 上最短路径 | 拓扑序动态规划 |

### 1. Dijkstra 算法

适用条件：

- 单源最短路径。
- 边权非负。

核心思想：

```text
每次选出当前距离起点最近、且还未确定的顶点，然后用它更新其他顶点。
```

教材版邻接矩阵写法：

```python
def dijkstra_matrix(matrix, start):
    n = len(matrix)
    INF = float("inf")
    dist = [INF] * n
    visited = [False] * n
    parent = [-1] * n
    dist[start] = 0

    for _ in range(n):
        u = -1
        min_dist = INF

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if not visited[v] and matrix[u][v] != INF:
                if dist[u] + matrix[u][v] < dist[v]:
                    dist[v] = dist[u] + matrix[u][v]
                    parent[v] = u

    return dist, parent
```

堆优化邻接表写法：

```python
import heapq


def dijkstra(graph, start):
    n = len(graph)
    INF = float("inf")
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cur_dist, u = heapq.heappop(heap)

        if cur_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = cur_dist + weight

            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(heap, (new_dist, v))

    return dist, parent
```

复杂度：

- 邻接矩阵教材版：$O(n^2)$。
- 堆优化邻接表：$O(e \log n)$。

易错点：

- Dijkstra 不能处理负权边。
- `visited[u] = True` 表示 `u` 的最短距离已经确定。
- 堆优化写法可以不用 `visited`，但要跳过过期状态。

### 2. Bellman-Ford 算法

适用条件：

- 单源最短路径。
- 可以处理负权边。
- 可以检测负权回路。

核心思想：

```text
对所有边做 n - 1 轮松弛。
```

如果不存在负权回路，最短路径最多包含 `n - 1` 条边。

```python
def bellman_ford(n, edges, start):
    INF = float("inf")
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = 0

    for _ in range(n - 1):
        updated = False

        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True

        if not updated:
            break

    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None

    return dist, parent
```

复杂度：

- 时间复杂度：$O(n e)$。
- 空间复杂度：$O(n)$。

返回 `None` 表示存在从起点可达的负权回路。

### 3. Floyd 算法

适用条件：

- 多源最短路径。
- 顶点数量不太大。
- 可以处理负权边，但不能有负权回路。

核心思想：

```text
依次尝试把每个顶点 k 作为中转点，更新 i 到 j 的最短距离。
```

```python
def floyd(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]
    next_node = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if dist[i][j] != float("inf") and i != j:
                next_node[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node
```

还原 `start` 到 `target` 的路径：

```python
def restore_floyd_path(next_node, start, target):
    if start == target:
        return [start]

    if next_node[start][target] == -1:
        return []

    path = [start]

    while start != target:
        start = next_node[start][target]
        path.append(start)

    return path
```

复杂度：

- 时间复杂度：$O(n^3)$。
- 空间复杂度：$O(n^2)$。

### 4. 最短路径算法对比

| 算法 | 解决问题 | 能否处理负权边 | 能否检测负权回路 | 时间复杂度 |
| --- | --- | --- | --- | --- |
| BFS | 无权图单源最短路径 | 不涉及 | 不能 | $O(n + e)$ |
| Dijkstra | 非负权单源最短路径 | 不能 | 不能 | $O(n^2)$ 或 $O(e \log n)$ |
| Bellman-Ford | 单源最短路径 | 能 | 能 | $O(n e)$ |
| Floyd | 多源最短路径 | 能 | 可通过 `dist[i][i] < 0` 判断 | $O(n^3)$ |

---

## 拓扑排序

拓扑排序用于有向无环图，也就是 DAG。

典型场景：

- 课程先修关系。
- 编译依赖。
- 任务调度。
- AOV 网。

拓扑序要求：

```text
如果存在边 u -> v，那么 u 必须排在 v 前面。
```

如果图中有环，则不存在拓扑序。

### 1. Kahn 算法

核心思想：

```text
不断取出入度为 0 的顶点，并删除它指出去的边。
```

```python
from collections import deque


def topological_sort(n, edges):
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    order = []

    while queue:
        u = queue.popleft()
        order.append(u)

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if len(order) != n:
        return []

    return order
```

复杂度：

- 时间复杂度：$O(n + e)$。
- 空间复杂度：$O(n + e)$。

### 2. DFS 拓扑排序

DFS 完成一个顶点后，把它放入结果。最后反转结果。

```python
def topological_sort_dfs(graph):
    n = len(graph)
    state = [0] * n
    order = []

    def dfs(u):
        state[u] = 1

        for v in graph[u]:
            if state[v] == 0:
                if not dfs(v):
                    return False
            elif state[v] == 1:
                return False

        state[u] = 2
        order.append(u)
        return True

    for i in range(n):
        if state[i] == 0:
            if not dfs(i):
                return []

    order.reverse()
    return order
```

---

## AOV 网和 AOE 网

### 1. AOV 网

AOV 网是 Activity On Vertex。

特点：

- 顶点表示活动。
- 有向边表示活动之间的先后关系。
- 通常用拓扑排序解决。

例子：

```text
课程 A -> 课程 B
表示必须先学 A，才能学 B
```

### 2. AOE 网

AOE 网是 Activity On Edge。

特点：

- 顶点表示事件。
- 有向边表示活动。
- 边权表示活动持续时间。
- 通常用于求关键路径。

例子：

```text
事件 u -> 事件 v，权值 w
表示某个活动从事件 u 开始，到事件 v 结束，耗时 w
```

---

## 关键路径

关键路径用于 AOE 网。

目标：

```text
找出从源点到汇点的最长路径，以及不能延误的关键活动。
```

关键概念：

- `ve[i]`：事件 `i` 的最早发生时间。
- `vl[i]`：事件 `i` 的最晚发生时间。
- `e[k]`：活动 `k` 的最早开始时间。
- `l[k]`：活动 `k` 的最晚开始时间。
- 如果 `e[k] == l[k]`，活动 `k` 是关键活动。

求解步骤：

1. 对 AOE 网做拓扑排序。
2. 按拓扑序求每个事件的最早发生时间 `ve`。
3. 按逆拓扑序求每个事件的最晚发生时间 `vl`。
4. 枚举每条边，求活动的 `e` 和 `l`。
5. `e == l` 的活动就是关键活动。

模板：

```python
from collections import deque


def critical_path(n, edges):
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v, w in edges:
        graph[u].append((v, w))
        indegree[v] += 1

    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    topo = []
    ve = [0] * n

    while queue:
        u = queue.popleft()
        topo.append(u)

        for v, w in graph[u]:
            if ve[u] + w > ve[v]:
                ve[v] = ve[u] + w

            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if len(topo) != n:
        return None

    project_time = max(ve)
    vl = [project_time] * n

    for u in reversed(topo):
        for v, w in graph[u]:
            if vl[v] - w < vl[u]:
                vl[u] = vl[v] - w

    key_activities = []

    for u, v, w in edges:
        earliest = ve[u]
        latest = vl[v] - w

        if earliest == latest:
            key_activities.append((u, v, w))

    return project_time, ve, vl, key_activities
```

注意：

- AOE 网必须是 DAG。
- 数据结构课本里的 AOE 网通常有一个源点和一个汇点；如果有多个汇点，可以加一个耗时为 `0` 的虚拟汇点。
- 关键路径可能不止一条。
- 关键活动延误会导致整个工程延误。
- 非关键活动有一定时间余量。

---

## 强连通分量

强连通分量用于有向图。

定义：

```text
在同一个强连通分量中，任意两个顶点都可以互相到达。
```

### Kosaraju 算法

核心步骤：

1. 在原图上 DFS，记录顶点完成顺序。
2. 把所有边反向。
3. 按完成顺序的逆序，在反图上 DFS。
4. 每次 DFS 得到一个强连通分量。

```python
def kosaraju(graph):
    n = len(graph)
    visited = [False] * n
    order = []

    def dfs1(u):
        visited[u] = True

        for v in graph[u]:
            if not visited[v]:
                dfs1(v)

        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    reverse_graph = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            reverse_graph[v].append(u)

    visited = [False] * n
    components = []

    def dfs2(u, component):
        visited[u] = True
        component.append(u)

        for v in reverse_graph[u]:
            if not visited[v]:
                dfs2(v, component)

    for u in reversed(order):
        if not visited[u]:
            component = []
            dfs2(u, component)
            components.append(component)

    return components
```

复杂度：

- 时间复杂度：$O(n + e)$。
- 空间复杂度：$O(n + e)$。

数据结构课本里有时只要求掌握强连通分量概念，不一定要求写 Tarjan。先掌握 Kosaraju 更容易理解。

---

## 常见算法复杂度速查

设顶点数为 `n`，边数为 `e`。

| 算法 | 主要用途 | 常用表示 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- | --- | --- |
| DFS | 遍历、连通性、判环 | 邻接表 | $O(n + e)$ | $O(n)$ |
| BFS | 遍历、无权最短路径 | 邻接表 | $O(n + e)$ | $O(n)$ |
| Prim | 最小生成树 | 邻接矩阵 | $O(n^2)$ | $O(n)$ |
| Kruskal | 最小生成树 | 边列表 | $O(e \log e)$ | $O(n)$ |
| Dijkstra | 非负权单源最短路径 | 邻接矩阵 / 邻接表 | $O(n^2)$ 或 $O(e \log n)$ | $O(n + e)$ |
| Bellman-Ford | 含负权边单源最短路径 | 边列表 | $O(n e)$ | $O(n)$ |
| Floyd | 多源最短路径 | 邻接矩阵 | $O(n^3)$ | $O(n^2)$ |
| 拓扑排序 | DAG 依赖顺序 | 邻接表 | $O(n + e)$ | $O(n + e)$ |
| 关键路径 | AOE 网工程最短工期 | 邻接表 | $O(n + e)$ | $O(n + e)$ |
| Kosaraju | 强连通分量 | 邻接表 | $O(n + e)$ | $O(n + e)$ |

---

## 常见题型

- 给出图，写出 DFS / BFS 遍历序列。
- 判断无向图是否连通。
- 求无向图的连通分量个数。
- 判断无向图或有向图是否有环。
- 求无权图从起点到各点的最短距离。
- 求带权图的单源最短路径。
- 求任意两点之间的最短路径。
- 求最小生成树的权值和。
- 判断课程安排是否可完成。
- 输出一个合法的拓扑序。
- 根据 AOE 网求关键路径。
- 判断一个有向图的强连通分量。

---

## 易错点

- 无向图建邻接表时，一条边要加两次：`u -> v` 和 `v -> u`。
- 有向图建边时不要反向添加。
- 图遍历必须记录 `visited`，否则有环时会无限递归。
- BFS 一般在入队时标记访问，避免同一个点重复入队。
- 无权最短路径用 BFS，不需要 Dijkstra。
- Dijkstra 不能处理负权边。
- Floyd 三层循环中，`k` 必须放在最外层。
- 拓扑排序只适用于有向无环图。
- 最小生成树只适用于无向连通带权图。
- 关键路径求的是最长路径意义上的工程工期，不是最短路径。
- 邻接矩阵里无边通常用 `INF`，对角线通常是 `0`。
- 顶点编号如果是从 `1` 开始，数组大小要开 `n + 1`。

---

## 相关变形

- 多源 BFS：多个起点同时入队，常用于腐烂橘子、地图扩散。
- 双向 BFS：起点和终点同时扩展，适合状态空间很大的最短步数问题。
- 0-1 BFS：边权只有 `0` 和 `1` 时，用双端队列优化。
- A* 搜索：加入启发函数的最短路径搜索，常用于地图寻路。
- 并查集判连通：适合离线处理无向图连通性。
- 拓扑排序 + DP：适合 DAG 上最长路径、最短路径、方案数。

---

## 选择算法口诀

```text
访问全图 DFS BFS，
无权最短 BFS。
非负单源 Dijkstra，
负权单源 Bellman-Ford。
多源最短用 Floyd，
最小生成 Prim Kruskal。
有向无环拓扑排，
AOE 网找关键线。
```

---

## 复习顺序

建议按下面顺序学：

1. 图的基本概念：顶点、边、度、路径、连通。
2. 图的存储结构：邻接矩阵、邻接表。
3. DFS 和 BFS。
4. 连通分量和判环。
5. 最小生成树：Prim、Kruskal。
6. 最短路径：BFS、Dijkstra、Bellman-Ford、Floyd。
7. 拓扑排序。
8. AOV 网、AOE 网、关键路径。
9. 强连通分量等进阶内容。
