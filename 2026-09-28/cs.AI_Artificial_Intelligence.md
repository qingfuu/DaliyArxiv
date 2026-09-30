# cs.AI | Artificial Intelligence | 2026-09-28

#arxiv #ComputerScience

**论文数**: 24

### [[20_Research/Papers/大模型/PriceBench_A_Diagnostic_Benchmark_for_Price,_Quality,_and_Brand_Preferences_in_LLM_Booking_Agents|PriceBench: A Diagnostic Benchmark for Price, Quality, and Brand Preferences in LLM Booking Agents]]

![[assets/2609.31468_figure.png|800]]

- **arXiv**: [2609.31468](https://arxiv.org/abs/2609.31468)
- **PDF**: https://arxiv.org/pdf/2609.31468
- **详细分析**: [[20_Research/Papers/大模型/PriceBench_A_Diagnostic_Benchmark_for_Price,_Quality,_and_Brand_Preferences_in_LLM_Booking_Agents|PriceBench: A Diagnostic Benchmark for Price, Quality, and Brand Preferences in LLM Booking Agents]]
- **作者**: Pavel Kireyev
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《PriceBench: A Diagnostic Benchmark for Price, Quality, and Brand Preferences in LLM Booking Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ECom-Bench, PriceBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLMs increasingly act as purchasing agents, which makes the LLM, not the user, the one choosing among the options that satisfy a request; its preferences quietly fix what gets bought and what it costs. Hotel booking is a clean instance: a high-volume choice settled on a few comparable attributes, where the pick reveals those preferences. We introduce PriceBench, a diagnostic benchmark that recovers an LLM's price, quality, and brand preferences from its booking choices with a logit choice model, applied to 28 LLMs from 8 providers on 3,600 hotel tasks from 179 real New York City properties. We find that capability is associated with how consistently an LLM chooses, not with what it chooses: more capable LLMs hold stronger, more consistent preferences, while weaker ones either lock onto one position, exploitable by whoever controls listing order, or choose almost indifferently. What those preferences favor varies sharply across providers and even within one family: price sensitivity spans more than an order of magnitude, and the price/quality trade-off moves mean booked nightly price from \$247 to \$393 on identical tasks. What an agent buys must therefore be measured per LLM, not inferred, and we release the tasks, code, and all 28 response sets.

</details>

---

### [[20_Research/Papers/大模型/From_Reward_Signal_to_Visual_Utility_A_Controlled_Audit_of_Medical_VLM_Post-Training|From Reward Signal to Visual Utility: A Controlled Audit of Medical VLM Post-Training]]

![[assets/2609.31450_figure.png|800]]

- **arXiv**: [2609.31450](https://arxiv.org/abs/2609.31450)
- **PDF**: https://arxiv.org/pdf/2609.31450
- **详细分析**: [[20_Research/Papers/大模型/From_Reward_Signal_to_Visual_Utility_A_Controlled_Audit_of_Medical_VLM_Post-Training|From Reward Signal to Visual Utility: A Controlled Audit of Medical VLM Post-Training]]
- **作者**: Wang Jingxin
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.9（加权：大模型 0.7，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《From Reward Signal to Visual Utility: A Controlled Audit of Medical VLM Post-Training》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PMC-VQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Medical vision-language model (VLM) post-training is commonly evaluated through answer accuracy. We examine how changes in accuracy and training objectives relate to image-conditioned decisions in a controlled Qwen2.5-VL-3B study on PMC-VQA. We compare supervised fine-tuning (SFT) with low-rank adaptation (LoRA) restricted to the language model, expanded multimodal adaptation scopes, standard answer-only Group Relative Policy Optimization (GRPO), and a counterfactual evidence objective. On 2,000 clean-test questions, language model LoRA SFT changes correct-image accuracy by +1.10 percentage points (95% paired bootstrap CI:-0.85 to +3.05), while visual-benefit events decrease by 2.40 points and image sensitivity decreases by 5.60 points. Paired records reveal 155 acquired and 203 lost visual-benefit events. Broader adaptation yields lower correct-image accuracy than language-model LoRA SFT. Standard GRPO produces mixed-reward groups and parameter updates, with an uncertain clean test accuracy change. A generation audit reveals that canonical option scores can follow a different token path from generated answers. With scores taken along the greedy generation path, the evidence target improves on the training set; its gains over standard GRPO remain inconsistent on validation data at matched training doses. Sample-level analyses trace how evidence scores, decision margins, and generated answers change during post-training. This empirical and measurement audit identifies gaps between optimization activity, target acquisition, and useful held-out visual behavior.

</details>

---

### [[20_Research/Papers/机器人/Sorry_Robot,_Happy_Human_Vision-Language_Models_Read_Only_One_of_Two_Legible_Typographic_Layers|Sorry Robot, Happy Human: Vision-Language Models Read Only One of Two Legible Typographic Layers]]

![[assets/2609.31403_figure.png|800]]

- **arXiv**: [2609.31403](https://arxiv.org/abs/2609.31403)
- **PDF**: https://arxiv.org/pdf/2609.31403
- **详细分析**: [[20_Research/Papers/机器人/Sorry_Robot,_Happy_Human_Vision-Language_Models_Read_Only_One_of_Two_Legible_Typographic_Layers|Sorry Robot, Happy Human: Vision-Language Models Read Only One of Two Legible Typographic Layers]]
- **作者**: Mert İncidelen, Yamen Kashkash, Asya Berker, Murat Aydoğan
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 0.85（加权：大模型 0.25，机器人 0.6）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Sorry Robot, Happy Human: Vision-Language Models Read Only One of Two Legible Typographic Layers》归入 机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DecoyBench, ImageNet, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs), despite their success in optical character recognition (OCR) tasks, are vulnerable to typographic attacks and have a fragile structure for images with multiple text layers. In this study, the DecoyBench dataset was created using the Decoy Font method. The dataset consists of 300 images, each containing text with sharp contour lines superimposed on another text with soft shading. Six recent closed-source models from three different model families were evaluated using this dataset under two different prompting conditions (naive and guided) and at two different resolutions ($512\times512$ and $64\times64$). A validation study showed that human participants could read both text layers with high accuracy. In contrast, the models, with most variants and both prompting methods, read the contour text with near-human accuracy at high resolution, but almost never fully extracted the shading text. At low resolution, the contour text could not be read by either the models or humans, while the shading text could be extracted with high accuracy. The findings indicate that the evaluated VLMs exhibit a consistent behavioral limitation when processing typographic structures containing multiple spatial frequency layers.

</details>

---

### [[20_Research/Papers/具身智能/DyMD_Preserving_Interaction_Dynamics_through_Distribution_Matching_Distillation_in_Few-Step_Video_World_Models|DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation in Few-Step Video World Models]]

![[assets/2609.31349_figure.png|800]]

- **arXiv**: [2609.31349](https://arxiv.org/abs/2609.31349)
- **PDF**: https://arxiv.org/pdf/2609.31349
- **详细分析**: [[20_Research/Papers/具身智能/DyMD_Preserving_Interaction_Dynamics_through_Distribution_Matching_Distillation_in_Few-Step_Video_World_Models|DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation in Few-Step Video World Models]]
- **作者**: Haojun Xu, Jie Huang, Xin Lu, Mingchen Zhong, Zihao Fan, Linjiang Huang, Si Liu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.3，世界模型 0.6，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation in Few-Step Video World Models》归入 世界模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ABot-PhysWorld, EZS-Bench, PAI-Bench, R-Bench, Training-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large video diffusion models offer expressive priors for embodied prediction and learning, yet their many-step sampling remains costly for interactive downstream use. Distribution Matching Distillation (DMD) enables few-step video generation, but can suppress robot--object motion while preserving visual quality. Examining DMD's teacher and fake-score signals, we find that weak re-noising keeps the teacher posterior concentrated near motion-deficient rollouts, limiting motion-restoring guidance. Meanwhile, stronger-motion rollouts tend to incur larger fake-score fitting errors, which can hinder the generator's learning of interaction dynamics. We propose DyMD, a DMD framework that adapts both teacher supervision and critic fitting to the evolving student. Temporal affinity--conditioned re-noise sampling adapts the timestep distribution to each rollout's current interaction fidelity by mixing the base schedule with a teacher prior motivated by local posterior variation, thereby balancing motion recovery and appearance refinement. To better track stronger-motion rollouts, dynamics-guided fake-score tracking uses a noise-conditioned predictor to estimate noise-relative fitting difficulty from latent temporal dynamics, then upweights predicted-hard rollouts in the critic loss. Using DyMD, we distill a 14B teacher into a four-step 1.3B student with no auxiliary modules at inference. On embodied-video benchmarks, the student improves R-Bench task adherence by $9.6$ percentage points and PAI-Bench-G Domain score by $5.1$ points over Base DMD while maintaining comparable visual quality. As a backbone for downstream action planning, our student achieves 34% mean success across two WorldArena tasks, compared with 16% for Base DMD.

</details>

---

### [[20_Research/Papers/具身智能/Towards_VLA-Dreamer_Refining_VLA_Behavior_Using_World_Models|Towards VLA-Dreamer: Refining VLA Behavior Using World Models]]

![[assets/2609.31313_figure.png|800]]

- **arXiv**: [2609.31313](https://arxiv.org/abs/2609.31313)
- **PDF**: https://arxiv.org/pdf/2609.31313
- **详细分析**: [[20_Research/Papers/具身智能/Towards_VLA-Dreamer_Refining_VLA_Behavior_Using_World_Models|Towards VLA-Dreamer: Refining VLA Behavior Using World Models]]
- **作者**: Parsa Mastouri Kashani, Jan-Gerrit Habekost, Stefan Wermter
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 3.7（加权：具身智能 1.8，世界模型 1.4，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Towards VLA-Dreamer: Refining VLA Behavior Using World Models》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CoRL, OpenVLA, SmolVLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action models (VLAs), while showing strong potential for robot control, require massive amounts of high-quality imitation learning data. Moreover, the absence of an explicit world model casts further doubt on their control capabilities. In this concept paper, we propose a novel architecture that addresses sample efficiency in VLAs by training a predictive world model on the embedding space of the VLA's vision encoder. We hypothesize that these embeddings are action-relevant and usable for future prediction. To this end, we propose using the suggested architecture to investigate how well these embeddings predict the future based on actions, as the inability to do so would mark a key limitation of VLA architectures: the lack of a non-lossy implicit world model to simulate real-world dynamics. The proposed architecture differs from the standard world model dynamics as the loss comes from the embedding space rather than the pixel space, similar to joint embedding predictive architectures. Furthermore, the trained world model can be utilized for short-term planning tasks by sampling VLA actions given goal images. We intend to examine the richness of vision embeddings in VLAs and reduce their high data requirements through a world model that can also generate plans during inference.

</details>

---

### [[20_Research/Papers/强化学习/MA-WAM_Multi-Agent_World-Action_Model_for_Test-Time_Planning|MA-WAM: Multi-Agent World-Action Model for Test-Time Planning]]

![[assets/2609.31281_figure.png|800]]

- **arXiv**: [2609.31281](https://arxiv.org/abs/2609.31281)
- **PDF**: https://arxiv.org/pdf/2609.31281
- **详细分析**: [[20_Research/Papers/强化学习/MA-WAM_Multi-Agent_World-Action_Model_for_Test-Time_Planning|MA-WAM: Multi-Agent World-Action Model for Test-Time Planning]]
- **作者**: Guowei Zou, Haitao Wang, Guoxin Wang, Beiwen Zhang, Zhiquan Chen, Guojie Wang, Hejun Wu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.9（加权：大模型 0.5，强化学习 0.2，世界模型 0.2）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《MA-WAM: Multi-Agent World-Action Model for Test-Time Planning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent cooperative tasks require different agents to execute a joint action simultaneously, and each agent's action affects both the observations and responses of the other agents. Hence, a world model is needed to predict the team return resulting from the joint actions of all agents. A naive extension directly applies a single-agent world model to each agent's action when predicting the team return step by step. However, such an extension fails to capture the dependencies among the simultaneous actions of multiple agents. We propose Multi-Agent World-Action Model (MA-WAM), a test-time planning framework that enables a frozen multi-agent flow policy to evaluate futures of candidate joint actions. To our knowledge, MA-WAM is the first test-time world-model planner for multi-agent flow policies. MA-WAM predicts the consequences of each joint action according to cross-agent dependencies and enables efficient candidate scoring. Across 30 offline multi-agent reinforcement learning (MARL) settings on MAMuJoCo, SMAC, and MPE, MA-WAM achieves mean relative gains of 22.0% over direct execution and 25.6% over uniform action selection. Under the standard evaluation protocol on an A100 GPU, MA-WAM adds 12.1 ms, accounting for 2.5% of the measured generation-and-scoring time.

</details>

---

### [[20_Research/Papers/大模型/AgentRecommender_LLM_Agents_Enable_Customizable_Recommender_Systems_on_the_User_Side|AgentRecommender: LLM Agents Enable Customizable Recommender Systems on the User Side]]

![[assets/2609.31166_first_page.png|800]]

- **arXiv**: [2609.31166](https://arxiv.org/abs/2609.31166)
- **PDF**: https://arxiv.org/pdf/2609.31166
- **详细分析**: [[20_Research/Papers/大模型/AgentRecommender_LLM_Agents_Enable_Customizable_Recommender_Systems_on_the_User_Side|AgentRecommender: LLM Agents Enable Customizable Recommender Systems on the User Side]]
- **作者**: Ryoma Sato
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AgentRecommender: LLM Agents Enable Customizable Recommender Systems on the User Side》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recommender systems have traditionally been developed for platforms. However, this has given rise to many phenomena that may be advantageous for platform lock-in but are a nuisance to users, such as clickbait, filter bubbles, and the spread of fake news. Recently, user-side recommender systems have been proposed as a new paradigm for solving this problem. If users deploy their own recommender systems, they are no longer at the mercy of the platform's interests. However, building a user-side recommender system is not trivial; in particular, customizing one for oneself requires additional data. We propose AgentRecommender, a method that leverages the investigation capability and internal knowledge of LLM agents to flexibly build user-side recommender systems without additional data. AgentRecommender allows users to easily create recommender systems tailored to their own preferences.

</details>

---

### [[20_Research/Papers/强化学习/JevAdvBench_A_Benchmark_and_Black-Box_Attacks_for_Reinforcement_Learning_for_Calibrated_Decisions_Models|JevAdvBench: A Benchmark and Black-Box Attacks for Reinforcement Learning for Calibrated Decisions Models]]

![[assets/2609.31142_first_page.png|800]]

- **arXiv**: [2609.31142](https://arxiv.org/abs/2609.31142)
- **PDF**: https://arxiv.org/pdf/2609.31142
- **详细分析**: [[20_Research/Papers/强化学习/JevAdvBench_A_Benchmark_and_Black-Box_Attacks_for_Reinforcement_Learning_for_Calibrated_Decisions_Models|JevAdvBench: A Benchmark and Black-Box Attacks for Reinforcement Learning for Calibrated Decisions Models]]
- **作者**: Jianyi Hu, Hangtao Zhang, Yi Liu, Yeqi Zeng, Li Zeng, Xianlong Wang, Rui Wang, Leo Yu Zhang
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Security

#### 研究背景与动机

《JevAdvBench: A Benchmark and Black-Box Attacks for Reinforcement Learning for Calibrated Decisions Models》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HarmBench, JevAdvBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Models trained with reinforcement learning for calibrated decisions (RLCD), such as Jev, answer a typed question about an input, the state, with a probability, a choice, or a score, and software acts on the answer without a person reading it. Their robustness has not been measured: adversarial benchmarks score what a model generates or executes, whereas a typed model generates nothing and returns a well-formed answer even when manipulated. Measurement is also hard, because identical requests can return different answers, most available labels come from the model itself, and the API preprocesses each request out of view. Our key idea is to score each attacked decision against the model's own clean decision rather than against labels, and to read it against the change caused by an identical re-run. Building on this, we introduce JevAdvBench, to our knowledge the first adversarial benchmark for RLCD models, with 812 typed questions over 66 scenarios, and a black-box attack suite of 9,744 single-edit variants that each edit one part of a request, with billed input tokens confirming that the edit reached the model. On jev-1.13.0, rewording stays within 1.2 percentage points of the re-run baseline, and fields outside the schema never reach the model. In contrast, one unverified opinion appended to the state flips 12.1% of decisions, statistically tied with the strongest injected command (10.1%), and pushes 38% of confident answers below the 0.8 confidence threshold that routes them to human review. Applications built on RLCD models should therefore treat the state as untrusted, argued input. Project website: https://JevAdvBench.github.io/JevAdvBench/

</details>

---

### [[20_Research/Papers/大模型/Up_and_Down_the_Abstraction_Ladder_Code-Based_Skills_for_Language_Agents|Up and Down the Abstraction Ladder: Code-Based Skills for Language Agents]]

![[assets/2609.31076_figure.png|800]]

- **arXiv**: [2609.31076](https://arxiv.org/abs/2609.31076)
- **PDF**: https://arxiv.org/pdf/2609.31076
- **详细分析**: [[20_Research/Papers/大模型/Up_and_Down_the_Abstraction_Ladder_Code-Based_Skills_for_Language_Agents|Up and Down the Abstraction Ladder: Code-Based Skills for Language Agents]]
- **作者**: Bartłomiej Cupiał, Jens Tuyls, Maciej Wołczyk, Davide Paglieri, Martin Klissarov, Benjamin Eysenbach, Piotr Miłoś, Karthik R. Narasimhan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.6，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Up and Down the Abstraction Ladder: Code-Based Skills for Language Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language agents struggle to act and learn in environments that require long sequences of low-level actions. Code-based abstractions can make these agents more productive by letting them invoke reusable skills instead of repeatedly selecting individual actions. The code handles recurring local decisions, while the language model decides which skills to use and how to combine them. Yet abstractions are leaky, and situations beyond a skill's capabilities may require a return to primitive actions. Motivated by this tradeoff between productivity and flexibility, we systematically study how code-based action abstraction affects the performance, inference cost, and learning of language agents. We study this in NetHack, a challenging, long-horizon game environment, using CodeHack, our library of code-based skills with natural-language descriptions. We use this library to compare agents restricted to primitives with those using semantic skills alone or in combination with primitives. We evaluate these agents in three settings: zero-shot prompting, supervised fine-tuning, and reinforcement learning. Across a broad zero-shot evaluation on NetHack, we find that compared with primitives, skills nearly triple game progression, while reducing inference cost per episode by 86%. Combining skills with primitives retains much of this benefit while preserving a path back down to low-level actions. Finally, in RL, we find that skill-based agents learn significantly faster than agents acting on primitives, achieving a 7.2x larger average gain in dungeon level over the same training budget. These results show that a supplied skill library can improve performance, efficiency, and learning, while retaining primitives provides flexibility when the library is insufficient. We release CodeHack together with training and evaluation code.

</details>

---

### [[20_Research/Papers/大模型/Cheap,_open_agents_make_LLM_pollution_harder_to_mitigate|Cheap, open agents make LLM pollution harder to mitigate]]

![[assets/2609.31054_figure.png|800]]

- **arXiv**: [2609.31054](https://arxiv.org/abs/2609.31054)
- **PDF**: https://arxiv.org/pdf/2609.31054
- **详细分析**: [[20_Research/Papers/大模型/Cheap,_open_agents_make_LLM_pollution_harder_to_mitigate|Cheap, open agents make LLM pollution harder to mitigate]]
- **作者**: Raluca Rilla, Anne-Marie Nussberger, Rui Mata, Dirk U. Wulff
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Cheap, open agents make LLM pollution harder to mitigate》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) pollution occurs when synthetic responses contaminate data intended to capture human behavior. High deployment costs have so far limited the risk posed by autonomous survey agents. However, open-weight models paired with open-source agentic frameworks may have removed this barrier. We compared the performance and detectability of nine agent configurations, ranging from fully open variants to closed commercial ones. Each agent autonomously completed a survey containing multiple response types yielding various detection checks. Fully open agents ran locally without usage fees and performed competitively with commercial alternatives. Open and commercial agents failed different sets of checks, and no single check reliably detected all agents, but open-text responses discriminated best between agents and humans. These findings identify fully open agents as a distinct risk for LLM pollution and support multilayered detection strategies emphasizing open-text analysis.

</details>

---

### [[20_Research/Papers/具身智能/The_Linear_Representation_Hypothesis_for_Vision-Language-Action_Models|The Linear Representation Hypothesis for Vision-Language-Action Models]]

![[assets/2609.30996_figure.png|800]]

- **arXiv**: [2609.30996](https://arxiv.org/abs/2609.30996)
- **PDF**: https://arxiv.org/pdf/2609.30996
- **详细分析**: [[20_Research/Papers/具身智能/The_Linear_Representation_Hypothesis_for_Vision-Language-Action_Models|The Linear Representation Hypothesis for Vision-Language-Action Models]]
- **作者**: Minseok Jeong, Hyewon Choi, Hiroyasu Tsukamoto, SooJean Han
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.8（加权：具身智能 1.8）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《The Linear Representation Hypothesis for Vision-Language-Action Models》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The linear representation hypothesis (LRH) has become a standard lens for measuring and intervening on semantic information through the internal representations of large language models (LLMs). A growing body of work has begun extending this perspective to vision-language-action (VLA) models, but the dynamical nature of embodied interaction introduces an additional challenge. Unlike semantic attributes commonly studied in LLMs, such as gender or language, a physical quantity of interest (QoI) in a VLA evolves jointly with the system dynamics: the representation influences the actions selected by the policy, which alter the physical state and, in turn, the next representation. In this paper, we develop a theoretical, signature-based formulation of the LRH for VLA that unifies representations and policies. On the representation side, we establish the existence of representations from which the future evolution of a QoI under a candidate action trajectory can be recovered via linear probing. On the policy side, we introduce a signature generalized linear model for stochastic action chunks. This structure yields a monotonic change in the expected future QoI along linear paths in natural parameter space, enabling linear steering. We construct an explicit oracle representation in a planar control-affine navigation experiment and verify the predicted linear probing and steering mechanisms.

</details>

---

### [[20_Research/Papers/具身智能/SciHorizon-eLab_An_Agentic_Protocol-to-Task_Compiler_for_Scalable_Benchmarking_of_Scientific_Embodied_Agents|SciHorizon-eLab: An Agentic Protocol-to-Task Compiler for Scalable Benchmarking of Scientific Embodied Agents]]

![[assets/2609.30971_first_page.png|800]]

- **arXiv**: [2609.30971](https://arxiv.org/abs/2609.30971)
- **PDF**: https://arxiv.org/pdf/2609.30971
- **详细分析**: [[20_Research/Papers/具身智能/SciHorizon-eLab_An_Agentic_Protocol-to-Task_Compiler_for_Scalable_Benchmarking_of_Scientific_Embodied_Agents|SciHorizon-eLab: An Agentic Protocol-to-Task Compiler for Scalable Benchmarking of Scientific Embodied Agents]]
- **作者**: Maokai Qin, Chuan Qin, Qi Zhang, Dianyu Liu, Zirui Liu, Hongting Niu, Yuanchun Zhou, Hengshu Zhu
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 1.2，大模型 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《SciHorizon-eLab: An Agentic Protocol-to-Task Compiler for Scalable Benchmarking of Scientific Embodied Agents》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LabVLA, RLBench, SciVLABench, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied agents offer a promising route to automating scientific experimentation, yet their progress is constrained by the lack of reliable and systematic evaluation environments. Existing simulation-based laboratory benchmarks rely heavily on manual task engineering, making it challenging to systematically compile diverse scientific protocols into executable and verifiable embodied tasks at scale. To address this challenge, we introduce SciHorizon-eLab, an agentic protocol-to-task compiler that formulates scientific embodied task construction as a compilation problem. Given a natural-language protocol of scientific experiments, SciHorizon-eLab progressively compiles laboratory protocols into semantic-preserving embodied tasks through semantic grounding, executable task synthesis, and multi-stage simulation-based certification. The system generates semantically grounded environments, executable manipulation programs, and step-level success specifications, while enabling reproducible generation of expert demonstrations and execution traces. Using this pipeline, we further construct \BenchName, a ready-to-use benchmark comprising 300 certified tasks across diverse laboratory operations. It supports HIL task execution, reproducible expert-demonstration generation, and ordered step-level evaluation. Across representative tasks, the strongest policy attains an average success rate of only 49.7%, with further evaluations revealing pronounced weaknesses in human and embodied agent coordination. We publicly release the code, benchmark data, and evaluation toolkit at https://github.com/SciHorizon-elab/SciHorizon-elab.

</details>

---

### [[20_Research/Papers/强化学习/PORL_Pretrained_Offline_Reinforcement_Learning_for_the_Job_Shop_Scheduling_Problem|PORL: Pretrained Offline Reinforcement Learning for the Job Shop Scheduling Problem]]

![[assets/2609.30948_first_page.png|800]]

- **arXiv**: [2609.30948](https://arxiv.org/abs/2609.30948)
- **PDF**: https://arxiv.org/pdf/2609.30948
- **详细分析**: [[20_Research/Papers/强化学习/PORL_Pretrained_Offline_Reinforcement_Learning_for_the_Job_Shop_Scheduling_Problem|PORL: Pretrained Offline Reinforcement Learning for the Job Shop Scheduling Problem]]
- **作者**: Mateo Toro Diz, Jonathan Hoss, Noah Klarmann
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《PORL: Pretrained Offline Reinforcement Learning for the Job Shop Scheduling Problem》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Job Shop Scheduling Problem (JSSP) is a fundamental combinatorial optimization problem in industrial optimization. This work introduces Pretrained Offline Reinforcement Learning (PORL), a hybrid approach that combines simulation-based online pretraining with offline fine-tuning on production-specific data. Reinforcement learning through online interaction enables exploration of general scheduling strategies, but typically relies on simulation environments and may suffer from a simulation-to-reality gap. In contrast, offline RL avoids direct interaction with the environment by learning from historical data, but its performance is strongly influenced by dataset quality and coverage. PORL combines the strengths of both paradigms by first learning a general scheduling policy through online interaction and subsequently adapting it offline to a target distribution. A KL-divergence-based policy constraint is introduced to limit deviations from the pretrained policy during fine-tuning. The approach is evaluated on JSSP instances with distribution shift and datasets generated from heuristic, noisy-expert, and random behavioral policies. The results show that PORL consistently achieves lower optimality gaps than standalone offline RL and the considered general scheduling baselines. Furthermore, its advantage over standalone offline RL increases as dataset quality decreases, indicating reduced sensitivity to the quality and coverage of the available offline data. The results suggest that offline adaptation of pretrained policies is a promising approach for industrial scheduling environments where direct online exploration is impractical.

</details>

---

### [[20_Research/Papers/世界模型/OneWorld_Learning_Consistent_Physics_Across_Actions_in_World_Models|OneWorld: Learning Consistent Physics Across Actions in World Models]]

![[assets/2609.30946_figure.png|800]]

- **arXiv**: [2609.30946](https://arxiv.org/abs/2609.30946)
- **PDF**: https://arxiv.org/pdf/2609.30946
- **详细分析**: [[20_Research/Papers/世界模型/OneWorld_Learning_Consistent_Physics_Across_Actions_in_World_Models|OneWorld: Learning Consistent Physics Across Actions in World Models]]
- **作者**: Ke He, Yichen Ding, Bin Yang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《OneWorld: Learning Consistent Physics Across Actions in World Models》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Mismatched-World, OneWorld, RoboNet, Same-World, Shared-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned video world models aim to predict scene evolution under different actions, a capability that is essential for reliable planning, decision-making, and interaction in dynamic environments. However, futures generated independently from the same initial scene may each appear plausible while implying incompatible physical properties, such as friction or mass. This inconsistency can lead to contradictory predictions across interventions, making it difficult for the model to maintain a coherent understanding of the underlying world and limiting its reliability for planning and decision-making. To address these issues, we propose OneWorld, a shared-mechanism counterfactual generation framework that jointly models multiple action-conditioned futures under a common latent physical mechanism. A physical mechanism interpreter first infers a distribution over latent mechanisms from each action-outcome branch. These distributions are then aggregated into shared-world evidence, which captures whether the branches admit a common physical explanation while accounting for uncertainty in less informative branches. This evidence constrains flow training and guides sampling, encouraging consistency in the underlying physical mechanism while preserving the distinct outcomes induced by different actions. We further introduce a multi-intervention evaluation protocol in controlled environments, following the interaction settings of ACWM-Phys, to assess whether generated futures can be jointly explained by the same physical parameters, alongside standard measures of single-rollout prediction quality. Experiments in these environments show that OneWorld improves cross-intervention physical consistency while maintaining competitive single-rollout prediction quality.

</details>

---

### [[20_Research/Papers/大模型/LogicTree-RAG_Logic_Tree-guided_Retrieval-Augmented_Generation_for_Long-form_Patent_Drafting|LogicTree-RAG: Logic Tree-guided Retrieval-Augmented Generation for Long-form Patent Drafting]]

![[assets/2609.30943_figure.png|800]]

- **arXiv**: [2609.30943](https://arxiv.org/abs/2609.30943)
- **PDF**: https://arxiv.org/pdf/2609.30943
- **详细分析**: [[20_Research/Papers/大模型/LogicTree-RAG_Logic_Tree-guided_Retrieval-Augmented_Generation_for_Long-form_Patent_Drafting|LogicTree-RAG: Logic Tree-guided Retrieval-Augmented Generation for Long-form Patent Drafting]]
- **作者**: Jiaqi Zhu, Naili Xing, Hexiang Pan, Haotian Gao, Jianwei Yin, Xiaokui Xiao, Beng Chin Ooi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM

#### 研究背景与动机

《LogicTree-RAG: Logic Tree-guided Retrieval-Augmented Generation for Long-form Patent Drafting》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-form technical text generation underpins knowledge-intensive workflows, yet remains challenging for large language models (LLMs) due to the need for globally consistent logical structuring and faithful technical reasoning beyond local coherence. Patent drafting is a canonical instance of this challenge, demanding holistic generation of a legally compliant and technically exhaustive document through sustained multi-expert collaboration. Existing approaches often focus on partial section generation or rely on manually crafted outlines, limiting scalable automation in realistic settings. In this work, we propose LogicTree-RAG, a logic tree-guided retrieval-augmented generation framework that induces a hierarchical logic tree as a global organizational backbone to organize and ground technical disclosures, without relying on expert-defined drafting priors. Each node in the logic tree represents a technical element and is constructed through evidence-guided recursive generation. A hybrid traversal mechanism then maps the logic tree into patent sections, enabling controllable and section-balanced generation. Extensive experiments show that LogicTree-RAG consistently improves content quality and language conformity over strong LLM-based baselines and achieves longer structured generation with high token efficiency, demonstrating the effectiveness of logic-centric generation for complex technical document drafting.

</details>

---

### [[20_Research/Papers/大模型/Financial_Fragility_in_Societies_of_LLM_Agents_Coordination_Failures_and_Stabilizing_Mechanisms|Financial Fragility in Societies of LLM Agents: Coordination Failures and Stabilizing Mechanisms]]

![[assets/2609.30940_figure.jpg|800]]

- **arXiv**: [2609.30940](https://arxiv.org/abs/2609.30940)
- **PDF**: https://arxiv.org/pdf/2609.30940
- **详细分析**: [[20_Research/Papers/大模型/Financial_Fragility_in_Societies_of_LLM_Agents_Coordination_Failures_and_Stabilizing_Mechanisms|Financial Fragility in Societies of LLM Agents: Coordination Failures and Stabilizing Mechanisms]]
- **作者**: Zhenhao Fu, Ruipeng Xu, Qibing Ren
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Financial Fragility in Societies of LLM Agents: Coordination Failures and Stabilizing Mechanisms》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CoopEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Individually protective decisions can produce avoidable collective failures. As large language model (LLM) agents take on greater roles in financial decision-making, financial AI safety must therefore be considered not only at the level of individual agents, but also at the level of the systems they jointly create. We study this problem with FRAIL, a controlled experimental framework that places LLM agents in three dynamic financial environments---bank runs, debt rollover, and reward crowdfunding---where agents' decisions reshape the financial conditions faced by others. Across seven leading LLMs, we find widespread collective fragility even when no agent is instructed to destabilize the system: 77\% of baseline bank-run episodes and 83\% of debt-rollover episodes end in failure. We then compare three interaction mechanisms based on compensated commitments, centralized commitment agreements, and participant-led coalitions. All three improve aggregate outcomes, but no single mechanism performs best across all financial structures. Across mechanisms, successful stabilization shares a common temporal pattern: broad commitment forms early, before defensive behavior becomes self-reinforcing. Our findings show that individually capable agents do not automatically form safe financial systems, highlighting system-level evaluation and interaction design as central problems for financial AI safety. Code is available at https://anonymous.4open.science/r/FinFrail-CF26.

</details>

---

### [[20_Research/Papers/具身智能/NavGen_Visual_Generative_Models_as_a_Scalable_Data_Engine_for_Embodied_3D_Navigation|NavGen: Visual Generative Models as a Scalable Data Engine for Embodied 3D Navigation]]

![[assets/2609.30770_figure.jpg|800]]

- **arXiv**: [2609.30770](https://arxiv.org/abs/2609.30770)
- **PDF**: https://arxiv.org/pdf/2609.30770
- **详细分析**: [[20_Research/Papers/具身智能/NavGen_Visual_Generative_Models_as_a_Scalable_Data_Engine_for_Embodied_3D_Navigation|NavGen: Visual Generative Models as a Scalable Data Engine for Embodied 3D Navigation]]
- **作者**: Xijie Huang, Yongyang Wan, Chengbin Dong, Zimo Ding, Mo Zhu, Yijin Wang, Zhiyang Liu, Fei Gao, Yuze Wu, Xin Zhou
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《NavGen: Visual Generative Models as a Scalable Data Engine for Embodied 3D Navigation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AirSim, Real-World, VBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose robot models increasingly rely on large and diverse datasets. For embodied 3D navigation, however, existing data sources face a fundamental trade-off: simulated data can be generated at scale but often suffer from the visual sim-to-real gap, whereas real-world flight data provide realistic observations but are costly to collect. This paper studies another direction: the use of high-fidelity visual generative models as scalable data engines for embodied 3D navigation. We introduce NavGen, a text-to-video data generation pipeline that produces diverse vision-language navigation (VLN) episodes across indoor and outdoor scenes. We also propose a style-diversification method that scales up long-tail data that are difficult and costly to collect. The resulting dataset contains approximately 400K navigation episodes. We evaluate our dataset against existing UAV navigation datasets across multiple metrics, and find that the model trained on our data generally improves with scale, outperforming those trained on existing datasets. To validate real-world transferability, we deploy the trained model in world-action-model paradigm to real-world flying experiments. The final model achieves a 75\% success rate across different navigation tasks and environments.

</details>

---

### [[20_Research/Papers/机器人/Anatomy-Aware_Dexterity-Driven_Design_Optimization_of_Surgical_Continuum_Robots|Anatomy-Aware Dexterity-Driven Design Optimization of Surgical Continuum Robots]]

![[assets/2609.30745_figure.png|800]]

- **arXiv**: [2609.30745](https://arxiv.org/abs/2609.30745)
- **PDF**: https://arxiv.org/pdf/2609.30745
- **详细分析**: [[20_Research/Papers/机器人/Anatomy-Aware_Dexterity-Driven_Design_Optimization_of_Surgical_Continuum_Robots|Anatomy-Aware Dexterity-Driven Design Optimization of Surgical Continuum Robots]]
- **作者**: Tony Qin, Peter Connor, Khoa Dang, Carter Hatch, Caleb Rucker, Robert J. Webster, Ron Alterovitz
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Anatomy-Aware Dexterity-Driven Design Optimization of Surgical Continuum Robots》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BOBYQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Performing complex medical procedures with continuum robots requires careful selection of their geometric design parameters. The robot should have high dexterity in the specific anatomical environment of its procedure. This work presents a design optimization method that considers both dexterity and anatomy. We introduce the Reachable Volumetric Dexterous Solid Angle (RVDSA) metric as our objective, which measures the ability of a robot's end effector to reach the points in a goal volume from different directions via collision-free paths from a start configuration. We present a computationally efficient motion planner to compute this objective function for a given robotic design, and we use an asymptotically optimal simulated annealing optimizer to compute an optimized design. We applied our new method to optimize the design of a bimanual dexterous sheaths robot for performing procedures on cancerous polyps in colon anatomies, achieving a 78% higher RVDSA on average than optimizing for 3D voxel coverage alone.

</details>

---

### [[20_Research/Papers/具身智能/VLALight_Lightweight_Vision-Language-Action_Models_for_Emergency-Aware_Traffic_Signal_Control|VLALight: Lightweight Vision-Language-Action Models for Emergency-Aware Traffic Signal Control]]

![[assets/2609.30709_figure.png|800]]

- **arXiv**: [2609.30709](https://arxiv.org/abs/2609.30709)
- **PDF**: https://arxiv.org/pdf/2609.30709
- **详细分析**: [[20_Research/Papers/具身智能/VLALight_Lightweight_Vision-Language-Action_Models_for_Emergency-Aware_Traffic_Signal_Control|VLALight: Lightweight Vision-Language-Action Models for Emergency-Aware Traffic Signal Control]]
- **作者**: Kemou Jiang, Maonan Wang, Xingchen Zou, Jiayue Zhu, Yuhang Fu, Sicheng Wang, Xi Chen, Yirong Chen, Zhiyong Cui
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.2（加权：具身智能 1.2）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《VLALight: Lightweight Vision-Language-Action Models for Emergency-Aware Traffic Signal Control》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, OpenVLA, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traffic signal control (TSC) is essential for mitigating urban congestion. Recent advances in vision-language models (VLMs) enable richer interpretation of intersection scenes, opening new opportunities for visual-context-aware TSC. However, the loose coupling and repeated information conversion between modules can lead to the loss of fine-grained visual details, while sequential inference introduces substantial latency. To address these limitations, we propose VLALight, a lightweight end-to-end vision-language-action framework that directly maps intersection observations and signal-phase information to discrete signal actions. To handle the multi-view nature of TSC, VLALight combines multiple directional camera views into a unified visual input and uses textual instructions to establish their correspondence with traffic movements and signal phases. This design enables direct action prediction with a compact 0.5 B-parameter model, without intermediate image-to-text descriptions or handcrafted traffic-state representations. Experiments show that VLALight delivers the best emergency-vehicle service of all compared methods, reducing pooled emergency waiting time by 21.1% over the cascaded VLMLight while running in real time on local hardware and generalizing to unseen intersection topologies and traffic-flow patterns.

</details>

---

### [[20_Research/Papers/强化学习/Threat-Aware_Energy-Efficient_Deployment_for_Dynamic_UAV_Networks_A_Multi-Agent_RL_Approach|Threat-Aware Energy-Efficient Deployment for Dynamic UAV Networks: A Multi-Agent RL Approach]]

![[assets/2609.30690_figure.png|800]]

- **arXiv**: [2609.30690](https://arxiv.org/abs/2609.30690)
- **PDF**: https://arxiv.org/pdf/2609.30690
- **详细分析**: [[20_Research/Papers/强化学习/Threat-Aware_Energy-Efficient_Deployment_for_Dynamic_UAV_Networks_A_Multi-Agent_RL_Approach|Threat-Aware Energy-Efficient Deployment for Dynamic UAV Networks: A Multi-Agent RL Approach]]
- **作者**: Faisal Al-Kamali, Hussein A. Ammar, Francois Chan, James H. Bayes, Yasser Gadallah, Mohamed H. Ahmed
- **cs 子类**: cs.AI, cs.IT, cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 强化学习, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 0.36，世界模型 0.16，机器人 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Threat-Aware Energy-Efficient Deployment for Dynamic UAV Networks: A Multi-Agent RL Approach》归入 机器人、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ensuring operational safety in threat-prone environments remains a critical challenge for multi-UAV networks serving as aerial base stations. This paper proposes an efficient framework to maximize global energy efficiency (EE) while promoting safe operation through threat-aware clustering and reward-based safety enforcement. The proposed framework is executed in three steps. First, a threat-aware K-means (TAKM) algorithm determines the minimum required UAVs and computes safe initial placements. Second, an optimal matching stage assigns physical UAVs to these centroids to minimize energy expenditure. Third, a threat-aware multi-agent twin delayed deep deterministic policy gradient (MATD3) algorithm dynamically optimizes trajectories, power, and user associations. Simulation results show that the proposed framework achieves zero observed safety violations in the considered scenarios while achieving superior EE and faster convergence than other learning methods and non-clustering baselines. Compared to heuristic optimization, the proposed framework outperforms the greedy particle swarm optimization (GPSO) and achieves performance comparable to that of the optimized PSO (OPSO), while incurring significantly lower online deployment computational complexity. Furthermore, the proposed framework demonstrates effective generalization to unseen user distributions, large UAV fleets, and different threat geometries, while maintaining zero safety violations.

</details>

---

### [[20_Research/Papers/世界模型/Causal_Retention_in_Interactive_Agents_Interface_Factorization_and_Selective_Adaptation|Causal Retention in Interactive Agents: Interface Factorization and Selective Adaptation]]

![[assets/2609.30650_first_page.png|800]]

- **arXiv**: [2609.30650](https://arxiv.org/abs/2609.30650)
- **PDF**: https://arxiv.org/pdf/2609.30650
- **详细分析**: [[20_Research/Papers/世界模型/Causal_Retention_in_Interactive_Agents_Interface_Factorization_and_Selective_Adaptation|Causal Retention in Interactive Agents: Interface Factorization and Selective Adaptation]]
- **作者**: Shengjun Zhang, Tingyi Liu, Dong Xie, Yunlong Dong, Xiang Wang, Cheng Zeng
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型, 强化学习
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.16，世界模型 0.36）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Causal Retention in Interactive Agents: Interface Factorization and Selective Adaptation》归入 大模型、世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task performance need not determine which intervention mechanism an agent retains. We study causal retention: whether a frozen learned state answers a mechanism-probe map fixed independently of training, including action, context, direct target, value, and delay. For finite structural causal model classes, the optimal probe error is a Bayes decision risk. It vanishes exactly when every learning-interface fiber lies within one probe-answer fiber; any state obtained by post-processing that interface inherits the same lower bound. A posterior-coverage theorem characterizes budgeted retesting, while an exact edit decomposition shows that the shifted set is the unique support of an error-free target update. Causal Core implements these conditions through evidence-gated writing, readout filtering, temporal credit, hidden-context setup, and local diagnostic updates. Experiments cover finite causal systems, continuous simulators, an official TD-MPC2 world model, and Qwen2.5-7B-Instruct. A frozen Qwen last-layer probe reaches 0.958 balanced accuracy on source mechanisms but 0.583 on changed delays; the gated mechanism state reaches 1.000 and accepts only 0.056 of synchronized-readout candidates. In TD-MPC2, five target states per actuator recover effect-sign accuracy from 0.057 to 0.948 without degrading stable responses. Causal retention is therefore distinct from task sufficiency and source-domain decodability.

</details>

---

### [[20_Research/Papers/大模型/Thinking_Less_to_Simulate_Better_Intuitive_Prompting_Improves_LLM_Agents_Simulating_Individual_Social_Media_Reactions,_Including_Unfamiliar_|Thinking Less to Simulate Better: Intuitive Prompting Improves LLM Agents Simulating Individual Social Media Reactions, Including Unfamiliar Content]]

![[assets/2609.30563_first_page.png|800]]

- **arXiv**: [2609.30563](https://arxiv.org/abs/2609.30563)
- **PDF**: https://arxiv.org/pdf/2609.30563
- **详细分析**: [[20_Research/Papers/大模型/Thinking_Less_to_Simulate_Better_Intuitive_Prompting_Improves_LLM_Agents_Simulating_Individual_Social_Media_Reactions,_Including_Unfamiliar_|Thinking Less to Simulate Better: Intuitive Prompting Improves LLM Agents Simulating Individual Social Media Reactions, Including Unfamiliar Content]]
- **作者**: Ljubisa Bojic, Tijana Stanic, Joerg Matthes, Agariadne Dwinggo Samala, Bojana Dinic, Jue Wang
- **cs 子类**: cs.AI, cs.CL, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Thinking Less to Simulate Better: Intuitive Prompting Improves LLM Agents Simulating Individual Social Media Reactions, Including Unfamiliar Content》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Platform policies are increasingly tested on artificial users, making agent fidelity important. Yet convincing fake profiles could also manipulate perceived public opinion before elections. Validation has concentrated on agreement with human behaviour and has paid little attention to whether an agent behaves in line with the profile it was given. The present study profiled eight Serbian participants through a questionnaire, a deep interview, and a written self-presentation, recorded their reactions to sixty-eight social media posts, and asked four language models to predict those reactions under five prompt conditions varying profile content and instruction style. Attitudinal content improved prediction over demographic backstories by a wide margin. Agents matched their stated profiles more closely than participants matched their own survey answers, and consistency proved unrelated to fidelity once profile information was present. Instructing models to respond intuitively and immediately rather than analytically gave the highest fidelity of any condition and cut the compression of individual differences from seven times the human level to three. The advantage held on posts about topics the questionnaire never raised, where that condition reached the highest fidelity of any setup and beat a crowd baseline by a wide margin, which suggests that agents prompted this way could serve as general-purpose simulated users rather than specialists on the topics they were profiled for. Results may bear implications for the development of language models, because intuition-based setups appear better suited to some tasks than reasoning-based ones.

</details>

---

### [[20_Research/Papers/大模型/Actively_Resolving_Contextual_Uncertainty_for_Underspecified_Tasks_in_Natural_Language|Actively Resolving Contextual Uncertainty for Underspecified Tasks in Natural Language]]

![[assets/2609.30428_figure.png|800]]

- **arXiv**: [2609.30428](https://arxiv.org/abs/2609.30428)
- **PDF**: https://arxiv.org/pdf/2609.30428
- **详细分析**: [[20_Research/Papers/大模型/Actively_Resolving_Contextual_Uncertainty_for_Underspecified_Tasks_in_Natural_Language|Actively Resolving Contextual Uncertainty for Underspecified Tasks in Natural Language]]
- **作者**: Zachary Ravichandran, Jonathan Diller, Fernando Cladera, Varun Murali, George J. Pappas, Vijay Kumar
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Actively Resolving Contextual Uncertainty for Underspecified Tasks in Natural Language》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models provide robots with the ability to interpret natural language and reason about environmental context, yet most language-conditioned policies assume that goals are well-specified and that task-relevant information is provided upfront via a prior map. Operating in unfamiliar environments with underspecified tasks entails high contextual uncertainty: the robot must jointly infer what constitutes task success, what constitutes relevant information, and where (or whether) that information exists. We address these limitations via CLUE (Closed-Loop contextual Uncertainty rEsolution), a framework for actively resolving contextual uncertainty given underspecified tasks in natural language. CLUE uses an LLM-derived policy to hypothesize task-relevant concepts and potential plans. It then uses a language-embedded map, which is constructed online, to ground these hypotheses into actions. The policy sequentially evaluates hypotheses via closed-loop environment interaction and refines its plans as it gathers new information. We deploy CLUE on a Boston Dynamics Spot across three real indoor and outdoor environments spanning 15 tasks that require object disambiguation, functional inference, and occlusion reasoning. CLUE achieves a success rate within 7 percentage points of an oracle policy and outperforms an LLM-enabled planner without closed-loop feedback by a 4x margin. Supporting experiments demonstrate that simply building and then querying a language-enriched map is insufficient to resolve complex contextual planning tasks; these approaches achieve roughly one third the success rate of CLUE while requiring over 10x more VLM tokens. We provide additional information at https://zacravichandran.github.io/CLUE.

</details>

---

### [[20_Research/Papers/大模型/Bridging_LLM_Agents_and_Data_Spaces_An_Architectural_Mediation_Approach_using_the_Model_Context_Protocol|Bridging LLM Agents and Data Spaces: An Architectural Mediation Approach using the Model Context Protocol]]

![[assets/2609.30341_first_page.png|800]]

- **arXiv**: [2609.30341](https://arxiv.org/abs/2609.30341)
- **PDF**: https://arxiv.org/pdf/2609.30341
- **详细分析**: [[20_Research/Papers/大模型/Bridging_LLM_Agents_and_Data_Spaces_An_Architectural_Mediation_Approach_using_the_Model_Context_Protocol|Bridging LLM Agents and Data Spaces: An Architectural Mediation Approach using the Model Context Protocol]]
- **作者**: Jaime Alonso Ruiz, Carlos Aparicio, Gabriel Huecas, Joaquín Salvachúa, Andres Munoz-Arcentales
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Bridging LLM Agents and Data Spaces: An Architectural Mediation Approach using the Model Context Protocol》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Data Spaces enable sovereign and governed data sharing across organizational boundaries, but their integration with AI agents remains challenging due to mismatches between probabilistic language model interactions and policy-driven data infrastructures. This article presents an architectural mediation approach based on the Model Context Protocol (MCP), implemented through the Eunomia Agent, to enable controlled interaction between large language model (LLM) agents and data space services. The proposed mediation layer translates data space capabilities into structured, schema-driven tools that AI agents can discover and invoke while preserving governance constraints. A prototype implementation validates end-to-end interaction across catalog discovery, metadata retrieval, and data service invocation without modifying existing data space components. Results demonstrate that protocol-based mediation enables interoperable and standards-aligned integration of AI agents into data space ecosystems. The approach provides practical guidance for organizations seeking to introduce AI-driven automation into governed data-sharing environments while maintaining compliance, interoperability, and architectural separation of concerns.

</details>

---
