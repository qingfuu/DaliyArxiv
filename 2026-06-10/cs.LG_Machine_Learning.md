# cs.LG | Machine Learning | 2026-06-10

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/强化学习/Flow-DPPO_Divergence_Proximal_Policy_Optimization_for_Flow_Matching_Models|Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models]]

![[assets/2606.11025_figure.png|800]]

- **arXiv**: [2606.11025](https://arxiv.org/abs/2606.11025)
- **PDF**: https://arxiv.org/pdf/2606.11025
- **详细分析**: [[20_Research/Papers/强化学习/Flow-DPPO_Divergence_Proximal_Policy_Optimization_for_Flow_Matching_Models|Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models]]
- **作者**: Bowen Ping, Xiangxin Zhou, Penghui Qi, Minnan Luo, Liefeng Bo, Tianyu Pang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：UniRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work has demonstrated that online reinforcement learning (RL) can substantially improve the quality and alignment of flow matching models for image and video generation. Methods such as Flow-GRPO and CPS cast the denoising process as a Markov Decision Process and apply PPO-style ratio clipping to enforce a trust region. However, we argue that ratio clipping is structurally ill-suited for flow models: the probability ratio between new and old policies is a noisy, single-sample estimate of the true policy divergence, leading to over-constraining in some regions of the trajectory and under-constraining in others. We propose Flow-DPPO (Flow Divergence Proximal Policy Optimization), which replaces ratio clipping with a divergence proximal constraint. A key observation is that the per-step policy in flow models is Gaussian, enabling exact and cheap computation of the KL divergence between old and new policies. Flow-DPPO employs an asymmetric divergence mask that blocks gradient updates only when they simultaneously move away from the trusted region and violate the divergence threshold. Experiments show that Flow-DPPO achieves higher rewards with better KL-proximal efficiency, alleviates catastrophic forgetting, promotes balanced multi-objective optimization, and enables stable multi-epoch training where ratio clipping degrades. Code and models are available at https://github.com/Tencent-Hunyuan/UniRL/tree/main/FlowDPPO.

</details>

---

### [[20_Research/Papers/强化学习/Task_Robustness_via_Re-Labelling_Vision-Action_Robot_Data|Task Robustness via Re-Labelling Vision-Action Robot Data]]

![[assets/2606.10918_figure.png|800]]

- **arXiv**: [2606.10918](https://arxiv.org/abs/2606.10918)
- **PDF**: https://arxiv.org/pdf/2606.10918
- **详细分析**: [[20_Research/Papers/强化学习/Task_Robustness_via_Re-Labelling_Vision-Action_Robot_Data|Task Robustness via Re-Labelling Vision-Action Robot Data]]
- **作者**: Artur Kuramshin, Özgür Aslan, Cyrus Neary, Glen Berseth
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Task Robustness via Re-Labelling Vision-Action Robot Data》归入 机器人、具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The recent trend in scaling models for robot learning has resulted in impressive policies that can perform various manipulation tasks and generalize to novel scenarios. However, these policies continue to struggle with following instructions, likely due to the limited linguistic and action sequence diversity in existing robotics datasets. This paper introduces Task Robustness via Re-Labelling Vision-Action Robot Data (TREAD), a scalable framework that leverages large Vision-Language Models (VLMs) to augment existing robotics datasets without additional data collection, harnessing the transferable knowledge embedded in these models. Our approach leverages a pretrained VLM through three stages: generating semantic sub-tasks from original instruction labels and initial scenes, segmenting demonstration videos conditioned on these sub-tasks, and producing diverse instructions that incorporate object properties, effectively decomposing longer demonstrations into grounded language-action pairs. We further enhance robustness by augmenting the data with linguistically diverse versions of the text goals. Evaluations on LIBERO demonstrate that policies trained on our augmented datasets exhibit improved performance on novel, unseen tasks and goals. Our results show that TREAD enhances both planning generalization through trajectory decomposition and language-conditioned policy generalization through increased linguistic diversity.

</details>

---

### [[20_Research/Papers/强化学习/Embodiment-conditioned_Generalist_Control_for_Multirotor_Aerial_Robots|Embodiment-conditioned Generalist Control for Multirotor Aerial Robots]]

![[assets/2606.10857_figure.png|800]]

- **arXiv**: [2606.10857](https://arxiv.org/abs/2606.10857)
- **PDF**: https://arxiv.org/pdf/2606.10857
- **详细分析**: [[20_Research/Papers/强化学习/Embodiment-conditioned_Generalist_Control_for_Multirotor_Aerial_Robots|Embodiment-conditioned Generalist Control for Multirotor Aerial Robots]]
- **作者**: Orestis Konstantaropoulos, Welf Rehberg, Mihir Kulkarni, Kostas Alexis
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.32（加权：具身智能 0.3，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Embodiment-conditioned Generalist Control for Multirotor Aerial Robots》归入 机器人、强化学习、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a generalist position control policy capable of controlling arbitrary multirotor configurations of a certain rotor count (e.g., hexarotors or quadrotors) with a single set of network weights. The policy is conditioned on a physics-grounded embodiment descriptor: a mass and inertia-normalized control allocation matrix that captures how mass-normalized motor thrusts generate linear and angular accelerations in the body-frame. To train the policy, we sample from a broad distribution of arbitrary multirotor configurations, including non-planar and asymmetric systems, and optimize a single, compact network using Proximal Policy Optimization. Training requires only five minutes on an RTX 3090 GPU using a custom NVIDIA Warp-based dynamics simulator. Through extensive simulation experiments, we show that embodiment conditioning enables robust generalist control across arbitrary morphologies. We demonstrate zero-shot real-world transfer of this generalist policy on three diverse hexarotor systems, including a planar robot, a partially symmetric non-planar system, and a random asymmetric, non-planar configuration.

</details>

---

### [[20_Research/Papers/强化学习/MODIP_Efficient_Model-Based_Optimization_for_Diffusion_Policies|MODIP: Efficient Model-Based Optimization for Diffusion Policies]]

![[assets/2606.10825_figure.png|800]]

- **arXiv**: [2606.10825](https://arxiv.org/abs/2606.10825)
- **PDF**: https://arxiv.org/pdf/2606.10825
- **详细分析**: [[20_Research/Papers/强化学习/MODIP_Efficient_Model-Based_Optimization_for_Diffusion_Policies|MODIP: Efficient Model-Based Optimization for Diffusion Policies]]
- **作者**: Zakariae El Asri, Philippe Gratias-Quiquandon, Nicolas Thome, Olivier Sigaud
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 机器人
- **相关性评分**: 0.92（加权：强化学习 0.36，世界模型 0.36，机器人 0.2）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《MODIP: Efficient Model-Based Optimization for Diffusion Policies》归入 强化学习、世界模型、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：D4RL, DSRL, MBRL, PA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion policies (DPs) have emerged as expressive policy representations for robot learning, often used with imitation learning methods such as behavioral cloning (BC). However, while their success has largely been confined to BC, direct reinforcement learning (RL) fine-tuning remains challenging because actions are generated through a multi-step denoising process. In this work, we propose MODIP, a framework for the offline-to-online fine-tuning of DPs. Rather than directly applying RL to the DPs, MODIP leverages a world model (WM) to guide policy adaptation and keeps the simplicity and stability of BC. We utilize model predictive control (MPC) to generate high-quality trajectories within the WM, and use them as supervised targets for fine-tuning the DP. To make MPC planning efficient, MODIP uses a terminal state value instead of a policy-dependent state-action value, reducing inference time. Additionally, MODIP trains critics with policy-independent TD targets, reducing training time. Experiments on D4RL (MuJoCo, Kitchen) and RoboMimic tasks show that MODIP improves diffusion policies beyond BC, and is competitive with or outperforms diffusion policy RL fine-tuning methods and strong model-based baselines such as TD-MPC2.

</details>

---

### [[20_Research/Papers/强化学习/On-sky_demonstration_of_reinforcement_learning_for_adaptive_optics_control|On-sky demonstration of reinforcement learning for adaptive optics control]]

![[assets/2606.10771_first_page.png|800]]

- **arXiv**: [2606.10771](https://arxiv.org/abs/2606.10771)
- **PDF**: https://arxiv.org/pdf/2606.10771
- **详细分析**: [[20_Research/Papers/强化学习/On-sky_demonstration_of_reinforcement_learning_for_adaptive_optics_control|On-sky demonstration of reinforcement learning for adaptive optics control]]
- **作者**: Jalo Nousiainen, Vincent Chambouleyron, Benoit Neichel, Sylvain Cetre, Jean-Francois Sauvage, Angelie Alagao, Markus Kasper, Jonathan Dray, Romain Fetick, Byron Engler
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《On-sky demonstration of reinforcement learning for adaptive optics control》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL)-based algorithms have recently emerged as a promising approach for adaptive optics (AO) control. In simulations and laboratory experiments, they have demonstrated robustness to real-world effects such as photon and detector noise, misregistration, vibrations, and rapid variations in seeing conditions. However, their performance has not yet been validated on sky. We report the first on-sky demonstration of a reinforcement learning controller for adaptive optics, named Policy Optimization for AO (PO4AO). We further analyze its on-sky behavior and identify directions for improving the algorithm and its implementation.PO4AO was implemented and deployed on the Papyrus adaptive optics system installed at the Coudé focus of the 1.52 m telescope (T152) at the OHP. A Python-based implementation was interfaced with the existing real-time controller (DAO RTC) via shared-memory buffers. The performance of PO4AO was compared to that of a standard integrator controller over several nights, covering a range of flux levels and atmospheric conditions. PO4AO consistently outperformed the standard integrator in all tested configurations. The controller successfully learned and compensated for vibration patterns and demonstrated strong robustness to measurement noise. Once tuned for Papyrus, PO4AO operated in a turnkey fashion, using a single set of hyperparameters across varying observing conditions and science targets. These performance gains were achieved despite a non-optimized Python implementation introducing approximately $750\,μ\text{s}$ of additional latency, along with control jitter and occasional frame drops. When properly implemented and optimized, PO4AO constitutes a robust and high-performance turnkey controller for single-conjugate adaptive optics systems, paving the way for broader adoption of reinforcement learning strategies in on-sky AO operations.

</details>

---

### [[20_Research/Papers/强化学习/Discovering_Interpretable_Multi-Parameter_Control_Policies_for_Evolutionary_Algorithms_Using_Deep_Reinforcement_Learning|Discovering Interpretable Multi-Parameter Control Policies for Evolutionary Algorithms Using Deep Reinforcement Learning]]

![[assets/2606.10129_figure.png|800]]

- **arXiv**: [2606.10129](https://arxiv.org/abs/2606.10129)
- **PDF**: https://arxiv.org/pdf/2606.10129
- **详细分析**: [[20_Research/Papers/强化学习/Discovering_Interpretable_Multi-Parameter_Control_Policies_for_Evolutionary_Algorithms_Using_Deep_Reinforcement_Learning|Discovering Interpretable Multi-Parameter Control Policies for Evolutionary Algorithms Using Deep Reinforcement Learning]]
- **作者**: Tai Nguyen, Phong Le, Carola Doerr, Nguyen Dang
- **cs 子类**: cs.LG, cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 2.12（加权：强化学习 1.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Discovering Interpretable Multi-Parameter Control Policies for Evolutionary Algorithms Using Deep Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Deep-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While deep Reinforcement Learning (deep-RL) has been increasingly applied to parameter control in evolutionary algorithms, rigorous theoretical analysis of parameter control remains largely restricted to single-parameter settings, owing to the difficulty of deriving effective, interpretable multi-parameter policies amenable to formal study. We demonstrate how deep-RL can be leveraged to overcome this barrier, using the (1+($λ$,$λ$))-genetic algorithm optimizing OneMax, one of the few problems where a super-constant speedup of dynamic control has been formally proven, as a representative case study. We first show that standard approaches struggle to converge in this multi-parameter setting, and introduce algorithm-agnostic enhancements targeting action-space decomposition, reward shifting, and long-horizon discounting. With these in place, we compare common deep-RL methods and find that Double Deep Q-Networks uniquely avoid the policy collapse observed in Proximal Policy Optimization, yielding trajectories suitable for downstream analysis. Crucially, we move beyond the ``black-box'' nature of neural networks by distilling the learned behaviors into a transparent, symbolic control policy. This resulting policy does not only offer interpretability for future theoretical analysis but also yields exceptional performance, consistently outperforming existing baselines across a wide range of problem sizes.

</details>

---

### [[20_Research/Papers/大模型/From_Confident_Closing_to_Silent_Failure_Characterizing_False_Success_in_LLM_Agents|From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents]]

![[assets/2606.09863_figure.png|800]]

- **arXiv**: [2606.09863](https://arxiv.org/abs/2606.09863)
- **PDF**: https://arxiv.org/pdf/2606.09863
- **详细分析**: [[20_Research/Papers/大模型/From_Confident_Closing_to_Silent_Failure_Characterizing_False_Success_in_LLM_Agents|From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents]]
- **作者**: Laksh Advani
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgentBench, AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents can fail silently by asserting task completion when the environment state shows otherwise. We study this failure mode, false success, across two agent benchmarks: 9,876 tau2-bench trajectories from 8 model families and 1,879 AppWorld trajectories from 4 model families with text-independent ground truth. False success is common but varies by setting: 45--48% of failures in single-control tau2-bench domains, 3% in dual-control telecom, and 75.8% among AppWorld self-assessing coding-agent trajectories with explicit status claims. LLM judges fail reliably: no configuration across 5 judges, 5 prompt strategies, and full task specifications exceeds AUROC 0.65 on tau2-bench, and the same judges reach only 0.54 AUROC on AppWorld API-call traces. Judges rely on surface completion proxies -- confident closing language in tau2-bench and coarse action-sequence volume in AppWorld -- rather than verified state changes. Lightweight TF-IDF detectors achieve task-disjoint AUROC 0.83 on tau2-bench and 0.95 on AppWorld, recovering 4--8x more false successes than the best judge at the same flag rate with 3,300x lower latency. These results suggest that production monitoring should use lightweight, domain-calibrated detectors as triage signals rather than relying on LLM judges as the primary monitor for false success.

</details>

---

### [[20_Research/Papers/强化学习/Multi-parameter_Control_for_the_$(1+(λ,λ))$-GA_on_OneMax_via_Deep_Reinforcement_Learning|Multi-parameter Control for the $(1+(λ,λ))$-GA on OneMax via Deep Reinforcement Learning]]

![[assets/2505.12982_first_page.png|800]]

- **arXiv**: [2505.12982](https://arxiv.org/abs/2505.12982)
- **PDF**: https://arxiv.org/pdf/2505.12982
- **详细分析**: [[20_Research/Papers/强化学习/Multi-parameter_Control_for_the_$(1+(λ,λ))$-GA_on_OneMax_via_Deep_Reinforcement_Learning|Multi-parameter Control for the $(1+(λ,λ))$-GA on OneMax via Deep Reinforcement Learning]]
- **作者**: Tai Nguyen, Phong Le, Carola Doerr, Nguyen Dang
- **cs 子类**: cs.LG, cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Multi-parameter Control for the $(1+(λ,λ))$-GA on OneMax via Deep Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

It is well known that evolutionary algorithms can benefit from dynamic choices of the key parameters that control their behavior, to adjust their search strategy to the different stages of the optimization process. A prominent example where dynamic parameter choices have shown a provable super-constant speed-up is the $(1+(λ,λ))$ Genetic Algorithm optimizing the OneMax function. While optimal parameter control policies result in linear expected running times, this is not possible with static parameter choices. This result has spurred a lot of interest in parameter control policies. However, many works, in particular theoretical running time analyses, focus on controlling one single parameter. Deriving policies for controlling multiple parameters remains very challenging. In this work we reconsider the problem of the $(1+(λ,λ))$ Genetic Algorithm optimizing OneMax. We decouple its four main parameters and investigate how well state-of-the-art deep reinforcement learning techniques can approximate good control policies. We show that although making deep reinforcement learning learn effectively is a challenging task, once it works, it is very powerful and is able to find policies that outperform all previously known control policies on the same benchmark. Based on the results found through reinforcement learning, we derive a simple control policy that consistently outperforms the default theory-recommended setting by $27\%$ and the irace-tuned policy, the strongest existing control policy on this benchmark, by $13\%$, for all tested problem sizes up to $40{,}000$.

</details>

---
