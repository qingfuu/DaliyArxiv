# cs.CR | Cryptography and Security | 2026-11-13

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Bait_Mitigating_Harmful_Agentic_Reinforcement_Learning_via_Probing_Reward_Function|Bait: Mitigating Harmful Agentic Reinforcement Learning via Probing Reward Function]]

![[assets/2611.16369_figure.png|800]]

- **arXiv**: [2611.16369](https://arxiv.org/abs/2611.16369)
- **PDF**: https://arxiv.org/pdf/2611.16369
- **详细分析**: [[20_Research/Papers/大模型/Bait_Mitigating_Harmful_Agentic_Reinforcement_Learning_via_Probing_Reward_Function|Bait: Mitigating Harmful Agentic Reinforcement Learning via Probing Reward Function]]
- **作者**: Tiansheng Huang, Ananth Balashankar, Virat Shejwalkar, Santosh Pande, Ling Liu
- **cs 子类**: cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《Bait: Mitigating Harmful Agentic Reinforcement Learning via Probing Reward Function》归入 强化学习、大模型、世界模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We expose a safety vulnerability on nascent agentic reinforcement-learning-as-a-service. Specifically, with a cost as low as \$20, we show that safety alignment of a large language model (e.g., Inkling) can be completely subverted through rounds of harmful agentic reinforcement learning (agentic RL) with a toxic environment from its users. We also demonstrate that upon a successful harmful agentic RL attack via the service API, the attackers can potentially use the safety-degraded model to assist with real-world harmful activities, e.g., exploit software vulnerabilities and launch code re-use attacks. To mitigate harmful agentic RL, we propose Bait, a defense that mitigates the attack via proactively probing the reward function. Experimental results show that such a simple defense can sufficiently mitigate learning from a harmful reward function and can still learn from a benign reward function that promotes benign agentic tasks. Further analysis on both empirical and theoretical aspects shows that an adaptive attacker who assumes the knowledge of Bait defense cannot perfectly subvert it due to a systematic challenge. Source code is available at https://github.com/git-disl/Bait.

</details>

---

### [[20_Research/Papers/强化学习/FOE-Dreamer_Deployment-Efficient_Learning_of_Cyber_Defense_Policies_in_Operational_Networks|FOE-Dreamer: Deployment-Efficient Learning of Cyber Defense Policies in Operational Networks]]

![[assets/2611.14880_figure.png|800]]

- **arXiv**: [2611.14880](https://arxiv.org/abs/2611.14880)
- **PDF**: https://arxiv.org/pdf/2611.14880
- **详细分析**: [[20_Research/Papers/强化学习/FOE-Dreamer_Deployment-Efficient_Learning_of_Cyber_Defense_Policies_in_Operational_Networks|FOE-Dreamer: Deployment-Efficient Learning of Cyber Defense Policies in Operational Networks]]
- **作者**: Yinuo Du, Christopher Kiekintveld
- **cs 子类**: cs.CR, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.92（加权：强化学习 0.56，世界模型 1.36）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《FOE-Dreamer: Deployment-Efficient Learning of Cyber Defense Policies in Operational Networks》归入 世界模型、强化学习 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CyberBattleSim, MHBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous cyber defense is widely studied with deep reinforcement learning, but most work trains policies inside simulators because learning requires many trial-and-error interactions. Simulator-based training carries a fidelity gap: trained policies face authentication delays, partial action failures, service dependencies, and user traffic patterns that the simulator did not represent, and degrade on transfer. Training directly in the network being defended removes the gap but makes every interaction slow and costly, so sample efficiency becomes the binding constraint. Model-based reinforcement learning has reduced sample requirements on games and physical robots by orders of magnitude by planning inside a learned world model, but it has not been applied to defenders trained in operational networks. We present FOE-Dreamer (Factored Opponent-Enhanced Dreamer), a model-based reinforcement learning framework that trains a defender online and directly in a network on cloud infrastructure, without a simulator stage. FOE-Dreamer separates three sources of variation in the latent state: a controllable component driven by defender actions, an exogenous component driven by benign user activity, and an opponent embedding inferred from defender-observable signals alone. Separating the components reduces the variance in policy gradients during planning in imagination. Against two scripted attacker profiles with user activity emulated by the GHOSTS framework on an 8-host OpenStack testbed, FOE-Dreamer trains within a 3-day budget on a single GPU and achieves about 2$\times$ better episode loss than Rainbow and IQN baselines under matched compute. Both the factoring and the opponent model contribute to the gain, and the learned latents are consistent with the intended separation.

</details>

---
