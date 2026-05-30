# cs.CY | Computers and Society | 2026-05-28

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/APS_Bias-Controlled_Adaptive_Prototype_Simulation_for_Population-Scale_LLM_Agents|APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents]]

![[assets/2605.27419_figure.png|800]]

- **arXiv**: [2605.27419](https://arxiv.org/abs/2605.27419)
- **PDF**: https://arxiv.org/pdf/2605.27419
- **详细分析**: [[20_Research/Papers/大模型/APS_Bias-Controlled_Adaptive_Prototype_Simulation_for_Population-Scale_LLM_Agents|APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents]]
- **作者**: Quan Zheng, Yan Gao, Shaobin He, Haoxiang Guan, Yuanhe Tian, Jie Feng, Ming Wang, Shuxin Zheng, Zhen Liu
- **cs 子类**: cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型
- **相关性评分**: 1.1（加权：大模型 0.9，世界模型 0.2）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents》归入 大模型、世界模型 方向。该论文围绕 Computers and Society 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-agent simulation offers a flexible computational tool for studying population response trajectories that depend on scenario events, memory, demographics, and evolving social context. However, full multi-round simulation scales linearly with both population size and horizon, requiring every agent to query the LLM at every round. We propose Adaptive Prototype Simulation (APS), a framework that reframes scalable LLM-based simulation as a recurrent oracle-allocation problem. APS retains the designated LLM as the online transition oracle while querying adaptive core prototypes, selected singleton-tail agents, and shadow-audit agents. Prototype responses induce local response surfaces for nearby agents, reducing online LLM calls without replacing the underlying transition model. To control approximation bias, shadow-audit residual correction estimates propagation residuals for aggregate correction and future budget allocation, while tail-protected singleton routing directly queries selected isolated, heterogeneous, or high-curvature regions that are vulnerable to smoothing. Theoretically, we treat APS as an estimator for full-scale high-precision individual social simulation and decompose its errors into prototype-coverage error, shadow-audit residual-correction error, local-propagation bias, and temporal context mismatch. Under the reported protocols, APS gives lower reference-aligned distributional discrepancy than scale-oriented and same-budget baselines while reducing online LLM calls, with ablations and compact robustness checks diagnosing the main bias-control mechanisms. In a 10M-agent, multi-round public-opinion simulation, APS achieves a 381.1-fold reduction over full simulation, with reference-aligned final-round JSD of 0.094 against the corresponding full-LLM reference.

</details>

---

### [[20_Research/Papers/机器人/Surprising_Performances_of_Students_with_Autism_in_Classroom_with_NAO_Robot|Surprising Performances of Students with Autism in Classroom with NAO Robot]]

![[assets/2407.12014_first_page.png|800]]

- **arXiv**: [2407.12014](https://arxiv.org/abs/2407.12014)
- **PDF**: https://arxiv.org/pdf/2407.12014
- **详细分析**: [[20_Research/Papers/机器人/Surprising_Performances_of_Students_with_Autism_in_Classroom_with_NAO_Robot|Surprising Performances of Students with Autism in Classroom with NAO Robot]]
- **作者**: Qin Yang, Huan Lu, Dandan Liang, Shengrong Gong, Huanghao Feng
- **cs 子类**: cs.CY, cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Surprising Performances of Students with Autism in Classroom with NAO Robot》归入 机器人、具身智能 方向。该论文围绕 Computers and Society 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autism is a developmental disorder that manifests in early childhood and persists throughout life, profoundly affecting social behavior and hindering the acquisition of learning and social skills in those diagnosed. As technological advancements progress, an increasing array of technologies is being utilized to support the education of students with Autism Spectrum Disorder (ASD), aiming to improve their educational outcomes and social capabilities. Numerous studies on autism intervention have highlighted the effectiveness of social robots in behavioral treatments. However, research on the integration of social robots into classroom settings for children with autism remains sparse. This paper describes the design and implementation of a group experiment in a collective classroom setting mediated by the NAO robot. The experiment involved special education teachers and the NAO robot collaboratively conducting classroom activities, aiming to foster a dynamic learning environment through interactions among teachers, the robot, and students. Conducted in a special education school, this experiment served as a foundational study in anticipation of extended robot-assisted classroom sessions. Data from the experiment suggest that ASD students in classrooms equipped with the NAO robot exhibited notably better performance compared to those in regular classrooms. The humanoid features and body language of the NAO robot captivated the students' attention, particularly during talent shows and command tasks, where students demonstrated heightened engagement and a decrease in stereotypical repetitive behaviors and irrelevant minor movements commonly observed in regular settings. Our preliminary findings indicate that the NAO robot significantly enhances focus and classroom engagement among students with ASD, potentially improving educational performance and fostering better social behaviors.

</details>

---
