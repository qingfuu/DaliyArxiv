# cs.OH | cs.OH | 2026-09-21

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/其他/Learning-Based_Augmentation_and_Adaptation_for_Grid_Sim-to-Real_Model_Discrepancy|Learning-Based Augmentation and Adaptation for Grid Sim-to-Real Model Discrepancy]]

![[assets/2609.21986_figure.png|800]]

- **arXiv**: [2609.21986](https://arxiv.org/abs/2609.21986)
- **PDF**: https://arxiv.org/pdf/2609.21986
- **详细分析**: [[20_Research/Papers/其他/Learning-Based_Augmentation_and_Adaptation_for_Grid_Sim-to-Real_Model_Discrepancy|Learning-Based Augmentation and Adaptation for Grid Sim-to-Real Model Discrepancy]]
- **作者**: Sayak Mukherjee, Kyung-Bin Kwon, Ramij R. Hossain, Marcelo Elizondo
- **cs 子类**: 
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 0.9（加权：具身智能 0.9）
- **关联关键词**: 未提取到

#### 研究背景与动机

《Learning-Based Augmentation and Adaptation for Grid Sim-to-Real Model Discrepancy》归入 具身智能 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern power systems can encounter increased discrepancy between the operators' simulation model and the actual true dynamics of the grid, driven by uncertainties caused by integration of new inverter-based resources (IBRs), large loads, unmodeled dynamics, parameter drifts, etc., to name a few. All of these impact the control room operations, where some critical oscillations may not be captured during the transient studies. To circumvent these issues, we propose a learning-augmented hybrid approach where the operator simulation model is supplemented with artificial intelligence (AI)-learned residual models using the phasor measurement unit (PMU)/ point-on-wave (PoW) based sensed trajectory data. The physics-based operator model provides interpretability and structural consistency, while the learned residual captures discrepancies caused by non-idealities. The learned model employs advanced neural architectures and consists of a backbone encoder and multi-head decoder layers for heterogeneous grid channels. Subsequently, we formulated a continual learning-motivated adaptation framework such that the baseline residual AI model can also be updated when the underlying real grid model changes in future conditions. Extensive numerical simulations are performed on the IEEE 68-bus benchmark model with a diverse set of disturbances, and different state-of-the-art predictive architectures involving recurrent learners, latent neural ODEs, and transformers are explored to demonstrate both residual learning and adaptation capabilities.

</details>

---
