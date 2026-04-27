# 🧠 CNN（卷积神经网络）

> 标签：#深度学习 #神经网络 #模型 #CNN #图像

---

## 📌 一句话总结

CNN 是一种特别适合处理图像数据的神经网络，它通过卷积核自动提取局部特征，再逐层组合成更高级的图像语义。

---

## 🔍 核心问题

CNN 主要解决图像特征提取和图像分类问题。

- 任务类型：图像分类 / 目标检测 / 图像分割 / 图像识别
- 输入是什么：图像张量，例如 `(batch_size, channels, height, width)`
- 输出是什么：类别、目标位置、像素级分类结果等
- 适合什么样的数据：图像、二维网格数据、局部结构明显的数据
- 不适合什么样的数据：纯文本序列、长距离依赖特别强的数据

CNN 最核心的问题是：

```text
如何从图片中自动提取有用特征，而不是手工设计特征。
```

---

## 🧩 核心思想

CNN 的本质是：用小窗口在图像上滑动，提取局部特征。

一张图片里，局部区域往往包含重要信息，比如边缘、角点、纹理、形状。CNN 通过卷积核不断扫描图片，把这些局部信息提取出来。

重点理解：

1. 信息是怎么流动的？
   图像先经过卷积层提取局部特征，再经过激活函数增加非线性，再通过池化层压缩尺寸，最后进入全连接层或分类头输出结果。

2. 模型学到的是什么？
   浅层学边缘、颜色、纹理；中层学局部形状；深层学更抽象的物体结构。

3. 为什么比普通全连接网络强？
   CNN 利用了图像的空间结构，不需要每个像素都和所有神经元连接，参数更少，泛化更好。

4. 它解决了旧方法的什么问题？
   传统图像方法依赖人工设计特征，CNN 可以自动学习特征。

---

## ⚙️ 模型结构

### 结构组成

- 卷积层 `Conv2d`：提取局部特征
- 激活函数 `ReLU`：增加非线性表达能力
- 池化层 `MaxPool2d`：降低特征图尺寸，保留重要信息
- 展平层 `Flatten`：把二维特征图拉平成一维向量
- 全连接层 `Linear`：完成分类或回归

### 数据流动

```text
输入图像 -> 卷积层 -> ReLU -> 池化层 -> 卷积层 -> ReLU -> 池化层 -> 展平 -> 全连接层 -> 输出类别
```

### 张量形状

PyTorch 中图像张量通常是：

```text
输入形状: (batch_size, channels, height, width)
```

以 MNIST 为例：

```text
输入: (batch_size, 1, 28, 28)
卷积后: (batch_size, 16, 28, 28)
池化后: (batch_size, 16, 14, 14)
再次卷积: (batch_size, 32, 14, 14)
再次池化: (batch_size, 32, 7, 7)
展平: (batch_size, 32 * 7 * 7)
输出: (batch_size, 10)
```

---

## 🔥 核心机制

### 1. 卷积核

卷积核是一个小矩阵，例如 `3x3` 或 `5x5`，它会在图片上滑动，提取局部特征。

```text
卷积核负责看局部区域，判断这个区域有没有某种特征。
```

例如：

- 某些卷积核可能学到边缘
- 某些卷积核可能学到纹理
- 某些卷积核可能学到局部形状

---

### 2. 局部感受野

CNN 的神经元不是一次看完整张图，而是先看局部区域。

这符合图像特点：

```text
图像中的局部像素之间关系更紧密。
```

层数越深，神经元能看到的原图范围越大，也就是感受野越来越大。

---

### 3. 参数共享

同一个卷积核会在整张图上滑动，因此不同位置使用同一组参数。

好处：

- 参数量更少
- 可以识别不同位置出现的同一种特征
- 比全连接网络更适合图像

---

### 4. 池化

池化层用于降低特征图尺寸。

常见池化：

```text
Max Pooling: 取局部区域最大值
Average Pooling: 取局部区域平均值
```

池化的作用：

- 减少计算量
- 保留主要特征
- 增强一定的位置鲁棒性

---

## 🔢 数学表达

二维卷积可以简单理解为：

$$
\text{输出特征} = \text{局部区域} \times \text{卷积核权重} + \text{偏置}
$$

卷积输出尺寸：

$$
out = \frac{in + 2 \times padding - kernel\_size}{stride} + 1
$$

说明：

- `in`：输入宽度或高度
- `padding`：边缘填充大小
- `kernel_size`：卷积核大小
- `stride`：卷积核每次滑动的步长
- `out`：输出宽度或高度

---

## ✅ 优点

- 非常适合图像数据。
- 参数共享让参数量比全连接网络少很多。
- 能自动提取特征，不需要人工设计图像特征。
- 对局部平移有一定鲁棒性。
- 可以通过堆叠多层学习从低级到高级的特征。

---

## ⚠️ 缺点

- 对长距离依赖建模能力不如 Transformer。
- 需要较多训练数据才能学到稳定特征。
- 对旋转、尺度变化等情况不一定天然鲁棒。
- 模型越深，训练和调参越复杂。

---

## 🎯 适用场景

- 图像分类
- 手写数字识别
- 人脸识别
- 医学影像分析
- 目标检测
- 图像分割
- 视频帧特征提取

---

## 🚫 不适用场景

- 纯文本长序列建模
- 需要强长距离依赖的任务
- 样本极少且没有预训练模型可用的任务
- 图像空间结构不明显的数据

---

## 🧪 评价指标

分类任务：

```text
Accuracy / Precision / Recall / F1 / AUC
```

目标检测任务：

```text
mAP / IoU
```

图像分割任务：

```text
Pixel Accuracy / mIoU / Dice
```

CNN 常用指标：

- 图像分类：Accuracy、Top-5 Accuracy
- 类别不均衡：Precision、Recall、F1
- 检测分割：mAP、IoU、Dice

---

## 💻 PyTorch 代码模板

```python
import torch
import torch.nn as nn


class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()

        self.features = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 7 * 7, 128),
            nn.ReLU(),
            nn.Linear(128, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x


model = SimpleCNN(num_classes=10)

dummy_x = torch.randn(4, 1, 28, 28)
output = model(dummy_x)
print(output.shape)  # torch.Size([4, 10])
```

---

## 🏋️ 训练流程

1. 准备图像数据
2. 对图像做预处理，例如 resize、归一化、数据增强
3. 定义 CNN 模型
4. 定义损失函数
5. 定义优化器
6. 前向传播得到预测结果
7. 计算损失
8. 反向传播
9. 更新参数
10. 在验证集上评估模型

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
| `in_channels` | 输入通道数 | 适配更多输入通道 | 适配更少输入通道 |
| `out_channels` | 输出通道数，也就是卷积核个数 | 特征更多，参数更多 | 特征更少，参数更少 |
| `kernel_size` | 卷积核大小 | 感受野更大，参数更多 | 感受野更小，参数更少 |
| `stride` | 滑动步长 | 输出尺寸更小 | 输出尺寸更大 |
| `padding` | 边缘填充 | 更容易保持尺寸 | 输出尺寸更小 |
| `pool_size` | 池化窗口大小 | 压缩更强 | 保留更多空间信息 |

---

## 🧯 易错点

- PyTorch 图像输入格式是 `(N, C, H, W)`，不是 `(N, H, W, C)`。
- `Linear` 层输入维度容易算错，需要根据卷积和池化后的尺寸计算。
- 分类任务最后一层通常输出 logits，不需要手动加 `softmax` 再传给 `CrossEntropyLoss`。
- 忘记对图像做归一化，可能导致训练不稳定。
- 卷积核、步长、padding 改变后，特征图尺寸也会变化。
- 模型太深但数据太少，容易过拟合。

---

## 🔁 和其他模型的对比

| 模型 | 主要用途 | 核心机制 | 优点 | 缺点 |
| --- | --- | --- | --- | --- |
| CNN | 图像 | 卷积 | 擅长提取局部空间特征 | 长距离依赖较弱 |
| RNN | 序列 | hidden state | 适合时间序列 | 并行能力弱 |
| Transformer | 序列 / 多模态 | attention | 擅长长距离依赖 | 计算量较大 |
| MLP | 通用特征 | 全连接 | 结构简单 | 不利用图像空间结构 |

---

## 🧠 记忆口诀

```text
卷积看局部，池化压尺寸；
浅层看边缘，深层看语义；
图像进 CNN，特征一层层提。
```

---

## 📚 常见面试问题

1. CNN 为什么适合处理图像？
2. 卷积核的作用是什么？
3. 什么是局部感受野？
4. 什么是参数共享？
5. 池化层有什么作用？
6. `padding` 和 `stride` 会如何影响输出尺寸？
7. PyTorch 中图像张量的形状是什么？
8. 为什么 `CrossEntropyLoss` 前通常不需要加 `softmax`？
