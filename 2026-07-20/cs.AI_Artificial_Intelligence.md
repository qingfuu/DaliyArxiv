# cs.AI | Artificial Intelligence | 2026-07-20

#arxiv #ComputerScience

**论文数**: 40

### [[20_Research/Papers/强化学习/When_Does_Muon_Help_Agentic_Reinforcement_Learning|When Does Muon Help Agentic Reinforcement Learning?]]

![[assets/2607.16169_figure.png|800]]

- **arXiv**: [2607.16169](https://arxiv.org/abs/2607.16169)
- **PDF**: https://arxiv.org/pdf/2607.16169
- **详细分析**: [[20_Research/Papers/强化学习/When_Does_Muon_Help_Agentic_Reinforcement_Learning|When Does Muon Help Agentic Reinforcement Learning?]]
- **作者**: Kai Ruan, Jinghao Lin, Zihe Huang, Ziqi Zhou, Qianshan Wei, Xuan Wang, Hao Sun
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《When Does Muon Help Agentic Reinforcement Learning?》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Muon is competitive with AdamW in large-scale pre-training, but its value for reinforcement-learning (RL) post-training remains unclear. We study vanilla Muon in sparse-reward agentic RL through matched single-seed comparisons with AdamW on ALFWorld using Qwen2.5-0.5B-Instruct. Under Group-in-Group Policy Optimization (GiGPO), applying Muon only to hidden weight matrices raises final-window validation success from 0.290 to 0.546 (+88%); high-rate AdamW controls retain no post-update success. The effect depends on the advantage estimator and learning rate. At 3e-5, Muon improves GRPO from 0.161 to 0.268, whereas GraphGPO's late-window gap narrows near saturation. At 1e-5, GraphGPO Muon reaches 0.901, raises normalized validation AUC from 0.399 to 0.556, and reaches 0.5 and 0.75 success 30 and 60 updates earlier, respectively. These exploratory results show that Muon can benefit agentic RL and motivate studying the policy optimizer, advantage estimator, and learning rate jointly. Multi-seed and cross-task validation remain open.

</details>

---

### [[20_Research/Papers/大模型/When_Do_Multi-Agent_Systems_Help_An_Information_Bottleneck_Perspective|When Do Multi-Agent Systems Help? An Information Bottleneck Perspective]]

![[assets/2607.16133_figure.png|800]]

- **arXiv**: [2607.16133](https://arxiv.org/abs/2607.16133)
- **PDF**: https://arxiv.org/pdf/2607.16133
- **详细分析**: [[20_Research/Papers/大模型/When_Do_Multi-Agent_Systems_Help_An_Information_Bottleneck_Perspective|When Do Multi-Agent Systems Help? An Information Bottleneck Perspective]]
- **作者**: Wendi Yu, Lianhao Zhou, Xiangjue Dong, Sai Sudarshan Barath, Declan Staunton, Byung-Jun Yoon, Xiaoning Qian, James Caverlee, Shuiwang Ji
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《When Do Multi-Agent Systems Help? An Information Bottleneck Perspective》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, WorkBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM powered multi-agent systems (MAS) have emerged as a promising paradigm for complex tasks. However, their advantages over single-agent systems (SAS) remain unclear, with performance varying inconsistently across settings. Here, we provide an information bottleneck perspective on elucidating the differences between MAS and SAS. Specifically, our key observation is that a SAS accumulates its full reasoning trace in one shared context, while a MAS uses isolated local contexts connected by bounded relay messages. We show that, under infinite relay bandwidth, any SAS can be simulated by a MAS that transmits the full upstream context. Thus, the nontrivial advantage of MAS arises under bounded relays, where compression introduces a fundamental trade-off: reducing redundant context can improve efficiency, but may also incur loss of task-relevant information. We formalize this trade-off as an information bottleneck controlled by an effective parameter $β$, which captures how the balance shifts with model capability, and shows that MAS gains arise when context reduction outweighs relay information loss. We conduct 18 controlled experiments across five benchmarks and three model scales to validate our theoretical studies. We observe that MAS consistently helps when relays are near-sufficient, especially for weaker models. In contrast, MAS gains shrink or reverse when relays incur information loss, especially for stronger models that can already extract useful information from redundant context and thus gain little from compression. Our study shows that multi-agent design is fundamentally an information-bottleneck optimization problem. This perspective explains when bounded inter-agent communication helps or hurts.

</details>

---

### [[20_Research/Papers/大模型/ToolSciVer_Multimodal_Scientific_Claim_Verification_with_Visual_Tool_Augmented_Reinforcement_Learning|ToolSciVer: Multimodal Scientific Claim Verification with Visual Tool Augmented Reinforcement Learning]]

![[assets/2607.16131_figure.png|800]]

- **arXiv**: [2607.16131](https://arxiv.org/abs/2607.16131)
- **PDF**: https://arxiv.org/pdf/2607.16131
- **详细分析**: [[20_Research/Papers/大模型/ToolSciVer_Multimodal_Scientific_Claim_Verification_with_Visual_Tool_Augmented_Reinforcement_Learning|ToolSciVer: Multimodal Scientific Claim Verification with Visual Tool Augmented Reinforcement Learning]]
- **作者**: Binglin Zhou, Peng Shi, Ryo Kamoi, Nan Zhang, Rui Zhang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.55（加权：大模型 0.75，强化学习 0.8）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《ToolSciVer: Multimodal Scientific Claim Verification with Visual Tool Augmented Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ChartQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal Scientific Claim Verification (MSCV) requires models to verify scientific claims using visually grounded evidence from papers, including figures, tables, charts, and textual context. However, existing methods often fail because they struggle to locate decisive visual evidence, accurately read structured scientific visuals, and integrate multimodal observations into reliable reasoning. We introduce ToolSciVer, the first tool-augmented framework for MSCV to our knowledge. ToolSciVer equips a VLM with three type-aware visual tools, table row/column focus, chart-to-structure parsing, and high-resolution region zoom, which convert dense scientific visuals into explicit, claim-facing evidence, and trains the policy with Group Relative Policy Optimization (GRPO) under a composite reward of answer correctness, format validity, length control, tool-use efficiency, and tool-validity penalties. Experiments on SciVer and MuSciClaims datasets on five VLMs from three model families (Qwen, InternVL, Gemma) demonstrate that our method achieves superior performance compared to four competitive baselines including prompting-based and RL-based tool-use methods, highlighting the effectiveness of learned, type-aware tool use for scientific claim verification.

</details>

---

### [[20_Research/Papers/大模型/Understanding_Reasoning_from_Pretraining_to_Post-Training|Understanding Reasoning from Pretraining to Post-Training]]

![[assets/2607.16097_figure.png|800]]

- **arXiv**: [2607.16097](https://arxiv.org/abs/2607.16097)
- **PDF**: https://arxiv.org/pdf/2607.16097
- **详细分析**: [[20_Research/Papers/大模型/Understanding_Reasoning_from_Pretraining_to_Post-Training|Understanding Reasoning from Pretraining to Post-Training]]
- **作者**: Jingyan Shen, Ang Li, Salman Rahman, Yifan Sun, Micah Goldblum, Matus Telgarsky, Pavel Izmailov
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.87（加权：大模型 0.35，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Understanding Reasoning from Pretraining to Post-Training》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Pre-RL, Pretraining-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has become central to improving large language models (LLMs) on complex reasoning tasks, yet RL post-training is largely studied in isolation from the pretraining that precedes it. As a result, two basic questions remain open: (1) how do pretraining choices (model size, data) shape the returns to RL compute, and (2) what does RL actually do to the model? These questions are difficult to study in the standard LLM setting: pretraining corpora are vast and uncontrolled, making it hard to attribute behaviors to pretraining versus RL, and systematic compute sweeps across both stages are prohibitively expensive. To address these challenges, we use chess as a controlled testbed for studying reasoning across the full pretraining-to-post-training pipeline. We follow the standard LLM training pipeline by pretraining language models from 5M to 1B parameters on human chess games, supervised fine-tuning on synthetic reasoning traces, and running RL on chess puzzles with verifiable rewards. Using this framework, we find that the post-RL performance at given RL compute level is well-predicted from the pretraining loss, and slope of the RL reward curves improves approximately linearly with the pretraining tokens. Beyond scaling, we find that RL does not simply sharpen the SFT policy: on easy puzzles it amplifies correct moves the SFT policy already preferred, while on hard puzzles it surfaces correct moves that were nearly absent under SFT. We further test whether our findings transfer beyond chess by training a 1B language model on math-domain text, where the same predictive pattern emerges: longer-pretrained checkpoints reach higher post-RL performance and improve faster under RL. In sum, we provide a quantitative account of the pretraining-to-RL interface and a controlled testbed for studying the science of reasoning across the full pretraining-to-post-training pipeline.

</details>

---

### [[20_Research/Papers/强化学习/DADiff_Diffusion-Driven_Cross-Domain_Policy_Adaptation_for_Reinforcement_Learning|DADiff: Diffusion-Driven Cross-Domain Policy Adaptation for Reinforcement Learning]]

![[assets/2607.16090_figure.png|800]]

- **arXiv**: [2607.16090](https://arxiv.org/abs/2607.16090)
- **PDF**: https://arxiv.org/pdf/2607.16090
- **详细分析**: [[20_Research/Papers/强化学习/DADiff_Diffusion-Driven_Cross-Domain_Policy_Adaptation_for_Reinforcement_Learning|DADiff: Diffusion-Driven Cross-Domain Policy Adaptation for Reinforcement Learning]]
- **作者**: Hanyang Chen, Anirudh Satheesh, Longchao Da, Hua Wei
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《DADiff: Diffusion-Driven Cross-Domain Policy Adaptation for Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Transferring policies across domains poses a vital challenge in reinforcement learning, due to the dynamics mismatch between the source and target domains. In this paper, we consider the setting of online dynamics adaptation, where policies are trained in the source domain with sufficient data, while only limited interactions with the target domain are allowed. There are a few existing works that address the dynamics mismatch by employing domain classifiers, value-guided data filtering, or representation learning. Instead, we study the domain adaptation problem from a generative modeling perspective. Specifically, we introduce DADiff, a diffusion-based framework that leverages the discrepancy between source and target domain generative trajectories in the generation process of the next state to estimate the dynamics mismatch. Both reward modification and data selection variants are developed to adapt the policy to the target domain. We also provide a theoretical analysis to show that the performance difference of a given policy between the two domains is bounded by the generative trajectory deviation. More discussions on the applicability of the variants and the connection between our theoretical analysis and the prior work are further provided. We conduct extensive experiments in environments with various shifts to validate the effectiveness of our method. The results demonstrate that our method provides superior performance compared to existing approaches, effectively addressing the dynamics mismatch. We provide the code of our method at https://github.com/hanyang-chen/DADiff-release

</details>

---

### [[20_Research/Papers/大模型/HCIG_A_Hierarchical_Cross-Modal_Incongruity_Graph_Network_for_Multimodal_Sarcasm_and_Cyberbullying_Detection|HCIG: A Hierarchical Cross-Modal Incongruity Graph Network for Multimodal Sarcasm and Cyberbullying Detection]]

![[assets/2607.16076_figure.png|800]]

- **arXiv**: [2607.16076](https://arxiv.org/abs/2607.16076)
- **PDF**: https://arxiv.org/pdf/2607.16076
- **详细分析**: [[20_Research/Papers/大模型/HCIG_A_Hierarchical_Cross-Modal_Incongruity_Graph_Network_for_Multimodal_Sarcasm_and_Cyberbullying_Detection|HCIG: A Hierarchical Cross-Modal Incongruity Graph Network for Multimodal Sarcasm and Cyberbullying Detection]]
- **作者**: Bhavana Verma, Priyanka Meel, Dinesh Kumar Vishwakarma
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, ComputerVision, Systems

#### 研究背景与动机

《HCIG: A Hierarchical Cross-Modal Incongruity Graph Network for Multimodal Sarcasm and Cyberbullying Detection》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal sarcasm and cyberbullying detection remain challenging because the intended meaning often emerges from incongruity between textual and visual information rather than from either modality alone. Existing multimodal approaches primarily rely on feature fusion or cross-modal attention, which may not effectively capture hierarchical semantic inconsistencies across different levels of representation. To address this limitation, this paper proposes HCIG (Hierarchical Cross-modal Incongruity Graph Network), a novel framework that models cross-modal incongruity at token, phrase, and global levels using graph attention networks and adaptively integrates these representations through a learned hierarchical attention mechanism. As a complementary architecture, we also introduce GCCN (Graph-based Cross-modal Contradiction Network), which performs graph-based reasoning using contradiction-aware pooling for efficient multimodal interaction learning. The proposed models are evaluated on the MMSD sarcasm benchmark and the MultiBully cyberbullying dataset, together with comprehensive ablation studies and cross-task transfer experiments. Experimental results demonstrate that HCIG achieves the best performance on MMSD with 85.74% accuracy and 85.29% macro-F1, while GCCN attains the highest macro-F1 (68.66%) on MultiBully and HCIG achieves the highest accuracy (69.62%) and bullying-class F1 (74.90%). The findings demonstrate that hierarchical multi-granularity incongruity modeling provides more effective multimodal reasoning than conventional fusion strategies, offering a robust framework for sarcasm and cyberbullying detection in social media.

</details>

---

### [[20_Research/Papers/具身智能/JoyNexus_Service-Oriented_Multi-Tenant_Post-Training_for_VLA_Models|JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models]]

![[assets/2607.16074_figure.png|800]]

- **arXiv**: [2607.16074](https://arxiv.org/abs/2607.16074)
- **PDF**: https://arxiv.org/pdf/2607.16074
- **详细分析**: [[20_Research/Papers/具身智能/JoyNexus_Service-Oriented_Multi-Tenant_Post-Training_for_VLA_Models|JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models]]
- **作者**: Haoran Sun, Wentao Zhang, Junyang Hua, Hedan Yang, Yongjian Guo, Yifei Zhang, Xiaolong Xiang, Mingxi Luo, Jing Long, Chen Zhao, Chen Zhou, Wanting Xu...
- **cs 子类**: cs.AI, cs.DC, cs.SE
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.8，强化学习 0.2，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, ProRL, RL-VLA, RLBench, RLinf-VLA, SimpleVLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The post-training of Vision-Language-Action (VLA) models is essential due to the diversity of simulators, robot embodiments, and task objectives. Existing compute services, whether offered as direct accelerator rental or batch-workload submission, typically allocate an exclusive set of GPU and CPU resources to a single tenant. While this paradigm maximizes client flexibility, it burdens users with infrastructure adaptation, and the fixed card-hour accounting model renders short or bursty workloads both expensive for tenants and inefficient for the service provider. To address these challenges, we present JoyNexus, a unified service for multi-tenant VLA supervised fine-tuning, reinforcement learning, and evaluation. JoyNexus decouples the Training Model Service, Inference Model Service, and Environment Service, each accessed through APIs and backed by resident shared base models with tenant-specific slots. Tenants can directly invoke high-level semantic APIs for training, rollout, and evaluation, or compose custom algorithms using lower-level APIs and their assigned endpoints. Multiple tenants submit workloads concurrently; their action modules, optimizers, rollout records, and policy versions remain isolated, and the service is scheduled by the global Training Queue and Inference Queue. To further improve multi-tenant training efficiency, JoyNexus introduces group batching for heterogeneous VLA data schemas that share a compatible model-facing prefix, enabling a single shared backbone forward pass over grouped samples. Finally, we evaluate JoyNexus through workload simulation and a group-batching pipeline in a realistic embodied scenario. Results show that, compared with isolated single-tenant execution, JoyNexus reduces aggregate GPU time and improves service utilization via cross-tenant scheduling on shared resources.

</details>

---

### [[20_Research/Papers/大模型/LLM-Powered_Agentic_AI_for_5G_6G_Networks_A_Tutorial_and_Survey_on_Architectures,_Protocols,_and_Standardization|LLM-Powered Agentic AI for 5G/6G Networks: A Tutorial and Survey on Architectures, Protocols, and Standardization]]

![[assets/2607.16066_figure.png|800]]

- **arXiv**: [2607.16066](https://arxiv.org/abs/2607.16066)
- **PDF**: https://arxiv.org/pdf/2607.16066
- **详细分析**: [[20_Research/Papers/大模型/LLM-Powered_Agentic_AI_for_5G_6G_Networks_A_Tutorial_and_Survey_on_Architectures,_Protocols,_and_Standardization|LLM-Powered Agentic AI for 5G/6G Networks: A Tutorial and Survey on Architectures, Protocols, and Standardization]]
- **作者**: Mazene Ameur, Abdelkader Mekrache, Bouziane Brik, Adlen Ksentini
- **cs 子类**: cs.AI, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LLM-Powered Agentic AI for 5G/6G Networks: A Tutorial and Survey on Architectures, Protocols, and Standardization》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic Artificial Intelligence (AI), enabled by Large Language Models, marks a shift from rule-based automation toward autonomous, goal-driven control of Next-Generation Networks (NGNs). Existing surveys treat the two domains in isolation, leaving protocol integration, evaluation, and standardization alignment underexplored. To address this gap, a two-part tutorial-and-survey is presented. Part I formalises the control, management, and AI-native planes of 5G and 6G. It then covers the foundations of agentic systems: reasoning, planning, tool use, multi-agent coordination, and evaluation. Part II maps agentic capabilities onto 5G/6G control surfaces, standardization, and major 6G initiatives. Finally, it identifies open challenges shaping autonomous telecommunications.

</details>

---

### [[20_Research/Papers/强化学习/When_Model_Merging_Rivals_Joint_Multi-Task_Reinforcement_Learning_A_Task-Vector_Geometry_Analysis|When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector Geometry Analysis]]

![[assets/2607.16062_figure.png|800]]

- **arXiv**: [2607.16062](https://arxiv.org/abs/2607.16062)
- **PDF**: https://arxiv.org/pdf/2607.16062
- **详细分析**: [[20_Research/Papers/强化学习/When_Model_Merging_Rivals_Joint_Multi-Task_Reinforcement_Learning_A_Task-Vector_Geometry_Analysis|When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector Geometry Analysis]]
- **作者**: S. Aaron McClendon
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.2，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector Geometry Analysis》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model merging is promoted as a substitute for joint multi-task training, yet in the reinforcement-learning setting this substitution is essentially never tested against the baseline it claims to replace: methods merge independently released agents precisely because a joint model is unavailable. We build the missing comparison. Training difficulty-1 and difficulty-2 Qwen3-8B specialists on the AppWorld agent benchmark with LOOP, we merge them (TIES, RAM+) and pit the result against a jointly trained model on the same data. On task-goal completion, merging matches joint RL -- and every merge variant is statistically indistinguishable. To explain why merge method does not matter here, we measure the geometry of the specialists' task vectors, which carries no task-sampling noise: they are near-orthogonal (cosine 0.06 - 0.10) despite ~65% support overlap, a small, shared direction that grows over training and that we calibrate against a random-init floor and a same-run ceiling to confirm it reflects learning, not the low-rank parameterization. Because direction and support are decoupled, support and sign-based merging (RAM, TIES) collapse to near-uniform averaging. We release all code and statistics.

</details>

---

### [[20_Research/Papers/大模型/SciForge_An_AI-Native,_Multimodal_Workbench_for_Scientific_Discovery|SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery]]

![[assets/2607.16038_figure.png|800]]

- **arXiv**: [2607.16038](https://arxiv.org/abs/2607.16038)
- **PDF**: https://arxiv.org/pdf/2607.16038
- **详细分析**: [[20_Research/Papers/大模型/SciForge_An_AI-Native,_Multimodal_Workbench_for_Scientific_Discovery|SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery]]
- **作者**: SciForge Team, Zhangyang Gao, Minghao Fang, Yifei Liu, Hanhui Yang, Xinyu Gu, Shixiang Tang, Siqi Sun, Lei Bai, Cheng Tan, Mengdi Liu, Hao Wu...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Multimodal, Agent, Systems

#### 研究背景与动机

《SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DiscoveryWorld, ScholarQA, ScienceAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scientific work increasingly spans heterogeneous artifacts -- papers, code, datasets, scientific file formats, model outputs, figures, manuscripts, and team decisions -- yet general-purpose AI assistants rarely preserve these objects as a coherent, auditable research state. We present SciForge, a multimodal research-native AI workbench that reserves the graphical interface for human judgment while search, parsing, model routing, workflow execution, plotting, writing, and presentation generation run as modular agent-accessible services. SciForge is built around five pillars: (i) \emph{goal-scoped scientific decision governance} for \textbf{goal-oriented} research, with review gates and shared review surfaces; (ii) \emph{translate-then-reason} for \textbf{multimodal} input, routing scientific objects through domain translators before the agent reasons; (iii) \emph{evidence governance} for \textbf{auditable} traceability, linking claims to provenance chains and audit findings; (iv) \emph{collaborative team science} for \textbf{collaborative} research, enabling multi-role decision governance, with shared team workspaces planned for future releases; and (v) \emph{real-world application scenarios} for \textbf{practical} impact, demonstrated through eight end-to-end user cases, with flagship demonstrations including multi-day agentic research sprints for gene discovery, AI-guided de novo protein design, molecular optimization, and genome-to-BGC discovery. The system combines a thin interaction layer, contextual research capability patterns, an Agent Runtime and Workflow Engine, an Evidence-DAG audit sidecar and a Scientific Model Router. SciForge currently runs as a desktop application, with mobile supervision support; future releases will deepen team collaboration. The system is open-source and available at https://github.com/AGI4Sci/SciForge

</details>

---

### [[20_Research/Papers/大模型/Revisiting_data-driven_dynamic_security_assessment_with_a_tabular_foundation_model|Revisiting data-driven dynamic security assessment with a tabular foundation model]]

![[assets/2607.16031_figure.png|800]]

- **arXiv**: [2607.16031](https://arxiv.org/abs/2607.16031)
- **PDF**: https://arxiv.org/pdf/2607.16031
- **详细分析**: [[20_Research/Papers/大模型/Revisiting_data-driven_dynamic_security_assessment_with_a_tabular_foundation_model|Revisiting data-driven dynamic security assessment with a tabular foundation model]]
- **作者**: Olayiwola Arowolo, Maosheng Yang, Jochen Cremer
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM, Security, Systems

#### 研究背景与动机

《Revisiting data-driven dynamic security assessment with a tabular foundation model》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Data-driven pre-fault dynamic security assessment (DSA) rapidly evaluates the dynamic risk of credible contingencies on a power system using machine learning. Existing approaches face two limitations. First, they require a large labelled database for training, with a separate model trained, tuned, and maintained for each contingency in a potentially long list of credible contingencies. Second, the trained models generalize poorly to unseen contingencies. This work addresses the limitations by using a tabular foundation model (TFM) that assesses stability through in-context learning, requiring no retraining or hyperparameter optimization. A single TFM can assess many contingencies at once, removing the need for one model per classifier. We also characterize when the use of electrical distance coordinates (EDC) as continuous features enables generalization of TFM to unseen contingencies and when they do not, demonstrating how a few labelled samples can reliably improve generalization. Through comprehensive case studies on the IEEE 68-bus system, we show that a single TFM attains an average Macro F1 score of about 90% with only 120 labelled samples per contingency, roughly two orders of magnitude fewer than conventionally assumed, without any model retraining or hyperparameter tuning. For new/unseen contingencies, we show that using just 10 labelled samples of the new contingency with EDC encoding matches the best achievable transfer learning oracle model, which requires fully labelled data and is not deployable in practice. Overall, this initial study paves the way towards developing and deploying foundation models for power system operations, with possible applications across multiple operational tasks.

</details>

---

### [[20_Research/Papers/机器人/DPNeXt_A_Lightweight_Multi-Scale_Feature_Fusion_Framework_for_Efficient_ViT-Based_Multi-Task_Dense_Prediction|DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction]]

![[assets/2607.16012_figure.png|800]]

- **arXiv**: [2607.16012](https://arxiv.org/abs/2607.16012)
- **PDF**: https://arxiv.org/pdf/2607.16012
- **详细分析**: [[20_Research/Papers/机器人/DPNeXt_A_Lightweight_Multi-Scale_Feature_Fusion_Framework_for_Efficient_ViT-Based_Multi-Task_Dense_Prediction|DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction]]
- **作者**: Jehun Kang, Jungha Wang, Youngjun Hwang, David Hyunchul Shim
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PIDNet, RefineNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-Task Learning (MTL) in robotics perception systems supports comprehensive 3D spatial scene understanding by integrating semantic segmentation and depth estimation. While Vision Foundation Models (VFMs) are increasingly adopted as robust feature encoders, existing decoding strategies present a critical bottleneck. To address this, we propose DPNeXt, a streamlined multi-scale feature fusion decoder and efficient alternative to the standard Dense Prediction Transformer (DPT). DPNeXt uses dual depthwise separable inverted bottlenecks to improve frozen VFM utilization through fusion-centric decoding and independent task modularization. To further mitigate negative inductive transfer between tasks, we introduce the Multi-Task Boundary Guidance (MTBG) strategy. Unlike prior boundary-aware methods that add fusion modules or gating, MTBG applies symmetric boundary-focused supervision to encourage geometric consistency without extra annotation or inference cost. Experiments on Cityscapes show that DPNeXt-S outperforms prior state-of-the-art (SOTA) MTL models, while DPNeXt-B further improves the overall performance and achieves the best results among the compared methods. On NYUv2, DPNeXt-B also achieves the best semantic segmentation and depth estimation results among the compared methods while requiring substantially fewer trainable parameters than prior large-scale MTL models. Compared with the standard DPT, DPNeXt-S reduces trainable parameters by 78.6% and achieves the fastest inference speed among the compared models on resource-constrained laptop hardware. The source code, model checkpoints, and a demo video will be made available at https://github.com/kangjehun/DPNeXt.

</details>

---

### [[20_Research/Papers/强化学习/Robustness_of_Reinforcement_Learning-Based_Congestion_Management_in_Low-Voltage_Grids|Robustness of Reinforcement Learning-Based Congestion Management in Low-Voltage Grids]]

![[assets/2607.16004_figure.png|800]]

- **arXiv**: [2607.16004](https://arxiv.org/abs/2607.16004)
- **PDF**: https://arxiv.org/pdf/2607.16004
- **详细分析**: [[20_Research/Papers/强化学习/Robustness_of_Reinforcement_Learning-Based_Congestion_Management_in_Low-Voltage_Grids|Robustness of Reinforcement Learning-Based Congestion Management in Low-Voltage Grids]]
- **作者**: Josef Hoppe, Sarra Bouchkati, Farah Nasr, Jonathan Krapp, Alexander Och, Maximilian Wirth, Jan Schiefelbein-Lach, Oliver Pohl, Andreas Ulbig, Michael T. Schaub
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, ComputerVision, Systems

#### 研究背景与动机

《Robustness of Reinforcement Learning-Based Congestion Management in Low-Voltage Grids》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SimBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Increases in photovoltaic generation, charging of electric vehicles and heat-pump demand challenge operating limits in low-voltage distribution grids. This requires curative curtailment methods that can operate under sparse observability, noisy measurements, and imperfect grid models. Unlike prior end-to-end reinforcement-learning approaches for partially observable curtailment, this work decouples congestion detection and control by combining a random-forest violation pre-classifier with an actor-critic controller, and evaluates its robustness to measurement noise and grid-parameter mismatch. The framework is tested on a real low-voltage grid using synthetic future operating scenarios with low observability and controllability. With accurate grid parameters, the controller reduces total violation magnitude by 98.9%, and this performance remains nearly unchanged under the tested measurement-noise settings. Grid-model mismatch proves to be more challenging, but the controller still mitigates most violations under the tested mismatch assumptions.

</details>

---

### [[20_Research/Papers/大模型/DSWorld_A_Data_Science_World_Model_for_Efficient_Autonomous_Agents|DSWorld: A Data Science World Model for Efficient Autonomous Agents]]

![[assets/2607.15901_figure.png|800]]

- **arXiv**: [2607.15901](https://arxiv.org/abs/2607.15901)
- **PDF**: https://arxiv.org/pdf/2607.15901
- **详细分析**: [[20_Research/Papers/大模型/DSWorld_A_Data_Science_World_Model_for_Efficient_Autonomous_Agents|DSWorld: A Data Science World Model for Efficient Autonomous Agents]]
- **作者**: Zherui Yang, Fan Liu, Hao Liu
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.6（加权：大模型 0.6，强化学习 0.2，世界模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《DSWorld: A Data Science World Model for Efficient Autonomous Agents》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DSWorld, MLE-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite strong capabilities in data understanding and decision-making, autonomous data science agents still heavily rely on trial-and-error workflows that involve expensive computation. This bottleneck motivates models that can anticipate the effects of data science operations before real execution. In this paper, we introduce the concept of Data Science World Model, which model the data science execution environment by predicting environment state transitions conditioned on current workflow states and candidate operations. We further propose DSWorld, a practical framework that combines structured state construction, cost-aware routing, lightweight real execution, and an LLM-based simulator for expensive operations. To support training, we construct an 8K-scale transition trajectory dataset and introduce Reflective World Model Optimization, an error-aware reinforcement learning strategy for improving transition prediction. Experiments show that DSWorld accelerates RL-based agent training by approximately $14\times$ and search-based inference by approximately $3$-$6\times$ while maintaining competitive performance, and outperforms the strongest LLM baseline by 35.6% on transition prediction tasks. The code is available at https://anonymous.4open.science/r/DSWorld.

</details>

---

### [[20_Research/Papers/世界模型/Orbis_2_A_Hierarchical_World_Model_for_Driving|Orbis 2: A Hierarchical World Model for Driving]]

![[assets/2607.15898_figure.png|800]]

- **arXiv**: [2607.15898](https://arxiv.org/abs/2607.15898)
- **PDF**: https://arxiv.org/pdf/2607.15898
- **详细分析**: [[20_Research/Papers/世界模型/Orbis_2_A_Hierarchical_World_Model_for_Driving|Orbis 2: A Hierarchical World Model for Driving]]
- **作者**: Sudhanshu Mittal, Arian Mousakhan, Silvio Galesso, Karim Farid, Jonannes Dienert, Rajat Sahay, Thomas Brox
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: WorldModel, Systems

#### 研究背景与动机

《Orbis 2: A Hierarchical World Model for Driving》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DrivingWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current world models operate at a single level of abstraction, with most prioritizing perceptual fidelity while lacking the spatial reasoning and semantic understanding required for real-world downstream tasks. We present a hierarchical driving world model that factorizes future prediction across two levels operating at distinct temporal and abstraction scales: a high-level predictor that forecasts coarse scene structure over extended temporal horizons, and a low-level generator that produces detailed predictions conditioned on the high-level output. This decomposition yields high perceptual fidelity while also capturing strong spatial and semantic representations. We further show that pretraining with a diffusion forcing objective yields substantially richer internal representations than the standard teacher forcing objective, while teacher forcing -- predicting only the next frame from clean context -- produces more stable autoregressive rollouts. We therefore introduce a generic two-stage training paradigm that pretrains the model with diffusion forcing and fine-tunes with teacher forcing, combining the representational benefits of the former with the rollout stability of the latter. Our approach achieves state-of-the-art results across the standard suite of driving world model evaluations on established benchmarks, including long-horizon generation fidelity, steering responsiveness evaluated on counterfactual scenarios, and internal representation quality. Project page with code, demo, checkpoints and qualitative results: https://lmb-freiburg.github.io/orbis2.github.io/

</details>

---

### [[20_Research/Papers/具身智能/EgoExoMoCap_Distributed_Ego-Exo_Human_Motion_Capture|EgoExoMoCap: Distributed Ego-Exo Human Motion Capture]]

![[assets/2607.15868_figure.png|800]]

- **arXiv**: [2607.15868](https://arxiv.org/abs/2607.15868)
- **PDF**: https://arxiv.org/pdf/2607.15868
- **详细分析**: [[20_Research/Papers/具身智能/EgoExoMoCap_Distributed_Ego-Exo_Human_Motion_Capture|EgoExoMoCap: Distributed Ego-Exo Human Motion Capture]]
- **作者**: Jiaxi Jiang, Bharat Lal Bhatnagar, Nan Yang, Lingni Ma, Sebastian Starke, Robin Kips, Nadine Bertsch, Christian Holz, Federica Bogo
- **cs 子类**: cs.AI, cs.CV, cs.GR, cs.HC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.9，机器人 0.3）
- **关联关键词**: EmbodiedAI, ComputerVision, Systems

#### 研究背景与动机

《EgoExoMoCap: Distributed Ego-Exo Human Motion Capture》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EgoNet, EgoSim, QuestSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human motion capture from head-mounted devices (HMDs) offers a scalable way to acquire real-world human motion and interaction data, which is crucial for applications in embodied AI and VR/AR. Existing approaches focus on either egocentric body tracking, estimating the motion of the subject wearing the device, or exocentric tracking, capturing the movements of people in the wearer's surroundings. So far, these two paradigms have largely been explored in isolation. In this paper, we propose a novel distributed framework that jointly leverages ego- and exocentric multi-modal signals for human motion estimation from HMDs. Unlike traditional motion capture systems requiring bulky multi-camera setups or obtrusive mocap suits, our approach, EgoExoMoCap, is as simple as two (or more) people, each wearing a pair of smart glasses. The method leverages head (plus potentially wrist) tracking signals for accurate estimation of global motion in the 3D world and combines context-aware image features based on DINOv3 to achieve robustness in the presence of noise and occlusions. Extensive experiments on two in-the-wild datasets show that our approach can robustly reconstruct motion even in challenging scenarios.

</details>

---

### [[20_Research/Papers/大模型/Knowledge-Centric_Agents_for_Workflow_Generation|Knowledge-Centric Agents for Workflow Generation]]

![[assets/2607.15845_figure.png|800]]

- **arXiv**: [2607.15845](https://arxiv.org/abs/2607.15845)
- **PDF**: https://arxiv.org/pdf/2607.15845
- **详细分析**: [[20_Research/Papers/大模型/Knowledge-Centric_Agents_for_Workflow_Generation|Knowledge-Centric Agents for Workflow Generation]]
- **作者**: Zhendong Li, Lei Sun, Ruibo Ming, He Zhang, Danda Pani Paudel, Luc Van Gool, Jinjin Gu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Knowledge-Centric Agents for Workflow Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ComfyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Workflow generation in visual creation systems such as ComfyUI demands not only syntactic accuracy but also expert-level reasoning over modular compositions. Existing large language model (LLM) approaches often treat this as a direct text-to-JSON generation task, struggling with structural brittleness and lacking the experiential knowledge required for effective design. We argue that successful workflow generation requires modeling knowledge itself, including its structure, hierarchy, and reasoning dynamics. To this end, we propose a knowledge-centric framework that learns to invert, inject, and infer with knowledge across multiple abstraction levels. We first perform knowledge inversion to distill hierarchical representations, ranging from full pseudo-codes and skeletons to high-level strategies, from large collections of real-world workflows. We then conduct knowledge injection through supervised fine-tuning, teaching the model to reason from task descriptions to strategies and from strategies to executable structures. During inference, the model performs reversible reasoning to synthesize executable workflows, augmented by self-refinement for structural coherence. Extensive experiments demonstrate that our method produces workflows with richer node diversity, more coherent structures, and higher execution success rates than existing systems, establishing a new foundation for knowledge-driven, agentic workflow generation.

</details>

---

### [[20_Research/Papers/大模型/AgentFAIR_A_Multi-Agent_Collaborative_Framework_for_FAIRness_Evaluation_of_Geospatial_Datasets|AgentFAIR: A Multi-Agent Collaborative Framework for FAIRness Evaluation of Geospatial Datasets]]

![[assets/2607.15781_figure.png|800]]

- **arXiv**: [2607.15781](https://arxiv.org/abs/2607.15781)
- **PDF**: https://arxiv.org/pdf/2607.15781
- **详细分析**: [[20_Research/Papers/大模型/AgentFAIR_A_Multi-Agent_Collaborative_Framework_for_FAIRness_Evaluation_of_Geospatial_Datasets|AgentFAIR: A Multi-Agent Collaborative Framework for FAIRness Evaluation of Geospatial Datasets]]
- **作者**: Ming Chen, Pranav Pai
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AgentFAIR: A Multi-Agent Collaborative Framework for FAIRness Evaluation of Geospatial Datasets》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Geospatial datasets support applications from urban planning to climate modeling, yet consistent assessment of FAIR compliance is difficult. Existing evaluators use different rubrics and evidence sources and may fail on JavaScript-rendered pages or repository-specific identifiers. For 50 datasets from 10 repositories, the standard deviation of normalized scores across available tools averages 15.0 percentage points and reaches 30.3 for one dataset. Because these outputs are not equivalent measurements, we use them to characterize disagreement and failure modes, not comparative accuracy. We present AgentFAIR, a multi-agent framework combining structured metadata extraction with 13 sub-principle-specific LLM evaluators. Each produces a 0-3 maturity score, cited evidence, and recommendations; a critic checks evidence and consistency and can request targeted re-evaluation. Mean Findability, Accessibility, Interoperability, and Reusability scores are 79.7%, 70.4%, 45.3%, and 72.0%. Rank correlations with four baseline tools range from 0.31 to 0.61; the FAIR-enough comparison is not statistically significant. On a 10-dataset repeated-run subset, sub-principle agreement averages 89% (standard deviation: 3 percentage points), versus 71% without the critic. A preliminary 15-dataset expert study yields Fleiss' kappa of 0.71 and 82% alignment with expert consensus. API cost is approximately USD 0.054 per dataset. These results support auditability and feasibility, while the limited benchmark, incomplete ablations, and single-model-family validation constrain claims about accuracy and generalization.

</details>

---

### [[20_Research/Papers/大模型/Modularized_Dynamic-Granularity_Video_LLM_for_Multi-Event_Long_Video_Understanding|Modularized Dynamic-Granularity Video LLM for Multi-Event Long Video Understanding]]

![[assets/2607.15778_figure.png|800]]

- **arXiv**: [2607.15778](https://arxiv.org/abs/2607.15778)
- **PDF**: https://arxiv.org/pdf/2607.15778
- **详细分析**: [[20_Research/Papers/大模型/Modularized_Dynamic-Granularity_Video_LLM_for_Multi-Event_Long_Video_Understanding|Modularized Dynamic-Granularity Video LLM for Multi-Event Long Video Understanding]]
- **作者**: Wei Feng, Xin Wang, Yu-Wei Zhan, Yuwei Zhou, Wenwu Zhu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: LLM, RL, ComputerVision

#### 研究背景与动机

《Modularized Dynamic-Granularity Video LLM for Multi-Event Long Video Understanding》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MEventBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video Large Language Models (Video LLMs) have made significant advancements in various video understanding tasks. However, long-video scenarios remain challenging due to the tension between limited visual token budgets and the need to capture multiple key events. Existing approaches typically process long videos in two stages, i.e., i) select keyframes and ii) perform detailed perception, which exhibit limitations: they lack a modular mechanism for adaptive capacity allocation and self-correction, resulting in unreliable modeling. To tackle these challenges, we propose MoD-VLLM, a novel Modularized Dynamic-Granularity Video LLM framework for multi-event long video understanding, which unifies temporal grounding and semantic understanding iteratively and self-reflectively. Specifically, we propose a Positive-Negative Video Segments Grounding module and a Modularized Dynamic-Granularity Reflection module, which form a closed loop to progressively localize the question-related video segments. The grounding module instructs a Video LLM to distinguish relevant from irrelevant video segments based on the video question. The reflection module employs a modularized scheduler that dynamically selects fine-grained encoding for relevant positive segments to capture detailed perception and coarse-grained encoding for negative segments to maintain global context. We further propose a dynamic-granularity reinforcement learning strategy, allowing MoD-VLLM to learn optimal grounding policies and dynamic granularity visual representation jointly. Moreover, we propose MEventBench, a challenging Multi-Event Long Video Benchmark for complex long video reasoning. Extensive experiments on several long video understanding benchmarks and our MEventBench demonstrate that MoD-VLLM significantly outperforms state-of-the-art baselines.

</details>

---

### [[20_Research/Papers/大模型/Debiasing_Text-to-Image_Evaluation_via_Implicit_Cultural_Alignment_Reward_Modeling|Debiasing Text-to-Image Evaluation via Implicit Cultural Alignment Reward Modeling]]

![[assets/2607.15740_figure.png|800]]

- **arXiv**: [2607.15740](https://arxiv.org/abs/2607.15740)
- **PDF**: https://arxiv.org/pdf/2607.15740
- **详细分析**: [[20_Research/Papers/大模型/Debiasing_Text-to-Image_Evaluation_via_Implicit_Cultural_Alignment_Reward_Modeling|Debiasing Text-to-Image Evaluation via Implicit Cultural Alignment Reward Modeling]]
- **作者**: Bo-An Chang, Yu-Chih Chen
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.4，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Debiasing Text-to-Image Evaluation via Implicit Cultural Alignment Reward Modeling》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：T2IEval, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As Text-to-Image (T2I) systems rapidly advance, evaluating the cultural authenticity of synthesized content has become increasingly important for fair and trustworthy generative AI. Existing T2I evaluation metrics and multimodal judges often rely on visual-semantic representations that underrepresent implicit cultural norms, leading to biased preference judgments and the omission of fine-grained cultural cues. In addition, visual question answering (VQA)-based evaluators typically depend on autoregressive text generation, which limits their scalability for real-time reward modeling. To address these limitations, we introduce an Implicit Cultural Alignment Reward Model built upon a lightweight 4.2-billion-parameter Multimodal Large Language Model (MLLM). Our framework integrates an Implicit Cultural Probe with a Skip-connection Cross-Attention (SkipCA) mechanism, enabling late-stage semantic features to directly attend to early-stage visual representations and better preserve culturally salient details. Evaluations on 3,323 challenging and carefully curated image pairs from the CulturalFrames benchmark show that our approach achieves 80.54% pairwise accuracy, with Pearson and Kendall correlation coefficients of 0.546 and 0.377, respectively, outperforming representative vision-language metrics and MLLM-based evaluators. Moreover, by bypassing autoregressive text generation, our model processes each evaluation in 0.21 seconds under our local inference setup, achieving a $10\times$ speedup over standard VQA-based evaluators. These results suggest that the proposed reward model can provide an efficient and culturally aware scalar signal for preference optimization pipelines such as Reinforcement Learning from Human Feedback and Direct Preference Optimization.

</details>

---

### [[20_Research/Papers/大模型/Behavioral_Controllability_of_Agentic_Models_for_Information_Extraction_From_Fixed_Workflows_to_Reflective_Agents|Behavioral Controllability of Agentic Models for Information Extraction: From Fixed Workflows to Reflective Agents]]

![[assets/2607.15715_figure.png|800]]

- **arXiv**: [2607.15715](https://arxiv.org/abs/2607.15715)
- **PDF**: https://arxiv.org/pdf/2607.15715
- **详细分析**: [[20_Research/Papers/大模型/Behavioral_Controllability_of_Agentic_Models_for_Information_Extraction_From_Fixed_Workflows_to_Reflective_Agents|Behavioral Controllability of Agentic Models for Information Extraction: From Fixed Workflows to Reflective Agents]]
- **作者**: Lujia Zhang, Xingzhou Chen, Hongwei Feng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Behavioral Controllability of Agentic Models for Information Extraction: From Fixed Workflows to Reflective Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly used for complex information-extraction tasks, yet it remains unclear whether agentic components such as reflection and memory lead to observable and controllable improvements over fixed LLM workflows. We study this question through conference-paper dataset extraction, where a system must identify datasets mentioned in scholarly PDFs and produce structured records. We compare a fixed workflow baseline with reflective agent variants and specify an optimized agent condition (S2) that extends the same task with richer PDF tools and dynamic tool selection. Our evaluation emphasizes process-level behavior--including tool execution, retries, reflection, memory use, runtime, and failure recovery--while treating extraction coverage and field completeness as secondary outcome measures. The paper characterizes when agentic mechanisms change system behavior, whether these changes improve task completion, and how the observed failure modes motivate an optimized agent design under the same evaluation harness.

</details>

---

### [[20_Research/Papers/大模型/S1-Omni_A_Unified_Multimodal_Reasoning_Model_for_Scientific_Understanding,_Prediction,_and_Generation|S1-Omni: A Unified Multimodal Reasoning Model for Scientific Understanding, Prediction, and Generation]]

![[assets/2607.15686_figure.png|800]]

- **arXiv**: [2607.15686](https://arxiv.org/abs/2607.15686)
- **PDF**: https://arxiv.org/pdf/2607.15686
- **详细分析**: [[20_Research/Papers/大模型/S1-Omni_A_Unified_Multimodal_Reasoning_Model_for_Scientific_Understanding,_Prediction,_and_Generation|S1-Omni: A Unified Multimodal Reasoning Model for Scientific Understanding, Prediction, and Generation]]
- **作者**: Jiahao Zhao, Junyi Liu, Lifeng Xu, Nan Xu, Qingli Wang, Qingxiao Li, Tianle Chen, Xiaoyu Wu, Yawen Zheng, Zikai Wang, Guanming Liu, Hequn Zhou...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《S1-Omni: A Unified Multimodal Reasoning Model for Scientific Understanding, Prediction, and Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Natural-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present S1-Omni, a unified multimodal reasoning model for scientific understanding, prediction, and generation. AI for Science (AI4S) has advanced significantly through domain-specific models, tool-augmented LLMs, and scientific language models. However, model capabilities remain highly fragmented, limiting the joint modeling of heterogeneous data, scientific laws, and expert knowledge. S1-Omni addresses this gap by consolidating these capabilities into a single, coherent scientific reasoning model. The architecture of S1-Omni is built upon three core components: unified representation of scientific data, natural-world knowledge alignment, and decoding for domain-specific tasks. First, S1-Omni maps natural-language instructions and scientific objects, including CIF, SMILES, protein sequences, spectra, and scientific images, into a shared representation space. Second, it incorporates scientific laws and expert knowledge into data construction and training, enabling the model to reason from scientific evidence. Third, it performs task-specific decoding to support a broad range of applications, including property prediction, spectrum-to-molecular generation, protein site and structure prediction, and scientific image generation and editing. S1-Omni is trained on S1-Omni-Corpus, which covers 200 scientific tasks and contains millions of reasoning samples, and is evaluated on over 60 scientific benchmarks. It outperforms GPT-5.5 and Gemini-3.1-Pro on most benchmarks and matches or surpasses domain-specific models on several benchmarks. Overall, S1-Omni provides a practical path toward unified scientific modeling.

</details>

---

### [[20_Research/Papers/大模型/ToolVerse_Unlocking_Massive_Environments_and_Long-Horizon_Tasks_for_Agentic_Reinforcement_Learning|ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning]]

![[assets/2607.15660_figure.png|800]]

- **arXiv**: [2607.15660](https://arxiv.org/abs/2607.15660)
- **PDF**: https://arxiv.org/pdf/2607.15660
- **详细分析**: [[20_Research/Papers/大模型/ToolVerse_Unlocking_Massive_Environments_and_Long-Horizon_Tasks_for_Agentic_Reinforcement_Learning|ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning]]
- **作者**: Shuaiyu Zhou, Fengpeng Yue, Zengjie Hu, Yuanzhe Shen, Chenyang Zhang, feng hong, Cao Liu, Ke Zeng
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.1（加权：大模型 0.3，强化学习 0.6，世界模型 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FTRL, TORL, ToolRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While LLM agents demonstrate strong reasoning abilities in compact and well-defined scenarios, they struggle to maintain robustness and effectiveness when faced with large-scale, diverse, and dynamic real-world environments that demand seamless tool integration. To address this gap, we introduce ToolVerse, a comprehensive framework that scales up agentic RL environments and enables agents to perform complex long-horizon reasoning in Tool-Integrated Reasoning (TIR) tasks. First, ToolVerse automatically builds the massive executable agent training environments from nearly 400 real-world Model Context Protocols (MCPs) that contain about 4500 tools. Second, we propose a task design strategy based on a tool dependency graph, utilizing Dynamic Unlocking Sampling Algorithm to generate long-horizon tasks, and produce GUST (Graph Unlocking Sampling Tasks) dataset. Third, to alleviate the credit assigment problem in long-horizon agentic RL, we propose a fine-grained Turn-Aware Relative Advantage algorithm. We conduct extensive Agentic RL training using ToolVerse and evaluate our framework on serveral agentic benchmarks. Experimental results demonstrate that our framework significantly strengthens LLMs' capabilities in long-horizon tool use, achieving a marked performance boost and showcasing robust reasoning within dynamic environments.

</details>

---

### [[20_Research/Papers/具身智能/IMBench_A_Benchmark_for_Intuitive_Robotic_Manipulation|IMBench: A Benchmark for Intuitive Robotic Manipulation]]

![[assets/2607.15641_first_page.png|800]]

- **arXiv**: [2607.15641](https://arxiv.org/abs/2607.15641)
- **PDF**: https://arxiv.org/pdf/2607.15641
- **详细分析**: [[20_Research/Papers/具身智能/IMBench_A_Benchmark_for_Intuitive_Robotic_Manipulation|IMBench: A Benchmark for Intuitive Robotic Manipulation]]
- **作者**: Anurag Maurya, Sukhvansh Jain, Prajwal Avhad, Gautham Balachandran, Ziyi Zhou, Atharva Kshirsagar, Satyam Singh, Bowen Li. Rishabh Mukund, Ritul Singh, Jatin Vira, Suvonil Chatterjee, Devesh K. Jha
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《IMBench: A Benchmark for Intuitive Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans combine reasoning and motor control to solve complex manipulation tasks under diverse constraints. They build an understanding of the physical world that helps them convert reasoning into actions and quickly adapt to new scenes, tasks, and rules. We refer to this capability as intuitive manipulation. Existing benchmarks fail to capture this integration: they evaluate physical reasoning in isolation from execution, or measure policy performance without requiring explicit reasoning. We introduce IMBENCH, a benchmark designed to evaluate intuitive manipulation as an integrated capability spanning perception, physical reasoning, action generation, and iterative execution. Our tasks require models to infer task-relevant physical structure and generate feasible action sequences under explicit constraints, including contact-rich manipulation, tool use, and multi-stage dependencies. We introduce a benchmark of 35 tasks, 14K filtered trajectories, and scalable tools for generating diverse scenarios. Experiments reveal a consistent gap: vision language models show partial physical reasoning ability but fail to produce executable plans, while state-of-the-art vision-language-action models struggle to satisfy task constraints and generalize across scenarios. These results identify intuitive manipulation as a missing axis in current foundation models and generalist robot policies, and position IMBENCH as a step toward evaluating and enabling more integrated, adaptive physical intelligence.

</details>

---

### [[20_Research/Papers/具身智能/Think_at_5_Hz,_Act_at_20_Hz_Asynchronous_Fast-Slow_Vision-Language-Action_Inference_for_Closed-Loop_Driving|Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving]]

![[assets/2607.15621_figure.png|800]]

- **arXiv**: [2607.15621](https://arxiv.org/abs/2607.15621)
- **PDF**: https://arxiv.org/pdf/2607.15621
- **详细分析**: [[20_Research/Papers/具身智能/Think_at_5_Hz,_Act_at_20_Hz_Asynchronous_Fast-Slow_Vision-Language-Action_Inference_for_Closed-Loop_Driving|Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving]]
- **作者**: Yun Li, Jiachen Gong, Simon Thompson, Ehsan Javanmardi, Qunli Zhang, Zifan Zeng, Shiming Liu, Peng Wang, Zixuan Guo, Manabu Tsukada
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.6（加权：具身智能 1.2，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DriveVLA, ReasonNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models bring instruction following and scene reasoning to end-to-end driving, but their inference latency collides with the control rate a vehicle requires. Existing closed-loop agents hide this gap by invoking the model on alternate simulation ticks and replaying the previous command in between, so half of all control outputs ignore the newest observations. We present a fast-slow architecture that removes this compromise. A frozen 7B vision-language backbone acts as the slow system, digesting navigation instructions and visual history at low frequency while exposing its per-layer key-value cache as a standing representation of the scene. A lightweight action expert acts as the fast system, attending to this cache and to the current camera frame at every simulation tick to regress waypoints in a single forward pass. Since the cache lags behind the world at deployment, we train the expert under randomized staleness, aligning training with asynchronous execution. On LangAuto-Short routes in CARLA, our system produces fresh control at every 50 ms simulation tick and lifts route completion from 37.0 to 94.0 over the frame-skipping baseline. A frame-skip ablation with the same expert separates the two factors at work: the expert raises the driving score on its own, while per-tick freshness raises completion from 82.1 to 94.0 and cuts red-light violations by a third. Trained on a single town, the expert transfers zero-shot to two unseen towns, holding 84-94% route completion where the baseline reaches 31-41%. It reduces open-loop waypoint error by nearly a factor of four compared to the backbone's own action head, at a per-tick model cost of 32 ms that is independent of history length on a single consumer GPU.

</details>

---

### [[20_Research/Papers/大模型/Process_Reward_Informed_Tree_Rollout_for_Effective_Multi-Turn_RL|Process Reward Informed Tree Rollout for Effective Multi-Turn RL]]

![[assets/2607.15610_figure.png|800]]

- **arXiv**: [2607.15610](https://arxiv.org/abs/2607.15610)
- **PDF**: https://arxiv.org/pdf/2607.15610
- **详细分析**: [[20_Research/Papers/大模型/Process_Reward_Informed_Tree_Rollout_for_Effective_Multi-Turn_RL|Process Reward Informed Tree Rollout for Effective Multi-Turn RL]]
- **作者**: Xintong Li, Sha Li, Yuwei Zhang, Changlong Yu, Rongmei Lin, Hongye Jin, Shuyi Guan, Xin Liu, Linwei Li, Qingyu Yin, Jingbo Shang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.17（加权：大模型 0.45，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Process Reward Informed Tree Rollout for Effective Multi-Turn RL》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has become a key approach for training LLM agents, yet popular methods such as GRPO/RLOO rely on multiple independently sampled complete trajectories for advantage estimation. In long-horizon agentic tasks, such a uniform rollout strategy can waste budget on uninformative dead-end attempts, while promising intermediate states do not receive sufficient exploration. The multi-turn structure of agentic trajectories, with interleaved actions and observations, naturally supports organizing a trajectory group as a tree, where each turn serves as a decision point for exploration. This perspective reframes effective exploration as the problem of deciding where to branch. We propose Process-Scorer Guided Adaptive Tree Rollout (PATR), a quality-aware rollout framework for multi-turn agent RL. PATR uses task-appropriate process feedback to score partial trajectories, selectively branches from promising states, reuses shared prefixes, and conservatively stops degenerate paths to reduce wasted sampling. The resulting rollout groups remain compatible with standard policy optimization while providing more efficient exploration under the same training budget. We evaluate PATR on FrozenLake and the challenging SWE-Bench, which is largely unexplored by prior tree-rollout agent RL methods. Experiments show that PATR improves performance by up to +5.0 points on SWE-Bench and +9.3 points on FrozenLake, highlighting process-guided tree rollouts as an effective strategy for scalable multi-turn RL.

</details>

---

### [[20_Research/Papers/大模型/Scalable_LLM_Agent_Tool_Access_in_the_Cloud|Scalable LLM Agent Tool Access in the Cloud]]

![[assets/2607.15593_figure.png|800]]

- **arXiv**: [2607.15593](https://arxiv.org/abs/2607.15593)
- **PDF**: https://arxiv.org/pdf/2607.15593
- **详细分析**: [[20_Research/Papers/大模型/Scalable_LLM_Agent_Tool_Access_in_the_Cloud|Scalable LLM Agent Tool Access in the Cloud]]
- **作者**: Mingxin Li, Enge Song, Yueshang Zuo, Xiaodong Liu, Rong Wen, Qiang Fu, Gianni Antichi, Jian He, Jing Tie, Zhou Shao, Xiaobo Xue, Xiong Xiao...
- **cs 子类**: cs.AI, cs.DC, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Scalable LLM Agent Tool Access in the Cloud》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly rely on tool calling to act on external systems, and the Model Context Protocol (MCP) has quickly become its de facto interface. Operating MCP at cloud scale, however, becomes difficult. On the tool provider side, legacy services are not directly callable through MCP; the rapid protocol development also creates ongoing compatibility cost. On the agent side, the number of accessible tool is limited by the LLM context window and inference overhead; mounting a large tool set increases token usage and inference latency and can reduce task success rate. Moreover, for stateful MCP backends with multiple replicas, preserving session affinity increases client-side complexity. We present a cloud-scale gateway system for MCP service. It breaks the direct-connect model on the data plane and offloads legacy service integration, consolidating incompatible MCP variants, access control, tool recommendation, and session-aware routing to the gateway. Hybrid retrieval sustains 98% Top-15 recall; it scales agent tool access to 3,000+ with high tool selection accuracy, and reduces tool selection time by $8.9\times$ and token usage by $23.8\times$, with low per-call overhead, stable under scale-out. Finally, we share the lessons learned from deploying the gateway system in production.

</details>

---

### [[20_Research/Papers/大模型/MGDT_MLLM-Guided_Diffusion_Transformer_with_Relation-Adaptive_Mixture-of-Experts_for_Multimodal_Knowledge_Graph_Completion|MGDT: MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts for Multimodal Knowledge Graph Completion]]

![[assets/2607.15592_figure.png|800]]

- **arXiv**: [2607.15592](https://arxiv.org/abs/2607.15592)
- **PDF**: https://arxiv.org/pdf/2607.15592
- **详细分析**: [[20_Research/Papers/大模型/MGDT_MLLM-Guided_Diffusion_Transformer_with_Relation-Adaptive_Mixture-of-Experts_for_Multimodal_Knowledge_Graph_Completion|MGDT: MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts for Multimodal Knowledge Graph Completion]]
- **作者**: Xu Hou, Meiyu Liang, Wei Huang, Yawen Li, Zhe Xue, Wu Liu, Guanhua Ye, Lei Shi, Kangkang Lu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《MGDT: MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts for Multimodal Knowledge Graph Completion》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IKRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal Knowledge Graph Completion (MKGC) requires inferring missing entities from structural, textual, and visual cues. Existing diffusion-based MKGC methods usually denoise directly on raw multimodal features. Such a design forces the denoiser to simultaneously perform relation-dependent cue selection, cross-modal semantic alignment, and structure-aware entity generation, which introduces noisy and semantically inconsistent conditions for diffusion and consequently leads to suboptimal completion performance. To address this limitation, we propose MGDT: MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts (MGDT), a novel MKGC framework built on an align-then-diffuse paradigm. MGDT first employs a Relation-Adaptive Semantic Routing Mixture-of-Experts (RASR-MoE) module to select relation-relevant multimodal semantic transformation paths and suppress irrelevant modality interference. MGDT then uses a frozen Multimodal Large Language Model (MLLM) as a semantic anchor to align the routed multimodal representations into a unified latent space and reduce cross-modal semantic heterogeneity. Finally, a Knowledge Graph Diffusion Transformer (KGDT) performs graph-conditioned denoising generation in the aligned space to produce the missing entity representation. Experiments on three benchmark datasets show that MGDT consistently outperforms strong baselines.

</details>

---

### [[20_Research/Papers/具身智能/MemoGuard_An_Adaptive_Runtime_for_Guarding_Against_Memory_Traps_in_Communication-Limited_Robot_Navigation|MemoGuard: An Adaptive Runtime for Guarding Against Memory Traps in Communication-Limited Robot Navigation]]

![[assets/2607.15589_figure.png|800]]

- **arXiv**: [2607.15589](https://arxiv.org/abs/2607.15589)
- **PDF**: https://arxiv.org/pdf/2607.15589
- **详细分析**: [[20_Research/Papers/具身智能/MemoGuard_An_Adaptive_Runtime_for_Guarding_Against_Memory_Traps_in_Communication-Limited_Robot_Navigation|MemoGuard: An Adaptive Runtime for Guarding Against Memory Traps in Communication-Limited Robot Navigation]]
- **作者**: Rajat Bhattacharjya, Hyeonjong Ju, Sing-Yao Wu, Eli Bozorgzadeh, Nikil Dutt
- **cs 子类**: cs.AI, cs.NI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.2，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《MemoGuard: An Adaptive Runtime for Guarding Against Memory Traps in Communication-Limited Robot Navigation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Communication-limited robots in mission-critical scenarios such as disaster inspection and search-and-rescue must make reliable onboard decisions without access to remote operators or high-capacity reasoning services. Episodic memory reuse is an attractive low-cost fallback, but retrieval similarity does not guarantee execution validity, i.e., a retrieved action may match the current context yet be unsafe due to changed topology, insufficient battery margin, or unreliable prior outcomes. We call such high-similarity but execution-invalid episodes memory traps. This creates a safety-efficiency design space where similarity only reuse minimizes fallback cost but can be unsafe, while always invoking local reasoning improves safety at high computational and energy cost. This paper presents MemoGuard, a lightweight adaptive runtime that validates episodic memories against topology, resource, and outcome contracts before reuse, invoking fallback only when validation fails. In a graph-based corridor-inspection simulator, MemoGuard reduces battery safety violations by 76.6% over similarity-only top-1 reuse while reducing fallback calls by 21.4% over always reasoning. On an NVIDIA Jetson AGX Xavier with local llama3.2:3b fallback reasoning, this corresponds to 3.67 s and 36.97 J of avoided fallback-reasoning overhead per trial. We open-source MemoGuard at https://github.com/hetheiin/memoguard.

</details>

---

### [[20_Research/Papers/强化学习/From_Feasibility_to_Desirability_Plan,_Learn,_Adapt_(PLA)_Framework_for_Personalized_On-Device_Itinerary_Generation|From Feasibility to Desirability: Plan, Learn, Adapt (PLA) Framework for Personalized On-Device Itinerary Generation]]

![[assets/2607.15552_figure.png|800]]

- **arXiv**: [2607.15552](https://arxiv.org/abs/2607.15552)
- **PDF**: https://arxiv.org/pdf/2607.15552
- **详细分析**: [[20_Research/Papers/强化学习/From_Feasibility_to_Desirability_Plan,_Learn,_Adapt_(PLA)_Framework_for_Personalized_On-Device_Itinerary_Generation|From Feasibility to Desirability: Plan, Learn, Adapt (PLA) Framework for Personalized On-Device Itinerary Generation]]
- **作者**: Himel Dev, Tanmoy Sen, Madhusudan Basak, Bashima Islam
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《From Feasibility to Desirability: Plan, Learn, Adapt (PLA) Framework for Personalized On-Device Itinerary Generation》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating personalized trip itineraries is a complex planning task and involves a tension between hard combinatorial feasibility and soft latent desirability. Classical optimization enforces constraints but fails to capture subjective traveler preferences. While learning-based approaches model preferences, they cannot guarantee feasibility. Mobile deployment imposes additional resource constraints on both. To address this, we propose Plan, Learn, Adapt (PLA), a three-stage framework for personalized on-device itinerary generation. The Plan stage builds a heterogeneous ensemble of lightweight planners that produces structurally diverse feasible candidates. From pairwise itinerary comparisons, Learn fits a compact Bradley-Terry reward model that captures emergent schedule properties such as pacing, geographic coherence, and day balance, which per-POI signals miss. Finally, Adapt applies feasibility-preserving local refinement within a device-aware compute budget; every intermediate state is feasible by construction. On 2,519 pairwise human comparisons across more than 100 U.S. cities, the reward-guided ensemble achieves a 67.8% win rate, 11.2 percentage points above the best single planner, with 100% feasibility. Three frontier LLMs, GPT-5, Claude Opus 4.5, and Gemini 3 Pro, achieve 0% feasibility under the same constraints. The reward model generalizes across held-out cities, with a 67.6% mean leave-one-city-out accuracy. In production deployment within FlyEnJoy, PLA increased itinerary completion rates by 91%, with 109.9 ms average on-device latency.

</details>

---

### [[20_Research/Papers/世界模型/SeerGuard_A_Safety_Framework_for_Mobile_GUI_Agents_via_World_Model_Prediction|SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction]]

![[assets/2607.15550_figure.png|800]]

- **arXiv**: [2607.15550](https://arxiv.org/abs/2607.15550)
- **PDF**: https://arxiv.org/pdf/2607.15550
- **详细分析**: [[20_Research/Papers/世界模型/SeerGuard_A_Safety_Framework_for_Mobile_GUI_Agents_via_World_Model_Prediction|SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction]]
- **作者**: Xue Yu, Bo Yuan, Pengshuai Yang, Kailin Zhao, Hong Hu, Junlan Feng
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，世界模型 0.8）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DigiRL, MobileSafetyBench, MobileWorld, WebWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile graphical user interface (GUI) agents have demonstrated remarkable capabilities in automating complex tasks, yet they introduce critical safety risks where a single erroneous action can lead to irreversible consequences. Existing safety mechanisms are primarily reactive, lacking the ability to assess risks before execution. In this paper, we introduce SeerGuard, a consequence-aware safety framework designed to mitigate these risks through pre-execution instruction-level screening and action-level risk assessment. Specifically, the action-level assessment analyzes agent-proposed actions within current GUI states, anticipating likely outcomes to identify risks before they are executed. To enable these capabilities, we construct a unified safety-augmented world model (SAWM) via multi-task learning, integrating semantic next-state prediction with safety risk assessment. Extensive experiments demonstrate that SeerGuard generalizes effectively across diverse mobile GUI agents. On Qwen3-VL-8B-Instruct, it increases the safety-utility score from $0.191$ to $0.596$ at $ω=0.8$ and reduces the risk-cost score from $0.347$ to $0.130$ at $α=0.8$. Further analyses on our SAWM validate the effectiveness of the instruction-level screening, alongside the capability of action risk assessment and next-state prediction.

</details>

---

### [[20_Research/Papers/大模型/CoWeaver_A_Bi-directional,_Learnable_and_Explainable_Matching_Engine_for_Mixed_Human-Agent_Science_Collaboration|CoWeaver: A Bi-directional, Learnable and Explainable Matching Engine for Mixed Human-Agent Science Collaboration]]

![[assets/2607.15545_figure.png|800]]

- **arXiv**: [2607.15545](https://arxiv.org/abs/2607.15545)
- **PDF**: https://arxiv.org/pdf/2607.15545
- **详细分析**: [[20_Research/Papers/大模型/CoWeaver_A_Bi-directional,_Learnable_and_Explainable_Matching_Engine_for_Mixed_Human-Agent_Science_Collaboration|CoWeaver: A Bi-directional, Learnable and Explainable Matching Engine for Mixed Human-Agent Science Collaboration]]
- **作者**: Jiayao Gu, Kexin Chu, Peidong Liu, Yue Yang, Lynn Ai, Qi Zhang, Ling Yang, Tianyu Shi
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《CoWeaver: A Bi-directional, Learnable and Explainable Matching Engine for Mixed Human-Agent Science Collaboration》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based agents excel at writing articles, coding and information retrieval. However, they fail to form strong collaborations within the scientific community due to the bidirectional, dynamic nature of the problem and a high demand of decision interpretability. We proposed COWEAVER, a bidirectional, learnable and explainable algorithm to match scientists and form strong collaborations within a human-agent network. COWEAVER matches candidates and requesters through filling capability gaps and filters candidates through a two-stage ranking step. Finally, the model explores newcomers by maintaining uncertainty-aware capability estimates and updating them through requester's feedback. We show that the selection mechanism of combining both exploration (UCB) and greedy of COWEAVER exceeds the greedy-only mechanism - the analytical best solution - on 6 out of the 20 tasks and performed on par with the greedy-only mechanism in terms of selecting the best candidate. We compared COWEAVER baselines in terms of matching quality and efficiency. COWEAVER outperforms baselines on all metrics.

</details>

---

### [[20_Research/Papers/大模型/SLAPBench_Benchmarking_Multimodal_Large_Language_Models_for_Four-Finger_SLAP_Fingerprint_Verification|SLAPBench: Benchmarking Multimodal Large Language Models for Four-Finger SLAP Fingerprint Verification]]

![[assets/2607.15517_figure.png|800]]

- **arXiv**: [2607.15517](https://arxiv.org/abs/2607.15517)
- **PDF**: https://arxiv.org/pdf/2607.15517
- **详细分析**: [[20_Research/Papers/大模型/SLAPBench_Benchmarking_Multimodal_Large_Language_Models_for_Four-Finger_SLAP_Fingerprint_Verification|SLAPBench: Benchmarking Multimodal Large Language Models for Four-Finger SLAP Fingerprint Verification]]
- **作者**: Bibesh Pyakurel, M. G. Sarwar Murshed
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《SLAPBench: Benchmarking Multimodal Large Language Models for Four-Finger SLAP Fingerprint Verification》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FPBench, FaceRecBench, FaceXBench, FingerNet, SLAPBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Four-finger SLAP fingerprints are flat live-scan impressions of the index, middle, ring, and little fingers of one hand, used for identity verification in border control and law enforcement. No benchmark has evaluated whether multimodal large language models (MLLMs) can verify identity from SLAP images. We introduce SLAPBench, the first benchmark for MLLM-based four-finger SLAP fingerprint verification, built from NIST SD302b with 7,832 pairs (176 mated, 7,656 non-mated). We evaluate four open-source MLLMs (InternVL3-8B, Qwen2.5-VL-7B, Qwen3-VL-8B, Gemma-3-12B) and the proprietary Claude Opus 4.8 under zero-shot, task-description, and similarity-scoring prompts. Prompting governs verification behavior. Task-description prompting collapses all four open-source models to near-100% False Accept Rate (FAR), and Gemma-3-12B collapses under zero-shot as well; Claude Opus 4.8 alone resists collapse under both binary prompts, giving the best binary result (FAR = 20.2%). Similarity scoring removes collapse across the open-source models and exposes wide capability gaps: Claude reaches AUC = 0.953 and Gemma-3-12B 0.837, while InternVL3-8B is inverted (AUC = 0.590) and Qwen2.5-VL-7B near random (0.567). Qwen3-VL-8B attains perfect separation (AUC = 1.000), which we treat as a diagnostic rather than as capability: SD302b holds one SLAP capture per finger position, so mated pairs are cross-resolution. A matched-resolution control leaves the perfect score intact, ruling out the resolution shortcut; what cannot be excluded within SD302b is near-duplicate detection, since a mated pair is one capture rendered twice. A fairness probe over gender, race, and age suggests disparity grows as discrimination weakens. SLAPBench establishes the first SLAP-specific MLLM baseline and shows that prompting governs collapse while model capability governs discrimination.

</details>

---

### [[20_Research/Papers/大模型/Cache-Aware_Prompt_Compression_A_Two-Tier_Cost_Model_for_LLM_API_Caching|Cache-Aware Prompt Compression:A Two-Tier Cost Model for LLM API Caching]]

![[assets/2607.15516_figure.png|800]]

- **arXiv**: [2607.15516](https://arxiv.org/abs/2607.15516)
- **PDF**: https://arxiv.org/pdf/2607.15516
- **详细分析**: [[20_Research/Papers/大模型/Cache-Aware_Prompt_Compression_A_Two-Tier_Cost_Model_for_LLM_API_Caching|Cache-Aware Prompt Compression:A Two-Tier Cost Model for LLM API Caching]]
- **作者**: Yan Song
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Cache-Aware Prompt Compression:A Two-Tier Cost Model for LLM API Caching》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：LongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Production LLM deployments combine two cost-reduction primitives: prompt caching (a discounted rate for re-used token prefixes) and prompt compression (fewer tokens sent). The compression literature has standardized on query-aware methods that produce a different compressed prefix per query, mechanically invalidating the prefix-strict cache on every call. We characterize this cost empirically on Anthropic's Sonnet 4.6 API and find caching is far from the rho=1.0 ideal the literature assumes: Sonnet's cache has a two-tier architecture with a sharp threshold near 3,500 tokens, below which the hit rate plateaus at rho~0.83 across 30-call sessions. Our cost model predicts, and experiments confirm, that under realistic rho, query-aware compression beats naive caching at high compression ratios (r&gt;=6). We propose Cache-Aware Prompt Compression (CAPC), pairing query-agnostic compression with explicit cache_control plus a tier-preserving ratio bound that prevents over-compression from pushing the cached prefix into the hot tier. CAPC is the cheapest strategy in 16/16 configurations on LongBench-v2, with mean savings of 49% over cache-only, 64% over query-aware compression, and 90% over vanilla, at quality within 0.05 of the uncompressed baseline. We validate CAPC on three production workloads: an enterprise tool-using assistant with a 94k-token schema prefix (51.7% cost reduction at r=3); a graphify knowledge-graph RAG pipeline across two codebases (9.3x vs cache-all on FastAPI, 2.4x on httpx); and the public tau-bench retail benchmark (50 tasks), where CAPC is the cheapest of four strategies with reward exactly equal to vanilla (both 36/50, p=1.00) while query-aware compression is the most expensive at +40.1% over vanilla -- the first production confirmation of the crossover model's negative-ROI prediction on a public benchmark.

</details>

---

### [[20_Research/Papers/大模型/LLM-Driven_AutoML_for_Cross-Lingual_Handwritten_OCR_Closed-Loop_Neural_Architecture_Search_with_GPT-5,_GPT-4o,_and_Claude_Sonnet_4|LLM-Driven AutoML for Cross-Lingual Handwritten OCR: Closed-Loop Neural Architecture Search with GPT-5, GPT-4o, and Claude Sonnet 4]]

![[assets/2607.15509_figure.png|800]]

- **arXiv**: [2607.15509](https://arxiv.org/abs/2607.15509)
- **PDF**: https://arxiv.org/pdf/2607.15509
- **详细分析**: [[20_Research/Papers/大模型/LLM-Driven_AutoML_for_Cross-Lingual_Handwritten_OCR_Closed-Loop_Neural_Architecture_Search_with_GPT-5,_GPT-4o,_and_Claude_Sonnet_4|LLM-Driven AutoML for Cross-Lingual Handwritten OCR: Closed-Loop Neural Architecture Search with GPT-5, GPT-4o, and Claude Sonnet 4]]
- **作者**: Mobina Kashaniyan, Amirhossein Ghassemi, Nasser Mozayani
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《LLM-Driven AutoML for Cross-Lingual Handwritten OCR: Closed-Loop Neural Architecture Search with GPT-5, GPT-4o, and Claude Sonnet 4》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DenseNet, ImageNet, NAS-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a fully automated closed-loop AutoML framework that uses GPT-5, GPT-4o, and Claude Sonnet 4 as autonomous neural architecture designers for cross-lingual handwritten optical character recognition. Each large language model independently generates, trains, evaluates, and iteratively refines neural network architectures using performance feedback from previous trials. The framework is evaluated on Arabic, Persian, and English handwriting datasets through 270 independent experiments. It consistently discovers accurate and computationally efficient models without manual architecture design, domain-specific preprocessing, or hyperparameter tuning. The generated models achieve mean test accuracies above 93 percent, a best accuracy of 98.1 percent, and inference latency between 41 and 44 milliseconds. The results demonstrate that large language models can function as effective AutoML agents for neural architecture search, enabling scalable, script-adaptive, and reproducible handwriting recognition across languages.

</details>

---

### [[20_Research/Papers/强化学习/From_Black_Box_to_Executable_Logic_Explainable_Reinforcement_Learning_through_Prolog_Expert_Systems|From Black Box to Executable Logic: Explainable Reinforcement Learning through Prolog Expert Systems]]

![[assets/2607.15459_first_page.png|800]]

- **arXiv**: [2607.15459](https://arxiv.org/abs/2607.15459)
- **PDF**: https://arxiv.org/pdf/2607.15459
- **详细分析**: [[20_Research/Papers/强化学习/From_Black_Box_to_Executable_Logic_Explainable_Reinforcement_Learning_through_Prolog_Expert_Systems|From Black Box to Executable Logic: Explainable Reinforcement Learning through Prolog Expert Systems]]
- **作者**: Eduardo C. Garrido-Merchán
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.2（加权：强化学习 1.2）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《From Black Box to Executable Logic: Explainable Reinforcement Learning through Prolog Expert Systems》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A trained deep reinforcement learning policy is a black box, and we ask whether it can be made explainable by rewriting it as an executable logic program that reproduces its behaviour and that a person can read, a logic engine can run, and an optimizer can edit. We present a three-stage post-hoc transformation that extracts a frozen proximal policy optimization teacher, induces an ordered rule list from its decisions in the manner of classical relational learning, and emits the result as a Prolog program whose every decision is executed by an off-the-shelf logic engine; a subsequent expansion stage edits the rule base and accepts an edit only when policy evaluation certifies a return increase. We prove four guarantees. A return-loss bound makes the distilled program a machine-checkable certificate in a finite Markov decision process, and the expansion loop improves monotonically and terminates. For the continuous-observation setting we answer whether the conversion is possible at all: the propositional threshold instantiation converts the network to arbitrary fidelity as the resolution B grows, with disagreement O(1/B) and a return gap that closes at the same rate, and a matching lower bound shows the cost is exponential in the observation dimension for an oblique decision boundary. Empirically, on a two-room key-and-door task with 16,944 reachable states the expanded Prolog program attains exact optimal return in every seed and, in a budget-capped regime, exceeds the stochastic teacher on exact return in ten of ten seeds. On three continuous-control tasks the emitted program substitutes the network, matching the neural teacher within noise on Acrobot with eleven clauses and recovering about 97% of its return on CartPole, while on the finer-control LunarLander it recovers only partially, exactly the ceiling the exponential lower bound predicts.

</details>

---

### [[20_Research/Papers/世界模型/Do_Coding_Agents_Need_Executable_World_Models,_Simplification,_and_Verification_to_Solve_ARC-AGI-3|Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?]]

![[assets/2607.15439_first_page.png|800]]

- **arXiv**: [2607.15439](https://arxiv.org/abs/2607.15439)
- **PDF**: https://arxiv.org/pdf/2607.15439
- **详细分析**: [[20_Research/Papers/世界模型/Do_Coding_Agents_Need_Executable_World_Models,_Simplification,_and_Verification_to_Solve_ARC-AGI-3|Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?]]
- **作者**: Sergey Rodionov
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，世界模型 0.8）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Our previous ARC-AGI-3 agent bundled executable world modeling, scheduled simplification, and exact replay verification, leaving unclear which idea accounted for its performance. We address this attribution question with four nested Codex-based agents: a textual baseline; a flexible-interface executable world model without replay verification; the same executable model with scheduled simplification; and a fixed-interface verification treatment that retains simplification and requires exact reproduction of recorded observations. The main study evaluates all four agents with gpt-5.4 and gpt-5.5 at high and xhigh reasoning effort on the public ARC-AGI-3 games. Exploratory follow-ups evaluate the textual and verification variants with gpt-5.6-sol at xhigh and max. The most robust result is that every agent variant improves with a stronger model and with greater reasoning effort. Within each model-effort setting, differences among variants are smaller than anticipated, while the effects of individual components vary across settings. Requiring a persistent executable deliverable is not universally beneficial: the textual variant outperforms the flexible-interface executable variant in both gpt-5.5 settings. Simplification improves performance in three of the four model-effort settings, with the weakest setting as the only exception. The complete verification treatment ranks first in all four settings, although it uses substantially more resources. In the gpt-5.6-sol follow-up, the verification variant fully solves every public game at both reasoning efforts, achieves about 99% RHAE, and uses fewer than half the total actions of the human baseline. Because the model postdates these games and held-out performance remains untested, this result should be interpreted as saturation of the public set only.

</details>

---

### [[20_Research/Papers/大模型/Large_Language_Models_as_Unified_Multimodal_Learners_for_Clinical_Prediction|Large Language Models as Unified Multimodal Learners for Clinical Prediction]]

![[assets/2607.15380_first_page.png|800]]

- **arXiv**: [2607.15380](https://arxiv.org/abs/2607.15380)
- **PDF**: https://arxiv.org/pdf/2607.15380
- **详细分析**: [[20_Research/Papers/大模型/Large_Language_Models_as_Unified_Multimodal_Learners_for_Clinical_Prediction|Large Language Models as Unified Multimodal Learners for Clinical Prediction]]
- **作者**: Ajay Madhavan Ravichandran, Bilgin Osmandoja, Klemens Budde, Klaus Netter, Tobias Strapatsas, Aljoscha Burchardt, Sebastian Möller, Roland Roller
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《Large Language Models as Unified Multimodal Learners for Clinical Prediction》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Electronic health records combine free-text clinical narratives with structured measurements such as vital signs, laboratory values, and comorbidities. Yet most clinical prediction systems still rely on task-specific fusion architectures, pairing dedicated encoders for each modality with learned combination mechanisms that must be re-engineered for every new task and clinical setting. We propose a simpler alternative: convert all patient data, regardless of modality, into a single natural language sequence and fine-tune a pretrained language model end-to-end, with no architectural modification for fusion. We evaluate this approach across three clinically distinct prediction tasks: in-hospital mortality on MIMIC-III, graft failure prediction using longitudinal data from a German transplant center, and emergency triage classification from ambulance records - comparing encoder-based (ModernBERT) and decoder-based (Llama 3.1, Gemma, DeepSeek-R1-Qwen, Qwen3) fine-tuning against established multimodal baselines and, for graft failure, a gradient boosting model currently used in clinical practice for post-transplant patient management. Across all three tasks, unified textual serialization matches or exceeds task-specific multimodal baselines, and outperforms the clinically deployed gradient boosting system on graft failure prediction. These results indicate that a single serialization-based paradigm, without bespoke fusion architectures, is sufficient for multimodal clinical prediction - substantially reducing system complexity while matching or exceeding specialized designs.

</details>

---

### [[20_Research/Papers/大模型/AnovaX_A_Local,_Multi-Agent_Voice_Assistant_with_LLM_Planning,_Typed_Executors,_and_Adaptive_Recovery|AnovaX: A Local, Multi-Agent Voice Assistant with LLM Planning, Typed Executors, and Adaptive Recovery]]

![[assets/2607.15367_first_page.png|800]]

- **arXiv**: [2607.15367](https://arxiv.org/abs/2607.15367)
- **PDF**: https://arxiv.org/pdf/2607.15367
- **详细分析**: [[20_Research/Papers/大模型/AnovaX_A_Local,_Multi-Agent_Voice_Assistant_with_LLM_Planning,_Typed_Executors,_and_Adaptive_Recovery|AnovaX: A Local, Multi-Agent Voice Assistant with LLM Planning, Typed Executors, and Adaptive Recovery]]
- **作者**: Raunak B Sinha
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《AnovaX: A Local, Multi-Agent Voice Assistant with LLM Planning, Typed Executors, and Adaptive Recovery》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Desktop voice assistants are still dominated by cloud pipelines that ship raw audio off the machine and expose a fixed set of skills. We describe AnovaX, a small local-first assistant that runs entirely on the user's computer and treats the desktop itself as its action surface. A single Python process wires together a wake-word gate, a speech pipeline, an LLM planner (Gemini) that emits a JSON plan of tool calls, a whitelist-and-denylist safety layer, a multi-agent orchestrator that translates each plan into typed child agents on a bounded thread pool, and an adaptive recovery loop that takes over whenever a core step fails. Every tool corresponds to a specialized agent class (AppAgent, TypingAgent, BrowserAgent and six others) with its own timeout, retry policy, and shared-resource locks. A recursive MetaAgent lets the planner delegate a sub-goal back to itself, capped at two levels of nesting. The recovery loop uses a compact ReAct-style prompt and hides Gemini's latency behind speculative execution of read-only tools. A companion Flask server exposes a phone-friendly remote over the local WiFi, mirrors every agent lifecycle event to the phone in real time, and streams the laptop's screen back over MJPEG so the user can watch remote commands land as they run. The point of the project is less to compete with Siri or Alexa than to show that a legible, few-thousand-line assistant is enough to open apps, type into them, run searches, coordinate concurrent actions, recover from single-step failures, and be driven entirely from a phone in another room -- without the LLM ever touching the keyboard.

</details>

---

### [[20_Research/Papers/大模型/GraphDx_A_Cost-Aware_Knowledge-Enhanced_Multi-Agent_Framework_for_Sequential_Diagnosis|GraphDx: A Cost-Aware Knowledge-Enhanced Multi-Agent Framework for Sequential Diagnosis]]

![[assets/2607.15280_figure.png|800]]

- **arXiv**: [2607.15280](https://arxiv.org/abs/2607.15280)
- **PDF**: https://arxiv.org/pdf/2607.15280
- **详细分析**: [[20_Research/Papers/大模型/GraphDx_A_Cost-Aware_Knowledge-Enhanced_Multi-Agent_Framework_for_Sequential_Diagnosis|GraphDx: A Cost-Aware Knowledge-Enhanced Multi-Agent Framework for Sequential Diagnosis]]
- **作者**: Shaoting Tan, Ning Liu, Yuntao Du, Shuyue Wei, Wu Shuai, Qian Li, Yanyu Xu, Wei Zhang, Lizhen Cui, Haitao Yuan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《GraphDx: A Cost-Aware Knowledge-Enhanced Multi-Agent Framework for Sequential Diagnosis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ClinicSim, DiagGym, MedQA, Open-Set, SDBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sequential diagnosis requires balancing diagnostic accuracy against resource costs through iterative information gathering. Existing Large Language Model (LLM) approaches exhibit a critical knowledge-reasoning gap: despite encoding extensive medical knowledge, they struggle to reason systematically under cost constraints, often resorting to excessive testing. We propose GraphDx, a knowledge-enhanced framework with two core innovations. First, we design an automated pipeline that leverages LLMs to construct Medical Diagnosis Knowledge Graphs (MDKGs) with quantized typicality, action-centric topology, and dual-objective attributes for both diagnostic relevance and cost-sensitivity. Second, we introduce three collaborative agents (Perception, Reasoning, and Decision) where the Perception and Decision Agents handle language understanding and generation, while the Reasoning Agent performs deterministic evidence scoring and cost-aware planning on the MDKG. Experiments on MedQA and MIMIC-IV across three LLM backbones (DeepSeek-V3, Kimi-k2, Llama-3.3) show that GraphDx improves diagnostic success rates from 50--68% to 79--93% while reducing test costs by 20--54%, providing a robust, economical, and interpretable solution for automated clinical diagnosis.

</details>

---
