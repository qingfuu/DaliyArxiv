# cs.AI | Artificial Intelligence | 2026-11-04

#arxiv #ComputerScience

**论文数**: 34

### [[20_Research/Papers/强化学习/DreamX_Video_Diffusion_Model_is_a_Universal_Latent_Action_Learner|DreamX: Video Diffusion Model is a Universal Latent Action Learner]]

![[assets/2611.05377_figure.png|800]]

- **arXiv**: [2611.05377](https://arxiv.org/abs/2611.05377)
- **PDF**: https://arxiv.org/pdf/2611.05377
- **详细分析**: [[20_Research/Papers/强化学习/DreamX_Video_Diffusion_Model_is_a_Universal_Latent_Action_Learner|DreamX: Video Diffusion Model is a Universal Latent Action Learner]]
- **作者**: Jisoo Kim, Chaehyun Kim, Junsu Kim, Jiho Park, Seongchan Kim, Eunbeen Hong, Soowon Son, Fu-En Yang, Seungryong Kim
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《DreamX: Video Diffusion Model is a Universal Latent Action Learner》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AdaWorld, LARY-Bench, LARYBench, Real-World, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning a universal action representation from video requires modeling dynamics that are consistent across different executions of the same action yet invariant to changes in embodiment and appearance. Existing latent action models infer actions from visual transitions, but their representations often entangle the underlying action with irrelevant visual variations, limiting transfer across embodiments. We introduce DreamX, which repurposes a pretrained video diffusion model as a universal latent action learner. Our approach extracts compact latent actions from the video model's rich spatiotemporal features, compressing each latent video frame by $\boldsymbol{300\times}$ ($\boldsymbol{1{,}200 \rightarrow 4}$ tokens). In addition, by leveraging the video model's generative prior, these latent actions capture action-relevant dynamics disentangled from visual appearance. The resulting latent space serves as a shared action interface across embodiments (human and robot), environments, and action parameterizations. On LARY-Bench, DreamX achieves state-of-the-art performance among latent action models. Moreover, actions encoded in one setting remain effective in another: the latent space supports any-to-any video transfer and zero-shot action transfer across diverse embodiments and environments. Furthermore, this shared interface also enables policy learning in a compact latent action space, reducing the computational cost of video-diffusion-based policies.

</details>

---

### [[20_Research/Papers/具身智能/From_Autonomous_Agents_to_Cognitive_Symbionts_Toward_AI-Augmented_Human_Intelligence|From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence]]

![[assets/2611.05376_figure.png|800]]

- **arXiv**: [2611.05376](https://arxiv.org/abs/2611.05376)
- **PDF**: https://arxiv.org/pdf/2611.05376
- **详细分析**: [[20_Research/Papers/具身智能/From_Autonomous_Agents_to_Cognitive_Symbionts_Toward_AI-Augmented_Human_Intelligence|From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence]]
- **作者**: Hao Fei
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.05（加权：具身智能 0.3，大模型 0.55，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For a decade, progress in artificial intelligence has been measured by how much a machine can do on its own. Large foundation models now write code and run multistep tasks, and personal agents act on a person's behalf. Yet people still forget what they once knew, miss what they are not looking at, fail to find the right words, and face hard choices without the benefit of their own history, because the machine that could help stands outside the situation. As AI moves into the physical world, attention has settled on one kind of intelligent individual, the embodied robot; we argue that the era of Physical AI holds a second kind of equal importance, the person augmented by AI. Alongside artificial general intelligence, which asks how intelligent a machine can be, stands AI-augmented human intelligence (AHI), which asks how much intelligence a machine can enable in a particular person. Realizing it calls for a new kind of system, a cognitive symbiont: a lifelong, embedded, real-time, private, low-friction, and proactive companion that senses what the person senses through external devices, keeps their context across years, models their situation and their mind, takes part in their thinking at the right moment, carries out everyday tasks with their context, and keeps learning the person as both change. We give the paradigm a conceptual core, the cognitive gap between what a person could bring to a situation and what they can hold in working memory, and organize its design space as a symbiosis loop of sensing, keeping, understanding, living alongside, acting for and thinking with the person, and growing, enclosed by a personal runtime and by trust. Because a symbiont changes what a person can do in front of others, it also raises risks of a new kind, from covert assistance in examinations to pressure on everyone to adopt it, and we treat their governance as part of the paradigm.

</details>

---

### [[20_Research/Papers/大模型/PyRUA-DataFarm_LLM_Agent_as_a_Cost-Efficient_Teleoperator_for_Real-Ready_Robot_Data|PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data]]

![[assets/2611.05320_figure.png|800]]

- **arXiv**: [2611.05320](https://arxiv.org/abs/2611.05320)
- **PDF**: https://arxiv.org/pdf/2611.05320
- **详细分析**: [[20_Research/Papers/大模型/PyRUA-DataFarm_LLM_Agent_as_a_Cost-Efficient_Teleoperator_for_Real-Ready_Robot_Data|PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data]]
- **作者**: Kewei Zhang, Juncheng Ma, Guodong Lv, Duomin Wang, Feixiang Ruan, Ruiyang Si, Chuanrui Zhang, Yuxuan Chen, Hao Chen, Yichen Liu, Yintianrun Zhang, Yufan Deng...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.3，大模型 0.7，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SplatSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch. We ask whether a coding agent can take over the teleoperator's job. In our DataFarm, the agent receives a data request and one calibration episode of the robot in the target scene and rebuilds the task in simulation: it writes the scene, an expert controller, and a success judge. The simulator supplies exact actions, and a video model conditioned on real images renders each rollout as photographic video, generating all camera views together consistently. The output is real-ready data: synchronized camera views labelled with the robot's actions, on which a policy can be trained directly and deployed on the real robot. Independent judges certify the expert and every rendered episode before admission. On five real-robot tasks, policies trained only on farm data match policies trained on as many teleoperated episodes (93 vs. 84 successes in 100 trials), and under an unseen tablecloth and coloured light they keep 87 successes where the teleoperation-trained policies fall to 46. Adapting a task is fully automatic and costs \$21 of API usage on average, paid once per task, plus \$5 for a render contract; every further episode costs \$0.80 on average for simulation, rendering, and review, with no robot or operator. One hour of three-view data for a task costs \$107 on average, these costs included, slightly below a quote of \$117 for teleoperation in China and below \$290 in labour alone in North America.

</details>

---

### [[20_Research/Papers/具身智能/JHiMA-WebRL_A_Joint_Hierarchical_Multi-Agent_Reinforcement_Learning_Framework_for_Long-Horizon_Web_Tasks|JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks]]

![[assets/2611.05263_figure.png|800]]

- **arXiv**: [2611.05263](https://arxiv.org/abs/2611.05263)
- **PDF**: https://arxiv.org/pdf/2611.05263
- **详细分析**: [[20_Research/Papers/具身智能/JHiMA-WebRL_A_Joint_Hierarchical_Multi-Agent_Reinforcement_Learning_Framework_for_Long-Horizon_Web_Tasks|JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks]]
- **作者**: Shanka Subhra Mondal, Jiayun Wang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.6（加权：大模型 0.6，强化学习 1）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：JHiMA-WebRL, OSWorld, OpenWebRL, SWIRL, WebRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal web agents have shown promising capabilities for interacting with websites through graphical user interfaces (GUIs), yet realistic web tasks often require long-horizon, multi-step planning that remains challenging for monolithic policies. Such agents must jointly infer high-level plans, navigate through intermediate states, track progress over extended interaction histories, and execute visually grounded actions. Although prior work has explored modular multi-agent systems with a separate planner, the planner is typically not updated jointly with the actor. We investigate whether explicitly separating and jointly training planning and execution provides a stronger inductive bias for long-horizon web navigation. We introduce JHiMA-WebRL, a joint hierarchical multi-agent reinforcement learning framework for web agents that couples a task decomposer with an actor. To train the decomposer, we use a strong teacher model to construct structured subtask supervision from multimodal GUI trajectories, and use these annotations to fine-tune both the decomposer and the subtask-conditioned actor. We then extend Group Relative Policy Optimization (GRPO) to jointly optimize the decomposer and actor in the interactive WebArena environment through hierarchical rollout grouping and role-specific advantages. On WebArena-Lite-v2, JHiMA-WebRL-14B, consisting of a 7B actor and a 7B decomposer, achieves an average success rate of 37.2%, compared with 24% for a ScaleCUA-32B agent that we fine-tune with RL on the same training tasks and evaluate under the same protocol. Ablations show that jointly updating the decomposer during RL outperforms updating the actor alone. These results suggest that jointly learned role factorization with smaller models can be a competitive alternative to scaling monolithic agents for long-horizon web tasks.

</details>

---

### [[20_Research/Papers/强化学习/RoboTryOn_Synthesizing_Dexterous_Robot_Demonstrations_from_Human_Videos_via_Virtual_Try-On|RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On]]

![[assets/2611.05163_figure.jpg|800]]

- **arXiv**: [2611.05163](https://arxiv.org/abs/2611.05163)
- **PDF**: https://arxiv.org/pdf/2611.05163
- **详细分析**: [[20_Research/Papers/强化学习/RoboTryOn_Synthesizing_Dexterous_Robot_Demonstrations_from_Human_Videos_via_Virtual_Try-On|RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On]]
- **作者**: Seungyong Lee, Suhyeok Jang, Minyoung Kim, Jinwoo Shin
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.0（加权：具身智能 1.5，世界模型 0.2，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On》归入 具身智能、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot foundation models have shown remarkable performance in robot control, yet adapting them to a new task still relies heavily on teleoperated demonstrations. Egocentric human videos offer a scalable substitute, but overlaying rendered robots on human videos or retargeting human poses into robot actions leaves significant visual or action gaps for high-DoF robot embodiments. To address this limitation, we propose RoboTryOn, which treats human-to-robot translation as virtual try-on: try-on keeps the person and swaps the garment, RoboTryOn keeps the demonstrated motion and swaps the human for the robot. Specifically, RoboTryOn converts a human video into a video of the target robot specified by a reference image, while preserving the original task, objects, and background. To maintain visual consistency, we translate selected keyframes autoregressively and use them to guide video synthesis with motion conditioned on the human hand skeleton. Additionally, we use an inverse dynamics model (IDM) that incorporates depth features to infer action labels from synthesized videos for policy learning. Our experiments across multiple humanoid embodiments show that policies trained with our synthetic data improve the average success rate on novel tasks, including challenging bimanual manipulation, from 2% to 60%, without any real robot demonstration of those tasks. Moreover, training with our synthetic data matches the performance of policies trained solely on teleoperated demonstrations at approximately a third of the collection cost, demonstrating the cost efficiency of our approach.

</details>

---

### [[20_Research/Papers/具身智能/Asynchronous_Robot_Policies|Asynchronous Robot Policies]]

![[assets/2611.05155_figure.png|800]]

- **arXiv**: [2611.05155](https://arxiv.org/abs/2611.05155)
- **PDF**: https://arxiv.org/pdf/2611.05155
- **详细分析**: [[20_Research/Papers/具身智能/Asynchronous_Robot_Policies|Asynchronous Robot Policies]]
- **作者**: Sombit Dey, Luc Van Gool, Danda Pani Paudel
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.2，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Asynchronous Robot Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AR-VLA, AsyncVLA, Franka-DROID。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling vision-language foundation models has significantly advanced generalist robot manipulation, but the increased model scale introduces computational latency that degrades real-time physical reactivity. Existing Vision-Language-Action (VLA) architectures execute high-level semantic reasoning and action ex- ecution sequentially within the primary control loop, creating a fundamental tension between semantic-reasoning capability and robot agility. To address this, we propose Asynchronous Robot Policy (ARP), an architectural framework that decouples semantic reasoning from low-level action generation using asynchronous processes operating at independent frequencies. In ARP, a high-capacity Vision-Language Model (VLM) asynchronously updates a semantic memory at low fre- quency, while a lightweight Vision-Action Expert, conditioned on this semantic memory, generates robot actions at a much higher control frequency. Such a formulation, enables having a fast perception-action loop without compromising on the semantic capability. To overcome asynchronous memory staleness, ARP trains the vision-action expert on the semantic staleness and execution delay, with temporally mismatched observation across processes. On Franka manipulation tasks, ARP achieves an 18% higher success rate and 20% less time need for execution in quasi-static setups, while 3-5 times baseline performance in dynamic simulation environments. Furthermore, ARP enables operating the VLM at 10 times lower than its nominal frequency with no significant performance loss making it much more efficient than the baseline. These results highlight the architectural advantages of modeling robot policies as asynchronous processes, enabling real-world reactive deployment without sacrificing the scale of foundation models.

</details>

---

### [[20_Research/Papers/强化学习/Catalyzing_Interactive_HTML_Generation_Capabilities_via_High-Fidelity_Reinforcement_Learning|Catalyzing Interactive HTML Generation Capabilities via High-Fidelity Reinforcement Learning]]

![[assets/2611.05151_figure.png|800]]

- **arXiv**: [2611.05151](https://arxiv.org/abs/2611.05151)
- **PDF**: https://arxiv.org/pdf/2611.05151
- **详细分析**: [[20_Research/Papers/强化学习/Catalyzing_Interactive_HTML_Generation_Capabilities_via_High-Fidelity_Reinforcement_Learning|Catalyzing Interactive HTML Generation Capabilities via High-Fidelity Reinforcement Learning]]
- **作者**: Xujia Wang, Yixuan Liu, Shaohan Huang, Furu Wei, Lei Hou, Bin Xu, Juanzi Li
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Catalyzing Interactive HTML Generation Capabilities via High-Fidelity Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Cookie-Bench, WebGen-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating HTML from natural-language specifications is an important application of code large language models (LLMs). Despite producing renderable pages, current models often fail to ensure functionality and visual quality during actual interaction. Existing methods typically target task-specific webpage supervision, leaving demanding interactive artifact optimization underexplored. Using mini-games as a challenging testbed, we expose limitations in interaction experience, reward signal, and credit assignment fidelity that are obscured by shallow webpage interactions. We introduce WebCatalyst, a browser-interaction reinforcement learning framework with three complementary components: a game-level GUI assessor for sustained interaction and evaluation, Visual Anchor for mitigating VLM reward hacking, and Action-Trace Credit for grounding token-level credit assignment in runtime execution traces. Trained on fewer than 1K requests, predominantly for games, WebCatalyst raises the Cookie-Bench Mini Games score from 68.8 to 75.3 and also the WebGen-Bench accuracy from 48.8 to 56.9 on Qwen3.6-35B-A3B, outperforming Claude Opus 4.7 in average rank across evaluated metrics. Further analysis shows that Visual Anchor prevents aesthetic degradation, while runtime-grounded credit assignment accelerates functional improvement. Together, our results show that improving feedback fidelity is the key to substantially advancing interactive HTML generation.

</details>

---

### [[20_Research/Papers/世界模型/Trajectory_Evaluation_via_Rollout-Free_World_Model_for_End-to-end_Autonomous_Driving|Trajectory Evaluation via Rollout-Free World Model for End-to-end Autonomous Driving]]

![[assets/2611.05072_figure.png|800]]

- **arXiv**: [2611.05072](https://arxiv.org/abs/2611.05072)
- **PDF**: https://arxiv.org/pdf/2611.05072
- **详细分析**: [[20_Research/Papers/世界模型/Trajectory_Evaluation_via_Rollout-Free_World_Model_for_End-to-end_Autonomous_Driving|Trajectory Evaluation via Rollout-Free World Model for End-to-end Autonomous Driving]]
- **作者**: Junzhe Wang, Jinqing Zhang, Qingjie Liu
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Trajectory Evaluation via Rollout-Free World Model for End-to-end Autonomous Driving》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although existing candidate trajectory evaluators have substantially improved end-to-end planning accuracy, their underlying mechanism remains suboptimal. Model-based evaluators typically make scoring future-aware by explicitly predicting candidate-conditioned future states over the planning horizon, which we term rollout. However, rollout incurs high inference cost and accumulates prediction errors. We argue that planning does not require reconstructing a full future scene for each candidate, but only future-relevant information for reliable comparison. We therefore propose RFWorld, a Rollout-Free World model for end-to-end trajectory evaluation. RFWorld constructs a shared scene memory and shapes it into a future-readable representation via lightweight training-time temporal readout with semantic supervision, keeping training overhead low. At inference time, candidate trajectories directly query the shared memory via sparse spatial readout for scoring, reducing computation by roughly the planning horizon times the number of candidate trajectories, while avoiding recursive rollout errors. Experiments on NAVSIM and Bench2Drive show that RFWorld learns a more planning-aligned world representation and achieves state-of-the-art performance.

</details>

---

### [[20_Research/Papers/大模型/Do_Agentic_Policies_Need_to_Look_at_Every_Step_Geometric_Abstraction_for_Reasoning_and_Action|Do Agentic Policies Need to Look at Every Step? Geometric Abstraction for Reasoning and Action]]

![[assets/2611.05058_figure.png|800]]

- **arXiv**: [2611.05058](https://arxiv.org/abs/2611.05058)
- **PDF**: https://arxiv.org/pdf/2611.05058
- **详细分析**: [[20_Research/Papers/大模型/Do_Agentic_Policies_Need_to_Look_at_Every_Step_Geometric_Abstraction_for_Reasoning_and_Action|Do Agentic Policies Need to Look at Every Step? Geometric Abstraction for Reasoning and Action]]
- **作者**: Yihang Liu, Yiming Chen, Mingzhe Zheng
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Do Agentic Policies Need to Look at Every Step? Geometric Abstraction for Reasoning and Action》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent multimodal language models can reason directly about robot scenes, but it is unclear whether they need to repeatedly reinterpret raw visual observations at every step of an interaction. We propose shifting routine spatial reasoning from images to text and symbols through a 3D geometric abstraction that is refreshed locally from observations and read directly by the language models. Specifically, our interface represents scene geometry via typed, evidence-aware symbolic references to object parts, grounds them from calibrated RGB-D, and returns compact textual checkpoints with metric residuals after each action. Symbolic task structure can thus be reused across decisions while metric values are rebound to the current scene, with direct visual reasoning invoked only on demand. Across offline policy synthesis and continuous online execution, reasoning over grounded text and symbols improves multi-step manipulation completion while substantially reducing repeated multimodal queries, positioning explicit geometric state as an effective substrate for agentic robot policies.

</details>

---

### [[20_Research/Papers/大模型/LLMs_as_MDP_Designers_A_Dependency-Aware_Agentic_Framework_for_Automated_Robot_Policy_Generation|LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation]]

![[assets/2611.04974_figure.png|800]]

- **arXiv**: [2611.04974](https://arxiv.org/abs/2611.04974)
- **PDF**: https://arxiv.org/pdf/2611.04974
- **详细分析**: [[20_Research/Papers/大模型/LLMs_as_MDP_Designers_A_Dependency-Aware_Agentic_Framework_for_Automated_Robot_Policy_Generation|LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation]]
- **作者**: Hong Je-Gal, Jinwoo Kim, Chanbin Yi, Hyun-Suk Lee
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 大模型
- **相关性评分**: 2.7（加权：具身智能 0.3，大模型 0.1，强化学习 1，机器人 1.3）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We investigate the automated generation of executable robot reinforcement learning (RL) policies from natural-language task descriptions. Rather than using large language models (LLMs) as execution-time decision makers, we use them as designers that construct RL pipelines before deployment, including Markov decision process (MDP) formulation and simulator implementation. We identify a phase-wise structure in this problem: MDP formulation is dependency-structured and sequential, whereas simulator implementation becomes modular once the formulation is fixed. Based on this structure, we propose ARPG, a dependency-aware agentic framework that performs sequential MDP modeling, localized verification and correction, and simulator-structured implementation while externalizing intermediate artifacts. ARPG targets a key failure mode of automated policy generation: executable code may still yield non-learnable policies when state, action, reward, and termination artifacts are not semantically aligned. Experiments in Isaac Sim show that ARPG improves modeling correctness, environment executability, and policy-generation success compared with monolithic LLM baselines and off-the-shelf agentic systems. Additional demonstrations on custom robotics, standard RL, and engineering-domain MDPs further suggest that the same modeling pipeline can be reused beyond the main benchmark suite.

</details>

---

### [[20_Research/Papers/大模型/VisSearch-Bench_Evaluating_Long_Horizon_Visual_Search_in_Multimodal_Agents|VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents]]

![[assets/2611.04894_figure.png|800]]

- **arXiv**: [2611.04894](https://arxiv.org/abs/2611.04894)
- **PDF**: https://arxiv.org/pdf/2611.04894
- **详细分析**: [[20_Research/Papers/大模型/VisSearch-Bench_Evaluating_Long_Horizon_Visual_Search_in_Multimodal_Agents|VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents]]
- **作者**: ZhengXian Wu, Qianhao Nie, Zhuohong Chen, Junjie Gao, Yuyao Zhang, Yunyao Yu, Hangrui Xu, Cheng Cheng, Guiyu Ma, Jin Zhang, Xingzhong Xu, Kai Yang...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DeepSearchQA, VDR-Bench, VisBrowse-Bench, VisSearch-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal agents use web and image tools to answer questions beyond their internal knowledge. Some search tasks use images mainly to identify an initial entity, then rely on text retrieval. These tasks offer limited insight into how agents connect information across images, objects, and search steps. We therefore focus on visual context management. This involves organizing and using visual information and linking it to other findings during search. Visually intensive tasks require agents to combine object appearance, local details, or spatial relations with external information. We introduce VisSearch-Bench, with 204 human-written tasks across 7 main domains and 25 subdomains. It covers Set-wise Visual Search, Sequential Visual Search, Hybrid Wide-Deep Search, Competitive Visual Disambiguation, and Visual-Structure-Guided Search. Each task provides a reference answer, traceable evidence, and scoring rules. Accuracy measures complete task success, while Process Score measures the correctness and completeness of individual results and subquestion answers. Across 16 multimodal models, the best system fully solves only 26.47% of tasks, even with search tools. These results highlight the challenge of linking visual evidence with search results to produce complete answers.

</details>

---

### [[20_Research/Papers/具身智能/HTCE_Homeomorphism-inspired_Topological_Cross-Scene_Experience_Canonicalization_and_Reuse_for_Object_Navigation|HTCE: Homeomorphism-inspired Topological Cross-Scene Experience Canonicalization and Reuse for Object Navigation]]

![[assets/2611.04836_figure.png|800]]

- **arXiv**: [2611.04836](https://arxiv.org/abs/2611.04836)
- **PDF**: https://arxiv.org/pdf/2611.04836
- **详细分析**: [[20_Research/Papers/具身智能/HTCE_Homeomorphism-inspired_Topological_Cross-Scene_Experience_Canonicalization_and_Reuse_for_Object_Navigation|HTCE: Homeomorphism-inspired Topological Cross-Scene Experience Canonicalization and Reuse for Object Navigation]]
- **作者**: Xiaoran Xu, Yupeng Wu, Tianyu Xue, Xuanran Dong, Yifan Xu, Xiaoshan Yang, Changsheng Xu
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 1.2，大模型 0.1）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《HTCE: Homeomorphism-inspired Topological Cross-Scene Experience Canonicalization and Reuse for Object Navigation》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GOAT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As embodied agents perform object-goal navigation across residential environments, they accumulate successful experiences whose semantic structure recurs across scenes even when geometric trajectories do not. Reusing such experience is challenging because differences in region naming and observation granularity produce distinct graph representations of similar approaches, while meaningful differences in anchors, branches, and endpoints must stay distinguishable. We introduce HTCE, a homeomorphism-inspired topological framework that canonicalizes and reuses navigation experience. Feature and topology subdivisions characterize representational variations, and their semantically constrained reductions produce comparable semantic sequences and structural signatures while preserving semantic anchors, branching relations, and navigation endpoints. HTCE then retrieves historical successful approaches through subdivision-aware matching as guidance for a frozen vision-language policy. Canonicalization compresses the experience index losslessly, merging 17.7--23.6\% of distinct stored route descriptions while retaining full task performance. Under a single frozen vision-language backbone shared by all compared systems, HTCE attains the best SR and SPL in every setting---59.9\%/31.8\% on HM3D v0.1, 71.0\%/31.5\% on HM3D v0.2, and 46.6\%/16.6\% on MP3D---with SR gains of up to 4.9 points and structured retrieval contributing up to 2.8 SPL points. The code is available in https://github.com/startracker0/htce.git

</details>

---

### [[20_Research/Papers/强化学习/Reconstructing_Fraudulent_Strategies_in_Online_Payments_via_Interpretable_Inverse_Reinforcement_Learning|Reconstructing Fraudulent Strategies in Online Payments via Interpretable Inverse Reinforcement Learning]]

![[assets/2611.04819_figure.png|800]]

- **arXiv**: [2611.04819](https://arxiv.org/abs/2611.04819)
- **PDF**: https://arxiv.org/pdf/2611.04819
- **详细分析**: [[20_Research/Papers/强化学习/Reconstructing_Fraudulent_Strategies_in_Online_Payments_via_Interpretable_Inverse_Reinforcement_Learning|Reconstructing Fraudulent Strategies in Online Payments via Interpretable Inverse Reinforcement Learning]]
- **作者**: Huilin He, Weiyu Han, Linbo Shao, Ruobing Zuo, Xiao Tan, Shuai Chen, Dawei Cheng
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL, ComputerVision, Security

#### 研究背景与动机

《Reconstructing Fraudulent Strategies in Online Payments via Interpretable Inverse Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Payment fraud causes financial losses and undermines users' trust in web payment services. Although fraud detection is a critical defense for payment security, complex and diverse fraudulent behaviors can still evade detection. Generating fraud samples for data augmentation can broaden detectors' coverage of different fraud patterns. However, existing methods matching the distribution of transaction attributes alone do not ensure that generated sequences preserve the sequential relationships among transaction choices, payment feedback, and subsequent behavioral adjustments. To this end, we propose PaySeqGen, an interpretable inverse reinforcement learning framework that reconstructs fraud behavior policies from fraudsters' observed payment trajectories. We design a mechanism for constructing candidate actions to support plausible payment sequence generation while enabling exploration. The framework also learns interpretable behavioral rewards that capture fraudsters' preferences across different transaction contexts. By alternating between reward learning and policy optimization, the framework reconstructs policies that generate new fraud sequences for detector augmentation and learns interpretable rewards supporting sequential fraud-pattern analysis in real trajectories. Experiments in real-world payment scenarios at Ant International, a leading global digital payment provider, show that PaySeqGen outperforms state-of-the-art generative augmentation methods. Reward-based trajectory analysis also identifies fraud patterns of practical value, helping analyst locating suspicious segments and examine multistep fraud tactics. Evaluation in the deployed system of online payment further confirms its effectiveness.

</details>

---

### [[20_Research/Papers/具身智能/Density-Aware_Reward_Scaling_A_Reinforcement_Learning_Framework_for_Reward-Proportional_Sampling|Density-Aware Reward Scaling: A Reinforcement Learning Framework for Reward-Proportional Sampling]]

![[assets/2611.04792_figure.png|800]]

- **arXiv**: [2611.04792](https://arxiv.org/abs/2611.04792)
- **PDF**: https://arxiv.org/pdf/2611.04792
- **详细分析**: [[20_Research/Papers/具身智能/Density-Aware_Reward_Scaling_A_Reinforcement_Learning_Framework_for_Reward-Proportional_Sampling|Density-Aware Reward Scaling: A Reinforcement Learning Framework for Reward-Proportional Sampling]]
- **作者**: Ria Shekhawat, Abhijeet Sinha, Yingtao Zhu, Dianbo Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《Density-Aware Reward Scaling: A Reinforcement Learning Framework for Reward-Proportional Sampling》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GFlowNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning objectives that maximize expected return can concentrate probability mass on a small subset of high-reward outcomes, limiting diversity when multiple distinct solutions are desirable. We introduce Density-Aware Reward Scaling (DARS), a simple reward-processing mechanism that promotes reward-proportional sampling in continuous outcome spaces while retaining standard policy-gradient training. DARS estimates the local density of outcomes within each on-policy rollout group and inversely scales rewards by this density. The method requires no learned density model, auxiliary objective, critic, or modification to the underlying policy-gradient objective. In a controlled multimodal navigation task, DARS-GRPO avoids the single-mode collapse exhibited by GRPO and closely recovers the target mode allocation. Applied to text-to-image prompt adaptation, DARS-GRPO consistently improves image and prompt diversity across datasets, Policy LMs, and reward settings while maintaining good semantic alignment. These results show that density-aware reward scaling provides a lightweight way to improve coverage of diverse high-reward outcomes within existing reinforcement-learning pipelines.

</details>

---

### [[20_Research/Papers/机器人/CLARA_A_Cognitively-Driven_Clarification_Framework_for_Grounding_Ambiguous_Requests|CLARA: A Cognitively-Driven Clarification Framework for Grounding Ambiguous Requests]]

![[assets/2611.04708_figure.jpeg|800]]

- **arXiv**: [2611.04708](https://arxiv.org/abs/2611.04708)
- **PDF**: https://arxiv.org/pdf/2611.04708
- **详细分析**: [[20_Research/Papers/机器人/CLARA_A_Cognitively-Driven_Clarification_Framework_for_Grounding_Ambiguous_Requests|CLARA: A Cognitively-Driven Clarification Framework for Grounding Ambiguous Requests]]
- **作者**: Dimitrios Bekris, Marios Glytsos, Panagiotis P. Filntisis, Niki Efthymiou, George Retsinas, Petros Maragos
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《CLARA: A Cognitively-Driven Clarification Framework for Grounding Ambiguous Requests》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotics and AI systems are increasingly deploying large vision-language models (LVLMs) to follow high-level instructions, from routine household chores to more complex organizational tasks. Yet, broad directives like "clean the room" or "organize the desk" frequently omit crucial details about user preferences and specific arrangement of objects that influence the desired outcome. Without any further guidance, such models tend to overestimate their grasp of ambiguous instructions and frequently assume they have sufficient understanding despite missing important details. In this paper, we propose CLARA (Conversational cLArification for Robotic Arrangement), a cognitively-driven clarification framework that proactively elicits key information from users, in a similar fashion as humans' clarification seeking behavior. Through targeted questioning, CLARA refines ambiguous requests into structured, detailed instructions describing precisely how objects should be organized or rearranged, according to the user's preferences. These clarifications then guide a diffusion-based image generation pipeline, producing realistic visual renderings of the final, desired scene. This final rendering also serves as a visual confirmation of the system's understanding from the user. Experimental results and user studies demonstrate that CLARA leads to more accurate and consistent outcomes compared to another State-of-the-Art LVLM system, highlighting the importance of interactive clarification for bridging the gap between vague directives and fully grounded task specifications.

</details>

---

### [[20_Research/Papers/大模型/A_research_world_model_of_power_engineering_learns_its_dynamics_and_reveals_what-ifs|A research world model of power engineering learns its dynamics and reveals what-ifs]]

![[assets/2611.04566_figure.png|800]]

- **arXiv**: [2611.04566](https://arxiv.org/abs/2611.04566)
- **PDF**: https://arxiv.org/pdf/2611.04566
- **详细分析**: [[20_Research/Papers/大模型/A_research_world_model_of_power_engineering_learns_its_dynamics_and_reveals_what-ifs|A research world model of power engineering learns its dynamics and reveals what-ifs]]
- **作者**: Fanping Sui, Ying Zhang, Liwei Lin
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，世界模型 1）
- **关联关键词**: LLM, WorldModel, Systems

#### 研究背景与动机

《A research world model of power engineering learns its dynamics and reveals what-ifs》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Decisions about the direction of research in power engineering determine which technologies mature and, through them, shape infrastructure that lasts decades, yet their consequences cannot be observed before they are taken, and existing forecasts of research fields extrapolate a single trajectory. Here we introduce research world models, which treat a research field as a dynamical system that can be acted upon, and establish one for power engineering from 1.1 million papers. A distilled language model reads each paper into role-typed concepts, two sophisticated, high-fidelity graph-temporal neural network cores learn how the resulting concept network evolves, and operators learned from natural experiments in the publication record estimate the effects of interventions. In temporally held-out tests, the model forecast years ahead which concepts would grow and which method-target pairs would be joined for the first time, outperforming tuned machine-learning baselines in most settings, and its estimated intervention effects tracked those realized in natural experiments it had not seen. Its training scheme and three of its operators replicated in two fields withheld from development. Questions posed in natural language are compiled by a domain-specialized 27-billion-parameter language model into executable actions and answered as paired simulations with and without the intervention. The answers were rated 4.1 of 5 for faithfulness by an independent language-model judge. By revealing the latent dynamics of a research field and its response to interventions, research world models offer a new way to simulate and test research decisions before they are made.

</details>

---

### [[20_Research/Papers/强化学习/CANDO_Conservative_Action-Noise_Directional_Optimization_for_Residual_Reinforcement_Learning|CANDO: Conservative Action-Noise Directional Optimization for Residual Reinforcement Learning]]

![[assets/2611.04543_figure.png|800]]

- **arXiv**: [2611.04543](https://arxiv.org/abs/2611.04543)
- **PDF**: https://arxiv.org/pdf/2611.04543
- **详细分析**: [[20_Research/Papers/强化学习/CANDO_Conservative_Action-Noise_Directional_Optimization_for_Residual_Reinforcement_Learning|CANDO: Conservative Action-Noise Directional Optimization for Residual Reinforcement Learning]]
- **作者**: Zeyu Gao, Chengkai Hou, Chaoyue Li, Zhuangzhe Wu, Jiaming Liu, Yao Mu, Peng Jia, Li Zhang, Shanghang Zhang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型
- **相关性评分**: 1.32（加权：强化学习 0.96，世界模型 0.16，机器人 0.2）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《CANDO: Conservative Action-Noise Directional Optimization for Residual Reinforcement Learning》归入 强化学习、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DSRL, IBRL, SPiRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained generative policies provide strong behavior priors for robot control, but adapting them efficiently with online reinforcement learning remains difficult. A central challenge is how to improve a frozen generative policy without destroying the structure learned from offline demonstrations. Noise-space residual methods address this by modifying the policy's input noise, but existing noise-space methods typically regulate adaptation through fixed latent feasible regions, which may exclude valuable noise edits. In contrast, action-space residual methods are more sample-efficient, but their efficiency can still be further improved. We propose Conservative Noise Directional Optimization (CNDO), a noise-space residual RL method that improves a frozen generative policy by learning state- and noise-conditioned directions around Gaussian latent samples. CNDO removes predefined latent feasible regions and instead regulates noise-space adaptation through the soft conservative constraint, which consists of conservative value estimation and gated execution. We further introduce Conservative Action-Noise Directional Optimization (CANDO), which adds an action-space residual, combining structured latent-space improvement with local action correction. Experiments show that, once CNDO narrows the gap between noise-space and action-space residual learning, CANDO further improves over single-space optimization, achieving 76.1 NAUC and a 91.4% final success rate, surpassing the best single-space results by 6.6 NAUC and 4.1% success rate. More demos and info are available on https://cando-rl.github.io/.

</details>

---

### [[20_Research/Papers/大模型/Large_Language_Model-Assisted_Adaptive_Heuristic_Search_for_Agile_Earth_Observation_Satellite_Scheduling|Large Language Model-Assisted Adaptive Heuristic Search for Agile Earth Observation Satellite Scheduling]]

![[assets/2611.04458_figure.png|800]]

- **arXiv**: [2611.04458](https://arxiv.org/abs/2611.04458)
- **PDF**: https://arxiv.org/pdf/2611.04458
- **详细分析**: [[20_Research/Papers/大模型/Large_Language_Model-Assisted_Adaptive_Heuristic_Search_for_Agile_Earth_Observation_Satellite_Scheduling|Large Language Model-Assisted Adaptive Heuristic Search for Agile Earth Observation Satellite Scheduling]]
- **作者**: He Wang, Yeye Liu, Ruijie Li, Xuemei Jiang, Junyu Wu, Lining Liu Zhuoqi Man, Tao Li, Yanjie Song
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM

#### 研究背景与动机

《Large Language Model-Assisted Adaptive Heuristic Search for Agile Earth Observation Satellite Scheduling》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agile Earth observation satellites must coordinate imaging tasks within limited observation windows, while accounting for attitude maneuvering and onboard energy constraints. Competition among observation opportunities makes scheduling performance sensitive to the heuristic rules used for task selection. This letter proposes a large language model (LLM)-assisted adaptive heuristic search method for agile Earth observation satellite scheduling. The LLM generates an initial heuristic rule according to the characteristics of the scheduling instance. During the subsequent ant colony search, search performance and scheduling information are fed back to the LLM to refine the heuristic rule. The proposed modifications are evaluated through paired solution constructions before being incorporated into the search process. A unified scheduling procedure determines task selection, satellite assignment, and observation timing under the operational constraints. Experiments on six scheduling scenarios involving 50--200 imaging tasks demonstrate that the proposed method achieves 4.3\%--9.6\% higher mean observation benefit than the strongest baseline.

</details>

---

### [[20_Research/Papers/具身智能/Human-to-Robot_Transfer_via_Bridging_Representation_and_Action_Space_in_VLAs|Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs]]

![[assets/2611.04391_figure.png|800]]

- **arXiv**: [2611.04391](https://arxiv.org/abs/2611.04391)
- **PDF**: https://arxiv.org/pdf/2611.04391
- **详细分析**: [[20_Research/Papers/具身智能/Human-to-Robot_Transfer_via_Bridging_Representation_and_Action_Space_in_VLAs|Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs]]
- **作者**: Junhyeong Park, Wook Jung, Taeyoung Kim, Huiwon Jang, Jinwoo Shin
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.6，机器人 1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained Vision-Language-Action (VLA) policies provide a strong starting point for deployment, but adapting them to a target robot and environment still requires costly embodiment-specific demonstrations. Human demonstrations are far easier to collect, yet directly leveraging them is challenging due to the substantial human-robot embodiment gap, particularly when the underlying VLA has been pretrained primarily on robot data. We introduce H2RB (Human-To-Robot Bridge), a human-robot co-training framework for adapting pretrained VLA policies from unpaired human and robot demonstrations. H2RB bridges the embodiment gap at both interfaces: geometry-anchored alignment grounds human and robot observations in a compatible representation, while a decoupled-decoder tokenizer shares action latents without forcing both domains through a single action mapping. This design allows human demonstrations to provide useful behavioral supervision while retaining the rich visual, semantic, and control priors of the pretrained VLA. Across real-world tasks, H2RB substantially improves object transfer performance from 8.0 to 51.8 and enables skill transfer to score 62.7, in settings where co-train baselines totally fail to transfer human-demonstrated skills. The benefit also persists under object-placement shifts, improving out-of-distribution transfer from 6.0 to 45.3. H2RB suggests a way for human demonstrations to serve as a scalable supervision source for adapting pretrained robotic policies, reducing the dependence on costly target-robot data collection.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_AI_for_Scientific_Discovery_From_Physical_Action_to_Scientific_Evidence|Embodied AI for Scientific Discovery: From Physical Action to Scientific Evidence]]

![[assets/2611.04371_figure.png|800]]

- **arXiv**: [2611.04371](https://arxiv.org/abs/2611.04371)
- **PDF**: https://arxiv.org/pdf/2611.04371
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_AI_for_Scientific_Discovery_From_Physical_Action_to_Scientific_Evidence|Embodied AI for Scientific Discovery: From Physical Action to Scientific Evidence]]
- **作者**: Wenhao Xu, Changwei Wang, Shunpeng Chen, Yukun Song, Sifan Zhou, Kaize Luo, Shibiao Xu, Yuehua Zhao, Rongtao Xu
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.4，世界模型 0.2，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Embodied AI for Scientific Discovery: From Physical Action to Scientific Evidence》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scientific experiments are increasingly selected, executed and interpreted by learned systems that act through physical interfaces. Robot learning builds physical competence, whereas AI for science chooses which experiment to run, each reporting different endpoints. This review treats their interface as one problem, embodied AI for science, where the experiment itself is partially observed: specimen state, apparatus state and measurement processes are latent, actions are costly and irreversible, and missingness depends on execution and outcome. We organize the literature by three closures operating at distinct levels: operational closure (the experiment realized is the one intended), epistemic closure (the result updates beliefs or selects subsequent experiments) and evidential closure (the record supports a claim). We analyze workflows through a record-linked evidence cycle - Record, Diagnose, Calibrate, Confirm - as analytic functions with feedback. A taxonomy crosses these closures with six delegated decisions and five embodiment classes. Our formulation separates commanded, realized and observed conditions and models diagnosis with explicit resource, risk and sample-change costs. We compare experiment-selection methods by terminal decision, review perception, protocol compilation, visuomotor policies, world models, recovery and transfer by evidence emission requirements, and compare chemistry, materials, biology, microscopy and field workflows by what their records establish. An appendix provides an evidence map of 28 workflows (26 physical, two software-boundary), characterizing validation pathways and claim confirmation requirements. We propose evaluation that separates actions, valid experiments, campaigns and confirmed claims, framing open challenges as controlled comparisons with measurable failure conditions.

</details>

---

### [[20_Research/Papers/具身智能/Drift_No_More_Spectral_Locking_for_Long-Horizon_Open-Weight_Multi-Agent_AI|Drift No More: Spectral Locking for Long-Horizon Open-Weight Multi-Agent AI]]

![[assets/2611.04315_figure.png|800]]

- **arXiv**: [2611.04315](https://arxiv.org/abs/2611.04315)
- **PDF**: https://arxiv.org/pdf/2611.04315
- **详细分析**: [[20_Research/Papers/具身智能/Drift_No_More_Spectral_Locking_for_Long-Horizon_Open-Weight_Multi-Agent_AI|Drift No More: Spectral Locking for Long-Horizon Open-Weight Multi-Agent AI]]
- **作者**: Vishal Pramanik, Maisha Maliha, Susmit Jha, Sumit Kumar Jha
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.6）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《Drift No More: Spectral Locking for Long-Horizon Open-Weight Multi-Agent AI》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AMemGym, EverMemBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon multi-agent systems suffer from three tightly coupled failures: task drift, role drift, and state staleness. We test the hypothesis that these share a common representational cause: agent hidden states move away from the directions encoding the active task, assigned role, and current shared state. A pilot study over 14,832 annotated turns supports this: drifted turns collapse near-uniformly across all three anchor subspaces (pairwise r = 0.72-0.78). Existing methods address these failures separately, operating at the surface-text level or treating control directions independently. We introduce ATLAS (Algebraic Task-role Locking with Adaptive Spectral Memory), a training-free intervention acting on hidden states before a token is generated. ATLAS builds a positive-semidefinite anchor kernel over task, role, and state subspaces and steers hidden states toward their shared high-coherence eigendirections; a low-rank Gram decomposition keeps this tractable. Across long-horizon memory, state maintenance, tool use, least-privilege coordination, and embodied stress tests, ATLAS outperforms prompting, retrieval, memory, and activation-steering baselines. Against A-MEM it improves memory macro-average accuracy by up to 5.7 points and reduces write/read failures by up to 31.7%/24.8%; against MemoryArena-Agent it gains up to 4.8 points. It gains 10.7-12.1 points under perturbation, reaches 93.5% role consistency, and transfers to a 72B backbone (macro-average 61.0 vs. 56.2). Ablating the joint task-role-state span costs 7.2 points against 0.8 for a matched-rank random span, indicating these directions are functionally implicated, not incidental; supplying them by prompt or retrieval recovers 4.3 points less. ATLAS is therefore a representation-level controller for open-weight multi-agent systems, complementary to output-level protocols for black-box agents.

</details>

---

### [[20_Research/Papers/具身智能/AceAction-5M_Hierarchical_Goals_for_Generalist_Action_Learning_Across_3D_Game_Worlds|AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds]]

![[assets/2611.04241_figure.png|800]]

- **arXiv**: [2611.04241](https://arxiv.org/abs/2611.04241)
- **PDF**: https://arxiv.org/pdf/2611.04241
- **详细分析**: [[20_Research/Papers/具身智能/AceAction-5M_Hierarchical_Goals_for_Generalist_Action_Learning_Across_3D_Game_Worlds|AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds]]
- **作者**: Kailing Li, Ruoxuan Zhang, Zheyuan Zhou, Boyang Chu, Yingshan Lei, Hongxia Xie, Liang Du, Zixun Sun
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.6，大模型 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MineRL, WildWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video games provide a practical setting for collecting vision-language-action (VLA) data, whose acquisition in physical environments is costly. Existing datasets, however, remain limited by restricted game coverage, sparse language supervision, or temporal hierarchies that do not necessarily reflect changes in task objectives. We introduce AceAction, a dataset of human gameplay across multiple 3D games for learning skill composition and subgoal transitions. AceAction organizes demonstrations around complete tasks, linking overall instructions, ordered subgoals, and local skill instructions to temporally aligned visual observations and keyboard-and-mouse actions. To construct these annotations, we develop a vision-language model pipeline that identifies subgoals from changes in objectives or interaction targets, anchors navigation goals to visually recognizable waypoints, and composes adjacent subgoals into task instructions. The resulting demonstrations cover navigation, reconnaissance, combat, interaction, and recovery, with explicit stage boundaries that connect task progression to fine-grained control. We assess annotation quality through model-based verification and human inspection. An audit of 500 trajectories yields a 95.8% pass rate across independent reviewer assessments. AceAction provides a data foundation for studying how agents execute, combine, and switch skills to follow complex instructions in dynamic game environments.

</details>

---

### [[20_Research/Papers/具身智能/DualWorldBench_Can_Agents_Plan_Deliveries_across_Symbolic_and_Grounded_Worlds|DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?]]

![[assets/2611.04228_figure.png|800]]

- **arXiv**: [2611.04228](https://arxiv.org/abs/2611.04228)
- **PDF**: https://arxiv.org/pdf/2611.04228
- **详细分析**: [[20_Research/Papers/具身智能/DualWorldBench_Can_Agents_Plan_Deliveries_across_Symbolic_and_Grounded_Worlds|DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?]]
- **作者**: Yang Chen, Bin Wen, Danyang Peng, Hong-Jie You, Zi-Qiao Shang, Lan-Zhe Guo
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.6，机器人 0.2）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DualWorld, DualWorld-VQA, DualWorldBench, SimWorld, TextWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent multimodal agents have shown promising progress in embodied planning and web interaction. However, existing evaluations often rely on simplified tasks with limited combinatorial structure, leaving it unclear whether current agents can robustly integrate perception and reasoning for multi-goal planning under temporal, physical, and multimodal constraints. We introduce DualWorldBench, a unified benchmark for evaluating agent planning under controlled symbolic--temporal and grounded--topological complexity. Built around a shared pickup--delivery interface, DualWorldBench consists of three complementary components: TextWorld, which isolates symbolic planning under varying task compositions and release dynamics; SimWorld, which evaluates grounded path planning under controlled topological variation with text, image, or multimodal inputs; and DualWorld-VQA, a diagnostic suite spanning perception, scene understanding, and planning. Experiments reveal a common gap between local understanding and globally consistent planning. In TextWorld, agents struggle to derive optimal task sequences under interacting temporal constraints; in SimWorld, grounded observations are not reliably converted into feasible action sequences. DualWorld-VQA further confirms that perception and topology understanding do not necessarily translate into constrained planning. Together, these results identify the central challenge as composing symbolic or grounded evidence into globally feasible and efficient multi-goal plans. These findings establish DualWorldBench as a challenging testbed for agents with tighter perception--reasoning--planning integration. All datasets and code are publicly available at our project website https://dualworld.netlify.app/.

</details>

---

### [[20_Research/Papers/具身智能/DiMuRe_Diagnosis-Guided_Multilevel_Recovery_for_Robotic_Task_Execution|DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution]]

![[assets/2611.04226_figure.png|800]]

- **arXiv**: [2611.04226](https://arxiv.org/abs/2611.04226)
- **PDF**: https://arxiv.org/pdf/2611.04226
- **详细分析**: [[20_Research/Papers/具身智能/DiMuRe_Diagnosis-Guided_Multilevel_Recovery_for_Robotic_Task_Execution|DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution]]
- **作者**: Renkai Yi, Yuwei Wu, Haoyu Zhang, Penghao Dai, Zhi Gao, Jin Chen, Che Sun
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.2，大模型 0.5，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GraspVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Disturbances can invalidate the conditions required by a robot's next action even when much of its task program remains useful. A recovery system must therefore choose a response suited to the current state. We present DiMuRe (diagnosis-guided multilevel recovery), a framework for robot-use agents that uses phase-specific evidence and method preconditions to select program reuse or predefined recovery skills, including bounded vision-language-action (VLA) grasping. After the original program exits, a multimodal large language model (MLLM) can generate corrective code from images and execution feedback. Local verification checks the outcome of each recovery attempt. We also introduce LIBERO-Disturb, a benchmark for robustness and recovery under mid-execution disturbances, supporting program-based agents and VLA policies. On 801 scheduled disturbed Encore development cases, Local DiMuRe (program reuse and recovery skills) achieves 77.65% complete-task success, compared with 58.68% for the original program under the same physical-step allowance. Full DiMuRe achieves 81.90% with terminal replanning, an additional step allowance, and early handoff. Local DiMuRe also uses fewer physical steps per scheduled episode than the original program.

</details>

---

### [[20_Research/Papers/大模型/AlgoPilot_Cross-Paradigm_Reasoning_in_Language_Models_via_Strategy_Selection_and_Guidance|AlgoPilot: Cross-Paradigm Reasoning in Language Models via Strategy Selection and Guidance]]

![[assets/2611.04079_figure.png|800]]

- **arXiv**: [2611.04079](https://arxiv.org/abs/2611.04079)
- **PDF**: https://arxiv.org/pdf/2611.04079
- **详细分析**: [[20_Research/Papers/大模型/AlgoPilot_Cross-Paradigm_Reasoning_in_Language_Models_via_Strategy_Selection_and_Guidance|AlgoPilot: Cross-Paradigm Reasoning in Language Models via Strategy Selection and Guidance]]
- **作者**: Yilun Hao, Ruixiao Yang, Hudson Hilal, Yongchao Chen, Kaizhi Qian, Yada Zhu, Yang Zhang, Chuchu Fan
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.87（加权：大模型 0.35，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《AlgoPilot: Cross-Paradigm Reasoning in Language Models via Strategy Selection and Guidance》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world problems span diverse domains, including program synthesis, symbolic reasoning, planning, and optimization, and often require fundamentally different solution paradigms. A central challenge for LLM-based reasoning is twofold: identifying an appropriate problem-solving approach and formulating it correctly. In this paper, we propose AlgoPilot, a cross-paradigm reasoning framework that enables adaptive selection of the solving approaches and structured problem formulation prior to execution. The AlgoPilot framework contains three components: 1) a SteerLM, trained via supervised fine-tuning (SFT) and reinforcement learning (RL), that adaptively selects the solving strategy (paradigm and modes) based on input problems, 2) the corresponding expert GuideLM, trained via SFT, that generates structured formulation guidance tailored to the selected strategy, and 3) an ExecutionLM that generates solutions conditioned on both the selected strategy and its formulation. Unlike prompting-based methods that rely on fixed reasoning templates, our approach learns to adaptively choose and structure problem-solving strategies based on the input. We build AlgoPilot on Qwen3-8B and evaluate across 5 problem categories and 13 benchmarks with 66 unique domains, comparing against both the latest similarly scaled small models and large LLMs. AlgoPilot significantly improves average accuracy for the same model from 38.4% to 72.9%, outperforming the best large LLM prompting baseline GLM-5 by 11.7%. Ablation studies confirm the effectiveness of each component. Notably, we show that the learned steering and formulation modules can transfer across execution models, suggesting their potential to improve other LLMs. Project page: https://sites.google.com/view/algopilot.

</details>

---

### [[20_Research/Papers/机器人/A_Practical_Causal_Framework_for_Autonomous_Mobile_Robots_From_Simulation_to_Real-World_Human_Environments|A Practical Causal Framework for Autonomous Mobile Robots: From Simulation to Real-World Human Environments]]

![[assets/2611.04027_figure.png|800]]

- **arXiv**: [2611.04027](https://arxiv.org/abs/2611.04027)
- **PDF**: https://arxiv.org/pdf/2611.04027
- **详细分析**: [[20_Research/Papers/机器人/A_Practical_Causal_Framework_for_Autonomous_Mobile_Robots_From_Simulation_to_Real-World_Human_Environments|A Practical Causal Framework for Autonomous Mobile Robots: From Simulation to Real-World Human Environments]]
- **作者**: Luca Castri, Gloria Beraldo, Nicola Bellotto
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Practical Causal Framework for Autonomous Mobile Robots: From Simulation to Real-World Human Environments》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Causal inference has emerged as a powerful paradigm enabling robots to make safe, efficient decisions by reasoning about the ``why'' behind events. However, its real-world application is hindered by the difficulty of collecting causal data, especially in human-populated environments where training takes time, while users expect immediate operation. To this end, we tackle the challenge of transferring simulation-learnt causal relations to the real world with minimal effort. While retaining the invariant high-level causal structure, we empirically demonstrate the system adapts efficiently to real-world situations by updating only the causal model parameters with a limited set of new observations. Our results show that the parameter update enables rapid sim-to-real transfer. The framework runs efficiently onboard of a mobile robot and significantly outperforms a non-causal baselines navigating successfully and safely in complex human-shared scenarios.

</details>

---

### [[20_Research/Papers/具身智能/Controlling_Action-Head_Co-Adaptation_to_VLM_Representation_Anisotropy|Controlling Action-Head Co-Adaptation to VLM Representation Anisotropy]]

![[assets/2611.04006_figure.png|800]]

- **arXiv**: [2611.04006](https://arxiv.org/abs/2611.04006)
- **PDF**: https://arxiv.org/pdf/2611.04006
- **详细分析**: [[20_Research/Papers/具身智能/Controlling_Action-Head_Co-Adaptation_to_VLM_Representation_Anisotropy|Controlling Action-Head Co-Adaptation to VLM Representation Anisotropy]]
- **作者**: Ruijie Zhang, Jiayin Zheng, Yequan Zhao, Liyan Tan, Ziyue Liu, Zhengyang Wang, Kunpeng Song, Nathan Zhao, Jian Yao, Yin Zhang, Zheng Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 世界模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.6，世界模型 0.2）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Controlling Action-Head Co-Adaptation to VLM Representation Anisotropy》归入 大模型、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ResNet, StarVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern learning systems increasingly combine pretrained models with downstream heads. Despite the growing importance of such modular designs, how the downstream model co-adapts to the geometry of pretrained representations remains relatively underexplored. We study this problem through vision-language-action models (VLAs), where a pretrained vision-language model (VLM) conditions an action model for control. We find that the action model progressively concentrates its sensitivity on high-variance dimensions of the VLM outputs. Through controlled experiments across different backbone-head models, we further show that counteracting this sensitivity concentration can be beneficial under representation--task mismatch settings. Motivated by these observations, we introduce \emph{Adaptive Interface Equalizer} (AdaIE), a parameter-free mechanism that reweights pretrained representations according to the evolving downstream sensitivity during training. AdaIE improves VLA success rates on simulation benchmarks, with gains of up to $+5.28$ percentage points (pp) on RoboCasa-GR1 and $+1.68$ pp on RoboTwin 2.0, and achieves an average gain of $+19$ pp across five real-world manipulation tasks. It further generalizes to diffusion policies and world models, improving downstream performance in both settings. Our results highlight interface co-adaptation as an important optimization problem when coupling pretrained representations with downstream models.

</details>

---

### [[20_Research/Papers/大模型/Measure_Before_You_Repair_An_Explainable_Agent_for_Blind_Restoration_of_Multi-Artifact_3-D_MRI|Measure Before You Repair: An Explainable Agent for Blind Restoration of Multi-Artifact 3-D MRI]]

![[assets/2611.03996_figure.png|800]]

- **arXiv**: [2611.03996](https://arxiv.org/abs/2611.03996)
- **PDF**: https://arxiv.org/pdf/2611.03996
- **详细分析**: [[20_Research/Papers/大模型/Measure_Before_You_Repair_An_Explainable_Agent_for_Blind_Restoration_of_Multi-Artifact_3-D_MRI|Measure Before You Repair: An Explainable Agent for Blind Restoration of Multi-Artifact 3-D MRI]]
- **作者**: Necati Sefercioglu, Mehmet Ozan Unal, Metin Ertas, Altan Cakir, Isa Yildirim
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Measure Before You Repair: An Explainable Agent for Blind Restoration of Multi-Artifact 3-D MRI》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRUNet, MMRQA, MRI-AgentNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A brain MRI scan can carry an unknown mix of artifacts, so restoration has to be blind, yet most deep-learning methods are built to correct one known artifact. We present Dx-Rx, an agent in which a multimodal large language model (MLLM) measures suspected artifacts before it repairs them. To our knowledge, it is the first agent to restore whole 3-D MRI volumes, whereas earlier MRI agents restore 2-D slices. In a loop, it looks at slices of the 3-D volume, calls five diagnostic tools (noise, spike, ghosting, bias field, motion) and four restoration tools in any order it chooses, checks each repair, can return to any earlier version to change the order, and ends with a radiology-style report of its diagnostic reasons, the repairs it applied and their results. We simulated up to five artifacts on 148 whole 3-D T1-weighted volumes, at levels calibrated to radiologists' grades of real scans. An MLLM that only looked at the image, as earlier MRI agents do, removed at most 19.7 % of the artifact error. With the best of five MLLMs, Dx-Rx removed a mean 64.5 %, nearly matching the 64.6 % of the same tools given the ground-truth artifacts, which are never known for a clinical scan. With all five models, it made no volume worse and was on par with or better than an expert rule-based pipeline built from the same tools (62.3 %). Code and demo are public at https://itu-biai.github.io/measure-before-you-repair.

</details>

---

### [[20_Research/Papers/大模型/Measuring_Model-Specific_Alignment_Drift_in_LLM-Based_Opinion_Dynamics|Measuring Model-Specific Alignment Drift in LLM-Based Opinion Dynamics]]

![[assets/2611.03980_first_page.png|800]]

- **arXiv**: [2611.03980](https://arxiv.org/abs/2611.03980)
- **PDF**: https://arxiv.org/pdf/2611.03980
- **详细分析**: [[20_Research/Papers/大模型/Measuring_Model-Specific_Alignment_Drift_in_LLM-Based_Opinion_Dynamics|Measuring Model-Specific Alignment Drift in LLM-Based Opinion Dynamics]]
- **作者**: Nataša Djurdjevac Conrad, Sebastian Pokutta, Christof Schütte
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型
- **相关性评分**: 1.0（加权：大模型 0.8，世界模型 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Measuring Model-Specific Alignment Drift in LLM-Based Opinion Dynamics》归入 大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly used as synthetic participants in opinion-dynamics experiments, often assuming that an agent's behaviour is fully determined by its prompt. We test this assumption with a framework in which LLM agents discuss a contested policy issue over repeated rounds while their stance is quantified by a fixed psychometric instrument independent of any dynamics model. Across six LLMs, committed personas are intrinsically stable: in each of the five models tested without peer input, every agent keeps its assigned side for 20 rounds. The observed loss of alignment under discussion is therefore interaction-induced, we call it alignment drift, and model-specific: gpt-4.1 keeps opinion clusters apart, claude-sonnet-5 holds them partially, and gpt-5.6-sol and claude-opus-5 abandon them. Under selective attention, one LLM maintains separated opinion clusters under stance-homophilous attention. Qualitative profiles persist at doubled population and horizon and on a second issue. Such heterogeneity makes the LLM choice a first-class validity variable for social simulation.

</details>

---

### [[20_Research/Papers/具身智能/RoboScope_Kit_Unified_Interfaces_for_Fast_and_Scalable_Embodied-AI_Evaluation|RoboScope Kit: Unified Interfaces for Fast and Scalable Embodied-AI Evaluation]]

![[assets/2611.03850_figure.png|800]]

- **arXiv**: [2611.03850](https://arxiv.org/abs/2611.03850)
- **PDF**: https://arxiv.org/pdf/2611.03850
- **详细分析**: [[20_Research/Papers/具身智能/RoboScope_Kit_Unified_Interfaces_for_Fast_and_Scalable_Embodied-AI_Evaluation|RoboScope Kit: Unified Interfaces for Fast and Scalable Embodied-AI Evaluation]]
- **作者**: Deng-Ke Wu, Yifan Jin, Yida Yang, Lei Qian, Zhaoye Zhou, Hongru Zhang, Kai Ye, Shuyuan Hu, Yiran Mao, Zewei Ye, Bo Zhao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《RoboScope Kit: Unified Interfaces for Fast and Scalable Embodied-AI Evaluation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：StarVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation benchmarks are the standard way to compare robot policies, but each benchmark brings its own evaluator, observation layout, and action convention, and evaluation is slow: 500 RoboTwin Easy episodes with one simulator and one model on one GPU take 359.7 minutes. Profiling the official StarVLA evaluator shows that simulation occupies CPU cores while the GPU averages 14.3% utilization. RoboScope Kit wraps each model once in a Python class called a Policy, and each benchmark once in an adapter around the benchmark's own evaluator, so the benchmark's rules and scoring stay unchanged. Scheduling runs simulator workers and Policy replicas as separate pools, sizes both from measured probes, and shards work deterministically across GPU instances; runtime optimization renders only the observations an action-chunk Policy reads. Adapters cover six benchmark families. On LIBERO-Long with a StarVLA checkpoint on one 48 GiB RTX 4090, the concurrency search selects twelve simulator workers sharing three Policy replicas, which evaluate 500 episodes 4.45$\times$ faster than the official StarVLA evaluation with equivalent success rates, 2.78$\times$ faster than RLinf, and 1.52$\times$ faster than vla-eval at its tuned configuration. With CUDA MPS, which lets the replicas run their kernels concurrently, the search selects sixteen workers sharing four replicas, 6.16$\times$ faster than StarVLA, 3.85$\times$ faster than RLinf, and 2.10$\times$ faster than vla-eval. On RoboTwin Easy, four GPUs with chunk-boundary observation complete the 500 episodes in 14.4 minutes, 25.04$\times$ faster than the single-GPU baseline, with identical success outcomes and terminal steps.

</details>

---

### [[20_Research/Papers/具身智能/AIRoA-0_Long-Horizon,_Precise,_Cross-Embodiment_Manipulation_from_Handheld_Data|AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data]]

![[assets/2611.03815_first_page.png|800]]

- **arXiv**: [2611.03815](https://arxiv.org/abs/2611.03815)
- **PDF**: https://arxiv.org/pdf/2611.03815
- **详细分析**: [[20_Research/Papers/具身智能/AIRoA-0_Long-Horizon,_Precise,_Cross-Embodiment_Manipulation_from_Handheld_Data|AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data]]
- **作者**: Yueh-Hua Wu, Kei Ota, Hanlong Li, Hayata Yuasa, Jason Wang, Kengo Ikeuchi, Kensuke Chiyoma, Makoto Sugiura, Masafumi Takahashi, Masatoshi Tateno, Naoaki Kanazawa, Nicola Scianca...
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 1.62（加权：具身智能 0.6，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AIRoA-0 (A-0) is a bimanual manipulation system learned from 16,151 hours of handheld demonstrations, with no robot data collected at any stage. The demonstrations are recorded with YUBI, our open-source handheld gripper, which lets people record manipulation data anywhere with no robot present. From a single instruction, A-0 sorts more than a dozen small parts into their numbered cells and changes the mop pads and brush of a robot vacuum; among other tasks, it unzips a pencil case and folds a towel. It performs these tasks using only a camera on each wrist, with no head or scene camera, at a site where none of its training data was recorded. Across the ten tasks of our evaluation, it averages a success rate of 78%, against 27% for the strongest of four other vision-language-action models post-trained on the same task demonstrations. We collect no teleoperation data and use no reinforcement learning or on-robot corrections, and the robot appears only at test time. The system learns which regions of each wrist view matter for the task, predicts the stage the task has reached, and decodes actions as a continuous stream. A-0 is embodiment-agnostic: it runs on robots that mount the YUBI gripper, such as a bimanual Franka, TX-G2, OpenArm and UR. We are releasing the dataset, to our knowledge the largest open dataset of handheld-gripper demonstrations with task and subtask instructions, together with the pre-trained weights and the post-training recipe. Videos of A-0 on every task are on the project page, https://a-0.airoa.io. Anyone can build the gripper, record a task of their own and post-train the model on it in under four hours on a single node of eight H200 GPUs.

</details>

---

### [[20_Research/Papers/具身智能/VagueBench_Benchmarking_the_Robustness_of_Embodied_Agents_on_Ambient_Context_Illusions|VagueBench: Benchmarking the Robustness of Embodied Agents on Ambient Context Illusions]]

![[assets/2611.03765_figure.png|800]]

- **arXiv**: [2611.03765](https://arxiv.org/abs/2611.03765)
- **PDF**: https://arxiv.org/pdf/2611.03765
- **详细分析**: [[20_Research/Papers/具身智能/VagueBench_Benchmarking_the_Robustness_of_Embodied_Agents_on_Ambient_Context_Illusions|VagueBench: Benchmarking the Robustness of Embodied Agents on Ambient Context Illusions]]
- **作者**: Yang Qu, Qiang Fu, Zonghao Ying, Jiayi Zhao, Yaoyuan Zhang, Jinyang Guo, Jian Yang, Aishan Liu, Yingxun Wang, Xianglong Liu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，大模型 0.5，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《VagueBench: Benchmarking the Robustness of Embodied Agents on Ambient Context Illusions》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld, AgentNoiseBench, EmbodiedBench, ReliabilityBench, SafeAgentBench, VagueBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied agents are increasingly deployed in open-world environments, yet current robustness evaluations remain biased toward hazardous instructions and jailbreak vulnerabilities. A more fundamental issue is largely overlooked: agents are rarely tested under semantically sufficient but contextually minimal instructions (i.e., common in real-world human communication), where auxiliary contextual cues are absent. For the first, we identify a novel phenomenon termed Ambient Context Illusion, where agents fail to execute tasks correctly when non-essential contextual details are omitted, despite unchanged task semantics. To systematically study this, we establish VagueBench, a benchmark built upon the AI2-THOR interactive simulation environment for the evaluation of context dependency in embodied agents. We systematically consider key semantic components of instructions (entities, procedures, constraints, and prior knowledge) and derive a unified taxonomy with four categories and nine subtypes to reduce auxiliary information. VagueBench contains 1,303 instruction pairs across diverse indoor environments, constructed via a human-agent co-generation framework that integrates semantic redundancy estimation, taxonomy-guided transformation, and rigorous semantic-invariance verification. Through extensive evaluation on 6 state-of-the-art embodied agents, we observe significant degradation on VagueBench in both task performance and executability (relatively -19.65% in task success rate and relatively +54.10% in empty plan rate) revealing a strong reliance on auxiliary linguistic signals rather than core task semantics. Furthermore, we demonstrate that this phenomenon persists in real-world robotic systems, where it can lead to incorrect decisions and potential safety risks.

</details>

---

### [[20_Research/Papers/大模型/EvoMemState_Evolving_Memory_State_for_Personal_Agents|EvoMemState: Evolving Memory State for Personal Agents]]

![[assets/2611.03743_figure.png|800]]

- **arXiv**: [2611.03743](https://arxiv.org/abs/2611.03743)
- **PDF**: https://arxiv.org/pdf/2611.03743
- **详细分析**: [[20_Research/Papers/大模型/EvoMemState_Evolving_Memory_State_for_Personal_Agents|EvoMemState: Evolving Memory State for Personal Agents]]
- **作者**: Zhishang Xiang, Yunbo Tang, Zhongqiao Liu, Junkai Chen, Zerui Chen, Qingguo Hu, Yuxuan Zhang, William Grant, Qinggang Zhang, Jinsong Su
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.0（加权：大模型 0.8，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《EvoMemState: Evolving Memory State for Personal Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MemSyco-Bench, MemTrapBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term memory enables large language model (LLM) agents to provide continuous personalized assistance by retaining user information across interactions. Existing systems support this process through fact extraction, organization, updating, and retrieval, but largely maintain memories as independent facts. This fact-centric paradigm may overlook how new facts update, constrain, or conflict with earlier ones, while leaving their applicability, role, and priority for the current request implicit. In this paper, we introduce EvoMemState, a state-centric framework that augments persistent facts with two complementary states: Relational States that capture how facts remain valid and relate to one another as memory evolves, and a Reasoning State that determines how these facts should be applied to the current request. Specifically, EvoMemState consists of three key components: (i) Ontology-Guided Memory State Induction extracts Persistent Facts and constructs Relational States that maintain their validity, scope, and evolving relations. (ii) RL-Based State Evolution internalizes memory-use experience into a policy through reinforcement learning to generate a request-specific Reasoning State. (iii) State-Aware Reasoning then combines the relevant facts with their Relational States and the generated Reasoning State to guide the personal agent. Extensive experiments on long-term dialogue and memory-use benchmarks demonstrate consistent improvements over existing memory systems in retrieval completeness and memory-grounded response accuracy. Our code and implementation details are available at https://github.com/XMUDeepLIT/EvoMemState.git.

</details>

---

### [[20_Research/Papers/大模型/Behavioral_Prior_Elicitation_via_LLM_for_Heterogeneous-Agent_Bitcoin_Flash-Crash_Simulation|Behavioral Prior Elicitation via LLM for Heterogeneous-Agent Bitcoin Flash-Crash Simulation]]

![[assets/2611.03660_figure.png|800]]

- **arXiv**: [2611.03660](https://arxiv.org/abs/2611.03660)
- **PDF**: https://arxiv.org/pdf/2611.03660
- **详细分析**: [[20_Research/Papers/大模型/Behavioral_Prior_Elicitation_via_LLM_for_Heterogeneous-Agent_Bitcoin_Flash-Crash_Simulation|Behavioral Prior Elicitation via LLM for Heterogeneous-Agent Bitcoin Flash-Crash Simulation]]
- **作者**: Tran Phuong Linh Pham, Thi Minh Phuong Ngo, Phuong Thao Nguyen, Quang Minh Nguyen, Thai Hoa Ngo, Trong Nghia Nguyen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Behavioral Prior Elicitation via LLM for Heterogeneous-Agent Bitcoin Flash-Crash Simulation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bitcoin perpetual futures trade continuously with shallow liquidity and high price impact, making them prone to millisecond-scale flash crashes. Agent-based limit order book simulators are a natural tool for studying such events, but their behavioral parameters are usually hand-crafted or require full order book histories that are rarely available at scale. We propose a four-stage pipeline that constructs a reproducible 100 ms BTCUSDT flash-crash event panel from 66 detected events, elicits behavioral priors for four agent archetypes using an offline large language model conditioned on empirical microstructure anchors, instantiates a heterogeneous limit order book simulator with the validated priors, and applies causal discovery plus counterfactual analysis to the resulting synthetic panel. Across 500 simulation runs, LLM-elicited priors produce a crash rate of 0.176 versus 0.008 under uninformative uniform priors and generate heav- ier return tails. In the frozen counterfactual analysis, reducing leverage amplification by one within-sample standard deviation lowers the predicted crash rate from 0.176 to 0.136, whereas reducing directional pressure yields only a marginal change. These find- ings suggest that empirically anchored LLM elicitation can improve simulator fidelity and help identify plausible crash-amplification mechanisms in a controlled synthetic environment

</details>

---
