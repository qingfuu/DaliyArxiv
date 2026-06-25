# cs.CR | Cryptography and Security | 2026-06-23

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/A_Watermark_for_Vision-Language-Action_and_World_Action_Models|A Watermark for Vision-Language-Action and World Action Models]]

![[assets/2606.23574_figure.png|800]]

- **arXiv**: [2606.23574](https://arxiv.org/abs/2606.23574)
- **PDF**: https://arxiv.org/pdf/2606.23574
- **详细分析**: [[20_Research/Papers/具身智能/A_Watermark_for_Vision-Language-Action_and_World_Action_Models|A Watermark for Vision-Language-Action and World Action Models]]
- **作者**: Yule Liu, Shuai Liu, Jiaheng Wei, Xinlei He
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《A Watermark for Vision-Language-Action and World Action Models》归入 具身智能、机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models and world-action models (WAM) are the generative models now driving general-purpose robot control, turning raw camera input directly into motor commands. They are increasingly deployed as black-box services, where a partner runs the policy through an interface while the owner keeps the weights private. Training such a model takes proprietary data and heavy computational power, making the deployed model itself a valuable intellectual property. To address this, we propose the \emph{keyed latent-provenance verification} method, which fingerprints the policy through the seed of the Gaussian noise vector that the models draw before generation. At the injection stage, the owner swaps this seed for a keyed one with the same distribution as ordinary noise, so the fingerprinted actions are statistically identical to those of an ordinary run and an adversary watching the output finds no signal to detect or remove. At the verification stage, the owner runs the suspect model under authorized access and records the action channels the robot executes, a partial and possibly post-processed view of the policy's output. From this view, the verifier recovers the seed by gradient-based maximum a posteriori (MAP) optimization, tests it for the secret key to score each rollout, and aggregates these scores into a single decision on whether the suspect model belongs to the owner. We evaluate the method on two representative models across two robot suites. The experiments cover detection of the fingerprint, identification of which of several keys a suspect carries, robustness to a range of attacks, and an analysis of why the design works. Across both models, the fingerprint can be detected reliably with little change to task performance, and it remains detectable under output-side removal attacks and weight-level edits.

</details>

---
