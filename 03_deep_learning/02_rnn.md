# 🧠 RNN（循环神经网络）

> 标签：#深度学习 #神经网络 #模型 #RNN #序列

---

## 📌 一句话总结

RNN 是一种用于处理序列数据的神经网络，它通过隐藏状态 `hidden state` 把前面时间步的信息传递到后面时间步。

---

## 🔍 核心问题

RNN 主要解决序列建模问题。

- 任务类型：文本 / 时间序列 / 语音 / 序列分类 / 序列预测
- 输入是什么：按时间顺序排列的数据，例如单词序列、时间序列数值
- 输出是什么：类别、下一个时间步的预测值、每个时间步的标签等
- 适合什么样的数据：前后顺序重要、当前结果依赖历史信息的数据
- 不适合什么样的数据：超长序列、需要强并行计算、长距离依赖特别强的数据

RNN 最核心的问题是：

```text
如何让模型记住前面出现过的信息，并用这些信息影响后面的判断。
```

---

## 🧩 核心思想

RNN 的本质是：同一个神经网络在不同时间步反复使用，并不断更新隐藏状态。

普通神经网络每次只看当前输入，而 RNN 会同时看：

```text
当前输入 + 上一个时间步留下来的记忆
```

重点理解：

1. 信息是怎么流动的？
   每个时间步接收当前输入 `x_t` 和上一个隐藏状态 `h_{t-1}`，计算出新的隐藏状态 `h_t`，再传给下一个时间步。

2. 模型学到的是什么？
   模型学到如何把历史信息压缩进 hidden state，并用它辅助当前判断。

3. 为什么比普通神经网络强？
   普通神经网络无法自然处理顺序关系，RNN 能让前面的信息影响后面的输出。

4. 它解决了旧方法的什么问题？
   它让神经网络具备了处理变长序列和时间依赖的能力。

---

## ⚙️ 模型结构

### 结构组成

- 输入序列 `x_t`：每个时间步的输入
- 隐藏状态 `h_t`：当前时间步的记忆
- 循环单元 `RNN Cell`：负责更新隐藏状态
- 输出层 `Linear`：把隐藏状态转换成最终预测结果

### 数据流动

```text
x_1 -> RNN Cell -> h_1
x_2 + h_1 -> RNN Cell -> h_2
x_3 + h_2 -> RNN Cell -> h_3
...
x_t + h_{t-1} -> RNN Cell -> h_t -> 输出
```

简写：

```text
输入序列 -> RNN 层 -> hidden state -> 全连接层 -> 输出
```

### 张量形状

PyTorch 中如果设置 `batch_first=True`：

```text
输入形状: (batch_size, sequence_length, input_size)
输出形状: (batch_size, sequence_length, hidden_size)
最后隐藏状态: (num_layers, batch_size, hidden_size)
```

示例：

```text
输入: (32, 10, 8)
含义: 32 个样本，每个样本 10 个时间步，每个时间步 8 个特征

RNN 输出: (32, 10, 64)
含义: 每个时间步输出一个 64 维隐藏状态

最后隐藏状态: (1, 32, 64)
含义: 1 层 RNN，32 个样本，每个样本最后记忆是 64 维
```

---

## 🔥 核心机制

### 1. hidden state

`hidden state` 是 RNN 的记忆。

它保存前面时间步的信息，并传给下一个时间步。

```text
h_t = 当前时间步的记忆
h_{t-1} = 上一个时间步的记忆
```

如果没有 hidden state，模型就只能看当前输入，无法利用历史信息。

---

### 2. 时间步传递

RNN 会按照序列顺序一步一步处理数据。

```text
第 1 个词 -> 第 2 个词 -> 第 3 个词 -> ...
```

每一步都使用同一套参数，所以 RNN 可以处理不同长度的序列。

---

### 3. 参数共享

RNN 在所有时间步使用同一个 RNN Cell。

好处：

- 参数量不会随着序列长度增加而增加
- 可以处理变长序列
- 能学习通用的序列变化规律

---

### 4. 梯度消失和梯度爆炸

RNN 需要把梯度沿着时间步往回传。

如果序列很长，梯度可能会：

```text
越来越小 -> 梯度消失
越来越大 -> 梯度爆炸
```

这会导致 RNN 难以学习长距离依赖。

LSTM 和 GRU 就是为了解决普通 RNN 记忆能力不足的问题。

---

## 🔢 数学表达

RNN 的核心公式可以简化为：

```text
h_t = tanh(W_x x_t + W_h h_{t-1} + b)
y_t = W_y h_t + c
```

说明：

- `x_t`：当前时间步的输入
- `h_{t-1}`：上一个时间步的隐藏状态
- `h_t`：当前时间步的隐藏状态
- `y_t`：当前时间步的输出
- `W_x`：输入到隐藏状态的权重
- `W_h`：隐藏状态到隐藏状态的权重
- `W_y`：隐藏状态到输出的权重

---

## ✅ 优点

- 适合处理序列数据。
- 能利用历史信息影响当前输出。
- 参数在时间步之间共享，可以处理变长序列。
- 结构比 LSTM、Transformer 更简单。

---

## ⚠️ 缺点

- 难以学习长距离依赖。
- 容易出现梯度消失或梯度爆炸。
- 训练速度较慢，因为时间步之间难以完全并行。
- 在很多任务上已经被 LSTM、GRU、Transformer 替代。

---

## 🎯 适用场景

- 简单时间序列预测
- 短文本分类
- 序列标注基础模型
- 语音信号基础建模
- 学习序列模型原理

---

## 🚫 不适用场景

- 很长的文本序列
- 长距离依赖很强的任务
- 需要高并行训练的大规模任务
- 对效果要求很高的现代 NLP 任务

---

## 🧪 评价指标

分类任务：

```text
Accuracy / Precision / Recall / F1 / AUC
```

序列标注任务：

```text
Token Accuracy / Precision / Recall / F1
```

时间序列回归任务：

```text
MSE / RMSE / MAE
```

语言模型任务：

```text
Perplexity
```

---

## 💻 PyTorch 代码模板

```python
import torch
import torch.nn as nn


class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()

        self.rnn = nn.RNN(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=1,
            batch_first=True,
        )
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        output, h_n = self.rnn(x)

        # 取最后一个时间步的输出做分类
        last_output = output[:, -1, :]
        logits = self.fc(last_output)

        return logits


model = SimpleRNN(input_size=8, hidden_size=64, num_classes=3)

dummy_x = torch.randn(32, 10, 8)
output = model(dummy_x)
print(output.shape)  # torch.Size([32, 3])
```

---

## 🏋️ 训练流程

1. 准备序列数据
2. 将序列转换成张量
3. 处理变长序列，例如 padding
4. 定义 RNN 模型
5. 定义损失函数
6. 定义优化器
7. 前向传播
8. 计算损失
9. 反向传播
10. 更新参数
11. 在验证集上评估模型

示例：

```python
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for x, y in dataloader:
    optimizer.zero_grad()
    y_pred = model(x)
    loss = criterion(y_pred, y)
    loss.backward()
    optimizer.step()
```

---

## 🔧 重要参数

| 参数 | 含义 | 调大影响 | 调小影响 |
| --- | --- | --- | --- |
| `input_size` | 每个时间步的特征维度 | 输入信息更多 | 输入信息更少 |
| `hidden_size` | 隐藏状态维度 | 表达能力更强，参数更多 | 表达能力更弱，参数更少 |
| `num_layers` | RNN 层数 | 模型更深，表达更强 | 模型更简单 |
| `batch_first` | batch 维度是否放第一维 | 输入更符合常用习惯 `(N, T, D)` | 默认是 `(T, N, D)` |
| `bidirectional` | 是否使用双向 RNN | 同时看前后文 | 只能看过去信息 |

---

## 🧯 易错点

- PyTorch 默认输入形状是 `(sequence_length, batch_size, input_size)`，设置 `batch_first=True` 后才是 `(batch_size, sequence_length, input_size)`。
- `output` 包含每个时间步的隐藏状态，`h_n` 是最后的隐藏状态。
- 做序列分类时，常用最后一个时间步的输出 `output[:, -1, :]`。
- 普通 RNN 不擅长长距离依赖，长序列任务优先考虑 LSTM、GRU 或 Transformer。
- 分类任务最后一层通常输出 logits，不需要手动加 `softmax` 再传给 `CrossEntropyLoss`。
- 变长序列需要 padding，必要时使用 `pack_padded_sequence`。

---

## 🔁 和其他模型的对比

| 模型 | 主要用途 | 核心机制 | 优点 | 缺点 |
| --- | --- | --- | --- | --- |
| RNN | 序列 | hidden state | 结构简单，能处理序列 | 长距离依赖弱，并行能力差 |
| LSTM | 序列 | 门控机制 | 更擅长长距离依赖 | 参数更多，计算更复杂 |
| GRU | 序列 | 简化门控 | 比 LSTM 简洁，效果通常不错 | 表达能力略弱于 LSTM |
| Transformer | 序列 / 多模态 | attention | 并行能力强，长距离依赖好 | 计算量较大 |

---

## 🧠 记忆口诀

```text
当前输入加旧记忆，
一步一步往后传；
短序列能处理，
长依赖找 LSTM 或 Transformer。
```

---

## 📚 常见面试问题

1. RNN 为什么适合处理序列数据？
2. 什么是 hidden state？
3. RNN 的输入和输出形状是什么？
4. `output` 和 `h_n` 有什么区别？
5. RNN 为什么会出现梯度消失？
6. RNN 为什么不擅长长距离依赖？
7. LSTM 和 RNN 有什么区别？
8. 为什么 Transformer 在很多任务上替代了 RNN？
