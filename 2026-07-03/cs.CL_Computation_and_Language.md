# cs.CL | Computation and Language | 2026-07-03

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/具身智能/Visually_Grounded_Self-Reflection_for_Vision-Language_Models_via_Reinforcement_Learning|Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning]]

![[assets/2607.02490_figure.png|800]]

- **arXiv**: [2607.02490](https://arxiv.org/abs/2607.02490)
- **PDF**: https://arxiv.org/pdf/2607.02490
- **详细分析**: [[20_Research/Papers/具身智能/Visually_Grounded_Self-Reflection_for_Vision-Language_Models_via_Reinforcement_Learning|Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning]]
- **作者**: Liyan Tang, Fangcong Yin, Greg Durrett
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VRRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large vision-language models can reason over multimodal inputs by generating textual chains of thought (CoT). A key capability exhibited in CoT reasoning is self-reflection: revisiting earlier decisions and correcting previous errors. However, existing LVLMs often fail to properly attend to visual inputs during reflection, limiting their ability to translate feedback into grounded corrections, especially for out-of-distribution images. To address this issue, we propose a novel reinforcement learning training framework VRRL, with two components explicitly designed to elicit visually grounded self-reflection. First, we randomly mask trajectory prefixes during training to emphasize recovery from incorrect intermediate predictions rather than making early mistakes. Second, we introduce buffered roll-ins from an experience replay buffer to expose the model to diverse failure states that it must learn to correct. We evaluate our approach on visual grounding tasks involving tables and charts, as well as spatial navigation benchmarks. While off-the-shelf and conventionally fine-tuned models degrade substantially under distribution shift, our method substantially improves average out-of-distribution accuracy over standard RL and reflection-oriented fine-tuning baselines by using self-reflection effectively.

</details>

---

### [[20_Research/Papers/大模型/CheckRLM_Effective_Knowledge-Thought_Coherence_Checking_in_Retrieval-Augmented_Reasoning|CheckRLM: Effective Knowledge-Thought Coherence Checking in Retrieval-Augmented Reasoning]]

![[assets/2607.02262_figure.png|800]]

- **arXiv**: [2607.02262](https://arxiv.org/abs/2607.02262)
- **PDF**: https://arxiv.org/pdf/2607.02262
- **详细分析**: [[20_Research/Papers/大模型/CheckRLM_Effective_Knowledge-Thought_Coherence_Checking_in_Retrieval-Augmented_Reasoning|CheckRLM: Effective Knowledge-Thought Coherence Checking in Retrieval-Augmented Reasoning]]
- **作者**: Dingling Xu, Ruobing Wang, Qingfei Zhao, Yukun Yan, Zhichun Wang, Daren Zha, Shi Yu, Zhenghao Liu, Shuo Wang, Xu Han, Maosong Sun
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《CheckRLM: Effective Knowledge-Thought Coherence Checking in Retrieval-Augmented Reasoning》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning Language Models (RLMs) have significantly improved performance on complex tasks by extending the reasoning chain. However, these chains are prone to containing factual errors, particularly in knowledge-intensive tasks. To address this issue, we propose CheckRLM, a framework that improves the reliability of the reasoning process through Retrieval-Augmented Generation (RAG) by timely checking and correcting factual errors. Specifically, CheckRLM extracts factual claims from the reasoning chain to identify and localize subtle knowledge inconsistencies during inference. Upon detection of errors, a refinement mechanism performs minimal-cost yet precise corrections by leveraging external knowledge, ensuring coherence between the reasoning chain and correct knowledge. Extensive experiments demonstrate that CheckRLM substantially outperforms existing baselines, exhibiting a strong capability to mitigate error accumulation in long-horizon reasoning with lower costs. The code and data are available at https://github.com/AI9Stars/CheckRLM.

</details>

---

### [[20_Research/Papers/大模型/Unlocking_Speech-Text_Compositional_Powers_Instruction-Following_Speech_Language_Models_without_Instruction_Tuning|Unlocking Speech-Text Compositional Powers: Instruction-Following Speech Language Models without Instruction Tuning]]

![[assets/2607.02214_figure.png|800]]

- **arXiv**: [2607.02214](https://arxiv.org/abs/2607.02214)
- **PDF**: https://arxiv.org/pdf/2607.02214
- **详细分析**: [[20_Research/Papers/大模型/Unlocking_Speech-Text_Compositional_Powers_Instruction-Following_Speech_Language_Models_without_Instruction_Tuning|Unlocking Speech-Text Compositional Powers: Instruction-Following Speech Language Models without Instruction Tuning]]
- **作者**: Congrui Du, Yang Zhang, Kaizhi Qian, Shiyu Chang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Unlocking Speech-Text Compositional Powers: Instruction-Following Speech Language Models without Instruction Tuning》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Instruction tuning for speech language models (SLMs) is substantially more challenging than for text-based large language models (LLMs), as it requires learning a new modality and a wide range of speech-specific instructions in addition to those supported by text LLMs. Existing SLM training approaches largely replicate the text LLM training paradigm by synthesizing large-scale speech pre-training and instruction-tuning datasets. However, this strategy is difficult to scale, since speech sequences are significantly longer than text sequences. In this paper, we propose SpeechCombine, an instruction-following speech language model trained without any instruction tuning, using only a single round of speech pre-training on 30k hours of data. Starting from a text LLM base model, we perform continuous pre-training on speech utterances to obtain a speech-adapted model, and then directly combine its weights with the weight difference between the instruction-tuned and base versions of the text LLM. Our results show that this simple combination strategy not only preserves the knowledge and capabilities of the original text LLM, but also effectively transfers them to the speech domain. These findings suggest a new direction for SLM training that avoids reliance on massive speech data.

</details>

---

### [[20_Research/Papers/大模型/Bayesian_Sparse_Low-Rank_Adaptation_for_Large_Language_Model_Uncertainty_Estimation|Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation]]

![[assets/2607.02182_figure.png|800]]

- **arXiv**: [2607.02182](https://arxiv.org/abs/2607.02182)
- **PDF**: https://arxiv.org/pdf/2607.02182
- **详细分析**: [[20_Research/Papers/大模型/Bayesian_Sparse_Low-Rank_Adaptation_for_Large_Language_Model_Uncertainty_Estimation|Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation]]
- **作者**: Jijie Zhang, Zhe Ren, Quan Zhang, Dandan Guo
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) exhibit remarkable reasoning capabilities, but their task-specific fine-tuning is notoriously plagued by overconfidence, severely hindering trustworthy deployment. We propose Data-Adaptive Lower-Rank Adaptation (DALorRA), a simple and effective variational Bayesian sparse framework that shifts the paradigm of uncertainty quantification from the dense parameter space to the lightweight rank level of low-rank adaptation (LoRA). With the insight that LoRA essentially aggregates multiple rank-one components that may provide superfluous model capacity, DALorRA imposes stochastic masking on rank dimensions, enabling Bayesian regularization of model capacity during training and ensemble-like calibration during inference. Extensive experiments demonstrate DALorRA's excellent calibration of LLMs without compromising reasoning accuracy.

</details>

---

### [[20_Research/Papers/强化学习/Denser_$_neq$_Better_Limits_of_On-Policy_Self-Distillation_for_Continual_Post-Training|Denser $\neq$ Better: Limits of On-Policy Self-Distillation for Continual Post-Training]]

![[assets/2607.01763_first_page.png|800]]

- **arXiv**: [2607.01763](https://arxiv.org/abs/2607.01763)
- **PDF**: https://arxiv.org/pdf/2607.01763
- **详细分析**: [[20_Research/Papers/强化学习/Denser_$_neq$_Better_Limits_of_On-Policy_Self-Distillation_for_Continual_Post-Training|Denser $\neq$ Better: Limits of On-Policy Self-Distillation for Continual Post-Training]]
- **作者**: Meng Wang, Haohan Zhao, Wenzhuo Liu, Lu Yang, Geng Liu, Haiyang Guo, Guo-Sen Xie, Gaofeng Meng, Hongbin Liu, Fei Zhu
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Denser $\neq$ Better: Limits of On-Policy Self-Distillation for Continual Post-Training》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continual post-training enables foundation models to acquire new knowledge while preserving existing capabilities. Recent work suggests that on-policy learning can mitigate forgetting, with on-policy self-distillation emerging as a particularly attractive approach. In this work, we revisit this optimistic view through self-distillation policy optimization (SDPO). Our experiments show that SDPO can accelerate in-domain specialization when teacher signals are stable and well aligned, but it struggles to generalize to out-of-distribution scenarios. In continual post-training, SDPO exhibits stronger forgetting and can even collapse, whereas on-policy reinforcement learning methods such as GRPO adapt more conservatively and better preserve prior capabilities. Further analyses reveal that denser self-distillation induces larger drift in both parameter space and response space, and can amplify high-frequency formatting artifacts through a self-reinforcing teacher--student loop. These findings suggest that on-policy data alone is insufficient for continual learning. Dense self-distillation can accelerate specialization when teacher targets are stable and token-level supervision is reliable, but it should not be treated as a default stabilizer for continual post-training. Our code is available at https://github.com/Moenupa/SDPO-CL.

</details>

---

### [[20_Research/Papers/大模型/BOUNDARY_SYNC_Measuring_Communication-Induced_Representational_Coupling_in_Multi-Agent_LLM_Systems|BOUNDARY_SYNC: Measuring Communication-Induced Representational Coupling in Multi-Agent LLM Systems]]

![[assets/2607.01600_figure.png|800]]

- **arXiv**: [2607.01600](https://arxiv.org/abs/2607.01600)
- **PDF**: https://arxiv.org/pdf/2607.01600
- **详细分析**: [[20_Research/Papers/大模型/BOUNDARY_SYNC_Measuring_Communication-Induced_Representational_Coupling_in_Multi-Agent_LLM_Systems|BOUNDARY_SYNC: Measuring Communication-Induced Representational Coupling in Multi-Agent LLM Systems]]
- **作者**: Zewen Liu
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《BOUNDARY_SYNC: Measuring Communication-Induced Representational Coupling in Multi-Agent LLM Systems》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language models (LLMs) are deployed as communicating agents, does inter-agent communication cause outputs to converge? We introduce BOUNDARY_SYNC, a protocol measuring representational coupling via the Coupling Amplification Factor (CAF = JSD_cond / JSD_baseline), where CAF &lt; 1 indicates homogenization and CAF &gt; 1 indicates diversification. In controlled GPT-4o experiments (N=30, ~9,900 API calls), we measure coupling in text and image communication. Key findings: (1) text communication causes significant homogenization (CAF=0.803 [0.740, 0.873], d=1.30, p&lt;0.001), confirmed by no-communication ablation and prompt-perturbation controls; (2) image communication also homogenizes under within-modality baselines (CAF=0.834 [0.811, 0.858]), with comparable proportional effect; (3) group size moderates coupling direction -- K=5 produces homogenization while K=3 yields CAF &gt; 1.0 (point estimates 1.14 and 1.06, CI pending), suggesting a directional shift toward diversification; (4) cross-model replication shows extreme variation (CAF 0.034-0.803), with DeepSeek dominated by format artifacts; (5) coupling is stateless -- driven by prompt context rather than cumulative updating, with continuous consensus producing monotonic convergence. These results establish LLM agent coupling as real, measurable, and controllable at the prompt level, with direct implications for multi-agent system design.

</details>

---
