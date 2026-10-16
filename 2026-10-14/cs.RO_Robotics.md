# cs.RO | Robotics | 2026-10-14

#arxiv #ComputerScience

**论文数**: 38

### [[20_Research/Papers/具身智能/EmbodiedEvo_Self-improving_Coding_Agents_for_Physical_Intelligence|EmbodiedEvo: Self-improving Coding Agents for Physical Intelligence]]

![[assets/2610.18867_figure.png|800]]

- **arXiv**: [2610.18867](https://arxiv.org/abs/2610.18867)
- **PDF**: https://arxiv.org/pdf/2610.18867
- **详细分析**: [[20_Research/Papers/具身智能/EmbodiedEvo_Self-improving_Coding_Agents_for_Physical_Intelligence|EmbodiedEvo: Self-improving Coding Agents for Physical Intelligence]]
- **作者**: Wenyi Li, Yizhe Chi, Youjie Zheng, Chunyu Liu, Xiaoqiu Wang, Mingju Gao, Zheng Jiang, Deyao Hong, Calvin Xiao, Kaisen Yang, Qinhuai Na
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.5，机器人 0.3）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《EmbodiedEvo: Self-improving Coding Agents for Physical Intelligence》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, RoboDojo-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bringing general-purpose agents into the physical world calls for an executable representation of physical intelligence. Compared with vision-language-action (VLA) models, which map observations and language instructions directly to actions, code makes control logic explicit and reusable. Code can serve not only as a policy representation but also as the workspace in which the agent solves a task. Rather than following a prescribed workflow of planning, execution, and verification, the agent can autonomously inspect the state, revise and execute code, and use feedback to choose the next step. The success of this SWE-style loop in digital environments motivates its extension to physical tasks. Yet physical execution remains prone to recurring failures. To retain and refine experience for later scenes, we introduce EmbodiedEvo, where a coding agent evolves reusable Skills and Lessons through feedback on a single Playground scene, then freezes the resulting harness for diverse new scenes. On RoboDojo-Sim, EmbodiedEvo achieves an average score of 44.48 and a success rate of 37.82\%, surpassing all officially verified results. Paired tests show the largest gains on memory-dependent tasks and successful reuse of coordinated procedures, while fine contact control remains difficult. Experience from stronger models also improves weaker executors: Astra's experience raises Sol and Luna's success rates by 8.86 and 5.50 percentage points over no experience. Compared with raw interaction history, Skills and Lessons achieve comparable task performance at 53.0\% lower execution cost.

</details>

---

### [[20_Research/Papers/强化学习/EgoMatrix_Physically_Faithful_Dexterous_Robot_Demonstrations_from_Egocentric_Human_Videos|EgoMatrix: Physically Faithful Dexterous Robot Demonstrations from Egocentric Human Videos]]

![[assets/2610.18822_figure.jpg|800]]

- **arXiv**: [2610.18822](https://arxiv.org/abs/2610.18822)
- **PDF**: https://arxiv.org/pdf/2610.18822
- **详细分析**: [[20_Research/Papers/强化学习/EgoMatrix_Physically_Faithful_Dexterous_Robot_Demonstrations_from_Egocentric_Human_Videos|EgoMatrix: Physically Faithful Dexterous Robot Demonstrations from Egocentric Human Videos]]
- **作者**: Ziheng Wang, Yanming Shao, Ting Mao, Kaihan Chen, Yiqun Wang, Xuanye Wu, Yao Mu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《EgoMatrix: Physically Faithful Dexterous Robot Demonstrations from Egocentric Human Videos》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Egocentric human videos offer a scalable alternative to robot teleoperation for collecting dexterous manipulation data. However, two challenges limit their use as reliable training data: accurate hand-object interaction (HOI) reconstruction from monocular RGB and high-quality robot demonstrations, especially visual observations. We present EgoMatrix, an end-to-end data engine that converts monocular egocentric human videos into bimanual dexterous trajectories and paired robot observation videos, with the trajectories directly replayable on real robots. It reconstructs HOI with emphasis on relative geometry and contact rather than exact metric scene recovery, then uses retargeting and reinforcement learning (RL) to reproduce the demonstrated tasks in simulation. We jointly render robot hands and objects from these simulated trajectories to produce physically faithful observations synchronized with state and control records. Rendering the same trajectories in diverse, task-compatible backgrounds expands paired training data while preserving robot-object motion and contact. Across TACO, OakInk2, and self-collected data, EgoMatrix achieves 54.84% end-to-end success in simulation versus 14.52% for the strongest baseline. Reconstruction reaches state-of-the-art performance on most metrics of the two public benchmarks. Qualitative results show more faithful hand-object interactions than prior methods, while feature-space analysis shows closer alignment with real-robot observations than GPT-6 Astra. Our project page is available at https://spikew726.github.io/EgoMatrix/.

</details>

---

### [[20_Research/Papers/具身智能/EqC_Equilibrium_Energy_Control_for_Introspective_Lifelong_Robot_Learning|EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning]]

![[assets/2610.18790_figure.png|800]]

- **arXiv**: [2610.18790](https://arxiv.org/abs/2610.18790)
- **PDF**: https://arxiv.org/pdf/2610.18790
- **详细分析**: [[20_Research/Papers/具身智能/EqC_Equilibrium_Energy_Control_for_Introspective_Lifelong_Robot_Learning|EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning]]
- **作者**: Haodong Yang, Runhan Huang, Bowen Zhang, Iofai Lei, Zunzhe Zhang, Xiangcheng Zhang, Shaoting Zhu, Linzhan Mou, Yicheng Liu, Hang Zhao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term robot autonomy depends on more than effective action generation: a policy must recognize when its behavior is no longer sufficiently supported and use assistance to improve. We introduce Equilibrium Energy Control (EqC), a framework for introspective lifelong robot learning built around an explicit conditional energy landscape. EqC casts generative action refinement as equilibrium-seeking optimization, while the geometry of the refinement process reveals whether the generated behavior remains consistent with the learned landscape. This competence signal enables Energy-Gated DAgger, where persistent energy-consistency violations trigger expert takeover and the resulting recovery trajectories are aggregated for subsequent policy updates. EqC integrates naturally into both Diffusion Transformer policies and flow-matching-based vision-language-action (VLA) policies. Across simulation and real-world bimanual manipulation, EqC matches or improves control performance and robustness while enabling timely intervention near the policy's competence boundary. A real-world study further shows how these interventions progressively expand the range of situations handled autonomously, providing a practical path from static generative controllers toward self-improving robot systems.

</details>

---

### [[20_Research/Papers/具身智能/GreenWAM_A_World_Foundation_Model_for_Robotics|GreenWAM: A World Foundation Model for Robotics]]

![[assets/2610.18774_first_page.png|800]]

- **arXiv**: [2610.18774](https://arxiv.org/abs/2610.18774)
- **PDF**: https://arxiv.org/pdf/2610.18774
- **详细分析**: [[20_Research/Papers/具身智能/GreenWAM_A_World_Foundation_Model_for_Robotics|GreenWAM: A World Foundation Model for Robotics]]
- **作者**: Gennady Sidorov, Valerii Kornilov, Denis Grankin, Polina Fedotova, Aleksey Postnikov
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型, 世界模型
- **相关性评分**: 3.3（加权：具身智能 1.2，大模型 0.4，世界模型 0.2，机器人 1.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《GreenWAM: A World Foundation Model for Robotics》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions. Models are usually built and evaluated for only one of these roles, and every robot records its actions in its own format. We ask whether one robot world model can serve both roles across different bodies, and what makes this work. We present GreenWAM, a world foundation model for robotics, together with the recipe that produces it: (1) a shared anatomical action space that describes 20 robot families, from bimanual arms to dexterous humanoids, in common joint coordinates; (2) joint training on these families in visual, action-conditioned and world-action modes; and (3) policies that split an action expert off the generator. As a world model, GreenWAM attains top-tier trajectory, depth and 3D accuracy on WorldArena 1.0, ahead of every world-action model and video generator in our comparison. As a policy, it scores among the top entries of the RoboTwin 2.0 leaderboard, reaches the highest zero-shot LIBERO-plus success among the compared methods and is competitive with dedicated vision-language-action and world-action policies on CALVIN and LIBERO. We further adapt GreenWAM to a real humanoid, where it succeeds more often than policies adapted from $π_{0.5}$ and from Cosmos 3 Edge, and distill it into a single-step policy for real-time control. Controlled experiments yield three findings: robot specialization improves world prediction and control together; an action expert helps when split off at the start of adaptation; and keeping world-model modes during policy adaptation preserves robustness to scene changes.

</details>

---

### [[20_Research/Papers/具身智能/ForkCast_Predictive_Recovery_for_Vision-Language-Action_Policies_via_Counterfactual_Futures|ForkCast: Predictive Recovery for Vision-Language-Action Policies via Counterfactual Futures]]

![[assets/2610.18650_figure.png|800]]

- **arXiv**: [2610.18650](https://arxiv.org/abs/2610.18650)
- **PDF**: https://arxiv.org/pdf/2610.18650
- **详细分析**: [[20_Research/Papers/具身智能/ForkCast_Predictive_Recovery_for_Vision-Language-Action_Policies_via_Counterfactual_Futures|ForkCast: Predictive Recovery for Vision-Language-Action Policies via Counterfactual Futures]]
- **作者**: Chenru Wen, Huajian Zeng, Haokai Ding, Jian Kang, Anqing Duan, Dawei Zhou, Dezhen Song, Xingxing Zuo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.5（加权：具身智能 1.8，世界模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ForkCast: Predictive Recovery for Vision-Language-Action Policies via Counterfactual Futures》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies perform manipulation tasks using camera images and language instructions, but object slip or visual occlusion can disrupt execution. Recovery is typically learned during policy training or delegated to a monitor that triggers a scripted repair after detecting a failure. We introduce ForkCast, a predictive recovery framework that compares counterfactual futures to determine whether and how to intervene in a frozen VLA policy. At each decision point, ForkCast evaluates three candidates: executing the policy's nominal action chunk (Commit), adjusting the camera viewpoint (Reobserve), and replanning the arm trajectory (Replan). A candidate-conditioned world model forecasts the latent outcome of each candidate at a common future horizon, and a shared task-progress head scores the predicted outcomes. By evaluating the policy's own continuation alongside the repair candidates, a single comparison based on task progress determines both whether and how to intervene, without a failure detector, an intervention threshold, or updates to the VLA backbone. On five simulated RoboTwin 2.0 tasks with injected occlusion and object slip, ForkCast increases pooled success from 13.3% for the frozen $π_{0.5}$ policy to 30.0% and transfers to two additional VLA backbones without updating ForkCast. After adaptation on real-robot candidate rollouts, ForkCast also improves success over the base policy under both clean and visibility-limited conditions. Code will be released to benefit the research community.

</details>

---

### [[20_Research/Papers/具身智能/WAVE-0_Bridging_VLA_Policies_and_WAMs_with_Lightweight_Latent_Future_Prediction|WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction]]

![[assets/2610.18568_first_page.png|800]]

- **arXiv**: [2610.18568](https://arxiv.org/abs/2610.18568)
- **PDF**: https://arxiv.org/pdf/2610.18568
- **详细分析**: [[20_Research/Papers/具身智能/WAVE-0_Bridging_VLA_Policies_and_WAMs_with_Lightweight_Latent_Future_Prediction|WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction]]
- **作者**: Haomin Wang, Anqiong Ji, Ke Wang, Zhongshan Liu, Ru Ying, Ran Zheng, Zhipeng Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 3.1（加权：具身智能 2.1，大模型 0.1，世界模型 0.2，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies excel at generalist robotic manipulation but generate actions without explicitly modeling their environmental consequences. World action models (WAMs) incorporate future prediction, yet most rely on costly video generation, while latent alternatives either use predicted futures only as auxiliary targets or infer latent actions from suboptimal visual transitions through costly large-scale video pretraining. We introduce WAVE-0 (World-model-Augmented VLA Execution), a framework that bridges VLAs and WAMs through a lightweight latent world model. By connecting the semantic understanding of pretrained VLAs with explicit future prediction, WAVE-0 allows anticipated action consequences to directly guide action generation. Built on a pretrained VLA, its 257M world model translates VLM-generated latent action plans into predicted future representations that condition the action expert, unifying latent planning, future prediction, and action generation. The world model is trained directly on ground-truth robot actions with a counterfactual ranking objective, requiring neither pixel reconstruction nor large-scale video pretraining. WAVE-0 achieves success rates of 91.47% on RoboTwin 2.0 and 98.7% on LIBERO, along with 88.0%, 61.4%, and 75.0% on LIBERO-Plus, LIBERO-Pro, and LIBERO-Para, respectively. On real-world tasks, it improves the success rate of $π_{0.5}$ from 38.3% to 73.3%. These results demonstrate strong manipulation performance and generalization across diverse distribution shifts.

</details>

---

### [[20_Research/Papers/强化学习/CALM_Decentralized_Control_of_Cooperative_Aerial_Manipulation_with_Multi-Agent_Reinforcement_Learning|CALM: Decentralized Control of Cooperative Aerial Manipulation with Multi-Agent Reinforcement Learning]]

![[assets/2610.18425_figure.jpg|800]]

- **arXiv**: [2610.18425](https://arxiv.org/abs/2610.18425)
- **PDF**: https://arxiv.org/pdf/2610.18425
- **详细分析**: [[20_Research/Papers/强化学习/CALM_Decentralized_Control_of_Cooperative_Aerial_Manipulation_with_Multi-Agent_Reinforcement_Learning|CALM: Decentralized Control of Cooperative Aerial Manipulation with Multi-Agent Reinforcement Learning]]
- **作者**: Jiaxi Huo, Petre Ricioppo, Fausto Francesco Lizzio
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 大模型, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，大模型 0.4，强化学习 1，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《CALM: Decentralized Control of Cooperative Aerial Manipulation with Multi-Agent Reinforcement Learning》归入 强化学习、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CrazyMARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative aerial manipulation is difficult under wind, payload motion, and noisy goal broadcasts because multiple Unmanned Aerial Vehicles (UAVs) are coupled through a shared payload. We present CALM (Cooperative Aerial Learned Manipulation), a decentralized controller for aerial manipulators carrying a basket while tracking a moving ground robot. CALM combines a parameter-shared Multi-Agent Reinforcement Learning (MARL) policy, trained using Multi-Agent Proximal Policy Optimization (MAPPO), with goal estimation, per-UAV Extended State Observers (ESOs), basket-mass estimation, and anticipatory formation-yaw feedforward. The anticipatory formation-yaw feedforward uses estimated goal motion to rotate the formation before position error develops, reducing basket-yaw lag without adding net commanded force. A disturbance-conditioned critic supports centralized training while execution remains decentralized. Across held-out trajectories, CALM achieves lower mean position and orientation errors than all evaluated baselines, including the matched arm baseline (7.68 versus 10.95 cm and 3.3 versus 4.7$^\circ$), the cable-suspended realization, and two model-based controllers. Under unseen full-information-path degradation, CALM remains statistically comparable or superior to the arm baseline. Videos are available at https://petreric.github.io/CALM/.

</details>

---

### [[20_Research/Papers/具身智能/DR-VLA_Learning_Human-Like_Quadruped_Navigation_from_Egocentric_Web_Videos_via_Domain-Invariant_Scene_Representations|DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations]]

![[assets/2610.18373_figure.png|800]]

- **arXiv**: [2610.18373](https://arxiv.org/abs/2610.18373)
- **PDF**: https://arxiv.org/pdf/2610.18373
- **详细分析**: [[20_Research/Papers/具身智能/DR-VLA_Learning_Human-Like_Quadruped_Navigation_from_Egocentric_Web_Videos_via_Domain-Invariant_Scene_Representations|DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations]]
- **作者**: Jun Tian, Yingjie Niu, Ruo Chen, Hongyi Lin, Chao Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.3（加权：具身智能 3，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DR-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadruped robots performing outdoor deliveries must interpret complex scenes, anticipate changes, and navigate in socially compliant ways. Robot demonstrations are costly to collect at the scale needed for generalization. Egocentric web videos offer abundant human navigation experience, but differences in viewpoint and motion make this experience difficult to transfer to robots. We introduce DR-VLA, a Mixture-of-Transformers framework that transfers human navigation experience through a domain-invariant scene representation (DISR). The framework combines vision-language understanding and latent world modeling with a flow-matching action expert. We introduce EgoLynx, comprising 10,000 hours of curated egocentric web video (EgoLynx-Web) and 2,000 clips of teleoperated robot navigation collected during real-world deliveries (EgoLynx-Robot). We pretrain the understanding and world experts on EgoLynx-Web without action labels, then adapt the model to robot observations and train the action expert on EgoLynx-Robot to predict executable trajectories. We also propose the Quadruped Navigation Score (QNS), a pseudo-closed-loop metric combining safety, instruction compliance, comfort, and progress. On the held-out EgoLynx-Robot test split, DR-VLA improves QNS by approximately 5% and reduces open-loop final heading error (FHE) by 14.6%, each relative to the best competing result for that metric. Ablations show that web-video pretraining improves generalization and that the model's key components contribute to performance. As a future-prediction target, DISR outperforms five generic visual representations and yields performance close to task-specific 3D perception without dedicated geometric labels or point clouds for target construction. Trained separately on NAVSIM v1 without web pretraining, DR-VLA achieves 92.1 PDMS, suggesting that the framework also applies to autonomous driving.

</details>

---

### [[20_Research/Papers/具身智能/CoSMO_Conformal_Semantic_Mapping_for_Open-World_Safe_Robot_Navigation|CoSMO: Conformal Semantic Mapping for Open-World Safe Robot Navigation]]

![[assets/2610.18321_figure.png|800]]

- **arXiv**: [2610.18321](https://arxiv.org/abs/2610.18321)
- **PDF**: https://arxiv.org/pdf/2610.18321
- **详细分析**: [[20_Research/Papers/具身智能/CoSMO_Conformal_Semantic_Mapping_for_Open-World_Safe_Robot_Navigation|CoSMO: Conformal Semantic Mapping for Open-World Safe Robot Navigation]]
- **作者**: Shuqi Wang, Yiwei Zheng, Pingrui Zhang, Yue Gao, Xiang Yin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《CoSMO: Conformal Semantic Mapping for Open-World Safe Robot Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Closed-Set, Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe autonomous navigation requires not only geometric obstacle avoidance but also semantic awareness. Different object categories demand different safety clearances, and the set of relevant categories may expand as the robot explores novel environments. Vision-language models (VLMs) offer rich semantic representations for building maps of unknown scenes, yet their confidence scores are poorly calibrated, making raw predictions unreliable for safety-critical planning. Conformal prediction (CP) can provide coverage guarantees, but existing methods assume a fixed label set and stationary data, limiting their use in open-world settings. We propose Conformal Semantic Mapping for Open-World Safe Robot Navigation (CoSMO), a semantic safety mapping framework that transforms VLM embeddings into calibrated coverage sets and safety-aware obstacle dilations over a dynamically expanding hazard vocabulary, even under distribution shift. Experiments on the Matterport3D (MP3D) dataset show that CoSMO reduces semantic collisions by 61.6% relative to a geometry-only baseline, while maintaining formal coverage guarantees even under delayed expert feedback. Real-world experiments on a quadruped robot further demonstrate generalization by achieving long-run empirical coverage of 90.73% against the 90% target. Project website: https://yangming911.github.io/cosmo-page/.

</details>

---

### [[20_Research/Papers/具身智能/Cross-Embodiment_Affordance_Transfer_for_Robotic_Manipulation|Cross-Embodiment Affordance Transfer for Robotic Manipulation]]

![[assets/2610.18194_figure.jpg|800]]

- **arXiv**: [2610.18194](https://arxiv.org/abs/2610.18194)
- **PDF**: https://arxiv.org/pdf/2610.18194
- **详细分析**: [[20_Research/Papers/具身智能/Cross-Embodiment_Affordance_Transfer_for_Robotic_Manipulation|Cross-Embodiment Affordance Transfer for Robotic Manipulation]]
- **作者**: Sawera Yaseen, Serge Thill, Rekha Raja
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Cross-Embodiment Affordance Transfer for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AffordanceNet, PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation systems commonly learn object affordances from human-annotated datasets, which reflect interaction possibilities for a human hand rather than the physical constraints of a specific robot. For example, a surface region of an object identified as graspable by a human annotator may be geometrically unreachable or mechanically infeasible for a robot, yet this mismatch is rarely addressed explicitly. To tackle this challenge, we proposed a framework that translates human affordance annotations into robot-executable affordance predictions conditioned on the physical properties of the robot. The network predicts which surface regions of an object are physically executable by the robot, given a 3D point cloud of an object and a descriptor encoding the robot's geometry and constraints. The model was trained using human-annotated affordances together with robotic execution outcomes from multiple sampled approach trials in simulation, where execution outcomes determined which regions are executable for the robot. The evaluation was performed on a household objects dataset using two parallel-jaw gripper configurations on a UR5e robot arm. The framework outperformed a model that does not receive information about the robot. The experimental results demonstrated that affordance prediction must be conditioned on the robot and that human annotations alone are insufficient for learning robot-executable affordance representations.

</details>

---

### [[20_Research/Papers/具身智能/Walk_Like_This_Stylized_Locomotion_for_Physics-Based_Characters_through_Example-Driven_Diffusion|Walk Like This: Stylized Locomotion for Physics-Based Characters through Example-Driven Diffusion]]

![[assets/2610.18147_figure.png|800]]

- **arXiv**: [2610.18147](https://arxiv.org/abs/2610.18147)
- **PDF**: https://arxiv.org/pdf/2610.18147
- **详细分析**: [[20_Research/Papers/具身智能/Walk_Like_This_Stylized_Locomotion_for_Physics-Based_Characters_through_Example-Driven_Diffusion|Walk Like This: Stylized Locomotion for Physics-Based Characters through Example-Driven Diffusion]]
- **作者**: Joshua Aurand, Agon Serifi, Sammy Christen, Ruben Grandia, Espen Knoop, Marco Hutter, Moritz Bächer
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.7（加权：具身智能 1.8，强化学习 0.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Walk Like This: Stylized Locomotion for Physics-Based Characters through Example-Driven Diffusion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a real-time framework for expressive legged locomotion that enables independent control over velocity and style. Unlike existing data-driven controllers, which typically require explicit style labels for training, our method efficiently leverages large-scale unstructured motion data and generalizes to unseen styles. We disentangle style from functional locomotion through a tailored sampling strategy used to train a style encoder whose output conditions an autoregressive diffusion model. During inference, the user provides a style reference clip and a joystick velocity command. The diffusion model then generates a kinematic reference tracked by a reinforcement learning controller. To improve user controllability and stylization strength, we propose an attention biasing mechanism and a velocity command correction strategy. We demonstrate our method on a physics-based humanoid character in simulation and on a physical robot, showcasing robust real-time control and continuous style modulation. The results can be best seen in our supplemental video (https://www.youtube.com/watch?v=roFnS6N7nJ4).

</details>

---

### [[20_Research/Papers/大模型/MARTS_A_Modular_Agricultural_Robot_for_Targeted_Spraying_of_Diseased_Tomato_Plants_in_Greenhouses|MARTS: A Modular Agricultural Robot for Targeted Spraying of Diseased Tomato Plants in Greenhouses]]

![[assets/2610.18123_figure.jpg|800]]

- **arXiv**: [2610.18123](https://arxiv.org/abs/2610.18123)
- **PDF**: https://arxiv.org/pdf/2610.18123
- **详细分析**: [[20_Research/Papers/大模型/MARTS_A_Modular_Agricultural_Robot_for_Targeted_Spraying_of_Diseased_Tomato_Plants_in_Greenhouses|MARTS: A Modular Agricultural Robot for Targeted Spraying of Diseased Tomato Plants in Greenhouses]]
- **作者**: Rajmeet Singh, Manveen Kaur, Yusuf Adamu, Lochan Kshetrimayum, Irfan Hussain
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.1，机器人 1.5）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《MARTS: A Modular Agricultural Robot for Targeted Spraying of Diseased Tomato Plants in Greenhouses》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Broadcast spraying remains the dominant method of disease control in greenhouse tomato production, yet it treats healthy and diseased tissue alike, exposes workers to hazardous aerosols, and depends on operator skill. This paper presents MARTS (Modular Agricultural Robot for Targeted Spraying), a low-cost robotic platform that closes the loop from plant-level disease detection to leaf-localised spray delivery in commercial greenhouses. MARTS integrates a Clearpath Husky A200 mobile base, a UR5 manipulator, a novel modular spraying end-effector built around a single 12 V micro-diaphragm pump, and a wrist-mounted Intel RealSense D435 RGB-D camera. Disease detection reuses our previously published Tomato Leaf Disease Vision Language Model (TLDVLM; Grounding DINO, SAM-2 and LoRA-tuned BLIP-2, 97.27% accuracy over 10 classes); this work focuses on actuation, control and system integration. A ROS pipeline lifts detections into 3D targets, generates collision-aware nozzle poses at a 120 mm stand-off using fitted leaf normals, and scales pump pulse duration to lesion area. Water-sensitive paper calibration showed a linear pulse-volume relationship (R^2 = 0.994). In MuJoCo simulation, an adaptive base-repositioning strategy achieved 100% coverage of 18 waypoints with a maximum orientation error of 1.1 deg. Deployed at the SILAL commercial greenhouse (Al Ain, UAE) on cherry tomatoes under natural infection, MARTS treated 312 diseased leaves in 12 autonomous trials with 92.4% targeting success, 18.7 mm mean spray-centre error, 6.1% adjacent-leaf overspray, and a 71% reduction in pesticide volume versus broadcast spraying. Mean cycle time was 4.8 s per leaf, and the spraying subsystem costs USD 412, 6-10x lower than comparable systems, showing that accurate leaf-level targeting is achievable on commodity hardware.

</details>

---

### [[20_Research/Papers/具身智能/TRACE_Efficient_Transfer_Learning_for_Neural_Whole-Body_Control_Across_Humanoid_Embodiments|TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments]]

![[assets/2610.17999_figure.jpg|800]]

- **arXiv**: [2610.17999](https://arxiv.org/abs/2610.17999)
- **PDF**: https://arxiv.org/pdf/2610.17999
- **详细分析**: [[20_Research/Papers/具身智能/TRACE_Efficient_Transfer_Learning_for_Neural_Whole-Body_Control_Across_Humanoid_Embodiments|TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments]]
- **作者**: Qingyu Lan, Zhihao Tian, Zifan Wang, Junwei Liang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.3（加权：具身智能 1.8，强化学习 0.2，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid behavior foundation models (BFMs) enable diverse whole-body control, but adapting a pretrained controller to a new embodiment remains challenging because of kinematic and dynamic mismatch. We present TRACE, a framework for efficient cross-embodiment adaptation that preserves pretrained motion representations while specializing feedback control to the target robot.TRACE first injects kinematic priors into input and output projection layers and aligns nominal joint dynamics to reduce embodiment mismatch and support stable fine-tuning. It then combines encoder distillation with low-rank reinforcement learning on a compact, quality-screened motion set, using a two-phase curriculum to establish stable tracking before refining difficult motions. We apply TRACE to transfer SONIC from Unitree G1 to Unitree H2 using 10 million motion frames and approximately eight hours of training on a single RTX PRO 6000 GPU, at less than 0.1% of the GPU-hour cost of training SONIC from scratch. The adapted controller achieves 96.08\% success on 67,953 evaluation motions under a height-scaled tracking criterion. Real-robot demonstrations span dynamic motion tracking and whole-body teleoperation, with collected demonstrations supporting downstream vision-language-action policy post-training. These results demonstrate practical reuse of a pretrained humanoid controller across robots with different body scales and dynamics.

</details>

---

### [[20_Research/Papers/具身智能/Breaking_the_Average_Overcoming_Convergent_Defaults_in_Robotic_Manipulation_via_Diagnostic_Chain-of-Thought_and_Structured_Guidance|Breaking the Average: Overcoming Convergent Defaults in Robotic Manipulation via Diagnostic Chain-of-Thought and Structured Guidance]]

![[assets/2610.17983_figure.png|800]]

- **arXiv**: [2610.17983](https://arxiv.org/abs/2610.17983)
- **PDF**: https://arxiv.org/pdf/2610.17983
- **详细分析**: [[20_Research/Papers/具身智能/Breaking_the_Average_Overcoming_Convergent_Defaults_in_Robotic_Manipulation_via_Diagnostic_Chain-of-Thought_and_Structured_Guidance|Breaking the Average: Overcoming Convergent Defaults in Robotic Manipulation via Diagnostic Chain-of-Thought and Structured Guidance]]
- **作者**: Mohammed Daba, Waleed Abdulrahman Saleh AlAkwa
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.8，大模型 0.1，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Breaking the Average: Overcoming Convergent Defaults in Robotic Manipulation via Diagnostic Chain-of-Thought and Structured Guidance》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent Vision-Language-Action (VLA) models, such as $π_{0.5}$, have demonstrated impressive generalization capabilities by scaling behavior cloning across massive datasets. However, these models frequently suffer from distributional convergence, a phenomenon where the policy regresses to "safe" but suboptimal mean behaviors due to mode averaging in the training data. This often results in generic grasp strategies, Convergent Defaults, that fail in constrained or long-tail scenarios. In this work, we propose a novel framework to identify and correct these behaviors without parameter updates. We introduce a three-stage methodology: (1) Probing for Defaults, identifying task-specific mode collapse; (2) Diagnostic Root Cause Analysis, utilizing the VLA's latent reasoning capabilities to verbalize the logic behind suboptimal actions; and (3) Structured Guidance Injection, where concrete, distinct alternatives are encoded into reusable "Lens Prompts" that shift the sampling distribution. We validate this approach using $π_{0.5}$ in ManiSkill3 simulation environments. We hypothesize that our method outperforms vanilla $π_{0.5}$ and standard Chain-of-Thought prompting by effectively breaking convergent defaults in complex manipulation tasks.

</details>

---

### [[20_Research/Papers/具身智能/Locomotion_with_Online_Awareness_of_Dynamics_for_Precision_Footholds|Locomotion with Online Awareness of Dynamics for Precision Footholds]]

![[assets/2610.17930_figure.png|800]]

- **arXiv**: [2610.17930](https://arxiv.org/abs/2610.17930)
- **PDF**: https://arxiv.org/pdf/2610.17930
- **详细分析**: [[20_Research/Papers/具身智能/Locomotion_with_Online_Awareness_of_Dynamics_for_Precision_Footholds|Locomotion with Online Awareness of Dynamics for Precision Footholds]]
- **作者**: Kunzhao Ren, Zhishuo Zhu, Xiaobin Xiong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Locomotion with Online Awareness of Dynamics for Precision Footholds》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unknown payloads alter robot dynamics and make precise contact execution difficult when foothold margins are small. We present LOAD, a perceptive locomotion framework that combines explicit inertial estimates with implicit dynamics features for narrow-beam traversal. Separate recurrent modules infer torso inertial changes and task-relevant history from proprioception, while a height-map teacher is distilled into a depth-based student. We extensively evaluate LOAD and its variants in simulation and on hardware across beam widths and payload configurations. The results show that implicit dynamics features accelerate training, while explicit inertial estimation further improves traversal success; combining both enables LOAD to approach the performance of a privileged policy supplied with ground-truth inertial parameters. Hardware experiments demonstrate traversal with unilateral payloads of 6 kg on a 10 cm beam and 9 kg on a 15 cm beam, and an evenly distributed 11 kg payload on a 15 cm beam. These results support combining physical estimates and history features for precision locomotion under unknown loads.

</details>

---

### [[20_Research/Papers/具身智能/WoVR+_World_Model_as_Reliable_Simulator_for_Versatile_VLA_Policy_Optimization_with_RL|WoVR+: World Model as Reliable Simulator for Versatile VLA Policy Optimization with RL]]

![[assets/2610.17922_figure.png|800]]

- **arXiv**: [2610.17922](https://arxiv.org/abs/2610.17922)
- **PDF**: https://arxiv.org/pdf/2610.17922
- **详细分析**: [[20_Research/Papers/具身智能/WoVR+_World_Model_as_Reliable_Simulator_for_Versatile_VLA_Policy_Optimization_with_RL|WoVR+: World Model as Reliable Simulator for Versatile VLA Policy Optimization with RL]]
- **作者**: Shangqing Zhou, Zhennan Jiang, Ning Ma, Xin Fu, Yupeng Zheng, Shuai Tian, Huangrui Li, Jiahao Liu, Chao Yu, Zhongpu Xia, Haoran Li, Dongbin Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 世界模型, 机器人
- **相关性评分**: 4.3（加权：具身智能 1.8，强化学习 1，世界模型 1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《WoVR+: World Model as Reliable Simulator for Versatile VLA Policy Optimization with RL》归入 具身智能、强化学习、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Ctrl-World, GeniWorld, GigaWorld, ProphRL, VLA-RL, WM-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned world models can reduce costly real-robot interaction in reinforcement learning for Vision-Language-Action models (VLA-RL), but hallucinations can mislead policy optimization. Extending them to richer VLA interfaces and long-horizon tasks raises challenges in spatiotemporal and cross-modal consistency, exploration-reliability balance in RL, and compounding rollout errors. We present WoVR+, extending WoVR's hallucination-aware WM-RL framework by redesigning the learned environment and imagined interaction protocol: A VLA-interface-aligned world model provides multi-view prediction and proprioceptive updates while mitigating hallucinations. Chunk-wise noise preserves flow-based policy exploration while limiting prediction-degrading action jitter. For long-horizon tasks, stage-local imagined training combines stage-entry resets, stage-specific rewards, local horizons, and controllable sampling to shorten generated prefixes and balance training across stages. WoVR+ improves success over SFT by 21.09% and 16.7% on RoboTwin and 6 real-robot tasks. Long-horizon phone-packaging success rises from 30% to 75%. Videos are available at https://youmo445.github.io/WoVR_Plus.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/Physics-Aware_Object-Centric_SE(3)_Forecasting_for_Real-Time_Proactive_Dynamic_Grasping|Physics-Aware Object-Centric SE(3) Forecasting for Real-Time Proactive Dynamic Grasping]]

![[assets/2610.17843_figure.png|800]]

- **arXiv**: [2610.17843](https://arxiv.org/abs/2610.17843)
- **PDF**: https://arxiv.org/pdf/2610.17843
- **详细分析**: [[20_Research/Papers/具身智能/Physics-Aware_Object-Centric_SE(3)_Forecasting_for_Real-Time_Proactive_Dynamic_Grasping|Physics-Aware Object-Centric SE(3) Forecasting for Real-Time Proactive Dynamic Grasping]]
- **作者**: Yirui Zhou, Hongli Xu, Ying Zheng, Yi Wang, Lap-Pui Chau
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Physics-Aware Object-Centric SE(3) Forecasting for Real-Time Proactive Dynamic Grasping》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DynamicVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Proactive dynamic grasping requires robots to predict the future state at which physical contact will occur, rather than reacting to the currently observed object pose. But what future must the robot predict, and at what level of abstraction? We argue that contact-relevant rigid-body state in SE(3) is a compact task-sufficient abstraction for this problem: it directly determines where and when the robot should establish contact, without requiring visually complete future scenes. This insight leads to a lightweight object-centric forecast-then-select framework that predicts future rigid-body trajectories from short pose histories and uses a reachability-aware interception selector to choose feasible contact states under kinematic and timing constraints. Trained with randomized physics simulation over primitive shapes, the forecaster transfers to real objects once their metric geometry and SE(3) state histories are recovered. Experiments across simulation and real-world dynamic grasping tasks show that our framework improves the average success rate from \(24.5\%\) to \(62.0\%\) in simulation, and from \(15.3\%\) to \(67.3\%\) in real-world catching, conveyor, and turntable interception. The SE(3) forecaster runs in \(15\,\mathrm{ms}\), orders of magnitude faster than dense visual future prediction, enabling real-time contact decision making. Our results suggest that effective proactive grasping does not require imagining the entire future scene. Instead, predicting the compact physical future that determines contact provides an effective and practical abstraction for real-time dynamic grasping.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Robot_Policies_for_Whole-Body_Mobility_Assistance_via_Dynamic_Human_Motion_Generation|Learning Robot Policies for Whole-Body Mobility Assistance via Dynamic Human Motion Generation]]

![[assets/2610.17750_figure.jpg|800]]

- **arXiv**: [2610.17750](https://arxiv.org/abs/2610.17750)
- **PDF**: https://arxiv.org/pdf/2610.17750
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Robot_Policies_for_Whole-Body_Mobility_Assistance_via_Dynamic_Human_Motion_Generation|Learning Robot Policies for Whole-Body Mobility Assistance via Dynamic Human Motion Generation]]
- **作者**: Shikun Ban, Shohei Nagai, Qingyang Song, Hanxi Wan, Eric Zhao, Thomas Wang, Zackory Erickson
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Learning Robot Policies for Whole-Body Mobility Assistance via Dynamic Human Motion Generation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic assistance for human mobility could benefit care recipients and reduce caregiver burden during physically demanding tasks such as Sit-to-Stand (STS) and Lift-and-Transfer (L&amp;T). Learning robot policies for these whole-body assistive tasks is challenging: real-world data collection for human-robot interaction is costly and safety-critical, making simulation an attractive alternative. Prior work, however, typically treats the human as static or minimally responsive and thus fails to capture the cooperative nature of mobility assistance. We present a simulation-based framework for learning whole-body assistive robot policies. At its core is a human policy trained with an adversarial motion prior that produces realistic care-recipient motion in response to the robot's actions. A human-adaptive scripted controller interacts with this policy to collect diverse robot demonstrations at scale. From these demonstrations, we train 3D diffusion policies that map segmented human point clouds and robot joint positions to whole-body actions for a mobile manipulator, without relying on privileged human state at deployment. The resulting robot policies successfully perform both STS and L&amp;T assistance in simulation. Preliminary experiments further demonstrate sim-to-real transfer for STS after fine-tuning on a small amount of real-world data. Videos are available on our project page: https://rchi-lab.github.io/human-gen-mobility-assistance/

</details>

---

### [[20_Research/Papers/具身智能/The_Human--VLA_Communication_Gap_What_Humans_Leave_Implicit_and_What_Policies_Cannot_Recover|The Human--VLA Communication Gap: What Humans Leave Implicit and What Policies Cannot Recover]]

![[assets/2610.17746_figure.png|800]]

- **arXiv**: [2610.17746](https://arxiv.org/abs/2610.17746)
- **PDF**: https://arxiv.org/pdf/2610.17746
- **详细分析**: [[20_Research/Papers/具身智能/The_Human--VLA_Communication_Gap_What_Humans_Leave_Implicit_and_What_Policies_Cannot_Recover|The Human--VLA Communication Gap: What Humans Leave Implicit and What Policies Cannot Recover]]
- **作者**: Yiqing Xu, Jiajun Wu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《The Human--VLA Communication Gap: What Humans Leave Implicit and What Policies Cannot Recover》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot may know how to perform a task yet fail when a human asks for it naturally. We study this human--VLA communication gap by separating an \emph{information gap}, where task semantics, grounding, or event structure remain unresolved, from a residual \emph{execution gap}, where even a fully specified task depends on how it is organized and invoked. To do this, we characterize how people naturally express demonstrated objectives and evaluate controlled variants of the same physical tasks, with detailed analysis on $π_{0.5}$ and consistent trends on $π_0$-FAST and Cosmos3-Edge. Our study reveals that humans increasingly compress instructions as tasks grow, relying more on contextual grounding and implicit execution structure. Current policies are misaligned with this behavior: they tolerate grounding dependence relatively well, but struggle when task semantics or event structure must be reconstructed. Even after the information gap is resolved, execution remains sensitive to command granularity and invocation state. These findings identify concrete targets for human-centered policy learning and interfaces that better bridge natural human objectives to robot behavior. Project website: https://commgap.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/Towards_a_Systematic_Study_of_Embodied_System_2_over_Full_Task_Execution_Cycles|Towards a Systematic Study of Embodied System 2 over Full Task Execution Cycles]]

![[assets/2610.17657_figure.png|800]]

- **arXiv**: [2610.17657](https://arxiv.org/abs/2610.17657)
- **PDF**: https://arxiv.org/pdf/2610.17657
- **详细分析**: [[20_Research/Papers/具身智能/Towards_a_Systematic_Study_of_Embodied_System_2_over_Full_Task_Execution_Cycles|Towards a Systematic Study of Embodied System 2 over Full Task Execution Cycles]]
- **作者**: Yuxi Wei, Ye Fang, Shuai Yang, Tong Wu, Tai Wang, Xiaojuan Qi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Towards a Systematic Study of Embodied System 2 over Full Task Execution Cycles》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ECBench, EmbodiedBench, EmbodiedEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

An embodied brain, or System 2, must turn an abstract goal into actions while discovering relevant scene conditions and checking whether executed skills achieved their intended effects. Open-loop evaluations cannot test observations shaped by an agent's decisions, while some closed-loop evaluations provide limited evidence during execution or assume idealized skill outcomes. We introduce SCOPER, a suite for studying observation-grounded planning, execution, and recovery. SCOPER-bench combines high-level goals, ongoing visual observations, a shared rule-based System 1 for low-level actions, and controlled execution failures. Its construction and validation pipeline yields 870 tasks across BEHAVIOR and ProcTHOR, complemented by about 3,500 situated questions tied to the evaluated agent's execution. Benchmark results reveal difficulties in retaining scene evidence, monitoring progress, and recovering from unexpected outcomes. To address these difficulties, SCOPER-harness combines Evidence Memory and Progress Verification with a dynamic task agenda and bounded exploration, without additional model training. Across two evaluated open-source backbones and two simulators, the harness improves task success by 11.1-28.6%; a harnessed 9B model outperforms a directly executed 27B model on both simulators. In an offline next-action evaluation using observations from 200 real-robot demonstrations, the harness also improves full-call accuracy by 14.7% and 15.3%. SCOPER provides a setting for diagnosing and improving embodied reasoning throughout a complete task execution cycle.

</details>

---

### [[20_Research/Papers/机器人/EgoCPT_Learning_Dexterous_Manipulation_from_a_Single_Ego-Centric_Video_with_Contact-Aware_Optimization|EgoCPT: Learning Dexterous Manipulation from a Single Ego-Centric Video with Contact-Aware Optimization]]

![[assets/2610.17572_figure.png|800]]

- **arXiv**: [2610.17572](https://arxiv.org/abs/2610.17572)
- **PDF**: https://arxiv.org/pdf/2610.17572
- **详细分析**: [[20_Research/Papers/机器人/EgoCPT_Learning_Dexterous_Manipulation_from_a_Single_Ego-Centric_Video_with_Contact-Aware_Optimization|EgoCPT: Learning Dexterous Manipulation from a Single Ego-Centric Video with Contact-Aware Optimization]]
- **作者**: Zhixin Sun, Kairui Shi, Tianao Ren, Ming Yang, Mark Cutkosky, James Jingxi Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《EgoCPT: Learning Dexterous Manipulation from a Single Ego-Centric Video with Contact-Aware Optimization》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While expert demonstrations on real robots are difficult to collect, human ego-centric videos are easy to collect and abundant on the internet. However, learning dexterous manipulation policies from human videos remains challenging---one of the most important challenges being the difficulty of reconstructing physically grounded robot trajectories due to the large embodiment gap. In this paper, we propose EgoCPT, a novel paradigm for learning high-quality retargeted dexterous hand trajectories directly from an ego-centric video, which can then be deployed directly on real robots. The only inputs to our method are an ego-centric RGB video and a reference hand pose trajectory, which can be easily obtained through off-the-shelf software or specialized cameras during recording. Our method is particularly robust to noisy hand poses attributed to our novel contact-aware optimization framework, which iteratively optimizes the contact points between the robot hands and objects. Across five manipulation tasks, our method achieves overall success rates of 67.3% on noisy EgoDex hand-pose reconstructions and 92.0% on high-quality TACO reconstructions collected using motion-capture hardware, outperforming multiple baselines on both benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/Can_a_Frontier_VLM_Serve_as_a_Robot_Policy_for_Memory-Dependent_Manipulation|Can a Frontier VLM Serve as a Robot Policy for Memory-Dependent Manipulation?]]

![[assets/2610.17350_figure.png|800]]

- **arXiv**: [2610.17350](https://arxiv.org/abs/2610.17350)
- **PDF**: https://arxiv.org/pdf/2610.17350
- **详细分析**: [[20_Research/Papers/具身智能/Can_a_Frontier_VLM_Serve_as_a_Robot_Policy_for_Memory-Dependent_Manipulation|Can a Frontier VLM Serve as a Robot Policy for Memory-Dependent Manipulation?]]
- **作者**: Jack B. Jedlicki, Amish Sethi, Heng Yang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.6，大模型 0.5，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Can a Frontier VLM Serve as a Robot Policy for Memory-Dependent Manipulation?》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We use a frozen frontier vision-language model, GPT-6-Astra, directly as the robot policy on RoboMME, a benchmark of 16 memory-dependent manipulation tasks spanning temporal, spatial, object, and procedural memory. The model keeps the whole episode in context and outputs every end-effector waypoint and gripper command, with no RoboMME-specific training. On the 800 test episodes it succeeds in 92.1%, above the previously reported human score of 90.5%, which was obtained with an oracle skill interface, and far ahead of the best leaderboard entry (60.8%) and of a hierarchical system that pairs the same model with a RoboMME-trained policy (79.1%). It matches or exceeds the human score on 13 of the 16 tasks. Its 63 failures concentrate in two tasks and are mostly premature completions and mistimed or unintended button presses. These results blur the usual division between long-horizon planning, memory and end-effector control, and raise the question of how much of this stack a single general-purpose model can take over in embodied systems. Project website: https://embodied-astra.github.io. Code, prompts and all episode logs: https://github.com/jackbjed/embodied-astra-robomme.

</details>

---

### [[20_Research/Papers/具身智能/LiDAR-based_Humanoid_Navigation_in_Dynamic,_Non-Convex_Environments_via_Spatio-Temporal_Safe_Corridors|LiDAR-based Humanoid Navigation in Dynamic, Non-Convex Environments via Spatio-Temporal Safe Corridors]]

![[assets/2610.17232_figure.png|800]]

- **arXiv**: [2610.17232](https://arxiv.org/abs/2610.17232)
- **PDF**: https://arxiv.org/pdf/2610.17232
- **详细分析**: [[20_Research/Papers/具身智能/LiDAR-based_Humanoid_Navigation_in_Dynamic,_Non-Convex_Environments_via_Spatio-Temporal_Safe_Corridors|LiDAR-based Humanoid Navigation in Dynamic, Non-Convex Environments via Spatio-Temporal Safe Corridors]]
- **作者**: Shubham S. Kumbhar, Panagiotis Artemiadis
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《LiDAR-based Humanoid Navigation in Dynamic, Non-Convex Environments via Spatio-Temporal Safe Corridors》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Navigating humanoid robots through dynamic, non-convex environments requires tightly coupling onboard perception with footstep planning and dynamic locomotion control. Existing methods frequently discard complex free space through simplified convex obstacle bounds and fail to account for real-time dynamic occupancy predictions. This paper presents a real-time framework for humanoid navigation that directly constructs spatio-temporal safe corridors from LiDAR-based particle representations and couples them with Linear Inverted Pendulum (LIP)-based planning and Whole Body Control (WBC) to enable navigation around and within moving non-convex structures without restrictive geometric assumptions. Simulations on the Digit humanoid yield a 96% success rate in navigating around and inside moving non-convex obstacles in a 24 by 24 m^2 arena. Ablation studies confirm that the proposed iterative polytope generation significantly outperforms single-iteration baselines in narrow corridors, while evaluations demonstrate robustness to clutter, sensor noise, control delays, and force perturbations.

</details>

---

### [[20_Research/Papers/大模型/Declarative_Reactive_Robot_Behaviors_from_Imperative_Language_Models|Declarative Reactive Robot Behaviors from Imperative Language Models]]

![[assets/2610.17083_figure.jpg|800]]

- **arXiv**: [2610.17083](https://arxiv.org/abs/2610.17083)
- **PDF**: https://arxiv.org/pdf/2610.17083
- **详细分析**: [[20_Research/Papers/大模型/Declarative_Reactive_Robot_Behaviors_from_Imperative_Language_Models|Declarative Reactive Robot Behaviors from Imperative Language Models]]
- **作者**: Vincent Berenz, Tasha Kim, Bernhard Schölkopf
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.2，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Declarative Reactive Robot Behaviors from Imperative Language Models》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) are predominantly trained on imperative programming languages, and existing work on LLM-based robot programming reflects this: it focuses on goal-directed tasks expressed as plans. However, many robotic applications require not tasks but behaviors--open-ended, continuous patterns of sensory-motor engagement with no termination condition (e.g., greeting visitors, patrolling an area). Such behaviors are better served by declarative and reactive programming, on which LLMs have virtually no training. We investigate whether this gap can be bridged. Using Playful, a reactive scripting language, we show that an LLM-based coding agent can generate correct declarative and reactive programs for robotic behaviors. These programs are produced from under-specified natural language descriptions, given suitable context and a set of reusable programming guidelines. The guidelines encode design principles that redirect the agent from imperative defaults toward proper reactive patterns. Developed once by an expert, they generalize across robots and behaviors. Starting from only the generic robot operating system API, the agent jointly designs both the imperative component (Python modules for sensing, acting, and evaluating) and the declarative component (the reactive script that composes them into behavior logic). The declarative nature of reactive programming supports both incremental refinement through conversational turns and one-shot generation of complete behaviors.

</details>

---

### [[20_Research/Papers/具身智能/Task-Space_Motion-Force_Nonlinear_Model_Predictive_Control_for_Precise_and_Compliant_Control_under_Uncertainties|Task-Space Motion-Force Nonlinear Model Predictive Control for Precise and Compliant Control under Uncertainties]]

![[assets/2610.17069_figure.jpg|800]]

- **arXiv**: [2610.17069](https://arxiv.org/abs/2610.17069)
- **PDF**: https://arxiv.org/pdf/2610.17069
- **详细分析**: [[20_Research/Papers/具身智能/Task-Space_Motion-Force_Nonlinear_Model_Predictive_Control_for_Precise_and_Compliant_Control_under_Uncertainties|Task-Space Motion-Force Nonlinear Model Predictive Control for Precise and Compliant Control under Uncertainties]]
- **作者**: Quang-Nam Nguyen, Ludovic Righetti
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.9，机器人 0.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Task-Space Motion-Force Nonlinear Model Predictive Control for Precise and Compliant Control under Uncertainties》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In Nonlinear Model Predictive Control (NMPC), the control law is implicitly determined by the solution of an Optimal Control Problem (OCP). Consequently, OCP design is often tailored to specific platforms and tasks, demanding extensive expert knowledge and tuning effort. To address this, we propose a unified NMPC framework that directly plans and controls the robot joints subject to task-space motion and force requirements and is capable of seamlessly generalizing across multiple robotic platforms and diverse tasks. Furthermore, optimization-based methods often treat interactions as rigid contacts, making the torque solution sensitive to the modeling errors of the robot dynamics and the environment. We study the intrinsic task-space impedance of our proposed controller, its partial contraction for differential stability and differential passivity under unmodeled interactions. As a result, our framework enables closing the force-feedback loop in the high-level planning layer to achieve precise motion-force tracking performance, addressing the long-standing challenge of force-feedback NMPC. Finally, we validate our framework on physical hardware, demonstrating hybrid motion-force control on a redundant manipulator and compliant locomotion on a quadruped, while preserving core NMPC advantages such as hard constraint satisfaction, optimal redundancy exploitation, and real-time planning under unforeseen interactions.

</details>

---

### [[20_Research/Papers/具身智能/MOSAIC_Mode-_and_Support-Aware_Inference-Time_Control_of_Robot_Diffusion_Models|MOSAIC: Mode- and Support-Aware Inference-Time Control of Robot Diffusion Models]]

![[assets/2610.17001_first_page.png|800]]

- **arXiv**: [2610.17001](https://arxiv.org/abs/2610.17001)
- **PDF**: https://arxiv.org/pdf/2610.17001
- **详细分析**: [[20_Research/Papers/具身智能/MOSAIC_Mode-_and_Support-Aware_Inference-Time_Control_of_Robot_Diffusion_Models|MOSAIC: Mode- and Support-Aware Inference-Time Control of Robot Diffusion Models]]
- **作者**: Sabrina Bodmer, Rahel Rickenbach, René Zurbrügg, Melanie N. Zeilinger, Colin Jones
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.9，机器人 1.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《MOSAIC: Mode- and Support-Aware Inference-Time Control of Robot Diffusion Models》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative policies such as diffusion models provide expressive data-driven priors for robot behavior, yet the situations a robot faces at execution time rarely match its training data and impose constraints and objectives the policy never learned. Existing inference-time guidance methods either rely on gradients that can push samples away from the learned prior, or on sampling procedures that can be inefficient, collapse modes, or average them into out-of-distribution predictions. We introduce MOSAIC, a mode- and support-aware framework for gradient-free inference-time control of robotic diffusion models. MOSAIC treats the initial noise and all stochastic reverse-step perturbations as a joint input to the pretrained denoising process and adapts a distribution over this input using importance weights computed from fully denoised outputs. Physical feasibility and consistency with the learned support are balanced using adaptive penalties, while mode-wise importance-weighted updates preserve modes and avoid destructive averaging. The same formulation can jointly steer multiple independently trained diffusion models through shared coupling costs, enabling coordinated behavior without requiring a joint model. We evaluate MOSAIC on navigation, dexterous grasping, motion planning with unseen geometry, and collaborative box manipulation with independently trained robot priors. Across these settings, MOSAIC adapts and composes frozen diffusion priors under new deployment constraints without retraining.

</details>

---

### [[20_Research/Papers/机器人/Human-Like_Redundancy_Resolution_for_Real-Time_Bimanual_Humanoid_Teleoperation|Human-Like Redundancy Resolution for Real-Time Bimanual Humanoid Teleoperation]]

![[assets/2610.16855_figure.png|800]]

- **arXiv**: [2610.16855](https://arxiv.org/abs/2610.16855)
- **PDF**: https://arxiv.org/pdf/2610.16855
- **详细分析**: [[20_Research/Papers/机器人/Human-Like_Redundancy_Resolution_for_Real-Time_Bimanual_Humanoid_Teleoperation|Human-Like Redundancy Resolution for Real-Time Bimanual Humanoid Teleoperation]]
- **作者**: Chao Tan, Ming Shin Cindy Sung, Shuxian Liang, Chaoqun Wan, Zhen Huang, Xian-Sheng Hua
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Human-Like Redundancy Resolution for Real-Time Bimanual Humanoid Teleoperation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-time bimanual humanoid teleoperation requires accurate wrist tracking while keeping arm configurations predictable. Because a 7-DoF arm admits multiple elbow configurations for the same wrist pose, wrist-only tracking can cause elbow drift or abrupt configuration changes. Fixed anthropomorphic constraints can stabilize elbow posture, but they can also block the redundant adjustments needed near singular configurations. We propose a human-like redundancy-resolution framework that combines adaptive elbow guidance with singularity-robust wrist tracking. Shoulder-wrist geometric retargeting generates robot-scale wrist targets. An adaptive elbow-offset criterion uses the offset direction to guide posture and scales this guidance by the offset magnitude, so the redundant degree of freedom is progressively released as the human arm straightens. A hierarchical velocity solver prioritizes wrist tracking and projects the adaptive elbow guidance into the wrist-task null space. In a fixed-wrist-target ablation, adaptive guidance reduces mean elbow-direction error by 54.4% compared with removing this guidance. In a workspace-boundary stress test, singularity-robust tracking reduces peak raw joint-velocity demand by 97.9% compared with the undamped pseudoinverse. Real-world bimanual tasks and cross-platform retargeting show applicability across robot morphologies.

</details>

---

### [[20_Research/Papers/具身智能/Design_and_Analysis_of_a_Nonlinear_Parallel_Mechanism_Coupling_for_Dynamic_Humanoid_Legs|Design and Analysis of a Nonlinear Parallel Mechanism Coupling for Dynamic Humanoid Legs]]

![[assets/2610.16604_figure.png|800]]

- **arXiv**: [2610.16604](https://arxiv.org/abs/2610.16604)
- **PDF**: https://arxiv.org/pdf/2610.16604
- **详细分析**: [[20_Research/Papers/具身智能/Design_and_Analysis_of_a_Nonlinear_Parallel_Mechanism_Coupling_for_Dynamic_Humanoid_Legs|Design and Analysis of a Nonlinear Parallel Mechanism Coupling for Dynamic Humanoid Legs]]
- **作者**: Rohit Kumar, Heiner Peters, Felix Wiebe, Franek Stark, Janne Janzen, Dennis Mronga, Shubham Vyas, Frank Kirchner
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Design and Analysis of a Nonlinear Parallel Mechanism Coupling for Dynamic Humanoid Legs》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoids increasingly demand lightweight leg mechanisms for agile, dynamic, and energy-efficient locomotion. Reducing distal inertia through proximal actuation has thus become a common design goal. Yet, compact transmissions that preserve torque capability and efficient force transmission remain hard to achieve. This paper presents a novel series-parallel leg design combining a knee parallel mechanism, an ankle parallel mechanism, and a nonlinear knee-ankle coupling where all actuators placed closer to the hip. As the knee flexes, the coupling passively assists ankle dorsiflexion for foot clearance and, as it extends it assists plantarflexion for push-off, redistributing ankle load through the knee transmission. We derive the coupling's nonlinear transmission models and validate them in simulation and on hardware. The design shows that the shared transmission lets both joints draw on each other's actuator capacity by easing the knee's peak torque demand under load and the ankle's peak speed demand during fast motion. %Together With the leg's proximal actuator placement, the leg achieves an effective reflected mass of 0.37kg at the foot for a 6kg leg, demonstrating very low distal leg inertia for dynamic humanoid robots.

</details>

---

### [[20_Research/Papers/具身智能/SHOES_Sim-to-real_Hardware-adaptation_via_On-policy_Expansion_of_Skills_for_Legged_Robots|SHOES: Sim-to-real Hardware-adaptation via On-policy Expansion of Skills for Legged Robots]]

![[assets/2610.16457_figure.png|800]]

- **arXiv**: [2610.16457](https://arxiv.org/abs/2610.16457)
- **PDF**: https://arxiv.org/pdf/2610.16457
- **详细分析**: [[20_Research/Papers/具身智能/SHOES_Sim-to-real_Hardware-adaptation_via_On-policy_Expansion_of_Skills_for_Legged_Robots|SHOES: Sim-to-real Hardware-adaptation via On-policy Expansion of Skills for Legged Robots]]
- **作者**: Kota Tsuruhara, Tsung-Yuan Chen, Kento Kawaharazuka
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《SHOES: Sim-to-real Hardware-adaptation via On-policy Expansion of Skills for Legged Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans expand their locomotion capability by wearing appropriate footwear, such as hiking boots for mountains or skates for ice. Footwear changes the ground-contact interface and enables traversal of otherwise difficult terrain. In contrast, locomotion controllers are typically trained for a fixed morphology, and their performance can degrade when shoes alter foot geometry, mass, and friction. We propose SHOES, a sample-efficient framework for adapting locomotion policies to footwear-induced morphology changes. SHOES freezes a simulation-trained nominal policy and fine-tunes only lightweight, identity-initialized modulation modules on the robot, preserving the initial behavior while enabling efficient hardware adaptation. We also introduce SafeBox, a workspace-aware waypoint sampler that constrains online adaptation within a user-defined workspace. The simulation results with a shoe-equipped Unitree Go2 show that SHOES substantially recovers locomotion performance after footwear-induced morphology changes using limited additional adaptation. Under the same adaptation budget, SHOES outperforms FiLM-only, Linear Adapter-only, and residual-RL baselines. Real-world experiments on a Unitree Go2 fitted with human shoes further evaluate the effectiveness of SHOES for hardware deployment.

</details>

---

### [[20_Research/Papers/具身智能/LABIT_Long-Horizon_Robotic_Assembly_Benchmark_for_Industrial_Tasks|LABIT: Long-Horizon Robotic Assembly Benchmark for Industrial Tasks]]

![[assets/2610.16398_figure.png|800]]

- **arXiv**: [2610.16398](https://arxiv.org/abs/2610.16398)
- **PDF**: https://arxiv.org/pdf/2610.16398
- **详细分析**: [[20_Research/Papers/具身智能/LABIT_Long-Horizon_Robotic_Assembly_Benchmark_for_Industrial_Tasks|LABIT: Long-Horizon Robotic Assembly Benchmark for Industrial Tasks]]
- **作者**: Constantin Schempp, Christian Friedrich, Luca Kofler, Laura Suhm
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《LABIT: Long-Horizon Robotic Assembly Benchmark for Industrial Tasks》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FurnitureBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot learning has undergone significant advancements in the domain of compliant control and robotic assembly. The development of novel methodologies has transcended the capacity to address discrete tasks, such as grasping or inserting, and has evolved to encompass the comprehensive construction of entire assemblies. Conventional benchmarks, which are predominantly focused on single tasks, are no longer adequate to address the complexity and interconnected nature of modern manufacturing processes. Consequently, the necessity for benchmarks to encompass a broader spectrum of assembly and subassembly steps is becoming apparent. In light of these developments, we propose LABIT, an industrial robotic assembly benchmark for long-horizon manipulation. This benchmark encompasses DIN-norm assembly tasks, including screwing, placing, inserting, and snapping, under both high and low tolerance conditions. The successive nature of these assembly steps implies that prior errors can influence subsequent manipulation. Consequently, this benchmark is particularly relevant for assessing the robustness of intelligent robotic systems. The proposed benchmarking protocols and novel performance metric, based on a taxonomy of assembly complexity in conjunction with the comprehensive list of parts and their corresponding CAD models, serve as essential tools for research and development in the field. To provide a baseline, we evaluate the benchmark using traditional force-position control and report reliability and score metrics per primitive, subtask, assembly category, and subassembly. Accompanying data is available at https://irp-hka.github.io/robotic-assembly-benchmark/.

</details>

---

### [[20_Research/Papers/具身智能/PINT_A_Unified_Model_with_Shared_Predictive_Intent_for_Robot_Manipulation|PINT: A Unified Model with Shared Predictive Intent for Robot Manipulation]]

![[assets/2610.16355_figure.png|800]]

- **arXiv**: [2610.16355](https://arxiv.org/abs/2610.16355)
- **PDF**: https://arxiv.org/pdf/2610.16355
- **详细分析**: [[20_Research/Papers/具身智能/PINT_A_Unified_Model_with_Shared_Predictive_Intent_for_Robot_Manipulation|PINT: A Unified Model with Shared Predictive Intent for Robot Manipulation]]
- **作者**: Xinyu Guo, Chao Jing, Li Yi, Xingyu Chen, Zhengxing Wu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.8，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《PINT: A Unified Model with Shared Predictive Intent for Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoT-VLA, DreamVLA, InternVLA, OpenVLA, Real-World, StarVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot manipulation can benefit from pretrained vision-language models (VLMs) for semantic reasoning and video generation models (VGMs) for world modeling. However, existing unified models that directly fuse them through shared attention at multiple layers can make it harder to draw on their specialized capabilities. We introduce PINT, a unified model that coordinates semantic reasoning, world modeling, and action generation through a shared chunk-level Predictive Intent while preserving expert-specific pathways. PINT inserts learnable Intent Tokens into the VLM sequence to form this representation, conditioning both the VGM and an Action Expert (AE). It replaces only the VGM's prompt conditioning and retains the VGM at inference, where the AE reads its representations through one-way attention. Rather than prescribing what Predictive Intent should encode, PINT learns it jointly from the native prediction objectives of the VLM, VGM, and AE, which provide complementary views of the same upcoming task execution. Training uses two stages: Stage 1 freezes the VGM so that future video prediction shapes Predictive Intent with task-relevant future dynamics, while Stage 2 fixes the learned Intent and adapts the VGM and AE. Without embodied pretraining, PINT achieves strong in-distribution (ID) performance and substantially improves out-of-distribution (OOD) generalization, reaching 15.5% on RoboTwin 2.0-Hard compared with 1.8% for Fast-WAM and 3.2% for StarVLA, and 79.5% on LIBERO-Plus compared with 51.5% and 75.0%, respectively. Across five real-world bimanual tasks, PINT reaches 68% ID and 24% OOD success, compared with 35%/9% for pretrained Motus and 67%/35% for pretrained $π_{0.5}$.

</details>

---

### [[20_Research/Papers/具身智能/Listen_Before_Act_Audio-Conditioned_Robot_Manipulation_with_ListenVLA|Listen Before Act: Audio-Conditioned Robot Manipulation with ListenVLA]]

![[assets/2610.16313_figure.png|800]]

- **arXiv**: [2610.16313](https://arxiv.org/abs/2610.16313)
- **PDF**: https://arxiv.org/pdf/2610.16313
- **详细分析**: [[20_Research/Papers/具身智能/Listen_Before_Act_Audio-Conditioned_Robot_Manipulation_with_ListenVLA|Listen Before Act: Audio-Conditioned Robot Manipulation with ListenVLA]]
- **作者**: Jiaqi Fan, Rui Xu, Jiakun Xia, Xuyu Fan, Shuailei Ma, Yuefeng Wang, Qing Wang, Jiarui Zhang, Yili Fu, Xu Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Listen Before Act: Audio-Conditioned Robot Manipulation with ListenVLA》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Audio-VLA, HEAR-Bench, ListenVLA, OpenVLA, RLBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have advanced robotic manipulation by connecting visual perception and language instructions to action generation. However, many manipulation tasks depend on auditory cues that cannot be reliably inferred from visual observations and may need to be elicited through physical interaction. To address this gap, we present ListenVLA, an audio-conditioned VLA policy built on GR00T N1.7 for sound-guided manipulation. ListenVLA combines semantic audio embeddings with waveform-derived acoustic cues over a causal audio history and conditions continuous action generation through audio tokens and feature modulation. Moreover, we introduce an audio-action binding objective that uses context-matched demonstrations to link auditory differences to demonstrated action differences. The objective supervises short-horizon differences between flow-velocity predictions under different audio conditions, with shared pure-noise action inputs and fixed non-audio observations, alongside full-chunk action supervision. Furthermore, we develop LIBERO-Audio, an eight-task benchmark covering sound-based target selection, responses to auditory events, and physical interactions that reveal acoustic evidence. Experiments on LIBERO-Audio and three real-world manipulation tasks show excellent performance. Ablation studies support the contributions of binding supervision and audio modulation, while audio swap tests show that sound influences action predictions. Our code and videos are available at https://anonymous.4open.science/r/listenvla-F18D

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Skill_Bench_Benchmarking_How_Well_Agents_with_Embodied_Skills_Perform_on_Physical_Tasks|Embodied Skill Bench: Benchmarking How Well Agents with Embodied Skills Perform on Physical Tasks]]

![[assets/2610.16238_figure.png|800]]

- **arXiv**: [2610.16238](https://arxiv.org/abs/2610.16238)
- **PDF**: https://arxiv.org/pdf/2610.16238
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Skill_Bench_Benchmarking_How_Well_Agents_with_Embodied_Skills_Perform_on_Physical_Tasks|Embodied Skill Bench: Benchmarking How Well Agents with Embodied Skills Perform on Physical Tasks]]
- **作者**: Zhi Han, Zihan Guo, Chenxi Zeng, Zicai Cui, Yue Xin, Ming Zhou, Dongzhan Zhou, Weinan Zhang, Yang Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.8，大模型 0.6，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Embodied Skill Bench: Benchmarking How Well Agents with Embodied Skills Perform on Physical Tasks》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EmbodiedBench, EmbodiedSkill-Bench, EmbodiedSkillBench, HarnessVLA, RLBench, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly control robots using VLA policies, perception models, and procedural knowledge. These modules are difficult to reuse because their interfaces, embodiment assumptions, and conditions of use differ, and their benefits on physical tasks remain unclear. We package them as embodied skills that extend agent skills with explicit embodiment assumptions and conditions of use, building 250 action, perception, and experience skills from 1,052 resources. On this basis we introduce EmbodiedSkillBench, which runs an agent in a closed observation-action loop and records success, actions, tokens, and wall-clock time. It supports three modes: native control, skill-only execution, and Agent-Directed Reuse (ADR), a mode we propose in which the agent keeps its native controls and decides for each skill whether to invoke, modify, or ignore it. Across four agents on 100 perturbed LIBERO-Pro tasks, we find that skills help an agent only as far as they exceed what it can already do. Skill-only execution lifts GPT-5.6-Sol from 11% to 63% and Kimi-K3 and Claude-Opus-5 by about 20 points, while cutting their token usage by 58% to 85%. Yet all four agents then end up between 61% and 64%, and GPT-6-Astra falls from 92% under native control to 61%. This suggests that as agents grow stronger, the role of embodied skills shifts from supplying missing capability to reducing cost: GPT-6-Astra already solves most tasks through native control, so restricting it to skills removes more than it adds. Under ADR, which lets it keep native control and call skills selectively, GPT-6-Astra recovers to 85%, within 7 points of native control, while using 14.1% fewer tokens and 11.9% less time. With Jev as a skill choosing motion directions and gripper actions, it reaches 81% with 50% fewer tokens and 57% less time. The code is available at https://github.com/HanZhi306/EmbodiedSkill-Bench.

</details>

---

### [[20_Research/Papers/具身智能/FlowVLA_Enabling_World_Dynamics_Understanding_through_Pluggable_3D_Flow_Learning|FlowVLA: Enabling World Dynamics Understanding through Pluggable 3D Flow Learning]]

![[assets/2610.16160_figure.png|800]]

- **arXiv**: [2610.16160](https://arxiv.org/abs/2610.16160)
- **PDF**: https://arxiv.org/pdf/2610.16160
- **详细分析**: [[20_Research/Papers/具身智能/FlowVLA_Enabling_World_Dynamics_Understanding_through_Pluggable_3D_Flow_Learning|FlowVLA: Enabling World Dynamics Understanding through Pluggable 3D Flow Learning]]
- **作者**: Junhyeong Go, Mingyu Jung, Woobin Im, Jongbin Ryu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《FlowVLA: Enabling World Dynamics Understanding through Pluggable 3D Flow Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BridgeVLA, FlowVLA, GeoVLA, OpenVLA, PointVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in 3D reconstruction enable the extraction of temporally consistent 3D motion from RGB observations; however, current Vision-Language-Action (VLA) models still predominantly rely on 2D image-text priors. Therefore, they do not accurately represent the fundamental dynamics of the 3D world associated with physical actions. This over-reliance on static 2D visual cues limits the capacity of VLA models in achieving robust robot manipulation. To address these limitations, we introduce FlowVLA, a reconstruction-guided, pluggable 3D flow learning framework aimed at empowering VLA models with an inherent understanding of action-relevant dynamics. Instead of requiring explicit 3D sensor inputs or altering the inference-time architecture, our method is designed to utilize temporally aligned 3D flow only during training. This allows the model to learn the dynamic evolution of the physical scene while preserving the computational efficiency of conventional 2D VLA backbones. To bridge scene-level dynamics with robotic manipulation, we propose a modular 3D flow learning framework with dual-level flow supervision. Specifically, point-level flow guides the model to forecast the future displacements of task-critical 3D points, while TCP-level flow aggregates these motions to align with the robot's TCP trajectories. This dual-level flow supervision encourages the model to focus on semantically meaningful dynamic regions, effectively coupling scene-level motion with precise control signals. Extensive evaluations across simulation and real-world experiments demonstrate that FlowVLA consistently improves manipulation performance, zero-shot robustness, and optimizes data efficiency. FlowVLA adds only lightweight auxiliary heads during training and discards them at inference. Therefore, FlowVLA introduces no additional 3D sensor inputs, architectural modifications, or inference-time computation.

</details>

---

### [[20_Research/Papers/大模型/P-BFM_Perceptive_Behavioral_Foundation_Models_for_Humanoid_Control_via_Unsupervised_Reinforcement_Learning|P-BFM: Perceptive Behavioral Foundation Models for Humanoid Control via Unsupervised Reinforcement Learning]]

![[assets/2610.15833_figure.png|800]]

- **arXiv**: [2610.15833](https://arxiv.org/abs/2610.15833)
- **PDF**: https://arxiv.org/pdf/2610.15833
- **详细分析**: [[20_Research/Papers/大模型/P-BFM_Perceptive_Behavioral_Foundation_Models_for_Humanoid_Control_via_Unsupervised_Reinforcement_Learning|P-BFM: Perceptive Behavioral Foundation Models for Humanoid Control via Unsupervised Reinforcement Learning]]
- **作者**: Xue Wang, Yitang Li, Yiming Zhang, Siqin Wang, Junhan Sun, Zhihao Liu, Yaojie Shen, Jingbo Yuan, Hao Zhao, Qingdu Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 3.3（加权：具身智能 1.5，大模型 0.1，强化学习 0.6，机器人 1.1）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《P-BFM: Perceptive Behavioral Foundation Models for Humanoid Control via Unsupervised Reinforcement Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Behavioral foundation models (BFMs) provide humanoids with reusable repertoires of whole-body behaviors; in real-world humanoid control, the same behavioral intent may require fundamentally different motions under different terrain constraints. Covering such variation with terrain-matched demonstrations requires enumerating a combinatorial space of behaviors and terrain geometries. We introduce P-BFM, a perceptive behavioral foundation model that factorizes humanoid control into terrain-invariant intent and terrain-conditioned realization. A forward-backward representation maps motion references, target states, and reward functions into a shared intent space without terrain information, while a perceptive policy learns how to realize each intent under the surrounding terrain geometry. We further identify a complementary limitation of purely latent control: behavioral latents can preserve local motion patterns while losing precise global progress. We therefore introduce Explicit Root Instructions (ERI), which separates global transport (e.g., heading and planar velocity) from behavioral intent, while leaving local whole-body adaptation to the perceptive policy. This decomposition leads to a characteristic capability absent from conventional BFMs: one fixed intent induces different, terrain-appropriate behaviors, including changes in step height, stride, posture, foothold placement, and contacts, without terrain-specific demonstrations. Across challenging terrains, P-BFM improves motion fidelity, root-control precision, and perturbation recovery over strong baselines. A single frozen policy further supports motion tracking, goal reaching, reward inference, teleoperation, and terrain-aware recovery, and transfers zero-shot to a Unitree G1 using onboard depth sensing.

</details>

---

### [[20_Research/Papers/具身智能/ReTrace_Cross-Stage_Failure_Attribution_for_Self-Improving_Robotic_Manipulation|ReTrace: Cross-Stage Failure Attribution for Self-Improving Robotic Manipulation]]

![[assets/2610.15814_figure.png|800]]

- **arXiv**: [2610.15814](https://arxiv.org/abs/2610.15814)
- **PDF**: https://arxiv.org/pdf/2610.15814
- **详细分析**: [[20_Research/Papers/具身智能/ReTrace_Cross-Stage_Failure_Attribution_for_Self-Improving_Robotic_Manipulation|ReTrace: Cross-Stage Failure Attribution for Self-Improving Robotic Manipulation]]
- **作者**: Yue Yu, Bin Zhu, Junhui Li, Jiayu Wang, Shijie Zhou, Jingjing Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《ReTrace: Cross-Stage Failure Attribution for Self-Improving Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose multimodal foundation models are increasingly capable of directly controlling robots, yet improving their manipulation capabilities through autonomous interaction remains challenging. A key challenge to such self-improvement is learning from failures in complex manipulation tasks involving cross-stage dependencies, where an action may succeed locally but cause a later stage to fail. To address this challenge, we introduce ReTrace, a self-improvement framework for robotic manipulation through autonomous physical interaction and retrospective reasoning, without provided demonstrations or model-parameter updates. ReTrace retrospectively traces downstream failures to earlier decisions, proposes targeted corrections, and evaluates them through subsequent interactions. Across attempts, ReTrace progressively consolidates validated corrections into a reusable manipulation skill that guide subsequent execution. We evaluate ReTrace on four real-world manipulation tasks using a Franka Research 3 robot. On the two tasks with strong cross-stage dependencies, GPT-6 Astra-low improves from 0% to 80% success on plug insertion and from 0% to 100% on ball pouring, while GPT-6 Sol-xhigh improves from 0% to 10% and 0% to 90%, respectively. The learned skills also transfer across model and reasoning configurations and reduce inference-time decision cost in most evaluated settings.

</details>

---

### [[20_Research/Papers/具身智能/$Δ$_Flow_Matching_for_Robot_Foundation_Models|$Δ$ Flow Matching for Robot Foundation Models]]

![[assets/2610.15794_figure.png|800]]

- **arXiv**: [2610.15794](https://arxiv.org/abs/2610.15794)
- **PDF**: https://arxiv.org/pdf/2610.15794
- **详细分析**: [[20_Research/Papers/具身智能/$Δ$_Flow_Matching_for_Robot_Foundation_Models|$Δ$ Flow Matching for Robot Foundation Models]]
- **作者**: Kuangji Zuo, Tuo An, Xinying Guo, Gen Li, Mengfei Zhao, Jiaqi Bai, Bofan Lyu, Zhuoyuan Yu, Jinghan Yang, Jiayi Li, Jindou Jia, Jianfei Yang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《$Δ$ Flow Matching for Robot Foundation Models》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow matching is a common generative recipe for robot foundation models. Vision-language-action models (VLAs) generate action chunks, while world-action models (WAMs) additionally generate future visual states. Both start generation from a fixed Gaussian prior, despite temporal continuity between past and future states and actions. This requires costly training and iterative sampling, especially for WAMs with an additional visual branch. We introduce $Δ$-flow, which constructs the source from recent history with mild noise rather than from a fixed Gaussian prior. This moves the source closer to the target, reducing transport to a small residual $Δ$ that can be learned efficiently and enables single-step inference. We integrate $Δ$-flow into the VLA policy $π_{0.5}$ and the WAM policies ImageWAM and Fast-WAM. On LIBERO, ImageWAM reaches 90% success in one epoch rather than six, and Fast-WAM reaches 95% in two epochs rather than eight. With LoRA fine-tuning, $π_{0.5}$ exceeds its baseline's five-epoch performance after one epoch. Single-step inference gives $1.54\times$, $2.49\times$, and $4.45\times$ speedups on $π_{0.5}$, ImageWAM, and Fast-WAM, respectively. It preserves action smoothness, achieving a $4.5\times$ reduction in action jerk compared with one-step Gaussian sampling. $Δ$-flow reaches state-of-the-art generalization performance on LIBERO-Plus. Action-history sources can be applied to pretrained WAM policies without retraining. Replacing the Gaussian action source at inference largely preserves task success with a single sampling step and can slightly improve it. We further study how action representation and visual information in action learning affect history-to-future prediction in $Δ$-flow. These results show that $Δ$-flow is simple yet effective, improving the efficiency and generalization of robot foundation models.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_Sensor-Gated_Mid-Air_Launch_and_Vision-Based_Recovery_of_a_Child_UAV_on_a_Hovering_Mothership_Drone|Multimodal Sensor-Gated Mid-Air Launch and Vision-Based Recovery of a Child UAV on a Hovering Mothership Drone]]

![[assets/2610.15740_figure.png|800]]

- **arXiv**: [2610.15740](https://arxiv.org/abs/2610.15740)
- **PDF**: https://arxiv.org/pdf/2610.15740
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Sensor-Gated_Mid-Air_Launch_and_Vision-Based_Recovery_of_a_Child_UAV_on_a_Hovering_Mothership_Drone|Multimodal Sensor-Gated Mid-Air Launch and Vision-Based Recovery of a Child UAV on a Hovering Mothership Drone]]
- **作者**: Aashish Sahu, R. Prasanth Kumar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.3（加权：具身智能 0.3，大模型 0.3，机器人 1.7）
- **关联关键词**: Multimodal, ComputerVision, Systems

#### 研究背景与动机

《Multimodal Sensor-Gated Mid-Air Launch and Vision-Based Recovery of a Child UAV on a Hovering Mothership Drone》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Launching a micro unmanned aerial vehicle (UAV) from a hovering carrier and recovering it in flight requires reliable confirmation that the child is securely seated before the carrier is allowed to descend. This is challenging because vision provides relative guidance but does not directly indicate load transfer, and a downward-facing camera can lose its fiducial near touchdown. This letter presents a mothership-child quadrotor system in which mission transitions are gated by complementary nonvisual sensing. An upward-facing single-beam LiDAR on the recovery deck provides a binary occupancy state using hysteresis and a debounce interval derived from the child's occluding footprint and crossing speed; real-time kinematic (RTK) positioning conditions the carrier hover; and carrier thrust provides a proprioceptive indication of load transfer. In ten outdoor missions using an F450-class mothership and a Q250-class child with camera-guided recovery, nine completed successfully while RTK-fixed positioning was maintained through release and capture. A complementary MuJoCo study of fully autonomous fiducial-based recovery achieved touchdown 0.077 m from the deck center, while marker detection was lost within the final approximately 0.2 m above the docked configuration. In simulation, carrier thrust changed by -17.0 N at release and +17.3 N at capture, agreeing within 6% with the child's 18.0 N hover thrust. The results support a sensing architecture in which vision guides the approach, while range and proprioceptive information corroborate the final docking decision.

</details>

---
