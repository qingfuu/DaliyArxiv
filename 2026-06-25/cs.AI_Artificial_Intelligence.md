# cs.AI | Artificial Intelligence | 2026-06-25

#arxiv #ComputerScience

**论文数**: 27

### [[20_Research/Papers/具身智能/Learning_Action_Priors_for_Cross-embodiment_Robot_Manipulation|Learning Action Priors for Cross-embodiment Robot Manipulation]]

![[assets/2606.26095_figure.png|800]]

- **arXiv**: [2606.26095](https://arxiv.org/abs/2606.26095)
- **PDF**: https://arxiv.org/pdf/2606.26095
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Action_Priors_for_Cross-embodiment_Robot_Manipulation|Learning Action Priors for Cross-embodiment Robot Manipulation]]
- **作者**: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.8，大模型 0.3，机器人 0.9）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Learning Action Priors for Cross-embodiment Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AdaWorld, OpenVLA, UniVLA, VA-to-VLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.

</details>

---

### [[20_Research/Papers/大模型/Neglected_Free_Lunch_from_Post-training_Progress_Advantage_for_LLM_Agents|Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents]]

![[assets/2606.26080_figure.png|800]]

- **arXiv**: [2606.26080](https://arxiv.org/abs/2606.26080)
- **PDF**: https://arxiv.org/pdf/2606.26080
- **详细分析**: [[20_Research/Papers/大模型/Neglected_Free_Lunch_from_Post-training_Progress_Advantage_for_LLM_Agents|Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents]]
- **作者**: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.6，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.

</details>

---

### [[20_Research/Papers/世界模型/The_Unfireable_Safety_Kernel_Execution-Time_AI_Alignment_for_AI_Agents_and_Other_Escapable_AI_Systems|The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems]]

![[assets/2606.26057_figure.png|800]]

- **arXiv**: [2606.26057](https://arxiv.org/abs/2606.26057)
- **PDF**: https://arxiv.org/pdf/2606.26057
- **详细分析**: [[20_Research/Papers/世界模型/The_Unfireable_Safety_Kernel_Execution-Time_AI_Alignment_for_AI_Agents_and_Other_Escapable_AI_Systems|The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems]]
- **作者**: Seth Dobrin, Łukasz Chmiel
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型, 强化学习
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.16，世界模型 0.36）
- **关联关键词**: Agent, WorldModel, Security

#### 研究背景与动机

《The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems》归入 大模型、世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.

</details>

---

### [[20_Research/Papers/其他/Can_Trustless_Agents_Be_Trusted_An_Empirical_Study_of_the_ERC-8004_Decentralized_AI_Agent_Ecosystem|Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem]]

![[assets/2606.26028_figure.png|800]]

- **arXiv**: [2606.26028](https://arxiv.org/abs/2606.26028)
- **PDF**: https://arxiv.org/pdf/2606.26028
- **详细分析**: [[20_Research/Papers/其他/Can_Trustless_Agents_Be_Trusted_An_Empirical_Study_of_the_ERC-8004_Decentralized_AI_Agent_Ecosystem|Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem]]
- **作者**: Xihan Xiong, Zelin Li, Wei Wei, Qin Wang, William Knottenbelt, Zhipeng Wang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent

#### 研究背景与动机

《Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As autonomous AI agents increasingly transact across organizational boundaries, a fundamental trust challenge emerges: how can an agent assess whether an unknown counterpart is trustworthy? The ERC-8004 protocol addresses this challenge with the first permissionless trust layer for AI agent economies, built around three on-chain registries for Identity, Reputation, and Validation. Despite its rapid adoption, the protocol has not been studied empirically, leaving it unclear whether the information it records provides a trustworthy basis for decision-making. To address this gap, we present the first empirical study of ERC-8004 across three chains: Ethereum, BNB Smart Chain (BSC), and Base, covering the period from protocol deployment through May 13, 2026. We crawl on-chain Identity and Reputation events, off-chain files, and x402 payment transactions. On the identity side, we find that most registrations are placeholders rather than active agents, with only a small fraction (3%, 4%, and 15% across Ethereum, BSC, and Base) exposing a valid ERC-8004 registration file with at least one live service endpoint. On the reputation side, we show that the Registry, as currently deployed, cannot function as a trust signal: values are not commensurable, feedback records are rarely grounded in verifiable interactions, and reputation can be manipulated at minimal cost. Consistent with these design weaknesses, we find that a substantial fraction of reviewers (73.6%, 59.2%, and 90.6% across Ethereum, BSC, and Base) exhibit coordinated Sybil behavior. After removing Sybil-flagged feedback, 15.5%, 72.3%, and 89.4% of rated agents, respectively, are left with no valid feedback. We then turn these findings into concrete recommendations for future revisions of ERC-8004. Our study yields actionable protocol-design implications and establishes an empirical baseline for research on AI agent markets.

</details>

---

### [[20_Research/Papers/具身智能/FORCE_Efficient_VLA_Reinforcement_Fine-Tuning_via_Value-Calibrated_Warm-up_and_Self-Distillation|FORCE: Efficient VLA Reinforcement Fine-Tuning via Value-Calibrated Warm-up and Self-Distillation]]

![[assets/2606.26006_figure.png|800]]

- **arXiv**: [2606.26006](https://arxiv.org/abs/2606.26006)
- **PDF**: https://arxiv.org/pdf/2606.26006
- **详细分析**: [[20_Research/Papers/具身智能/FORCE_Efficient_VLA_Reinforcement_Fine-Tuning_via_Value-Calibrated_Warm-up_and_Self-Distillation|FORCE: Efficient VLA Reinforcement Fine-Tuning via Value-Calibrated Warm-up and Self-Distillation]]
- **作者**: Shuyi Zhang, Yunfan Lou, Hongyang Cheng, Yichen Guo, Chuyao Fu, Yaoxu Lyu, Xiaojie Zhang, Haoran Li, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《FORCE: Efficient VLA Reinforcement Fine-Tuning via Value-Calibrated Warm-up and Self-Distillation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, PA-RL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are often constrained by the imitation ceiling imposed by sub-optimal data. While Reinforcement Learning (RL) fine-tuning can surpass this limit, it is notoriously sample inefficient. This challenge arises from two core issues: (1) catastrophic initial unlearning due to an unstable Q-function and (2) inefficient policy updates caused by low-quality exploration data, often forcing a reliance on costly human interventions. We introduce FORCE, a 3-stage framework that stabilizes fine-tuning by tackling both issues. FORCE first incorporates a Value-Calibrated Warm-Up phase, utilizing on-policy rollouts to mitigate the distributional shift of the Q-function. Subsequently, during the online stage, this calibrated Q-function acts as a filter for both the policy's own action proposals and expert data, ensuring only high-value actions are used for the policy update. We evaluate FORCE on various simulation and real-world tasks, and the result shows that FORCE achieves a 79% absolute improvement in success rates and outperform prior RL methods by 10%, while accelerating training by 32.5%. Critically, it mitigates the common success rate drop and achieves this robust performance without human intervention, marking a significant step towards deploying capable and autonomous robotic agents.

</details>

---

### [[20_Research/Papers/强化学习/Hierarchical_Reinforcement_Learning_for_Neural_Network_Compression_(HiReLC)_Pruning_and_Quantization|Hierarchical Reinforcement Learning for Neural Network Compression (HiReLC): Pruning and Quantization]]

![[assets/2606.26002_figure.png|800]]

- **arXiv**: [2606.26002](https://arxiv.org/abs/2606.26002)
- **PDF**: https://arxiv.org/pdf/2606.26002
- **详细分析**: [[20_Research/Papers/强化学习/Hierarchical_Reinforcement_Learning_for_Neural_Network_Compression_(HiReLC)_Pruning_and_Quantization|Hierarchical Reinforcement Learning for Neural Network Compression (HiReLC): Pruning and Quantization]]
- **作者**: Kamar Hibatallah Baghdadi, Kawther Guoual Belhamidi, Sara Belhadj, Aissa Boulmerka, Nadir Farhi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Hierarchical Reinforcement Learning for Neural Network Compression (HiReLC): Pruning and Quantization》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL, MobileNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present HiReLC, a hierarchical ensemble-reinforcement learning framework for automated joint quantization and structured pruning of deep neural networks. The framework decomposes the compression search across two levels of abstraction: low-level agents (LLAs) operate independently per block, selecting per-kernel configurations over a multi-discrete action space spanning bitwidth, pruning keep-ratio, quantization type, and granularity, while high-level agents (HLAs) coordinate global budget allocation via ensemble voting guided by Fisher Information-based sensitivity estimates. To mitigate the computational cost of policy evaluation, an iterative active learning loop interleaves surrogate-guided RL optimization with post-compression fine-tuning, using a lightweight MLP surrogate to amortize expensive evaluations and a logit-MSE proxy during cold-start. The surrogate is used for reward shaping rather than as a replacement for final post-compression evaluation. The controller is architecture-agnostic by design, with a modular layer abstraction decoupling the RL environment from the underlying network topology. Experiments across Vision Transformer and CNN benchmarks demonstrate effective parameter-storage compression ratios of 5.99 - 6.72$\times$ with a 3.83 % gain in one setting and 0.55 - 5.62 % accuracy drops elsewhere, supporting hierarchical policy decomposition and sensitivity-aware guidance as practical design choices for joint neural network compression.

</details>

---

### [[20_Research/Papers/强化学习/Multi-Agent_Goal_Recognition_with_Team-_and_Goal-Conditioned_Reinforcement_Learning_and_Factorized_Branch-and-Bound|Multi-Agent Goal Recognition with Team- and Goal-Conditioned Reinforcement Learning and Factorized Branch-and-Bound]]

![[assets/2606.25978_figure.png|800]]

- **arXiv**: [2606.25978](https://arxiv.org/abs/2606.25978)
- **PDF**: https://arxiv.org/pdf/2606.25978
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Agent_Goal_Recognition_with_Team-_and_Goal-Conditioned_Reinforcement_Learning_and_Factorized_Branch-and-Bound|Multi-Agent Goal Recognition with Team- and Goal-Conditioned Reinforcement Learning and Factorized Branch-and-Bound]]
- **作者**: Thiago Thomas, Gabriel de Oliveira Ramos, Felipe Meneguzzi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 机器人, 世界模型
- **相关性评分**: 1.82（加权：大模型 0.5，强化学习 0.76，世界模型 0.16，机器人 0.4）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Multi-Agent Goal Recognition with Team- and Goal-Conditioned Reinforcement Learning and Factorized Branch-and-Bound》归入 强化学习、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GRNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent goal recognition asks an observer to jointly infer which agents act together and what each team is trying to achieve, so the hypothesis space grows combinatorially with the number of team partitions and goals per team. Real applications such as drone surveillance and collaborative robotics expose only the agents' trajectory, which forces the observer to rank team-goal hypotheses from behavior alone. Multi-Agent Goal Recognition with Branch-and-Bound (MAGR-BB) addresses this setting with a shared team- and goal-conditioned policy used as the scoring model inside a factorized branch-and-bound search. On a controlled multi-agent Blocksworld benchmark, MAGR-BB returns the same top-ranked hypothesis as exhaustive search throughout the trajectory while cutting hypothesis materialization by orders of magnitude and reducing cumulative recognition runtime substantially.

</details>

---

### [[20_Research/Papers/大模型/Explainable_Control_Framework_(XCF)_based_on_Fuzzy_Model-Agnostic_Explanation_and_LLM_Agent-Supported_Interface|Explainable Control Framework (XCF) based on Fuzzy Model-Agnostic Explanation and LLM Agent-Supported Interface]]

![[assets/2606.25941_figure.jpg|800]]

- **arXiv**: [2606.25941](https://arxiv.org/abs/2606.25941)
- **PDF**: https://arxiv.org/pdf/2606.25941
- **详细分析**: [[20_Research/Papers/大模型/Explainable_Control_Framework_(XCF)_based_on_Fuzzy_Model-Agnostic_Explanation_and_LLM_Agent-Supported_Interface|Explainable Control Framework (XCF) based on Fuzzy Model-Agnostic Explanation and LLM Agent-Supported Interface]]
- **作者**: Faliang Yin, Hak-Keung Lam, David Watson
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Explainable Control Framework (XCF) based on Fuzzy Model-Agnostic Explanation and LLM Agent-Supported Interface》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Increasing demand for precise and reliable control in complex scenarios has led to the development of increasingly sophisticated controllers, including data-driven approaches employing closed box models and mathematically rigorous yet complex designs. This complexity highlights the needs for explainable control that can provide human-understandable insights into controller behavior. In this paper, an explainable control framework (XCF) along with supporting algorithms and user interface are proposed to explain how controllers determine their control actions and their underlying working mechanism. The novel contributions of this work are threefold: First, the XCF is designed to provide model-agnostic explanations for controllers in closed-loop systems and can optionally refine local explanations by system response dynamics. Second, a novel explanation method, hierarchical fuzzy model-agnostic explanation for control systems (HFMAE-C), is proposed based on the designed framework. The HFMAE-C employs a fuzzy logic system to approximate the controller's behavior and system dynamics, providing sample, local, domain and universe level explanations via IF-THEN rules revealing the controller's decision logic and salience values quantifying the contribution of system states to control actions. Third, a large language model agent-supported user interface is developed to automatically analyze user requirements, select appropriate algorithms, interpret the generated explanations to a natural language report, and provide interactive consultation. Case studies on inverted pendulum system and Turtlebot obstacle avoidance demonstrate the effectiveness of the proposed method through simulated user experiments and quantitative comparisons with mainstream explainable control approaches.

</details>

---

### [[20_Research/Papers/大模型/Semantic_Consistency_Policy_Optimization_for_Reinforcement_Learning_of_LLM_Agents|Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents]]

![[assets/2606.25852_figure.png|800]]

- **arXiv**: [2606.25852](https://arxiv.org/abs/2606.25852)
- **PDF**: https://arxiv.org/pdf/2606.25852
- **详细分析**: [[20_Research/Papers/大模型/Semantic_Consistency_Policy_Optimization_for_Reinforcement_Learning_of_LLM_Agents|Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents]]
- **作者**: Peng Xu, Sijia Chen, Junzhuo Li, Xuming Hu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.72（加权：大模型 0.8，强化学习 1.76，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Group-based reinforcement learning effectively post-trains LLM agents for long-horizon, sparse-reward tasks by deriving step-level credit from trajectory outcomes. However, this ties a step's credit to its rollout's final outcome: semantically near-identical intermediate steps receive opposite credit depending on whether their trajectory eventually succeeded or failed. Such semantic credit inconsistency sends conflicting gradients to similar actions and wastes the partially-correct progress inside failed rollouts. Motivated by this, we propose Semantic Consistency Policy Optimization (SCPO), a value-free reward-shaping method that mitigates this inconsistency by recovering step-level credit from successful siblings in the same rollout group. Concretely, SCPO scores each failed step against a successful sibling and adds positive step-level credit for new progress along that sibling. On ALFWorld and WebShop, SCPO matches or exceeds strong group-based baselines, reaching 93.7+/-4.1 percent success on ALFWorld and 74.8+/-2.0 percent on WebShop at 1.5B parameters, with gains concentrated on the hardest multi-step tasks.

</details>

---

### [[20_Research/Papers/大模型/Uncertainty_Quantification_for_Computer-Use_Agents_A_Benchmark_across_Vision-Language_Models_and_GUI_Grounding_Datasets|Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets]]

![[assets/2606.25760_figure.png|800]]

- **arXiv**: [2606.25760](https://arxiv.org/abs/2606.25760)
- **PDF**: https://arxiv.org/pdf/2606.25760
- **详细分析**: [[20_Research/Papers/大模型/Uncertainty_Quantification_for_Computer-Use_Agents_A_Benchmark_across_Vision-Language_Models_and_GUI_Grounding_Datasets|Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets]]
- **作者**: Divake Kumar, Sina Tayebati, Devashri Naik, Amanda Sofie Rios, Nilesh Ahuja, Omesh Tickoo, Ranganath Krishnan, Amit Ranjan Trivedi
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OSWorld, VLM-UQ-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computer-use agents turn vision-language model (VLM) predictions into executable GUI clicks, so reliable uncertainty estimates are essential for rejection, calibration, miss-severity ranking, and spatial safety regions. Yet evidence on post-hoc uncertainty quantification (UQ) for these agents is fragmented across isolated model and dataset pairs, leaving it unclear whether UQ rankings stay stable when the agent, benchmark, or observable interface changes. We present Argus, a cross-regime benchmark for post-hoc UQ in single-step executable GUI grounding: a 27-method open-weight matrix over 4 VLM agents and 4 datasets, plus an 8-method closed-source matrix across 3 frontier vendors where logits, hidden states, and attention maps are unavailable. Evaluated methods span logit-based scores, sampling and consistency measures, hidden-state and density estimators (Mahalanobis, SAPLMA), attention-based scores, P(True) and verbalised-confidence prompting, and split-conformal prediction. The main finding is selective transfer: UQ rankings are stable across datasets for a fixed model, but degrade across model classes and observable interfaces. Hidden-state and density methods are the most stable open-weight family, while CoCoA-1MCA, Focus, sampling-based scores, and verbalised self-assessment win in specific regimes. Within-model ranking transfer is strong (Spearman rho up to 0.969), but cross-tier transfer to closed-source vendors averages only +0.08, so closed-source UQ should be reranked on the target rather than extrapolated. Conformal click regions show score-level discrimination is not enough for deployment: locally weighted disks shrink radii by 40-60% when the plug-in UQ is calibrated, but coverage degrades under calibration-test or interface mismatch. We release per-item records, calibration/test splits, UQ scores, and analysis scripts for regime-aware UQ selection in GUI agents.

</details>

---

### [[20_Research/Papers/大模型/BiPACE_Bisimulation-Guided_Policy_Optimization_with_Action_Counterfactual_Estimation_for_LLM_Agents|BiPACE: Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation for LLM Agents]]

![[assets/2606.25556_figure.png|800]]

- **arXiv**: [2606.25556](https://arxiv.org/abs/2606.25556)
- **PDF**: https://arxiv.org/pdf/2606.25556
- **详细分析**: [[20_Research/Papers/大模型/BiPACE_Bisimulation-Guided_Policy_Optimization_with_Action_Counterfactual_Estimation_for_LLM_Agents|BiPACE: Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation for LLM Agents]]
- **作者**: Hanyang Wang, Weijieying Ren, Yuxiang Zhang, Ding Cao, Zhizhao Zeng, Ke Zeng, Tianxiang Zhao
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.07（加权：大模型 0.95，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《BiPACE: Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation for LLM Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, Pre-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Stepwise group-based RL is an attractive way to train long-horizon LLM agents without a learned critic: it reuses multiple sampled rollouts to estimate local advantages. Its weakness is less visible but more fundamental: every group-relative estimator assumes that the steps it compares are equivalent for credit assignment. We show that current agentic variants violate this assumption through a state-action credit mismatch. The observation-hash partition is overly fine on the state side, creating singleton groups with zero step-level signal, while a single within-group mean is too coarse on the action side, mixing state-value estimation with action-specific credit. We introduce BiPACE (Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation), a drop-in advantage estimator that fixes both sides without adding a critic, auxiliary loss, or extra rollouts. BiGPO clusters steps by cosine distance in the actor's own hidden-state geometry, an empirical policy-induced proxy for bisimulation that substantially lowers the singleton rate left by observation hashing. PACE then recenters returns within each behavioral cluster using action-conditioned peer baselines; its Q-style instance estimates a local Q(s,a)-V(s) nonparametrically. On ALFWorld/Qwen2.5-7B, BiPACE_Q raises overall validation success from GiGPO's 90.8 to $97.1\pm0.9$ over three seeds, and crosses the 95% threshold on every seed, which GiGPO never does within the same budget. On Qwen2.5-1.5B it reaches $93.5\pm1.2$ versus GiGPO's 86.7, and on WebShop and TextCraft it improves over GRPO and GiGPO at both model scales. The measured BiPACE-specific overhead is 11.3% of a single training-step wall time. Yet it changes the estimator's comparison unit from surface identity to approximate behavioral equivalence plus action-side counterfactuals. The code is available at https://github.com/TianxiangZhao/BiPACE.

</details>

---

### [[20_Research/Papers/强化学习/Rate-Aware_Quantum-Inspired_Trajectory_Learning_for_Interference-Limited_Multi-UAV_Networks|Rate-Aware Quantum-Inspired Trajectory Learning for Interference-Limited Multi-UAV Networks]]

![[assets/2606.25480_first_page.png|800]]

- **arXiv**: [2606.25480](https://arxiv.org/abs/2606.25480)
- **PDF**: https://arxiv.org/pdf/2606.25480
- **详细分析**: [[20_Research/Papers/强化学习/Rate-Aware_Quantum-Inspired_Trajectory_Learning_for_Interference-Limited_Multi-UAV_Networks|Rate-Aware Quantum-Inspired Trajectory Learning for Interference-Limited Multi-UAV Networks]]
- **作者**: Khaoula Khaled, Muhammad Afaq, Ali Arshad Nasir, Zeeshan Kaleem
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习
- **相关性评分**: 1.0（加权：强化学习 0.2，机器人 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Rate-Aware Quantum-Inspired Trajectory Learning for Interference-Limited Multi-UAV Networks》归入 机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicle (UAV) can provide on-demand, high-capacity connectivity in disaster and normal situation. However, it faces a challenge of curse of dimensionality in trajectory optimization, where interference-limited environments and vast search spaces make real-time coordination computationally expensive. To overcome this challenge, we propose the Rate-Aware Quantum-Annealed Graph Condensation (RA-QAGC) scheme, which combines rate-aware graph abstraction with decentralized reinforcement learning to enable scalable, interference-aware UAV coordination. By identifying high throughput locations and guiding UAV trajectory adaptation toward throughput-optimal regions, RA-QAGC effectively balances network capacity by maintaining quality-of-service (QoS) requirements. Simulation results demonstrate the proposal outperformed over existing schemes by achieving 59.4 Mbps total throughput and 23.9 Mbps priority-user throughput, representing gains of approximately 15% and 34%, respectively, over the baseline schemes.

</details>

---

### [[20_Research/Papers/大模型/BrainAgent_A_Large_Language_Model-Driven_Multi-Agent_Framework_for_Autonomous_Brain_Signal_Understanding|BrainAgent: A Large Language Model-Driven Multi-Agent Framework for Autonomous Brain Signal Understanding]]

![[assets/2606.25400_figure.png|800]]

- **arXiv**: [2606.25400](https://arxiv.org/abs/2606.25400)
- **PDF**: https://arxiv.org/pdf/2606.25400
- **详细分析**: [[20_Research/Papers/大模型/BrainAgent_A_Large_Language_Model-Driven_Multi-Agent_Framework_for_Autonomous_Brain_Signal_Understanding|BrainAgent: A Large Language Model-Driven Multi-Agent Framework for Autonomous Brain Signal Understanding]]
- **作者**: Yangxuan Zhou, Sha Zhao, Jiquan Wang, Shijian Li, Gang Pan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《BrainAgent: A Large Language Model-Driven Multi-Agent Framework for Autonomous Brain Signal Understanding》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Brain-Computer Interfaces (BCIs) and brain signal understanding are pivotal for clinical health and next-generation interactions. Despite this significance, its widespread adoption in real-world scenarios remains restricted, primarily because current analytical paradigms lack sufficient agentic intelligence. First, existing methodologies impose prohibitive technical barriers, requiring extensive specialized expertise. Second, they remain inherently static and task-specific, failing to execute the complex, long-horizon workflows essential for real-world deployment. To accelerate the democratization of brain signal understanding, we draw inspiration from Large Language Models (LLMs) to introduce BrainAgent, an LLM-driven multi-agent framework designed to ground abstract natural language intent into rigorous, executable, and end-to-end processing pipelines. BrainAgent employs a hierarchical architecture where a central supervisor orchestrates specialized sub-agents for adaptive task decomposition and execution. Furthermore, we establish a comprehensive, systematic benchmark for evaluating agentic systems in brain signal analysis. Empirical results demonstrate that BrainAgent effectively automates complex workflows with superior reliability, marking a paradigm shift toward democratized brain signal understanding.

</details>

---

### [[20_Research/Papers/大模型/Agentic_Knowledge_Tracing_A_Multi-Agent_LLM_Architecture_for_Stealth_Assessment_of_Financial_Literacy_in_Serious_Games|Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games]]

![[assets/2606.25358_figure.png|800]]

- **arXiv**: [2606.25358](https://arxiv.org/abs/2606.25358)
- **PDF**: https://arxiv.org/pdf/2606.25358
- **详细分析**: [[20_Research/Papers/大模型/Agentic_Knowledge_Tracing_A_Multi-Agent_LLM_Architecture_for_Stealth_Assessment_of_Financial_Literacy_in_Serious_Games|Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games]]
- **作者**: Gabriel Santos, Rita Julia, Marcelo Nascimento
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Assessing financial literacy during gameplay without disrupting the learning experience remains a key challenge in serious games for education. We present the Agentic BKT pipeline, a multi-agent large language model architecture for stealth assessment of financial competencies from open-ended gameplay events. The pipeline processes events from a 2D platformer serious game aligned with the OECD/INFE financial literacy framework through four phases: (1) the game captures every player decision as a structured event log; (2) an LLM event classifier labels each action on a four-point rubric validated against three domain experts (Fleiss kappa = 0.624, substantial agreement); (3) four domain-specific agents specializing in risk mitigation, investing, spending, and credit management perform session-level reasoning over behavioral trajectories, feeding per-competency Bayesian Knowledge Tracing that estimates mastery within each domain; and (4) an expert judge agent synthesizes the domain-level estimates into an overall mastery score. Evaluated with 193 K-12 participants across 264 game sessions, the Agentic BKT pipeline yields mastery estimates significantly correlated with learning gain (r = 0.276, p = 0.0001) and post-test scores (r = 0.333, p &lt; 0.0001) while showing no correlation with pre-test scores, providing both convergent and discriminant validity. The multi-agent approach approximately triples the predictive validity of a single-LLM baseline (r = 0.095, not significant) in this study, demonstrating that domain decomposition and session-level reasoning play a central role in capturing the multidimensional nature of financial literacy from gameplay

</details>

---

### [[20_Research/Papers/强化学习/Compositional_Behavioral_Semantics_for_State_Abstraction_in_Reinforcement_Learning|Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning]]

![[assets/2606.25357_first_page.png|800]]

- **arXiv**: [2606.25357](https://arxiv.org/abs/2606.25357)
- **PDF**: https://arxiv.org/pdf/2606.25357
- **详细分析**: [[20_Research/Papers/强化学习/Compositional_Behavioral_Semantics_for_State_Abstraction_in_Reinforcement_Learning|Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning]]
- **作者**: Yivan Zhang, Ziyan Luo, Manuel Baltieri
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

State abstraction plays a key role in scaling reinforcement learning to complex but structured systems. In studying such systems, a wide range of behavioral structures have been studied in reinforcement learning, including value functions, invariants, bisimulation relations, and behavioral metrics. However, a general principle for determining what structures are provably preserved under state abstraction is still lacking. In this paper, we present a unified framework for defining and analyzing behavioral structures in reinforcement learning. Our framework provides a compositional way to specify behavioral semantics based on local, one-step descriptions of system dynamics. Using this framework, we establish results showing how behavioral structures can be safely transferred between abstract and concrete systems. We further show how to construct quantitative metrics from logical behavioral semantics with soundness guarantees. Together, these results provide a principled foundation for reasoning about behaviors under state abstraction in reinforcement learning and offer reusable definition and proof principles for a broad class of behavioral structures in reinforcement learning.

</details>

---

### [[20_Research/Papers/具身智能/AI_Coaching_for_Accelerating_Human_Skill_Development_with_Reinforcement_Learning|AI Coaching for Accelerating Human Skill Development with Reinforcement Learning]]

![[assets/2606.25337_figure.png|800]]

- **arXiv**: [2606.25337](https://arxiv.org/abs/2606.25337)
- **PDF**: https://arxiv.org/pdf/2606.25337
- **详细分析**: [[20_Research/Papers/具身智能/AI_Coaching_for_Accelerating_Human_Skill_Development_with_Reinforcement_Learning|AI Coaching for Accelerating Human Skill Development with Reinforcement Learning]]
- **作者**: Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam
- **cs 子类**: cs.AI, cs.HC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.9，大模型 0.1，强化学习 0.8，机器人 0.5）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《AI Coaching for Accelerating Human Skill Development with Reinforcement Learning》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI copilots can substantially boost human performance through shared control, but excessive assistance can induce over-reliance and skill atrophy. This paper studies how an embodied AI agent can act as a coach that accelerates human motor-skill development. We argue that effective coaching requires strategic scaffolding and stepping back that are aligned with the learner's capability, allowing productive failures that drive learning. We formalize the interactive AI coaching process as a non-cooperative dynamic game in which the learner optimizes task performance while the coach targets the learner's independent competence. Building on this formalism, we develop a reinforcement learning framework combining adaptive shared control with probabilistic models of the coach's causal influence on skill evolution, enabling tractable training of coaching policies. A comprehensive user study (N=33) on first-person-view drone racing shows significant gains in human learning outcomes over state-of-the-art AI coaching baselines.

</details>

---

### [[20_Research/Papers/大模型/Omni-Perception_Policy_Optimization_for_Multimodal_Emotion_Reasoning|Omni-Perception Policy Optimization for Multimodal Emotion Reasoning]]

![[assets/2606.25325_figure.png|800]]

- **arXiv**: [2606.25325](https://arxiv.org/abs/2606.25325)
- **PDF**: https://arxiv.org/pdf/2606.25325
- **详细分析**: [[20_Research/Papers/大模型/Omni-Perception_Policy_Optimization_for_Multimodal_Emotion_Reasoning|Omni-Perception Policy Optimization for Multimodal Emotion Reasoning]]
- **作者**: Zhiyuan Han, Beier Zhu, Wenwen Tong, Pengyang Shao, Peipei Song, Xinyi Wang, Jiangnan Chen, Lewei Lu, Xun Yang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.4，强化学习 1）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Omni-Perception Policy Optimization for Multimodal Emotion Reasoning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MEP-Bench, MER-UniBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We find that current emotion-oriented Omni-MLLMs still lack reliable omni-modal perception: they (i) underutilize multimodal cues in their reasoning trajectories and (ii) exhibit unfaithful behavior, often hallucinating modality-specific statements from other modalities. Building on these insights, we propose OPPO (Omni-Perception Policy Optimization), a reinforcement learning framework that explicitly optimizes multimodal perception. First, an Omni-Perception Reward decomposes ground-truth reasoning into fine-grained visual, acoustic, and emotion cues and rewards trajectories that semantically recover these cues. Second, an Omni-Perception Loss compares the policy under full and unimodally masked inputs, applying a KL penalty only to modality-specific evidence tokens to suppress cross-modal hallucination. We further introduce MEP-Bench, a diagnostic benchmark that quantifies utilization and faithfulness. Experiments show that OPPO achieves state-of-the-art performance on MER-UniBench and MME-Emotion, while substantially improving utilization and faithfulness scores on MEP-Bench, highlighting the importance of sufficient and faithful omni perception for multimodal emotion reasoning.

</details>

---

### [[20_Research/Papers/具身智能/RAVEN_Long-Horizon_Reasoning_&_Navigation_with_a_Visuo-Spatio-Temporal_Memory|RAVEN: Long-Horizon Reasoning & Navigation with a Visuo-Spatio-Temporal Memory]]

![[assets/2606.25206_figure.png|800]]

- **arXiv**: [2606.25206](https://arxiv.org/abs/2606.25206)
- **PDF**: https://arxiv.org/pdf/2606.25206
- **详细分析**: [[20_Research/Papers/具身智能/RAVEN_Long-Horizon_Reasoning_&_Navigation_with_a_Visuo-Spatio-Temporal_Memory|RAVEN: Long-Horizon Reasoning & Navigation with a Visuo-Spatio-Temporal Memory]]
- **作者**: Yixun Hu, Zhicheng Zheng, Lihan Zha, Chunwei Xing, Rajdeep Singh, Omar Hossain, Antonio Loquercio, Dhruv Shah
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《RAVEN: Long-Horizon Reasoning & Navigation with a Visuo-Spatio-Temporal Memory》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：NaVQA, RAVEN-QA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term robot deployment requires a compact and scalable memory that preserves fine-grained visual semantics, grounds observations in space and time, and enables efficient storage and retrieval. In this paper, we propose RAVEN, an agentic memory system for long-horizon robotic question answering and navigation. RAVEN stores visual embeddings with pose and time in a vector database, and grounds retrieval in a spatial map to answer queries and navigate to goals. By operating directly on visual embeddings, RAVEN avoids lossy image-to-text captioning and enables accurate semantic, spatial, and temporal retrieval at scale. Across several simulated and real-world video question-answering benchmarks, RAVEN consistently surpasses caption-based memory systems and matches frontier VLMs on long-horizon tasks at 10$\times$ lower retrieval cost. Finally, we instantiate RAVEN on a Unitree Go1 robot for the task of long-horizon navigation for natural language goal-reaching, and show successful deployment over several large indoor environments.

</details>

---

### [[20_Research/Papers/大模型/To_Isolate_or_to_Score_Model-Adaptive_Assessment_for_Cost-Efficient_Multi-Agent_RAG|To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG]]

![[assets/2606.25191_figure.png|800]]

- **arXiv**: [2606.25191](https://arxiv.org/abs/2606.25191)
- **PDF**: https://arxiv.org/pdf/2606.25191
- **详细分析**: [[20_Research/Papers/大模型/To_Isolate_or_to_Score_Model-Adaptive_Assessment_for_Cost-Efficient_Multi-Agent_RAG|To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG]]
- **作者**: Jungseob Lee, Chanjun Park, Heuiseok Lim
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Agent

#### 研究背景与动机

《To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent document assessment for retrieval-augmented generation is computationally expensive, driving practitioners toward smaller, deployable models whose assessment mechanisms remain poorly understood. We conduct a controlled study of training-free interventions on 7B-9B instruction-tuned models across diverse QA benchmarks, revealing a sharp dichotomy in how models benefit from assessment. For weaker baselines, the dominant mechanism is per-document isolation. Astoundingly, assessment-free isolation matches full multi-agent assessment, demonstrating that resolving multi-document context confusion, rather than scoring quality, drives outsized gains of up to 50 percentage points. Conversely, for strong baselines where scoring quality matters, we introduce Reasoning-Score Coupling, a label-free perturbation probe that classifies scoring behavior. Integrating these findings, we propose MADARA, a model-adaptive routing architecture. Crucially, MADARA's diagnostic thresholds derived from a single pilot model generalize zero-shot to four unseen model families, providing a robust, lightweight pipeline to eliminate computational overhead.

</details>

---

### [[20_Research/Papers/大模型/TRUSTMEM_Learning_Trustworthy_Memory_Consolidation_for_LLM_Agents_with_Long-Term_Memory|TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory]]

![[assets/2606.25161_figure.png|800]]

- **arXiv**: [2606.25161](https://arxiv.org/abs/2606.25161)
- **PDF**: https://arxiv.org/pdf/2606.25161
- **详细分析**: [[20_Research/Papers/大模型/TRUSTMEM_Learning_Trustworthy_Memory_Consolidation_for_LLM_Agents_with_Long-Term_Memory|TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory]]
- **作者**: Tianyu Yang, Sudipta Paul, Vijay Srinivasan, Vivek Kulkarni, Srinivas Chappidi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.2（加权：大模型 1，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongMemEval, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents rely on long-term memory to support extended interactions and personalized assistance beyond finite context windows. Existing memory agents actively update external memory through generated write, revise, and delete operations, but these updates may omit important information, corrupt existing memory, or introduce unsupported hallucinated content. Once stored, such errors become persistent system-state failures that can affect future reasoning and generation. In this paper, we propose TrustMem, a framework designed to improve the trustworthiness of memory consolidation. TrustMem relies on a Memory Transition Verifier to evaluate the transition process of memory updates in terms of coverage, preservation, and faithfulness. It further constructs preference pairs among candidate updates under the same memory state, enabling preference-guided reinforcement learning to directly optimize memory updating behaviors. Extensive experiments demonstrate that TrustMem improves both memory utility and reliability: it achieves state-of-the-art results across MemoryAgentBench, HaluMem, and the Mem-alpha validation set, improves HaluMem memory extraction by 12.14 F1 points, and reduces transition-level omission, corruption, and hallucination by 40.1\%, 79.1\%, and 50.0\%, respectively, compared with the strongest baseline for each error type.

</details>

---

### [[20_Research/Papers/具身智能/Reward-Conditioned_Attention_How_Reward_Design_Shapes_What_Autonomous_Driving_Agents_See|Reward-Conditioned Attention: How Reward Design Shapes What Autonomous Driving Agents See]]

![[assets/2606.25127_figure.png|800]]

- **arXiv**: [2606.25127](https://arxiv.org/abs/2606.25127)
- **PDF**: https://arxiv.org/pdf/2606.25127
- **详细分析**: [[20_Research/Papers/具身智能/Reward-Conditioned_Attention_How_Reward_Design_Shapes_What_Autonomous_Driving_Agents_See|Reward-Conditioned Attention: How Reward Design Shapes What Autonomous Driving Agents See]]
- **作者**: Mohamed Benabdelouahad, Ahmed Djalal Hacini, Nadir Farhi, Aissa Boulmerka
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Reward-Conditioned Attention: How Reward Design Shapes What Autonomous Driving Agents See》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We investigate how reward design shapes the internal attention patterns of reinforcement learning agents trained for autonomous driving. Using three Perceiver-based agents that share identical architectures and training data but differ only in their reward configurations$\unicode{x2014}$ranging from basic violation penalties to continuous proximity penalties$\unicode{x2014}$we analyze cross-attention allocation across 50 real-world scenarios from the Waymo Open Motion Dataset. A central methodological finding is that naïve pooling of timesteps across episodes substantially underestimates the attention$\unicode{x2013}$risk relationship; within-episode correlation with Fisher z-transform aggregation is the appropriate statistic and reveals a robustly positive link between collision risk and agent-directed attention. Building on this validated methodology, we demonstrate two reward-conditioned effects: agents trained with navigation rewards allocate up to $2.0\times$ more attention to GPS-path tokens than those trained with additional proximity penalties$\unicode{x2014}$and $4.7\times$ more than agents with no navigation incentive$\unicode{x2014}$revealing that reward content directly determines which scene elements the encoder prioritizes, and continuous time-to-collision penalties create a $\textit{learned vigilance prior}$$\unicode{x2014}$elevated resting agent surveillance maintained throughout collision-free phases. In several scenarios, the complete-reward and minimal-reward models exhibit opposite attention$\unicode{x2013}$risk correlation directions, demonstrating that reward design can qualitatively reverse attentional strategy rather than merely modulating its magnitude. These results suggest that attention analysis is a practical diagnostic for verifying that a reward function produces the intended representational behaviour in safety-critical RL systems.

</details>

---

### [[20_Research/Papers/强化学习/GCT-MARL_Graph-Based_Contrastive_Transfer_for_Sample-Efficient_Cooperative_Multi-Agent_Reinforcement_Learning|GCT-MARL: Graph-Based Contrastive Transfer for Sample-Efficient Cooperative Multi-Agent Reinforcement Learning]]

![[assets/2606.25073_figure.png|800]]

- **arXiv**: [2606.25073](https://arxiv.org/abs/2606.25073)
- **PDF**: https://arxiv.org/pdf/2606.25073
- **详细分析**: [[20_Research/Papers/强化学习/GCT-MARL_Graph-Based_Contrastive_Transfer_for_Sample-Efficient_Cooperative_Multi-Agent_Reinforcement_Learning|GCT-MARL: Graph-Based Contrastive Transfer for Sample-Efficient Cooperative Multi-Agent Reinforcement Learning]]
- **作者**: Animesh Animesh, Satheesh K Perepu, Kaushik Dey
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《GCT-MARL: Graph-Based Contrastive Transfer for Sample-Efficient Cooperative Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Continual-RL, GCT-MARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In cooperative multi-agent reinforcement learning (MARL), from a deployment perspective, it is challenging and expensive to train agents from scratch for each new environment or task. In this work, we propose GCT-MARL, a transfer learning framework that builds on the multi-view graph contrastive backbone of MAIL and augments it with a per-view, adaptively weighted alignment loss and a two-phase training protocol specifically designed for transfer across populations of varying sizes and compositions. We empirically demonstrate that the proposed framework markedly accelerates convergence on the target task relative to from-scratch training, in both homogeneous (within-faction, varying N) and heterogeneous (cross-faction and mixed unit-type) transfer scenarios. Furthermore, we show that the framework naturally supports continual learning by sequentially chaining the two-phase transfer protocol across a series of related tasks. Overall, this work provides a unified approach to mitigating key limitations in current MARL transfer methods with new insights at both methodological and empirical levels.

</details>

---

### [[20_Research/Papers/大模型/ExTra_Exploratory_Trajectory_Optimization_for_Language_Model_Reinforcement_Learning|ExTra: Exploratory Trajectory Optimization for Language Model Reinforcement Learning]]

![[assets/2606.24994_figure.png|800]]

- **arXiv**: [2606.24994](https://arxiv.org/abs/2606.24994)
- **PDF**: https://arxiv.org/pdf/2606.24994
- **详细分析**: [[20_Research/Papers/大模型/ExTra_Exploratory_Trajectory_Optimization_for_Language_Model_Reinforcement_Learning|ExTra: Exploratory Trajectory Optimization for Language Model Reinforcement Learning]]
- **作者**: Wenyang Hu, Junxiang Jia, Zhen Shu, Daniel Dahlmeier, See-Kiong Ng, Bryan Kian Hsiang Low
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《ExTra: Exploratory Trajectory Optimization for Language Model Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OlympiadBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) for language-model reasoning can fail at both extremes of task difficulty: easy prompts often produce all-correct, low-diversity rollout groups with little gradient signal, while hard prompts can produce all-incorrect groups with no positive reward. We introduce ExTra (Exploratory Trajectory Optimization), a GRPO-compatible framework that extracts exploration signals from the model's own rollouts. ExTra combines two mechanisms: (i) a novelty reward that adds embedding-based diversity bonuses after GRPO normalization, rewarding diverse correct solutions; and (ii) entropy-guided prefix regeneration, which scores partial trajectories using entropy signals and continues exploration from promising intermediate steps. Across six mathematical reasoning benchmarks, ExTra improves Qwen3-1.7B over GRPO by about +5 points on pass@1 and +7 points on pass@16, showing that trajectory-level exploration signals can improve both single-sample accuracy and inference-time coverage.

</details>

---

### [[20_Research/Papers/强化学习/Uncertainty-aware_reinforcement_learning_for_chemical_language_models|Uncertainty-aware reinforcement learning for chemical language models]]

![[assets/2606.24990_first_page.png|800]]

- **arXiv**: [2606.24990](https://arxiv.org/abs/2606.24990)
- **PDF**: https://arxiv.org/pdf/2606.24990
- **详细分析**: [[20_Research/Papers/强化学习/Uncertainty-aware_reinforcement_learning_for_chemical_language_models|Uncertainty-aware reinforcement learning for chemical language models]]
- **作者**: Borja Medina, Jon Paul Janet
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Uncertainty-aware reinforcement learning for chemical language models》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has become a powerful paradigm for de novo molecular design, enabling Chemical Language Models (CLMs) to navigate and explore the chemical space while optimizing specific desired properties. However, the existing RL frameworks treat all scoring functions as deterministic oracles, neglecting the inherent uncertainty attached to the predictions of the different molecular properties. This can lead to the exploration of highly-uncertain regions of the chemical space, focusing on the generation of highly scored molecules which are poorly supported by the training data. This can destabilize the optimization process, yielding predictions that are far from their true values. We propose and compare two complementary ways of incorporating predictive uncertainty into RL. In the first one, uncertainty is treated as an additional optimization objective and incorporated along with the rest of the scoring functions, allowing the policy to trade off exploitation against reliability. Secondly, uncertainty is used to modulate policy updates, reducing the influence of molecules whose properties lie far outside the scoring function confidence domain. Both approaches were evaluated across three different settings: (i) a controlled model system, in which the prediction error is modeled as a Gaussian distribution, with a variance proportional to the distance to the training data; and two real-world tasks, making use of (ii) ChemProp models and (iii) a Conformal Prediction wrapper applied to a Random forest classifier. We show that uncertainty-aware RL enables CLMs to explore chemical space more robustly by favoring lower-uncertainty regions. This leads to more reliable hit discovery without compromising molecular score, increasing the true hit rate by 0.25 (from 0.5 to 0.75), and nearly doubling the total number of true hits.

</details>

---

### [[20_Research/Papers/大模型/The_Hitchhiker's_Guide_to_Agentic_AI_From_Foundations_to_Systems|The Hitchhiker's Guide to Agentic AI: From Foundations to Systems]]

![[assets/2606.24937_first_page.png|800]]

- **arXiv**: [2606.24937](https://arxiv.org/abs/2606.24937)
- **PDF**: https://arxiv.org/pdf/2606.24937
- **详细分析**: [[20_Research/Papers/大模型/The_Hitchhiker's_Guide_to_Agentic_AI_From_Foundations_to_Systems|The Hitchhiker's Guide to Agentic AI: From Foundations to Systems]]
- **作者**: Haggai Roitman
- **cs 子类**: cs.AI, cs.CL, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.07（加权：大模型 0.55，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《The Hitchhiker's Guide to Agentic AI: From Foundations to Systems》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Hitchhiker's Guide to Agentic AI is a comprehensive practitioner's reference for building autonomous AI systems. The book covers the full stack from first principles to production deployment, organized around a central thesis: building great agentic systems requires understanding every layer of the pipeline, not just one. The book opens with the LLM substrate -- transformer architecture, GPU systems, training and fine-tuning (SFT,LoRA, MoE), model compression, and inference optimization -- treated as essential foundations rather than the primary focus. It then develops the alignment and reasoning layer: reinforcement learning from human feedback (RLHF), PPO, DPO and its variants, GRPO, reward modeling, and RL for large reasoning models including chain-of-thought and test-time scaling. The second half is devoted to agentic AI proper. Topics include agentic training and trajectory-based RL, retrieval-augmented generation (RAG and Agentic RAG), memory systems (in-context, external, episodic, and semantic), agent harness design and context management, and a taxonomy of agent design patterns. Inter-agent coordination is covered in depth: the Model Context Protocol (MCP), agent skills and tool use, the Agent-to-Agent (A2A) communication protocol, and multi-agent architectures spanning centralized, decentralized, and hierarchical topologies. The book concludes with agent development frameworks, agentic UI design, evaluation methodology for agentic tasks, and production deployment. Each chapter pairs rigorous theoretical foundations with implementation guidance, code examples, and references to the primary literature.

</details>

---

### [[20_Research/Papers/机器人/End-to-End_Voice_Intent_Recognition_for_Spontaneous_Human-Drone_Interaction_with_Naive_Users|End-to-End Voice Intent Recognition for Spontaneous Human-Drone Interaction with Naive Users]]

![[assets/2606.24910_first_page.png|800]]

- **arXiv**: [2606.24910](https://arxiv.org/abs/2606.24910)
- **PDF**: https://arxiv.org/pdf/2606.24910
- **详细分析**: [[20_Research/Papers/机器人/End-to-End_Voice_Intent_Recognition_for_Spontaneous_Human-Drone_Interaction_with_Naive_Users|End-to-End Voice Intent Recognition for Spontaneous Human-Drone Interaction with Naive Users]]
- **作者**: Allan Henry, Solange Rossato, Christian Graff, Sylvain Huet, Jose-Ernesto Gomez-Balderas
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: cs.AI

#### 研究背景与动机

《End-to-End Voice Intent Recognition for Spontaneous Human-Drone Interaction with Naive Users》归入 机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Voice control offers an intuitive alternative to manual drone piloting, yet most existing systems rely on rigid command vocabularies that fail to handle the spontaneous, disfluent speech of naive users. This paper addresses this gap by proposing an End-to-End Spoken Language Understanding architecture for real-time human-drone interaction in French. Our model combines a frozen Self-Supervised Learning acoustic encoder with a lightweight LSTM-based classification head, augmented by a cross-modal knowledge distillation objective that aligns acoustic representations with semantic embeddings from a text teacher, without requiring transcription at inference time. We evaluate our approach on VoiceStick, a novel French corpus of spontaneous speech collected during real teleoperation sessions with 29 nonexpert dyads. On simple voice commands, our best configuration achieves 93% accuracy at 7 ms inference latency, outperforming cascade baselines (79%, 202 ms) with a 29x speedup. On the full spontaneous speech test set, our architecture reaches 82% accuracy, with crossmodal distillation consistently improving robustness across all configurations. These results demonstrate that End-to-End architectures are not only feasible but preferable for spontaneous voice-guided UAV teleoperation, combining semantic robustness, low latency, and calibrated confidence.

</details>

---

### [[20_Research/Papers/大模型/LLM_Evolution_as_an_Industry-Scale_Ecosystem_A_Lifecycle_Perspective_on_Continual_Learning|LLM Evolution as an Industry-Scale Ecosystem: A Lifecycle Perspective on Continual Learning]]

![[assets/2606.24901_figure.png|800]]

- **arXiv**: [2606.24901](https://arxiv.org/abs/2606.24901)
- **PDF**: https://arxiv.org/pdf/2606.24901
- **详细分析**: [[20_Research/Papers/大模型/LLM_Evolution_as_an_Industry-Scale_Ecosystem_A_Lifecycle_Perspective_on_Continual_Learning|LLM Evolution as an Industry-Scale Ecosystem: A Lifecycle Perspective on Continual Learning]]
- **作者**: Hao Jiang, Enneng Yang, Guojie Zhu, Yibin Chen, Yunkun Xu, Zifu Kou, Jiayi Li, Chong Chen, Zhao Cao, Li Shen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《LLM Evolution as an Industry-Scale Ecosystem: A Lifecycle Perspective on Continual Learning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continual learning capability is critical for Industrial LLMs, as deployed models must be continuously updated to meet evolving requirements and environments, rather than repeatedly retrained from scratch. However, most existing research focuses on improvements on static benchmarks, failing to capture real industrial needs. In this survey, we reformulate Industrial Continual Learning (ICL) for LLMs as a closed-loop update-and-release problem in a versioned ecosystem, where updates propagate hierarchically to industrial, application-specific models and LLM-powered applications, with capability inheritance and transfer across versions and model families. From this ecosystem perspective, we identify three core challenges: repeated adaptation erodes model plasticity, foundation-model upgrades break capability inheritance, and long-term sustainability is constrained by deployment requirements. We then organize the technical landscape of ICL around five lifecycle design principles: preserving plasticity headroom, treating upgrades as capability transfer, enabling trustworthy continual reinforcement learning, making training recipes self-optimizing, and building accountability as a base layer for long-term iteration. For each principle, we synthesize representative technical directions. Finally, we evaluate the maturity of each principle and its technical components via an evidence-based lens, identify key gaps hindering real-world deployment, and outline a practical ICL deployment blueprint and a pathway for feeding industrial realities back into academic research.

</details>

---
