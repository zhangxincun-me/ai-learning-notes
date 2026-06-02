# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在本仓库中工作时提供指引。

## 仓库概述

个人 AI 学习笔记仓库 (ai-learning-notes)，所有笔记使用**简体中文**撰写。涵盖算法、机器学习、深度学习，后续将扩展至 LLM/RAG/Agent 方向。

## 常用命令

本仓库无构建系统、包管理器或依赖文件。Python 代码仅使用标准库。

```bash
# 运行算法模板（尚无测试用例，pytest 已配置但未使用）
python 01_algorithms/algorithm_templates.py

# 运行 pytest（VSCode 中已配置，测试目录：00_index/）
pytest 00_index/
```

Python 环境：conda，Python 3.13。

## 目录结构

```
00_index/               # 预留目录（当前为空）
01_algorithms/          # 算法笔记 + algorithm_templates.py
02_machine_learning/    # 机器学习笔记（sklearn 代码示例）
03_deep_learning/       # 深度学习笔记（PyTorch 代码示例）
```

每个主题目录下有一个 `00_template` 文件（无扩展名），定义笔记结构。新建笔记时从该模板复制。

`01_algorithms/algorithm_templates.py` 是唯一的 Python 文件，包含可复用的算法实现（UnionFind、TreeNode、遍历、BST 操作等）。仅使用标准库中的 `collections.deque`。

## 笔记写作规范

- **四问原则**：每篇笔记必须回答：(1) 这个概念/模型/算法是什么？(2) 解决什么核心问题？(3) 本质思路是什么？(4) 如何写代码或在面试/做题中表达？
- **文件命名**：`NN_主题名.md`，序号递增（`01_`、`02_`、...）。模板文件为 `00_template`。
- **标签行**：每篇笔记以 `> 标签：#算法 #数据结构 #模板题` 开头
- **章节标题**：使用 emoji 装饰的 `##` 标题（如 `## 一句话总结`、`## 核心问题`）
- **章节分隔**：使用 `---` 水平线
- **数学公式**：使用 `$$...$$` 块书写 LaTeX
- **代码块**：Python 代码用 ` ```python `，概念性文字用 ` ```text `
- **图片**：与相关 `.md` 文件存放在同一目录下（如 `union_find.png` 在 `01_algorithms/` 中）

### 模板章节

**算法笔记**：做题心得、一句话总结、核心问题、核心思路、核心操作/步骤、模板代码、复杂度分析、常见题型、易错点、变体、记忆口诀

**机器学习笔记**（额外包含）：数学表达式 (LaTeX)、工作流程、输入/输出、优缺点、适用/不适用场景、评估指标、重要参数表、sklearn 代码示例、模型对比表、常见面试题

**深度学习笔记**（额外包含）：模型结构（层数/数据流/张量形状）、核心机制、PyTorch 代码模板、训练工作流程

## 规划扩展方向

- 算法：BFS、DFS、贪心、图算法
- 机器学习：线性回归、逻辑回归、决策树
- 深度学习：LSTM/GRU、Transformer、损失函数、优化器、训练技巧
- 未来目录：`04_llm/`、`05_rag/`、`06_agent/`、项目总结
