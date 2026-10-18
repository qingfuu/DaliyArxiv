# cs.GR | Graphics | 2026-10-16

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/世界模型/Decoupling_Appearance_and_Geometry_in_Diffusion_World_Models|Decoupling Appearance and Geometry in Diffusion World Models]]

![[assets/2610.20625_figure.png|800]]

- **arXiv**: [2610.20625](https://arxiv.org/abs/2610.20625)
- **PDF**: https://arxiv.org/pdf/2610.20625
- **详细分析**: [[20_Research/Papers/世界模型/Decoupling_Appearance_and_Geometry_in_Diffusion_World_Models|Decoupling Appearance and Geometry in Diffusion World Models]]
- **作者**: Rajit Rajpal
- **cs 子类**: cs.GR
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《Decoupling Appearance and Geometry in Diffusion World Models》归入 世界模型 方向。该论文围绕 Graphics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study the problem of learning diffusion-based world models that jointly capture scene geometry and visual appearance in complex first-person environments. Existing approaches typically train a single action-conditioned model that predicts future RGB frames, but they either ignore geometry or require action supervision for all modalities, limiting scalability to large unlabeled video datasets. In this work, we introduce a two-stage diffusion world model that separates geometric and appearance prediction while maintaining joint temporal coherence. Our key idea is a staggered RGB-depth formulation: depth at time $t+1$ is predicted first using an action-conditioned diffusion transformer, and the RGB frame at the same timestep is then generated conditioned on this predicted depth using a second diffusion model without action inputs. We show that this decoupled design faithfully approximates a hypothetical joint RGBD diffusion model trained with diffusion forcing, enabling the second stage to be trained or fine-tuned on additional RGB-depth data without requiring action labels. Experiments on the CS:GO Dust 2 dataset demonstrate that our approach improves both depth accuracy and RGB fidelity compared to fully joint models and RGB-only baselines, while significantly enhancing scalability to augmented or unlabeled datasets. Our results highlight the effectiveness of geometry-guided diffusion for world modeling and open a path toward large-scale action-free video model training. Code to be released upon acceptance of paper.

</details>

---
