# cs.CY | Computers and Society | 2026-10-19

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/A_Large_Language_Model_LLM_Approach_to_COVID-19_Fake_News_Detection|A Large Language Model LLM Approach to COVID-19 Fake News Detection]]

![[assets/2610.23800_figure.png|800]]

- **arXiv**: [2610.23800](https://arxiv.org/abs/2610.23800)
- **PDF**: https://arxiv.org/pdf/2610.23800
- **详细分析**: [[20_Research/Papers/大模型/A_Large_Language_Model_LLM_Approach_to_COVID-19_Fake_News_Detection|A Large Language Model LLM Approach to COVID-19 Fake News Detection]]
- **作者**: Muhammad Arif, Samah Fodeh-Jarad, Elyas Irankhah, Uroosa Fatima, Lama Ayash, Sreeraj Ramachandran
- **cs 子类**: cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《A Large Language Model LLM Approach to COVID-19 Fake News Detection》归入 大模型 方向。该论文围绕 Computers and Society 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：XLNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Text classification is a widely studied problem in information retrieval and data mining, with applications ranging from healthcare diagnosis to the detection of COVID-19-related fake news. Social media platforms generate vast volumes of user-generated text, and the rapid spread of misinformation during the pandemic has made automated fake news detection an important task. In this study, we apply pretrained transformer-based transfer learning (TL) models and large language models (LLMs), namely BERT-base, ALBERT-base, XLM-RoBERTa-base, DistilBERT, GPT-2, XLNet, and T5, to the COVID-19 English Tweets dataset, which contains 6,420 tweets labeled as real or fake. To further improve performance, we apply six late-fusion optimization techniques: weighted fusion, particle swarm optimization (PSO) fusion, the Nelder-Mead algorithm, Powell's method, the Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm, and trust-region constrained optimization. Models are evaluated using accuracy, precision, recall, and F1-score, and confusion-matrix heatmaps are used to visualize the predictions of each model. GPT-2 achieved the best performance, with an accuracy of 0.9631, precision of 0.9612, recall of 0.9610, and F1-score of 0.9600, while Nelder-Mead fusion achieved the best result among the fusion methods with an accuracy of 0.9610. These results highlight the value of LLMs for COVID-19 fake news detection. We conclude by outlining future directions, including multiclass classification, multilingual datasets, and real-time social media streams.

</details>

---
