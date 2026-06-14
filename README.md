# AI Learning Notes

这是我的 AI 学习笔记仓库，用来长期整理算法、机器学习、深度学习以及后续 LLM / RAG / 项目相关内容。

当前阶段先保持目录精简，重点把基础笔记模板和第一批核心内容写扎实。

## 当前目录结构

```text
AI-Learning-Notes/
├── README.md
├── 01_algorithms/
│   ├── 00_template
│   ├── 01_union_find.md
│   ├── 02_dynamic_programming.md
│   ├── 03_binary_tree.md
│   ├── 04_binary_search.md
│   ├── 05_sorting.md
│   ├── 06_graph.md
│   ├── algorithm_templates.py
│   └── union_find.png
├── 02_machine_learning/
│   ├── 00_template
│   └── 01_svm.md
├── 03_deep_learning/
│   ├── 00_template
│   ├── 01_cnn.md
│   └── 02_rnn.md
└── 04_llm/
    ├── 00_template
    └── 01_llm_application_interview.md
```

## 目录说明

### 01_algorithms

算法与数据结构笔记。

主要用于整理：

- 并查集
- BFS / DFS
- 动态规划
- 二分查找
- 贪心
- 图论
- 高频刷题模板

当前已有：

- [算法笔记模板](./01_algorithms/00_template)
- [并查集](./01_algorithms/01_union_find.md)
- [动态规划](./01_algorithms/02_dynamic_programming.md)
- [二叉树](./01_algorithms/03_binary_tree.md)
- [二分查找](./01_algorithms/04_binary_search.md)
- [排序算法](./01_algorithms/05_sorting.md)
- [图算法](./01_algorithms/06_graph.md)

### 02_machine_learning

传统机器学习笔记。

后续计划整理：

- 线性回归
- 逻辑回归
- 决策树
- SVM
- 模型评估

当前已有：

- [机器学习笔记模板](./02_machine_learning/00_template)
- [SVM](./02_machine_learning/01_svm.md)

### 03_deep_learning

深度学习笔记。

后续计划整理：

- CNN
- RNN
- LSTM / GRU
- Transformer
- Loss Function
- Optimizer
- Training Tricks

当前已有：

- [深度学习笔记模板](./03_deep_learning/00_template)
- [CNN](./03_deep_learning/01_cnn.md)
- [RNN](./03_deep_learning/02_rnn.md)

### 04_llm

大模型应用开发笔记。

主要用于整理：

- LLM 基础
- Prompt Engineering
- RAG
- 微调
- Agent
- 推理部署
- 评估与可观测性
- 面试题和项目总结

当前已有：

- [大模型笔记模板](./04_llm/00_template)
- [大模型应用开发面试笔记](./04_llm/01_llm_application_interview.md)

## 笔记写作原则

每篇笔记尽量回答 4 个问题：

1. 这个概念 / 模型 / 算法是干嘛的？
2. 它解决什么核心问题？
3. 它的本质思想是什么？
4. 面试或实战中怎么写代码、怎么表达？

算法笔记里的模板代码优先使用教材版基础写法，重点保证步骤清楚、变量直观、方便手写。随机化、工程优化、三路划分等进阶版本可以作为补充说明，但不作为主模板。

## 学习路线

当前优先级：

1. 先补算法基础，重点写模板和高频题型。
2. 再整理传统机器学习模型，建立基本建模思维。
3. 然后进入深度学习，重点理解 CNN、RNN、Transformer。
4. 后续扩展到 LLM、RAG、Agent 和项目总结。

## 使用方式

- 新增算法笔记时，从 `01_algorithms/00_template` 复制结构。
- 新增机器学习笔记时，从 `02_machine_learning/00_template` 复制结构。
- 新增深度学习笔记时，从 `03_deep_learning/00_template` 复制结构。
- 新增大模型应用笔记时，从 `04_llm/00_template` 复制结构。
- 每篇笔记都尽量补充一句话总结、核心思想和代码模板。

## 后续计划

- 继续完善 `01_algorithms/algorithm_templates.py`
- 新增 BFS、DFS、贪心、图论笔记
- 修正并完善机器学习和深度学习模板
- 按主题拆分并完善 LLM / RAG / Agent / 项目总结笔记

