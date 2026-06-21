# cs.HC | Human-Computer Interaction | 2026-06-19

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/MobileForge_Annotation-Free_Adaptation_for_Mobile_GUI_Agents_with_Hierarchical_Feedback-Guided_Policy_Optimization|MobileForge: Annotation-Free Adaptation for Mobile GUI Agents with Hierarchical Feedback-Guided Policy Optimization]]

![[assets/2606.19930_figure.png|800]]

- **arXiv**: [2606.19930](https://arxiv.org/abs/2606.19930)
- **PDF**: https://arxiv.org/pdf/2606.19930
- **详细分析**: [[20_Research/Papers/强化学习/MobileForge_Annotation-Free_Adaptation_for_Mobile_GUI_Agents_with_Hierarchical_Feedback-Guided_Policy_Optimization|MobileForge: Annotation-Free Adaptation for Mobile GUI Agents with Hierarchical Feedback-Guided Policy Optimization]]
- **作者**: Guangyi Liu, Pengxiang Zhao, Gao Wu, Yiwen Yin, Mading Li, Liang Liu, Congxiao Liu, Zhang Qi, Mengyan Wang, Liang Guo, Yong Liu
- **cs 子类**: cs.HC
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.6，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《MobileForge: Annotation-Free Adaptation for Mobile GUI Agents with Hierarchical Feedback-Guided Policy Optimization》归入 强化学习、大模型 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ACuRL, AndroidWorld, MobileGUI-RL, MobileGym, MobileWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

MLLM-based mobile GUI agents have made substantial progress in UI understanding and action execution, but adapting them to real target apps remains costly because mobile apps are numerous, frequently updated, and hard to cover with human-written tasks, demonstrations, or reward labels. Existing annotation-free GUI learning reduces manual supervision, yet lacks a unified substrate connecting target-app exploration, curriculum mining, rollout execution, and feedback, while policy optimization often relies on isolated rollouts and coarse rewards that are hard to convert into reliable improvement signals. We present MobileForge, an annotation-free adaptation system for mobile GUI agents. MobileForge consists of MobileGym, which grounds task generation and rollout evaluation in real mobile app interaction, and Hierarchical Feedback-Guided Policy Optimization (HiFPO), which turns trajectory outcomes, step-level process feedback, and corrective hints into hint-contextualized step-level GRPO updates. Using only automatically generated annotation-free adaptation data, MobileForge adapts Qwen3-VL-8B to 67.2% Pass@3 on AndroidWorld, close to the closed-data GUI-specialized GUI-Owl-1.5-8B base model at 69.0%. The MobileForge-adapted ForgeOwl-8B further reaches 77.6% Pass@3 on AndroidWorld and 41.0% success on the out-of-domain MobileWorld GUI-only split, establishing the strongest open-data mobile GUI agent in our evaluation. Code, data, and trained models will be released at https://mobile-forge.github.io/.

</details>

---
