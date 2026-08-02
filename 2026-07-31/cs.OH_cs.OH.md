# cs.OH | cs.OH | 2026-07-31

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Self-Evolving_Learning_for_Embodied_AI_with_Criticality_Model|Self-Evolving Learning for Embodied AI with Criticality Model]]

![[assets/2607.28251_figure.png|800]]

- **arXiv**: [2607.28251](https://arxiv.org/abs/2607.28251)
- **PDF**: https://arxiv.org/pdf/2607.28251
- **详细分析**: [[20_Research/Papers/具身智能/Self-Evolving_Learning_for_Embodied_AI_with_Criticality_Model|Self-Evolving Learning for Embodied AI with Criticality Model]]
- **作者**: Linxuan He, Yuying Tian, Lingxiang Fan, Jiaqi Pi, Yinqiao Lu, Shang Su, Mengkai Shi, Shuo Feng
- **cs 子类**: 
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 3，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Self-Evolving Learning for Embodied AI with Criticality Model》归入 具身智能、机器人 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HIL-SERL, Real-World, SERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite rapid advances in policy pretraining, embodied AI systems routinely plateau during task-specific finetuning. The root cause lies in how finetuning data are collected: the default pipeline gathers data randomly, treating every sample as informative. Datasets become dominated by nominal scenarios, while rare failure cases--the most valuable for improvement--are missed. We propose a self-evolving method that breaks this plateau. Our core insight is that a state-wise criticality model, learned from the policy's own execution outcomes to predict the probability of future failure, can guide importance sampling toward failure-prone scenarios. After replacing redundant nominal scenarios with diverse failure-prone ones, importance weights are used to resample the data during training. This effectively preserves an unbiased learning objective while fundamentally increasing the information density of the training pool. Across quadrupedal locomotion, multi-task manipulation, vision-language-action benchmarks, and a real-robot task, our method reduces failure rates by 51--67% relative to trained baselines and by 8-25% relative to state-of-the-art vision-language-action models.

</details>

---
