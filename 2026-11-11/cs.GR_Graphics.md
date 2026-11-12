# cs.GR | Graphics | 2026-11-11

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/FAME-QP_A_GPU-Accelerated_Quadratic-Programming_Solver_for_Real-Time_Model_Predictive_Control|FAME-QP: A GPU-Accelerated Quadratic-Programming Solver for Real-Time Model Predictive Control]]

![[assets/2611.13766_figure.png|800]]

- **arXiv**: [2611.13766](https://arxiv.org/abs/2611.13766)
- **PDF**: https://arxiv.org/pdf/2611.13766
- **详细分析**: [[20_Research/Papers/机器人/FAME-QP_A_GPU-Accelerated_Quadratic-Programming_Solver_for_Real-Time_Model_Predictive_Control|FAME-QP: A GPU-Accelerated Quadratic-Programming Solver for Real-Time Model Predictive Control]]
- **作者**: Santosh Mohan Rajkumar, Debdipta Goswami, Stephanie Stockar
- **cs 子类**: cs.GR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: cs.GR

#### 研究背景与动机

《FAME-QP: A GPU-Accelerated Quadratic-Programming Solver for Real-Time Model Predictive Control》归入 具身智能、机器人 方向。该论文围绕 Graphics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present FAME-QP, a GPU-accelerated solver for dense quadratic programs arising in linear model predictive control. FAME-QP combines constraint-dependent operator representations with fused single- and two-kernel iterations replayed through CUDA graphs, automatically selecting the execution configuration through device calibration and problem-specific timing. It probes a cached operator bank to select the initial penalty and updates operators lazily when problem matrices change. Numerical benchmarks and simulated humanoid and quadrotor control experiments demonstrate reduced latency relative to competing GPU solvers while maintaining solution accuracy and control performance.

</details>

---
