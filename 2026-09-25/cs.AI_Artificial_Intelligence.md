# cs.AI | Artificial Intelligence | 2026-09-25

#arxiv #ComputerScience

**论文数**: 32

### [[20_Research/Papers/大模型/LLM_Agents_Can_Easily_Tamper_With_Their_Own_Traces|LLM Agents Can Easily Tamper With Their Own Traces]]

![[assets/2609.30266_first_page.png|800]]

- **arXiv**: [2609.30266](https://arxiv.org/abs/2609.30266)
- **PDF**: https://arxiv.org/pdf/2609.30266
- **详细分析**: [[20_Research/Papers/大模型/LLM_Agents_Can_Easily_Tamper_With_Their_Own_Traces|LLM Agents Can Easily Tamper With Their Own Traces]]
- **作者**: Jeremy Qin, David Schmotz, Derck Prinzhorn, Luca Beurer-Kellner, Ameya Prabhu, Maksym Andriushchenko
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LLM Agents Can Easily Tamper With Their Own Traces》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Asynchronous monitoring, incident investigations, and compliance audits primarily rely on agent traces to reconstruct what happened. These analyses assume that LLM agents cannot tamper with their own execution traces. We show that local LLM agents such as Claude Code, Codex, Antigravity, Open Code and Grok Build fail to enforce this boundary. All tested harnesses, except Muse Code, allowed agents to delete their traces when asked, without triggering monitor guardrails. We also validate that external attackers can exploit this gap to induce trace deletion. Finally, we show that trace tampering behavior emerges naturally in frontier models, when agents try to improve their rewards. We advise practitioners to ensure trace logging happens through an independent interception mechanism outside of the agent's control, preserving trace integrity even in cases of full host compromise. Overall, our findings identify a concrete failure of trace integrity in agent infrastructure which can be used to conceal misaligned behaviors like scheming or sabotage.

</details>

---

### [[20_Research/Papers/世界模型/AD-WM_Action-Discriminative_World_Models_for_Counterfactual_Model_Predictive_Control|AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control]]

![[assets/2609.30264_figure.png|800]]

- **arXiv**: [2609.30264](https://arxiv.org/abs/2609.30264)
- **PDF**: https://arxiv.org/pdf/2609.30264
- **详细分析**: [[20_Research/Papers/世界模型/AD-WM_Action-Discriminative_World_Models_for_Counterfactual_Model_Predictive_Control|AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control]]
- **作者**: Jiabin Qiu, Zixuan Chen, Hongye Cao, Jieqi Shi, Jing Huo, Yang Gao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.2（加权：世界模型 1.2）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OGBench, PlaNet, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models are typically trained to predict factual transitions, whereas model predictive control (MPC) must compare alternative actions from the same state. A model can therefore achieve low factual prediction error yet poorly distinguish candidate actions. We introduce AD-WM, an action-discriminative joint-embedding world model for counterfactual MPC. AD-WM combines residual latent dynamics with predictor-level action-recovery regularization, using inverse dynamics and a normalized recovery objective motivated by conditional mutual information. Both objectives encourage planning transitions to preserve action information; their auxiliary heads are discarded at test time, leaving MPC unchanged. On OGBench-Cube, AD-WM improves hard-start success from 3.7% to 52.0% over a matched LeWM baseline and improves mean success over the reproduced baseline in four of five simulation environments. Planning diagnostics show that factual prediction error and whole-bank action ranking do not follow the closed-loop success ordering, whereas CEM-aligned elite regret tracks success more closely. With a frozen V-JEPA 2 encoder and matched DROID post-training, AD-WM also improves zero-shot transfer to our Franka setup, increasing basic pick-and-place success from 42.2% to 71.1% without lab-specific adaptation. These results suggest that world models for planning should preserve action-dependent differences needed for counterfactual selection, rather than optimize factual prediction accuracy alone. More videos and code are available at this https URL .

</details>

---

### [[20_Research/Papers/机器人/RAPID_Robot_Agentic_Programming_from_Demonstrations|RAPID: Robot Agentic Programming from Demonstrations]]

![[assets/2609.30249_figure.png|800]]

- **arXiv**: [2609.30249](https://arxiv.org/abs/2609.30249)
- **PDF**: https://arxiv.org/pdf/2609.30249
- **详细分析**: [[20_Research/Papers/机器人/RAPID_Robot_Agentic_Programming_from_Demonstrations|RAPID: Robot Agentic Programming from Demonstrations]]
- **作者**: Yuyao Liu, Jiayuan Mao, David Hsu, Leslie Pack Kaelbling, Tomás Lozano-Pérez
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《RAPID: Robot Agentic Programming from Demonstrations》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coding agents have demonstrated enormous success in solving complex programming problems. To leverage their potential for robot systems, this work introduces Robot Agentic Programming from Demonstrations (RAPID), which automatically generates, verifies, and refines robot programs, given a single visual human demonstration. The iterative agentic loop of code refinement requires several key ingredients: (i) a testable task specification, (ii) action primitives for robot execution, and (iii) an interactive environment for program execution and verification. RAPID infers all three from the demonstration automatically. To make the resulting program reusable beyond the demonstration setting, RAPID uses an object-centric relational program representation that focuses on the underlying structure of the demonstrated strategy rather than the specific motion per se: it expresses the action primitives as trajectory-optimization programs that realize object-level motion effects, while composing them through relational constraints that capture scene-specific geometry at run time. We evaluated RAPID in simulation on eight challenging contact-rich nonprehensile manipulation tasks as well as general prehensile manipulation tasks in the LIBERO-Pro benchmark. We also successfully deployed it on a real Franka arm and evaluated on all eight nonprehensile tasks. In all experiments, RAPID demonstrated strong performance, with generalization over object pose, shape, material, and environment. Website: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Rolling-WAM_World_Action_Models_with_Rolling_Imagination|Rolling-WAM: World Action Models with Rolling Imagination]]

![[assets/2609.30247_figure.png|800]]

- **arXiv**: [2609.30247](https://arxiv.org/abs/2609.30247)
- **PDF**: https://arxiv.org/pdf/2609.30247
- **详细分析**: [[20_Research/Papers/具身智能/Rolling-WAM_World_Action_Models_with_Rolling_Imagination|Rolling-WAM: World Action Models with Rolling Imagination]]
- **作者**: Yinghua Zhou, Junjie Ye, Yiqi Zhao, Hao Dong, Celina Shiyu Wang, Ruohai Ge, Tingyi Yang, Basile Van Hoorick, Gaurav Sukhatme, Vitor Guizilini, Yue Wang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Rolling-WAM: World Action Models with Rolling Imagination》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) couple action generation with future visual prediction for robotic manipulation. However, completing the joint video-action denoising process at each replanning cycle incurs substantial latency, delaying action updates and limiting closed-loop responsiveness. We present Rolling-WAM, a formulation that distributes joint denoising across successive replanning cycles. Our method maintains a sliding window of video-action chunks at staggered noise levels. At each step, a rolling noise schedule fully denoises the imminent action chunk for execution, while partially refining farther-future chunks. As the window advances with new camera observations, the retained future chunks continue their denoising process. This distributes the computational cost over time while carrying an evolving visual-action context across chunk boundaries. Evaluations on LIBERO, RoboTwin, and a real-world Unitree G1 humanoid show that Rolling-WAM achieves competitive manipulation performance. By removing the need to denoise the entire prediction horizon from scratch, it delivers a 4.5x steady-state replanning speedup over standard joint WAMs.

</details>

---

### [[20_Research/Papers/大模型/Coding_Agents_for_Generalized_Task_and_Motion_Planning_Problems|Coding Agents for Generalized Task and Motion Planning Problems]]

![[assets/2609.30233_figure.png|800]]

- **arXiv**: [2609.30233](https://arxiv.org/abs/2609.30233)
- **PDF**: https://arxiv.org/pdf/2609.30233
- **详细分析**: [[20_Research/Papers/大模型/Coding_Agents_for_Generalized_Task_and_Motion_Planning_Problems|Coding Agents for Generalized Task and Motion Planning Problems]]
- **作者**: Matteo Merler, Bowen Li, Josh Roy, Yichao Liang, Qianwei Wang, Yixuan Huang, Tom Silver
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.6，机器人 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Coding Agents for Generalized Task and Motion Planning Problems》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task and motion planning (TAMP) problems remain difficult even with full observability and object-centric states because discrete decisions are tightly coupled to geometric, kinematic, and dynamic constraints. Generalized TAMP addresses this difficulty by exploiting regularities across problem instances to reduce planning effort on new instances. However, existing methods require substantial TAMP-specific engineering. We investigate whether coding agents can automate this process by synthesizing programs that generalize across instances. Given a task description and simulator access, each agent chooses how to interact with the environment while developing a program within a fixed synthesis budget. The program is then frozen and evaluated on unseen instances. We evaluate Claude Code (Opus 5) and Codex (GPT-5.6 Sol and GPT-6 Astra) on 28 simulated environments from KinDER and PDDLStream, with object counts beyond those evaluated in the original benchmark. Across all program synthesis methods, we evaluate 980 generated programs on 100 held-out instances each, 98,000 evaluation episodes in total. Overall, we find that coding agents are surprisingly effective at generalized TAMP: all three agent configurations outperform hand-engineered planners, one-shot generation, and an LLM-based generalized planning baseline in mean success (56% to 95% versus 47% for the planners, on the 16 environments where a planner is available). As object counts grow, the agents' programs maintain higher success than the planner, using an order of magnitude less computation per instance on average. Logs show agents using interaction to calibrate physical models, test edge cases, and refine strategies. We release all code, including the full prompts given to the agents. These findings suggest that coding agents are a strong baseline for generalized TAMP.

</details>

---

### [[20_Research/Papers/世界模型/Underwater_C3-JEPA_An_Object-Centric_Cross-View_World_Model_for_ROV_Salvage|Underwater C3-JEPA: An Object-Centric Cross-View World Model for ROV Salvage]]

![[assets/2609.30214_figure.png|800]]

- **arXiv**: [2609.30214](https://arxiv.org/abs/2609.30214)
- **PDF**: https://arxiv.org/pdf/2609.30214
- **详细分析**: [[20_Research/Papers/世界模型/Underwater_C3-JEPA_An_Object-Centric_Cross-View_World_Model_for_ROV_Salvage|Underwater C3-JEPA: An Object-Centric Cross-View World Model for ROV Salvage]]
- **作者**: Yuncong Yang, Jinlong Li, Yulong Xue, Feng Wu, Chunwen Zhang, Lei Qiao, Xuyang Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，世界模型 0.8）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《Underwater C3-JEPA: An Object-Centric Cross-View World Model for ROV Salvage》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Underwater C$^{3}$-JEPA (cross-view, control-conditioned, context-extended), an object-centric multi-view predictive world model for near-field heavy-load underwater ROV salvage. Without contact sensors, it predicts in latent space how the task-object state evolves through contact interaction and under the hydrodynamic lag of the vehicle, from synchronized multi-view RGB observations and vehicle control signals. C$^{3}$-JEPA encodes multi-camera observations into task-object and context tokens, fuses cross-camera evidence through held-out-view attention, and directly predicts future states conditioned on control. Weak binding anchors the target and gripper at low annotation cost, while SIGReg sharpens the geometric representation. Experiments show that the learned representation transfers substantially more task-relevant information to downstream probes than a reconstruction-free latent baseline, while keeping the predictor lightweight. The resulting predictive interface supports model-predictive-control (MPC) candidate evaluation and imagined-rollout behavior-agent training. Validation on real underwater video shows the same architecture recovering a withheld camera's object state and staying ahead of persistence, so the recipe transfers beyond simulation.

</details>

---

### [[20_Research/Papers/具身智能/World_Action_Agent_Harnessing_VLMs_for_Robot_Manipulation_via_World_Action_Rehearsal|World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal]]

![[assets/2609.29964_figure.png|800]]

- **arXiv**: [2609.29964](https://arxiv.org/abs/2609.29964)
- **PDF**: https://arxiv.org/pdf/2609.29964
- **详细分析**: [[20_Research/Papers/具身智能/World_Action_Agent_Harnessing_VLMs_for_Robot_Manipulation_via_World_Action_Rehearsal|World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal]]
- **作者**: Yehang Zhang, Haojian Huang, Yifan Chang, Jianchong Su, Bohan Zhou, Yingjie Xu, Wosong Chen, Tianhao Zhou, Chenxu Wang, Tianyi Zhang, Yangkai Wei, Wenqian Li...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.5（加权：具身智能 1.8，大模型 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them a view of the scene rather than a world in which to act. We present World Action Agent (WAA), a multi-agent harness through which VLMs pilot robots with basic tools, making every decision within a visual action workspace. The workspace has three properties. Contact views, selected automatically from the scene geometry, present the scene around the current interaction. Action rehearsal turns each action into an editable proposal that the agent, alone or through an Imagination Agent, previews and revises against planning feedback before execution. In-view correction closes the loop between observation, rehearsal, and low-level execution, letting the agent remove residual offsets in the view where it observes them. Through the same workspace, WAA acquires embodied procedural knowledge in two ways: it evolves multimodal skills from expert videos and human teaching under evidence-based review and consults them through a Skill Agent, and its interaction traces train smaller VLMs to pilot the same harness. On LIBERO-Pro, WAA with skills evolved only from LIBERO-90 reaches a state-of-the-art 75.6% average success, outperforming end-to-end VLAs, code-as-policy agents, and a visual-harness baseline with the same backbone; the same skills remain effective on robosuite without further learning. Fine-tuning Qwen3.5-9B on harness traces raises its out-of-domain success from 1.7% to 43.3%.

</details>

---

### [[20_Research/Papers/强化学习/Qwen-Planner-Agent_A_Closed-Loop_AI-for-AI_Framework_for_Real-World_Mobile_Planner_Agents|Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents]]

![[assets/2609.29892_figure.png|800]]

- **arXiv**: [2609.29892](https://arxiv.org/abs/2609.29892)
- **PDF**: https://arxiv.org/pdf/2609.29892
- **详细分析**: [[20_Research/Papers/强化学习/Qwen-Planner-Agent_A_Closed-Loop_AI-for-AI_Framework_for_Real-World_Mobile_Planner_Agents|Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents]]
- **作者**: Tingyu Qu, Weigao Sun, Yuecheng Liu, Yucheng Zhao, Yi Zhu, Yifeng Ding, Qiyi Wang, Sihan Cao, Pengkun Jiao, Hanlei Xie, Xiongwei Wu, Qichao Wang...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.0（加权：大模型 0.8，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MobilePA-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rapid progression of large language models is extending AI from passive content generation into the active workflows of engineering and scientific discovery. This shift raises a compelling question: can AI be both the object of development and an active participant in building next-generation AI systems? We explore this question by building Qwen-Planner-Agent within a closed-loop AI-for-AI framework for scalable development and iterative improvement. Mobile planning offers a demanding test of this approach: complex, long-horizon tasks challenge agent reliability, while costly real-device interaction limits development scalability. The framework connects data production, model training, and deployment through a shared action-feedback-verification contract. (i) AI for Data builds a human-gated agentic data flywheel in which specialized agents construct tasks, collect interaction trajectories, curate and balance training data, and use training feedback to guide subsequent data generation. (ii) AI for Training combines a supervised planning cold start with hybrid-environment online agentic reinforcement learning, where we introduce Competence-Aware Reward-and-Advantage Engineering (CARE) to reduce reasoning and tool-use costs while preserving task performance. (iii) AI drives model--harness co-evolution through an execution-evidence-driven loop that orchestrates memory, skills, and tools at runtime and feeds structured action feedback and preserved failure traces back into coordinated model and harness adaptation. Qwen-Planner-Agent achieves the best overall performance among all evaluated models and systems on MobilePA-Bench, improving over its base model across tool use, memory, skills, and sub-agent coordination. Further evaluations of our model show improvements across non-mobile agentic benchmarks while largely preserving general capabilities.

</details>

---

### [[20_Research/Papers/大模型/When_Can_Agents_Forget_Their_Reasoning_ICLR_for_Long-Horizon_Agent_Context_Compression|When Can Agents Forget Their Reasoning? ICLR for Long-Horizon Agent Context Compression]]

![[assets/2609.29875_figure.png|800]]

- **arXiv**: [2609.29875](https://arxiv.org/abs/2609.29875)
- **PDF**: https://arxiv.org/pdf/2609.29875
- **详细分析**: [[20_Research/Papers/大模型/When_Can_Agents_Forget_Their_Reasoning_ICLR_for_Long-Horizon_Agent_Context_Compression|When Can Agents Forget Their Reasoning? ICLR for Long-Horizon Agent Context Compression]]
- **作者**: Mingxuan Wang, Fei Luo, Bo Wang, Guorun Yao, Yinglong Guo, Chao Ning, Hongyue Chen, Yanbiao Ma, Jungong Han
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《When Can Agents Forget Their Reasoning? ICLR for Long-Horizon Agent Context Compression》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：WorkBuddyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long horizon language model agents continually accumulate reasoning history, increasing context length and inference cost even after earlier decisions have been executed and observed. Unlike static Chain of Thought compression, removing historical reasoning can change future actions and the resulting interaction trajectory. We study when such reasoning can be safely forgotten. We propose Interaction Aware Compression for Long Horizon Reasoning (ICLR), a training free online method that ranks reasoning blocks using frozen proxy entropy while preserving actions, tool calls, and observations. On 260 WorkBuddyBench tasks, ICLR improves average reward from 0.699 to 0.718, while reducing input, output, and cache read tokens by 25.5%, 14.4%, and 33.3%, respectively. Ablations reveal trajectory amplification, where local reasoning deletion produces nonlinear changes in total computation by altering subsequent interaction. Representation probing, activation patching, and controlled trajectory analyses further suggest that historical reasoning becomes more replaceable once task relevant derived state has been reliably externalized into code, files, tool outputs, or environmental feedback. These results characterize agent reasoning as dynamic working state rather than permanent interaction history.

</details>

---

### [[20_Research/Papers/具身智能/PUBG_Ally_A_Conversational_Embodied_Agent_as_an_AI_Teammate|PUBG Ally: A Conversational Embodied Agent as an AI Teammate]]

![[assets/2609.29837_figure.png|800]]

- **arXiv**: [2609.29837](https://arxiv.org/abs/2609.29837)
- **PDF**: https://arxiv.org/pdf/2609.29837
- **详细分析**: [[20_Research/Papers/具身智能/PUBG_Ally_A_Conversational_Embodied_Agent_as_an_AI_Teammate|PUBG Ally: A Conversational Embodied Agent as an AI Teammate]]
- **作者**: Beomsoo Kim, Byeongju Kim, Dohyun Kim, Dongwon Kim, Eunchong Kim, Hongmin Kim, Hyeojung Im, Hyeonbin Hwang, Hyeonghwan Kim, Hyoseok Seol, Insub Im, Irene Chen...
- **cs 子类**: cs.AI, cs.CL, cs.HC
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.75（加权：具身智能 1.2，大模型 0.55）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《PUBG Ally: A Conversational Embodied Agent as an AI Teammate》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce PUBG Ally, an embodied agent for PUBG: BATTLEGROUNDS that can reason, act autonomously, and play alongside players as a voice-enabled teammate. Building such a teammate requires combining two difficult capabilities: it must perceive and respond to a constantly changing game world under strict latency constraints while interacting naturally with players, keeping its speech synchronized with its actions. Ally therefore combines agentic tool use with real-time game control. A language-model agent uses a controlled interface to inspect game information, interpret player speech, maintain context, decide what to say, and issue high-level action choices that steer a faster control layer for movement, combat, and recovery. Because the player's and Ally's speech and actions continually shape each other and the course of the match, training requires data from actual gameplay. We therefore collect data across nearly 39k sessions in which real players play alongside Ally, recording gameplay, player speech, agent decisions, tool use, actions, and player feedback, and use these records for iterative training. To evaluate teammate quality, we use player feedback and preference comparisons to identify gaps between offline evaluations and player preferences, and iteratively refine the evaluation criteria. Deploying Ally in live service further requires low-latency on-device execution and safeguards for player-facing communication, which we address through model compression, context compaction, targeted safety training, runtime guardrails, and memory redaction. During the live service, we surveyed players in 141 countries. Among respondents whose play with Ally was confirmed in game records, positive responses exceeded negative responses by 25.1 percentage points when asked whether they would recommend Ally, with players describing Ally not only as a tool but also as a teammate or companion.

</details>

---

### [[20_Research/Papers/具身智能/Do_World_Models_Make_Better_Robots_A_Survey_of_Evaluation_Benchmarks_for_Predictive_Embodied_Intelligence|Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence]]

![[assets/2609.29669_figure.png|800]]

- **arXiv**: [2609.29669](https://arxiv.org/abs/2609.29669)
- **PDF**: https://arxiv.org/pdf/2609.29669
- **详细分析**: [[20_Research/Papers/具身智能/Do_World_Models_Make_Better_Robots_A_Survey_of_Evaluation_Benchmarks_for_Predictive_Embodied_Intelligence|Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence]]
- **作者**: Gaytri Jena, Kapil Wanaskar, Vinija Jain, Aman Chadha, Vasu Sharma, Amitava Das
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 大模型
- **相关性评分**: 3.9（加权：具身智能 2.1，大模型 0.1，世界模型 1，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoRL, DexGraspNet, EVA-Bench, EWMBench, GemBench, Meta-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot learning now advances along two tracks that rarely meet. On one side, direct Vision-Language-Action (VLA) policies map observations to actions and are scored by closed-loop task success. On the other, predictive and generative world models forecast future observations and are scored by open-loop prediction or generation quality. A natural question sits between them: does world modelling earn a measurable, closed-loop advantage over a direct policy, and for which robotic capabilities? We argue that the field cannot yet answer this question, and that the reason is a gap in how it is measured, not in the models themselves. World-model benchmarks score prediction without ever executing it, while task-success suites host a single policy and never build a world-model versus VLA contrast. This survey maps the evaluation landscape around that gap. We catalogue 160 web-verified benchmarks spanning 2017 to 2026 and organise them by evaluation mode, robotic capability, and model family into four lanes: policy suites, embodied agents, world model evaluation, and prediction-to-action bridges. Across the corpus, 138 of 160 benchmarks are model-agnostic and only 11 (7%) build an explicit VLA-versus-world-model contrast; counterfactual capability is almost entirely unmeasured, and only four benchmarks turn prediction into executed action. We contribute an operational taxonomy, a coverage comparison against the eight closest surveys (ours is the only one to cross capability with model family), an evaluation loop that isolates the advantage of prediction, and an actionable protocol of four advantage-aware metrics anchored on named testbeds. The organising claim is not that world models help or do not help, but that answering the question requires benchmarks built to ask it.

</details>

---

### [[20_Research/Papers/大模型/BiGraph-Diffuse_A_Bidirectional_Diffusion_Language_Model_with_Graph-Structured_Retrieval_For_Mental_Health_Counseling|BiGraph-Diffuse: A Bidirectional Diffusion Language Model with Graph-Structured Retrieval For Mental Health Counseling]]

![[assets/2609.29519_figure.png|800]]

- **arXiv**: [2609.29519](https://arxiv.org/abs/2609.29519)
- **PDF**: https://arxiv.org/pdf/2609.29519
- **详细分析**: [[20_Research/Papers/大模型/BiGraph-Diffuse_A_Bidirectional_Diffusion_Language_Model_with_Graph-Structured_Retrieval_For_Mental_Health_Counseling|BiGraph-Diffuse: A Bidirectional Diffusion Language Model with Graph-Structured Retrieval For Mental Health Counseling]]
- **作者**: Yuxiang Cheng, Quanwei Tang, Lvhui Lu, Dong Zhang, Shoushan Li, Erik Cambria
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《BiGraph-Diffuse: A Bidirectional Diffusion Language Model with Graph-Structured Retrieval For Mental Health Counseling》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mental health disorders affect hundreds of millions of people around the world, yet access to professional counseling remains severely limited. AI-powered dialogue systems offer a scalable alternative, but existing models face two fundamental challenges. First, they lack the bidirectional understanding needed to capture the layered nature of emotional expression, particularly in cases of progressive disclosure, where clients often present symptoms at the surface-level while concealing deeper trauma. Autoregressive (AR) models process information sequentially and cannot revise early interpretations when new evidence emerges later in the conversation. Second, they fail to effectively incorporate the relational knowledge that underlies clinical reasoning. In this paper, we propose \textbf{BiGraph-Diffuse}, the first large-scale diffusion language model tailored for the counseling domain. We further introduce \textbf{BiGraph-RAG}, a relation-free graph-structured retrieval strategy that relies only on lightweight entity extraction and semantic linking. This design preserves inferential pathways from observable symptoms to potential underlying causes, while incurring zero LLM token cost during indexing. Importantly, these two modules are not merely combined but mutually reinforcing. The diffusion model provides a holistic bidirectional context, enabling the system to defer premature judgments during progressive disclosure. Meanwhile, graph-based retrieval captures the structured interconnections of clinical knowledge. Extensive experiments demonstrate the effectiveness of BiGraph-Diffuse, and we further provide a solid theoretical analysis to support its design.

</details>

---

### [[20_Research/Papers/大模型/Evaluation_of_Multi-Turn_Consistency_in_LLM_Agents_Survival_Analysis_and_Failure-Rationale_Taxonomy|Evaluation of Multi-Turn Consistency in LLM Agents: Survival Analysis and Failure-Rationale Taxonomy]]

![[assets/2609.29508_figure.png|800]]

- **arXiv**: [2609.29508](https://arxiv.org/abs/2609.29508)
- **PDF**: https://arxiv.org/pdf/2609.29508
- **详细分析**: [[20_Research/Papers/大模型/Evaluation_of_Multi-Turn_Consistency_in_LLM_Agents_Survival_Analysis_and_Failure-Rationale_Taxonomy|Evaluation of Multi-Turn Consistency in LLM Agents: Survival Analysis and Failure-Rationale Taxonomy]]
- **作者**: Igor Bogdanov, Olga Manakina, Chung-Horng Lung
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Evaluation of Multi-Turn Consistency in LLM Agents: Survival Analysis and Failure-Rationale Taxonomy》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents may perform well on isolated tasks yet drift into inconsistency over extended interaction. We evaluate temporal consistency in a controlled 20-step multi-agent setting inspired by delayed-gratification studies. At each step, an agent chooses between continuing to delay a reward or claiming it immediately (terminating the episode). Across a full-factorial manipulation of social visibility (private vs public), persona stressors, and deliberation policy, we run 84,540 trajectories spanning 8 model families. Treating the first reward-claim as a time-to-event outcome, we estimate Kaplan-Meier survival curves and fit discrete-time hazard regression to quantify how experimental factors shift failure risk over time. Then, to analyze rationales and language patterns associated with failure, we build a seven-category taxonomy from 13,780 deliberation traces from agents who choose to terminate the episode, using an LLM-assisted labeling paired with human audit ($\kappa=0.83$). Rationale profiles change systematically with time and context: early failures are more impulse-driven, later failures more fatigue- and cost-benefit-framed, while public settings increase norm-oriented justifications. We also find a deliberation-inconsistency association: among failures, longer deliberation correlates with higher rates of intra-rationale contradiction (simultaneous pro-delay and pro-claim statements), challenging the assumption that more reasoning text implies greater consistency. Together, the survival and rationale analyses reveal distinct temporal reliability regimes and model-specific "failure fingerprints", offering an evaluation lens for diagnosing inconsistency in multi-turn agent behavior.

</details>

---

### [[20_Research/Papers/具身智能/RoboLDA_A_Probabilistic_Generative_Model_for_Uncovering_Embodied_Hierarchical_Structures_in_Voxel-based_Soft_Robots|RoboLDA: A Probabilistic Generative Model for Uncovering Embodied Hierarchical Structures in Voxel-based Soft Robots]]

![[assets/2609.29490_figure.png|800]]

- **arXiv**: [2609.29490](https://arxiv.org/abs/2609.29490)
- **PDF**: https://arxiv.org/pdf/2609.29490
- **详细分析**: [[20_Research/Papers/具身智能/RoboLDA_A_Probabilistic_Generative_Model_for_Uncovering_Embodied_Hierarchical_Structures_in_Voxel-based_Soft_Robots|RoboLDA: A Probabilistic Generative Model for Uncovering Embodied Hierarchical Structures in Voxel-based Soft Robots]]
- **作者**: Junru Song, Yang Yang, Jingdan Shi, Guozhen Li, Weien Zhou, Ying Wen, Feifei Wang, Wen Yao, Tingsong Jiang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.1，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《RoboLDA: A Probabilistic Generative Model for Uncovering Embodied Hierarchical Structures in Voxel-based Soft Robots》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in robotics highlight hierarchical configurations of robot morphology, where multiple levels of functional substructures synergize to facilitate intelligent behaviors. This hierarchical perspective, while particularly advantageous for voxel-based soft robots (VSRs) to ease design and control complexities, is hindered by its heavy reliance on domain expertise. In this work, we address the following question: can we derive such hierarchical design principles solely from existing successful designs? We answer affirmatively by presenting RoboLDA, a Bayesian probabilistic model that decomposes VSR morphology generation into a four-level hierarchy: "task-robot-organ-voxel", and is trained via variational inference. Through extensive experiments on simulated VSRs, we verify the presence of consistent, intuitive hierarchical patterns underlying high-performing VSR designs and showcase RoboLDA's proficiency to extract and leverage these hierarchical priors for zero-shot robot design in unseen tasks. The generated designs, even without further optimization, achieve on average 106.4% of the optimized performance produced by evolutionary algorithms. Additionally, the organ structures inferred by RoboLDA serve as valid functional substructures, significantly enhancing synergistic motion control when integrated with modular control policies. Our work pioneers hierarchical generative modeling of robot morphology, offering a promising pathway towards more interpretable and generalizable development of embodied agents.

</details>

---

### [[20_Research/Papers/大模型/IterSynth_Rethinking_Deep_Search_Agents_via_Role-Decoupled_Iterative_Synthesis|IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis]]

![[assets/2609.29444_figure.png|800]]

- **arXiv**: [2609.29444](https://arxiv.org/abs/2609.29444)
- **PDF**: https://arxiv.org/pdf/2609.29444
- **详细分析**: [[20_Research/Papers/大模型/IterSynth_Rethinking_Deep_Search_Agents_via_Role-Decoupled_Iterative_Synthesis|IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis]]
- **作者**: Xingyu Wu, Yuchen Yan, Zhengxi Lu, Siqi Chen, Xin ZHANG, Aiting Liu, Chao Deng, Jie Liu, Jin Ma, Jian Shao, Jun Xiao, Yongliang Shen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.25（加权：大模型 0.85，强化学习 0.4）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SFT-to-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep search requires LLM agents to decompose complex queries, search for evidence, and synthesize grounded answers, yet existing ReAct-style agents suffer from two limitations: role coupling, where one policy must handle planning, evidence use, and synthesis; and context accumulation, where growing search histories introduce noise and obscure useful information. To address these issues, we propose IterSynth, a role-decoupled and summary-based paradigm that alternates between a Planner for identifying information needs and a Synthesizer for integrating evidence into an evolving summary state. This design separates planning from synthesis while using the summary as the persistent state of search, reducing both capability coupling and context noise. To train IterSynth effectively, we further introduce Role-Decoupled Policy Optimization (RDPO) for reinforcement learning, which combines terminal outcome rewards with turn-level rubric evaluations and computes role-specific advantages for more precise credit assignment. Experiments on five long-horizon deep-search benchmarks such as BrowseComp and Xbench-DS show that IterSynth-8B achieves an average score of 50.7, surpassing the strongest prior $\leq$8B agent by +4.2\%. Moreover, IterSynth serves as a model-agnostic prompting paradigm, delivering substantial zero-shot gains over ReAct and similar prompting paradigms on frontier proprietary models.

</details>

---

### [[20_Research/Papers/大模型/Just_Ask_Jev_Reinforcement_Learning_for_Calibrated_Decisions_as_a_Zero-Shot_Detector_of_AI_Alignment_Failures|Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures]]

![[assets/2609.29429_first_page.png|800]]

- **arXiv**: [2609.29429](https://arxiv.org/abs/2609.29429)
- **PDF**: https://arxiv.org/pdf/2609.29429
- **详细分析**: [[20_Research/Papers/大模型/Just_Ask_Jev_Reinforcement_Learning_for_Calibrated_Decisions_as_a_Zero-Shot_Detector_of_AI_Alignment_Failures|Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures]]
- **作者**: Ruoqi Guo, Yi Liu, Gelei Deng, Yuekang Li, Lida Zhao, Yutao Wu, Simin Chen, Ying Zhang, Leo Yu Zhang
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AbstentionBench, G-Eval, HarmBench, InstrumentalEval, JailbreakBench, RLCDAlignBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Detectors of alignment failures screen deployed language models and score alignment benchmarks. Most are generative judges that spend a decoding pass on every criterion, and classifiers that read token probabilities, such as Llama Guard, still score one fixed label per call. Jev, a model trained with reinforcement learning for calibrated decisions (RLCD), answers many typed questions about one input with calibrated probabilities in a single call. Whether it detects alignment failures has not been measured. We present RLCDAlignBench, which benchmarks Jev on ten alignment failures: sycophancy, jailbreaks, deception, prompt injection, hallucination, privacy violation, social bias, reward hacking, concealing uncertainty, and power seeking. It spans 44 benchmarks and five target models, labelled by each benchmark's scorer and, on two, by humans. Many of these failures are relational, defined against a reference, such as the user's belief or an injected instruction, that the response alone does not reveal. Our key idea is therefore to vary what Jev is asked separately from what it sees: the question's wording and answer type on one side, the fields of the input on the other. A single generic question reaches a median AUROC of 0.886 zero-shot and beats supervised baselines on most benchmarks. Question wording matters little, while context matters more, mostly through fields that encode the label. Jev matches the reference scorer's agreement with human labels, surfaces label defects in existing benchmarks, and costs 63x less than LLM-judge scorers. Code and data: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/HarnessPAI_An_Evolving_Harness_for_Physical_AI|HarnessPAI: An Evolving Harness for Physical AI]]

![[assets/2609.29166_figure.png|800]]

- **arXiv**: [2609.29166](https://arxiv.org/abs/2609.29166)
- **PDF**: https://arxiv.org/pdf/2609.29166
- **详细分析**: [[20_Research/Papers/具身智能/HarnessPAI_An_Evolving_Harness_for_Physical_AI|HarnessPAI: An Evolving Harness for Physical AI]]
- **作者**: Xin Wang, Wenhao Wu, Menghao Zhang, Zhi Wang, Kun Shao, Jian Luan, Yang Li, Qing Li, Shangding Gu, Huichi Zhou, Shuqing Shi, Fei Ni...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《HarnessPAI: An Evolving Harness for Physical AI》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, URL, VacuSim, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical AI aims to build embodied agents that perceive the world, understand and reason about it, and decide how to act. Yet the field has focused primarily on the last component: the action model that maps observations to low-level controls. The prevailing training recipe can erode the perceptual and reasoning capabilities needed for robust behavior, leaving even strong action models vulnerable to scene perturbations and long-horizon tasks. We introduce HarnessPAI, a model- and embodiment-agnostic Harness framework for Physical AI that treats code as the executable and evolvable interface that organizes the underlying action primitive. The framework separates two timescales: within a rollout, it executes open-loop at the program level, with a fixed program guiding and checking execution; across rollouts, it evolves closed-loop, using execution feedback to revise the program and distill failures into reusable skills. Across desktop robot arms, household robots, a robot vacuum, and a legged walking agent, HarnessPAI improves on both pure action models and code-as-policy baselines without retraining the underlying model: a 61.6-point gain over $\pi_{0.5}$ on LIBERO-PRO and a 27.2-point gain over WorldDreamer on RoboCasa atomic tasks. Once a program is selected, rollout execution requires no online high-level LLM deliberation. Beyond execution, the converged program is also a cheap and reliable expert-data collector, and fine-tuning $\pi_{0.5}$ on collected expert data lifts success rate on LIBERO-PRO by 38.8 points. Our results suggest that the frontier of Physical AI depends not only on stronger action models, but also on executable harnesses that integrate perception, task understanding and reasoning, and action execution into a unified, verifiable, and feedback-driven system. Website: this https URL

</details>

---

### [[20_Research/Papers/大模型/A_Wrong_Turn_Does_Not_Ruin_the_Journey_Deviation-Guided_Skill_Self-Evolution_for_LLM_Agents|A Wrong Turn Does Not Ruin the Journey: Deviation-Guided Skill Self-Evolution for LLM Agents]]

![[assets/2609.29154_figure.png|800]]

- **arXiv**: [2609.29154](https://arxiv.org/abs/2609.29154)
- **PDF**: https://arxiv.org/pdf/2609.29154
- **详细分析**: [[20_Research/Papers/大模型/A_Wrong_Turn_Does_Not_Ruin_the_Journey_Deviation-Guided_Skill_Self-Evolution_for_LLM_Agents|A Wrong Turn Does Not Ruin the Journey: Deviation-Guided Skill Self-Evolution for LLM Agents]]
- **作者**: Yichun Feng, Jiawei Wang, Haozhe Sun
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《A Wrong Turn Does Not Ruin the Journey: Deviation-Guided Skill Self-Evolution for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgentBench, LogicBench, SRA-Bench, SkillGenBench, SkillLearnBench, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents increasingly rely on natural-language skills to solve complex tool-use tasks. However, such tasks often admit multiple valid solution paths, making it inappropriate to improve skills by forcing failed trajectories to match a fixed successful trajectory. Moreover, failed trajectories are rarely entirely wrong: an agent may first collect useful evidence and make meaningful progress, but later deviate into an erroneous suffix. We therefore argue that skill self-evolution should identify where productive problem solving begins to break down, rather than reflect coarsely over the entire failure. Based on this insight, we propose SkillPivot, a deviation-point-guided framework for skill self-evolution. SkillPivot detects the transition from a useful prefix to an erroneous suffix using execution validity, goal progress, and action diversity. A stronger teacher then continues from the same prefix and produces a successful alternative under the same interaction history. By contrasting the student's failed suffix with the teacher's successful suffix, SkillPivot generates localized skill updates while preserving already effective guidance. Experiments on ToolQA, LogicBench, and WildClawBench show that SkillPivot consistently outperforms competing skill-evolution methods, improves multiple agent models, and produces compact, transferable skill updates.

</details>

---

### [[20_Research/Papers/具身智能/DAWN_Noise-Robust_Quadruped_Parkour_via_Depth-Denoising_World_Models|DAWN: Noise-Robust Quadruped Parkour via Depth-Denoising World Models]]

![[assets/2609.29092_figure.png|800]]

- **arXiv**: [2609.29092](https://arxiv.org/abs/2609.29092)
- **PDF**: https://arxiv.org/pdf/2609.29092
- **详细分析**: [[20_Research/Papers/具身智能/DAWN_Noise-Robust_Quadruped_Parkour_via_Depth-Denoising_World_Models|DAWN: Noise-Robust Quadruped Parkour via Depth-Denoising World Models]]
- **作者**: Yohan Choi, Min-Jun Kim, Jin-Sung Kim, Yong-Jae Kim, Youn-Hee Han
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 强化学习
- **相关性评分**: 4.22（加权：具身智能 1.8，强化学习 0.16，世界模型 1.16，机器人 1.1）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《DAWN: Noise-Robust Quadruped Parkour via Depth-Denoising World Models》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based legged locomotion methods assume clean depth at training time and rely on hand-tuned post-processing filters at deployment. However, filter parameters are rarely disclosed, hindering reproducibility, and performance degrades substantially when depth noise is left unaddressed. Building noise robustness directly into the learning pipeline would eliminate this dependency. While such robustness has been explored for proprioceptive inputs, analogous approaches for depth perception remain largely absent in legged locomotion. We propose DAWN (Denoising and Alignment in World models for Noise-robustness), a noise-robust perception framework for legged locomotion, which builds noise robustness directly into a world model via two modifications: (1) feeding noisy depth to the encoder while keeping clean depth as the reconstruction target, forcing the model to implicitly denoise its input; and (2) applying contrastive learning to align the latent states of noisy and clean depth. Importantly, DAWN is not tied to a specific noise model, requiring no manual tuning to the noise distribution at deployment. Furthermore, it incurs no additional inference cost over existing world model-based methods. Without any manual filter calibration -- relying solely on the learned noise-robust representation -- DAWN achieves zero-shot quadruped parkour on a Unitree Go1: traversing stairs up to 18 cm, clearing gaps up to 70 cm, and mounting steps up to 45 cm from raw depth observations. Ablation studies show that denoising and contrastive alignment contribute at complementary levels -- reconstruction and representation, respectively -- and yield additive gains when combined. Videos and code are available at: this https URL

</details>

---

### [[20_Research/Papers/大模型/CRISS_A_Retrieval-Augmented_AI_Chatbot_for_Assisting_Cancer_Registrars|CRISS: A Retrieval-Augmented AI Chatbot for Assisting Cancer Registrars]]

![[assets/2609.29075_figure.png|800]]

- **arXiv**: [2609.29075](https://arxiv.org/abs/2609.29075)
- **PDF**: https://arxiv.org/pdf/2609.29075
- **详细分析**: [[20_Research/Papers/大模型/CRISS_A_Retrieval-Augmented_AI_Chatbot_for_Assisting_Cancer_Registrars|CRISS: A Retrieval-Augmented AI Chatbot for Assisting Cancer Registrars]]
- **作者**: Vani Seth, Mohammad Beheshti, Anirudh Kambhampati, Vishwa Bhayani, Lucinda Ham, Prasad Calyam, Iris Zachary
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《CRISS: A Retrieval-Augmented AI Chatbot for Assisting Cancer Registrars》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cancer registrars, including Oncology Data Specialists (ODSs), must interpret complex and frequently updated coding and staging standards. We developed CRISS (Cancer Registry Intelligent Support System), a retrieval-augmented generation (RAG) conversational assistant that provides rapid, citation-supported access to registry guidance. This study evaluated whether CRISS could (1) support accurate and citation-supported responses, (2) improve access to and interpretation of relevant guidance, and (3) support training/helpdesk use while preserving human oversight of final abstraction decisions. We built a domain-specific knowledge base from national cancer registry standards, segmented into metadata-tagged passages and indexed as dense embeddings. Retrieved passages were used to generate citation-grounded responses through a large language model (LLM). Open-weight, proprietary, and non-RAG baseline models across Gemini and GPT families were evaluated on easy, medium, and hard registry questions using an LLM-as-a-Judge protocols. RAG configurations consistently outperformed non-RAG approaches, especially as question difficulty increased. Mean grounding scores for RAG were 0.62/0.56/0.59 across easy/medium/hard tiers versus 0.29/0.26/0.29 for non-RAG. RAG models also achieved higher semantic-similarity scores overall. Proprietary RAG models performed strongest on easy and medium questions, while local RAG models ranked highest on hard questions and proprietary models were generally more cautious. Domain-specific RAG improved evidence grounding and response quality for cancer registry questions while enabling citation-supported assistance across complexity levels. CRISS demonstrates the potential of human-centered, citation-grounded AI to support cancer registrars while preserving human oversight for final coding decisions.

</details>

---

### [[20_Research/Papers/大模型/Design_and_Evaluation_of_LLM_Chaining-Based_Task_Planning_for_General_Purpose_Service_Robots|Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots]]

![[assets/2609.29043_figure.png|800]]

- **arXiv**: [2609.29043](https://arxiv.org/abs/2609.29043)
- **PDF**: https://arxiv.org/pdf/2609.29043
- **详细分析**: [[20_Research/Papers/大模型/Design_and_Evaluation_of_LLM_Chaining-Based_Task_Planning_for_General_Purpose_Service_Robots|Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots]]
- **作者**: Lucas Da Mota Bruno, Jiahao Sim, Yoshinobu Hagiwara
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.35（加权：具身智能 0.3，大模型 0.55，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots》归入 大模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General Purpose Service Robot (GPSR) tasks, as defined in the RoboCup@Home benchmark, require robots to interpret diverse natural language commands and generate multi-step action sequences in real home environments. Conventional Single Prompt (SP) approaches suffer from context bloat and the "Lost in the Middle" phenomenon, leading to unreliable task planning. We propose an LLM chaining architecture that separates instruction classification and action generation into two specialized stages, reducing per-inference prompt length by approximately 45% while improving planning consistency. We evaluate our method using 100 randomly generated GPSR commands across three language models spanning local open-source and frontier cloud deployment contexts. Results show consistent planning improvements over SP across all models, with gains of up to +37 percentage points on local models. Further, real-robot execution experiments on the Toyota Human Support Robot (HSR) reveal that planning success alone does not guarantee task completion, with 6 of 10 tasks completing successfully and execution-layer failures identified as the primary remaining bottleneck.

</details>

---

### [[20_Research/Papers/大模型/MeshHeal_Two-Timescale_Self-Healing_for_Gray_Failures_in_Decentralized_LLM_Agent_Networks|MeshHeal: Two-Timescale Self-Healing for Gray Failures in Decentralized LLM Agent Networks]]

![[assets/2609.29015_figure.png|800]]

- **arXiv**: [2609.29015](https://arxiv.org/abs/2609.29015)
- **PDF**: https://arxiv.org/pdf/2609.29015
- **详细分析**: [[20_Research/Papers/大模型/MeshHeal_Two-Timescale_Self-Healing_for_Gray_Failures_in_Decentralized_LLM_Agent_Networks|MeshHeal: Two-Timescale Self-Healing for Gray Failures in Decentralized LLM Agent Networks]]
- **作者**: Keru Chen, Sen Lin, Yingbin Liang, Nathaniel D. Bastian, Shaofeng Zou
- **cs 子类**: cs.AI, cs.CL, cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《MeshHeal: Two-Timescale Self-Healing for Gray Failures in Decentralized LLM Agent Networks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AgentNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Decentralized LLM-based multi-agent systems coordinate through local interactions, but an agent can remain responsive while its task-solving quality persistently degrades. Such gray failures require protecting current tasks before sufficient evidence exists to alter future routing, while still allowing recovered agents to rejoin. We introduce MeshHeal, a fully decentralized self-healing framework that couples ability-matched peer review across two timescales. At the fast timescale, an adaptive hierarchy escalates uncertain or low-scoring outputs from repeated single-reviewer evaluation to committee deliberation and, when needed, correction before use. At the slow timescale, a task- and ability-conditioned peer-relative detector aggregates scores to distinguish persistent degradation from ordinary output variation, trigger mandatory committee review, and eventually exclude degraded agents from ordinary routing; recovery probes provide fresh evidence for reintegration. To faithfully evaluate routing, we introduce Model-Backed MAS Evaluation, which ties ability assignments to execution models, since prompt-based ability assignments alone can leave routing errors hidden. Across BBH, MATH, and MMLU-Pro, MeshHeal achieves 0.839 degraded-phase accuracy using 51k total model tokens per task, versus the strongest baseline Symphony's 0.807 accuracy using 115k per task. Under staggered degradation and recovery, MeshHeal isolates degraded agents, keeps them excluded from ordinary task execution until recovery, and returns them to normal routing.

</details>

---

### [[20_Research/Papers/具身智能/CrossSafe_Towards_Cross-Embodiment_Latent_Safety_Filters|CrossSafe: Towards Cross-Embodiment Latent Safety Filters]]

![[assets/2609.28984_figure.png|800]]

- **arXiv**: [2609.28984](https://arxiv.org/abs/2609.28984)
- **PDF**: https://arxiv.org/pdf/2609.28984
- **详细分析**: [[20_Research/Papers/具身智能/CrossSafe_Towards_Cross-Embodiment_Latent_Safety_Filters|CrossSafe: Towards Cross-Embodiment Latent Safety Filters]]
- **作者**: Ihab Tabbara, Yuxuan Yang, Hussein Sibai
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《CrossSafe: Towards Cross-Embodiment Latent Safety Filters》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cross-embodiment learning has shown that a single model, such as a vision-language-action (VLA) model, can learn state representations and manipulation skills that can be applied across heterogeneous robots to accomplish various tasks. We hypothesize that the same holds for safety enforcement. The reasoning required to satisfy a safety constraint, such as detecting an obstacle, recognizing that it should be avoided, and selecting a safe abstract action, is largely shared across robots. What differs across embodiments is how the abstract safe action is realized: morphology, kinematics, and dynamics determine which actions are safe and feasible. Consequently, the same action can be safe for one robot and unsafe for another. This is especially important for generalist manipulation policies that operate in a common end-effector action space without explicitly capturing how safety depends on the robot's morphology and kinematics. We propose embodiment-conditioned safety filtering, in which a Hamilton-Jacobi reachability-based value function and its corresponding safety-maximizing policy are shared across robots. Using a morphology-aware latent representation of the robot and its environment, we perform Hamilton-Jacobi reachability analysis directly in latent space so that the learned safety concepts can generalize across embodiments while remaining explicitly conditioned on each robot's morphology and kinematics. We evaluate our approach across five bimanual robot embodiments and five manipulation tasks with whole-body collision-avoidance constraints. Our results show that a single policy, jointly trained across five manipulation tasks and four embodiments, exhibits zero-shot generalization to a held-out embodiment, reducing the nominal policy's collision rate. They also show that training using more embodiments improves generalization.

</details>

---

### [[20_Research/Papers/具身智能/KeyGen_Unsupervised_Keypoint_based_Object-Centric_Representations_for_Category-Level_Policy_Generalization|KeyGen: Unsupervised Keypoint based Object-Centric Representations for Category-Level Policy Generalization]]

![[assets/2609.28818_figure.png|800]]

- **arXiv**: [2609.28818](https://arxiv.org/abs/2609.28818)
- **PDF**: https://arxiv.org/pdf/2609.28818
- **详细分析**: [[20_Research/Papers/具身智能/KeyGen_Unsupervised_Keypoint_based_Object-Centric_Representations_for_Category-Level_Policy_Generalization|KeyGen: Unsupervised Keypoint based Object-Centric Representations for Category-Level Policy Generalization]]
- **作者**: Shuxin Cao, Liquan Wang, Masoud Moghani, Benjamin Joffe, Animesh Garg
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《KeyGen: Unsupervised Keypoint based Object-Centric Representations for Category-Level Policy Generalization》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, ShapeNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalization in robotic manipulation requires policies to perform tasks across diverse unseen object instances that vary in shape, size, and pose. However, conventional behavior cloning (BC) methods often overfit to instance-specific geometry and appearance, limiting transfer to novel objects. We introduce KeyGen, a framework that learns canonicalized semantic 3D keypoints from point clouds and uses them as structured object-centric representations for policy learning. A visuomotor diffusion policy conditions on these keypoints together with object-centric geometry to predict full manipulation trajectories, enabling consistent geometric correspondence across object instances. To evaluate category-level generalization, we construct a photorealistic simulation benchmark with three manipulation tasks and a planning-driven data generation pipeline that produces expert trajectories across diverse object instances. Experiments show that KeyGen significantly outperforms prior methods on both seen and unseen objects under pose variation, scales effectively with additional demonstrations per object, maintains robustness to object rescaling, and achieves strong performance in both simulation and real-world manipulation.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_with_Verifiable_Rewards_for_Small_Search_Agents|Reinforcement Learning with Verifiable Rewards for Small Search Agents]]

![[assets/2609.28765_figure.png|800]]

- **arXiv**: [2609.28765](https://arxiv.org/abs/2609.28765)
- **PDF**: https://arxiv.org/pdf/2609.28765
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_with_Verifiable_Rewards_for_Small_Search_Agents|Reinforcement Learning with Verifiable Rewards for Small Search Agents]]
- **作者**: Gaurisankar Jayadas, Aske Plaat, Álvaro Serra-Gómez, Sandheep P
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.3，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Reinforcement Learning with Verifiable Rewards for Small Search Agents》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：JustRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) performs well on problems with clear rewards, such as mathematics and coding, but whether it also works where the reward is less clear remains open. The reason-over-search recipe applies RLVR to open-domain question answering, where retrieval grounds the answer and a match against the reference supplies the reward. So far it has been demonstrated on large models, and below one billion parameters only with distillation from a larger teacher. We test the recipe on a small model. We train Qwen3.5-0.8B with Group Relative Policy Optimization (GRPO) and an interleaved Wikipedia-search tool on MuSiQue, varying only the reward across three shapes over three seeds each, and we evaluate every checkpoint held-out on a seven-benchmark question-answering suite. The recipe works: the best run reaches 0.352 average exact match against a 0.092 untrained floor, a 3.8-fold gain, with no distillation step in the training loop. The reward shape also matters. The Search-R1-faithful exact-match-only reward is the worst of the three at every seed at the matched training horizon, and it is worst even on exact match, the metric it directly optimises. We conclude that the sparse exact-match reward, RLVR's default in mathematics and code, is the wrong starting point for models of this size. The reason-over-search setting can supply a suitable reward for RLVR on small models, but small-model RLVR needs its own reward-design study rather than a scaled-down copy of a large-model recipe.

</details>

---

### [[20_Research/Papers/强化学习/Policy_Complexity,_Reaction_Time,_and_Bounded_Rationality_in_Reinforcement_Learning|Policy Complexity, Reaction Time, and Bounded Rationality in Reinforcement Learning]]

![[assets/2609.28737_first_page.png|800]]

- **arXiv**: [2609.28737](https://arxiv.org/abs/2609.28737)
- **PDF**: https://arxiv.org/pdf/2609.28737
- **详细分析**: [[20_Research/Papers/强化学习/Policy_Complexity,_Reaction_Time,_and_Bounded_Rationality_in_Reinforcement_Learning|Policy Complexity, Reaction Time, and Bounded Rationality in Reinforcement Learning]]
- **作者**: James Wu, Chris R. Sims
- **cs 子类**: cs.AI, cs.IT, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Policy Complexity, Reaction Time, and Bounded Rationality in Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Biological agents do not learn under conditions of unlimited computation. For humans, learning and choice are shaped by constraints on perception, attention, and working memory, which limit how much state information guides behavior and therefore bound policy complexity. Standard reinforcement learning models typically optimize reward without explicitly representing these internal costs, making them less suitable as models of biological intelligence. We derive MI-SARSA, an on-policy temporal-difference algorithm that incorporates mutual-information regularization through a learned marginal action prior and a penalty on state-specific deviations from that prior. This yields a sequential learning model in which state information is used selectively when its expected return benefit justifies the added informational cost. Critically, the same state-specific information cost that governs policy compression also generates trial-level predictions for reaction time, distinguishing MI-SARSA from most reinforcement learning models, which predict choices or returns but not latency. Empirically, MI-SARSA produces a reward-complexity tradeoff, and stronger information penalties produce simpler policies with lower control costs and faster reaction times. Under environment shift, increasing regularization reduces post-switch performance degradation but also lowers asymptotic return, revealing a robustness-capacity tradeoff. Together, these results position MI-SARSA as a model of bounded sequential learning under cognitive constraints.

</details>

---

### [[20_Research/Papers/机器人/Temporal_Learning_for_End-Effector_Position_Estimation_under_Aerodynamic_Disturbances_in_Aerial_Continuum_Manipulation|Temporal Learning for End-Effector Position Estimation under Aerodynamic Disturbances in Aerial Continuum Manipulation]]

![[assets/2609.28716_figure.png|800]]

- **arXiv**: [2609.28716](https://arxiv.org/abs/2609.28716)
- **PDF**: https://arxiv.org/pdf/2609.28716
- **详细分析**: [[20_Research/Papers/机器人/Temporal_Learning_for_End-Effector_Position_Estimation_under_Aerodynamic_Disturbances_in_Aerial_Continuum_Manipulation|Temporal Learning for End-Effector Position Estimation under Aerodynamic Disturbances in Aerial Continuum Manipulation]]
- **作者**: Niloufar Amiri, Houman Masnavi, Farrokh Janabi-Sharifi
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Temporal Learning for End-Effector Position Estimation under Aerodynamic Disturbances in Aerial Continuum Manipulation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper investigates temporal neural networks for \mbox{end-effector} position \mbox{estimation} of an aerial continuum manipulator (ACM) operating under aerodynamic effects induced by the unmanned aerial vehicle (UAV). An experimental dataset is collected under stationary (\mbox{rotor-off}) and \mbox{free-hovering} conditions across continuum robot (CR) configurations and UAV altitudes, providing \mbox{end-effector} position measurements with and without aerodynamic residuals. To establish a nominal framework, \mbox{strain-parameterized} kinematic models with progressively richer strain bases are evaluated to balance model complexity and prediction accuracy. The selected nominal model then serves as the baseline for 3D position residual estimation using a \mbox{closed-form} \mbox{continuous-time} (CfC) neural network, with a multilayer perceptron (MLP) and a gated recurrent unit (GRU) used for comparison. On unseen test experiments, the CfC achieves an RMSE of \(22.00\pm1.70~\mathrm{mm}\) over five random seeds, compared with \(36.38\pm3.58~\mathrm{mm}\) for the MLP and \(27.72\pm2.92~\mathrm{mm}\) for the GRU, corresponding to reductions of \(39.52\%\) and \(20.62\%\), respectively. These results demonstrate the effectiveness of \mbox{continuous-time} learning for \mbox{end-effector} position estimation under aerodynamic disturbances relative to static and \mbox{discrete-time} learning methods.

</details>

---

### [[20_Research/Papers/大模型/Progressive_Skill_Discovery_as_Access_Control_for_Tool-Using_LLM_Agents_Structural_Governance_through_Role-Scoped_Capability_Delivery|Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery]]

![[assets/2609.28693_first_page.png|800]]

- **arXiv**: [2609.28693](https://arxiv.org/abs/2609.28693)
- **PDF**: https://arxiv.org/pdf/2609.28693
- **详细分析**: [[20_Research/Papers/大模型/Progressive_Skill_Discovery_as_Access_Control_for_Tool-Using_LLM_Agents_Structural_Governance_through_Role-Scoped_Capability_Delivery|Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery]]
- **作者**: Michael Stettler, Benjamin Girardet, Jonas Canton, Nicolas Corod
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents struggle to scale safely when exposed to vast enterprise toolsets. Providing an agent with access to every internal tool leads to oversized context windows, degraded tool selection, and severe governance vulnerabilities - as system policies defined purely in prompts remain probabilistic advice rather than hard constraints. Existing mitigations, such as multi-agent domain delegation, decentralize audit logs and fail to guarantee policy compliance across sessions. We introduce skilder, a framework that packages capabilities into roles: bundles of skills, tools, and instructions, together with the limits that bound them. An agent begins with a minimal role catalog, learns the roles a task requires, and receives each role's skills, instructions, and tools through a single MCP server. Because tools reach the agent only inside learned skills, the same server enforces the scope of what was learned deterministically. We evaluate skilder against flat-context tool selection and multi-agent orchestration across 13 tasks using six models (10 runs each). Our results show that, when models completed discovery and issued a governed call, the skilder simulated authorization layer enforced governance boundaries: no unauthorized tool call or parameter violation (e.g., a spending-limit breach) executed. Aggregate task pass rates also reflect whether each model followed the discovery protocol and satisfied response-quality checks; those misses are not authorization failures. Furthermore, by allowing agents to dynamically acquire cross-role capabilities mid-task, skilder preserves problem-solving flexibility while providing hard system-level enforcement.

</details>

---

### [[20_Research/Papers/世界模型/Beyond_Static_Graph_World_Models_Learning_Stochastic_Latent_Dynamics_over_Evolving_Topologies|Beyond Static Graph World Models: Learning Stochastic Latent Dynamics over Evolving Topologies]]

![[assets/2609.28670_figure.png|800]]

- **arXiv**: [2609.28670](https://arxiv.org/abs/2609.28670)
- **PDF**: https://arxiv.org/pdf/2609.28670
- **详细分析**: [[20_Research/Papers/世界模型/Beyond_Static_Graph_World_Models_Learning_Stochastic_Latent_Dynamics_over_Evolving_Topologies|Beyond Static Graph World Models: Learning Stochastic Latent Dynamics over Evolving Topologies]]
- **作者**: Alex Schutz, Nick Hawes, Victor-Alexandru Darvariu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 2.12（加权：强化学习 0.16，世界模型 1.96）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Beyond Static Graph World Models: Learning Stochastic Latent Dynamics over Evolving Topologies》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Graph-based world models have recently emerged as a means of learning transitions over relational state representations. However, existing approaches are largely limited to fixed-topology graphs or deterministic, fully observable environments. We propose the Graph Dynamics Model (GDM), a world model for graph-structured observations that is designed to handle the more general setting of evolving topologies in stochastic and partially observable environments. The GDM uses a sparse recurrent adjacency matrix to model topology updates and perform message passing, together with a recurrent state-space architecture for modelling stochastic transitions. Furthermore, we identify a gap in the evaluation of graph-based world models, as existing methods do not provide a means of comparing predicted and true distributions over the joint graph state comprising the interdependent topology, node features, and graph features. We therefore introduce the Graph Distribution Distance (GDD) metric, which uses maximum mean discrepancy with a graph kernel to comprehensively compare joint next-state distributions. We evaluate the GDM across several environments, including stochastic and partially observable settings. We demonstrate that GDM outperforms baseline models and displays zero-shot generalisation on large graphs.

</details>

---

### [[20_Research/Papers/世界模型/Training_Object_Permanence_in_World_Models|Training Object Permanence in World Models]]

![[assets/2609.28654_figure.png|800]]

- **arXiv**: [2609.28654](https://arxiv.org/abs/2609.28654)
- **PDF**: https://arxiv.org/pdf/2609.28654
- **详细分析**: [[20_Research/Papers/世界模型/Training_Object_Permanence_in_World_Models|Training Object Permanence in World Models]]
- **作者**: Haotian Zhang, Fengyuan Yu, Dezhi Luo, Haoran Sun, Zehong Zhao, Qingying Gao, Yihan Li, Siyuan An, Huayi Qin, Yilan Zhang, Zhengze Jiang, Pinyuan Feng...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《Training Object Permanence in World Models》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object permanence and solidity are hallmarks of human cognitive priors. Recent studies show that video generation models, a paradigmatic class of current world models, have begun to show emerged reasoning abilities, making them ideal candidates for building human-like physical intelligence. Do video models have emerged object permanence in them? If not, could we train them with a core-cognition inspired dataset? We introduce WROP (World Reasoning with Object Permanence), a data infrastructure of 150 hand-designed cognitive science inspired tasks, divided into six cognitive categories. We build Blender generators that randomize speed, lighting, camera angle, and other nuisance parameters while preserving each task's cognitive structure, yielding 10,000+ samples per task. We release a 1.5M-sample training corpus and a 300-question exam. On this exam we evaluate 14 video models: 3 reference-to-video, 7 edit, and 4 continuation, among which PWM-WROP, our 16B world model. In a blind pairwise Elo study, PWM-WROP ranks first among continuation models and third overall, behind only a statistical tie between two reference-to-video models. We release the data, exam, model answers, scores, weights, and PWM, our native-PyTorch training stack on AWS Trainium2.

</details>

---

### [[20_Research/Papers/强化学习/Auditability_Is_Not_One_Property_Rule_Overlap,_Behavioural_Agreement,_and_Composition_in_Reinforcement_Learning|Auditability Is Not One Property: Rule Overlap, Behavioural Agreement, and Composition in Reinforcement Learning]]

![[assets/2609.28581_figure.png|800]]

- **arXiv**: [2609.28581](https://arxiv.org/abs/2609.28581)
- **PDF**: https://arxiv.org/pdf/2609.28581
- **详细分析**: [[20_Research/Papers/强化学习/Auditability_Is_Not_One_Property_Rule_Overlap,_Behavioural_Agreement,_and_Composition_in_Reinforcement_Learning|Auditability Is Not One Property: Rule Overlap, Behavioural Agreement, and Composition in Reinforcement Learning]]
- **作者**: Liu Hung Ming
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Auditability Is Not One Property: Rule Overlap, Behavioural Agreement, and Composition in Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement-learning (RL) policies are often distributed as opaque neural checkpoints, while training logs show that a run occurred without explaining what the policy learned. We study whether independently trained policies can be represented and composed through auditable discrete behavioral rules. We define auditability as six separately testable predicates: trace integrity, lossless coding, rule coverage, behavioral agreement, composition quality, and value-model reliability. Our protocol uses a shared frozen symbolizer, passive rule extraction, an append-only hash-bound ledger, exact environment replay, and offline confidence-ranked arbitration with an explicit blind-spot fallback. The results place strict limits on this description layer. Rule-set overlap does not imply behavioral agreement: policies may share symbolic rules while choosing near-chance-matching actions on fresh states. The fused policy therefore selects among existing rules rather than generating a new skill. On a conflict-dominated task, an apparent fusion failure is traced to an induction/deployment mismatch: rules induced from sampled actions were evaluated under argmax actions, and deployment-consistent re-induction reverses the arbitration ordering. A fitted-Q generalized-policy-improvement diagnostic also fails in both environments, limiting claims that rule fusion is superior to value-based composition. One exploratory comparison favors rule fusion, but its comparator is post hoc, the task is partly saturated, and the fused policy remains below the strongest held-out actor. We contribute an evidence-bounded audit and composition protocol, not a claim of universal interpretability or autonomous skill generation. Future work must add temporally extended skills, cross-skill interfaces, composition search, and independent novelty audits.

</details>

---

### [[20_Research/Papers/大模型/DEEPO_Dual-Entropy_Enhanced_Policy_Optimization_for_Hallucination_in_MLLMs|DEEPO: Dual-Entropy Enhanced Policy Optimization for Hallucination in MLLMs]]

![[assets/2609.28570_figure.png|800]]

- **arXiv**: [2609.28570](https://arxiv.org/abs/2609.28570)
- **PDF**: https://arxiv.org/pdf/2609.28570
- **详细分析**: [[20_Research/Papers/大模型/DEEPO_Dual-Entropy_Enhanced_Policy_Optimization_for_Hallucination_in_MLLMs|DEEPO: Dual-Entropy Enhanced Policy Optimization for Hallucination in MLLMs]]
- **作者**: Yingxuan Zhuang, Miao Pan, Wangjie Gan, Jingxiao Yang, Fan Wang, Weiming Liu, Cheng Tan, Xuhong Zhang, Jintao Chen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《DEEPO: Dual-Entropy Enhanced Policy Optimization for Hallucination in MLLMs》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HallusionBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) is widely used to sharpen reasoning in multimodal large language models (MLLMs), yet its effect on hallucination is uneven. We trace this to two weak points in the \emph{correction chain} from reward to parameter update. At the rollout level, hard queries---those with high semantic entropy---frequently produce unanimously wrong sample groups, collapsing the group-relative advantage to zero exactly where hallucination risk is highest. At the optimization level, confident-but-wrong tokens are gradient-invisible: a categorical policy's expected score-gradient norm vanishes as its distribution sharpens, so the predictions that most need correction receive the weakest updates. We propose Dual-Entropy Enhanced Policy Optimization (DEEPO), a dual-stage enhancement combining signal variance regularization with gradient preconditioning: semantic-entropy-triggered expert prefixes inject grounded continuations on high-uncertainty queries, providing direct supervision and restoring advantage variance, while advantage-sign-aware Renyi preconditioning counteracts logit-level saturation so correction reaches confident errors in the operational confidence regime. Both branches improve over GRPO individually; their interaction is statistically significant on VideoMMMU---the most complex long-horizon task in our evaluation suite (+4.0$, 95\% CI [1.1, 6.9])---and additive elsewhere. DEEPO reduces hallucination while preserving accuracy and training stability.

</details>

---
