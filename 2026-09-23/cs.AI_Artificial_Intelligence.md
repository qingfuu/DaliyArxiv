# cs.AI | Artificial Intelligence | 2026-09-23

#arxiv #ComputerScience

**论文数**: 21

### [[20_Research/Papers/大模型/REFLEX_with_Jev_for_Efficient_Selective_Control_in_LLM_Agents|REFLEX with Jev for Efficient Selective Control in LLM Agents]]

![[assets/2609.26532_first_page.png|800]]

- **arXiv**: [2609.26532](https://arxiv.org/abs/2609.26532)
- **PDF**: https://arxiv.org/pdf/2609.26532
- **详细分析**: [[20_Research/Papers/大模型/REFLEX_with_Jev_for_Efficient_Selective_Control_in_LLM_Agents|REFLEX with Jev for Efficient Selective Control in LLM Agents]]
- **作者**: Tiantong Wu, Wei Yang Bryan Lim
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《REFLEX with Jev for Efficient Selective Control in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LLMRouterBench, REFLEX-Sim, Reflex-Sim, RouterBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents often use generative models for bounded decisions, raising the question of when these decisions can be handled more efficiently without reducing task success. We study REFLEX, an agent architecture that uses Jev as a fast, typed decision layer and calls a strong LLM when confidence is low, or generation is required. On a frozen 100-task benchmark, REFLEX achieves 95% success with 72.7% fewer strong-model calls than a strong-only agent, with reductions persisting across three fallback families. Controlled interventions show that reliability depends on action-set size and near-valid alternatives near authorization boundaries. External BFCL and $\tau$-style evaluations reveal limited advantages over a cheap generative cascade when ordinary routing is already highly accurate. These findings identify when selective control with Jev can reduce computation and where its benefits are limited.

</details>

---

### [[20_Research/Papers/大模型/PACT_From_Credit_Assignment_to_Critic_Alignment|PACT: From Credit Assignment to Critic Alignment]]

![[assets/2609.26355_first_page.png|800]]

- **arXiv**: [2609.26355](https://arxiv.org/abs/2609.26355)
- **PDF**: https://arxiv.org/pdf/2609.26355
- **详细分析**: [[20_Research/Papers/大模型/PACT_From_Credit_Assignment_to_Critic_Alignment|PACT: From Credit Assignment to Critic Alignment]]
- **作者**: Jiayan Fu, Hang Xu, Yong Zhang, Zhaokai Luo, Yao Hu, Dongyan Zhao, Mu Chuan
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.22（加权：大模型 0.3，强化学习 0.76，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《PACT: From Credit Assignment to Critic Alignment》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has become a central component of large language model (LLM) post-training, yet token-level credit lacks a generally accepted mathematical definition, leaving its relationship to commonly used training signals unclear. We formulate three regularity conditions, namely Completeness, Prefix Consistency, and Neutrality, and prove that they uniquely determine token-level credit. This characterization provides a unified basis for explaining phenomena across existing algorithms and guides the development of an improved actor-critic training procedure. Through this lens, an ideal teacher in On-Policy Distillation (OPD) acts as an implicit critic, yielding an expected policy gradient proportional to that induced by token-level credit. Response-level REINFORCE Leave-One-Out (RLOO) signals match the expected policy-gradient contribution of token-level credit despite their coarser granularity. We further establish approximate credit sparsity under bounded outcome rewards and show how intermediate critic errors in Generalized Advantage Estimation (GAE) can become comparable to the underlying credit. These motivate Policy Aligned Critic Training (PACT), which adopts an Actor-then-Critic update order to apply importance sampling correction to critic training and better align the critic with the updated policy. In agentic mathematical reasoning, PACT achieves 72.87% average accuracy across four benchmarks, outperforming GRPO and PPO by 8.80 and 13.16 percentage points, respectively. On SWE-bench Verified, PACT achieves a pass rate of 67.4%, outperforming PPO, GRPO, and SAO by 2.4, 2.0, and 3.8 percentage points, respectively.

</details>

---

### [[20_Research/Papers/具身智能/TriWorldBench_A_Tri-View_Consistency_Perspective_on_Embodied_World_Models|TriWorldBench: A Tri-View Consistency Perspective on Embodied World Models]]

![[assets/2609.26314_figure.png|800]]

- **arXiv**: [2609.26314](https://arxiv.org/abs/2609.26314)
- **PDF**: https://arxiv.org/pdf/2609.26314
- **详细分析**: [[20_Research/Papers/具身智能/TriWorldBench_A_Tri-View_Consistency_Perspective_on_Embodied_World_Models|TriWorldBench: A Tri-View Consistency Perspective on Embodied World Models]]
- **作者**: Xuanyi Liu, Haofeng Wang, Ruiqi Li, Danni Yu, Rui Wan, Ruixu Zhang, Siyu Tao, Xue Yang, Shaofeng Zhang, Zicheng Zhang, Jiaqi Zhang, Siwei Ma
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，世界模型 0.8，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《TriWorldBench: A Tri-View Consistency Perspective on Embodied World Models》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Ctrl-World, EWMBench, PAVXploreRL, RBench, RoboWM-Bench, TriWorldBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied world models predict the outcomes of robot actions to support learning and planning. For robots equipped with head and wrist cameras, this requires complementary views: the head view captures the overall task, while wrist views reveal local gripper-object interactions. However, evaluating these views independently cannot determine whether they describe the same action and object state. We introduce TRIWORLDBENCH, a benchmark for evaluating embodied world models through synchronized head, left-wrist, and right-wrist videos. It contains 500 episodes across 50 bimanual manipulation tasks and uses 19 metrics to assess tri-view consistency, task alignment, physical and 3D coherence, motion quality, temporal consistency, and visual quality. By combining cross-view checks with measurements tailored to each camera, the benchmark evaluates whether plausible individual videos also form a consistent prediction of the intended task. We summarize overall performance with TWB-Score and retain per-view results to identify where predictions fail. This extends world-model evaluation beyond single-view visual quality. Code, data, and metric definitions are available at this https URL .

</details>

---

### [[20_Research/Papers/世界模型/Dual-Frontier_When_Can_an_Agent_Trust_Its_World_Model|Dual-Frontier: When Can an Agent Trust Its World Model?]]

![[assets/2609.26293_figure.png|800]]

- **arXiv**: [2609.26293](https://arxiv.org/abs/2609.26293)
- **PDF**: https://arxiv.org/pdf/2609.26293
- **详细分析**: [[20_Research/Papers/世界模型/Dual-Frontier_When_Can_an_Agent_Trust_Its_World_Model|Dual-Frontier: When Can an Agent Trust Its World Model?]]
- **作者**: Huatai Zhu, Qiang Chen, Ziqian Kou, Wenhao Li, Fei Wang, Yichao Cao, Xiu Su, Yi Chen
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.5（加权：大模型 0.5，世界模型 1）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Dual-Frontier: When Can an Agent Trust Its World Model?》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：AgentBench, DreamGym, Learned-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learned world models are becoming essential to general-purpose agents: by predicting action consequences, they support planning and decision-making while reducing reliance on costly trial and error. This reliance creates a fundamental ambiguity: when a world-model-guided decision fails, the trajectory alone may not reveal whether the agent's decision rule or the world model caused the loss. We formalize this failure-attribution problem as a counterfactual decomposition of return loss and prove that its components are not identifiable from passive interaction, even for finite-horizon planners. This obstruction motivates Dual-Frontier, a learning principle that admits a world-model-guided decision only when its predicted advantage exceeds a certified bound on decision-relevant world-model error; otherwise, evidence is allocated to world-model verification. Action-conditioned value bounds and a closed-loop extension guarantee non-decreasing return for admitted decisions. Calibrated gates and simultaneous confidence sequences support adaptive evidence reuse, with sufficient and necessary verification bounds. Controlled learned-model experiments validate the predicted failure modes and certification behavior, while cross-backbone tool-use benchmarks instantiate the same verify-then-promote rule in realistic agent world-model pipelines, consistently improving decision quality and reliability.

</details>

---

### [[20_Research/Papers/大模型/Silent_Sabotage_Internal_State_Triggered_Backdoor_Attacks_on_LLM-Powered_Robotic_Systems|Silent Sabotage: Internal State Triggered Backdoor Attacks on LLM-Powered Robotic Systems]]

![[assets/2609.26184_figure.png|800]]

- **arXiv**: [2609.26184](https://arxiv.org/abs/2609.26184)
- **PDF**: https://arxiv.org/pdf/2609.26184
- **详细分析**: [[20_Research/Papers/大模型/Silent_Sabotage_Internal_State_Triggered_Backdoor_Attacks_on_LLM-Powered_Robotic_Systems|Silent Sabotage: Internal State Triggered Backdoor Attacks on LLM-Powered Robotic Systems]]
- **作者**: Doniyorkhon Obidov, Shivayogi Akki, Tan Chen, Kaichen Yang
- **cs 子类**: cs.AI, cs.CR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，大模型 0.6，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Silent Sabotage: Internal State Triggered Backdoor Attacks on LLM-Powered Robotic Systems》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The integration of Large Language Models (LLMs) into robotic control systems is enabling a new generation of autonomous agents capable of complex reasoning and planning. While this paradigm shift accelerates progress, it also introduces novel security risks that remain largely unexplored. Current research into LLM backdoors has focused on attacks triggered by external stimuli, such as specific words, visual objects, or environmental states. These attacks, while potent, overlook a more insidious class of vulnerability where the trigger is internal to the agent's own operational logic. This paper presents the first comprehensive study of history-based backdoor attacks on LLM-powered robotic systems. We demonstrate that an attacker can embed a stealthy backdoor into an LLM-based robot controller by manipulating its instructions. This backdoor is triggered not by an external cue, but by a specific, rare sequence of the robot's own past actions. It remains dormant during normal operation, preserving the robot's utility, but can be activated to induce a malicious behavior, such as a complete stop or a collision. Our experiments, conducted in a simulated environment with a variety of robots and LLMs, show that this history-based attack is highly effective, achieving a near-perfect attack success rate while remaining exceptionally difficult to detect. These findings reveal a critical and previously unaddressed vulnerability in autonomous systems and underscore the urgent need for security measures that account for an agent's internal state.

</details>

---

### [[20_Research/Papers/大模型/The_Uncontrolled_Variable_Vision-Language_Model_Refusal_Responds_to_Image_Presence_in_Ways_Risk_Cannot_Explain|The Uncontrolled Variable: Vision-Language Model Refusal Responds to Image Presence in Ways Risk Cannot Explain]]

![[assets/2609.26174_figure.png|800]]

- **arXiv**: [2609.26174](https://arxiv.org/abs/2609.26174)
- **PDF**: https://arxiv.org/pdf/2609.26174
- **详细分析**: [[20_Research/Papers/大模型/The_Uncontrolled_Variable_Vision-Language_Model_Refusal_Responds_to_Image_Presence_in_Ways_Risk_Cannot_Explain|The Uncontrolled Variable: Vision-Language Model Refusal Responds to Image Presence in Ways Risk Cannot Explain]]
- **作者**: Haoyu Zhang, Yi Feng, Shibo Zheng, Zhuoxi Wang, Xiao Luo, Haowen Xu, Xiangchen Guan, Mohammad Zandsalimy, Shanu Sushmita
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《The Uncontrolled Variable: Vision-Language Model Refusal Responds to Image Presence in Ways Risk Cannot Explain》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：OR-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language Model (VLM) safety is expected to depend on what a request asks for. We show that safety-aligned VLMs also key refusal on a property of a request's form: whether an image is attached, holding everything the request asks fixed. Attaching a blank canvas - unreadable, unrelated to the request, identical across prompts - shifts refusal by tens of percentage points, with no defense in the loop. The shift is not blanket caution. Neutral instructions are almost unaffected while borderline-benign prompts move sharply, so the cost falls on sensitivity-adjacent traffic: benign questions about privacy, self-harm and violence. Attachment alone is sufficient, while the image's properties set the price: a black canvas costs substantially more than a white one of identical size, and on an open checkpoint the carrying axis is pixel count. Nor is the shift under instructional control - telling the model the image is a placeholder to be disregarded removes only a fraction of it, and on one model asserting that an attachment exists moves refusal substantially with nothing attached. Attachment may correlate with risk in deployment; what these models do with it does not track risk. It is not the serving stack, since the same weights reached two ways behave alike, nor a property of VLMs as such, since several open-weight checkpoints show nothing. It belongs to particular aligned checkpoints, one of them open. It is also decoupled from what it buys: the canvas does prevent some attack success on a matched harmful set, but far less than it costs, and its sign is not fixed - on one open model the identical canvas makes the model markedly easier to attack. Image presence is not a default a deployer chose or priced; it is an uncontrolled variable inherited with the weights.

</details>

---

### [[20_Research/Papers/强化学习/MGRL-RSCC_Multi-Granularity_Reward_Reinforcement_Learning_for_Fine-Grained_Remote_Sensing_Change_Captioning|MGRL-RSCC: Multi-Granularity Reward Reinforcement Learning for Fine-Grained Remote Sensing Change Captioning]]

![[assets/2609.26166_figure.jpg|800]]

- **arXiv**: [2609.26166](https://arxiv.org/abs/2609.26166)
- **PDF**: https://arxiv.org/pdf/2609.26166
- **详细分析**: [[20_Research/Papers/强化学习/MGRL-RSCC_Multi-Granularity_Reward_Reinforcement_Learning_for_Fine-Grained_Remote_Sensing_Change_Captioning|MGRL-RSCC: Multi-Granularity Reward Reinforcement Learning for Fine-Grained Remote Sensing Change Captioning]]
- **作者**: Futian Wang, Mengqi Wang, Xiao Wang, Wentao Wu, Haowen Wang, Zhicheng Zhao, Jin Tang
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《MGRL-RSCC: Multi-Granularity Reward Reinforcement Learning for Fine-Grained Remote Sensing Change Captioning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CapRL, ICT-Net, MGRL, PM3Net, PSNet, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Remote Sensing Change Captioning (RSCC), which aims to generate accurate and detailed linguistic descriptions of ground object variations from bi-temporal remote sensing images, is a critical and challenging task in intelligent remote sensing interpretation. The mainstream autoregressive training paradigm faces severe exposure bias and train-test distribution mismatch, resulting in cumulative generation errors. They tend to produce conservative and template-fixed captions while ignoring subtle scene change details. To address these challenges, this paper proposes a novel multi-granularity reward reinforcement learning paradigm, termed MGRL-RSCC. Specifically, we first leverage a CNN and hierarchical self-attention module to extract and enhance visual features from bi-temporal remote sensing images. A Transformer decoder is then utilized to complete visual-to-linguistic translation. Different from existing methods, we design a dual-decoding strategy and a two-stage joint optimization scheme, which combines token-level supervised learning via greedy decoding and multi-granularity reward-driven self-critical reinforcement learning via sampling decoding. We further construct three complementary reward functions covering linguistic fluency, change state consistency, and structural-semantic relevance to comprehensively optimize caption quality and alleviate false and missing change descriptions. Extensive experiments on multiple public RSCC benchmark datasets demonstrate that the proposed MGRL-RSCC effectively mitigates exposure bias and conservative generation problems in traditional autoregressive methods. The source code and pre-trained models will be released on this https URL

</details>

---

### [[20_Research/Papers/具身智能/StepTrigger_Contact-State-Triggered_Backdoor_Attacks_on_VLM-Powered_Legged_Robots|StepTrigger: Contact-State-Triggered Backdoor Attacks on VLM-Powered Legged Robots]]

![[assets/2609.26131_figure.png|800]]

- **arXiv**: [2609.26131](https://arxiv.org/abs/2609.26131)
- **PDF**: https://arxiv.org/pdf/2609.26131
- **详细分析**: [[20_Research/Papers/具身智能/StepTrigger_Contact-State-Triggered_Backdoor_Attacks_on_VLM-Powered_Legged_Robots|StepTrigger: Contact-State-Triggered Backdoor Attacks on VLM-Powered Legged Robots]]
- **作者**: Jiageng Zhang, Doniyorkhon Obidov, Kaichen Yang
- **cs 子类**: cs.AI, cs.CR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.2，大模型 0.7，机器人 0.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《StepTrigger: Contact-State-Triggered Backdoor Attacks on VLM-Powered Legged Robots》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models and vision-language models are increasingly used as high-level planners in robotic systems, using task goals and sensor summaries to select navigation or manipulation actions. This creates a new backdoor surface: a compromised planner can behave normally in most runs, yet change its target selection when a hidden trigger is present. Prior attacks on LLM-powered or embodied agents mainly rely on triggers that appear in language, camera-visible objects, scene semantics, or specific sequences of past actions. This paper presents StepTrigger, a contact-state-triggered backdoor attack for VLM-powered legged robots. The trigger is not a prompt token or a visible marker. It is produced by pressure and foot-ground contact patterns that arise when a Unitree Go1 quadruped walks across a dense terrain patch. Unlike conventional visual or textual triggers, contact signals are inherently noisy and may also arise during benign locomotion. To avoid treating every pressure anomaly as a trigger, StepTrigger learns a selective backdoor policy from multimodal robot state, using incidental pressure events as benign examples and dense-patch contacts as poisoned examples. In a stratified offline evaluation, the trained planner achieved 98.75% clean behavior preservation, 92.50% false-trigger rejection, 76.25% true-trigger activation, and 89.17% overall parsed behavior accuracy. These results reveal a backdoor surface in proprioceptive and contact channels that is not captured by defenses focused only on language, vision, or action history.

</details>

---

### [[20_Research/Papers/具身智能/Skytopia_Monocular_Drone_Navigation_with_Action-Conditioned_Latent_World_Models|Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models]]

![[assets/2609.26007_figure.png|800]]

- **arXiv**: [2609.26007](https://arxiv.org/abs/2609.26007)
- **PDF**: https://arxiv.org/pdf/2609.26007
- **详细分析**: [[20_Research/Papers/具身智能/Skytopia_Monocular_Drone_Navigation_with_Action-Conditioned_Latent_World_Models|Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models]]
- **作者**: Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，世界模型 1，机器人 1.1）
- **关联关键词**: EmbodiedAI, RL, WorldModel

#### 研究背景与动机

《Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models》归入 机器人、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monocular drone navigation requires reaching a goal in an unseen environment from a single forward-facing camera, which offers few cues for depth and scale. World models address this by modelling how observations evolve under actions, but they are built to be executed: the prediction is produced at deployment and fed back into action generation at every control step. We argue that what a policy needs from a world model is not the prediction but the representation required to produce it: in flight the executed action explains almost all of the change between observations, so prediction reduces to reprojecting a static scene under a known displacement. We therefore introduce skytopia, a policy built on an action-conditioned latent world model, and the 3D Gaussian Splatting platform on which it is trained. A forward objective predicts the representation of the next observation from the intended motion, and an inverse objective recovers that motion from the predicted transition. Because the prediction never reaches action generation, the predictor is discarded and one policy serves point-goal, image-goal, and goal-free navigation. Simulation experiments show that skytopia outperforms every baseline under all three specifications, attaining 57.8%, 66.0%, and 49.0% success rate, while discarding the predictor removes 59.4% of the inference cost. The same policy is subsequently deployed on a physical drone without fine-tuning and reaches goals in indoor, open outdoor, and woodland environments.

</details>

---

### [[20_Research/Papers/大模型/AgenticSizing_A_Large_Language_Model-based_Multi-Agent_Framework_for_Analog_Circuit_Sizing|AgenticSizing: A Large Language Model-based Multi-Agent Framework for Analog Circuit Sizing]]

![[assets/2609.25873_figure.png|800]]

- **arXiv**: [2609.25873](https://arxiv.org/abs/2609.25873)
- **PDF**: https://arxiv.org/pdf/2609.25873
- **详细分析**: [[20_Research/Papers/大模型/AgenticSizing_A_Large_Language_Model-based_Multi-Agent_Framework_for_Analog_Circuit_Sizing|AgenticSizing: A Large Language Model-based Multi-Agent Framework for Analog Circuit Sizing]]
- **作者**: Yijia Hao, Pratibha Verma, Dongxu Guo, Cristian Sestito, Michael O'Boyle, Christos-Savvas Bouganis, Themis Prodromakis
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.4（加权：大模型 1.4）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AgenticSizing: A Large Language Model-based Multi-Agent Framework for Analog Circuit Sizing》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Analog circuit sizing remains a challenging and time-consuming task due to the large design space, strong performance trade-offs, and increasing circuit complexity in scaled technologies. Although recent large language model (LLM)-based methods show promise in improving sample efficiency and interpretability, existing approaches often lack explicit circuit-topology understanding and are mainly evaluated on relatively simple analog building blocks. This paper presents a multi-agent LLM-based framework for complex analog circuit sizing. The proposed framework first analyzes the circuit topology and decomposes the netlist into functional blocks and substructures. It also extracts lightweight design knowledge for reuse. Based on the extracted topology and knowledge, a planner coordinates multiple role-specialized sizing agents to update design variables and achieve global performance specifications. This workflow mimics the collaborative process of an expert analog design team and provides a structured, interpretable, and simulation-driven optimization procedure. The framework was validated on eight circuits, with the largest design containing up to 55 transistors and 60 sizing variables. Notably, for the LDO benchmark, the proposed method achieved a 60\% success rate with an average of 83 iterations, where classical optimizers failed to find feasible solutions. Further, ablation studies demonstrate that topology understanding, design-knowledge infusion, and agent specialization provide complementary benefits. The source code is available to support reproducibility.

</details>

---

### [[20_Research/Papers/大模型/LingLan_An_Advancing_Traditional_Chinese_Medicine_Diagnosis_LLM_with_Multimodal_Data|LingLan: An Advancing Traditional Chinese Medicine Diagnosis LLM with Multimodal Data]]

![[assets/2609.25715_figure.png|800]]

- **arXiv**: [2609.25715](https://arxiv.org/abs/2609.25715)
- **PDF**: https://arxiv.org/pdf/2609.25715
- **详细分析**: [[20_Research/Papers/大模型/LingLan_An_Advancing_Traditional_Chinese_Medicine_Diagnosis_LLM_with_Multimodal_Data|LingLan: An Advancing Traditional Chinese Medicine Diagnosis LLM with Multimodal Data]]
- **作者**: Zheng Chen, Zhicheng Du, Haoxuan Li, Yingshan Liang, Peiwu Qin
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《LingLan: An Advancing Traditional Chinese Medicine Diagnosis LLM with Multimodal Data》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Though artificial intelligence (AI) increasingly transforms modern medicine, its integration into Traditional Chinese Medicine (TCM) has been relatively slow, primarily due to TCM's reliance on holistic, subjective diagnostic methods---namely Inspection, Auscultation and Olfaction, Inquiry, and Palpation(I-AOI-P)---which are difficult to align with quantitative, standardized medical systems. In this work, we introduce a Unification Framework for Multimodal Data (UFMD), which automatically processes tongue and pulse images into structured, clinically standard descriptions, integrating multi-source diagnostic information into a unified digital record of I-AOI-P process. Building on this structured data, we create LingLan-14B, a TCM-specific large language model fine-tuned via supervised learning to emulate the diagnostic logic and workflow of I-AOI-P process. Experimental results show that our method significantly enhances diagnostic accuracy, achieving a relative improvement of 103.5% over the baseline (62.72% vs. 30.82%) and reaching an F1-score of up to 82%.

</details>

---

### [[20_Research/Papers/大模型/How_Strongly_Should_Task_State_Influence_an_LLM_Agent|How Strongly Should Task State Influence an LLM Agent?]]

![[assets/2609.25686_first_page.png|800]]

- **arXiv**: [2609.25686](https://arxiv.org/abs/2609.25686)
- **PDF**: https://arxiv.org/pdf/2609.25686
- **详细分析**: [[20_Research/Papers/大模型/How_Strongly_Should_Task_State_Influence_an_LLM_Agent|How Strongly Should Task State Influence an LLM Agent?]]
- **作者**: Chenyu Zhang, Wonbin Kweon, Jiawei Han
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《How Strongly Should Task State Influence an LLM Agent?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PM-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon assigned work requires an LLM agent to track the state of a task: which steps are done, blocked, cancelled, or open to repetition. Agent systems either keep this state as text in the prompt and rely on the model to read that text, or move the state into a module that enforces it, and each system is evaluated as a whole, so no one knows how much reliability comes from the state being shown, told, or enforced. We fix the task rules, the model, and paired episodes and vary how strongly task state reaches the agent: a raw transcript, an exact checklist, per-turn directives from a state machine compiled from the brief and advanced only by execution receipts, or an enforcement gate on that machine that refuses state-violating actions; every episode is scored by exact payload matching against dynamic ground truth. Across three models, two reasoning regimes, and two domains, four findings hold without per-turn reasoning: displaying accurate state is unreliable, an unverified ledger the agent writes itself beats an accurate checklist it is shown, directives help in proportion to the model's obedience, and enforcement needs no obedience but is bounded by the correctness of its state and by the matcher that maps requests to steps; per-turn reasoning at a 235B agent compresses these separations without repairing the text rungs. The same gate, compiled from $\tau^2$-bench's airline policy, raises a 235B agent's pass$^1$ from 0.39 to 0.54 and changes nothing for a 35B agent that rarely violates the policy; on PM-Bench, where acting turns on recognizing a cue rather than on state, showing the record is the best rung--matching or beating both gates and reversing the ledger-over-checklist finding--and enforcing the matcher's judgement drops a 35B agent below its raw transcript. Enforcement pays when failures are state-decidable and frequent, and hurts when the gate's judgement is wrong.

</details>

---

### [[20_Research/Papers/强化学习/Teaching_Reinforcement_Learning_and_Humanoid_Robotics_to_High-School_Students_An_Expert-Validated_Curriculum_Design_on_a_Low-Cost_Open_Platf|Teaching Reinforcement Learning and Humanoid Robotics to High-School Students: An Expert-Validated Curriculum Design on a Low-Cost Open Platform]]

![[assets/2609.25674_figure.png|800]]

- **arXiv**: [2609.25674](https://arxiv.org/abs/2609.25674)
- **PDF**: https://arxiv.org/pdf/2609.25674
- **详细分析**: [[20_Research/Papers/强化学习/Teaching_Reinforcement_Learning_and_Humanoid_Robotics_to_High-School_Students_An_Expert-Validated_Curriculum_Design_on_a_Low-Cost_Open_Platf|Teaching Reinforcement Learning and Humanoid Robotics to High-School Students: An Expert-Validated Curriculum Design on a Low-Cost Open Platform]]
- **作者**: Yuanzhe Dong, Jie Cao, Shuman Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 4.6（加权：具身智能 1.5，强化学习 0.8，机器人 2.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Teaching Reinforcement Learning and Humanoid Robotics to High-School Students: An Expert-Validated Curriculum Design on a Low-Cost Open Platform》归入 机器人、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Lower cost open source robots and reinforcement learning (RL) simulation tools create new opportunities for precollege students to engage with contemporary robotics. However, translating a complete research workflow, spanning mechanical assembly, electrical setup, simulation, policy learning, system identification, and physical deployment, into a coherent course for novice learners remains challenging. We present an integrated robotics course framework that organizes these activities around a shared robotic artifact. The framework combines parallel disciplinary tracks, sequencing based on technical dependencies, progressive integration of simulation and hardware, layered performance checkpoints, and structures for balancing collaborative work with individual accountability. We illustrate the framework through a high school curriculum organized around a robot project in which pairs of students assemble an open source humanoid robot, train a walking policy in simulation, and deploy it on the physical platform. The framework was developed through an iterative design process that included formative review by five experts in robotics research, engineering, secondary STEM education, and curriculum design. Expert feedback highlighted three central design tensions: authenticity versus cognitive load, system integration versus timely visible progress, and team construction versus individual accountability. These tensions informed the final framework presented in this paper. This work offers a structured approach for adapting robotics research workflows into interdisciplinary precollege courses; future classroom studies are needed to examine implementation and student learning.

</details>

---

### [[20_Research/Papers/大模型/ChatT2_An_Adaptive_Framework_for_Developing_a_Large_Language_Model-Based_Agent_for_Natural_Product_Domain_Research|ChatT2: An Adaptive Framework for Developing a Large Language Model-Based Agent for Natural Product Domain Research]]

![[assets/2609.25620_figure.png|800]]

- **arXiv**: [2609.25620](https://arxiv.org/abs/2609.25620)
- **PDF**: https://arxiv.org/pdf/2609.25620
- **详细分析**: [[20_Research/Papers/大模型/ChatT2_An_Adaptive_Framework_for_Developing_a_Large_Language_Model-Based_Agent_for_Natural_Product_Domain_Research|ChatT2: An Adaptive Framework for Developing a Large Language Model-Based Agent for Natural Product Domain Research]]
- **作者**: Yihan Wang, Qiandi Gao, Yihui Zhuang, Liangjun Ge, Heqian Zhang, Jiaquan Huang, Zhiwei Qin
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.6（加权：大模型 1.6）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《ChatT2: An Adaptive Framework for Developing a Large Language Model-Based Agent for Natural Product Domain Research》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scientific investigations into microbial natural products (NPs) present significant challenges for novices, largely due to the complexity of microbial systems, biochemical diversity, technical skill requirements, and the demands of bioinformatics and data analysis processes. To address these issues, we introduce ChatT2, a large language model (LLM)-based agent that is specifically tailored to the unique characteristics of bacterial type II polyketides. These polyketides form a structurally distinct and therapeutically important NP family. ChatT2 was developed within an autonomous multiagent framework composed of a mentor, an executor, and an evaluator, each with defined responsibilities. The mentor acts as an intermediary between ChatT2 and the user, utilizing chain-of-thought prompting to refine the intent of the user. Under the guidance of the mentor, the executor synthesizes multimodal information via retrieval-augmented generation techniques and seamlessly integrates bioinformatics and cheminformatics tools. The evaluator ultimately assesses the output of the executor to ensure the richness and accuracy of the retrieved information. Our research highlights how ChatT2, designed with this multiagent framework, addresses the challenges faced by general LLMs in terms of understanding limited, specialized corpora and complex biological information and provides both experts and novices with a valuable tool for exploring various NPs of interest. The ChatT2 webserver can be accessed at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/IndustrialVLA-Bench_A_Traceable_Multi-Axis_Evaluation_of_Open_Robot_Policy_Models|IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models]]

![[assets/2609.25562_figure.png|800]]

- **arXiv**: [2609.25562](https://arxiv.org/abs/2609.25562)
- **PDF**: https://arxiv.org/pdf/2609.25562
- **详细分析**: [[20_Research/Papers/具身智能/IndustrialVLA-Bench_A_Traceable_Multi-Axis_Evaluation_of_Open_Robot_Policy_Models|IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models]]
- **作者**: Yiqi Wang, Zhifeng Rao, Jiaqi Zhang, Xiaoyang Li, Zhangkai Wu, Yiqun Duan, Mingkai Zheng, Fei Wang, Shan You, Taotao Cai
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：IndustrialVLA-Bench, MultiNet, OpenVLA, URL, UnifoLM-VLA, VLA-Eval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open robot policies increasingly follow two paradigms: vision-language-action models (VLAs) directly map observations and instructions to actions, whereas world-action models (WAMs) incorporate learned video or world dynamics into policy learning or action generation. Although both target the same manipulation tasks and represent alternative design choices, they are commonly reported under different evaluation protocols, leaving their capability, robustness, language sensitivity, and deployment-cost trade-offs unclear. We present IndustrialVLA-Bench, an evidence-aware evaluation of six released VLA and WAM systems under a unified reporting schema. It separately evaluates clean capability on LIBERO, non-language robustness on LIBERO-Plus, instruction sensitivity on LIBERO-Para, and observed execution cost. Reported task scores aggregate three complete evaluations with distinct random seeds under a fixed checkpoint and inference configuration. Across all six systems, clean LIBERO averages differ by only 1.58 points, whereas robustness and paraphrase summaries span 14.62 and 31.08 points. Restricting every comparison to the three protocol-faithful systems preserves the effect (1.36, 14.62 and 23.10 points), so the diagnostic separation reported here does not depend on the weaker evidence tiers. We additionally report observed inference latency, peak memory, runtime mode, and an evidence status for every system. Protocol-faithful, near-reproduction, and pending-verification entries remain visibly separated; only protocol-faithful entries support strict comparisons. Rather than claiming universal superiority of either paradigm, IndustrialVLA-Bench provides traceable evidence for comparing released robot policies on shared practical criteria. Code and evaluation records are available at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_on_Item-Compatibility_Graphs_for_One-Dimensional_Bin_Packing|Deep Reinforcement Learning on Item-Compatibility Graphs for One-Dimensional Bin Packing]]

![[assets/2609.25397_first_page.png|800]]

- **arXiv**: [2609.25397](https://arxiv.org/abs/2609.25397)
- **PDF**: https://arxiv.org/pdf/2609.25397
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_on_Item-Compatibility_Graphs_for_One-Dimensional_Bin_Packing|Deep Reinforcement Learning on Item-Compatibility Graphs for One-Dimensional Bin Packing]]
- **作者**: M. Aslı Aydın
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 2.12（加权：强化学习 1.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision, Systems

#### 研究背景与动机

《Deep Reinforcement Learning on Item-Compatibility Graphs for One-Dimensional Bin Packing》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The one-dimensional bin packing problem (1D-BPP) is a classical NP-hard combinatorial optimization problem with applications ranging from logistics and manufacturing to cloud resource management. Although deep reinforcement learning (DRL) has become a competitive paradigm for data-driven optimization, most learned packing methods target 2D and 3D variants, and intelligent learned solvers for 1D-BPP remain scarce. In this paper, we present a novel end-to-end, size-agnostic graph reinforcement learning framework for 1D-BPP. We formulate the packing process as a Markov decision process on an item-compatibility graph, serving as a structural knowledge representation in which every action merges two partial bins that fit together. A graph neural network actor-critic policy extracts relational features from this representation and is trained through reinforcement learning and decoded by stochastic beam search, enabling a single trained model to generalize zero-shot to instances of any size. We conduct a systematic empirical study across graph encoders, DRL algorithms, reward functions, training distributions, and hyperparameters. Evaluated zero-shot on the full BPPLIB benchmark against a constructive heuristic, a grouping genetic algorithm, and recent learned methods, our data-driven policy lowers the mean optimality gap of the constructive heuristic from 2.66\% to 2.31\%, with the largest gains on structured instances. Against learned baselines evaluated on the same benchmark, it attains a lower gap on most of the nine families and is far more stable across instance distributions. On the hardest benchmark family, it outperforms a state-of-the-art learned solver that relies on column generation and integer programming, while using no solver at all. A grouping genetic algorithm remains ahead overall, and we analyze where and why the residual gap arises.

</details>

---

### [[20_Research/Papers/大模型/Passes_Alone,_Fails_Together_Benchmarking_Semantic_Coordination_in_Parallel_LLM-Agent_Development|Passes Alone, Fails Together: Benchmarking Semantic Coordination in Parallel LLM-Agent Development]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2609.25396](https://arxiv.org/abs/2609.25396)
- **PDF**: https://arxiv.org/pdf/2609.25396
- **详细分析**: [[20_Research/Papers/大模型/Passes_Alone,_Fails_Together_Benchmarking_Semantic_Coordination_in_Parallel_LLM-Agent_Development|Passes Alone, Fails Together: Benchmarking Semantic Coordination in Parallel LLM-Agent Development]]
- **作者**: Haocheng Xia, Eugene Wu, Yongjoo Park
- **cs 子类**: cs.AI, cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Passes Alone, Fails Together: Benchmarking Semantic Coordination in Parallel LLM-Agent Development》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Parallel coding agents can produce patches that work alone but fail when merged. This happens when one agent changes an interface or rule that another agent still relies on. We study these failures with stale, a benchmark for semantic coordination. Our evaluation runs the same tests on each patch alone and on their combination, counting only failures introduced by combining the patches. We use three tiers: synthetic tasks with controlled interface changes, pairs of merged pull requests, and constructed tasks that use real Django helpers. Among 834 runs on 417 mined Django pairs, only one showed interference after correcting the grading procedure. On constructed tasks using 12 Django helpers, interference occurred in 97% of runs. A message describing the completed concurrent change recovered 82% of runs. Reviewed pull requests may contain few unresolved parallel changes, even when agents fail on controlled tasks using real code. The constructed failure rates do not estimate how often these problems occur in practice.

</details>

---

### [[20_Research/Papers/具身智能/VLAQuantBench_Closed-Loop_Evaluation_of_Post-Training_Quantization_for_Vision-Language-Action_Models|VLAQuantBench: Closed-Loop Evaluation of Post-Training Quantization for Vision-Language-Action Models]]

![[assets/2609.25376_figure.png|800]]

- **arXiv**: [2609.25376](https://arxiv.org/abs/2609.25376)
- **PDF**: https://arxiv.org/pdf/2609.25376
- **详细分析**: [[20_Research/Papers/具身智能/VLAQuantBench_Closed-Loop_Evaluation_of_Post-Training_Quantization_for_Vision-Language-Action_Models|VLAQuantBench: Closed-Loop Evaluation of Post-Training Quantization for Vision-Language-Action Models]]
- **作者**: Jiuyi Xu, Qing Jin, Meida Chen, Song Wang, Yang Sui, Yangming Shi
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《VLAQuantBench: Closed-Loop Evaluation of Post-Training Quantization for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BitVLA, DyQ-VLA, HBVLA, OpenVLA, QVLA, QuantVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Post-training quantization reduces the memory requirements of vision-language-action (VLA) models, but precision selection must account for the interaction between layer scope, numerical format, and calibration. We introduce \textbf{VLAQuantBench}, a controlled evaluation with 409 runs and 94,574 simulation episodes: four models on LIBERO, with X-VLA additionally evaluated on three simulation benchmark families. Under uncalibrated W4A4 round-to-nearest quantization, expanding a $\pi_{0.5}$ action-head subset from 126 to 167 layers raises success from 7.0\% to 70.5\%. Fixed-observation replay confirms a corresponding numerical recovery. Two-episode calibration removes the severe joint failures in the tested subsets, whereas the same smoothing-and-clipping recipe lowers $\pi_0$ success and does not recover OpenVLA-OFT end-to-end. For OpenVLA-OFT, protecting one 28,672-parameter output projection instead restores near-baseline success: the remaining 441 eligible linear layers retain W3 on LIBERO-Long or eight-bit activations across all four suites. Task-clustered intervals support the large failure and recovery contrasts. These results establish recipe-dependent interactions and identify concrete precision assignments, rather than universal layer-sensitivity rules. Real-kernel and physical-robot measurements complement the accuracy analysis. Code, configurations, and episode records are publicly available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/Trains_but_Doesn't_Learn_A_Post-Training_Delivery_Benchmark_for_LLM_Agents_as_Forward-Deployed_Engineers|Trains but Doesn't Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers]]

![[assets/2609.25237_first_page.png|800]]

- **arXiv**: [2609.25237](https://arxiv.org/abs/2609.25237)
- **PDF**: https://arxiv.org/pdf/2609.25237
- **详细分析**: [[20_Research/Papers/大模型/Trains_but_Doesn't_Learn_A_Post-Training_Delivery_Benchmark_for_LLM_Agents_as_Forward-Deployed_Engineers|Trains but Doesn't Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers]]
- **作者**: Weihang Ding, Junfei Zhan
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Trains but Doesn't Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FinQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Post-training is becoming a service (PTaaS): a customer hands an operator data and a goal, and a forward-deployed engineer (FDE) returns a fine-tuned, evaluated, and deployed model under a budget, a human-approval gate, and reproducibility requirements. Seating an LLM agent in the FDE seat raises a question existing benchmarks cannot answer: not whether an agent can raise a metric, but whether it can be trusted to deliver. We answer it on a governed delivery plane, where an agent drives ten stages and an oracle scores each stage from platform-recorded facts. The central silent failure is the run that trains but does not learn (TBDL): loss falls, every signal stays green, and the delivered model is no better than the base. An operator-run acceptance gate catches every such run before payment, and a detector calibrated on known-corrupted runs flags severe corruption mid-run. We ran four frontier agents (Claude Opus 5, GPT-5.6-luna, Gemini 3.7 Flash, DeepSeek V4-Pro) end to end on metered L40S, A100, and H200 GPUs across 8B to 70B open bases, certifying every scenario before scoring. We also ran a human FDE arm under the same oracle and compare every agent against it.

</details>

---

### [[20_Research/Papers/具身智能/X-Planner_Event-Structured_Task_Planning_for_Embodied_Intelligence|X-Planner: Event-Structured Task Planning for Embodied Intelligence]]

![[assets/2609.25187_figure.png|800]]

- **arXiv**: [2609.25187](https://arxiv.org/abs/2609.25187)
- **PDF**: https://arxiv.org/pdf/2609.25187
- **详细分析**: [[20_Research/Papers/具身智能/X-Planner_Event-Structured_Task_Planning_for_Embodied_Intelligence|X-Planner: Event-Structured Task Planning for Embodied Intelligence]]
- **作者**: Howard Lu, Shalfun Li, Porter Pan, Cris, Lumen, Cyril, Eric Hu, Lily Li, Maeve Zhang, Robert Wang, KZ Zheng, Viggo Chen...
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.8，大模型 0.1，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《X-Planner: Event-Structured Task Planning for Embodied Intelligence》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CoT-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task planning bridges high-level instructions and executable behavior in long-horizon manipulation, yet modern Vision-Language-Action (VLA) systems often leave this intermediate structure implicit. Existing chain-of-thought (CoT) planners also tend to rely on coarse task-level annotations or serialize long reasoning traces token by token. We present X-Planner, a planning front-end that addresses both the supervision and representation of embodied reasoning. Our planning data combine Ego, UMI, and teleoperation under a hierarchy granularity with source-dependent annotation depth. Takeover-time annotations and human-designed failures supervise ongoing error recognition. On the model side, a shared VLM backbone exposes two event-structured plan forms: a discrete interface that emits interpretable event states and a latent interface that relays continuous CoT states across staggered Transformer depths through Staircase Decoding. A frozen latent-to-text reconstruction objective provides a semantic anchor for the latent representation. Offline two-step planning evaluation places X-Planner second among four evaluated models on both BERTScore-F1 and a judge-based Overall score. In real-robot experiments, respectively, outperforming the evaluated baselines. These results characterize planning-text quality and downstream execution.

</details>

---

### [[20_Research/Papers/大模型/Do_Synthetic_Personas_Predict_Real_Audience_Response_A_Sim-to-Real_Study_Where_a_No-Persona_Baseline_Beats_Persona-Based_Copy_Simulation|Do Synthetic Personas Predict Real Audience Response? A Sim-to-Real Study Where a No-Persona Baseline Beats Persona-Based Copy Simulation]]

![[assets/2609.25010_figure.png|800]]

- **arXiv**: [2609.25010](https://arxiv.org/abs/2609.25010)
- **PDF**: https://arxiv.org/pdf/2609.25010
- **详细分析**: [[20_Research/Papers/大模型/Do_Synthetic_Personas_Predict_Real_Audience_Response_A_Sim-to-Real_Study_Where_a_No-Persona_Baseline_Beats_Persona-Based_Copy_Simulation|Do Synthetic Personas Predict Real Audience Response? A Sim-to-Real Study Where a No-Persona Baseline Beats Persona-Based Copy Simulation]]
- **作者**: Alexandre Cristovão Maiorano
- **cs 子类**: cs.AI, cs.CL, cs.CY
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.45（加权：具身智能 1.2，大模型 0.25）
- **关联关键词**: LLM

#### 研究背景与动机

《Do Synthetic Personas Predict Real Audience Response? A Sim-to-Real Study Where a No-Persona Baseline Beats Persona-Based Copy Simulation》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Marketers increasingly use large language models (LLMs) as "synthetic personas" to predict how an audience will react to a piece of copy before it ships, encouraged by evidence that profile-conditioned LLMs mimic human samples. But is that prediction actually valid against real behaviour - and does the persona machinery help? We present a sim-to-real validity study using the Upworthy Research Archive - thousands of headline A/B tests on shared real traffic, with measured click-through - as held-out ground truth. We compare a ten-persona panel, grounded in the real audience's demographics, against a no-persona zero-shot baseline that simply asks the model how likely a typical reader is to click. Two findings stand out. First, ground-truth reliability is the binding constraint: most A/B tests have no statistically distinguishable winner, so validity can only be measured on the reliable subset (n = 399). Second, and counter to the persona-simulation premise, persona conditioning degrades predictive validity: the no-persona baseline ranks variants markedly better (Kendall {\tau} = 0.361, a medium effect; top-1 accuracy 49.2%) than the persona panel ({\tau} = 0.084; top-1 34.6%), with non-overlapping confidence intervals. Asking the model directly taps an accurate population-level prior; forcing it to role-play specific personas injects bias and noise. The result replicates across three independent Upworthy splits, holds in direction on a different-domain news dataset, and is robust to seed, prompt phrasing, and model choice - across three Gemini tiers and a different model family (OpenAI gpt-4.1, significant paired gap). The takeaway: for predicting aggregate engagement, a plain LLM ranker beats persona simulation - synthetic personas are not merely a weak predictor, they are worse than not using them. All numbers regenerate from a public, artifact-first replication package.

</details>

---
