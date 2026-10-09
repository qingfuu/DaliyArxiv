# cs.CL | Computation and Language | 2026-10-08

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/具身智能/Rephrase_Before_You_Act_Characterizing_and_Mitigating_Language_Sensitivity_in_Vision-Language-Action_Models|Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models]]

![[assets/2610.10526_figure.png|800]]

- **arXiv**: [2610.10526](https://arxiv.org/abs/2610.10526)
- **PDF**: https://arxiv.org/pdf/2610.10526
- **详细分析**: [[20_Research/Papers/具身智能/Rephrase_Before_You_Act_Characterizing_and_Mitigating_Language_Sensitivity_in_Vision-Language-Action_Models|Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models]]
- **作者**: Mikey Watts, Yuchen Cui
- **cs 子类**: cs.CL, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.25（加权：具身智能 1.5，大模型 0.45，机器人 0.3）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models》归入 具身智能、大模型、机器人 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) are strikingly sensitive to instruction phrasing and do not inherit the language robustness of the vision-language models they are built on. A one-word edit can move success by tens of points: $π_{0.5}$ turns on a LIBERO stove 100% of the time for "switch on the stove" and 2% for "switch on the hot plate", and a $π_0$ checkpoint finetuned with rephrase augmentation still shows swings of up to 61 points. We characterize this sensitivity with statistically tested single-edit swings and an oracle phrase search, which shows that phrasing alone nearly closes the 21-point gap between in-distribution and out-of-distribution tasks. We then reduce it without modifying the policy. Because the sensitivity is systematic, it can be expressed as explicit rules: we score many phrasings of a few training tasks, have a large language model distill the evidence into ten to twenty rephrasing rules, and at deployment rewrite each incoming instruction once under these rules. The rules improve the frozen $π_0$ by 16 to 27% relative on twelve held-out tasks across adversarial, VLM-generated, and human-generated phrasings, with gains concentrated on out-of-distribution tasks. The pipeline replicates on $π_{0.5}$ and LIBERO, lifting in-finetune success from 93.6% to 97.8%. The method requires no retraining and no per-step verification, and applies zero-shot to unseen tasks and instructions. Project website: https://sttawm.github.io/rephrase-before-you-act

</details>

---

### [[20_Research/Papers/具身智能/SpikingVLA_Asynchronous_Spiking_Vision-Language-Action_Models|SpikingVLA: Asynchronous Spiking Vision-Language-Action Models]]

![[assets/2610.09710_figure.png|800]]

- **arXiv**: [2610.09710](https://arxiv.org/abs/2610.09710)
- **PDF**: https://arxiv.org/pdf/2610.09710
- **详细分析**: [[20_Research/Papers/具身智能/SpikingVLA_Asynchronous_Spiking_Vision-Language-Action_Models|SpikingVLA: Asynchronous Spiking Vision-Language-Action Models]]
- **作者**: Jingya Wang, Dehao Zhang, Shuai Wang, Malu Zhang, Yang Yang, Haizhou Li
- **cs 子类**: cs.CL
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《SpikingVLA: Asynchronous Spiking Vision-Language-Action Models》归入 具身智能 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EfficientVLA, OpenVLA, QVLA, QuantVLA, SmolVLA, SpikeVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

ANN-to-SNN conversion offers a practical route toward energy-efficient spiking Vision-Language-Action (VLA) models by bypassing the substantial cost of training large-scale SNNs from scratch. However, existing methods often require many timesteps to maintain competitive performance, resulting in substantial inference latency for real-time VLA deployment. To address this challenge, we introduce SpikingVLA, an ANN-to-SNN conversion framework that enables accurate and low-latency spiking VLA inference. Specifically, we propose a Dendritic Integrate-and-Fire (DIF) neuron that alleviates channel-wise activation outliers through dendritic mixing and adaptive somatic firing, enabling accurate ANN-to-SNN conversion with fewer timesteps. Building on DIF neurons, we further introduce an asynchronous execution mechanism that overlaps temporal computation across VLA components, reducing synchronization overhead and latency. Extensive experiments demonstrate that SpikingVLA achieves competitive navigation performance with substantially improved inference efficiency. Compared with existing spiking VLA methods, SpikingVLA improves SR and SPL by 11.9\% and 12.6\%, respectively, while reducing first-action latency by 11.2$\times$. These results establish SpikingVLA as a practical framework for deploying pretrained VLA models with high-performance and low-latency spiking inference.

</details>

---

### [[20_Research/Papers/具身智能/CARE_Certifying_Acceleration_for_Vision-Language-Action_Inference|CARE: Certifying Acceleration for Vision-Language-Action Inference]]

![[assets/2610.08917_figure.png|800]]

- **arXiv**: [2610.08917](https://arxiv.org/abs/2610.08917)
- **PDF**: https://arxiv.org/pdf/2610.08917
- **详细分析**: [[20_Research/Papers/具身智能/CARE_Certifying_Acceleration_for_Vision-Language-Action_Inference|CARE: Certifying Acceleration for Vision-Language-Action Inference]]
- **作者**: Rui Liu, Tong Zheng, Jindong Gu, Zhipeng Wang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.75（加权：具身智能 1.5，大模型 0.25）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《CARE: Certifying Acceleration for Vision-Language-Action Inference》归入 具身智能、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While vision-language-action (VLA) models have advanced rapidly, running them at every control step remains expensive. Prior work accelerates VLA inference using techniques like action chunking and visual-token pruning, typically evaluating based on latency and average task success. However, acceleration may discard information and break tasks the original policy would solve, a risk hidden by average metrics. Measuring these failures is challenging because action deviations compound over closed-loop trajectories, meaning task failure is only observable across full episodes. We therefore define an acceleration-induced failure via paired rollouts from identical initial conditions, tracking when the reference succeeds but the accelerated policy fails. To manage this, we introduce CARE, an approach for certified accelerator selection. CARE uses paired rollouts on a calibration set to provide finite-sample guarantees that acceleration-induced failure risk stays below a user-specified budget. It deploys the fastest certified candidate, falling back to the reference if none qualify. By relying only on terminal outcomes and measured compute, CARE applies unchanged across diverse acceleration mechanisms, while sequential testing and failure-triggered reference rollouts keep certification affordable. On four LIBERO suites with OpenVLA-OFT, CARE certifies $9.0$--$10.8\times$ speedups while guaranteeing (at $95\%$ confidence) that at least $85.8\%$ of reference-solved episodes are preserved. Under tight budgets, selectors without guarantees exceed the budget in up to $75\%$ of trials, whereas CARE stays within budget and its sequential form uses $78.9\%$ fewer rollouts than exhaustive evaluation. CARE further generalizes to flow-step reduction for $π_{0.5}$, and to Qwen3.5-9B and Llama-3.1-8B agents in Crafter.

</details>

---
