# cs.OH | cs.OH | 2026-11-20

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Thermal-Guided_Ensemble_Reinforcement_Learning_for_Regime-Adaptive_Short-Term_GPU_Power_Forecasting_in_AI_Data_Centers|Thermal-Guided Ensemble Reinforcement Learning for Regime-Adaptive Short-Term GPU Power Forecasting in AI Data Centers]]

![[assets/2611.26527_figure.png|800]]

- **arXiv**: [2611.26527](https://arxiv.org/abs/2611.26527)
- **PDF**: https://arxiv.org/pdf/2611.26527
- **详细分析**: [[20_Research/Papers/强化学习/Thermal-Guided_Ensemble_Reinforcement_Learning_for_Regime-Adaptive_Short-Term_GPU_Power_Forecasting_in_AI_Data_Centers|Thermal-Guided Ensemble Reinforcement Learning for Regime-Adaptive Short-Term GPU Power Forecasting in AI Data Centers]]
- **作者**: Yuanshuo Zhang, Ying Zhang, Ziying Wang, Fanping Sui
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Thermal-Guided Ensemble Reinforcement Learning for Regime-Adaptive Short-Term GPU Power Forecasting in AI Data Centers》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL, TERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI data centers (AIDCs) introduce bursty and regime-dependent load patterns, posing significant challenges for reliable energy management and predictive grid control. To address these challenges, this letter proposes a thermal-guided ensemble reinforcement learning framework for probabilistic AIDC load forecasting. A soft actor-critic (SAC) agent with a simplex-preserving policy adaptively weights LSTM, TCN, and Transformer predictors at every time step based on their realized errors. A thermal-guided neural correction estimates the ensemble residual, while a sensitivity-projection regularizer enforces the non-negative sensitivity of power to GPU utilization and temperature. The corrected ensemble output is further processed by a Bayesian probabilistic layer to produce predictive distributions and quantify forecasting uncertainty. Case studies on 1-second MIT Supercloud telemetry show that the proposed method reduces the normalized mean absolute error to about 1% across all computing regimes, compared with 4-11% for deep learning-based and ensemble learning benchmarks, and converges faster with narrower prediction intervals than a DRL ensemble without thermal guidance.

</details>

---
