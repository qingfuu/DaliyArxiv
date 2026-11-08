# cs.LG | Machine Learning | 2026-11-06

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/强化学习/Spectral_and_Subspace_Dynamics_of_LoRA_in_Supervised_Fine-Tuning_and_Reinforcement_Learning|Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning]]

![[assets/2611.08414_first_page.png|800]]

- **arXiv**: [2611.08414](https://arxiv.org/abs/2611.08414)
- **PDF**: https://arxiv.org/pdf/2611.08414
- **详细分析**: [[20_Research/Papers/强化学习/Spectral_and_Subspace_Dynamics_of_LoRA_in_Supervised_Fine-Tuning_and_Reinforcement_Learning|Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning]]
- **作者**: Chenruo Liu, Zihan Wang, Yijun Dong, Qi Lei
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Low-rank adaptation (LoRA) is commonly used in both supervised fine-tuning (SFT) and reinforcement learning (RL), often under similar optimizer settings. Yet, how the different dynamics of the two stages manifest in the low-rank increment that LoRA optimizes remains unclear. Tracking the singular spectrum and subspaces of LoRA updates on mathematical reasoning tasks, we find that RL concentrates the spectrum at every learning rate, while SFT expands it at moderate learning rates; moreover, RL rotates the singular subspaces much faster than SFT at small learning rates. Interpolating between SFT and RL one ingredient at a time, we pinpoint group-mean baseline subtraction as the source of both contrasts. A quadratic multi-index model updated via LoRA unveils the underlying mechanism: group-mean baseline subtraction tilts the balance between two competing forces, coherent fitting and gradient noise, toward spectral concentration and faster subspace rotation, while forcing the risk-favorable learning rate to be low. Guided by these dynamics, we tailor LoRA updates to each stage: in SFT, we flatten the spectrum of the full update to spread adaptation across singular directions, whereas in RL, we flatten the part of the update outside the current LoRA increment span to promote subspace rotation. Experiments on mathematical reasoning tasks across multiple models show that the respective configurations for SFT and RL yield the best performance among the compared methods in most evaluated settings.

</details>

---

### [[20_Research/Papers/强化学习/SHORE_Stability-Hybrid_On-Policy_Reinforcement_Learning_for_Online_Bin_Packing|SHORE: Stability-Hybrid On-Policy Reinforcement Learning for Online Bin Packing]]

![[assets/2611.08364_figure.png|800]]

- **arXiv**: [2611.08364](https://arxiv.org/abs/2611.08364)
- **PDF**: https://arxiv.org/pdf/2611.08364
- **详细分析**: [[20_Research/Papers/强化学习/SHORE_Stability-Hybrid_On-Policy_Reinforcement_Learning_for_Online_Bin_Packing|SHORE: Stability-Hybrid On-Policy Reinforcement Learning for Online Bin Packing]]
- **作者**: Chang Shi, Ann Majewicz Fey
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《SHORE: Stability-Hybrid On-Policy Reinforcement Learning for Online Bin Packing》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online 3D bin packing with a processing buffer requires choosing which box to pack, its orientation, and its placement while keeping the stack stable under unknown future arrivals. A collapse ends the episode and forfeits the remaining volume. Existing methods use geometric rules or hard stability masks, limiting how risk can influence the joint choice of box, orientation, and placement. We propose Stability-Hybrid On-Policy Reinforcement Learning (SHORE), which combines a learned stability probability of a placement with an on-policy estimate of its return conditional on stability. A 3D U-Net learns stability from executed outcomes and simulated alternatives, revealing outcomes of actions underrepresented in early rollouts. A discrete on-policy actor--critic uses stability predictions in both its action values and policy prior, with gates that limit the effect of an untrained or changing model. In deployment, SHORE does not require additional search or simulation overhead. In Isaac Gym, SHORE reaches 73\% space utilization by 0.4M environment steps, while the same learner without stability modeling reaches that level at about 1M. On the expanded 60-box set, SHORE achieves 0.734 space utilization versus 0.588 for the GOPT state-of-the-art baseline, with a higher placement-failure frequency (1.03\% vs. 0.63\%), trading more risk for greater packed volume. The results show faster learning and higher utilization on the more demanding realistic box arrival set. Ablations suggest that simulated alternatives provide useful early supervision, while executed outcomes alone sustain later performance. We also demonstrate the method on a real robot to verify the simplicity of integrating the method to real bin packing pipelines.

</details>

---

### [[20_Research/Papers/强化学习/Detecting_Silent_Faults_at_the_Environment-Trainer_Boundary_in_Reinforcement_Learning|Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning]]

![[assets/2611.08144_first_page.png|800]]

- **arXiv**: [2611.08144](https://arxiv.org/abs/2611.08144)
- **PDF**: https://arxiv.org/pdf/2611.08144
- **详细分析**: [[20_Research/Papers/强化学习/Detecting_Silent_Faults_at_the_Environment-Trainer_Boundary_in_Reinforcement_Learning|Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning]]
- **作者**: Zuo Gou, Chenhao Lu
- **cs 子类**: cs.LG, cs.RO, cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型, 大模型
- **相关性评分**: 2.02（加权：具身智能 0.3，大模型 0.1，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CleanRL, PlugRL, SRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot reinforcement learning increasingly runs environments outside the trainer: in another process, on another machine, in another language. Many faults at this boundary raise no error. We make the boundary a wire protocol and ask what notices a fault in it. On Pendulum, HalfCheetah, Hopper and a 7-joint arm (Pusher), we injected up to 23 faults into what crosses the wire and 2 into the trainer's log, from one value to every value. Unless every value was wrong, a learning-curve threshold caught at most one run in ten, and a comparison with ten fault-free seeds at most 21%. A clean evaluation of all 1,060 final policies agreed with the curves: of the 728 boundary-fault runs both curve checks passed, 723 scored no more than three standard deviations below fault-free seeds, though nearly all ended on other weights and, for reward faults, logged other returns. Checks of the run itself, not of its outcome, saw every fault. A step ledger kept on both sides and compared step by step caught and located every fault that crossed, on Pendulum, Hopper and Pusher on one machine and on Pendulum across two, with no fault-free run and, on Pendulum, a median 3% more training time. An episode record kept at the environment caught the faults in the trainer's log. We list such faults found in practice, in Gymnasium 1.3 and our own code and, reported by others, in five multi-agent libraries, and recommend a step ledger and episode counts kept at the environment.

</details>

---

### [[20_Research/Papers/强化学习/The_Blindfolded_Controller_Decision_Model-Guided_Training_for_Reinforcement_Learning|The Blindfolded Controller: Decision Model-Guided Training for Reinforcement Learning]]

![[assets/2611.07934_figure.png|800]]

- **arXiv**: [2611.07934](https://arxiv.org/abs/2611.07934)
- **PDF**: https://arxiv.org/pdf/2611.07934
- **详细分析**: [[20_Research/Papers/强化学习/The_Blindfolded_Controller_Decision_Model-Guided_Training_for_Reinforcement_Learning|The Blindfolded Controller: Decision Model-Guided Training for Reinforcement Learning]]
- **作者**: Muhammad Ibrahim Khan, Aniket Dixit, Faizan Ahmed, James Brusey
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《The Blindfolded Controller: Decision Model-Guided Training for Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) provides a framework for continuous improvement through interaction with an environment. However, RL agents struggle against tasks that offer exploration challenges and sparse rewards, because learning efficient policies from scratch is slow and sample-inefficient. In contrast, decision models (DMs), given a description of the environment and task, can perform well in sparse-reward tasks, but, as they do not learn from reward, they are not able to improve towards the optimal solution. In this paper, we present Decision Model-Guided Training (DMGT), a technique that uses a DM with a description of the environment and task to initialise an RL policy, combining the DM's ability to act without training with RL's ability to improve from reward. Instead of exploring from scratch, the agent reaches the goal and receives reward from its first episodes, and RL then improves its policy beyond what the DM achieves. We demonstrate through experiments on seven tasks that our approach outperforms RL in all seven and DM in five. In addition, we provide comprehensive guidelines, derived from ablation studies, for describing an environment and task to a DM.

</details>

---

### [[20_Research/Papers/强化学习/PBPO_Prefix-Block_Policy_Optimization_for_Diffusion_Language_Models|PBPO: Prefix-Block Policy Optimization for Diffusion Language Models]]

![[assets/2611.07783_first_page.png|800]]

- **arXiv**: [2611.07783](https://arxiv.org/abs/2611.07783)
- **PDF**: https://arxiv.org/pdf/2611.07783
- **详细分析**: [[20_Research/Papers/强化学习/PBPO_Prefix-Block_Policy_Optimization_for_Diffusion_Language_Models|PBPO: Prefix-Block Policy Optimization for Diffusion Language Models]]
- **作者**: Katherine Tieu, Dongqi Fu, Si Zhang, Hanqing Zeng, Tianxin Wei, Chenglin Wei, Yinglong Xia, Hong Li, Jingrui He
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《PBPO: Prefix-Block Policy Optimization for Diffusion Language Models》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion Large Language Models (dLLMs) commonly decode responses by proceeding autoregressively across blocks while iteratively denoising multiple tokens within each block. This structure makes block-level policy optimization a natural adaptation of autoregressive policy optimization. However, the exact likelihood of a completed block is intractable because it marginalizes over the intermediate states and reveal orders of the denoising process. To realize the block-level formulation, we construct a prefix-block state and use a single model evaluation to define a factorized one-step surrogate for the block likelihood. The resulting block surrogate ratio is a product of its token surrogate ratios, allowing variation at individual positions to propagate across the entire block before clipping. We therefore introduce Prefix-Block Policy Optimization (PBPO), which preserves block-level conditioning but applies surrogate importance weighting and clipping separately to each token. PBPO further diversifies repeated updates by resampling corrupted views of the prompt and revealed prefix, a design motivated by masked-dLLM pre-training. Under our analysis assumptions, block-product weighting amplifies the variance of gradient contributions relative to token-local weighting. Across two LLaDA-family initializations, six benchmarks, and three generation lengths, PBPO achieves competitive performance against existing dLLM RL methods.

</details>

---

### [[20_Research/Papers/强化学习/Foresee_to_Trade_Forecast-Augmented_Policy_Optimization_for_Portfolio_Management|Foresee to Trade: Forecast-Augmented Policy Optimization for Portfolio Management]]

![[assets/2611.07750_figure.png|800]]

- **arXiv**: [2611.07750](https://arxiv.org/abs/2611.07750)
- **PDF**: https://arxiv.org/pdf/2611.07750
- **详细分析**: [[20_Research/Papers/强化学习/Foresee_to_Trade_Forecast-Augmented_Policy_Optimization_for_Portfolio_Management|Foresee to Trade: Forecast-Augmented Policy Optimization for Portfolio Management]]
- **作者**: Zeyu Liu, Xuanzhi Feng, Haoran Xu, Lai Sing Kwong, Yang Li, Hualei Zhang, Hao Chen, Jie Zhang, Xiaoyi Pang, Song Guo
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Foresee to Trade: Forecast-Augmented Policy Optimization for Portfolio Management》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online investment services must translate asset opportunities into investment outcomes for users' accounts, yet the same market opportunity can warrant different account actions. We study how supervision from future asset opportunities can strengthen account-level trading decisions and propose Forecast-Augmented Relative Policy Optimization (FRPO). FRPO separately supervises asset opportunities and account decisions through a jointly learned representation: a Financial State Head (FSH) learns future relative-return targets to provide asset-level opportunity supervision, while Same-Path Group-Relative Optimization compares trading trajectories under the same market path and initial account to provide account-level relative-outcome supervision. An Adaptive Gate coordinates auxiliary supervision using predictive variance and gradient alignment. FSH is used only during training; inference uses the encoder and policy for trading. Across DJIA30, TOPIX Core30, and three investment-style portfolios, ten-seed evaluations show that FRPO achieves the highest mean cumulative and annualized returns among the compared methods in all five settings. These results support strengthening investment agents' trading decisions through joint supervision from asset opportunities and trading outcomes.

</details>

---

### [[20_Research/Papers/强化学习/Monotone_Viability_Learning_for_Offline_Safe_Reinforcement_Learning|Monotone Viability Learning for Offline Safe Reinforcement Learning]]

![[assets/2611.07616_figure.png|800]]

- **arXiv**: [2611.07616](https://arxiv.org/abs/2611.07616)
- **PDF**: https://arxiv.org/pdf/2611.07616
- **详细分析**: [[20_Research/Papers/强化学习/Monotone_Viability_Learning_for_Offline_Safe_Reinforcement_Learning|Monotone Viability Learning for Offline Safe Reinforcement Learning]]
- **作者**: Ziqian Wang, Zhen Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Monotone Viability Learning for Offline Safe Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Bullet-Safety-Gym, DSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline safe reinforcement learning requires reliable long-horizon safety estimates from fixed data. Learning Hamilton-Jacobi (HJ) viability in this setting calls for semantic preservation, convergence, and numerical stability. To address these challenges, we propose Monotone Viability Learning (MoViL), which learns viable sets from offline transitions through monotone finite-horizon set recursion. The recursion preserves finite-horizon safety semantics and converges to the infinite-horizon viability kernel. Binary supervision maintains a fixed target scale across horizons, avoiding discount-induced numerical attenuation. We further establish sufficient conditions for recovering behavior-supported viable subsets. The learned viability estimates are used to certify actions at deployment. Dubins car experiments validate the numerical accuracy of the learned viable sets. Evaluations on safe RL benchmarks demonstrate state-of-the-art reward-cost performance. MoViL satisfies the average cost constraint on every task and achieves the lowest average cost among the compared methods. These results highlight MoViL's potential to extend long-horizon HJ viability analysis to safety-critical systems where reliable dynamics models are unavailable and online exploration is unsafe.

</details>

---

### [[20_Research/Papers/具身智能/Binding_Paraphrased_Instructions_to_Encountered_Objects_in_sLLM_Agents_under_Partial_Observability|Binding Paraphrased Instructions to Encountered Objects in sLLM Agents under Partial Observability]]

![[assets/2611.07599_figure.png|800]]

- **arXiv**: [2611.07599](https://arxiv.org/abs/2611.07599)
- **PDF**: https://arxiv.org/pdf/2611.07599
- **详细分析**: [[20_Research/Papers/具身智能/Binding_Paraphrased_Instructions_to_Encountered_Objects_in_sLLM_Agents_under_Partial_Observability|Binding Paraphrased Instructions to Encountered Objects in sLLM Agents under Partial Observability]]
- **作者**: Chanyoung Kim, Harim Song, Byoungchan Ko, Keonyoung Lee, Myungwon Lee, Dahuin Jung
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.7）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Binding Paraphrased Instructions to Encountered Objects in sLLM Agents under Partial Observability》归入 大模型、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable deployment of LLM agents requires grounding diverse user expressions in their environments. Although RL-finetuned smaller large language model (sLLM) agents rival larger prompted LLMs on embodied tasks, their robustness to instruction paraphrases remains unclear. We introduce ALFWorld-Para to evaluate this robustness under controlled paraphrases, revealing 21-52% declines in success rates (SRs), predominantly driven by object synonyms. Despite retaining knowledge of synonym referents, agents often fail to take the corresponding objects even after observing them, exposing a gap between referential knowledge and object binding. Partial observability further complicates binding, as referents may remain unseen or have already been encountered under different labels. To address this challenge, we propose BINDIntent, a training-free framework that probabilistically binds referring expressions to observed labels using semantic proximity and estimated persistence against unseen candidates. Without additional training or LLM calls, BINDIntent improves synonym-paraphrase success of RL-finetuned sLLMs by 17.5-49.1 percentage points (pp) with only 0.4 ms of CPU overhead per step. It also raises GiGPO-7B's overall SR from 61.8% to 77.4%, surpassing a prompted 24B LLM. Code and benchmark are available at https://github.com/cau-hai-lab/ALFWorld-Para.

</details>

---

### [[20_Research/Papers/强化学习/Provable_Zeroth-Order_Safe_Exploration_for_Reinforcement_Learning_from_Human_Feedback|Provable Zeroth-Order Safe Exploration for Reinforcement Learning from Human Feedback]]

![[assets/2611.07561_first_page.png|800]]

- **arXiv**: [2611.07561](https://arxiv.org/abs/2611.07561)
- **PDF**: https://arxiv.org/pdf/2611.07561
- **详细分析**: [[20_Research/Papers/强化学习/Provable_Zeroth-Order_Safe_Exploration_for_Reinforcement_Learning_from_Human_Feedback|Provable Zeroth-Order Safe Exploration for Reinforcement Learning from Human Feedback]]
- **作者**: Weiqin Chen, Xinmeng Huang, Dongsheng Ding, Santiago Paternain
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Provable Zeroth-Order Safe Exploration for Reinforcement Learning from Human Feedback》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe reinforcement learning from human feedback (Safe-RLHF) seeks to improve helpfulness while satisfying harmlessness constraints. Existing primal-dual approaches can converge to feasible policies but do not prevent constraint violations during training. We study a stronger requirement, safe exploration for RLHF, under which every policy executed during training, including auxiliary exploration policies, remains feasible. We propose Zeroth-Order Log-Barrier Policy Gradient (ZO-LBPG), a reward-model-free method that optimizes a log-barrier objective using zeroth-order estimates derived directly from human preferences. To ensure safety under noisy feedback, we combine conservative constraint margin estimates with coupled rollouts and an adaptive step size that prevents updates from crossing constraint boundaries. We prove that, with high probability, all iterates and exploration policies remain strictly feasible, and that ZO-LBPG globally converges to an approximately optimal constrained policy. We establish a sample complexity of $\widetilde{\mathcal O}(\varepsilon^{-6}+d^3\varepsilon^{-5})$ trajectories and $\widetilde{\mathcal O}(\varepsilon^{-8}+d^5\varepsilon^{-7})$ human queries. Experiments on a synthetic CMDP and a language-model alignment task corroborate the training-time safety guarantees.

</details>

---

### [[20_Research/Papers/大模型/Learning_Multi-Agent_Orchestration_Higher-Order_Interactions_in_Policy_Improvement|Learning Multi-Agent Orchestration:Higher-Order Interactions in Policy Improvement]]

![[assets/2611.07495_figure.png|800]]

- **arXiv**: [2611.07495](https://arxiv.org/abs/2611.07495)
- **PDF**: https://arxiv.org/pdf/2611.07495
- **详细分析**: [[20_Research/Papers/大模型/Learning_Multi-Agent_Orchestration_Higher-Order_Interactions_in_Policy_Improvement|Learning Multi-Agent Orchestration:Higher-Order Interactions in Policy Improvement]]
- **作者**: Kaixuan Liu, Guojun Xiong
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.8，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Learning Multi-Agent Orchestration:Higher-Order Interactions in Policy Improvement》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learned orchestration has emerged as a promising paradigm for large language model (LLM)-based multi-agent systems, in which a central orchestrator selects agents and controls the information they receive throughout a task. Despite rapid empirical progress, existing methods train the orchestrator by crediting each decision with its own advantage, implicitly assuming that the other decisions in the episode stay fixed. This assumption fails in orchestration, where the contribution of each decision to the final outcome depends on the decisions preceding it, so the gain of a joint update is not the sum of its per-decision effects. To address this challenge, we introduce \textbf{IAPO}, an interaction-aware policy optimization framework that explicitly accounts for interactions among decisions. Specifically, IAPO exactly decomposes the performance difference between two policies into the effects of individual decisions and their interactions, which we prove can account for half of the attainable gain, and then optimizes both from sampled trajectories while certifying that every update is an improvement. On long-input versions of GSM8K, MATH, DROP, MBPP and HumanEval, against fifteen published multi-agent and workflow-search systems on the same 7B executor, IAPO's deployed plans reach the strongest system's accuracy with fewer tokens, and removing the interaction term costs 7 to 17 points of accuracy on code.

</details>

---

### [[20_Research/Papers/强化学习/Teaching_Agents_the_Principle_,_Not_the_Reward|Teaching Agents the "Principle", Not the "Reward"]]

![[assets/2611.07130_figure.png|800]]

- **arXiv**: [2611.07130](https://arxiv.org/abs/2611.07130)
- **PDF**: https://arxiv.org/pdf/2611.07130
- **详细分析**: [[20_Research/Papers/强化学习/Teaching_Agents_the_Principle_,_Not_the_Reward|Teaching Agents the "Principle", Not the "Reward"]]
- **作者**: Shan Yang
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Teaching Agents the "Principle", Not the "Reward"》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has achieved strong performance in many tasks by letting agents learn from nothing more than a reward signal. However, in more complex tasks, agents still struggle to learn good, generalizable policies, even with carefully designed rewards and abundant samples. We argue that this difficulty stems from the reward decoding burden: designers encode their knowledge of the desired behavior into rewards and penalties, and agents must infer this knowledge from long sequences of noisy scalars. To address this burden, we propose prescriptive policy learning (PPL), which directly teaches agents higher-level knowledge about the tasks, termed principles of behavior, such as how to maintain balance, how to accumulate energy, and how to land smoothly. Through appropriately selected key quantities and references, PPL can directly indicate at every step whether the agent follows the principles and to what extent. Our experiments show that agents can learn good, generalizable policies without any reward. Taught only simple heuristic principles, PPL agents outperform reward-based methods with far fewer samples. Their policies also transfer directly to harder settings and keep performing well, demonstrating their strong generalization ability. In summary, PPL provides a new approach in which rough knowledge of the desired behavior is enough for agents to learn good, generalizable policies, even when the system dynamics cannot be accurately modeled.

</details>

---

### [[20_Research/Papers/大模型/Regulating_Autonomous_Mobility-on-Demand_Operators_with_Fixed_and_Adaptive_Penalties_A_Multi-Agent_Reinforcement_Learning_Approach|Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach]]

![[assets/2611.07122_figure.png|800]]

- **arXiv**: [2611.07122](https://arxiv.org/abs/2611.07122)
- **PDF**: https://arxiv.org/pdf/2611.07122
- **详细分析**: [[20_Research/Papers/大模型/Regulating_Autonomous_Mobility-on-Demand_Operators_with_Fixed_and_Adaptive_Penalties_A_Multi-Agent_Reinforcement_Learning_Approach|Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach]]
- **作者**: Korbinian Kügler, Carolin Schmidt, Florian Dandl, Filipe Rodrigues
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Profit-maximizing Autonomous Mobility-on-Demand (AMoD) operators may exploit consumer surplus through excessive prices and underserve less profitable regions by relocating vehicles away from them. We study how penalty-based regulation of an AMoD operator in a multimodal mobility system can limit surge pricing and improve regional service availability. We model regulation as an outer control loop that acts on a learning-based operator. Static regulation with fixed penalties is formulated as a Markov Decision Process for an operator that jointly controls pricing and rebalancing, and dynamic regulation as a Partially Observable Stochastic Game in which a regulator periodically adjusts region-specific penalties in closed loop. Operator and regulator policies are learned with graph-based multi-agent reinforcement learning. In experiments with real-world Manhattan data, fixed surge pricing penalties reduce the share of travelers facing excessive prices from 22% to 1%. For regional service availability, dynamic regulation improves the regulator's reward by up to 15.6% over fixed penalties of equal mean intensity. The gains in service availability are strongest when spare fleet capacity exists, whereas service deficits persist in peak periods with highly utilized fleets. The learned regulator policy responds by reducing penalties where limited fleet capacity restricts compliance. The results identify trade-offs between regulatory targets, operator profitability, and traveler utility.

</details>

---
