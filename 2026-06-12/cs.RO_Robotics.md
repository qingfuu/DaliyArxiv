# cs.RO | Robotics | 2026-06-12

#arxiv #ComputerScience

**论文数**: 25

### [[20_Research/Papers/强化学习/Improving_Robotic_Generalist_Policies_via_Flow_Reversal_Steering|Improving Robotic Generalist Policies via Flow Reversal Steering]]

![[assets/2606.13675_figure.png|800]]

- **arXiv**: [2606.13675](https://arxiv.org/abs/2606.13675)
- **PDF**: https://arxiv.org/pdf/2606.13675
- **详细分析**: [[20_Research/Papers/强化学习/Improving_Robotic_Generalist_Policies_via_Flow_Reversal_Steering|Improving Robotic Generalist Policies via Flow Reversal Steering]]
- **作者**: Andy Tang, William Chen, Andrew Wagenmaker, Chelsea Finn, Sergey Levine
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Improving Robotic Generalist Policies via Flow Reversal Steering》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DSRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist policies can learn a wide range of skills from diverse robot datasets. In order to solve or improve on challenging news tasks, we need a way to infer and invoke the appropriate actions from the policy's rich behavioral prior, especially when directly commanding the policy fails. We focus on flow matching generalists and propose Flow Reversal Steering (FRS): a method that takes suboptimal but ``reasonable'' actions, finds their latent noises by passing them through the flow policy in reverse, and maps them to nearby generalist action modes. We evaluate FRS across many simulated and real-world manipulation settings. First, FRS can turn coarse semantic guidance from humans or vision-language models (VLMs) into corresponding good robot actions, improving zero-shot control. These gains can be distilled with behavioral cloning by training an auxiliary policy to output noises that the generalist maps to good actions -- showing up to 95% absolute task success rate boosts in under a minute of training. Finally, FRS enables policy improvement by bootstrapping reinforcement learning with semantic knowledge, improving on several tasks that standard RL fails to improve on.

</details>

---

### [[20_Research/Papers/具身智能/$_texttt{WEAVER}$,_Better,_Faster,_Longer_An_Effective_World_Model_for_Robotic_Manipulation|$\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation]]

![[assets/2606.13672_figure.png|800]]

- **arXiv**: [2606.13672](https://arxiv.org/abs/2606.13672)
- **PDF**: https://arxiv.org/pdf/2606.13672
- **详细分析**: [[20_Research/Papers/具身智能/$_texttt{WEAVER}$,_Better,_Faster,_Longer_An_Effective_World_Model_for_Robotic_Manipulation|$\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation]]
- **作者**: Arnav Kumar Jain, Yilin Wu, Jesse Farebrother, Gokul Swamy, Andrea Bajcsy
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 4.2（加权：具身智能 1.8，大模型 0.1，世界模型 0.8，机器人 1.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《$\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, WorldGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The potential impacts of world models (WMs, i.e., learned simulators) on robotics are far-reaching -- policy evaluation, policy improvement, and test-time planning -- all with limited real-world interaction. To unlock these downstream capabilities, a WM needs to jointly satisfy three desiderata: $\textit{(i)}$ fidelity (i.e., producing simulated trajectories that correlate with reality), $\textit{(ii)}$ consistency (i.e., producing simulated trajectories that are coherent over long horizons), and $\textit{(iii)}$ efficiency (i.e., producing simulated trajectories quickly). We propose $\texttt{WEAVER}$ (World Estimation Across Views for Embodied Reasoning): a WM architecture that simultaneously achieves all three desiderata, providing state-of-the-art results on robotic manipulation tasks. $\texttt{WEAVER}$ is a multi-view WM trained to predict future latents and reward values via a flow-matching loss. We distill the key design decisions across model architecture, memory, and prediction objectives required to unlock the kinds of long-horizon dynamic manipulation tasks that have confounded prior world modeling approaches. We apply $\texttt{WEAVER}$ in robotic hardware, demonstrating its effectiveness at policy evaluation ($ρ$=0.870 correlation with real-world success rate), policy improvement (real-world success rate improvement of $38\%$ on top of the $π_{0.5}$ robot foundation model), and test-time planning (real-world success rate improvement of $14\%$ with a $5-10\times$ speedup over prior WMs). $\texttt{WEAVER}$ also demonstrates better performance than prior WMs when evaluated on out-of-distribution scenarios. Code, models, and videos at: https://arnavkj1995.github.io/WEAVER/ .

</details>

---

### [[20_Research/Papers/机器人/MCR-Bionic_Hand_Anatomical_Structural_Priors_for_Dexterous_Manipulation|MCR-Bionic Hand: Anatomical Structural Priors for Dexterous Manipulation]]

![[assets/2606.13601_figure.png|800]]

- **arXiv**: [2606.13601](https://arxiv.org/abs/2606.13601)
- **PDF**: https://arxiv.org/pdf/2606.13601
- **详细分析**: [[20_Research/Papers/机器人/MCR-Bionic_Hand_Anatomical_Structural_Priors_for_Dexterous_Manipulation|MCR-Bionic Hand: Anatomical Structural Priors for Dexterous Manipulation]]
- **作者**: Haosen Yang, Guowu Wei
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《MCR-Bionic Hand: Anatomical Structural Priors for Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous robotic hands are usually formulated as high dimensional active control systems governed by degrees of freedom, actuation, and algorithms. Human hand dexterity, however, is partly encoded in the physical architecture of bones, ligaments, tendons, aponeuroses, and intrinsic muscles. This work describes that contribution as two linked forms of structural intelligence: structural prior generation, in which wrist to finger tenodesis, FDS/FDP routing, and the dorsal extensor hood transform low dimensional posture inputs into default grasp configurations and PIP to DIP coordination; and muscle mediated modulation, in which extrinsic muscles, lumbricals, and interossei regulate MCP posture, distal stability, fingertip force paths, and contact states around that default state. Based on this framework, MCR-Bionic Hand is developed as a 1:1 musculoskeletal biomimetic hand integrating a two row eight bone wrist, cross wrist tendons, anatomical flexor routing, volar plate and collateral ligament constraints, the dorsal extensor hood, and intrinsic muscle pathways within one body. Functional demonstrations and geometric mechanical models show that wrist posture induces multi joint pre shaping, the extensor hood maps PIP posture to a coupled DIP response, and intrinsic plus pathways modulate distal stability and fingertip action direction after grasp formation. Contact rich tasks, including coin rotation, pen transfer, dorsal coin flipping, and cube manipulation, show that MCR-Bionic links low dimensional state generation with fine post contact modulation. These results suggest that anatomical biomimetics is valuable not for visual similarity, but for identifying human hand structures that perform part of control.

</details>

---

### [[20_Research/Papers/具身智能/GIVE_Grounding_Human_Gestures_in_Vision-Language-Action_Models|GIVE: Grounding Human Gestures in Vision-Language-Action Models]]

![[assets/2606.13435_figure.png|800]]

- **arXiv**: [2606.13435](https://arxiv.org/abs/2606.13435)
- **PDF**: https://arxiv.org/pdf/2606.13435
- **详细分析**: [[20_Research/Papers/具身智能/GIVE_Grounding_Human_Gestures_in_Vision-Language-Action_Models|GIVE: Grounding Human Gestures in Vision-Language-Action Models]]
- **作者**: Pengfei Liu, Gen Li, Junqiao Fan, Boyu Ma, Jindou Jia, Yang Xiao, Jianfei Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 2.1，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《GIVE: Grounding Human Gestures in Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：IntentionVLA, OpenVLA, RoboNurse-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human communication is inherently multimodal, where language is often accompanied by non-verbal cues such as gestures to convey intentions. However, current Vision-Language-Action (VLA) models treat robotic manipulation as a pure text-driven task, overlooking the important role of gestures in Human-Robot Interaction (HRI). This often leads to inaccurate intent grounding and unreliable manipulation when language instructions are ambiguous or underspecified. To address this challenge, we propose GIVE (Gesture Intent via Visual-Semantic Enhancement), an effective approach that enhances pre-trained VLA models with human gesture understanding without architectural modifications. Specifically, GIVE incorporates gesture information through two complementary pathways: a visual pathway that overlays hand skeletons and fingertip rays onto robot observations for explicit object grounding, and a semantic pathway that generates high-level descriptions of human gestures and task instructions for robust intent grounding. By jointly leveraging visual and semantic guidance, GIVE enables VLA policies to better associate gestures with manipulation behaviors and adapt to dynamic interaction intents. In real-world HRI experiments, GIVE substantially outperforms the baseline, improving target object recognition accuracy by 40% and overall task success rate by 80%, while demonstrating strong robustness and generalization to unseen spatial layouts and diverse participants.

</details>

---

### [[20_Research/Papers/机器人/Low_cost,_easily_manufactured,_highly_flexible_strain_and_touch_sensitive_fiber_for_robotics_applications|Low cost, easily manufactured, highly flexible strain and touch sensitive fiber for robotics applications]]

![[assets/2606.13352_figure.png|800]]

- **arXiv**: [2606.13352](https://arxiv.org/abs/2606.13352)
- **PDF**: https://arxiv.org/pdf/2606.13352
- **详细分析**: [[20_Research/Papers/机器人/Low_cost,_easily_manufactured,_highly_flexible_strain_and_touch_sensitive_fiber_for_robotics_applications|Low cost, easily manufactured, highly flexible strain and touch sensitive fiber for robotics applications]]
- **作者**: Christian Diaz Herrera, Srushti Raste, Simin Liu, Miles Modeste, Jiyang, Yin, Katelyn McCall, Yuxing Jared Yao, Roopkamal Chahal, Simon Chidley, Trung Ha, T. David Westmoreland...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Low cost, easily manufactured, highly flexible strain and touch sensitive fiber for robotics applications》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing stretch and touch sensors for robots are generally expensive with respect to at least one of material costs, required manufacturing equipment, or manufacturing time. We present and experimentally characterize a conductive fiber made using only inexpensive commercial off-the-shelf parts (conductive thread at $0.07/ft, silicone tubing at $0.94/ft) and tools (loop-style needle threader at $2), which can be manufactured quickly (20 cm length in 2 minutes.) We demonstrate its use as a resistive strain sensor with three applications: Triggering a grasp in a pneumatically actuated assistive finger, sensing the pose of a pneumatically actuated robotic strap, and estimating the pose of a flexible solid. We also demonstrate that it can be used as a capacitive sensor with two applications: First, as a touch sensor which triggers a commercial robot arm to move, and second, as a near-field sensor enabling the robot arm to follow a moving hand. The capacitive sensors are knitted, showcasing the high flexibility of the fiber. We discuss methods for improving manufacturing scalability and their cost trade-offs. Finally, we demonstrate a method for repairing a cut fiber.

</details>

---

### [[20_Research/Papers/机器人/EMG-Based_Adaptation_of_Anisotropic_Virtual_Fixtures_for_Robot-Assisted_Surgical_Resection_and_Dissection|EMG-Based Adaptation of Anisotropic Virtual Fixtures for Robot-Assisted Surgical Resection and Dissection]]

![[assets/2606.13340_figure.png|800]]

- **arXiv**: [2606.13340](https://arxiv.org/abs/2606.13340)
- **PDF**: https://arxiv.org/pdf/2606.13340
- **详细分析**: [[20_Research/Papers/机器人/EMG-Based_Adaptation_of_Anisotropic_Virtual_Fixtures_for_Robot-Assisted_Surgical_Resection_and_Dissection|EMG-Based Adaptation of Anisotropic Virtual Fixtures for Robot-Assisted Surgical Resection and Dissection]]
- **作者**: Dario Onfiani, Michael Dyck, Luigi Biagiotti, Julian Klodmann
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《EMG-Based Adaptation of Anisotropic Virtual Fixtures for Robot-Assisted Surgical Resection and Dissection》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we address the development of an adaptive assistance system for robot-assisted laparoscopic surgery, specifically for delicate tasks such as Resection and Dissection. Even if Virtual Fixtures offer significant advantages for guiding a surgeon's movements, conventional Virtual Fixtures are often defined by fixed geometries, lacking the flexibility to adapt to the surgical workflow or the surgeon's immediate intent. To address these limitations, we propose a novel framework for an adaptive and anisotropic virtual fixture. In addition, we introduce an intuitive control interface that modulates the fixture's geometry in real-time based on the surgeon's intent, inferred from EMG signals. This approach allows the surgeon to dynamically expand or disengage the constraint by contracting their forearm muscles, enabling seamless transitions between precise guided motion and free repositioning of the tool. Experimental results from a pilot user study, based on a standardized surgical training task, demonstrate the effectiveness of the proposed method. The system showed significant improvements in task accuracy and movement consistency, alongside a reduction in perceived cognitive load, effort, and frustration.

</details>

---

### [[20_Research/Papers/具身智能/See_Selectively,_Act_Adaptively_Dual-Level_Structural_Decomposition_for_Bimanual_Robot_Manipulation|See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation]]

![[assets/2606.13279_first_page.png|800]]

- **arXiv**: [2606.13279](https://arxiv.org/abs/2606.13279)
- **PDF**: https://arxiv.org/pdf/2606.13279
- **详细分析**: [[20_Research/Papers/具身智能/See_Selectively,_Act_Adaptively_Dual-Level_Structural_Decomposition_for_Bimanual_Robot_Manipulation|See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation]]
- **作者**: Yoon-Ji Choi, Young-Chae Son, Soo-Chul Lim
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In bimanual robotic manipulation, task-relevant visual information varies with the task stage and context, while the interaction of the two arms shifts between independent and coordinated modes, making policy learning challenging. However, existing monolithic Vision-Language-Action (VLA) policies process diverse visual inputs and interaction patterns through a single shared representation and action generation pathway, often failing to separately account for visual relevance and bimanual interaction structure. To address this issue, we propose a bimanual manipulation VLA framework based on Dual-Level Structural Decomposition. The View-Selective Visual Router dynamically adjusts wrist-view contributions to emphasize relevant visual cues, while the Interaction-Aware Action Mixture-of-Experts (MoE) decomposes action generation into coordinated and arm-wise pathways to adapt to varying bimanual interaction modes. We evaluate the proposed method on six simulated bimanual manipulation tasks in RoboTwin 2.0 and three long-horizon real-world tasks. Our model improves the overall average success rate over a monolithic baseline by 27.7% in simulation and 43.3% in real-world evaluation, while consistently outperforming single-module variants across both settings. These results demonstrate that jointly considering selective visual processing and explicit decomposition of bimanual interaction structures provides an effective inductive bias for robust bimanual manipulation.

</details>

---

### [[20_Research/Papers/强化学习/WT-UMI_Tactile-based_Whole-Body_Manipulation_via_Force-Supervised_Contact-Aware_Planning|WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning]]

![[assets/2606.13232_first_page.png|800]]

- **arXiv**: [2606.13232](https://arxiv.org/abs/2606.13232)
- **PDF**: https://arxiv.org/pdf/2606.13232
- **详细分析**: [[20_Research/Papers/强化学习/WT-UMI_Tactile-based_Whole-Body_Manipulation_via_Force-Supervised_Contact-Aware_Planning|WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning]]
- **作者**: Jaehwi Jang, Zhaoyuan Gu, Alfred Cueva, Zimeng Chai, Junjie Sheng, Thong Nguyen, Himank Galundia, Yifan Wu, Huishu Xue, Isaac Legene, Ojas Mediratta, Davin Doan...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Whole-body humanoid manipulation of bulky, deformable, and shared-load objects requires distributed contact sensing and explicit force regulation, yet most imitation policies treat contact force only implicitly. On the other hand, different demonstration sources provide complementary modalities with inherent trade-offs: human demonstrations capture natural contact forces but not robot-executable actions, while teleoperation directly records robot actions but with less natural force regulation. This paper presents \textbf{WT-UMI}, a wearable whole-body tactile interface worn by human operators or mounted on humanoids, providing accurate observations of tactile images, contact forces, and end-effector poses across both human demonstration and humanoid teleoperation modes. We introduce a force-conditioned target-pose correction module that converts measured human poses into contact-aware robot targets by learning corrections from teleoperation data. To leverage the natural force interaction in human data, we propose a force-supervised planner that predicts end-effector pose chunks and contact-force trajectories. The predicted contact force serves as the reference for a tactile-based admittance controller. Across five contact-rich tasks spanning deformable objects, bulky rigid objects, and human--humanoid collaboration, WT-UMI improves success rate and reduces contact-position tracking error over four policy baselines. Our project page is available at https://wt-umi.github.io/WTUMI/.

</details>

---

### [[20_Research/Papers/机器人/Embedding_ISO_10218_Safety_Compliance_in_Robots_via_Control_Barrier_Functions_for_Human-Robot_Collaboration|Embedding ISO 10218 Safety Compliance in Robots via Control Barrier Functions for Human-Robot Collaboration]]

![[assets/2606.13203_figure.png|800]]

- **arXiv**: [2606.13203](https://arxiv.org/abs/2606.13203)
- **PDF**: https://arxiv.org/pdf/2606.13203
- **详细分析**: [[20_Research/Papers/机器人/Embedding_ISO_10218_Safety_Compliance_in_Robots_via_Control_Barrier_Functions_for_Human-Robot_Collaboration|Embedding ISO 10218 Safety Compliance in Robots via Control Barrier Functions for Human-Robot Collaboration]]
- **作者**: Federico Parma, Cesare Tonola, Nicola Pedrocchi, Manuel Beschi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Embedding ISO 10218 Safety Compliance in Robots via Control Barrier Functions for Human-Robot Collaboration》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-Robot Collaboration (HRC) requires strict adherence to safety standards, such as ISO 10218, to prevent harmful interactions. Standard Speed and Separation Monitoring (SSM) filters calculate safe robotic speeds based on conservative assumptions, such as constant human velocity, which prevents accurate predictions of minimum separation distances and causes unnecessary operational halts. This paper proposes a Control Barrier Function (CBF) that explicitly incorporates human acceleration data to analytically forward-predict the minimum human-robot separation distance during a worst-case robotic stopping trajectory. To guarantee safety at the control level, this predictive CBF is integrated as an inequality constraint within a Sequential Quadratic Programming (SQP) framework. Specifically, two methods are proposed: Method I, a CBF-constrained PD safety filter; and Method II, a task-scaling SQP controller that enforces a spatial tube constraint. Simulated and real-world experiments on a UR10e robot evaluate the two proposed methods against a standard industrial SSM module baseline. Results demonstrate that Method II dynamically modulates execution speed and confines spatial deviations. Compared to Method I, Method II achieves a 63\% reduction in mean trajectory error and avoids excessive evasive manoeuvres, ensuring high task throughput while complying with ISO 10218 SSM guidelines.

</details>

---

### [[20_Research/Papers/强化学习/Redesigning_Regularization_for_Effective_Policy_Smoothing|Redesigning Regularization for Effective Policy Smoothing]]

![[assets/2606.13169_figure.png|800]]

- **arXiv**: [2606.13169](https://arxiv.org/abs/2606.13169)
- **PDF**: https://arxiv.org/pdf/2606.13169
- **详细分析**: [[20_Research/Papers/强化学习/Redesigning_Regularization_for_Effective_Policy_Smoothing|Redesigning Regularization for Effective Policy Smoothing]]
- **作者**: Taisuke Kobayashi, Naoto Yamanaka
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.8（加权：具身智能 0.9，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Redesigning Regularization for Effective Policy Smoothing》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LipsNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper proposes a novel regularization design to effectively smooth policy functions in reinforcement learning. While regularization that enhances ``global'' Lipschitz continuity was initially considered, it has been limited to ``local'' Lipschitz continuity due to a tradeoff between smoothness and expressiveness. However, it has become apparent that the original implementation is cumbersome and does not provide sufficient smoothing, leading to a preference for simpler implementations. This stems from a discrepancy between theory and implementation, and a more appropriate implementation can expect to facilitate smoothing. Therefore, this paper identifies three reasons why the original implementation does not function adequately and provide remedies for them. This modified regularization performs well across multiple tasks and algorithms, successfully achieving smooth motion while improving control performance. Furthermore, by applying it to sim-to-real reinforcement learning for a quadruped robot, it is demonstrated that smooth motion provides robustness against sudden changes in target velocity commands.

</details>

---

### [[20_Research/Papers/强化学习/FTP-1_A_Generalist_Foundation_Tactile_Policy_Across_Tactile_Sensors_for_Contact-Rich_Manipulation|FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation]]

![[assets/2606.13102_figure.png|800]]

- **arXiv**: [2606.13102](https://arxiv.org/abs/2606.13102)
- **PDF**: https://arxiv.org/pdf/2606.13102
- **详细分析**: [[20_Research/Papers/强化学习/FTP-1_A_Generalist_Foundation_Tactile_Policy_Across_Tactile_Sensors_for_Contact-Rich_Manipulation|FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation]]
- **作者**: Chengbo Yuan, Zicheng Zhang, Mingjie Zhou, Wendi Chen, Yi Wang, Zhuoyang Liu, Dantong Niu, Shuo Wang, Hui Zhang, Wenkang Zhang, Yingdong Hu, Yuanqing Gong...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Tactile-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite the success of vision-based generalist robotic policies, existing tactile-based policies remain tied to fixed embodiments and sensor setups. This is because tactile signals are highly heterogeneous across hardware, making cross-sensor generalization difficult. We present FTP-1,the first generalist foundation tactile policy pretrained to acquire transferable tactile manipulation abilities across diverse sensors and embodiments. FTP-1 supports varied tactile inputs, including image-, array-, and state-based signals, by using heterogeneous encoders to project them into unified morphology-aware latent tokens that are jointly modeled by a shared tactile Transformer expert. Pretrained on around 3,000 hours of tactile manipulation data aggregated from 26 data sources, spanning human and robot demonstrations across 21 sensors, FTP-1 learns tactile skills that transfer beyond the sensors seen during pretraining. Across downstream finetuning experiments spanning 5 hardware configurations, FTP-1 improves contact-rich manipulation on seen sensor setups by +17.2% and, surprisingly, transfers to two previously unseen tactile-sensor setups, achieving a +31% gain in success rate. FTP-1 establishes the first unified foundation baseline for tactile manipulation, providing future tactile policies with a shared model-level starting point. Pretrained models, datasets, training code and more visualization at https://ftp1-policy.github.io.

</details>

---

### [[20_Research/Papers/具身智能/Y-BotFrame_An_Extensible_Embodied_Agent_Framework_for_Quadruped_Robot_Assistants|Y-BotFrame: An Extensible Embodied Agent Framework for Quadruped Robot Assistants]]

![[assets/2606.13049_figure.png|800]]

- **arXiv**: [2606.13049](https://arxiv.org/abs/2606.13049)
- **PDF**: https://arxiv.org/pdf/2606.13049
- **详细分析**: [[20_Research/Papers/具身智能/Y-BotFrame_An_Extensible_Embodied_Agent_Framework_for_Quadruped_Robot_Assistants|Y-BotFrame: An Extensible Embodied Agent Framework for Quadruped Robot Assistants]]
- **作者**: Luyao Zhang, Ke Li, Yuan Ding, Xulong Zhao, Guo Yu, Chengwei Yan, Fuyu Dong, Jiawei Hu, Di Wang, Nan Luo, Gang Liu, Quan Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 5.3（加权：具身智能 2.7，大模型 0.7，机器人 1.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Y-BotFrame: An Extensible Embodied Agent Framework for Quadruped Robot Assistants》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadruped robots are capable of traversing a wide range of complex terrains with high flexibility. As highly mobile ground-based intelligent platforms, they can be equipped with modules for navigation control, environmental perception, and intelligent interaction, thereby serving as real-world mobile deployment platforms for various algorithms. In this paper, we introduce Y-BotFrame, an extensible embodied platform that turns a robot into an intelligent ground assistant. Y-BotFrame integrates multimodal perception capabilities, including speech, vision, and LiDAR, and employs a large language model as the cognitive core for environmental understanding, contextual reasoning, and task planning. The system maps user natural-language instructions into executable embodied task units that can be carried out by the robot. Y-BotFrame supports natural interaction through voice commands and visual feedback, removing the need for a remote controller and enabling efficient human-robot collaboration. With a highly extensible framework, Y-BotFrame supports plug-and-play integration of new functional modules as well as modular upgrades and iterative development, offering a reference implementation for the real-world deployment of general-purpose, instruction-driven embodied agents.The supplementary video is available at https://xdei-group.github.io/Y-BotFrame/.

</details>

---

### [[20_Research/Papers/具身智能/RoboProcessBench_Benchmarking_Process-Aware_Understanding_in_Vision-Language_Robotic_Manipulation|RoboProcessBench: Benchmarking Process-Aware Understanding in Vision-Language Robotic Manipulation]]

![[assets/2606.13040_figure.png|800]]

- **arXiv**: [2606.13040](https://arxiv.org/abs/2606.13040)
- **PDF**: https://arxiv.org/pdf/2606.13040
- **详细分析**: [[20_Research/Papers/具身智能/RoboProcessBench_Benchmarking_Process-Aware_Understanding_in_Vision-Language_Robotic_Manipulation|RoboProcessBench: Benchmarking Process-Aware Understanding in Vision-Language Robotic Manipulation]]
- **作者**: Dayu Xia, Yue Shi, Yao Mu, Huiting Ji, Chaofan Ma, Yingjie Zhou, Hua Chen, Yang Liu, Jiezhang Cao, Guangtao Zhai
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RoboProcessBench: Benchmarking Process-Aware Understanding in Vision-Language Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ProcessData-Eval, RoboProcessBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) are increasingly explored as visual critics, reward generators, and failure detectors in robotic manipulation. These roles implicitly require models to judge not only final task success, but also how a manipulation execution is physically and temporally progressing. However, existing evaluations fail to test whether VLMs possess fine-grained process understanding. To address this gap, we present RoboProcessBench, a benchmark for process-aware understanding in vision-language robotic manipulation. RoboProcessBench decomposes such capability into two complementary dimensions, \emph{static monitoring} and \emph{dynamic reasoning}, instantiated as 12 diagnostic question families covering phase, contact, motion, coordination, primitive-local progress, temporal order, outcome, and primitive-level transitions. Built from physically grounded execution traces, the curated benchmark corpus ProcessData contains \textasciitilde 58k question-answer pairs across 260 manipulation tasks, which is further split into ProcessData-SFT and ProcessData-Eval for post-training and evaluation purposes. Extensive evaluation of various VLMs on ProcessData-Eval reveals broad limitations across 12 diagnostic task families, suggesting current models still lack robust process-aware understanding of manipulation executions. But with ProcessData-SFT, the post-trained \textit{Qwen2.5-VL-7B} and \textit{InternVL-3-8B} exhibit consistent gains on local state, motion, progress, and primitive-aware cues. These results demonstrate that RoboProcessBench serves as both an evaluation benchmark and a learnable supervision source for developing VLMs capable of monitoring and evaluating robotic manipulation processes. Project webpage: \href{https://processbench-2026.github.io/RoboProcessBench-Web/}{https://processbench-2026.github.io}.

</details>

---

### [[20_Research/Papers/具身智能/GenHOI_Contact-Aware_Humanoid-Object_Interaction_by_Imitating_Generated_Videos_without_Task-Specific_Training|GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training]]

![[assets/2606.12995_figure.jpg|800]]

- **arXiv**: [2606.12995](https://arxiv.org/abs/2606.12995)
- **PDF**: https://arxiv.org/pdf/2606.12995
- **详细分析**: [[20_Research/Papers/具身智能/GenHOI_Contact-Aware_Humanoid-Object_Interaction_by_Imitating_Generated_Videos_without_Task-Specific_Training|GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training]]
- **作者**: Zhihai Bi, Qiang Zhang, Guoyang Zhao, Jiahang Cao, Xueyin Luo, Yushan Zhang, Jinglan Xu, Ruoyu Geng, Yulin Li, Andrew F. Luo, Jun Ma
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid-Object Interaction (HOI) is a fundamental capability for humanoid robots, yet it remains challenging due to the tight coupling between dynamic balance and stable interaction with diverse objects. Existing methods often require time-consuming task-specific policy training or rely on rigid trajectory replay, which limits their ability to accommodate novel interaction scenarios. In this work, we present \textit{GenHOI}, a simple yet effective framework that enables humanoid robots to perform diverse object-interaction tasks in a zero-shot manner by directly imitating a single generated video, without task-specific training or physical demonstration data. GenHOI first reconstructs the robot-object scene in simulation and renders a first-frame image, which, together with the language command, conditions the synthesis of a task-oriented interaction video. The generated video is then analyzed to identify interaction-relevant contact events and estimate hand-object contact regions, which are encoded as object-centric geometric constraints that convert visual interaction cues into physically grounded optimization priors. Guided by these priors, the reference motion recovered from the video is refined and smoothed to resolve the scale ambiguity inherent in 2D video generation, while adapting a single reference trajectory to unseen robot-object relative poses. The optimized trajectory is finally executed by a closed-loop tracking controller. We validate the proposed framework in extensive simulation and real-world experiments across diverse object-interaction tasks, including box grasping, asymmetric bimanual chair carrying, table lifting from below, and cylindrical-object enveloping.

</details>

---

### [[20_Research/Papers/强化学习/EmbodiSteer_Steering_Embodiment-Agnostic_Visuomotor_Policies_with_Joint-Space_Guidance_for_Zero-Shot_Cross-Embodiment_Deployment|EmbodiSteer: Steering Embodiment-Agnostic Visuomotor Policies with Joint-Space Guidance for Zero-Shot Cross-Embodiment Deployment]]

![[assets/2606.12965_figure.png|800]]

- **arXiv**: [2606.12965](https://arxiv.org/abs/2606.12965)
- **PDF**: https://arxiv.org/pdf/2606.12965
- **详细分析**: [[20_Research/Papers/强化学习/EmbodiSteer_Steering_Embodiment-Agnostic_Visuomotor_Policies_with_Joint-Space_Guidance_for_Zero-Shot_Cross-Embodiment_Deployment|EmbodiSteer: Steering Embodiment-Agnostic Visuomotor Policies with Joint-Space Guidance for Zero-Shot Cross-Embodiment Deployment]]
- **作者**: Shihefeng Wang, Kangchen Lv, Mingrui Yu, Xiang Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《EmbodiSteer: Steering Embodiment-Agnostic Visuomotor Policies with Joint-Space Guidance for Zero-Shot Cross-Embodiment Deployment》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scalable robot imitation learning relies on large-scale heterogeneous data from diverse robots or body-free data, making Cartesian end-effector actions a key interface for embodiment-agnostic policy learning. However, end-effector-only abstraction leaves Cartesian policies unaware of the deployed robot body, making them brittle under robot-specific constraints such as whole-body collision avoidance. To overcome this limitation, we present EmbodiSteer, a training-free framework that steers embodiment-agnostic visuomotor policies toward zero-shot, embodiment-aware deployment. EmbodiSteer keeps policy learning in Cartesian space while efficiently lifting inference-time diffusion sampling into the target robot's joint space via forward kinematics and Jacobian-based updates. With whole-body collision-aware guidance over joint trajectories after each denoising step, the arm can be steered away from collisions while preserving learned end-effector behavior. Compared with Cartesian-only execution, EmbodiSteer reduces collision rate by 46.1% and improves task success rate by 28.5% across 9 simulated robots, and further achieves 90.0% collision rate reduction and 36.7% success rate increase on two physical robots in highly constrained scenarios. Our project page is at https://frankwang67.github.io/EmbodiSteer-Page.

</details>

---

### [[20_Research/Papers/具身智能/SERF_Spatiotemporal_Environment_and_Robot_Feature_Map_for_Long-Horizon_Mobile_Manipulation|SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation]]

![[assets/2606.12956_figure.jpg|800]]

- **arXiv**: [2606.12956](https://arxiv.org/abs/2606.12956)
- **PDF**: https://arxiv.org/pdf/2606.12956
- **详细分析**: [[20_Research/Papers/具身智能/SERF_Spatiotemporal_Environment_and_Robot_Feature_Map_for_Long-Horizon_Mobile_Manipulation|SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation]]
- **作者**: Sunghwan Kim, Byeonghyun Pak, Kehan Long, Yulun Tian, Nikolay Atanasov
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robot mobile manipulation requires continual reasoning about localization, environment changes, and task progress, all of which are challenging to infer from image observations alone. In this paper, we show that conditioning a mobile manipulation policy on a spatiotemporal feature map improves reasoning over long horizons. The map represents the environment and the articulated robot body as neural points in a shared latent space and is updated online from egocentric observations and proprioceptive state. We update the environment neural points using object-level rigid tracking and the robot neural points using forward kinematics. We use our spatiotemporal environment and robot feature (SERF) map as a state input to a vision-language-action (VLA) model by extracting map tokens from multiple reference frames and spatial scales, providing the policy with both local and global context. We demonstrate SERF on BEHAVIOR-1K, a benchmark for long-horizon mobile manipulation in household environments. Experiments show that the SERF VLA policy outperforms image-only baselines, reaches subgoals faster by following more direct trajectories, improves robustness to scene-configuration shifts, and recovers from object-drop failures.

</details>

---

### [[20_Research/Papers/具身智能/Towards_Reliable_Sequential_Object_Picking_in_Clutter_The_Runner-up_Solution_to_RGMC_2025|Towards Reliable Sequential Object Picking in Clutter: The Runner-up Solution to RGMC 2025]]

![[assets/2606.12954_first_page.png|800]]

- **arXiv**: [2606.12954](https://arxiv.org/abs/2606.12954)
- **PDF**: https://arxiv.org/pdf/2606.12954
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Reliable_Sequential_Object_Picking_in_Clutter_The_Runner-up_Solution_to_RGMC_2025|Towards Reliable Sequential Object Picking in Clutter: The Runner-up Solution to RGMC 2025]]
- **作者**: Wei Yu, Xidan Zhang, Ziyi Zheng, Weijie Kong, Huixu Dong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Towards Reliable Sequential Object Picking in Clutter: The Runner-up Solution to RGMC 2025》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As a long-standing challenge in robotic manipulation, stable and efficient grasping in cluttered environments is of great importance in industrial settings. While recent studies have achieved relatively high success rates in grasping from clutter, there remain few mature solutions for more demanding tasks such as sequential object search and sorting. This work addresses sequential object picking in cluttered environments based on the Cluttered Environment Picking Benchmark (CEPB) and presents our solution to the Pick-in-Clutter track of the 10th Robotic Grasping and Manipulation Competition (RGMC) at ICRA 2025. The task poses several key challenges. First, it requires robust and collision-aware grasping with high success rates across a diverse set of objects, including both rigid and deformable ones. Second, it demands efficient search for target objects, which places stringent requirements on the decluttering and searching strategies of the solution. To address the above challenges, we design an integrated hardware-software pipeline that combines object recognition, decluttering, and multi-modal grasping. The main contributions include the hardware design of a multifunctional gripper and novel representations for object distribution and occlusion relationships in cluttered space. This pipeline enables efficient recognition, search, and sequential grasping of objects in clutter, demonstrating strong performance in both laboratory tests and competition scenarios, and ultimately achieving second place in the Pick-in-Clutter track of the RGMC 2025.

</details>

---

### [[20_Research/Papers/强化学习/Learning_to_Adapt_Representation-Based_Reinforcement_Learning_for_Multi-Task_Skill_Transfer|Learning to Adapt: Representation-Based Reinforcement Learning for Multi-Task Skill Transfer]]

![[assets/2606.12890_figure.png|800]]

- **arXiv**: [2606.12890](https://arxiv.org/abs/2606.12890)
- **PDF**: https://arxiv.org/pdf/2606.12890
- **详细分析**: [[20_Research/Papers/强化学习/Learning_to_Adapt_Representation-Based_Reinforcement_Learning_for_Multi-Task_Skill_Transfer|Learning to Adapt: Representation-Based Reinforcement Learning for Multi-Task Skill Transfer]]
- **作者**: Aryan Naveen, Haitong Ma, Haldun Balim, Na Li
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《Learning to Adapt: Representation-Based Reinforcement Learning for Multi-Task Skill Transfer》归入 强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CTRL, MTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has achieved remarkable success in learning complex control policies, yet its applicability remains limited due to sample inefficiency and poor generalization across tasks. In this work, we propose RepMT-SAC, a framework for multi-task RL that enables efficient knowledge sharing and robust transfer to new tasks. RepMT-SAC uses spectral MDP decomposition to capture transferable dynamics, structuring the value function into a task-agnostic core with a minimal task-specific adjustment. This design allows for strong zero-shot performance on in-distribution tasks and rapid few-shot adaptation to out-of-distribution tasks. We evaluate RepMT-SAC on quadcopter trajectory-following tasks across in-distribution and out-of-distribution contexts, demonstrating that it outperforms baselines by up to 30%.

</details>

---

### [[20_Research/Papers/具身智能/AIR-VLA+_Decoupling_Movement_and_Manipulation_via_Cascaded_Dual-Action_Decoders_with_Asymmetric_MoE_for_Aerial_Robots|AIR-VLA+: Decoupling Movement and Manipulation via Cascaded Dual-Action Decoders with Asymmetric MoE for Aerial Robots]]

![[assets/2606.12859_figure.png|800]]

- **arXiv**: [2606.12859](https://arxiv.org/abs/2606.12859)
- **PDF**: https://arxiv.org/pdf/2606.12859
- **详细分析**: [[20_Research/Papers/具身智能/AIR-VLA+_Decoupling_Movement_and_Manipulation_via_Cascaded_Dual-Action_Decoders_with_Asymmetric_MoE_for_Aerial_Robots|AIR-VLA+: Decoupling Movement and Manipulation via Cascaded Dual-Action Decoders with Asymmetric MoE for Aerial Robots]]
- **作者**: Jianli Sun, Bin Tian, Qiyao Zhang, Zijian Liu, Yutong Wang, Zhiyong Cui, Bai Li, Yisheng Lv, Yonglin Tian
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《AIR-VLA+: Decoupling Movement and Manipulation via Cascaded Dual-Action Decoders with Asymmetric MoE for Aerial Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AIR-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Aerial manipulation systems have long suffered from representation coupling in end-to-end control, as platform-level Unmanned Aerial Vehicle (UAV) movement and end-effector-level arm manipulation differ substantially in action scale, dynamics, and control objectives. In this paper, we propose AIR-VLA+, a flow matching action generation architecture specifically designed for aerial manipulation, featuring cascaded dual-action decoders and an asymmetric feature-level Mixture of Experts (MoE). We construct cascaded manipulation and movement decoders, allowing the UAV to unidirectionally observe the manipulator's intent during movement to achieve workflow coordination, while isolating the impact of UAV movement information backpropagation on arm manipulation stability. Addressing the characteristic that UAV movement is highly dependent on high-level semantics and responsible for task state transitions in aerial manipulation, we design an input feature enhancement module for the UAV movement decoder. This module introduces an implicit visual grasp projector to perceive the interaction state between the gripper and the object, and injects compressed global semantic features. Within the UAV movement decoder, we deploy an implicit MoE architecture, enabling different movement experts to spontaneously exhibit capacity inclinations for various task stages during training. Through dense soft blending computation on the feature manifold, the UAV movement is endowed with stronger task-stage adaptability. Experiments on the standardized AIR-VLA benchmark demonstrate that our method comprehensively surpasses all baselines with an overall average score of 48.0. The overall task completion score improves by 80.2\% compared to the single-head $π_{0.5}$ policy, effectively mitigating the heterogeneous coordinated control conflicts of composite robots.

</details>

---

### [[20_Research/Papers/具身智能/Sparse2Act_Learning_Action-Aligned_Sparse_3D_Representations_for_Cross-Domain_Robot_Manipulation|Sparse2Act: Learning Action-Aligned Sparse 3D Representations for Cross-Domain Robot Manipulation]]

![[assets/2606.12759_figure.png|800]]

- **arXiv**: [2606.12759](https://arxiv.org/abs/2606.12759)
- **PDF**: https://arxiv.org/pdf/2606.12759
- **详细分析**: [[20_Research/Papers/具身智能/Sparse2Act_Learning_Action-Aligned_Sparse_3D_Representations_for_Cross-Domain_Robot_Manipulation|Sparse2Act: Learning Action-Aligned Sparse 3D Representations for Cross-Domain Robot Manipulation]]
- **作者**: Yu Guo, Chang Yu, Siyu Ma, Yunuo Chen, Yin Yang, Ying Nian Wu, Chenfanfu Jiang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Sparse2Act: Learning Action-Aligned Sparse 3D Representations for Cross-Domain Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LIBERO-10-to-Meta-World, LIBERO-to-Meta-World, Meta-World, PointWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Explicit 3D representations are attractive for manipulation because they expose object shape, workspace geometry, and robot-object relations in metric coordinates. However, sparse 3D encoders are often learned through downstream task objectives, tying the representation to a particular data distribution, policy architecture, and action parameterization. We introduce Sparse2Act, an observation-action alignment framework for pretraining sparse point-cloud encoders. The key idea is to use task-space end-effector actions as geometric supervision: masked sparse 3D tokens are trained to organize scene features around the workspace motion paired with the observation. After pretraining, only the encoder initialization is reused by downstream policies, allowing them to retain their own architectures and action spaces, including joint-space commands. On the LIBERO-10 benchmark, our method achieves 86.9% average success after 500 fine-tuning steps. The same pretrained encoder supports LIBERO-to-Meta-World cross-domain transfer, achieving 73.4% average success on the Meta-World-5 benchmark. Ablations on the objective and decoder capacity show that the gains come from the masked action-alignment signal and remain useful across downstream action decoders. In real-world experiments, simulation pretraining followed by limited real-data fine-tuning achieves an average success rate of 72.5% across four tasks, demonstrating effective sim-to-real transfer. These results suggest that robot actions can provide compact geometric supervision for reusable sparse 3D representations.

</details>

---

### [[20_Research/Papers/机器人/DARRMS_--_An_Efficient_Algorithm_for_Dynamic_Attention_Radius_in_Resource-Constrained_Multi-Agent_Systems|DARRMS -- An Efficient Algorithm for Dynamic Attention Radius in Resource-Constrained Multi-Agent Systems]]

![[assets/2606.12614_figure.png|800]]

- **arXiv**: [2606.12614](https://arxiv.org/abs/2606.12614)
- **PDF**: https://arxiv.org/pdf/2606.12614
- **详细分析**: [[20_Research/Papers/机器人/DARRMS_--_An_Efficient_Algorithm_for_Dynamic_Attention_Radius_in_Resource-Constrained_Multi-Agent_Systems|DARRMS -- An Efficient Algorithm for Dynamic Attention Radius in Resource-Constrained Multi-Agent Systems]]
- **作者**: Benjamin Alcorn, Eman Hammad
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.5，机器人 0.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《DARRMS -- An Efficient Algorithm for Dynamic Attention Radius in Resource-Constrained Multi-Agent Systems》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent systems are integral tools for various domains such as robotics, cybersecurity, and autonomous vehicle planning. These types of systems often have constraints on the computational resources, leading to a need for efficient lightweight algorithms. Traditional decision making frameworks often assume ideal conditions, such as full observability and unlimited computational capacity, which do not align with real-world challenges. In this paper, we introduce a new algorithm that allows for reduced demand on computational resources without a large cost of other performance metrics. Agents will limit their observability to some attention radius, which intentionally allows them to ignore parts of the environment that might be unnecessary for action planning. By optimizing both the attention radius and decision-making, our approach enhances coordination and scalability in uncertain environments. Through both theoretical analysis and empirical validation, we demonstrate the effectiveness of adaptive observation in improving system performance and maintaining robust decision-making strategies in resource-constrained systems.

</details>

---

### [[20_Research/Papers/强化学习/EgoEngine_From_Egocentric_Human_Videos_to_High-Fidelity_Dexterous_Robot_Demonstrations|EgoEngine: From Egocentric Human Videos to High-Fidelity Dexterous Robot Demonstrations]]

![[assets/2606.12604_first_page.png|800]]

- **arXiv**: [2606.12604](https://arxiv.org/abs/2606.12604)
- **PDF**: https://arxiv.org/pdf/2606.12604
- **详细分析**: [[20_Research/Papers/强化学习/EgoEngine_From_Egocentric_Human_Videos_to_High-Fidelity_Dexterous_Robot_Demonstrations|EgoEngine: From Egocentric Human Videos to High-Fidelity Dexterous Robot Demonstrations]]
- **作者**: Yangcen Liu, Shuo Cheng, Xinchen Yin, Woo Chul Shin, Alfred Cueva, Yiran Yang, Zhenyang Chen, Chuye Zhang, Danfei Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《EgoEngine: From Egocentric Human Videos to High-Fidelity Dexterous Robot Demonstrations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous manipulation is limited by the cost of collecting large-scale robot demonstrations. Egocentric human videos offer a scalable source of diverse manipulation behaviors, but directly using them for robot learning requires bridging two gaps: the visual gap between human and robot observations, and the action gap between human motion and robot-executable action. We propose EgoEngine, a scalable framework for transforming egocentric human manipulation videos into high-fidelity robot data. Given an egocentric RGB video, EgoEngine produces: (i) a high-fidelity robot observation video replacing human with robot while preserving scene context and temporal alignment, and (ii) a task-aligned, executable robot action trajectory under feasibility constraints. Experiments in simulation and on real robots show that EgoEngine enables scalable conversion of human videos into robot data and, to our knowledge, demonstrates the first zero-shot visuomotor dexterous policy learning from egocentric human videos without real-robot demonstrations. Project website: https://egoengine.github.io.

</details>

---

### [[20_Research/Papers/机器人/G-MAPP_GPU-accelerated_Multi-Agent_Planning_and_Perception_for_Reactive_Motion_Generation|G-MAPP: GPU-accelerated Multi-Agent Planning and Perception for Reactive Motion Generation]]

![[assets/2606.12579_figure.png|800]]

- **arXiv**: [2606.12579](https://arxiv.org/abs/2606.12579)
- **PDF**: https://arxiv.org/pdf/2606.12579
- **详细分析**: [[20_Research/Papers/机器人/G-MAPP_GPU-accelerated_Multi-Agent_Planning_and_Perception_for_Reactive_Motion_Generation|G-MAPP: GPU-accelerated Multi-Agent Planning and Perception for Reactive Motion Generation]]
- **作者**: Tanmay Bishnoi, Riddhiman Laha, Tobias Löw, Jose Alex Chandy, Luis F. C. Figueredo, Sami Haddadin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《G-MAPP: GPU-accelerated Multi-Agent Planning and Perception for Reactive Motion Generation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reactive motion generation in unstructured environments remains an open challenge in robotics. Due to the computational complexity of collision-free motion generation, existing methods either generate global trajectories for static scenarios, or employ models that make conservative assumptions about the environment. This paper identifies the primary bottleneck as the runtime performance demand of planning on high-fidelity environments, and the temporal integration between the perception and planning modules. Therefore, we propose a framework that does not compromise on runtime performance and world representations for perception and planning by accelerating world modeling and vector-field based planning using the GPU. This allows us to achieve faster parallel state exploration for quasi-global trajectory planning, and tighter coupling of the perception-action loop in real-time for dynamic cluttered environments with off-the-shelf depth sensors. We quantitatively evaluate the computation-time and success rate differences for the CPU and GPU versions of our planner, and perform qualitative evaluations of our coupled framework using real-world experiments on a 7-DoF Franka Emika robot. Experimental results demonstrate that our GPU-based framework achieves up to a 5x speedup over the CPU version and successfully avoids collisions across both trivial and challenging physical world scenarios.

</details>

---

### [[20_Research/Papers/具身智能/Action-Effect_Memory_Pretraining_for_Robot_Manipulation|Action-Effect Memory Pretraining for Robot Manipulation]]

![[assets/2606.12499_figure.png|800]]

- **arXiv**: [2606.12499](https://arxiv.org/abs/2606.12499)
- **PDF**: https://arxiv.org/pdf/2606.12499
- **详细分析**: [[20_Research/Papers/具身智能/Action-Effect_Memory_Pretraining_for_Robot_Manipulation|Action-Effect Memory Pretraining for Robot Manipulation]]
- **作者**: Yijing Zhou, Qiwei Liang, Sitong Zhuang, Jiaxi Li, Xianpeng Wang, Boyang Cai, Yunyang Mo, Renjing Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Action-Effect Memory Pretraining for Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：RMBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present AEM, an Action-Effect Memory pretraining framework for robot manipulation that learns compact temporal representations from vision-action history. Unlike prior robot representation pretraining methods that mainly focus on single-frame visual encoding, AEM targets the temporal nature of manipulation, where the current observation alone is often insufficient under partial observability. AEM models manipulation as an action-driven interaction process by interleaving visual and action features and applying masked modeling to recover missing content from incomplete histories, thereby learning action-conditioned state evolution. The Mamba-encoded output of the final vision token is used as a compact history representation, serving as the global context for decoding and downstream control. This design preserves a single-vector temporal bottleneck while keeping inference efficient. We evaluate AEM with Diffusion Policy and Flow Policy. AEM consistently improves manipulation performance in both simulation and real-world settings, outperforming baselines across clean scenes, cluttered and random scenes, and non-Markovian tasks. Ablation studies further show that history-aware pretraining surpasses single-frame pretraining and direct frame stacking, while reducing inference latency and computational cost.

</details>

---

### [[20_Research/Papers/具身智能/Learning_to_Assist_Collaborative_VLAs_for_Implicit_Human-Robot_Collaboration|Learning to Assist: Collaborative VLAs for Implicit Human-Robot Collaboration]]

![[assets/2606.12475_figure.png|800]]

- **arXiv**: [2606.12475](https://arxiv.org/abs/2606.12475)
- **PDF**: https://arxiv.org/pdf/2606.12475
- **详细分析**: [[20_Research/Papers/具身智能/Learning_to_Assist_Collaborative_VLAs_for_Implicit_Human-Robot_Collaboration|Learning to Assist: Collaborative VLAs for Implicit Human-Robot Collaboration]]
- **作者**: Leo Xu, Letian Li, Alex Cuellar, Michael Hagenow
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Learning to Assist: Collaborative VLAs for Implicit Human-Robot Collaboration》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-robot collaboration (HRC) combines the complementary strengths of humans and robots to improve task efficiency. However, many existing collaborative systems rely on hand-engineered pipelines, limiting their scalability and flexibility for new tasks. In this work, we show that models trained end-to-end with imitation learning, specifically vision-language-action (VLA) models, can support collaborative manipulation, and characterize the key factors affecting their real-world performance. We evaluate two state-of-the-art models and identify a failure mode of action-chunking policies in implicit HRC, where demonstration action leakage (i.e., action chunks crossing latent task transitions) can cause premature assistive behavior. We find that this issue increases with longer execution horizons and occurs in real-world collaborative VLA systems, such as when a robot attempts to hand over a tool before the person is ready. We propose an inference-time steering method to mitigate these erroneous assistive actions while preserving policy performance. Finally, through a 16-participant user study on a long-horizon collaborative assembly task, we show that steering enables a longer execution horizon while mitigating premature assistance, leading to faster collaboration and fewer failures compared to a shorter-horizon policy.

</details>

---
