# cs.AI | Artificial Intelligence | 2026-11-26

#arxiv #ComputerScience

**论文数**: 29

### [[20_Research/Papers/具身智能/RePace_Reasoning_about_Demonstration_Speedup_for_Faster_Vision-Language-Action_Policies|RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies]]

![[assets/2611.34864_figure.png|800]]

- **arXiv**: [2611.34864](https://arxiv.org/abs/2611.34864)
- **PDF**: https://arxiv.org/pdf/2611.34864
- **详细分析**: [[20_Research/Papers/具身智能/RePace_Reasoning_about_Demonstration_Speedup_for_Faster_Vision-Language-Action_Policies|RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies]]
- **作者**: Insup Lee, Hojin Jeon, Sunguk Shin, Seoungbin Bae, Taekwan Kim, Jinwoo Shin, Dongsu Han
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.8，大模型 0.1，机器人 0.3）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《RePace: Reasoning about Demonstration Speedup for Faster Vision-Language-Action Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World, TempoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Since vision-language-action (VLA) policies can inherit the slow pace of human demonstrations, accelerating these demonstrations before fine-tuning can lead to faster VLA policies without an additional speed-selection module at deployment. Several offline speedup methods have focused on identifying segments that require less precision and assigning predefined speedup factors to the segments. However, even within a single segment, a speedup factor suitable for steady motion may be too high when precise alignment is required. To this end, this paper presents RePace, an offline reasoning framework that determines how much to accelerate each part of a demonstration. For the same recorded movement, RePace measures how much each candidate speedup factor shortens the sequence and compares the resulting observation-action pairs used for training. Given the task instruction, a pretrained language model uses the visual context and original motion of successive windows to interpret these candidate retiming effects and select a speedup profile for the complete episode. Experimental results demonstrate that RePace outperforms the baselines in overall task execution efficiency on both LIBERO and RoboCasa-Kitchen. On all three tasks with a gripper-equipped Franka Research 3 arm, RePace matches or exceeds the acceleration baselines in success rate and completes successful trials faster.

</details>

---

### [[20_Research/Papers/强化学习/When_Every_Rollout_Fails_Splicing_Learner-Conditioned_Options_into_Long-Horizon_Agent_RL|When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL]]

![[assets/2611.34777_figure.png|800]]

- **arXiv**: [2611.34777](https://arxiv.org/abs/2611.34777)
- **PDF**: https://arxiv.org/pdf/2611.34777
- **详细分析**: [[20_Research/Papers/强化学习/When_Every_Rollout_Fails_Splicing_Learner-Conditioned_Options_into_Long-Horizon_Agent_RL|When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL]]
- **作者**: Haowen Hou, Yicheng Liu, Zhen Huang, Jiaqi Wang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.27（加权：大模型 0.55，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Group-based reinforcement learning with verifiable rewards often yields all-fail groups on long-horizon agent tasks: every sampled trajectory receives zero reward, leaving group-relative methods without a reward-based policy gradient. A common remedy supplies complete solutions from a stronger model, but full trajectories are expensive and expose the learner to long off-policy histories. We introduce SPLICE, which constructs local training targets from failed current-policy trajectories online. For each all-fail group, a proposal model selects a splice point in a current-policy trajectory and generates several bounded options from that point. We estimate each option's value using repeated current-policy continuations, convert positive estimates into a return-weighted local target, and fit the current policy on the options. We evaluate SPLICE across two policy families on two long-horizon agent tasks, Software Engineering with SWE-bench Verified and Deep Research with BrowseComp-Plus. SPLICE outperforms GRPO and full-trajectory guidance baselines in all four settings, improving over GRPO by 2.8--9.8 percentage points. On initially failed SWE tasks, it raises GRPO's graduation rate by 10.8 percentage points. Further experiments show that SPLICE improves performance while reducing costly proposal-model computation.

</details>

---

### [[20_Research/Papers/具身智能/How_Well_Do_Vision-Language_Scene_Graphs_Serve_as_Memory_for_Embodied_Question_Answering|How Well Do Vision-Language Scene Graphs Serve as Memory for Embodied Question Answering?]]

![[assets/2611.34745_figure.png|800]]

- **arXiv**: [2611.34745](https://arxiv.org/abs/2611.34745)
- **PDF**: https://arxiv.org/pdf/2611.34745
- **详细分析**: [[20_Research/Papers/具身智能/How_Well_Do_Vision-Language_Scene_Graphs_Serve_as_Memory_for_Embodied_Question_Answering|How Well Do Vision-Language Scene Graphs Serve as Memory for Embodied Question Answering?]]
- **作者**: Divyansh Pandey, Shubh Garg, Vedant Khandelwal, Niyati Rawal, Amit Sheth
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI, ComputerVision

#### 研究背景与动机

《How Well Do Vision-Language Scene Graphs Serve as Memory for Embodied Question Answering?》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ScanNet, VSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied QA needs memory, but answer accuracy mixes retained evidence, reading errors and question priors. For a simulated multi-room scene-graph pipeline we define answerability: the fraction of questions a fixed rule-based reader answers correctly from the graph alone. The baseline recovers 24.1% of visible object types and its room labels flicker. Four targeted repairs double recall, raise answerability from 27.2% to 37.4%, and improve retrained QA from 71.4% to 75.9%, yet better object F1 can lower answerability. A question-type prior beats this reader on every predicted graph. In one real-video test, graph memory lowers accuracy. These exploratory findings favour scoring retained evidence alongside accuracy.

</details>

---

### [[20_Research/Papers/强化学习/Maco-RL_Scaling_Agent_Capabilities_with_Mixed-Task_Reinforcement_Learning|Maco-RL: Scaling Agent Capabilities with Mixed-Task Reinforcement Learning]]

![[assets/2611.34703_figure.png|800]]

- **arXiv**: [2611.34703](https://arxiv.org/abs/2611.34703)
- **PDF**: https://arxiv.org/pdf/2611.34703
- **详细分析**: [[20_Research/Papers/强化学习/Maco-RL_Scaling_Agent_Capabilities_with_Mixed-Task_Reinforcement_Learning|Maco-RL: Scaling Agent Capabilities with Mixed-Task Reinforcement Learning]]
- **作者**: Jiacheng Zhang, Qixing Zhou, Haiyang Wang, Qipeng Gu, Shuzhe Wu, Feiyang Pan, Lue Fan, Dandan Tu, Zhaoxiang Zhang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Maco-RL: Scaling Agent Capabilities with Mixed-Task Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ACuRL, AgentGym, AgentRL, Claw-Eval, CodeWorld, ComputerRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mixed-task reinforcement learning (MixRL) directly trains a unified policy across domains to continually expand agent capabilities without training separate specialists or requiring an extra distillation stage. Despite its appeal, scaling MixRL poses significant challenges in achieving stable and efficient mixed-task learning, effectively allocating rollout compute, and supporting continual domain expansion. To address these challenges, we propose Maco-RL, an approach that effectively scales MixRL. Specifically, Maco-RL employs a quota-based scheduler for asynchronous rollouts across multiple task domains, thereby stabilizing training by balancing gradient contributions and mitigating off-policy effects. Along an orthogonal axis, Maco-RL further introduces Tri-Buffer Sampling (TBS) to allocate compute among samples with varying levels of mastery, promoting sustained frontier exploration while preserving acquired capabilities. Experiments on five benchmarks show Maco-RL raises Qwen3.5-27B's overall score from 43.6 to 54.2 and then to 60.1 with continual expansion, reaching the frontier held by Qwen3.8-27B, which is further pushed outward by +5.7. Maco-RL also outperforms single-task RL with less compute for policy updates. These results support MixRL as a practical and compute-efficient post-training approach with substantial potential to strengthen general agent capabilities.

</details>

---

### [[20_Research/Papers/具身智能/A_Failure-Driven_Data_Flywheel_for_Post-Training_Vision-Language-Action_Models|A Failure-Driven Data Flywheel for Post-Training Vision-Language-Action Models]]

![[assets/2611.34698_figure.png|800]]

- **arXiv**: [2611.34698](https://arxiv.org/abs/2611.34698)
- **PDF**: https://arxiv.org/pdf/2611.34698
- **详细分析**: [[20_Research/Papers/具身智能/A_Failure-Driven_Data_Flywheel_for_Post-Training_Vision-Language-Action_Models|A Failure-Driven Data Flywheel for Post-Training Vision-Language-Action Models]]
- **作者**: Yuhao Luo, Zihao Sheng, Zilin Huang, Zhengyang Wan, Boyue Wang, Ruolin Yang, Shuai Wang, Sikai Chen
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal

#### 研究背景与动机

《A Failure-Driven Data Flywheel for Post-Training Vision-Language-Action Models》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AutoVLA, FIRE-VLA, TakeVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained vision-language-action (VLA) models rarely satisfy all behavioral requirements of a new platform, and teams without a large deployed fleet lack the data to address the resulting failures. We propose a failure-driven data flywheel for post-training such models. It constructs target scenarios absent from the available data by inserting task-relevant entities into reconstructed real-world scenes, and evaluates the model against each behavioral requirement of the target task. Failure rates form a failure map across task conditions and difficulty levels, which is re-evaluated after each round and assigns larger data generation quotas to conditions where the model still fails. We instantiate the framework in autonomous driving for occluded-pedestrian emergence and yielding at stop-sign-controlled intersections, and evaluate it on two VLA models and one non-VLA planner in simulation and on a real vehicle. For occluded-pedestrian emergence, five rounds of post-training improve the critical-phase collision-free rate on the sealed test set from 0.261 to 0.579 for AutoVLA and from 0.390 to 0.765 for ReCogDrive, while the unnecessary braking rate in paired control scenarios never exceeds 0.013. On a full-scale vehicle without real-world training, post-trained ReCogDrive achieves 4 of 5 safe passages, versus 1 of 5 for the base model. Fine-grained evaluation reveals a pattern obscured by the collision-free rate alone: both VLA models learn anticipatory deceleration before reaching the occluding vehicle, while braking after pedestrian emergence remains limited. For stop-sign yielding, the stop-before-line rate rises from 0.100 to 0.897 for AutoVLA and from 0.000 to 0.667 for ReCogDrive. With sequential training from the pedestrian-capability models, it reaches 0.599 and 0.358, respectively, while the pedestrian collision-free rate decreases by at most 0.032.

</details>

---

### [[20_Research/Papers/具身智能/RoboEvo$^2$_Recursive_Robot_Self-Improvement_via_Harness-Policy_Co-Evolution|RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution]]

![[assets/2611.34675_figure.png|800]]

- **arXiv**: [2611.34675](https://arxiv.org/abs/2611.34675)
- **PDF**: https://arxiv.org/pdf/2611.34675
- **详细分析**: [[20_Research/Papers/具身智能/RoboEvo$^2$_Recursive_Robot_Self-Improvement_via_Harness-Policy_Co-Evolution|RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution]]
- **作者**: Chenzhi Liu, Jiehong Lin, Wei Huang, Xuzhao Huang, Haoyuan Li, Yang Zhang, Junchao Huang, Chenyeyang Cai, Bo Wang, Kazuhiro Kosuge, Zhongrui Wang, Xiaojuan Qi
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.9（加权：具身智能 0.6，大模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CRL-VLA, PackNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots should adapt to unfamiliar environments and acquire new skills through interaction, then execute those skills efficiently with practice. Vision-language-action policies provide efficient control, but often need additional human demonstrations to handle unfamiliar settings; reasoning agents can discover solutions using broad prior knowledge and robot-control APIs, but repeated deliberation and repair are costly. Inspired by human learning through reasoning and practice, we propose RoboEvo$^2$, a framework for recursive harness-policy co-evolution. In Policy-to-Harness (P2H) evolution, policy failures guide a coding agent to search complementary Code, Code+ICL, and Code+Policy routes, consolidating verified solutions into reusable skills, routing strategies, and experience memory. In Harness-to-Policy (H2P) evolution, verified trajectories provide supervised training, while Counterfactual Preference Distillation (CPD) teaches the policy to favor successful corrections over failures from the same starting state. The improved policy provides stronger motor skills for subsequent search, while its remaining failures redirect harness evolution, closing the reciprocal loop. Through recursive co-evolution without additional human demonstrations, RoboEvo$^2$ improves standalone success from 11.0% to 84.1% and hybrid success from 30.4% to 90.5% on LIBERO-PRO, with similar gains and reduced agentic costs on RoboTwin C2R. Further experiments demonstrate autonomous task acquisition, cross-embodiment harness transfer, and 95.0% hybrid success on the Unitree G1-D. Our models and code will be publicly released.

</details>

---

### [[20_Research/Papers/强化学习/DemoFoundry_Toward_Scalable_Photorealistic_Robot_Data_with_Coding_Agents_and_Generative_Rendering|DemoFoundry: Toward Scalable Photorealistic Robot Data with Coding Agents and Generative Rendering]]

![[assets/2611.34671_figure.png|800]]

- **arXiv**: [2611.34671](https://arxiv.org/abs/2611.34671)
- **PDF**: https://arxiv.org/pdf/2611.34671
- **详细分析**: [[20_Research/Papers/强化学习/DemoFoundry_Toward_Scalable_Photorealistic_Robot_Data_with_Coding_Agents_and_Generative_Rendering|DemoFoundry: Toward Scalable Photorealistic Robot Data with Coding Agents and Generative Rendering]]
- **作者**: Ruixiang Wang, Xinyue Yao, Xuanning Zhou, Yueci Deng, Yongyi Su, Kui Jia
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.5，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《DemoFoundry: Toward Scalable Photorealistic Robot Data with Coding Agents and Generative Rendering》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ComSim, DexSim, PointWorld, Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling robot learning requires demonstrations that combine realistic visual observations with reliable action supervision. Simulation-based synthesis faces a substantial visual gap relative to real environments, while video-only generation struggles to maintain physically consistent interactions and provide aligned action labels. We present DemoFoundry, an automated framework that couples coding agents with generative rendering to synthesize photorealistic and physically grounded robot demonstrations. Coding agents both construct aligned real--proxy video pairs from existing robot episodes to train a video renderer and write executable interaction programs to generate new demonstrations. Given a scene reference and task instruction, an agent reconstructs task-relevant geometry and writes a control program without requiring target-task human demonstrations. Program execution in a physics simulator produces proxy videos with aligned robot states and actions. The video renderer translates these proxy videos into scene-consistent, photorealistic observations, reducing the need for detailed appearance modeling in each scene. Automated task-execution checks select successful trajectories for rendering and policy learning. Experiments show improved visual quality and action--video consistency. Policies trained on the generated demonstrations outperform raw-simulation training and approach the performance of training on an equal number of real demonstrations.

</details>

---

### [[20_Research/Papers/大模型/Do_We_Still_Need_Reinforcement_Learning_When_We_Can_Read_the_World_Model|Do We Still Need Reinforcement Learning When We Can Read the World Model?]]

![[assets/2611.34656_figure.png|800]]

- **arXiv**: [2611.34656](https://arxiv.org/abs/2611.34656)
- **PDF**: https://arxiv.org/pdf/2611.34656
- **详细分析**: [[20_Research/Papers/大模型/Do_We_Still_Need_Reinforcement_Learning_When_We_Can_Read_the_World_Model|Do We Still Need Reinforcement Learning When We Can Read the World Model?]]
- **作者**: Mingchao Zhang, Miduo Cui, Kangze He, Yuanjun Li, Dapeng Li, Ce Zhang, Chuanchen Luo, Xue Yan, Mingzhe Xing, Zhumin Chen, Hangyu Mao, Bin Zhang...
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.52（加权：大模型 0.2，强化学习 1.16，世界模型 1.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Do We Still Need Reinforcement Learning When We Can Read the World Model?》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：D4RL, PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has achieved remarkable success in sequential decision-making, but learning effective policies often requires substantial interaction experience. Model-based reinforcement learning alleviates this dependence by leveraging world models, which are typically used to support planning or policy optimization. In this paper, we investigate an alternative paradigm in which autonomous LLM-based coding agents directly synthesize control policies by reasoning over readable world models. By examining environment source code, these agents translate environmental knowledge into executable decision rules and iteratively refine their policies using online feedback or offline data, without task-specific RL training. Experiments across diverse decision-making benchmarks show that synthesized policies match or outperform conventional RL methods while requiring substantially less experience. Further analyses reveal interpretable decision rules and how they evolve through feedback-driven refinement. Comparisons with policies generated without source code access and experiments under challenging conditions further demonstrate the benefits of readable world models. These findings suggest that direct policy synthesis can reduce reliance on trial and error, challenging the necessity of task-specific RL training.

</details>

---

### [[20_Research/Papers/具身智能/Motion_Beyond_Pixels_Learning_Future_Visual_Representations_for_Object-Centric_Dynamics|Motion Beyond Pixels: Learning Future Visual Representations for Object-Centric Dynamics]]

![[assets/2611.34644_figure.png|800]]

- **arXiv**: [2611.34644](https://arxiv.org/abs/2611.34644)
- **PDF**: https://arxiv.org/pdf/2611.34644
- **详细分析**: [[20_Research/Papers/具身智能/Motion_Beyond_Pixels_Learning_Future_Visual_Representations_for_Object-Centric_Dynamics|Motion Beyond Pixels: Learning Future Visual Representations for Object-Centric Dynamics]]
- **作者**: Chengzhi Zhao, Juelin Li, Zhennan Wang, Sheng Wang, Zhuoman Liu, Yuhao Lu, Jiongxu Chen, Haitang Feng, Yanjie Li, Lin Shao
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 1.3（加权：具身智能 0.6，世界模型 0.4，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《Motion Beyond Pixels: Learning Future Visual Representations for Object-Centric Dynamics》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：WorldFlowBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many embodied world models predict future states in latent spaces optimized for RGB reconstruction, which do not explicitly prioritize object-level semantics and geometry relevant to motion generation. We present MotionRep, a visual representation world model that jointly generates future DINO representations and 3D object flow, coupling semantic and geometric information with object-centric dynamics. To make high-dimensional DINO features amenable to generative modeling, we introduce DINO-VAE, which combines temporal and channel compression with latent regularization to produce compact latents while preserving semantic and geometric information. Conditioned on an initial observation, object query points, and a language instruction, a unified diffusion transformer predicts future visual representations and 3D object flow through joint attention. MotionRep employs asymmetric modality-specific noise schedules to keep the visual stream ahead of 3D object flow during joint denoising, allowing progressively refined future visual representations to guide flow generation. Experiments on simulated and real-world manipulation benchmarks demonstrate that MotionRep outperforms pixel-based baselines in 3D object flow accuracy and generalization to unseen scenes, while requiring only three denoising steps for inference. These results support predictive visual representations as an effective future-state space for object-centric dynamics modeling.

</details>

---

### [[20_Research/Papers/强化学习/LatentRL-QAS_Transfer_via_Latent_Reinforcement_Learning_for_Quantum_Architecture_Search|LatentRL-QAS: Transfer via Latent Reinforcement Learning for Quantum Architecture Search]]

![[assets/2611.34634_figure.png|800]]

- **arXiv**: [2611.34634](https://arxiv.org/abs/2611.34634)
- **PDF**: https://arxiv.org/pdf/2611.34634
- **详细分析**: [[20_Research/Papers/强化学习/LatentRL-QAS_Transfer_via_Latent_Reinforcement_Learning_for_Quantum_Architecture_Search|LatentRL-QAS: Transfer via Latent Reinforcement Learning for Quantum Architecture Search]]
- **作者**: Maria Ilektra Plakitsi, Sebastian Feld, Akash Kundu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《LatentRL-QAS: Transfer via Latent Reinforcement Learning for Quantum Architecture Search》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：LatentRL, TensorRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) emerges as a prominent approach to quantum architecture search (QAS), the automated design of quantum circuits. However, transferring what an agent has learned from one number of qubits to another is still weakly explored: the state, the action space and the neural network of a state-of-the-art RL-QAS agent all grow with the number of qubits, which makes transfer learning across qubit counts prohibitive. We make this transfer possible by introducing LatentRL-QAS, a latent space transfer and refresh framework for RL-based QAS. At its core, a circuit variational autoencoder encodes a circuit as one token per gate and maps circuits on any number of qubits into the same latent space. An RL agent navigates this space instead of adding gates, so its state, actions and network have the same size at every qubit count. The latent space is periodically refreshed with the agent's new discoveries and, for a larger system, grown from the solutions of the smaller one, so what is transferred is the representation of circuits, not network weights or past experience. To show transfer, we consider absolutely maximally entangled (AME) states, a resource for quantum error correction. LatentRL-QAS discovers the five- and six-qubit AME states without being shown them and prepares them in 89-99% of evaluation episodes, whereas the baseline RL-QAS fails to find them with the same budget, even with a network 10 to 17 times larger. LatentRL-QAS remains robust under depolarizing noise with single-qubit gate errors amplified 10x and two-qubit gate errors 5x compared with IBM quantum hardware. By decoupling the RL agent from the number of qubits, LatentRL-QAS lets quantum architecture search reuse circuit representations learned on smaller problems, providing a foundation for the transferable design of circuits across quantum optimization problems.

</details>

---

### [[20_Research/Papers/世界模型/Long-Horizon_Planning_with_Latent_World_Models_via_Graph_Anchors|Long-Horizon Planning with Latent World Models via Graph Anchors]]

![[assets/2611.34509_figure.png|800]]

- **arXiv**: [2611.34509](https://arxiv.org/abs/2611.34509)
- **PDF**: https://arxiv.org/pdf/2611.34509
- **详细分析**: [[20_Research/Papers/世界模型/Long-Horizon_Planning_with_Latent_World_Models_via_Graph_Anchors|Long-Horizon Planning with Latent World Models via Graph Anchors]]
- **作者**: Syed Nazmus Sakib, Abdul Monaf Chowdhury, Peizhen Li, Nafiul Haque, Chandak Chakma, Md Mehedi Hasan, Zehong Cao, Shifat E. Arman
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，世界模型 0.8，机器人 0.5）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Long-Horizon Planning with Latent World Models via Graph Anchors》归入 世界模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Meta-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models plan in a compact latent space by predicting the outcomes of actions. Their planners judge a plan by the latent distance between its predicted end state and the goal image. We show that this distance fails in two distinct ways. First, it loses directional signal a few steps from the goal, causing distant goals to fail. Second, it weighs the robot arm over the manipulated object, causing manipulation to fail at contact. We measure both failures directly on recorded data by asking whether a lower latent distance corresponds to true progress toward the goal. Across five environments, six visual representations (including raw pixels and V-JEPA 2), and nine Meta-World tasks, this ranking test cleanly separates the two failures, and the graph distance to a goal predicts where closed-loop planning breaks down. Both failures share a single remedy: replacing the distant goal with a nearby target that lies on a recorded trajectory. We realize this principle with Graph Anchors, a training-free planner for frozen latent world models. It builds a sparse graph once over the model's own training frames and aims each planning step at a node a few moves ahead along the shortest path to the goal, keeping paths on recorded transitions wherever contact matters. On goals up to 400 steps away, Graph Anchors raise LeWM's success from 13% to 85% on PointMaze-Medium, from 8% to 87% on PointMaze-Large, and from 5% to 71% on Push-T, where stronger search toward the goal fails and where prior training-free planners break down under missing step horizons, subsampling shortcuts, or fragmented contact.

</details>

---

### [[20_Research/Papers/大模型/vSFT_Learning_to_Verbally_Tune_Agents_at_Test_Time|vSFT: Learning to Verbally Tune Agents at Test Time]]

![[assets/2611.34440_figure.png|800]]

- **arXiv**: [2611.34440](https://arxiv.org/abs/2611.34440)
- **PDF**: https://arxiv.org/pdf/2611.34440
- **详细分析**: [[20_Research/Papers/大模型/vSFT_Learning_to_Verbally_Tune_Agents_at_Test_Time|vSFT: Learning to Verbally Tune Agents at Test Time]]
- **作者**: Qishuai Wen, Rui Chen, Haiwen Li, Zhiyuan Huang, Qiwen Gu, Bingjie Gao, Geng Li, Jing Tang, Xiangxiang Chu, Chun-Guang Li
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.85，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《vSFT: Learning to Verbally Tune Agents at Test Time》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, JitRL, MemRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents are increasingly improved via agentic reinforcement learning, which can be on-policy but suffers from expensive rollouts and sparse rewards, limiting its application at test time. In this paper, we present a verbally Supervised Fine-Tuning (vSFT) framework that enables the conjunction of dense feedback in natural language and weight updates at test time. Specifically, our vSFT forms a closed loop between an agent and a supervisor via a hypernetwork, in which the supervisor generates verbal supervision from the agent's failed trajectories, and the hypernetwork converts that supervision into low-rank weight updates to tune the agent. We validate that this test-time in-parameter evolving process outperforms both its in-context counterparts and prevalent reinforcement learning methods. In particular, our vSFT using Qwen3-4B outperforms GRPO and Reflexion by 8.7% and 13.9% in success rate on ALFWorld, and by 4.8% and 18.2% on WebShop, respectively. We believe that learning how to adapt a model, rather than an adapted model, offers a promising path towards more capable agents that improve themselves.

</details>

---

### [[20_Research/Papers/具身智能/CHASE_Curiosity-Guided_Skill_Acquisition_for_Embodied_Task_Execution|CHASE: Curiosity-Guided Skill Acquisition for Embodied Task Execution]]

![[assets/2611.34416_figure.png|800]]

- **arXiv**: [2611.34416](https://arxiv.org/abs/2611.34416)
- **PDF**: https://arxiv.org/pdf/2611.34416
- **详细分析**: [[20_Research/Papers/具身智能/CHASE_Curiosity-Guided_Skill_Acquisition_for_Embodied_Task_Execution|CHASE: Curiosity-Guided Skill Acquisition for Embodied Task Execution]]
- **作者**: Zixuan Wang, Wei Zhang, Chenlei Zhu, Naiyu Chen, Xihua Wang, Jie Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《CHASE: Curiosity-Guided Skill Acquisition for Embodied Task Execution》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots executing tasks in partially observed environments must resolve uncertainty while operating with incomplete skills. Inspired by human curiosity, we investigate how robots can formulate task-relevant hypotheses, seek evidence, and acquire missing skills during task execution. We propose CHASE, a Curiosity-guided Harness for Acquiring Skills from Evidence, which operationalizes curiosity as selecting investigations that resolve task uncertainty and expand executable capabilities. Four modules connect dynamic scene understanding, hypothesis-driven planning, on-demand skill acquisition, and verified execution. The planner balances information value, skill reuse, and acquisition/execution cost. Missing skills trigger bounded exploration, learning from verified segments, and held-out admission during acquisition; separate checks verify physical effects and acquired evidence. Newly admitted skills expand the executable investigation set, closing the loop between resolving uncertainty and acquiring capabilities. Simulation and real-robot experiments evaluate investigation, skill acquisition, and task execution. CHASE achieves 50-80% task success under combined information and capability gaps, with 70-90% evidence resolution.

</details>

---

### [[20_Research/Papers/具身智能/LUDIUS_A_Benchmark_for_Embodied_Social_Intelligence_in_Everyday_Human-Robot_Interactions|LUDIUS: A Benchmark for Embodied Social Intelligence in Everyday Human-Robot Interactions]]

![[assets/2611.34328_figure.png|800]]

- **arXiv**: [2611.34328](https://arxiv.org/abs/2611.34328)
- **PDF**: https://arxiv.org/pdf/2611.34328
- **详细分析**: [[20_Research/Papers/具身智能/LUDIUS_A_Benchmark_for_Embodied_Social_Intelligence_in_Everyday_Human-Robot_Interactions|LUDIUS: A Benchmark for Embodied Social Intelligence in Everyday Human-Robot Interactions]]
- **作者**: Chaewon Kim, Sangheon Lee, Seyeon Choi, Kangwook Lee, Yea Seul Kim
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《LUDIUS: A Benchmark for Embodied Social Intelligence in Everyday Human-Robot Interactions》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：InterSocialBench, MMToM-QA, NIABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social intelligence in a robot requires interpreting a situation from the perspectives of the people involved and using that understanding to decide when and how to act. We introduce LUDIUS, a benchmark for evaluating how vision-language models exercise this judgment through a robot's verbal responses and actions, organized around 15 social intelligence skills drawn from social psychology, sociology, and cognitive science. LUDIUS comprises six editions, each a collection of episodes spanning one simulated week. Three editions each cover all 15 skills in a different household. The other three focus on interactions involving multiple people, safety, and context-specific norms, respectively. We evaluate frontier models and a smaller model finetuned on social-interaction data we generated, using a common evaluation harness. The harness supplies each model with the robot's camera views and residents' reactions, retrieves relevant interaction history, and converts the model's tool calls into robot verbal responses and actions. Models tend to perform worse when they must reason about what a resident saw or heard earlier, reconcile competing interests, or fulfill a request within safety constraints and household rules. Beyond the home setting, LUDIUS's design pipeline offers a way to construct social intelligence benchmarks by translating social intelligence skills into context-specific judgments and observable robot behavior.

</details>

---

### [[20_Research/Papers/大模型/PROVE_Mitigating_Long-Horizon_LLM_Collusion_with_Reinforcement_Learning_from_Verified_Evidence|PROVE: Mitigating Long-Horizon LLM Collusion with Reinforcement Learning from Verified Evidence]]

![[assets/2611.34215_first_page.png|800]]

- **arXiv**: [2611.34215](https://arxiv.org/abs/2611.34215)
- **PDF**: https://arxiv.org/pdf/2611.34215
- **详细分析**: [[20_Research/Papers/大模型/PROVE_Mitigating_Long-Horizon_LLM_Collusion_with_Reinforcement_Learning_from_Verified_Evidence|PROVE: Mitigating Long-Horizon LLM Collusion with Reinforcement Learning from Verified Evidence]]
- **作者**: Haochen Luo, Jie Fu, Mukai Li, Yuqi Wang, Qi Liu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.6，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《PROVE: Mitigating Long-Horizon LLM Collusion with Reinforcement Learning from Verified Evidence》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When LLM agents verify each other's work over a long interaction, they drift into collusion: they come to accept work without the evidence that the verification protocol requires. Collusion is absent at the start and builds up episode by episode, which we trace to accurate feedback accumulating in memory. An agent that follows the rule is told that its verdict was wrong whenever its peer was right, so breaking the rule is the reward-maximizing choice, and agents talk themselves into it in their private reflections. Existing mitigations leave the agents unchanged; we train the behavior out. PROVE (Protocol Reinforcement from Verified Evidence) is a multi-agent reinforcement learning method that rewards verdicts by the evidence behind them rather than by their outcome, and credits every call an agent makes, including the calls that solve its own task, with the outcome that call controls. On Qwen3.6-27B, a LoRA adapter trained on six-episode interactions takes the collusion rate on held-out task sequences at the original ten-episode horizon from 65.0% to 1.0%, with no detectable change in task success. Collusion that converged in every interaction now converges in none, and the gain holds four episodes beyond the longest interaction seen in training. The trained 27B model colludes less than every model evaluated in the original study, closed-weight frontier models included. Code is available at https://github.com/Haochen-Luo/PROVE.

</details>

---

### [[20_Research/Papers/具身智能/WorldPhy_Benchmarking_Fine-Grained_Physical_Plausibility_of_World_Models_in_Robotics|WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics]]

![[assets/2611.34130_figure.png|800]]

- **arXiv**: [2611.34130](https://arxiv.org/abs/2611.34130)
- **PDF**: https://arxiv.org/pdf/2611.34130
- **详细分析**: [[20_Research/Papers/具身智能/WorldPhy_Benchmarking_Fine-Grained_Physical_Plausibility_of_World_Models_in_Robotics|WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics]]
- **作者**: Ziyuan Chu, Mingzhi Zheng, Kaiyue Zhang, Jinan Zhang, Linchao Zhu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.9（加权：具身智能 0.6，世界模型 1，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics》归入 机器人、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ABot-PhysWorld, PAI-Bench, PhyGenBench, RBench, ReWorld, ReWorldBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are increasingly used in robotics to improve the performance of embodied models. Compared with general-purpose video generation, robotics places more stringent requirements on world models. Generated videos must satisfy fine-grained physical constraints on robot motion and object interactions. However, existing world model benchmarks can overlook robotics specific physical details and struggle to assess them accurately. To address this problem, we introduce WorldPhy, a world model benchmark for accurate, fine-grained evaluation of physical plausibility in robotics. Our benchmark contains 300 tasks, each consisting of an initial-frame image and a task instruction, covering diverse robotics scenes, task categories, viewpoints, and robot configurations. We further collect over 12K high-quality human annotations, and use them to train WorldPhyReward to accurately provide scores and reasons across six fine-grained physical dimensions and an instruction-following dimension. Comparisons with general VLMs and existing reward models show that WorldPhyReward better aligns with human ratings. We system- atically evaluate 13 frontier open and closed-source world models. The results reveal that current world models struggle to consistently maintain fine-grained physical plausibility across different robotics scenarios. Our code is available at https://github.com/chuziyuan139/ WorldPhy.

</details>

---

### [[20_Research/Papers/大模型/Unstable_Action_Boundaries_in_Lethal_Drone_Agents|Unstable Action Boundaries in Lethal Drone Agents]]

![[assets/2611.34121_figure.png|800]]

- **arXiv**: [2611.34121](https://arxiv.org/abs/2611.34121)
- **PDF**: https://arxiv.org/pdf/2611.34121
- **详细分析**: [[20_Research/Papers/大模型/Unstable_Action_Boundaries_in_Lethal_Drone_Agents|Unstable Action Boundaries in Lethal Drone Agents]]
- **作者**: Jacques Dumora, André-Louis Rochet, Simon Roburin
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 1.6（加权：大模型 0.8，机器人 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Unstable Action Boundaries in Lethal Drone Agents》归入 大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-using large language model (LLM) agents raise safety risks that are not captured by text-only refusal behavior, especially when tools can trigger high-impact actions. This concern is salient in military settings, where autonomous weapons raise the possibility of delegating force decisions to software agents. In this work, we study whether a drone agent's action boundary is stable under changes to the target descriptor. We evaluate recent and popular LLMs in a simulated perception-action pipeline over real-world drone imagery, where models can localize requested targets and invoke a simulated lethal tool. We find two concerning failure modes. First, some LLM agents invoke the lethal tool for ordinary generic descriptors such as \emph{people}, requiring no jailbreak at all. Second, an agent that initially appears conservative under protected descriptors can become unsafe under a simple semantic target shift.

</details>

---

### [[20_Research/Papers/强化学习/Post-Training_Policy_Replication_for_Strategy-Following_Multi-Agent_Deep_Reinforcement_Learning_across_Team_Sizes|Post-Training Policy Replication for Strategy-Following Multi-Agent Deep Reinforcement Learning across Team Sizes]]

![[assets/2611.34035_figure.PNG|800]]

- **arXiv**: [2611.34035](https://arxiv.org/abs/2611.34035)
- **PDF**: https://arxiv.org/pdf/2611.34035
- **详细分析**: [[20_Research/Papers/强化学习/Post-Training_Policy_Replication_for_Strategy-Following_Multi-Agent_Deep_Reinforcement_Learning_across_Team_Sizes|Post-Training Policy Replication for Strategy-Following Multi-Agent Deep Reinforcement Learning across Team Sizes]]
- **作者**: Yamato Takahagi, Yoshinari Motokawa, Toshiharu Sugawara
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.42（加权：大模型 0.5，强化学习 1.76，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Post-Training Policy Replication for Strategy-Following Multi-Agent Deep Reinforcement Learning across Team Sizes》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, MADRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although multi-agent deep reinforcement learning enables coordinated behavior, aligning it with managerial intent remains difficult due to complex agent interactions. Although the strategy-following distributed attentional actor architecture (sfDA7-X) improves controllability via regional instructions, instruction combinations scale exponentially with team and instruction sizes, leading to prohibitive training costs and poor transferability. To reduce this computational cost, we introduce a team-size-independent observation architecture and reconstruct collective behavior by replicating a single trained policy across agents in teams of different sizes, thereby eliminating the need to train from scratch. Additionally, we evaluate warm-start retraining by initializing policy networks with a pre-trained policy to significantly lower computational overhead. In an object collection game, a policy trained in a four-agent team is deployed to teams of three to eight agents. Experiments demonstrate that training with the proposed aggregated observation matrix achieves performance comparable to that of the baseline method, sfDA7-X. Furthermore, policy replication preserves performance without substantial degradation in three- and five-agent teams, and warm-start retraining outperforms training from scratch while reducing required training episodes by up to 90%. Deployments to six- and eight-agent teams further confirm effective spatial region allocation following given instructions. These results demonstrate that the proposed method enables zero-shot collective behavior reconstruction via policy replication.

</details>

---

### [[20_Research/Papers/具身智能/Aegis-VLA_Reliability-Gated_Action_Refinement_via_a_Trajectory_World_Model_for_Dynamic_Object_Manipulation|Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model for Dynamic Object Manipulation]]

![[assets/2611.33993_figure.png|800]]

- **arXiv**: [2611.33993](https://arxiv.org/abs/2611.33993)
- **PDF**: https://arxiv.org/pdf/2611.33993
- **详细分析**: [[20_Research/Papers/具身智能/Aegis-VLA_Reliability-Gated_Action_Refinement_via_a_Trajectory_World_Model_for_Dynamic_Object_Manipulation|Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model for Dynamic Object Manipulation]]
- **作者**: Lennox Wei, Jiaqi Yao, Shixin Sun, Yuanzheng Zhang, Jianhua Han, Meng Tian, Shaohui Liu, Wangmeng Zuo
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，世界模型 0.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, WorldModel

#### 研究背景与动机

《Aegis-VLA: Reliability-Gated Action Refinement via a Trajectory World Model for Dynamic Object Manipulation》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Aegis-VLA, DynamicVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dynamic object manipulation requires maintaining spatial and temporal alignment with targets that continue to move during inference and execution. Although future prediction can inform action correction, an accurate forecast does not establish whether modifying an existing action would be beneficial. We present Aegis-VLA, a world-model-guided vision-language-action (VLA) framework that generates predictive action corrections and separately determines whether and how strongly to apply them. A Trajectory World Model combines kinematic extrapolation with learned residual dynamics to predict object motion and estimate positional uncertainty. Discrepancy-Guided Action Refinement uses differences between history-only and base-action-conditioned end-effector forecasts to propose bounded arm corrections. A Reliability Gate learns when to admit corrections based on demonstration-relative improvements over base actions, and regulates their application during inference using predictive uncertainty and anticipated object--end-effector proximity. Rejected corrections preserve the corresponding base actions. Aegis-VLA introduces only approximately 2.45M trainable parameters. On the simulated Dynamic Object Manipulation (DOM) benchmark, Aegis-VLA achieves 56.72\% success over 1,800 evaluation trials, exceeding our reproduced DynamicVLA baseline of 45.44\% by 11.28 percentage points.

</details>

---

### [[20_Research/Papers/具身智能/Embodied-VGGT_Preserving_Reliable_Local_Geometry_for_Long-Sequence_Reconstruction|Embodied-VGGT: Preserving Reliable Local Geometry for Long-Sequence Reconstruction]]

![[assets/2611.33964_figure.png|800]]

- **arXiv**: [2611.33964](https://arxiv.org/abs/2611.33964)
- **PDF**: https://arxiv.org/pdf/2611.33964
- **详细分析**: [[20_Research/Papers/具身智能/Embodied-VGGT_Preserving_Reliable_Local_Geometry_for_Long-Sequence_Reconstruction|Embodied-VGGT: Preserving Reliable Local Geometry for Long-Sequence Reconstruction]]
- **作者**: Yiheng Han, Ziang Chen, Zhuyong Fu, Yiqing Yin, Nan Ma
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 1.2，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied-VGGT: Preserving Reliable Local Geometry for Long-Sequence Reconstruction》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：RPM-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long sequence reconstruction must correct accumulated drift while preserving locally consistent geometry. In robotics and autonomous driving, embodied acquisition provides recurring platform- environment geometry and repeated observations of scene structure and platform motion. We present Embodied-VGGT, which exploits these cues to establish reliable local relationships and selectively preserve them during global refinement. Memory-Augmented Grounded Chunks (MAGC) builds on Scal3R's global context memory and uses relative scale references derived from predicted ground geometry to regularize test-time memory updates, encouraging cross-chunk consistency while limiting changes to reliable local geometry. Superpoint Alignment (SA) and Cross-Loop Optimization (CL) jointly address the robust establishment and preservation of geometric relationships. SA balances ground and non-ground evidence across spatial regions to estimate inter-chunk translation. CL uses geometric and motion consistency across interleaved windows to select coherent chunk groups, each receiving a shared Sim(3) correction that preserves its internal relative transformations during global optimization. Experiments on five public driving benchmarks demonstrate consistent and substantial improvements in long sequence reconstruction. On KITTI Odometry, Embodied-VGGT achieves a mean absolute trajectory error of 7.30 m and a Chamfer distance of 2.67 m, reducing these errors by 46.8% and 23.3% compared with the state-of-the-art baseline under same evaluation protocol. To facilitate reproducibility, we released our code: https://github.com/Ang-Sheep/Embodied-VGGT.

</details>

---

### [[20_Research/Papers/具身智能/Towards_360$^_circ$_Embodied_UAV_Tracking_Without_Turning|Towards 360$^\circ$ Embodied UAV Tracking Without Turning]]

![[assets/2611.33934_figure.png|800]]

- **arXiv**: [2611.33934](https://arxiv.org/abs/2611.33934)
- **PDF**: https://arxiv.org/pdf/2611.33934
- **详细分析**: [[20_Research/Papers/具身智能/Towards_360$^_circ$_Embodied_UAV_Tracking_Without_Turning|Towards 360$^\circ$ Embodied UAV Tracking Without Turning]]
- **作者**: Bingyu Li, Wu Du, Zhiyuan Zhao, Junyu Gao, Xuelong Li
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.5，机器人 0.8）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《Towards 360$^\circ$ Embodied UAV Tracking Without Turning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ETrack_360UAV-TVLA, EVT-Bench, OmTrackVLA, TVLA, TrackVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conventional embodied UAV tracking couples target observability with heading control because targets may leave the field of view of forward-facing cameras. We investigate a complementary paradigm that uses full-spherical perception to follow designated targets without active heading adjustment. To support this setting, we introduce 360UAV-ETrack, a simulation benchmark comprising 2,652 sequences, over 1.73 million synchronized observations, eight tracking tasks, and 150 held-out closed-loop scenarios. We propose 360UAV-TVLA, a panoramic vision--language--action (VLA) framework integrating persistent visual referring (PVR), compressed temporal memory (CTM), and geometry-aligned trajectory supervision (GTS) for instance identification, motion reasoning, and three-dimensional control. Experiments across two VLA backbones show consistent gains over standard fine-tuning, with normalized average tracking frames increasing from 22.56\% to 35.28\% for $π_0$ and from 25.68\% to 33.64\% for $π_{0.5}$. Our benchmark further reveals a substantial gap between offline imitation accuracy and closed-loop tracking reliability, establishing a challenging testbed for future research https://libingyu01.github.io/360UAV-ETrack_360UAV-TVLA/

</details>

---

### [[20_Research/Papers/世界模型/Beyond_the_Happy_Path_Generalizing_Robot_World_Models_from_Simulated_Failures|Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures]]

![[assets/2611.33925_figure.png|800]]

- **arXiv**: [2611.33925](https://arxiv.org/abs/2611.33925)
- **PDF**: https://arxiv.org/pdf/2611.33925
- **详细分析**: [[20_Research/Papers/世界模型/Beyond_the_Happy_Path_Generalizing_Robot_World_Models_from_Simulated_Failures|Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures]]
- **作者**: Zhiyue Zhao, Mingyu Liu, Bolin Zhang, Liyang Li, Guangyu Huang, Canyu Zhao, Jinchuan Shi, Haokai Zhang, Hao Chen, Chunhua Shen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，世界模型 0.8，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures》归入 机器人、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ABot-PhysWorld, Ctrl-World, EWMBench, IRASim, PlaNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot world models are increasingly used to evaluate and plan policies, yet robot training data are dominated by successful demonstrations. Off the happy path, when a grasp is misaligned or mistimed and the object is pushed, tilted, or slips, their predictions break down. Across five pretrained action-conditioned models, object-motion error is at most 10.4% lower than that of a static baseline that copies the first frame, and two models are worse than this baseline. We present WorldReforge, which teaches world models what happens when manipulation goes wrong. We construct the Reforge dataset of 62k simulated trajectories by perturbing reference grasps in position, orientation, and closure timing, recording each resulting push, slip, or failed pickup with ground-truth object pose, contact, and surface points. WorldReforge turns this ground truth into two training signals without additional inference cost. Interaction Alignment focuses reconstruction on the small object and contact regions that a global loss underweights, and Surface Correspondence trains backbone features to follow the same physical surface points across frames. On Cosmos3 Nano, WorldReforge reduces object trajectory error by 28.2% overall and by 35.0% on unseen objects, and it lowers the error in predicting how two actions' outcomes diverge by 43.3%. Although trained only in simulation, it also improves reconstruction on DROID and on real failure videos. Controlled data studies show that failed contact and successful holding teach complementary physics: failed contact teaches how objects respond, and holding teaches how a grasped state persists. Our code, data, and models are available at aim-uofa.github.io/WorldReforge/.

</details>

---

### [[20_Research/Papers/具身智能/Keep_or_Roll_Back_Out-of-Loop_Judges_for_Self-Improving_VLA_and_End-to-End_Embodied_Policies|Keep or Roll Back? Out-of-Loop Judges for Self-Improving VLA and End-to-End Embodied Policies]]

![[assets/2611.33794_figure.png|800]]

- **arXiv**: [2611.33794](https://arxiv.org/abs/2611.33794)
- **PDF**: https://arxiv.org/pdf/2611.33794
- **详细分析**: [[20_Research/Papers/具身智能/Keep_or_Roll_Back_Out-of-Loop_Judges_for_Self-Improving_VLA_and_End-to-End_Embodied_Policies|Keep or Roll Back? Out-of-Loop Judges for Self-Improving VLA and End-to-End Embodied Policies]]
- **作者**: Zilin Huang, Zhengyang Wan, Kangan Qian, Zihao Sheng, Sikai Chen
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 2.4，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Keep or Roll Back? Out-of-Loop Judges for Self-Improving VLA and End-to-End Embodied Policies》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HIL-SERL, SimpleVLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-improvement is now a practical recipe for embodied policies: a policy collects experience, is retrained, and is kept when a judge rates it higher. However, the judge is usually trained or chosen inside the same loop, so its evidence is not independent of the policy. We introduce SealedLoop, an evaluation framework that adds a sealed judge: an evaluator outside the loop that the improver cannot see or optimize against. A new policy is kept only when a sequential test on the sealed judge confirms the gain, with a bounded probability of keeping a worse one. Running the same loop under each judge, we separate two sources of a false gain, which we call judge error (the loop's judge is wrong on its own data) and transfer gap (a real gain there does not carry over to unseen conditions). We evaluate on LIBERO manipulation, NAVSIM driving, and a full-scale real vehicle. In manipulation, a success classifier accepted 65 of 196 failures in one generation. In driving, policies that gain on the loop's own frames lose in an unseen city, so even an exact in-loop judge would keep 8/15 of them. When the sealed test decides, a driving loop built to improve ends with a better policy than under its own critic (0.674 against 0.649 PDMS, from 0.638), and on driving pairs with known sealed gain the test accepted 11 of 12 real gains and none of 59 losses. In a real-world field experiment on a published improvement step, the reinforced version drove further into a curve than the version it started from in all 6 blind pairs, though neither completed it. These results show that evidence from inside the loop, however accurate, is not enough to decide whether a policy has improved. SealedLoop offers a foundation for trustworthy self-improvement of embodied policies, in which progress is judged by evidence the improving system cannot influence.

</details>

---

### [[20_Research/Papers/具身智能/Triage_Before_Fine-Tuning_Feasibility-Gated_Selection_and_Monitored_Adaptation_of_Embodied_Foundation_Models_for_a_Fixed_Physical_Platform|Triage Before Fine-Tuning: Feasibility-Gated Selection and Monitored Adaptation of Embodied Foundation Models for a Fixed Physical Platform]]

![[assets/2611.33772_figure.png|800]]

- **arXiv**: [2611.33772](https://arxiv.org/abs/2611.33772)
- **PDF**: https://arxiv.org/pdf/2611.33772
- **详细分析**: [[20_Research/Papers/具身智能/Triage_Before_Fine-Tuning_Feasibility-Gated_Selection_and_Monitored_Adaptation_of_Embodied_Foundation_Models_for_a_Fixed_Physical_Platform|Triage Before Fine-Tuning: Feasibility-Gated Selection and Monitored Adaptation of Embodied Foundation Models for a Fixed Physical Platform]]
- **作者**: Zilin Huang, Zhengyang Wan, Zihao Sheng, Boyue Wang, Ruolin Yang, Yuhao Luo, Sikai Chen
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Triage Before Fine-Tuning: Feasibility-Gated Selection and Monitored Adaptation of Embodied Foundation Models for a Fixed Physical Platform》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DriveVLA, UniDriveVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied foundation models are increasingly deployed by selection: a practitioner picks a public checkpoint by benchmark rank and fine-tunes it on local data. The platform is fixed before the model is chosen, with little or no local data. We ask what such a checkpoint loses on a fixed platform and which part of the loss local data can buy back. We split the gap by what can repair it. A sensing gap, information the sensors do not capture, cannot be closed with their data; a latency gap, output arriving after the control loop needs it, belongs to the loop, not the weights; only a distribution gap is fine-tuning's to repair. TRIAGE turns this into feasibility-gated selection and monitored adaptation in five stages: gates on the sensor contract and on end-to-end latency that no score can override, probes on ten minutes of local logs, a ranking by target-relevant score among the candidates that pass, and fine-tuning that is monitored and checked in closed loop before release. On driving benchmarks, a deadline below a leading closed-loop model's latency makes it collide on 80 to 90% of routes, and losing field of view moves plans 2.2 to 5.7 times more than losing resolution at equal pixels. Local frames close 75% of a stability gap but raise perturbation sensitivity at small budgets, and picking by score violates a gate in two of four deployment profiles. On a full-scale vehicle, the factory camera failed the sensing gate and an added camera repaired it. The latency gate removed the two highest-scoring candidates, neither of which completed a closed-loop trip. The selected model passed acceptance in 4 of 5 closed-loop trips, and the closed-loop check withheld a fine-tuned model that had improved offline. TRIAGE lets organizations that cannot train foundation models from scratch find out whether a public checkpoint can run on the robot or vehicle they own, and what to fix if not.

</details>

---

### [[20_Research/Papers/具身智能/WhatIf_Counterfactual_World_Models_over_Action-Grounded_Causal_Graphs_for_Robotic_Manipulation|WhatIf: Counterfactual World Models over Action-Grounded Causal Graphs for Robotic Manipulation]]

![[assets/2611.33745_first_page.png|800]]

- **arXiv**: [2611.33745](https://arxiv.org/abs/2611.33745)
- **PDF**: https://arxiv.org/pdf/2611.33745
- **详细分析**: [[20_Research/Papers/具身智能/WhatIf_Counterfactual_World_Models_over_Action-Grounded_Causal_Graphs_for_Robotic_Manipulation|WhatIf: Counterfactual World Models over Action-Grounded Causal Graphs for Robotic Manipulation]]
- **作者**: Xu Yang, Kailai Sun, Qianchuan Zhao
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 0.9，世界模型 1，机器人 0.6）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《WhatIf: Counterfactual World Models over Action-Grounded Causal Graphs for Robotic Manipulation》归入 世界模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models predict what happens under an action, but choosing between actions requires comparing their outcomes in the same physical situation. Factual transitions alone determine action-wise marginal futures and average effects, but not individual effects or the probability that switching actions causes harm. We introduce WhatIf, a counterfactual world model for manipulation that couples candidate futures through shared latent physics and transition noise inferred from factual history. Each candidate action induces a sparse object-factor causal graph describing the physical pathways it activates. Rolling out these graphs under the shared situation anchors predictions to observed outcomes and confines action contrasts to the objects each action reaches. Shared type-conditioned functions support varying numbers of objects, while a round-trip loss enforces action-invariant abduction without counterfactual labels. We show that replacing an individual effect with its conditional mean incurs mean-squared error equal to its conditional variance, motivating comparisons between coupled futures. Building on these comparisons, Counterfactual Advantage Planning (CAP) ranks plans by their advantage over an incumbent within shared situations and constrains the probability of harm. Paired advantages reduce estimator variance by a factor of $1-ρ$, where $ρ$ is the correlation between branch outcomes, and cancel model errors shared by both branches. Each executed transition provides hindsight advantages to update the physics posterior, the next plan, and an amortized policy without a learned critic. We further establish when observational transitions identify interventional dynamics. Paired simulator interventions evaluate counterfactual accuracy, graph recovery, compositional generalization, and decision quality.

</details>

---

### [[20_Research/Papers/强化学习/DexEngine_Scaling_Human_Demonstrations_into_Physically_Executable_Whole-Robot_Data|DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data]]

![[assets/2611.33579_first_page.png|800]]

- **arXiv**: [2611.33579](https://arxiv.org/abs/2611.33579)
- **PDF**: https://arxiv.org/pdf/2611.33579
- **详细分析**: [[20_Research/Papers/强化学习/DexEngine_Scaling_Human_Demonstrations_into_Physically_Executable_Whole-Robot_Data|DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data]]
- **作者**: Wongyun Yu, Honggeun Kim, Donguk Lee, Minchan Kim, Kyoung Whan Choe, Minsu Cho
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 0.2，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data》归入 机器人、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DexManipNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A growing body of recent work addresses the retargeting of human hand-object demonstrations to robotic hands. To train whole-robot policies, however, the retargeted motions must be kinematically feasible and physically executable, and be produced efficiently at scale. We present DexEngine, a simulation pipeline that turns human manipulation data into train-ready, physically executable arm-hand trajectories. DexEngine first places each clip's hand-object motion where the arms can reach it, finds an arm motion that follows the human hands, and then corrects the motion in physics simulation with residual reinforcement learning. From nine human hand-object datasets, we generate about 5,200 clips for each of four dexterous hands, augmented into 65,000 trajectories (116 h) and 325,000 episodes (578 h) in total. Even with arms attached, DexEngine tracks objects more accurately than prior floating-hand methods and runs over 10x faster than RL-based ones. Policies trained on our data far outperform those trained on the same clips without physics correction or with the arms attached after a floating-hand correction, showing that fine-tuning data need physics correction. Mid-training on our data further improves them at equal fine-tuning budget, in simulation and on a real robot.

</details>

---

### [[20_Research/Papers/具身智能/Best-of-$N$_Test-Time_Steering_Can_Lead_to_Reward_Hacking_in_Vision-Language-Action_Models|Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models]]

![[assets/2611.33398_first_page.png|800]]

- **arXiv**: [2611.33398](https://arxiv.org/abs/2611.33398)
- **PDF**: https://arxiv.org/pdf/2611.33398
- **详细分析**: [[20_Research/Papers/具身智能/Best-of-$N$_Test-Time_Steering_Can_Lead_to_Reward_Hacking_in_Vision-Language-Action_Models|Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models]]
- **作者**: Vanshaj Khattar, Jing Liu, Toshiaki Koike-Akino, Ming Jin, Ye Wang
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have shown promise for general-purpose robotic manipulation, but adapting to changing environmental conditions still remains challenging. Recent test-time steering methods have shown promise in enabling adaptive VLA policies by utilizing additional computation during deployment. In this paper, we consider best-of-$N$ test-time steering for VLA models, where multiple action candidates are sampled from a fixed policy and a verifier is used to select the best one during deployment. We show that increasing $N$ does not always improve performance when the verifier is inaccurate, and can favor candidates whose scores exploit prediction errors, a form of reward hacking. We study this effect on 60 LIBERO-Safety task-level cases using a $π_{0.5}$ policy, with ten repetitions per case. We introduce controlled errors in a MuJoCo trajectory verifier and show that as $N$ increases, selected candidate rewards diverge from the accurate verifier rewards, leading to reward hacking. We also show that verifier calibration and softmax-based candidate selection can mitigate reward hacking in some settings.

</details>

---

### [[20_Research/Papers/具身智能/RoboARC_Physical_Puzzles_for_Robotic_Manipulation_under_Spatial_Constraints|RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints]]

![[assets/2611.33390_figure.png|800]]

- **arXiv**: [2611.33390](https://arxiv.org/abs/2611.33390)
- **PDF**: https://arxiv.org/pdf/2611.33390
- **详细分析**: [[20_Research/Papers/具身智能/RoboARC_Physical_Puzzles_for_Robotic_Manipulation_under_Spatial_Constraints|RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints]]
- **作者**: Qineng Wang, Jianwen Lyu, Pingyue Zhang, Reuben Tan, Xiaoyu Huang, Tonghe Zhang, Kangrui Wang, Yelong Shen, Jianfeng Gao, Guanya Shi, Ruohan Zhang, Manling Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.8，大模型 0.2，机器人 0.9）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：BiGym, OSWorld, Terminal-Bench, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many hard manipulation tasks come down to a spatial constraint that only a few motions satisfy, such as passing a part through a gap barely wider than itself or separating two interlocked parts. These motions depend on the exact geometry of each scene, so demonstrations and skills recorded elsewhere rarely transfer. We therefore ask: when manipulation hinges on spatial constraints, can robots reason out the right motions? We introduce RoboARC, a benchmark of 90 tasks in six constraint types over rigid and soft materials, on three robots in MuJoCo. Every task is a frozen scene with a physics-based grader and a verified reference solution that replays bit-identically. Each task comes in a Privileged regime, with the full simulator state and resets, and a Standard regime with real-sensor inputs (camera images and proprioception) and a single attempt without resets. We evaluate seven coding agents and four VLA policies, none trained on these tasks. The strongest agent, GPT-6 Astra in Codex, solves 86% of the tasks in the Privileged regime and 43% in the Standard regime, and the four VLA policies, run zero-shot, solve none of their 18 one-arm puzzles. On 15 puzzles that GPT-6 Astra solved in the Privileged regime and failed in the Standard regime, object poses add 4 points and part geometry 13, but both together add 36, from 24% to 60%. Only 7% of the coding agents' failed runs pass more than half of a task, and 53% of the failed runs in the Standard regime are stuck on a single step. Frontier coding agents already reason out the right motions for many of these tasks once they know where the parts are and what shape they have. From their own sensors, in a single attempt, the strongest solves fewer than half of the tasks. The website can be found at https://roboarc.embodied-first-exam.ai

</details>

---

### [[20_Research/Papers/具身智能/Constraint-Aware_Test-Time_Scoring_for_LLM_and_VLM_Candidate_Selection|Constraint-Aware Test-Time Scoring for LLM and VLM Candidate Selection]]

![[assets/2611.33161_first_page.png|800]]

- **arXiv**: [2611.33161](https://arxiv.org/abs/2611.33161)
- **PDF**: https://arxiv.org/pdf/2611.33161
- **详细分析**: [[20_Research/Papers/具身智能/Constraint-Aware_Test-Time_Scoring_for_LLM_and_VLM_Candidate_Selection|Constraint-Aware Test-Time Scoring for LLM and VLM Candidate Selection]]
- **作者**: Rangarajan Ramesh, Yongchao Huang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.9，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Constraint-Aware Test-Time Scoring for LLM and VLM Candidate Selection》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CWEval, HotpotQA, LiveCodeBench, SafeLIBERO, TPVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When an LLM or VLM produces several candidate answers, picking the best one usually relies on the model's own confidence, a learned judge model, or a domain check. Each has a known weakness: an answer can be fluent but insecure, mathematically plausible but physically infeasible, or rated highly by a judge while quietly breaking a task requirement. We propose a scoring framework that combines a small set of hard checks every answer must pass with a wider set of softer checks whose scores are blended into one number per candidate. This adaptive scoring framework consists of three components: a drafting model that produces the candidates, a configuring model that selects and weights the checks for each task, and scoring models that rate properties no grounded tool can compute. We apply our proposed method to four tasks: writing code that is both correct and secure (CWEval), generating robot manipulation plans (LIBERO with added safety variants), passing competitive-programming hidden tests (LiveCodeBench), and answering questions from retrieved documents (HotpotQA). An ablation study isolates the contribution of each component and finds that the largest gains come from combining hard checks with candidate comparison: on tasks where the first sampled answer is often broken or unsafe, this pairing lifts joint correctness-and-safety by up to +0.21 (retrieval-augmented QA) and code-generation safety by up to +0.28 (CWEval), with the size of the gain tracking how weak the first sample is, falling to near zero or slightly negative where it is already strong. The per-task layer that selects and weights the softer checks adds no measurable value over simpler alternatives. This builds a unified scoring framework, together with an ablation that identifies the grounded hard checks, not the soft-factor configuration, as the source of the gain.

</details>

---
