# cs.AI | Artificial Intelligence | 2026-07-17

#arxiv #ComputerScience

**论文数**: 44

### [[20_Research/Papers/具身智能/RoboTTT_Context_Scaling_for_Robot_Policies|RoboTTT: Context Scaling for Robot Policies]]

![[assets/2607.15275_figure.png|800]]

- **arXiv**: [2607.15275](https://arxiv.org/abs/2607.15275)
- **PDF**: https://arxiv.org/pdf/2607.15275
- **详细分析**: [[20_Research/Papers/具身智能/RoboTTT_Context_Scaling_for_Robot_Policies|RoboTTT: Context Scaling for Robot Policies]]
- **作者**: Yunfan Jiang, Yevgen Chebotar, Ruijie Zheng, Fengyuan Hu, Yunhao Ge, Jimmy Wu, Tianyuan Dai, Scott Reed, Li Fei-Fei, Yuke Zhu, Linxi "Jim" Fan
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RoboTTT: Context Scaling for Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent robot foundation models operate with single-step or short-history visuomotor context. We introduce Test-Time-Training Robot Policies (RoboTTT), a robot model and training recipe that scale visuomotor context to 8K timesteps, three orders of magnitude beyond state-of-the-art policies, without growing inference latency. At this context length, we unlock new robot capabilities: one-shot in-context imitation from human video demonstrations, on-the-fly policy improvement, robustness to perturbations, and stronger performance on multi-stage, long-horizon tasks. We also observe, for the first time, steady gains in closed-loop performance as pretraining context length scales. At its core, RoboTTT integrates Test-Time Training into robot foundation models such as Vision-Language-Action policies, yielding a sequence model whose recurrent state consists of fast weights, parameters updated by gradient descent during both training and inference, compressing histories into weight space and retrieving contextual information for long-context conditioning. To scale training context length, the recipe combines sequence action forcing with truncated backpropagation through time. On challenging real-robot manipulation tasks, RoboTTT improves overall performance by 87% over the single-step context baseline and fully completes a five-minute, ten-stage assembly task, which no baseline ever does. RoboTTT trained with 8K-timestep context outperforms the same model pretrained with 1K timesteps by 62%, suggesting context length as a new scaling axis for robot foundation models. Videos are available at https://research.nvidia.com/labs/gear/robottt/

</details>

---

### [[20_Research/Papers/强化学习/Mask-Aware_Policy_Gradients_for_Diffusion_Language_Models|Mask-Aware Policy Gradients for Diffusion Language Models]]

![[assets/2607.15200_figure.png|800]]

- **arXiv**: [2607.15200](https://arxiv.org/abs/2607.15200)
- **PDF**: https://arxiv.org/pdf/2607.15200
- **详细分析**: [[20_Research/Papers/强化学习/Mask-Aware_Policy_Gradients_for_Diffusion_Language_Models|Mask-Aware Policy Gradients for Diffusion Language Models]]
- **作者**: Haran Raajesh, Kulin Shah, Adam Klivans, Philipp Krähenbühl
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Mask-Aware Policy Gradients for Diffusion Language Models》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has proven effective for improving reasoning in large language models, but extending it to Masked Diffusion Language Models (MDLMs) remains challenging due to the intractability of the log-likelihood estimation. Existing approaches approximate this log-likelihood by modeling only the token predictions, ignoring the order in which positions are unmasked during generation. We observe that MDLM generation involves two decisions at each step: what tokens to place at each masked position and which positions to remask. We formalize this as a two-stage action MDP, showing that the policy gradient naturally decomposes into a token term and a masking term. Combining optimization of both terms leads to state-of-the-art outcomes on mathematical reasoning and coding benchmarks, with scores of 87.1% on GSM8K and 53.4% on MBPP.

</details>

---

### [[20_Research/Papers/大模型/Benchmarking_Multimodal_Large_Language_Models_for_Scientific_Visualization_Literacy|Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy]]

![[assets/2607.15176_figure.png|800]]

- **arXiv**: [2607.15176](https://arxiv.org/abs/2607.15176)
- **PDF**: https://arxiv.org/pdf/2607.15176
- **详细分析**: [[20_Research/Papers/大模型/Benchmarking_Multimodal_Large_Language_Models_for_Scientific_Visualization_Literacy|Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy]]
- **作者**: Patrick Phuoc Do, Chau M. Ta, Chaoli Wang
- **cs 子类**: cs.AI, cs.CL, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ChartQA, DVQA, FigureQA, MultiChartQA, PlotQA, SPIQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) are increasingly used to interpret visualizations, yet current evaluations remain largely chart-centric and provide limited evidence of understanding of scientific visualization (SciVis). We benchmark six MLLMs on the scientific visualization literacy assessment test, a standardized SciVis literacy assessment comprising 49 items based on 18 scientific visualizations and illustrations, spanning 8 techniques and 11 task types. We evaluate three closed-source and three open-source models under a closed-world protocol and compare their performance using data from 485 human participants. Results show that current MLLMs do not exhibit uniform SciVis literacy. Gemini is the strongest model overall, exceeding the human mean across the evaluated subsets, whereas the open-source models remain below the human baseline. Performance is highly uneven across techniques and tasks: models perform best on scientific illustration, search, and spatial understanding, but struggle on texture-based and integration-based visualizations and on quantitative estimation. Error analysis reveals recurring failures in fine-grained quantitative estimation, flow-direction interpretation, and grounded encoding interpretation. These findings position SciVis literacy as a necessary benchmark dimension for evaluating multimodal AI systems. Our code and model outputs are publicly available at https://github.com/patdmp/mllm-scivis-lit-benchmark.

</details>

---

### [[20_Research/Papers/具身智能/Scaling_Behavior_Foundation_Model_for_Humanoid_Robots|Scaling Behavior Foundation Model for Humanoid Robots]]

![[assets/2607.15163_first_page.png|800]]

- **arXiv**: [2607.15163](https://arxiv.org/abs/2607.15163)
- **PDF**: https://arxiv.org/pdf/2607.15163
- **详细分析**: [[20_Research/Papers/具身智能/Scaling_Behavior_Foundation_Model_for_Humanoid_Robots|Scaling Behavior Foundation Model for Humanoid Robots]]
- **作者**: Weishuai Zeng, Kangning Yin, Xiaojie Niu, Shunlin Lu, Weixiang Zhong, Jiahe Chen, Feiyu Jia, Xiao Chen, Zirui Wang, Furui Xu, Ming Zhou, Kailin Li...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 1.8，大模型 0.4，机器人 1.1）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Scaling Behavior Foundation Model for Humanoid Robots》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid control requires natural whole-body coordination, precise real-time responses to control signals, and robust generalization across diverse environmental contexts, making it a cornerstone for generalist embodied agents. Behavior Foundation Models (BFMs) have recently emerged as a promising solution to address these challenges by leveraging large-scale behavioral data to achieve superior expressiveness, versatility and generalization. However, despite growing interest in scaling BFMs to further improve their capabilities, it remains unclear how key factors, including the learning paradigm, behavioral data and model architecture should be coordinated to enable effective scaling. In this work, we revisit the scaling recipe for BFMs and demonstrate that substantial performance gains can be achieved through the coordination of three core components: 1) the learning paradigm of motion tracking that reformulates diverse humanoid control problems as the reproduction of integrated whole-body behaviors in the global frame; 2) the strategic synergy between on-policy rollout quantity and reference motion diversity; and 3) the expressive and scalable model architecture termed Humanoid Transformer that facilitates the natural emergence of structured behavioral representations. Through extensive experiments in both simulation and real-world deployment, we demonstrate that our approach yields significant improvements in control fidelity and task generalization, reducing Mean Per-Keypoint Position Error (MPKPE) on the test set by over 10% in local mode and 82% in global mode compared with existing humanoid controllers. These results establish BFM as a principled and effective foundation for scalable and general-purpose humanoid control.

</details>

---

### [[20_Research/Papers/强化学习/Concept-Guided_Spatial_Regularization_for_World_Models_in_Atari_Pong|Concept-Guided Spatial Regularization for World Models in Atari Pong]]

![[assets/2607.15142_figure.png|800]]

- **arXiv**: [2607.15142](https://arxiv.org/abs/2607.15142)
- **PDF**: https://arxiv.org/pdf/2607.15142
- **详细分析**: [[20_Research/Papers/强化学习/Concept-Guided_Spatial_Regularization_for_World_Models_in_Atari_Pong|Concept-Guided Spatial Regularization for World Models in Atari Pong]]
- **作者**: Yukuan Lu, Zaishuo Xia, Weyl Lu, Yubei Chen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.92（加权：大模型 0.2，强化学习 0.36，世界模型 1.36）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Concept-Guided Spatial Regularization for World Models in Atari Pong》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MBRL, MoSim, RetNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are usually evaluated as components of model-based reinforcement learning (MBRL) systems, while the world models themselves are rarely studied in isolation. We examine five representative visual world-model agents in Atari Pong: DreamerV3, DIAMOND, TWISTER, Simulus, and STORM. After reproducing their training pipelines and matching the reported agent performance, we freeze the learned world models and evaluate them with a closed-loop rollout diagnostic: a policy trained separately from the corresponding MBRL agent interacts with each frozen model, and the generated video trajectories are inspected for visual and dynamical errors. Across all five models, the rollouts contain clear failures, including ball disappearance, incorrect ball motion, and invalid ball-paddle interactions. Beyond visual trajectories, we further evaluate them with pixel-space zero-shot MBRL, where a new policy is trained entirely inside a frozen world model and then evaluated in the real environment. Across all five models, the resulting policies substantially underperform those produced by the corresponding original MBRL training pipelines. The gap is particularly large for DreamerV3, whose mean return drops from -5.5 to -20.9, near the minimum Pong return of -21. We hypothesize that insufficient modeling of task-critical concepts, such as the ball in Pong, may contribute to these failures. We therefore propose Concept-Guided Spatial Regularization (CGSReg), an auxiliary pixel reconstruction loss applied to segmented concept regions. Experiments show that CGSReg improves both closed-loop rollouts and pixel-space zero-shot MBRL in DreamerV3, DIAMOND, and TWISTER. Its effects vary across the remaining models and evaluation metrics, indicating that CGSReg alone does not address all world-model bottlenecks.

</details>

---

### [[20_Research/Papers/大模型/Digital_Pantheon_Simulating_and_Auditing_Coalition_Formation_with_LLM_Agents|Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents]]

![[assets/2607.15095_figure.png|800]]

- **arXiv**: [2607.15095](https://arxiv.org/abs/2607.15095)
- **PDF**: https://arxiv.org/pdf/2607.15095
- **详细分析**: [[20_Research/Papers/大模型/Digital_Pantheon_Simulating_and_Auditing_Coalition_Formation_with_LLM_Agents|Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents]]
- **作者**: Dylan Van Mulders, Matthias Bogaert, Dirk Van den Poel
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.35（加权：大模型 1.15，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, UNBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The formation of political coalitions is a complex negotiation driven by both concrete policy objectives and deep-seated ideological convictions. While Large Language Models (LLMs) open new avenues for computational political science, the neutrality and helpfulness biases instilled by Reinforcement Learning from Human Feedback (RLHF) prevent them from sustaining steadfast partisan behaviour. We present a multi-agent framework that reconciles factual grounding with ideological alignment by combining Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and Retrieval-Augmented Generation (RAG): DPO instils aggressive party-specific personas, while a per-party RAG pipeline keeps each agent bounded to its official manifesto. We operationalize the framework on the 2019 Flemish election, deploying the partisan agents in a hub-and-spoke negotiation arbitrated by a formateur. To make the emergent negotiation interpretable, we introduce a Multi-Layered Information Lineage Topology (MILT) that traces every clause in the final agreement back to its manifesto origin and classifies it into five provenance states, a Coalition Influence Score (CIS) that aggregates these traceable contributions to identify which party shaped the agreement, and a real-world grounding pass that benchmarks each simulated provision against the historically adopted coalition agreement. Across three independent simulations the framework yields a stable winner and ranking (N-VA ahead of CD\&amp;V and Open Vld), and manifesto-anchored lineage reliably predicts real-world materialization whereas hallucinated content does not. The result is a transparent, scalable testbed for the ex-ante exploration of party compatibility and formateur-mediated compromise.

</details>

---

### [[20_Research/Papers/强化学习/SMC-ES_Automated_synthesis_of_formally_verified_control_policies|SMC-ES: Automated synthesis of formally verified control policies]]

![[assets/2607.15003_figure.png|800]]

- **arXiv**: [2607.15003](https://arxiv.org/abs/2607.15003)
- **PDF**: https://arxiv.org/pdf/2607.15003
- **详细分析**: [[20_Research/Papers/强化学习/SMC-ES_Automated_synthesis_of_formally_verified_control_policies|SMC-ES: Automated synthesis of formally verified control policies]]
- **作者**: Riccardo Curcio, Toni Mancini, Enrico Tronci
- **cs 子类**: cs.AI, cs.LG, cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《SMC-ES: Automated synthesis of formally verified control policies》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, Safe-DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The deployment of autonomous cyber-physical systems in safety-critical environments requires closed-loop control strategies (i.e., policies) that are not only performant but also provably safe and robust. While learning-based methodologies such as Reinforcement Learning offer flexible and scalable approaches to automatically synthesize such controllers, they typically lack the formal guarantees necessary for safe deployment. To bridge this gap, we propose a novel simulation-based methodology to automatically synthesize policies with formal guarantees regarding performance, safety, and robustness specifications. Specifically, given a set of properties to verify, a confidence parameter $δ$ and an allowable failure probability $\varepsilon$, our method guarantees that the synthesized policy comes with a certificate: with confidence at least $1 - δ$, the probability of encountering a scenario where the given properties are violated is at most $\varepsilon$. We demonstrate the feasibility of our approach by developing SMC-ES, an algorithm that integrates Evolutionary Strategies with Statistical Model Checking-based verification. We evaluate SMC-ES on a suite of continuous control tasks using Gymnasium and Safety Gymnasium testbeds. Results show that, at the price of a sustainable increase in computational cost, our algorithm provides formal guarantees regarding performance, safety, and robustness specifications, while performing competitively against leading model-free Deep Reinforcement Learning (DRL) and Safe-DRL baselines.

</details>

---

### [[20_Research/Papers/强化学习/Multi-Axis_Max@K_Reinforcement_Learning_for_Representative_Diversity_in_Text-to-Image_Generation|Multi-Axis Max@K Reinforcement Learning for Representative Diversity in Text-to-Image Generation]]

![[assets/2607.14962_figure.png|800]]

- **arXiv**: [2607.14962](https://arxiv.org/abs/2607.14962)
- **PDF**: https://arxiv.org/pdf/2607.14962
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Axis_Max@K_Reinforcement_Learning_for_Representative_Diversity_in_Text-to-Image_Generation|Multi-Axis Max@K Reinforcement Learning for Representative Diversity in Text-to-Image Generation]]
- **作者**: Ku Onoda, Paavo Parmas, Hiroki Furuta, Soichiro Nishimori, Yuta Oshima, Shohei Taniguchi, Yutaka Matsuo
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Multi-Axis Max@K Reinforcement Learning for Representative Diversity in Text-to-Image Generation》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Text-to-image (T2I) models can synthesize realistic, prompt-aligned images, yet samples generated for the same prompt often cover only a small subset of visually distinct modes. This limits the diversity of images, and for person-centric prompts, can reflect or amplify demographic skew. We formalize this problem as coverage of a predefined set of semantically specified modes, which we call target-mode coverage. We then propose multi-axis max@K, a group-based reinforcement learning objective for improving such coverage in diffusion-based T2I models. Given a group of samples and one score per target category, multi-axis max@K first takes the maximum score across samples for each category and then sums these category-wise maxima. The resulting credit assignment gives a sample positive weight on a category only when it increases that category's group-wise maximum, allowing different samples to contribute to different categories. We first validate the credit-assignment mechanism on a synthetic mixture and on SD3.5-M using deterministic pixel-based color rewards. We then evaluate the same objective on perceived-appearance fairness. Across three automatic evaluators on held-out prompts, multi-axis max@K improves the Fairness Score by 0.23-0.36 relative to the base model, while maintaining image quality and text alignment.

</details>

---

### [[20_Research/Papers/大模型/StructureClaw_Traceable_LLM_Agents_and_an_Executable_Benchmark_for_Structural_Engineering_Workflows|StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural Engineering Workflows]]

![[assets/2607.14896_figure.png|800]]

- **arXiv**: [2607.14896](https://arxiv.org/abs/2607.14896)
- **PDF**: https://arxiv.org/pdf/2607.14896
- **详细分析**: [[20_Research/Papers/大模型/StructureClaw_Traceable_LLM_Agents_and_an_Executable_Benchmark_for_Structural_Engineering_Workflows|StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural Engineering Workflows]]
- **作者**: Sizhong Qin, Yi Gu, Yao Jiang, Ao Cai, Changjian Zhou, Shaoxuan Shuai, Jiachang Wang, Tianhao Shen, Yueqiang Li, Xinhao Li, Li Zeng, Yueshi Chen...
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural Engineering Workflows》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：AEC-Bench, AECBench, AECV-Bench, AgentBench, DrafterBench, OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Addressing a structural-engineering request requires more than a single answer; it requires a chain of interdependent artifacts: interpreted requirements, a computable model, validation records, solver outputs, code-check records, and a final report. Evaluations centered on question answering or script generation rarely verify this complete evidence chain and may therefore reward fluent outputs even when the underlying engineering workflow is incomplete, internally inconsistent, or non-executable. To address this limitation, we present StructureClaw, an artifact-centered workbench in which LLM agents operate through governed engineering skills, typed tools, shared artifact state, and local analysis backends. We also introduce StructureClaw-Bench, an executable benchmark of 150 controlled scenarios spanning standard workflow execution, interactive robustness, and multimodal structural-model reconstruction. A scenario succeeds only when all required artifact- and execution-level assertions pass in a single run. Across ten agent-model configurations, each evaluated on the same 50 standard cases, the average Success Rate rises from 56.8% with the generic-skill baseline to 88.6% with the full automatic workflow. The interactive and multimodal evaluations identify two prominent remaining challenges: safe handling of invalid numerical inputs and fixture-consistent reconstruction of structural models. These findings show that artifact-centered evaluation can expose workflow-level failures that are difficult to identify from final responses alone, providing a more rigorous basis for evaluating and improving structural-engineering agents. The code and benchmark are available at https://github.com/structureclaw/structureclaw.

</details>

---

### [[20_Research/Papers/机器人/Interventional_Causal_Circuits_for_Safe_Robot_Action_Testing_and_Failure_Recovery|Interventional Causal Circuits for Safe Robot Action Testing and Failure Recovery]]

![[assets/2607.14826_figure.png|800]]

- **arXiv**: [2607.14826](https://arxiv.org/abs/2607.14826)
- **PDF**: https://arxiv.org/pdf/2607.14826
- **详细分析**: [[20_Research/Papers/机器人/Interventional_Causal_Circuits_for_Safe_Robot_Action_Testing_and_Failure_Recovery|Interventional Causal Circuits for Safe Robot Action Testing and Failure Recovery]]
- **作者**: Naren Vasantakumaar, Tom Schierenbeck, Michael Beetz
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Interventional Causal Circuits for Safe Robot Action Testing and Failure Recovery》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe physical AI for robot actions are required not only likely to succeed but tested to be safe before execution. In practice, however, formal testing of motion parameters is computationally expensive, and the cost scales poorly with the dimensionality of the action space. When a proposed action is rejected by a tester, the naive response is to resample blindly until a passing candidate is found. This is wasteful, uninformative, and offers no convergence. We argue that rejection should instead trigger causal diagnosis: a principled identification of which action parameter caused the failure and what corrective value maximises the probability of passing testing under the interventional probability distribution. We propose a closed-loop framework that couples a Joint Probability Tree (JPT) with a Causal Circuit derived from a Marginal-Deterministic Variable Tree, enabling exact polytime computation without retraining, or additional data collection. The framework validates tractability of all interventional queries before the robot begins operating, and out-of-support candidates are detected and excluded from correction automatically. We perform experiments in a ROS2 simulation environment, and the framework demonstrates complementary roles across quality of distribution: under a high-quality JPT, the Causal Circuit reduces failed attempts by 10.3% and under a degraded JPT, it reduces total failed attempts by 37%. Every rejected plan produces a structured, interpretable causal report naming the primary cause variable, its observed value, and the recommended corrective region, supporting operator oversight and autonomous recovery without a separately trained failure model.

</details>

---

### [[20_Research/Papers/具身智能/FoMoVLA_Bridging_Visual_Foresight_and_Motion_Guidance_for_Vision-Language-Action_Models|FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models]]

![[assets/2607.14739_figure.jpg|800]]

- **arXiv**: [2607.14739](https://arxiv.org/abs/2607.14739)
- **PDF**: https://arxiv.org/pdf/2607.14739
- **详细分析**: [[20_Research/Papers/具身智能/FoMoVLA_Bridging_Visual_Foresight_and_Motion_Guidance_for_Vision-Language-Action_Models|FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models]]
- **作者**: Wei Li, Peijin Jia, Yuan Ma, Xuefeng Jiang, Titong Jiang, Sheng Sun, Yujian Li, Xin Wen, Han Hong, Zhikang Liu, Bailin Li, Kun Zhan
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FlowVLA, FoMoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have achieved impressive results in visuomotor policy learning, yet remain fundamentally reactive, mapping current observations and language to actions without explicit forward prediction of world dynamics. Existing visual foresight methods predict future visual states but lack explicit motion guidance: they show where to go but not how to get there. We argue that future feature prediction and sparse point tracking are naturally complementary: the former provides the goal state, while the latter captures the continuous motion path toward it. We propose FoMoVLA, a framework that augments VLA representations with explicit spatio-temporal supervision by jointly learning future feature foresight and sparse 2D point tracking, enhancing the continuous action policy. FoMoVLA introduces compact foresight tokens to decode future feature states, decodes sparse temporal 2D point trajectories to model compact geometric motion, and couples both through a lightweight future-conditioned cross-attention module that enables consistent reasoning between anticipated states and point dynamics. Extensive experiments on LIBERO, RoboCasa GR-1 Tabletop, and LIBERO-Plus demonstrate state-of-the-art performance and strong zero-shot generalization. Project page is available at https://liauto-research.github.io/FoMoVLA.

</details>

---

### [[20_Research/Papers/大模型/Stop_Thinking,_Start_Looking_Efficient_Post-Training_for_Multimodal_Document_Question_Answering_via_Reasoning-Free_Alignment|Stop Thinking, Start Looking: Efficient Post-Training for Multimodal Document Question Answering via Reasoning-Free Alignment]]

![[assets/2607.14682_figure.png|800]]

- **arXiv**: [2607.14682](https://arxiv.org/abs/2607.14682)
- **PDF**: https://arxiv.org/pdf/2607.14682
- **详细分析**: [[20_Research/Papers/大模型/Stop_Thinking,_Start_Looking_Efficient_Post-Training_for_Multimodal_Document_Question_Answering_via_Reasoning-Free_Alignment|Stop Thinking, Start Looking: Efficient Post-Training for Multimodal Document Question Answering via Reasoning-Free Alignment]]
- **作者**: Harikrishnan P M, Goutham Vignesh, Ganesh Parab, Saisubramaniam Gopalakrishnan, Vishal Vaddina, Varun V, Rohit Agrawal
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.27（加权：大模型 0.55，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Stop Thinking, Start Looking: Efficient Post-Training for Multimodal Document Question Answering via Reasoning-Free Alignment》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Efficient multimodal document question answering with explicit visual grounding, locating the precise document region that supports each answer remains an open challenge. Current approaches bifurcate into Supervised Fine-Tuning (SFT), which requires large annotated datasets and reaches optimization plateaus, and reasoning-centric Reinforcement Learning (RL), which depends on verbose intermediate traces that inflate inference token cost without clear benefit. We introduce Perception-RFT, a training framework that applies Group Relative Policy Optimization (GRPO) to multimodal document QA, bypassing intermediate reasoning tokens to directly align visual features with structured grounding outputs. To rigorously evaluate the necessity of reasoning, we construct a reasoning variant under identical reward settings. We find that reasoning-enabled models suppress their reasoning traces during training, converging to direct perception-based policies at the 4B parameter scale, reducing per-query inference token length by more than 60%, while reasoning-enabled RL underperforms perception-only training. Through a fine-grained analysis of Qwen3-VL-4B optimization dynamics, we confirm that SFT saturation and cold-start RL instability established in text-domain post-training extend to multimodal, and identify a previously uncharacterized Grounding Divergence: a selective trade-off between semantic robustness and geometric precision on two out of distribution (OOD) benchmarks (4,828 samples) under joint RL optimization. We further show that an early SFT$\rightarrow$RL transition achieves comparable precision with 65% less training data.

</details>

---

### [[20_Research/Papers/大模型/An_Intelligent-Cloud_Edge_Multimodal_Interaction_System_for_Robots|An Intelligent-Cloud Edge Multimodal Interaction System for Robots]]

![[assets/2607.14675_figure.png|800]]

- **arXiv**: [2607.14675](https://arxiv.org/abs/2607.14675)
- **PDF**: https://arxiv.org/pdf/2607.14675
- **详细分析**: [[20_Research/Papers/大模型/An_Intelligent-Cloud_Edge_Multimodal_Interaction_System_for_Robots|An Intelligent-Cloud Edge Multimodal Interaction System for Robots]]
- **作者**: Zihan Guo, Xiaoqi Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 1，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《An Intelligent-Cloud Edge Multimodal Interaction System for Robots》归入 大模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EfficientNet, MobileNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robust human-robot interaction in complex environments requires accurate gesture perception, semantic scene understanding, and reliable task planning under limited onboard computing resources. This paper presents a cloud-edge multimodal interaction framework that integrates an enhanced YOLO-based gesture detector with coordinated large language model (LLM) and vision-language model (VLM) agents. The proposed detector, incorporates the Convolutional Block Attention Module (CBAM) into the neck and replaces the baseline bounding-box regression objective with Distance-IoU (DIoU) loss. These modifications improve feature discrimination and localization for small or partially occluded gestures in complex backgrounds. The cloud layer performs gesture detection, scene understanding, multimodal fusion, and action planning, whereas the TonyPi robot locally handles data acquisition, communication, action execution, and feedback. Experiments on a public gesture dataset and a custom dataset show that YOLO-DC achieves precision values of 98.9% and 95.0%, with mAP@0.5 values of 90.7% and 92.7%, respectively. System-level evaluation yields success rates of 95%, 88%, and 82% for single-action, composite-action, and vision-dependent tasks. A 30 participant evaluation yields an overall mean satisfaction score of 3.69 out of 5. These results demonstrate the feasibility of combining refined gesture detection with multimodal agents for resource-constrained robotic interaction.

</details>

---

### [[20_Research/Papers/大模型/TopoAgent_A_Self-Evolving_Topological_Agent_for_Multimodal_Scientific_Reasoning|TopoAgent: A Self-Evolving Topological Agent for Multimodal Scientific Reasoning]]

![[assets/2607.14658_figure.png|800]]

- **arXiv**: [2607.14658](https://arxiv.org/abs/2607.14658)
- **PDF**: https://arxiv.org/pdf/2607.14658
- **详细分析**: [[20_Research/Papers/大模型/TopoAgent_A_Self-Evolving_Topological_Agent_for_Multimodal_Scientific_Reasoning|TopoAgent: A Self-Evolving Topological Agent for Multimodal Scientific Reasoning]]
- **作者**: Mingze Xu, Yinghui Li, Jiayi Kuang, Zhanhui Kang, Di Yin, Ying Shen, Xing Sun, Yuxing Han
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《TopoAgent: A Self-Evolving Topological Agent for Multimodal Scientific Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Multimodal Large Language Models (MLLMs) excel in general tasks, rigorous scientific reasoning remains challenging due to the limitations of monolithic, linear planning. Such sequential designs often suffer from visual-semantic misalignment, long-context hallucinations, and brittle execution under fixed task granularity. We propose TopoAgent, a self-evolving topological framework that replaces linear trajectories with dynamic, state-isolated graph evolution. TopoAgent first employs a front-end decomposer to fracture complex queries into visually-grounded atoms. These atoms are organized into a Directed Acyclic Graph (DAG) based on their dependencies, enabling strict context isolation to shield the reasoning engine from irrelevant historical noise. Furthermore, we introduce adaptive atomic fission, which dynamically splits bottleneck nodes into finer-grained sub-atoms at runtime when tool capability boundaries are exceeded. Extensive experiments across mathematics, physics, and chemistry benchmarks demonstrate that TopoAgent significantly outperforms state-of-the-art linear agent frameworks, providing a robust, noise-resistant, and self-correcting paradigm for autonomous scientific reasoning.

</details>

---

### [[20_Research/Papers/大模型/MemPoison_Uncovering_Persistent_Memory_Threats_and_Structural_Blind_Spots_in_LLM_Agents|MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents]]

![[assets/2607.14651_figure.png|800]]

- **arXiv**: [2607.14651](https://arxiv.org/abs/2607.14651)
- **PDF**: https://arxiv.org/pdf/2607.14651
- **详细分析**: [[20_Research/Papers/大模型/MemPoison_Uncovering_Persistent_Memory_Threats_and_Structural_Blind_Spots_in_LLM_Agents|MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents]]
- **作者**: Jifeng Gao, Kang Xia, Yi Zhang, Xiaobin Hong, Mingkai Lin, Xingshen Wei, Wenzhong Li, Sanglu Lu
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MemPoison-Bench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Persistent external memory enhances agent continuity but introduces persistent security vulnerabilities: adversarial content can be injected via standard interaction channels, retained across turns, and later distort downstream behavior. To address this challenge, we propose MemPoison, a comprehensive benchmark and analysis framework featuring 1227 hand-validated cases across four attack types, three injection channels, and three representative memory substrates, evaluated on seven open-weight and three closed-weight model families. We introduce a three-tier taxonomy: (L1) direct single-record corruption, (L2) compositional multi-record corruption and (L3) context-triggered dormant corruption. Our evaluations reveal a distinct defense frontier: while baseline write-time defenses, such as consistency checks, substantially suppress direct L1 attacks, they fail to reliably suppress L2 and L3 attacks. Through mechanistic influence decomposition (MID), we demonstrate structural blind spots in write-time defenses, which admit seemingly benign records that later become harmful through joint retrieval composition or trigger-conditioned activation. Our findings advocate for shifting from static filtering to adaptive, context-sensitive memory defense strategies.

</details>

---

### [[20_Research/Papers/大模型/MCPEvol-Bench_Benchmarking_LLM_Agent_Performance_Across_Dynamic_Evolutions_of_MCP_Servers|MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers]]

![[assets/2607.14642_figure.png|800]]

- **arXiv**: [2607.14642](https://arxiv.org/abs/2607.14642)
- **PDF**: https://arxiv.org/pdf/2607.14642
- **详细分析**: [[20_Research/Papers/大模型/MCPEvol-Bench_Benchmarking_LLM_Agent_Performance_Across_Dynamic_Evolutions_of_MCP_Servers|MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers]]
- **作者**: Huanxi Liu, Kun Hu, Jiaqi Liao, Qiang Wang, Pengfei Qian, YuanZhao Zhai, Dawei Feng, Bo Ding, Huaimin Wang
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MCP-Bench, MCPEval, MCPEvol-Bench, MCPEvolBench, OSWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As Model Context Protocol (MCP) servers emerge as the core infrastructure for connecting LLMs with external tools, existing benchmarks leverage real-world MCP servers to evaluate LLM agents' tool-using capabilities. However, these benchmarks overlook the continuous evolution of tool interfaces and functionalities within MCP servers, resulting in flawed assessments that fail to capture the agent's adaptability in changing tool landscapes. To bridge this gap, we introduce \textbf{MCPEvol-Bench}, a novel benchmark for evaluating the task-solving capabilities of LLM agents under dynamic toolset evolution. Inspired by large-scale empirical study, we propose 11 mutation operators to simulate realistic tool evolution within 123 MCP servers. We benchmark 12 state-of-the-art LLMs on multiple versions of MCP servers, revealing that even frontier models struggle to adapt to evolving tools. For instance, GPT-5.4 and Claude-Sonnet-4-6 exhibit performance declines of 13.7\% and 14.4\% in evolved MCP servers, respectively, accompanied by substantial increases in planning and reasoning errors. These findings highlight the vulnerability of LLM-driven workflows, establishing MCPEvol-Bench as a standard for evaluating agent adaptability in dynamic tool environments.

</details>

---

### [[20_Research/Papers/具身智能/Action_QFormer_Structured_Representation_Shaping_under_Action_Supervision_in_Vision-Language-Action_Models|Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models]]

![[assets/2607.14635_figure.png|800]]

- **arXiv**: [2607.14635](https://arxiv.org/abs/2607.14635)
- **PDF**: https://arxiv.org/pdf/2607.14635
- **详细分析**: [[20_Research/Papers/具身智能/Action_QFormer_Structured_Representation_Shaping_under_Action_Supervision_in_Vision-Language-Action_Models|Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models]]
- **作者**: Yufeng Ji, Wenhao Tang, Haoyi Niu, Koushil Sreenath, Yi Wu, Zhongyu Li
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.5（加权：具身智能 2.1，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HARP-VLA, OpenVLA, RotVLA, UniVLA, VQ-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action prediction. In this paper, we study it instead as a force that shapes inherited multimodal representations. We show that this shaping has a dual effect: it is necessary for forming action-compatible representations, but when action supervision is applied too directly to the inherited multimodal pathway, it can also destabilize representations that support language-side processing and object grounding. To address this tension, we introduce Action QFormer, a query-based action-facing interface that uses instruction-conditioned queries to reorganize inherited multimodal information into action-facing representations before downstream action generation. In zero-shot sim-to-real navigation, Action QFormer improves average closed-loop task success from 18.8% to 56.3%, raises fixed-instruction action-generation correctness from 22.5% to 75.5%, and nearly eliminates out-of-distribution instruction generations. Further analyses show that Action QFormer changes how action supervision shapes inherited multimodal representations, reducing broad upstream rewriting while preserving targeted and sometimes constructive action-supervised adaptation. These results suggest that improving VLA performance requires not only stronger pretrained backbones, but also better ways of selecting and organizing inherited multimodal information while controlling how it is shaped under action supervision.

</details>

---

### [[20_Research/Papers/具身智能/Knowing_You_at_First_Glance_Inferring_Apparent_Personality_from_Faces|Knowing You at First Glance: Inferring Apparent Personality from Faces]]

![[assets/2607.14631_figure.png|800]]

- **arXiv**: [2607.14631](https://arxiv.org/abs/2607.14631)
- **PDF**: https://arxiv.org/pdf/2607.14631
- **详细分析**: [[20_Research/Papers/具身智能/Knowing_You_at_First_Glance_Inferring_Apparent_Personality_from_Faces|Knowing You at First Glance: Inferring Apparent Personality from Faces]]
- **作者**: Shuhuan Chen, Xiangyu Zhu, Weisong Zhao, Haichao Shi, Xiao-Yu Zhang, Zhen Lei
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 0.7（加权：具身智能 0.3，大模型 0.2，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Knowing You at First Glance: Inferring Apparent Personality from Faces》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Inferring apparent personality from facial images is important in social scenarios for embodied agents in human-robot interaction. Unlike inferring intrinsic personality traits via conversation, this task models first-impression personality perception based solely on facial appearance before interaction begins. Existing studies mainly focus on the Big Five personality model and often rely on language or multimodal inputs. As a result, it remains unclear whether facial cues alone can support meaningful associations with perceived personality traits. This question is particularly relevant for MBTI types, which are widely used in practice and more readily interpretable by large language models. To this end, we propose \textbf{GlanceFace}, an end-to-end framework for apparent personality inference leveraging vision-language models to introduce semantic priors and a semantic-enhanced facial representation module to capture subtle personality-related cues, together with an uncertainty-aware learning strategy to handle noisy and subjective annotations. Extensive experiments demonstrate strong performance on MBTI-based apparent personality benchmarks and reveal relationships between facial characteristics and perceived personality traits, highlighting its potential to support adaptive initial interaction strategies for embodied agents. The code and dataset are available at https://github.com/MrHuan3/GlanceFace.

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Entropy_Correctness-Aware_Advantage_Shaping_via_Contrastive_Policy_Optimization|Beyond Entropy: Correctness-Aware Advantage Shaping via Contrastive Policy Optimization]]

![[assets/2607.14614_figure.png|800]]

- **arXiv**: [2607.14614](https://arxiv.org/abs/2607.14614)
- **PDF**: https://arxiv.org/pdf/2607.14614
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Entropy_Correctness-Aware_Advantage_Shaping_via_Contrastive_Policy_Optimization|Beyond Entropy: Correctness-Aware Advantage Shaping via Contrastive Policy Optimization]]
- **作者**: Weiwen Xu, Jia Liu, Hou Pong Chan, Long Li, Deng Cai, Min Chen, Hao Zhang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Beyond Entropy: Correctness-Aware Advantage Shaping via Contrastive Policy Optimization》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) commonly uses entropy for advantage shaping. However, entropy cannot distinguish useful uncertainty from detrimental confusion, limiting its effectiveness as a correctness signal. We propose Contrastive Policy Optimization (CPO), which uses token-level contrastive disagreement between reference-guided and vanilla generation distributions for correctness-aware advantage shaping. Both theoretical and empirical results show that this disagreement reliably indicates token-level correctness. We further show that On-policy Distillation is a special case of CPO, where the posterior distribution is instantiated by an external teacher model. CPO also resolves the zero-advantage problem. Experiments on in-domain and out-of-domain benchmarks demonstrate that CPO substantially outperforms entropy-based RLVR methods while maintaining strong generalization. Further analysis shows that correct and incorrect responses naturally support exploration and exploitation respectively, and balancing both leads to the best performance.

</details>

---

### [[20_Research/Papers/大模型/Multi-LLM_Collaborative_MRI_Report_Generation_for_Visual_Instruction_Tuning_in_Brain_Oncology|Multi-LLM Collaborative MRI Report Generation for Visual Instruction Tuning in Brain Oncology]]

![[assets/2607.14581_figure.png|800]]

- **arXiv**: [2607.14581](https://arxiv.org/abs/2607.14581)
- **PDF**: https://arxiv.org/pdf/2607.14581
- **详细分析**: [[20_Research/Papers/大模型/Multi-LLM_Collaborative_MRI_Report_Generation_for_Visual_Instruction_Tuning_in_Brain_Oncology|Multi-LLM Collaborative MRI Report Generation for Visual Instruction Tuning in Brain Oncology]]
- **作者**: Sinyoung Ra, Jonghun Kim, Hyunjin Park
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Multi-LLM Collaborative MRI Report Generation for Visual Instruction Tuning in Brain Oncology》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in large language models (LLMs) and their extension to vision-language models (VLMs) have made it easier to combine text and images for tasks such as report generation. Existing VLMs in medicine typically focus on 2D images (chest X-rays), and their extension to 3D imaging has been difficult because of the lack of paired 3D imaging-text data. Thus, we introduce a new method for creating a 3D image-text dataset for brain oncology using 3D MRI scans of glioma and meningioma cases. We use a cooperative system in which several LLMs work together to generate and check reports, ensuring that they are accurate and clear. By leveraging the new 3D MRI-text dataset, we further build a VLM that converts MRI scans into tokens and aligns them with text instructions. Our VLM performed better in report generation and visual question answering tasks than other 2D and 3D methods. Our method not only improves the quality of reports but also helps with better diagnosis and treatment in brain oncology.

</details>

---

### [[20_Research/Papers/大模型/Collaborative_Spatial_Learning_with_Multi-LLM_Agents_in_Networked_Social_Experiments|Collaborative Spatial Learning with Multi-LLM Agents in Networked Social Experiments]]

![[assets/2607.14574_figure.png|800]]

- **arXiv**: [2607.14574](https://arxiv.org/abs/2607.14574)
- **PDF**: https://arxiv.org/pdf/2607.14574
- **详细分析**: [[20_Research/Papers/大模型/Collaborative_Spatial_Learning_with_Multi-LLM_Agents_in_Networked_Social_Experiments|Collaborative Spatial Learning with Multi-LLM Agents in Networked Social Experiments]]
- **作者**: Hao He, Chris J. Kuhlman, Xinwei Deng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Collaborative Spatial Learning with Multi-LLM Agents in Networked Social Experiments》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collective problem solving often requires that group members consider the tradeoff between exploitation of known solutions and exploration for new ones, where information of known solutions can be disseminated among individual members through communication networks. The Mason--Watts experiment (PNAS 2012) showed that human groups in shorter-path networks outperform those in longer-path networks on a two-dimensional search task. In this work, we focus on the investigation of such network-efficiency effects in the setting of a group of large language model (LLM) agents. Specifically, we consider groups of sixteen LLM agents playing the Mason--Watts experiment on the eight Mason--Watts network topologies. Moreover, we develop mechanistic Bayesian optimization agents such that the performance of LLM agents can be compared with both the mechanistic agents and the human experimental data. Our computational experiments indicate that the LLM agents show a significant network-efficiency effect when instructed to randomize their first-round choices, but not under the default initialization. In this experiment, adding a one-sentence first-round randomization instruction improves collective payoff by more than three times the estimated payoff difference across the eight network topologies. Also, the Bayesian optimization agents obtain higher payoffs than the evaluated LLM agents on this spatial search task. We further compare the agents' exploration--exploitation behavior, copying, and spatial diversity.

</details>

---

### [[20_Research/Papers/具身智能/SafeRelBench_A_Spatial-Relation-Aware_Benchmark_for_Process-Level_Safety_in_VLM-Driven_Embodied_Agents|SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents]]

![[assets/2607.14543_figure.png|800]]

- **arXiv**: [2607.14543](https://arxiv.org/abs/2607.14543)
- **PDF**: https://arxiv.org/pdf/2607.14543
- **详细分析**: [[20_Research/Papers/具身智能/SafeRelBench_A_Spatial-Relation-Aware_Benchmark_for_Process-Level_Safety_in_VLM-Driven_Embodied_Agents|SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents]]
- **作者**: Huaigang Yang, Ya Li, Min Ren, Bo Dai, Zhenliang Zhang, Zhaofeng He
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，大模型 0.8，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BeSafe-Bench, EARBench, EAsafetyBench, IS-Bench, SafeAgentBench, SafeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) are increasingly used as the reasoning backbone of embodied agents, enabling robots to interpret visual scenes, follow language instructions, and plan multi-step actions. In household environments, however, safety depends not only on recognizing objects, but also on how actions change the physical scene over time. Existing embodied safety evaluations largely focus on static risk recognition, unsafe instruction refusal, or final-state task completion. As a result, process-level safety failures induced by spatial relations such as support, containment, and proximity remain insufficiently studied. To address this gap, we introduce SAFERELBENCH, a spatial-relation-aware safety benchmark with 507 executable evaluation samples, including 248 spatial-relation samples and 259 non-spatial control samples. Using SAFERELBENCH to evaluate seven open- and closed-source VLM-driven embodied agents, we find a substantial gap between task success and process-level safety compliance: models often complete the requested task while violating process-level safety constraints. Unlike prior benchmarks, SAFERELBENCH explicitly tests whether agents satisfy safety conditions before risk-prone actions, making spatial relations a core dimension in embodied safety assessment. More broadly, our results show that safe embodied intelligence requires not only stronger perception and planning, but also reliable reasoning about how object relations shape risk during interaction.

</details>

---

### [[20_Research/Papers/大模型/Are_LLM-Generated_GPU_Kernels_Production-Ready_A_Trace-Driven_Benchmark_and_Optimization_Agent|Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent]]

![[assets/2607.14541_figure.png|800]]

- **arXiv**: [2607.14541](https://arxiv.org/abs/2607.14541)
- **PDF**: https://arxiv.org/pdf/2607.14541
- **详细分析**: [[20_Research/Papers/大模型/Are_LLM-Generated_GPU_Kernels_Production-Ready_A_Trace-Driven_Benchmark_and_Optimization_Agent|Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent]]
- **作者**: Lingyun Yang, Yuxiao Wang, Shenghao Liang, Linfeng Yang, Daocheng Ying, Chunbo You, Rui Zhang, Luping Wang, Yinghao Yu, Guodong Yang, Liping Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Atrex-Bench, BackendBench, CUDABench, FlashInfer-Bench, KernelBench, MultiKernelBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing GPU kernel generation benchmarks draw problems from synthetic or curated sources that diverge from deployed workloads. We present Atrex-Bench, a benchmark whose 30 operators and 440 shapes are sampled directly from full-cluster production inference traces of compute-limited, memory-rich GPUs. Each problem carries an importance weight derived from its share of observed GPU time, weighted by application card-hours and computed separately for the serving phases in which it runs, together with a per-problem roofline ceiling, so the aggregate score emphasizes the kernels that consume the most serving time. Evaluating six frontier coding agents on Atrex-Bench shows that even the best vanilla model reaches only ${\sim}10\%$ of the hardware roofline on production operators; and correctness alone overstates capability, since much of the apparent pass rate comes from PyTorch fallbacks rather than kernels the model wrote. To close this gap, we co-release Atrex-Kernel-Agent (AKA), a profile-driven kernel-optimization agent that combines iterative measure-revise search, optimization dropout for escaping stalled search contexts, and a layered GPU-optimization knowledge base (298 reference-kernel files and 244 optimization-knowledge documents, plus external upstream reference projects for API/ISA lookup). In a controlled case study, the agent converts zero-FlyDSL fallbacks into real kernels that match or exceed hand-tuned production baselines.

</details>

---

### [[20_Research/Papers/大模型/VLT_A_Vision-Language-Time_Series_Multimodal_Foundation_Model_for_Industrial_Intelligence|VLT: A Vision-Language-Time Series Multimodal Foundation Model for Industrial Intelligence]]

![[assets/2607.14510_figure.png|800]]

- **arXiv**: [2607.14510](https://arxiv.org/abs/2607.14510)
- **PDF**: https://arxiv.org/pdf/2607.14510
- **详细分析**: [[20_Research/Papers/大模型/VLT_A_Vision-Language-Time_Series_Multimodal_Foundation_Model_for_Industrial_Intelligence|VLT: A Vision-Language-Time Series Multimodal Foundation Model for Industrial Intelligence]]
- **作者**: Haiteng Wang, Jingheng Yan, Xiaokang Wang, Lei Ren
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《VLT: A Vision-Language-Time Series Multimodal Foundation Model for Industrial Intelligence》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industrial time series serve as the foundation for Prognostics and Health Management (PHM) to ensure the reliability and safety of industrial equipment such as aero-engines. However, existing approaches are typically limited to single-modality modeling, which restricts their generalization in complex scenarios. Although recent advances in large language models (LLMs) provide new opportunities for multimodal learning, bridging continuous time-series signals and discrete textual semantics remains an open challenge. To this end, we propose VLT, a multimodal foundation model that jointly models time-series, frequency-spectrum visual representations, and textual knowledge. A key insight is to utilize the frequency spectrum as a visual bridge to connect continuous temporal signals with discrete semantics. Specifically, a Time-aware Mixture-of-Experts (Time-MoE) is designed to capture heterogeneous temporal dynamics, while a Frequency-Text Augmented Learner enables joint modeling of spectral and semantic features within a shared representation space. Furthermore, a time-centric gradient alignment mechanism is introduced to mitigate cross-modal optimization conflicts via gradient normalization and reliability-aware dynamic reweighting. Extensive experiments on multiple industrial datasets demonstrate that VLT outperforms state-of-the-art methods, achieving superior robustness and generalization under few-shot, noisy, and incomplete-modality settings.

</details>

---

### [[20_Research/Papers/强化学习/Non-vacuous_Generalization_Bounds_for_Reinforcement_Learning_with_Verifiable_Rewards|Non-vacuous Generalization Bounds for Reinforcement Learning with Verifiable Rewards]]

![[assets/2607.14506_figure.png|800]]

- **arXiv**: [2607.14506](https://arxiv.org/abs/2607.14506)
- **PDF**: https://arxiv.org/pdf/2607.14506
- **详细分析**: [[20_Research/Papers/强化学习/Non-vacuous_Generalization_Bounds_for_Reinforcement_Learning_with_Verifiable_Rewards|Non-vacuous Generalization Bounds for Reinforcement Learning with Verifiable Rewards]]
- **作者**: Yuxuan Zhu, Rohan Alur, Daniel Kang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Non-vacuous Generalization Bounds for Reinforcement Learning with Verifiable Rewards》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While reinforcement learning with verifiable rewards (RLVR) is widely used to improve the reasoning capabilities of large language models (LLMs), the generalizability of the resulting models remains poorly understood. In this work, we establish the first non-vacuous generalization bounds for parameter-efficient RLVR fine-tuning at the billion-parameter scale. Our approach adapts PAC-Bayes compression bounds to this setting, and addresses the inherent stochasticity of token generation by applying the Gumbel-max reparameterization trick. To operationalize these bounds, we propose the Progressive RLVR framework, which integrates RLVR with on-policy distillation, TinyLoRA, and model quantization. Progressive RLVR empirically retains 84-97% performance of standard LoRA fine-tuning while producing models that are 14,796x more compressible. We show that this framework yields non-vacuous generalization bounds in four domains: mathematical problem-solving, programming, general-knowledge reasoning, and Text-to-SQL. Our bounds exceed the accuracy of the base model by 9-51% and lie within 6-11% of the accuracy of the fine-tuned models.

</details>

---

### [[20_Research/Papers/大模型/Step-Level_Preference_Learning_for_Generative_Agents_in_Social_Simulations|Step-Level Preference Learning for Generative Agents in Social Simulations]]

![[assets/2607.14485_figure.png|800]]

- **arXiv**: [2607.14485](https://arxiv.org/abs/2607.14485)
- **PDF**: https://arxiv.org/pdf/2607.14485
- **详细分析**: [[20_Research/Papers/大模型/Step-Level_Preference_Learning_for_Generative_Agents_in_Social_Simulations|Step-Level Preference Learning for Generative Agents in Social Simulations]]
- **作者**: Wenchang Gao, Pingyue Sheng, Lanlan Qiu, Yunfei Ma, Jian Zhao, Baicheng Chen, Kangda Wang, Yuyang Tian, Shunqiang Mao, Tianxing He
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Step-Level Preference Learning for Generative Agents in Social Simulations》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based generative agents simulate human behavior through long-horizon decision-making processes that comprise intermediate steps such as planning, memory retrieval, reflection, and action selection. However, fine-grained human annotations of these intermediate steps remain scarce, and existing agents are not grounded in human preferences over such intermediate decisions. To address this gap, we introduce \method, an interactive simulation interface that enables us to collect step-level human preference supervision over agent decision trajectories, leading to a dataset of 57K fine-grained annotations. We conduct step-level preference learning on open-weight language models using supervised finetuning and direct preference optimization on this data, consistently improving simulation fidelity, coordination, and interaction quality, and inducing more socially effective agent behavior. Our results show that step-level human supervision is an effective training signal for improving both local decision quality and long-horizon agent behavior.

</details>

---

### [[20_Research/Papers/具身智能/ConFlow_Constraints-Guided_Learning_with_Flow_Matching_for_Motion_Generation|ConFlow: Constraints-Guided Learning with Flow Matching for Motion Generation]]

![[assets/2607.14424_figure.png|800]]

- **arXiv**: [2607.14424](https://arxiv.org/abs/2607.14424)
- **PDF**: https://arxiv.org/pdf/2607.14424
- **详细分析**: [[20_Research/Papers/具身智能/ConFlow_Constraints-Guided_Learning_with_Flow_Matching_for_Motion_Generation|ConFlow: Constraints-Guided Learning with Flow Matching for Motion Generation]]
- **作者**: Nutan Chen, Jianxiang Feng, Marvin Alles, Botond Cseke
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《ConFlow: Constraints-Guided Learning with Flow Matching for Motion Generation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In recent years Flow Matching has become a prominent method for generative modeling robot motion generation. In its generic form Flow Matching is an ODE-based neural sampler that is trained by regressing empirical flow fields associated with motion samples as data. However, in robot motion generation we often have additional constraints that might not be present in the collected data. The majority of current approaches train the flow on the available data and use inference-time guidance to enforce task-specific constraints. To address this mismatch, we propose \textbf{ConFlow}, a constraint-guided flow matching framework that incorporates constraint information directly into the training objective via differentiable barrier or cost functions. To address design specifications such as smoothness and boundary conditions, we propose replacing the standard Gaussian source distribution used in flow matching training with a conditional Gaussian Process. Our approach also uses infeasible demonstrations as negative supervision, improving constraint satisfaction without requiring additional expert data. Experiments on a two-robot navigation task demonstrate that ConFlow achieves lower collision rates and higher trajectory quality than standard flow matching baselines, with or without inference-time guidance. These results validate training-time constraint integration as an effective approach to closing the training--inference gap in generative motion models.

</details>

---

### [[20_Research/Papers/强化学习/An_offline_approach_to_fNIRS-guided_reinforcement_learning_for_robot_behavior|An offline approach to fNIRS-guided reinforcement learning for robot behavior]]

![[assets/2607.14393_figure.jpg|800]]

- **arXiv**: [2607.14393](https://arxiv.org/abs/2607.14393)
- **PDF**: https://arxiv.org/pdf/2607.14393
- **详细分析**: [[20_Research/Papers/强化学习/An_offline_approach_to_fNIRS-guided_reinforcement_learning_for_robot_behavior|An offline approach to fNIRS-guided reinforcement learning for robot behavior]]
- **作者**: Julia Santaniello, Madelaine Brower, Benson Jiang, Donatello Sassaroli, Robert Jacob, Jivko Sinapov
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 大模型
- **相关性评分**: 2.4（加权：具身智能 0.3，大模型 0.2，强化学习 0.8，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《An offline approach to fNIRS-guided reinforcement learning for robot behavior》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HITL-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-in-the-loop Reinforcement Learning has become a popular approach to training, finetuning, and aligning robot behavior with user preferences. Our paper explores the feasibility of using brain signals via functional near-infrared spectroscopy (fNIRS) to modulate robot learning in simulation. We compare agents trained on passive (observational) versus active (demonstrative) interaction tasks, and test multiple methods for enhancing the RL algorithm with the neural signal, focusing on parameter augmentation rather than replacement. We further examine how model granularity and noise affect agent learning. Our results show that this framework is effective: the neural signal improves learning when augmenting trajectory priorities and state-action q-values. Additionally, the framework learns successfully from offline data, offering a practical alternative for settings where real-time BCI setups are impractical or only limited data is available.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Visual_Grasping_Benchmarking_Complex_Grasping_from_Detection_to_Execution|Beyond Visual Grasping: Benchmarking Complex Grasping from Detection to Execution]]

![[assets/2607.14341_figure.png|800]]

- **arXiv**: [2607.14341](https://arxiv.org/abs/2607.14341)
- **PDF**: https://arxiv.org/pdf/2607.14341
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Visual_Grasping_Benchmarking_Complex_Grasping_from_Detection_to_Execution|Beyond Visual Grasping: Benchmarking Complex Grasping from Detection to Execution]]
- **作者**: Hanyi Zhang, Khang Nguyen, Charith Munasinghe, Basu Hela, Tianyu Li, Zihong Luo, Hoan Nguyen, Hans Wernher van de Venn, Yalin Zheng, Ravi Prakash, Tung D. Ta, Anh Nguyen...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Beyond Visual Grasping: Benchmarking Complex Grasping from Detection to Execution》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FetchBench, GCA-Bench, GraspNet, RLBench, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robust robotic grasping remains a fundamental challenge for complex real-world applications. Recent advances in large-scale models demonstrate promising capabilities for reasoning in robotic tasks. However, existing benchmarks for grasping primarily focus on isolated, visual-based grasp pose detection, failing to capture the complexity of grasping tasks that require multi-step reasoning and semantic understanding during execution. To address this gap, we propose GCA-Bench, a benchmark featuring challenging \textit{grasping with complex action} scenarios that involve both scene-level reasoning and semantic constraints. GCA-Bench enables the evaluation of recent large foundation models under the same settings. To demonstrate the effectiveness of our new benchmark, we implement a diverse set of baselines, ranging from traditional grasp detection pipelines to end-to-end learning methods. Empirical studies achieve success rates below 70\% on complex grasping scenarios, underscoring critical limitations. In addition, we propose new evaluation metrics, analyze critical failure models, and provide insights to guide the development of more robust and generalizable grasping strategies.

</details>

---

### [[20_Research/Papers/具身智能/MEMORA_Embodied_Action_Memory_from_Egocentric_Videos_for_Reasoning_and_Planning|MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning]]

![[assets/2607.14252_figure.png|800]]

- **arXiv**: [2607.14252](https://arxiv.org/abs/2607.14252)
- **PDF**: https://arxiv.org/pdf/2607.14252
- **详细分析**: [[20_Research/Papers/具身智能/MEMORA_Embodied_Action_Memory_from_Egocentric_Videos_for_Reasoning_and_Planning|MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning]]
- **作者**: Zihao Yu, Xiu Yuan, Chongjie Zhang
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EAM-QA, MEMORA-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robot planning requires more than predicting what actions will do next; it also requires memory of the embodied experience that makes future goals interpretable. People do not plan from the present scene alone: they draw on remembered places, object-state changes, prior procedures, and regularities revealed through repeated action. We formulate Embodied Action Memory (EAM) as the capability to form, maintain, and use such experience as a persistent memory state for later decisions. MEMORA realizes EAM with a formation-consolidation-retrieval lifecycle and four typed stores: Environment Memory, Entity Memory, Activity Memory, and Inferred Knowledge. Online editing maintains object identities and state histories as new observations arrive; offline consolidation abstracts repeated experience into reusable procedures and participant-specific regularities. MEMORA-Bench evaluates this lifecycle on 45 hours of EPIC-KITCHENS-100 extension video across 18 participants through memory-grounded planning, including previously unseen goals, and a complementary memory-assessment task. Across four open-weight language models, full MEMORA--combining editing, typed stores, and consolidation--achieves the strongest aggregate results among the evaluated memory conditions. It improves memory-assessment accuracy by up to 20.5 points over the strongest controlled baseline and improves out-of-distribution Robot-Grounded Plan score by up to 16.6% relative. A qualitative two-task robot deployment study further illustrates how memory-grounded language plans can interface with downstream control, while the overall results show that editable, consolidated memory can supply remembered context for robot planning. Project page: https://yuzihaowashu.github.io/MEMORA/

</details>

---

### [[20_Research/Papers/具身智能/Never_Too_Late_for_Force_Accelerating_VLA_Post-Training_with_Reactive_Force_Injection|Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection]]

![[assets/2607.14236_figure.png|800]]

- **arXiv**: [2607.14236](https://arxiv.org/abs/2607.14236)
- **PDF**: https://arxiv.org/pdf/2607.14236
- **详细分析**: [[20_Research/Papers/具身智能/Never_Too_Late_for_Force_Accelerating_VLA_Post-Training_with_Reactive_Force_Injection|Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection]]
- **作者**: Yi Wang, Wendi Chen, Zimo Wen, Han Xue, Xueqi Li, Wenye Yu, Zhijie Chen, Hao Yang, Jun Lv, Chuan Wen, Cewu Lu
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained vision-language-action (VLA) policies provide strong language-conditioned manipulation knowledge, but they remain largely vision-driven and can struggle once manipulation enters contact states where the scene is occluded, depth is ambiguous, or small force errors push execution off the offline demonstration distribution. We present LIFT (Late Reactive Injection of Force for VLA Post-Training), a force-aware post-training framework that adds contact reactivity to a pretrained VLA policy while preserving its general manipulation knowledge. LIFT grafts a reactive action expert beside the original action expert, initializes it from pretrained action weights, and injects recent 6D end-effector force through causal force memory and zero-initialized cross attention, enabling actions to be refreshed during execution. To address the policy-dependent distribution shift of contact feedback, LIFT further couples reactive force injection with an online DAgger loop that trains on a mixture of offline task-alignment data and human-corrected online rollouts. Across towel folding, book insertion, and Hanoi ring placement, LIFT learns faster and reaches higher performance than vision-only post-training, while ablations show that reactive force memory and online corrective data are both important for robust contact-rich manipulation. Our code and data will be publicly available.

</details>

---

### [[20_Research/Papers/具身智能/RxBrain_Embodied_Cognition_Foundation_Model_with_Joint_Language-Visual_Reasoning_and_Imagination|RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination]]

![[assets/2607.14187_first_page.png|800]]

- **arXiv**: [2607.14187](https://arxiv.org/abs/2607.14187)
- **PDF**: https://arxiv.org/pdf/2607.14187
- **详细分析**: [[20_Research/Papers/具身智能/RxBrain_Embodied_Cognition_Foundation_Model_with_Joint_Language-Visual_Reasoning_and_Imagination|RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination]]
- **作者**: Haotian Liang, Mingkang Chen, Yufei Huang, Yuchun Guo, Xiaomeng Zhu, Xiangli Shi, Kaixuan Wang, Yunxuan Mao, Weijie Zhou, Ling Chen, Shirong Zeng, Yueyu Long...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人, 世界模型
- **相关性评分**: 2.8（加权：具身智能 1.5，大模型 0.6，世界模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RxBrain-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied cognition requires agents to connect high-level task reasoning with the physical states to be achieved. We introduce Hy-Embodied-RxBrain, an embodied cognition foundation model with joint language-visual reasoning and imagination. Unlike vision-language models that emphasize scene understanding and textual decision making, or generative world models that mainly predict future visual states, RxBrain represents embodied plans in a single planning sequence where language and visual imagination play complementary roles. Language provides the abstract structure of a plan, including task decomposition, planning primitives, constraints, temporal order, and decision logic, while visual imagination grounds this structure through world state prediction and joint subgoal planning, associating each planning step with intermediate and final physical states. RxBrain adopts a unified multimodal Mixture-of-Transformers architecture that supports language, image, and video understanding and generation within one model. To train this capability, we build an automatic pipeline that converts embodied videos into joint text-visual planning supervision by decomposing videos into planning steps and aligning them with visual state transitions. We further introduce RxBrain-Bench to evaluate whether models can represent embodied plans through joint textual and visual components rather than separate understanding or generation. Experiments show that RxBrain maintains embodied understanding and generation abilities, and produces plans with coupled textual reasoning, world state prediction, and joint subgoal planning. We also extend RxBrain to continuous robot action generation, where it shows promising real-robot performance without large-scale action-data pretraining. These results provide an initial step toward foundation models for embodied cognition.

</details>

---

### [[20_Research/Papers/强化学习/Semantic_Audio-driven_Understanding_for_Dynamic_Humanoid_Whole_Body_Control|Semantic Audio-driven Understanding for Dynamic Humanoid Whole Body Control]]

![[assets/2607.14182_figure.png|800]]

- **arXiv**: [2607.14182](https://arxiv.org/abs/2607.14182)
- **PDF**: https://arxiv.org/pdf/2607.14182
- **详细分析**: [[20_Research/Papers/强化学习/Semantic_Audio-driven_Understanding_for_Dynamic_Humanoid_Whole_Body_Control|Semantic Audio-driven Understanding for Dynamic Humanoid Whole Body Control]]
- **作者**: J. M. A. Marcelo, M. Brienza, E. Bugli, L. Comito, D. Nardi, D. D. Bloisi, V. Suriani
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.7（加权：具身智能 1.8，强化学习 0.2，机器人 1.7）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Semantic Audio-driven Understanding for Dynamic Humanoid Whole Body Control》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：AudioSet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in humanoid robotics and reinforcement learning have enabled the acquisition of highly expressive whole-body motion policies. However, most robotic performances remain based on pre-scripted sequences or externally triggered behaviors, limiting autonomy and responsiveness to dynamic environments. In this work, we introduce a novel multi-modal orchestration framework for semantic audio-driven humanoid control, enabling robots to autonomously select and execute appropriate motion skills in real time. The system processes continuous audio streams and routes them into music or speech branches. Music input is handled via audio fingerprinting and semantic embeddings to retrieve track identity and temporal alignment, allowing dynamic mapping between musical segments and motion policies. Speech input is grounded into a discrete library of imitation-learned skills, enabling direct human-robot interaction. Both modalities share a unified interface that schedules skill execution over a reinforcement learning control pipeline. We validate the approach in simulation and on a Unitree G1 humanoid, showing robust sim-to-real transfer and consistent audio-conditioned policy selection. Supplementary materials are available at the following site: https://lab-rococo-sapienza.github.io/semantic-WBC/

</details>

---

### [[20_Research/Papers/强化学习/RENEW_Towards_Learning_World_Models_and_Repairing_Model_Exploitation_from_Preferences|RENEW: Towards Learning World Models and Repairing Model Exploitation from Preferences]]

![[assets/2607.14180_figure.png|800]]

- **arXiv**: [2607.14180](https://arxiv.org/abs/2607.14180)
- **PDF**: https://arxiv.org/pdf/2607.14180
- **详细分析**: [[20_Research/Papers/强化学习/RENEW_Towards_Learning_World_Models_and_Repairing_Model_Exploitation_from_Preferences|RENEW: Towards Learning World Models and Repairing Model Exploitation from Preferences]]
- **作者**: Logan Mondal Bhamidipaty, Mykel Kochenderfer, Subramanian Ramamoorthy
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.72（加权：强化学习 0.36，世界模型 1.36）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《RENEW: Towards Learning World Models and Repairing Model Exploitation from Preferences》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are widely used in offline reinforcement learning (RL) to improve sample efficiency and generate experience beyond a fixed dataset. However, they are vulnerable to model exploitation where data coverage is thin. Prior work addresses this either by collecting more expert demonstrations, which is often expensive, unsafe, or unavailable, or by conservative algorithms that avoid uncertain regions, which limits generalization. We propose instead to repair exploitation directly using human preferences over imagined rollouts, leveraging the strong intuitive physics that allows humans to easily spot egregious dynamics hallucinations. We formalize this as Dynamics Learning from Human Feedback (DLHF), a Bradley-Terry preference loss over trajectory log-likelihoods under a learned dynamics model. Unfortunately, naive DLHF is sample inefficient, so we introduce RENEW, which uses epistemic uncertainty to focus finetuning where the model is most exploitable. We evaluate on several Jumanji and classic control environments and find that while naive DLHF requires an outsize preference budget, RENEW makes the framework practical by improving sample efficiency, limiting catastrophic forgetting, and reducing exploitation in pretrained world models. Taken together, our results provide initial evidence that preferences can supervise world model dynamics directly, offering a new approach to addressing exploitation in offline model-based RL.

</details>

---

### [[20_Research/Papers/大模型/When_a_Verified_World_Model_Still_Loses_Play-Adequacy_vs_Prediction-Accuracy_in_LLM-Synthesized_Code_World_Models|When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models]]

![[assets/2607.14169_figure.png|800]]

- **arXiv**: [2607.14169](https://arxiv.org/abs/2607.14169)
- **PDF**: https://arxiv.org/pdf/2607.14169
- **详细分析**: [[20_Research/Papers/大模型/When_a_Verified_World_Model_Still_Loses_Play-Adequacy_vs_Prediction-Accuracy_in_LLM-Synthesized_Code_World_Models|When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models]]
- **作者**: Javier Aguilar Martín
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 2.32（加权：大模型 0.4，强化学习 0.16，世界模型 1.76）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models can synthesize a game's rules as executable code - a Code World Model (CWM) - which a classical planner then searches over. Such models are typically accepted when they reach high transition accuracy on sampled trajectories. We argue this is the wrong notion of adequacy for planning. We show four things. (1) An LLM-synthesized CWM can pass a sampling gate at 100% transition accuracy and be $\geq 98\%$ state-accurate on the planner's own search distribution, yet lose systematically at play, because the $&lt;1\%$ it gets wrong is exactly the pivotal dynamics; the play cost of the omitted rule is $0.091$ (seed-clustered 95% CI $[0.065,0.117]$, $n=4800$). We call this the verified-vs-correct gap, and confirm it end-to-end through the synthesis pipeline. (2) The harm follows a quantitative law, $\mathrm{danger}=\mathrm{play\_cost}\times(1-\mathrm{rarity})^N$, whose $(1-\mathrm{rarity})^N$ gate-miss factor is proven exact and whose play cost is empirically bounded. (3) The failure is not repaired by more data: LLM synthesis behaves as rule translation, not rule inference, and did not infer the omitted rule across models (GPT-5.x) and data regimes (including DAgger and targeted examples). (4) The same mechanism recurs on the belief-inference function of imperfect-information CWMs: we prove a coverage bound (a size-$N$ gate is identifying when $N\gtrsim b^{d_{\max}}$), explaining why shallow games such as Kuhn poker show no gap, and hand-construct Beacon, a verified-but-wrong inference function that passes the gate yet loses every game. These results suggest adequacy for planning-oriented world models should be measured on the search distribution or by play directly, not by prediction accuracy on sampled transitions.

</details>

---

### [[20_Research/Papers/大模型/Structured_Feedback_Improves_Repair_in_an_LLM_Agent_Loop|Structured Feedback Improves Repair in an LLM Agent Loop]]

![[assets/2607.14167_first_page.png|800]]

- **arXiv**: [2607.14167](https://arxiv.org/abs/2607.14167)
- **PDF**: https://arxiv.org/pdf/2607.14167
- **详细分析**: [[20_Research/Papers/大模型/Structured_Feedback_Improves_Repair_in_an_LLM_Agent_Loop|Structured Feedback Improves Repair in an LLM Agent Loop]]
- **作者**: Jaideep Ray, Ankit Goyal
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Structured Feedback Improves Repair in an LLM Agent Loop》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HumanEval, TextWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents often retry after external validation rejects a candidate, but the interface between validation and the next model call remains underspecified. We introduce VeriHarness, a code-controlled agent loop in which models generate candidates while external validators control acceptance, budgets, and traces. We use it to compare raw diagnostics with feedback that identifies the failure location, observed value, and admissible alternatives. Across 50 paired TextWorld games under a four-call cap, feedback containing all three fields raises terminal success from 14/50 to 36/50 for Qwen2.5-Coder-14B (+44 percentage points) and from 8/50 to 29/50 for Llama-3.1-8B (+42 points). Ablations locate most of the gain in the admissible alternatives: feedback containing only the location and observed value remains near the raw diagnostic baseline. Presenting the complete repair information in prose instead of a keyed JSON record yields nearly the same success, providing no evidence that JSON syntax itself improves repair. The ordering persists across the tested call budgets and one sampled-decoding setting.

</details>

---

### [[20_Research/Papers/大模型/Towards_Reliable_AI-Assisted_Analog_Design_Template-Constrained_LLM_Agents_for_SAR_ADC_Generation|Towards Reliable AI-Assisted Analog Design: Template-Constrained LLM Agents for SAR ADC Generation]]

![[assets/2607.14165_figure.png|800]]

- **arXiv**: [2607.14165](https://arxiv.org/abs/2607.14165)
- **PDF**: https://arxiv.org/pdf/2607.14165
- **详细分析**: [[20_Research/Papers/大模型/Towards_Reliable_AI-Assisted_Analog_Design_Template-Constrained_LLM_Agents_for_SAR_ADC_Generation|Towards Reliable AI-Assisted Analog Design: Template-Constrained LLM Agents for SAR ADC Generation]]
- **作者**: Dimple Vijay Kochar, Hae-Seung Lee, Anantha P. Chandrakasan
- **cs 子类**: cs.AI, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Towards Reliable AI-Assisted Analog Design: Template-Constrained LLM Agents for SAR ADC Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Large Language Models (LLMs) have demonstrated significant capability in software code generation, their application to analog Electronic Design Automation (EDA) is bottlenecked. Owing to limited circuit topology understanding and data, directly prompting LLMs and multimodal models leads to hallucinations and failure to produce schematics capable of passing rigorous SPICE simulations, as we show in our work. Instead, we propose an end-to-end, multi-step LLM agentic framework ATLAS, capable of generating a functional Successive Approximation Register (SAR) Analog-to-Digital Converter (ADC) that successfully passes simulation validation. To adhere to the rigid constraints of analog design, we utilize expert knowledge to ground the LLM in its planning, selection, parameterization, and iterative modification. As part of ATLAS, we introduce Template-Constrained Generation - which unlike other template-based works - builds towards a more generalized SAR ADC generation flow. We demonstrate a strong proof-of-concept of our framework by developing SAR ADCs across technology nodes and input specs. Overall, our expert-knowledge grounded multi-step agentic ATLAS establishes a pragmatic foundation for integrating LLMs into reliable analog design methodologies.

</details>

---

### [[20_Research/Papers/大模型/MemoHarness_Agent_Harnesses_That_Learn_from_Experience|MemoHarness: Agent Harnesses That Learn from Experience]]

![[assets/2607.14159_figure.png|800]]

- **arXiv**: [2607.14159](https://arxiv.org/abs/2607.14159)
- **PDF**: https://arxiv.org/pdf/2607.14159
- **详细分析**: [[20_Research/Papers/大模型/MemoHarness_Agent_Harnesses_That_Learn_from_Experience|MemoHarness: Agent Harnesses That Learn from Experience]]
- **作者**: Yue Huang, Wenjie Wang, Han Bao, Yuchen Ma, Xiaonan Luo, Yi Nian, Haomin Zhuang, Zheyuan Liu, Yue Zhao, Xiangliang Zhang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《MemoHarness: Agent Harnesses That Learn from Experience》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

An agent harness is the external control layer that turns a base LLM into an executable agent by managing context, tools, orchestration, memory, decoding, and output handling. While harness design strongly affects agent behavior, most automatic improvement methods optimize narrower artifacts such as prompts, pipelines, or workflows, and deployed agents usually reuse a single global harness for all cases. We introduce MemoHarness, an adaptive harness optimization framework that learns from its own executions. MemoHarness decomposes the harness into six editable control dimensions, stores per-case diagnoses and distilled global patterns in a dual-layer experience bank, and adapts the learned harness to each test case using retrieved experience without test-time labels, feedback, or additional search. In our evaluation across shell-agent, code-generation, and analytical-reasoning benchmarks, MemoHarness improves over the fixed harnesses we compare against and shows selective transfer to unseen suites and base models. Its additional context can also remain cost-competitive when much of the retrieved experience is cacheable. These results provide evidence that execution experience is a practical substrate for building agent harnesses that are more adaptive than a single static configuration, while leaving broader claims about statistical robustness and component attribution to future work.

</details>

---

### [[20_Research/Papers/大模型/ToolAnchor_Anchoring_Counterfactual_Context_to_Boost_Agentic_Tool-use_Capability|ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability]]

![[assets/2607.14145_figure.png|800]]

- **arXiv**: [2607.14145](https://arxiv.org/abs/2607.14145)
- **PDF**: https://arxiv.org/pdf/2607.14145
- **详细分析**: [[20_Research/Papers/大模型/ToolAnchor_Anchoring_Counterfactual_Context_to_Boost_Agentic_Tool-use_Capability|ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability]]
- **作者**: Weiting Liu, Jieyi Bi, Wanqi Zhou, Jianfeng Feng, Yining Ma, Ai Han, Wenlian Lu
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgentErrorBench, VDR-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-augmented large language model agents excel at long-horizon tasks, yet they are typically post-trained on fixed toolsets. When tasks demand new tools, these agents struggle to incorporate them effectively, and retraining from scratch is often impractical. We identify the core obstacle in such toolset expansion problem as behavioral inertia: the tendency of agents to fall back on familiar tools and established reasoning patterns despite having access to new ones. We demonstrate that injecting counterfactual anchor contexts at critical decision points can break this inertia, recovering failed trajectories by eliciting suppressed agent capabilities. To scale this insight, we propose ToolAnchor, a framework that uses teacher models to hypothesize these counterfactual contexts, verifies them via student rollouts, and internalizes the successful interventions through agentic post-training. Extensive evaluations across general AI assistant (GAIA), textual search (BrowseComp), and visual search (VDR-Bench) tasks demonstrate that ToolAnchor consistently exhibits competitive performance under expanded toolsets. Our work bridges the gap between static post-training and dynamic adaptation, charting a new path for scalable agentic reinforcement learning.

</details>

---

### [[20_Research/Papers/大模型/Interpretable_Language_Model_for_Closed-Loop_Type_1_Diabetes_Control|Interpretable Language Model for Closed-Loop Type 1 Diabetes Control]]

![[assets/2607.14126_figure.png|800]]

- **arXiv**: [2607.14126](https://arxiv.org/abs/2607.14126)
- **PDF**: https://arxiv.org/pdf/2607.14126
- **详细分析**: [[20_Research/Papers/大模型/Interpretable_Language_Model_for_Closed-Loop_Type_1_Diabetes_Control|Interpretable Language Model for Closed-Loop Type 1 Diabetes Control]]
- **作者**: Maya Sarkar
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.07（加权：大模型 0.55，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《Interpretable Language Model for Closed-Loop Type 1 Diabetes Control》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World, XRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Type 1 Diabetes (T1D) is a chronic, life-threatening autoimmune condition characterized by the complete destruction of insulin-producing pancreatic beta cells. While Artificial Pancreas Systems (APS) powered by Reinforcement Learning (RL) have shown promise in automating insulin delivery, their ``black-box'' nature makes it hard for patients and doctors to trust them fully. This paper presents LLM-T1D, a promising approach that combines the precision of RL with the clear, human-like reasoning of Large Language Models (LLMs) to create a more transparent and reliable insulin pump controller. By training an expert RL system and distilling its knowledge into fine-tuned LLaMA 3.1 8B and Qwen3 8B models, we developed a controller that not only surpasses the RL system's performance but also explains its decisions in plain, understandable language. Tested on the FDA-approved UVA/Padova T1D simulator, the LLM controllers deliver excellent blood sugar control (73.5% Time in Range) while maintaining strict formal safety verification against hallucinations.

</details>

---

### [[20_Research/Papers/大模型/CoEvoT_Co-Evolving_Chain-of-Thought_Prompting_for_Graph-LLM_Reasoning|CoEvoT: Co-Evolving Chain-of-Thought Prompting for Graph-LLM Reasoning]]

![[assets/2607.14114_figure.png|800]]

- **arXiv**: [2607.14114](https://arxiv.org/abs/2607.14114)
- **PDF**: https://arxiv.org/pdf/2607.14114
- **详细分析**: [[20_Research/Papers/大模型/CoEvoT_Co-Evolving_Chain-of-Thought_Prompting_for_Graph-LLM_Reasoning|CoEvoT: Co-Evolving Chain-of-Thought Prompting for Graph-LLM Reasoning]]
- **作者**: Haohua Niu, Xingtong Yu, Yang Liu, Junfeng Fang, Xuanting Xie, Jie Tan, Zhongjian Zhang, Hong Cheng, Yuan Fang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《CoEvoT: Co-Evolving Chain-of-Thought Prompting for Graph-LLM Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Graph learning under distribution shift presents a persistent challenge, where models adapt to new graphs with limited or even no supervision. Recent graph--LLM approaches move toward label-efficient prediction by linearizing graphs into prompts and using large language models (LLMs) as predictors, and can adopt Chain-of-Thought (CoT) prompting to exploit LLM's multi-step reasoning capability. However, existing CoT-based graph--LLM methods generate intermediate thoughts while conditioning on fixed graph tokens, limiting step-wise refinement of structural cues. In this paper, we propose CoEvoT, a simple yet effective co-evolving CoT prompting framework for graph--LLM reasoning. CoEvoT couples text-to-graph token rewriting and graph-to-text reasoning guidance in a closed loop: each intermediate textual thought is used to update the graph token evidence state via a lightweight condition network, and the updated tokens are fed back into the next-step instruction to guide subsequent LLM reasoning. This enables step-wise, state-aware evidence refinement, rather than reasoning over a fixed graph snapshot. Extensive experiments on eight datasets demonstrate that CoEvoT consistently outperforms state-of-the-art baselines.

</details>

---

### [[20_Research/Papers/大模型/Simplicity_Paradox_Debunking_myths_about_prompting_and_datasets_for_LLM_evaluation|Simplicity Paradox: Debunking myths about prompting and datasets for LLM evaluation]]

![[assets/2607.14109_first_page.png|800]]

- **arXiv**: [2607.14109](https://arxiv.org/abs/2607.14109)
- **PDF**: https://arxiv.org/pdf/2607.14109
- **详细分析**: [[20_Research/Papers/大模型/Simplicity_Paradox_Debunking_myths_about_prompting_and_datasets_for_LLM_evaluation|Simplicity Paradox: Debunking myths about prompting and datasets for LLM evaluation]]
- **作者**: Inder Preet, Shuxin Lin, Dhaval Patel
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM

#### 研究背景与动机

《Simplicity Paradox: Debunking myths about prompting and datasets for LLM evaluation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MCQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Probing the capabilities of Large Language Models (LLMs) and building robust solutions for Multiple-Choice Question Answering (MCQA) remain central challenges in natural language understanding. Furthermore, the rapid proliferation of LLMs has created the implicit assumption that more sophisticated prompting techniques yield better performance. Several studies claim better performance with more sophisticated prompting techniques, but do not provide a comprehensive evaluation. We address this gap through a comprehensive empirical study of 8 prompting techniques across 10 multiple-choice question answering (MCQA) datasets, encompassing 27 model configurations and roughly 4,300 unique questions evaluated more than 430,000 times. Our findings reveal a striking paradox that baseline prompting consistently outperforms complex reasoning techniques on various benchmarks. Only minimal expert and inductive role framing (CoT-Expert and CoT-Inductive) yields a small but statistically significant $\sim$3 percentage-point (pp) gain over baseline whereas every other elaborate technique we tested matches or under-performs it, often by large margins (up to 31~pp for Self-Analogical). We further investigate three critical phenomena: (1) the unexpected victory of Qwen3-30B-A3B-Thinking-2507 in Elo ratings, (2) the performance-efficiency trade-offs across model variants with different thinking budgets, revealing model-dependent optimal configurations, and (3) the substantial variation in dataset difficulty, with 60% of benchmarks below 70% accuracy and a 47.5~pp spread from easiest to hardest, indicating considerable room for model improvement. These results suggest that the LLM evaluation community may be overcomplicating prompt engineering and that substantial performance gaps remain across diverse benchmarks, offering opportunities for genuine model improvements rather than prompt optimization.

</details>

---

### [[20_Research/Papers/大模型/HG-RAG_Hierarchy-Guided_Retrieval-Augmented_Generation_for_Structured_Knowledge_Graphs|HG-RAG: Hierarchy-Guided Retrieval-Augmented Generation for Structured Knowledge Graphs]]

![[assets/2607.14095_figure.png|800]]

- **arXiv**: [2607.14095](https://arxiv.org/abs/2607.14095)
- **PDF**: https://arxiv.org/pdf/2607.14095
- **详细分析**: [[20_Research/Papers/大模型/HG-RAG_Hierarchy-Guided_Retrieval-Augmented_Generation_for_Structured_Knowledge_Graphs|HG-RAG: Hierarchy-Guided Retrieval-Augmented Generation for Structured Knowledge Graphs]]
- **作者**: Pranav Yadav
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM

#### 研究背景与动机

《HG-RAG: Hierarchy-Guided Retrieval-Augmented Generation for Structured Knowledge Graphs》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：KGQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval Augmented Generation (RAG) has proven to be a widely successful process at improving the quality of outputs from a Large Language Model (LLM) for wider context. However, RAG systems typically retrieve context from flat document stores, which struggles when queries require hierarchical or relational reasoning across structured knowledge. I present HG-RAG (Hierarchy-Guided RAG), a framework that performs graph-traversal over a hierarchical knowledge graph to deliver structured context to a language model. My retrieval pipeline resolves a named entity anchor from the query, then expands context upward through parent nodes, laterally through relational neighbors, and downward through child nodes when needed. I evaluate HG-RAG against a dense retrieval baseline across three world scales (18-800 nodes) with four query types: local fact, hierarchical, neighborhood, and multi-hop. Results show HG-RAG consistently outperforms the flat baseline on hierarchical, relational, and multi-hop reasoning tasks, while reducing hallucination and maintaining locality coherence.

</details>

---

### [[20_Research/Papers/强化学习/Intelligent_Three_Level_Learning_Architecture_for_Autonomous_UAV_Swarms_in_Search_and_Rescue|Intelligent Three Level Learning Architecture for Autonomous UAV Swarms in Search and Rescue]]

![[assets/2607.14093_first_page.png|800]]

- **arXiv**: [2607.14093](https://arxiv.org/abs/2607.14093)
- **PDF**: https://arxiv.org/pdf/2607.14093
- **详细分析**: [[20_Research/Papers/强化学习/Intelligent_Three_Level_Learning_Architecture_for_Autonomous_UAV_Swarms_in_Search_and_Rescue|Intelligent Three Level Learning Architecture for Autonomous UAV Swarms in Search and Rescue]]
- **作者**: Oleksii Bychkov
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，强化学习 0.2，机器人 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Intelligent Three Level Learning Architecture for Autonomous UAV Swarms in Search and Rescue》归入 机器人、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a novel three level hierarchical learning architecture for autonomous UAV swarms performing search and rescue operations. Unlike conventional approaches that apply a single learning paradigm across all hierarchy levels, the proposed architecture integrates three qualitatively different learning mechanisms corresponding to the biological hierarchy of reflexes, skills, and reasoning such as Hebbian neuroplasticity for individual agent adaptation, multi agent reinforcement learning with graph neural networks and behavior trees for tactical coordination, and model agnostic meta learning with BDI reasoning and a digital twin for strategic decision making. The architecture is formalized through twenty two architectural contracts organized across six components such as BDI, Behavior Trees, GNN, MARL, Neuroplasticity, Meta Learning that collectively provide six classes of formal guarantees such as safety, budget correctness, optimality, liveness, starvation freedom, and inter level consistency. We introduce Swarm Meta Cognition as a compositional property arising from the structured interaction of all three levels, enabling the swarm to monitor its own cognitive state and switch between cognitive strategies. Five constructive progress functions for SAR task types bridge the gap between abstract optimization theory and concrete operational scenarios. The main integration theorem establishes that when all contracts are satisfied, the hybrid neuro-symbolic system preserves all six guarantee classes. For the dynamic case with active learning, five new contracts extend the framework with three additional guarantees such as cognitive resilience, graceful degradation, and monotonic meta improvement. Theoretical analysis demonstrates that the architecture addresses five fundamental limitations of existing hierarchical RL approaches.

</details>

---
