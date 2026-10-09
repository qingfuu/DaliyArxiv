# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-10-08

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/AeroEval_Staged_Program_and_Execution_Validation_for_AI-Generated_Drone_Missions|AeroEval: Staged Program and Execution Validation for AI-Generated Drone Missions]]

![[assets/2610.09764_figure.png|800]]

- **arXiv**: [2610.09764](https://arxiv.org/abs/2610.09764)
- **PDF**: https://arxiv.org/pdf/2610.09764
- **详细分析**: [[20_Research/Papers/具身智能/AeroEval_Staged_Program_and_Execution_Validation_for_AI-Generated_Drone_Missions|AeroEval: Staged Program and Execution Validation for AI-Generated Drone Missions]]
- **作者**: Kautuk Astu, Naina Rabha, Yogesh Simmhan
- **cs 子类**: cs.DC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《AeroEval: Staged Program and Execution Validation for AI-Generated Drone Missions》归入 机器人、大模型、具身智能 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AeroEval, AirSim, Co-zyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) can generate drone programs from natural-language mission descriptions, but syntactically valid programs may still violate user intent, environmental constraints, and mission-level behavior. This problem is pronounced in cyber-physical applications, where correctness depends on the interaction among generated code, mobile sensing, environmental geometry, event-driven analytics, and physical execution. Existing drone code-generation systems primarily use prompt guardrails or simulator outcomes and provide limited failure localization. We present AeroEval, an agent-assisted middleware for staged validation of AI-generated drone missions. AeroEval combines deterministic program analysis with context-grounded LLM agents. It first validates program syntax, platform API usage, and mission intent, and then evaluates the realized behavior using execution trajectories, mission requirements, and environmental context. Each stage returns structured failure information for iterative regeneration. In our evaluation using 20 navigation tasks and five analytical mission types over AirSim and Gazebo simulators, AeroEval improves navigation success from 55% to 95%. In a stagewise ablation study, our Code and Trajectory Validators by themselves achieve mean run-level success rates of 44% and 56%, respectively, while the full AeroEval pipeline achieves 88%; the stages detect complementary failures in program structure, API usage, mission intent, obstacle avoidance, altitude, coverage, and event-driven transitions and the guided regeneration corrects for them. Across the main analytics missions, AeroEval increases aggregate run-level success from 34% for one-shot AeroGen to 88% within the regeneration budget. These results demonstrate the benefit of combining program-level and execution-grounded agentic validation for AI-generated drone applications in the evaluated environment.

</details>

---
