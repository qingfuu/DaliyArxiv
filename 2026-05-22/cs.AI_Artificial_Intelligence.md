# cs.AI | Artificial Intelligence | 2026-05-22

#arxiv #ComputerScience

**论文数**: 45

### [[20_Research/Papers/大模型/Vector_Policy_Optimization_Training_for_Diversity_Improves_Test-Time_Search|Vector Policy Optimization: Training for Diversity Improves Test-Time Search]]

![[assets/2605.22817_figure.png|800]]

- **arXiv**: [2605.22817](https://arxiv.org/abs/2605.22817)
- **PDF**: https://arxiv.org/pdf/2605.22817
- **详细分析**: [[20_Research/Papers/大模型/Vector_Policy_Optimization_Training_for_Diversity_Improves_Test-Time_Search|Vector Policy Optimization: Training for Diversity Improves Test-Time Search]]
- **作者**: Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, Akarsh Kumar, Mehul Damani, Sebastian Risi, Omar Khattab, Zhang-Wei Hong, Pulkit Agrawal
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.25，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

大语言模型越来越多地被放进带有推理时搜索的系统中使用，例如 AlphaEvolve 这类会从多个候选结果中筛选解的流程，模型训练不再只是追求单次输出最优，而是要能提供足够多样、可供搜索利用的候选答案。现有后训练方法通常只优化一个预先固定的标量奖励，容易把分布压得很窄，导致采样时多个答案彼此相似，难以支撑后续搜索。作者因此提出：如果部署阶段本来就会做搜索，那么训练阶段更应该显式优化“候选集合的多样性”，让模型为不同奖励权衡预留空间。这篇工作值得关注之处在于，它把强化学习后训练从“收敛到单一点”改成“覆盖奖励空间中的一条前沿”，直接针对推理时搜索的需求来设计目标。

#### 方法概述和架构

论文提出 Vector Policy Optimization（VPO），核心思想是让模型在一次 rollout 中连续生成多个候选答案，并让这些答案在奖励空间中分担不同的权衡。具体做法上，模型输入一个提示词后，输出一个由多个 completion 组成的集合 S，每个 completion 都会被多个子奖励维度评价，例如代码任务中的逐测试用例正确性、复杂问答中的不同子问题成功率，或工具调用任务中的结构/内容评分。训练时不再固定一个标量权重，而是从 Dirichlet 分布中采样权重向量 w，对每个候选集合计算“在该权重下的集合内最优解”的期望奖励，即对每个 w 选取集合中 w^T r 最高的答案作为回报信号。这样，模型会被鼓励生成一组彼此专门化的答案，使不同成员分别覆盖奖励空间中的不同区域，而不是全部坍缩到同一种解。方法上它基本可视为对 GRPO 优势估计的替代：保留 RL 后训练流程，但把优化目标从单一标量转为集合级、向量化的奖励覆盖。

#### 实验结果分析

作者在四个任务上验证了 VPO，包括 Maze、MuSiQue、EUREQA 和 ToolRL，并进一步在 LiveCodeBench 上做了代码生成案例研究，评估指标包括 pass@k、best@k 以及奖励空间多样性。实验表明，VPO 在测试时搜索上的表现达到或超过最强的标量 RL 基线，而且随着搜索预算增大，优势会进一步扩大。论文还指出，在更复杂的演化式搜索设置中，VPO 训练出的模型能解开一些 GRPO 模型完全无法解决的问题。节选文本未给出具体数值，但结论明确支持“训练多样性”对于推理时搜索是关键增益来源。

<details>
<summary>完整摘要</summary>

语言模型如今必须能够开箱即用地泛化到新的环境，并能在推理缩放（inference-scaling）的搜索流程中工作，例如 AlphaEvolve 这类会针对多种任务特定奖励函数选择 rollout 的方法。不幸的是，标准的大语言模型后训练范式通常只优化一个预先指定的标量奖励，这往往会导致当前模型输出分布的熵很低，从而难以展现推理时搜索所需要的多样性。为此，我们提出 Vector Policy Optimization（VPO），一种强化学习算法，它显式训练策略去预期多样的下游奖励函数，并生成多样化的解。VPO 利用了一个事实：在实践中，奖励往往天然就是向量形式，例如代码生成中的逐测试用例正确性，或者不同用户画像、不同奖励模型所对应的多个偏好维度。VPO 本质上可以直接替换 GRPO 的优势估计器，但它训练大语言模型输出一个解集合，其中每个解会在向量奖励空间的不同权衡上各自专精。在四个任务上，VPO 在测试时搜索中与最强的标量 RL 基线持平或更优，例如 pass@k 和 best@k；而且随着搜索预算增大，这种差距还会继续扩大。对于演化式搜索，VPO 训练出的模型甚至能够解开 GRPO 模型完全无法解决的问题。随着测试时搜索逐渐变得标准化，优化多样性或许需要成为默认的后训练目标。

</details>

---

### [[20_Research/Papers/大模型/LCGuard_Latent_Communication_Guard_for_Safe_KV_Sharing_in_Multi-Agent_Systems|LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems]]

![[assets/2605.22786_figure.png|800]]

- **arXiv**: [2605.22786](https://arxiv.org/abs/2605.22786)
- **PDF**: https://arxiv.org/pdf/2605.22786
- **详细分析**: [[20_Research/Papers/大模型/LCGuard_Latent_Communication_Guard_for_Safe_KV_Sharing_in_Multi-Agent_Systems|LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems]]
- **作者**: Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas, Prasanna Sattigeri, Karthikeyan Natesan Ramamurthy
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

多智能体大模型系统越来越依赖中间通信来协调复杂任务，但传统的自然语言通信既低效又会丢失部分任务相关信息。近年来，基于Transformer的KV cache 作为一种“潜在通信”载体，能够在智能体之间直接传递更丰富的内部表征，从而提升效率与推理连续性。然而，KV cache 也会隐式携带上下文输入、推理状态和智能体特定信息，一旦被共享，就可能在不经过显式文本披露的情况下泄露敏感内容。本文关注的正是这一类“表示层面”的隐私风险，因此具有很强的现实意义。

#### 方法概述和架构

论文提出 LCGuard（Latent Communication Guard），目标是在多智能体系统中对共享 KV cache 进行安全控制。其核心做法是在 KV 片段跨智能体传输前，先通过可学习的表示变换函数 g_{ij} 对缓存进行加工，而不是直接共享原始 K/V 表征。作者将通信对象视为潜在工作记忆，并把“可重构性”定义为泄露强度：如果攻击者能从共享表征中重建出某个智能体的敏感输入，则该表征被视为不安全。基于这一定义，LCGuard 采用对抗式训练：一侧是重建器/攻击者，尽可能从观察到的共享表示中恢复敏感输入；另一侧是通信变换模块，在尽量保持下游任务语义与性能的同时，压低敏感信息的可重构性。整体训练目标是在任务损失与隐私泄露之间做最优化权衡，推理时则使用训练好的变换模块替代原始 KV 直传。

#### 实验结果分析

作者在多种模型家族与多智能体基准上评估了 LCGuard，包括 Qwen3、Gemma-2-9B、LLaMA 等模型，以及 AgentLeak、MAGPIE、PrivacyLens 等基准。实验指标覆盖任务准确率、帮助性、Privacy Score、Leak Rate、ASR（攻击成功率）和重建难度等。结果表明，LCGuard 相比标准 KV 共享基线，能够稳定降低基于重建的泄露和攻击成功率，同时保持有竞争力的任务表现。正文节选还显示作者进一步分析了不同通信拓扑、模型家族和系统级/局部级保护差异；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

基于大语言模型（LLM）的多智能体系统越来越依赖中间通信来协调复杂任务。尽管大多数现有系统通过自然语言进行通信，但近期研究表明，潜在通信，尤其是通过 Transformer 的 key-value（KV）缓存进行通信，能够提升效率并保留更丰富的任务相关信息。然而，KV 缓存也会编码上下文输入、中间推理状态以及智能体特定信息，从而形成一条不透明的通道，使敏感内容可能在没有显式文本披露的情况下在智能体之间传播。为了解决这一问题，我们提出 LCGuard（Latent Communication Guard），这是一个面向多智能体 LLM 系统中安全 KV 潜在通信的框架。LCGuard 将共享 KV 缓存视为潜在工作记忆，并在缓存工件跨智能体传输之前学习表示层面的变换。我们从操作层面将表示级敏感信息泄露形式化为重建问题：如果攻击者解码器能够从共享缓存工件中恢复出某个智能体特定的敏感输入，那么该缓存工件就是不安全的。由此得到一个对抗训练形式，其中对手学习重建敏感输入，而 LCGuard 学习在保留任务相关语义的同时，减少可被重建的信息。跨多个模型家族和多智能体基准的实验表明，与标准 KV 共享基线相比，LCGuard 能持续降低基于重建的泄露和攻击成功率，同时保持具有竞争力的任务性能。

</details>

---

### [[20_Research/Papers/大模型/DeltaBox_Scaling_Stateful_AI_Agents_with_Millisecond-Level_Sandbox_Checkpoint_Rollback|DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback]]

![[assets/2605.22781_figure.png|800]]

- **arXiv**: [2605.22781](https://arxiv.org/abs/2605.22781)
- **PDF**: https://arxiv.org/pdf/2605.22781
- **详细分析**: [[20_Research/Papers/大模型/DeltaBox_Scaling_Stateful_AI_Agents_with_Millisecond-Level_Sandbox_Checkpoint_Rollback|DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback]]
- **作者**: Yunpeng Dong, Jingkai He, Yuze Hou, Dong Du, Zhonghu Xu, Si Yu, Yubin Xia, Haibo Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.6，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

面向代码修复、网页操作和强化学习等场景的 LLM 智能体，往往需要在沙箱里频繁试错、回退和分叉搜索路径，因此对“检查点/回滚”能力的要求非常高。现实中，智能体不仅要保存文件系统状态，还要保存进程内存、上下文和打开的文件句柄等完整运行状态；而现有方案通常通过整份状态复制来实现，单次检查点/回滚往往要花费数百毫秒到数秒，严重拖慢深度搜索和大规模并行采样。本文值得关注之处在于，它指出智能体相邻检查点之间通常高度相似，真正需要复制的只是增量变化，但这一思路要落地需要操作系统层面的新支持。

#### 方法概述和架构

论文提出新的 OS 级抽象 DeltaState，把文件系统状态和进程状态视为一个“基于差分的事务性状态对”，并围绕这一抽象设计了两个协同机制。其中文件系统部分由 DeltaFS 负责：它借鉴 OverlayFS 的分层思想，将文件状态组织成多层，在检查点时动态冻结当前可写层并插入新层，从而把写入转化为写时复制，把回滚简化为层切换。进程状态部分由 DeltaCR 负责：它采用增量式 dump 保存变化，并在回滚时绕过传统恢复流水线，直接从冻结的模板进程 fork() 出新进程，以降低恢复延迟。DeltaBox 将 DeltaFS 与 DeltaCR 组合成一个面向智能体的沙箱系统，两者通过 StateManager 耦合，在每次检查点/恢复时同步处理文件系统与进程状态，保证两类状态不会脱节。系统还包含模板池、异步预热以及基于 LRU 的回收策略，用于在控制内存占用的同时维持快速恢复。

#### 实验结果分析

论文在 SWE-bench 和 RL 微基准上评估 DeltaBox，并与若干现有沙箱/快照方案对比。结果显示，DeltaBox 的检查点和回滚都能达到毫秒级延迟，摘要中给出的代表性数字分别为 14ms 和 5ms。正文节选还指出，在 SWE-bench 的 MCTS 场景中，DeltaBox 将状态管理开销从部分基线的 47%–77% 降至 3%–6%，从而让智能体在固定时间预算下探索更多搜索节点。可见文本未给出完整的消融细节，但节选表明系统还考察了写放大、累计存储开销和自适应优化效果等方面。

<details>
<summary>完整摘要</summary>

基于 LLM 的 AI 智能体需要高频率的状态探索，例如测试时树搜索和强化学习，这依赖于对完整沙箱状态的快速检查点与回滚，包括文件状态和进程状态（如内存、上下文等）。现有机制通常会复制整份状态，导致单次检查点/回滚产生数百毫秒到数秒的延迟，这严重限制了深度搜索和大规模分叉。本文观察到，智能体中的相邻检查点通常高度相似。因此，与其复制完整状态，不如只复制相邻检查点之间的变化部分（关键洞察）。然而，这一思路并不容易实现，主要原因是缺少操作系统层面的支持。为此，本文提出一种新的 OS 级抽象 DeltaState，用于支持面向智能体的基于变化的事务性检查点/回滚，并配套设计了两个协同的操作系统机制。首先，DeltaFS 通过将文件状态组织为多层，并在检查点时动态冻结可写层、插入新层，实现基于变化的文件系统检查点/回滚；这样可以把文件更新转化为写时复制，并使回滚变成简单的层切换。其次，DeltaCR 使用增量式 dump 实现基于变化的进程状态检查点/回滚，并通过绕过传统流水线、直接从冻结的模板进程 fork()，加速回滚。基于这两项机制，本文提出 DeltaBox，一种能够实现毫秒级检查点/回滚的智能体沙箱。对 SWE-bench 和 RL 微基准的评估表明，DeltaBox 能以毫秒级延迟完成检查点和回滚（分别为 14ms 和 5ms），使智能体在固定时间预算下探索更多节点。

</details>

---

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Flexible_Job_Shop_Scheduling_with_Random_Job_Arrivals|Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals]]

![[assets/2605.22773_figure.png|800]]

- **arXiv**: [2605.22773](https://arxiv.org/abs/2605.22773)
- **PDF**: https://arxiv.org/pdf/2605.22773
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Flexible_Job_Shop_Scheduling_with_Random_Job_Arrivals|Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals]]
- **作者**: Yu Tang, Muhammad Zakwan, Efe Balta, John Lygeros, Alisa Rupenyan
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.1，强化学习 1.4）
- **关联关键词**: Agent, RL

#### 研究背景与动机

柔性作业车间调度问题（FJSP）要在多台可兼容机器之间，为一系列工序做最优分配，以尽量缩短全部任务的完工时间。与静态设定不同，本文关注的是“随机到达新作业”的动态场景，这会让未来任务不可预知，进一步加大调度难度。与此同时，FJSP本身就是组合优化难题，传统MILP求解器在实时性和规模扩展上都面临明显瓶颈，因此用强化学习来处理动态调度具有现实价值。

#### 方法概述和架构

本文提出一种面向随机作业到达的事件驱动深度强化学习方法，用PPO作为训练算法。作者将动态调度环境建模为MDP，只在“作业到达”或“工序完成”这些事件点进行决策，而不是每个时刻都重新规划。状态由三部分组成：各作业下一道工序的位置、各机器的下次空闲时间、以及各作业的下次可用时间，且可直接从环境读取，避免复杂手工特征设计。动作空间不直接输出具体的“作业-机器”配对，而是从10种调度规则组合中选择，即5种作业排序规则（SPT、LPT、FIFO、LIFO、MWR）与2种机器分配规则（MIN、MINC）的组合。这样，DRL代理学习的是“何时用哪条规则”，再由规则完成具体派工，从而兼顾可解释性和训练稳定性。奖励采用分段式塑形，用当前部分调度的makespan变化作为反馈，目标是最小化最终总完工时间。

#### 实验结果分析

实验在不同异质性和不同到达率的数据集上进行，并将所提方法与单独的派工规则以及事件触发的MILP基线（AT-MILP）进行对比，评价指标为makespan。结果显示，该DRL方法整体优于任一单独调度规则，说明“学习选择规则”比固定规则更稳健。与AT-MILP相比，方法表现出较强竞争力，尤其在机器与作业更异质的数据集上优势更明显。可见文本未给出具体数值，但作者明确指出该方法在异质场景下效果较好。

<details>
<summary>完整摘要</summary>

柔性作业车间调度问题（FJSP）旨在将一组作业最优分配给各台机器。FJSP中仍然存在两个主要挑战：未来作业到达具有不确定性，以及问题本身具有组合复杂性，使其对传统混合整数线性规划求解器而言难以处理。本文提出一种事件驱动的深度强化学习（DRL）方法，用于解决具有随机作业到达的FJSP。具体来说，我们采用近端策略优化（PPO）算法，并使用轻量级多层感知机（MLP）来训练DRL智能体，以最小化所有作业的总完工时间。我们设计的状态表示可以直接从环境中获取，并将学习智能体的动作限制为从一组成熟的调度规则中进行选择。仿真结果表明，所提出的DRL方法在不同异质性和不同作业到达率的数据集上，均优于任一单独的调度规则。我们还将该DRL方法与一种到达触发的混合整数线性规划解法进行基准比较，结果表明，尤其在数据集具有较强异质性时，我们的方法能够取得较好的性能。

</details>

---

### [[20_Research/Papers/强化学习/Superhuman_Safe_and_Agile_Racing_through_Multi-Agent_Reinforcement_Learning|Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning]]

![[assets/2605.22748_figure.png|800]]

- **arXiv**: [2605.22748](https://arxiv.org/abs/2605.22748)
- **PDF**: https://arxiv.org/pdf/2605.22748
- **详细分析**: [[20_Research/Papers/强化学习/Superhuman_Safe_and_Agile_Racing_through_Multi-Agent_Reinforcement_Learning|Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning]]
- **作者**: Ismail Geles, Leonard Bauersfeld, Markus Wulfmeier, Davide Scaramuzza
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 机器人, 具身智能, 世界模型
- **相关性评分**: 2.42（加权：具身智能 0.3，大模型 0.5，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

自主系统在单机控制或仿真中已经能达到超人类水平，但一旦进入共享、动态的真实环境，就容易因为忽视其他参与者而变得脆弱。现有物理任务大多沿用单智能体范式，把其他主体当作环境噪声处理，难以学到有效的协同、避让与竞争策略。对于仓储物流、搜救、城市空中交通等需要多机器人同时运行的场景，这一瓶颈尤其突出，因此这篇工作值得关注。

#### 方法概述和架构

论文以高速四旋翼竞速作为高风险测试平台，研究多智能体强化学习能否在真实物理交互中同时实现安全与敏捷。方法核心是基于 league-based self-play 的训练机制：智能体不只与固定对手交互，而是与来自历史检查点及其他训练范式的多样化策略群体持续对战，从而形成更稳健的竞争行为。模型使用带有 Perceiver 风格的置换不变注意力编码器，输入包括自身状态以及所有竞争者的相对位置和速度，因此能够适应不同数量、不同排列顺序的对手。为了处理近距离飞行中的空气动力学耦合，方法还显式引入 particle-based downwash model，用于刻画邻近无人机尾流对飞行的扰动。训练采用 PPO，并结合 recurrent actor-critic 与 LSTM 保持时序上下文；推理时单一策略可直接在从单人到多人、从纯无人机到人机混合的多种赛况中运行。

#### 实验结果分析

作者在真实四旋翼竞速实验中验证了方法，场景包括计时赛、AI 多机对抗以及人机混合比赛，对手包含冠军级人类飞手；同时还在大规模模拟中评估了多达 8 个智能体、累计超过 64,000 局的四人竞赛。结果显示，league-play 训练相较于单智能体基线将碰撞率降低 50%，同时保持竞争性圈速，并且能够零样本泛化到与人类飞手交互的更安全行为。真实比赛中，所学策略在最高超过 22 m/s 的速度下，能够战胜冠军级人类飞手，并在多机对抗中保持较高完赛率。节选文本还显示，方法在不同人数配置下具有良好泛化，但部分细粒度消融与完整数值对比在可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

自主系统在孤立环境或仿真中已经取得了超越人类的表现，但在共享且动态变化的真实世界空间中，它们仍然十分脆弱。这种失败源于物理应用中占主导地位的单智能体范式：其他参与者要么被忽略，要么被当作环境噪声，从而无法形成有效协同。我们在此表明，多智能体强化学习能够提供真实世界交互所必需的安全支架。我们以高速四旋翼竞速作为高风险测试平台，训练智能体在可变数量竞赛者存在的情况下，处理复杂的气动交互与策略机动。通过基于联盟的自我博弈，智能体逐渐演化出复杂的预判行为，包括主动规避碰撞、超越对手，以及应对多智能体物理交互（包括空气动力学下洗）等。我们的智能体在速度超过 22 m/s 的多机竞赛中，表现优于冠军级人类飞手；同时，相比最先进的单智能体基线，碰撞率降低了 50%。更关键的是，使用多样化人工智能体进行训练，可以零样本泛化到更安全的人机交互。上述结果表明，通往鲁棒机器人共存的路径，不在于孤立的安全约束，而在于多智能体交互所施加的严格要求。多媒体材料见：https://rpg.ifi.uzh.ch/marl

</details>

---

### [[20_Research/Papers/大模型/Beyond_Acoustic_Emotion_Recognition_Multimodal_Pathos_Analysis_in_Political_Speech_Using_LLM-Based_and_Acoustic_Emotion_Models|Beyond Acoustic Emotion Recognition: Multimodal Pathos Analysis in Political Speech Using LLM-Based and Acoustic Emotion Models]]

![[assets/2605.22732_first_page.png|800]]

- **arXiv**: [2605.22732](https://arxiv.org/abs/2605.22732)
- **PDF**: https://arxiv.org/pdf/2605.22732
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Acoustic_Emotion_Recognition_Multimodal_Pathos_Analysis_in_Political_Speech_Using_LLM-Based_and_Acoustic_Emotion_Models|Beyond Acoustic Emotion Recognition: Multimodal Pathos Analysis in Political Speech Using LLM-Based and Acoustic Emotion Models]]
- **作者**: Juergen Dietrich
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

这篇论文关注政治演讲中的 Pathos（情感诉求）分析，具体任务是判断一段发言在情绪上是否具有煽动性、团结性或分裂性，这在计算政治传播和大模型辅助舆情分析中都很重要。传统语音情感识别主要依赖音频声学特征，但其常用基准多来自“表演式”情绪语料，与真实政治语境存在明显偏差。作者因此提出一个核心问题：声学情感模型能否充当政治语篇中 Pathos 的代理，还是需要结合大模型的多模态语义理解才能更准确地刻画。

#### 方法概述和架构

论文以德国联邦议院一次 Felix Banaszak 的全体会议发言为案例，将整段演讲切分为 51 个片段后分别送入三种分析路径。第一种是 emotion2vec_plus_large 声学情感识别模型，输出离散情绪类别概率，再通过 Russell Circumplex 的后验投影得到连续 Arousal 和 Valence。第二种是 Gemini 2.5 Flash，将完整音频与对应转写一并输入，采用开放式、上下文感知的多模态方式直接判断每段的主次情绪、Arousal、Valence 以及修辞功能。第三种是 TRUST-Pathos 管线中的多代理 LLM 评分，由三个 advocate 模型给出 Pathos 分值，再经 supervisor 汇总为最终结果。作者随后用 Spearman 秩相关比较不同模态与 TRUST-Pathos 的一致性，并额外用 Gemini 对 EMO-DB 做开放式标注，以检验传统 SER 基准的质量与适用性。

#### 实验结果分析

在 Banaszak 发言上，Gemini 的 Valence 与 TRUST-Pathos 呈显著正相关，而 emotion2vec 的 Valence 与 TRUST-Pathos 几乎不相关，说明大模型的多模态分析更能捕捉政治语境中的语义化情感。Arousal 方面，声学特征仍然具有一定信息量，适合刻画较低层次的激活度变化。论文还对 EMO-DB 做了质量评估，发现该语料存在表演式语音、文化偏差、类别不兼容以及固定句式导致的文本依赖问题；可见文本未给出具体数值以外的更多实验细节。

<details>
<summary>完整摘要</summary>

我们研究声学情感识别模型是否能够作为政治演讲分析中 Pathos 维度的代理，该维度由 TRUST 多智能体大模型管线进行操作化定义。以德国联邦议院中 Felix Banaszak 的一次全体会议发言为案例（51 个片段，245 秒），我们比较了三种分析方式：（1）emotion2vec_plus_large，一种声学语音情感识别（SER）模型，其连续的 Arousal 和 Valence 值通过事后 Russell Circumplex 投影得到；（2）Gemini 2.5 Flash，一种将整段演讲音频与转写共同纳入、以开放式且具上下文感知能力的方式进行分析的大模型；（3）来自三代理 LLM 审核集成的 TRUST-Pathos 评分。Spearman 秩相关结果显示，Gemini 的 Valence 与 TRUST-Pathos 呈强相关（rho = +0.664，p &lt; 0.001），而 emotion2vec 的 Valence 则不相关（rho = +0.097，p = 0.499）。我们进一步使用 Gemini 以开放式标注范式系统评估 Berlin Database of Emotional Speech（EMO-DB）的质量，证明标准 SER 基准语料普遍存在表演式语音、文化偏差以及类别不兼容问题。结果表明，基于 LLM 的多模态分析比单纯声学模型更能捕捉语义定义下的政治情绪，而声学特征仍对低层次 Arousal 估计有帮助。未来工作将把这一方法扩展到包含面部表情和注视信息的视频分析。

</details>

---

### [[20_Research/Papers/大模型/Post-Training_is_About_States,_Not_Tokens_A_State_Distribution_View_of_SFT,_RL,_and_On-Policy_Distillation|Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation]]

![[assets/2605.22731_first_page.png|800]]

- **arXiv**: [2605.22731](https://arxiv.org/abs/2605.22731)
- **PDF**: https://arxiv.org/pdf/2605.22731
- **详细分析**: [[20_Research/Papers/大模型/Post-Training_is_About_States,_Not_Tokens_A_State_Distribution_View_of_SFT,_RL,_and_On-Policy_Distillation|Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation]]
- **作者**: Dong Nie
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

大模型后训练通常被理解为不同损失函数之间的选择，例如SFT、RL或蒸馏，但这篇工作指出，真正关键的因素还包括“在什么状态上施加监督”。在自回归模型中，状态可以理解为“提示词加上已生成前缀”，而不同训练方法会把监督施加在不同来源的状态分布上。作者认为，这一视角有助于解释SFT为何有时会遗忘、RL为何可能更稳定，以及蒸馏学生为何有时能超过教师，因此值得关注。

#### 方法概述和架构

论文提出一个“状态分布视角”，将后训练拆解为两个轴：状态来源与信号来源。SFT对应的是数据集轨迹上的离策略状态拟合，RL对应的是当前策略采样得到的在策略局部改进，OPD则是学生自己采样状态、教师在这些状态上提供局部监督的在策略蒸馏。作者把后训练统一表示为：先从某个训练状态分布中取状态，再由某个信号提供器生成监督对象，最后更新模型参数，并由更新后的策略诱导新的状态分布。实验上使用 Qwen3-0.6B-Base，在 GSM8K 上做目标任务训练，并用 TruthfulQA 和 MMLU 评估保持能力与遗忘情况，同时比较轻量SFT、压力更大的SFT、基于退化教师的OPD，以及轻量在策略RL。

#### 实验结果分析

实验在单卡、Qwen3-0.6B-Base、GSM8K/TruthfulQA/MMLU 设置下进行，重点考察目标性能与保留性能。结果显示，轻量SFT可以提升 GSM8K 且几乎不遗忘，而高强度SFT会带来明显的保留能力损失。更有意思的是，基于一个已经退化的SFT教师进行的OPD，仍能在 GSM8K、TruthfulQA 和 MMLU 上超过该教师；轻量在策略RL也能提升 GSM8K 并较好保持保留能力。文中强调，单纯用一个标量漂移指标并不足以解释遗忘，状态来源与局部性同样重要。

<details>
<summary>完整摘要</summary>

诸如监督微调（SFT）、强化学习（RL）和蒸馏等大语言模型后训练方法，常常是从它们的损失函数来分析的：最大似然、策略梯度、正向KL、反向KL，或相关的目标函数变体。我们研究一个互补因素：施加监督时所依赖的状态分布。对于自回归策略而言，状态是提示词加上已生成的前缀。SFT在固定的数据集状态上训练，而RL和在策略蒸馏（OPD）则在当前学习器诱导的状态上训练。我们将后训练形式化为状态分布塑形，并在一个可控的小规模研究中使用 Qwen3-0.6B-Base，在 GSM8K 上进行实验，并以 TruthfulQA 和 MMLU 作为保留能力评估。结果显示三种现象。第一，轻量的 SFT 可以提升 GSM8K 且几乎不遗忘，而高强度的 SFT 会造成显著的保留能力损失。第二，来自一个性能已经退化的 SFT 教师的 OPD，尽管只把该教师作为唯一监督来源，却仍能在 GSM8K、TruthfulQA 和 MMLU 上超过教师本身。第三，轻量的在策略 RL 可以在保持保留能力的同时提升 GSM8K。这些结果支持一种以状态为中心的后训练观点：训练状态的来源与局部性，和监督信号的形式一样重要。

</details>

---

### [[20_Research/Papers/强化学习/Abstraction_for_Offline_Goal-Conditioned_Reinforcement_Learning|Abstraction for Offline Goal-Conditioned Reinforcement Learning]]

![[assets/2605.22711_figure.png|800]]

- **arXiv**: [2605.22711](https://arxiv.org/abs/2605.22711)
- **PDF**: https://arxiv.org/pdf/2605.22711
- **详细分析**: [[20_Research/Papers/强化学习/Abstraction_for_Offline_Goal-Conditioned_Reinforcement_Learning|Abstraction for Offline Goal-Conditioned Reinforcement Learning]]
- **作者**: Clarisse Wibault, Alexander Goldie, Antonio Villares, Maike Osborne, Jakob Foerster
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

离线目标条件强化学习（Offline Goal-Conditioned Reinforcement Learning, GCRL）旨在仅利用静态数据训练一个通用策略，使智能体能够在不同目标下完成长时程任务，常见于机器人控制与通用规划场景。现实数据往往覆盖不完整，且某些区域只包含低质量动作和转移，这会让离线RL在分布外动作、价值估计和策略提取上都更容易失败。本文关注的问题是：除了常见的时间抽象之外，层次化结构是否还能带来“绝对抽象”，从而让智能体在相似状态上下文中复用经验。这个视角对于高维任务中的数据稀疏与泛化问题尤其值得关注。

#### 方法概述和架构

论文提出 Abstractive Reinforcement Learning（ARL）作为离线层次化GCRL的统一框架，核心思想是用“相对化”的 options 替代绑定绝对坐标的 options。ARL 将策略分为高层和低层两部分：高层根据当前状态和目标选择 option，低层根据当前状态和 option 输出动作，但两层使用不同的表示，分别对应高层嵌入 ϕ_h(s,g) 和低层嵌入 ϕ_l(s,ω)。与传统做法不同，ARL 强调 option 应通过动作相似性来学习，即让能诱导相似动作序列的状态-中间目标对共享同一个 option。为适配高层与低层不同的决策时间尺度与表示空间，方法显式使用两个价值函数，将高层决策与低层动作选择解耦。基于这一框架，作者给出两个简单算法：ARLi 通过动作相似性隐式学习 relativised options；ARLe 则进一步在低层 MDP 上显式施加平移不变性，以增强高维操控任务中的泛化能力。

#### 实验结果分析

论文在离线GCRL的实验中系统比较了平坦策略、传统层次策略以及ARL系列方法，涉及高维任务与不同数据覆盖条件。结果显示，引入 relativised options 和相应的表示归纳偏置后，模型在数据存在低质量转移的区域更稳健，整体性能优于平坦策略和锚定在绝对状态空间中的层次方法。作者还报告了消融分析，表明基于动作相似性学习 option、使用双价值函数，以及在低层加入平移不变性，都是性能提升的重要因素。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

马尔可夫决策过程（MDP）在真实世界的目标条件强化学习（GCRL）中，常常由于对称性以及状态-目标对之间共享结构而呈现出显著冗余。虽然离线GCRL中的层次化策略通常被用于通过时间抽象缩短决策时域，我们进一步证明，层次化结构同样能够实现绝对抽象。通过引入相对化的 options，以及为层次结构的不同层级使用不同的表示，我们展示了智能体如何在状态空间的相似上下文中复用经验。基于这一框架，我们提出了两种用于学习相对化 options 并从绝对参考系中抽象出来的简单算法。实验结果表明，这类归纳偏置能够显著提升离线GCRL中的性能。

</details>

---

### [[20_Research/Papers/具身智能/Scout-Assisted_Planning_for_Heterogeneous_Robot_Teams_under_Partially_Known_Environments|Scout-Assisted Planning for Heterogeneous Robot Teams under Partially Known Environments]]

![[assets/2605.22693_figure.jpg|800]]

- **arXiv**: [2605.22693](https://arxiv.org/abs/2605.22693)
- **PDF**: https://arxiv.org/pdf/2605.22693
- **详细分析**: [[20_Research/Papers/具身智能/Scout-Assisted_Planning_for_Heterogeneous_Robot_Teams_under_Partially_Known_Environments|Scout-Assisted Planning for Heterogeneous Robot Teams under Partially Known Environments]]
- **作者**: Hoang-Dung Bui, Abhish Khanal, Raihan Islam Arnob, Gregory J. Stein
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

在部分已知环境中，异构机器人团队需要协同完成导航任务：地面机器人负责沿道路到达目标，但道路是否被阻塞往往只有在实际经过时才会暴露，这会导致频繁回溯和重规划，代价很高。为缓解这一问题，论文引入侦察无人机提前获取环境信息，让地面机器人在更早阶段就能调整路线。现有基于距离的侦察引导虽然有效，但只关注“近不近”，忽略了某条边的信息对地面机器人整体决策究竟有多大影响，因此仍可能把侦察资源浪费在低价值区域。

#### 方法概述和架构

论文提出 Scout-Assisted Planning（SAP）框架，将无人机侦察与地面机器人规划统一到部分可观测图上的高层联合动作建模中。作者先把问题形式化为带侦察者的 Canadian Traveler Problem（CTP-WS），并设计适用于无人机和地面机器人的抽象动作与信念状态表示，使得机器人在获得新观测后能够即时中断并重规划。随后提出基于 Information Gain 的 Action Pruning（IAP）：对候选侦察动作打分，衡量“若提前知道这条边是否阻塞，会对地面机器人行为和总代价产生多大改变”，再保留高价值候选、剪去低价值动作。由于精确计算信息增益代价过高，作者进一步用图神经网络从图结构和当前信念状态直接预测信息增益，从而把原本难以实时运行的评估过程压缩到毫秒级。整体流程上，SAP 先生成侦察候选，再由 IAP 或 GNN 版本的学习型筛选器选择值得侦察的边，最后在这些高价值动作上进行规划与执行。

#### 实验结果分析

作者在三类环境中进行了实验，包括城市河流跨越、乡村村落和密集城市小镇等场景，并与 Canadian Traveler Problem 基线以及基于距离的侦察引导方法进行比较。结果显示，采用信息增益引导的 SAP 相比 CTP 基线可将地面机器人的行驶代价降低 31.9%–37.7%，并且相较于基于距离的侦察策略还能进一步降低 8%–14%。节选文本还表明，GNN 近似器在保持解质量的同时显著减少规划时间，使系统更接近实时部署需求；更细的消融与具体数值在节选中未完整展开。

<details>
<summary>完整摘要</summary>

自主机器人团队在部分已知环境中导航时，如果地面机器人遇到阻塞道路，而这些阻塞只有在实际穿越后才会被发现，就会产生代价高昂的回溯。为解决这一问题，我们提出 Scout-Assisted Planning（SAP），这是一种异构规划框架，其中侦察无人机（UAV）主动收集环境信息，以提升无人地面车（UGV）的导航效果。为了将侦察聚焦于最关键的边，我们提出基于 Information Gain 的 Action Pruning（IAP），它根据候选侦察动作对地面机器人行为的预期影响进行打分。由于精确计算 IAP 的代价过高，我们进一步开发了一个基于图神经网络（GNN）的模型，能够直接从图结构和信念状态预测信息增益值，从而将规划时间降低到实时水平，同时不牺牲解质量。跨三类环境的实验表明，采用 Information Gain Action Pruning 的 SAP（SAP-IAP）相较于 Canadian Traveler Problem（CTP）基线，可将地面机器人的行驶代价降低 31.9%–37.7%，并且比基于距离的侦察引导方法进一步降低 8%–14%，说明基于信息增益原则引导侦察在实际部署中既更有效，也具有可计算性。

</details>

---

### [[20_Research/Papers/大模型/WorkstreamBench_Evaluating_LLM_Agents_on_End-to-End_Spreadsheet_Tasks_in_Finance|WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance]]

![[assets/2605.22664_figure.png|800]]

- **arXiv**: [2605.22664](https://arxiv.org/abs/2605.22664)
- **PDF**: https://arxiv.org/pdf/2605.22664
- **详细分析**: [[20_Research/Papers/大模型/WorkstreamBench_Evaluating_LLM_Agents_on_End-to-End_Spreadsheet_Tasks_in_Finance|WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance]]
- **作者**: Thomson Yen, Julian Poeltl, Harshith Srinivas Gear, Yilin Meng, Joshua Fan, Adam Shen, Yili Liu, Ali Bauyrzhan, Siri Du, Haoyang Liu, Daniel Guetta, Hongseok Namkoong
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

大模型代理正在从“回答问题”走向“端到端完成任务”，其中一个典型场景就是金融行业里的电子表格建模、预测和情景分析。现有 spreadsheet 基准大多只评估单公式编辑或问答能力，无法衡量代理从零构建完整、多工作表财务模型的真实能力。论文关注这一空缺，因为在金融工作流中，交付物往往要经过多方审核与反复修改，质量不只是算对结果，还包括可读性、结构清晰度和后续可修改性。

#### 方法概述和架构

论文提出 WorkstreamBench，用于评估 LLM agents 在金融场景下完成端到端 spreadsheet 任务的能力。数据集主要来自 Financial Modeling World Cup（FMWC）、ModelOff 和 Wall Street Prep（WSP）等来源，任务覆盖估值、三表建模、情景分析等真实金融工作流。作者将任务按难度分为多个等级，并标注任务类型，以便分析不同复杂度下的表现差异。为适配“完整工作簿”这一输出形式，论文设计了三维评价体系：Accuracy、Formula 和 Format，每个维度进一步细分为更具体的子指标，例如是否正确完成场景分析、公式是否稳健可审计、表格结构是否专业易读。由于这些标准难以通过简单的程序规则判断，论文还构建了基于 LLM 的 judge 流程，并用专家检查其判断与人工评估的一致性。

#### 实验结果分析

实验在 WorkstreamBench 上比较了多种 API 模型和 GUI/Excel 代理，指标围绕 Accuracy、Formula、Format 三个维度展开。结果显示，Claude 系列整体领先，其中 Claude Web 在三个核心维度上都表现最好，输出也最接近专业金融人员的工作产物。与此同时，即使是最强代理，也经常达不到专业金融标准；当任务复杂度超过少量链式计算后，性能会明显下降。节选文本还指出，任务规模显著大于以往 spreadsheet benchmark：golden solution 的平均单元格数约为传统基准的 33 倍，中位函数调用数约为 93 倍。

<details>
<summary>完整摘要</summary>

LLM 代理越来越被期待能够执行端到端工作流，并在高层级用户指令下生成完整的产物。为满足企业需求，前沿 AI 实验室已经开发出能够从零构建整张电子表格的代理。这一点在金融领域尤为重要，因为财务建模、预测和情景分析等核心工作流通常都通过电子表格完成。然而，现有的 spreadsheet 基准并不衡量这种更高级的能力，而是主要聚焦于问答或单公式编辑。为弥补这一空白，我们提供了针对端到端 spreadsheet 任务的最早一批评估之一，重点关注经济上至关重要的金融工作流，如建模和情景分析。由于这些交付物通常会被多个利益相关方审阅和修改，因此其质量评判必然涉及可读性或易修改性等高层标准。为了反映解答质量的多维性质，我们构建了一个评价分类体系，包含三个维度：Accuracy、Formula 和 Format，每个维度又由反映专业标准的细粒度准则组成。Claude 系列在该基准上领先，并在定性审查中产出最具专业外观的结果，但即便最强的代理也经常达不到金融专业标准，而且当难度增加到超出少量链式计算时性能会急剧下降。这表明当前代理还无法可靠地生成达到真实世界工作流所要求复杂度的专业级电子表格。

</details>

---

### [[20_Research/Papers/大模型/Spreadsheet-RL_Advancing_Large_Language_Model_Agents_on_Realistic_Spreadsheet_Tasks_via_Reinforcement_Learning|Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning]]

![[assets/2605.22642_figure.png|800]]

- **arXiv**: [2605.22642](https://arxiv.org/abs/2605.22642)
- **PDF**: https://arxiv.org/pdf/2605.22642
- **详细分析**: [[20_Research/Papers/大模型/Spreadsheet-RL_Advancing_Large_Language_Model_Agents_on_Realistic_Spreadsheet_Tasks_via_Reinforcement_Learning|Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning]]
- **作者**: Banghao Chi, Yining Xie, Mingyuan Wu, Jingcheng Yang, Jize Jiang, Zhaoheng Li, Shengyi Qian, Minjia Zhang, Klara Nahrstedt, Rui Hou, Xiangjun Fan, Hanchao Yu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 2.1（加权：大模型 1.3，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

电子表格系统（如 Microsoft Excel、Google Sheets）仍是数据分析、财务建模、供应链管理和日常办公中最核心的工作界面之一，但现有大模型代理多依赖通用 LLM 加提示词和工具调用，面对真实场景里长链路、多步骤、强状态依赖的表格操作时，往往稳定性不足。尤其是在复杂公式、格式处理、跨单元格编辑、验证与回溯等任务上，单纯靠推理时提示很难持续完成。本文值得关注之处在于，它把强化学习直接引入“真实 Excel 环境中的表格代理训练”，尝试把表格自动化从“会问答”推进到“能可靠执行任务”。

#### 方法概述和架构

作者提出 Spreadsheet-RL，一个面向电子表格任务的强化学习微调框架。其核心由三部分组成：一是 Spreadsheet Data Agent，用于从线上论坛自动收集真实表格任务种子，并构造初始表格与目标表格配对数据；二是 Spreadsheet Gym，在真实 Microsoft Excel 与 Python 沙箱中暴露较完整的表格能力，支持多轮交互式编辑；三是 Spreadsheet-native tool harness，为代理提供更适合表格任务的工具集与路由规则，帮助模型决定何时查看工作簿、修改单元格、验证结果或回退操作。训练时，LLM 代理在 Spreadsheet Gym 中根据自然语言任务描述与初始表格逐步执行编辑动作，系统再将生成的最终表格与 oracle 目标表格比对，采用基于结果的奖励进行 GRPO 强化学习优化。为了评估泛化能力，作者还构建了 Domain-Spreadsheet 基准，覆盖金融、供应链等领域任务，用于检验模型在真实业务场景中的迁移表现。

#### 实验结果分析

实验主要在 SpreadsheetBench 和作者构建的 Domain-Spreadsheet 上进行，基线包括 Qwen3 系列模型及其不同工具接口设置。结果显示，Spreadsheet-RL 能显著提升 Qwen3-4B-Thinking-2507 的表现：在 SpreadsheetBench 上的 Pass@1 从 12.0% 提升到 23.4%，在 Domain-Spreadsheet 上从 8.4% 提升到 17.2%。论文还指出，表格原生工具接口、完整工具访问与 RL 后训练三者都对性能有增益，说明提升并不只来自更强模型本身，而是来自“环境设计 + 工具设计 + RL 训练”的组合。进一步分析显示，RL 不仅提高最终准确率，也改善了交互效率和协议遵循行为。

<details>
<summary>完整摘要</summary>

电子表格系统（如 Microsoft Excel、Google Sheets）在现代数据密集型工作流中占据核心地位。随着 AI 代理在自动化复杂任务方面日益强大，例如控制计算机和生成演示文稿，构建一个由 AI 驱动的电子表格代理已成为一个很有前景的研究方向。现有大多数电子表格代理依赖于对通用大模型进行专门提示；这种设计在简单的电子表格操作上有一定潜力，但在真实应用中常见的复杂、多步骤工作流上却难以胜任。我们提出 Spreadsheet-RL，这是一个面向真实 Microsoft Excel 环境、用于训练专门电子表格代理的强化学习（RL）微调框架。Spreadsheet-RL 包含一个自动化流水线，可从在线论坛大规模收集成对的起始表格和目标表格；同时还提供面向金融和供应链管理等领域的专门评测任务，我们将其整理为新的 Domain-Spreadsheet 基准数据集。它还包含一个 Spreadsheet Gym 环境，专为多轮 RL 设计：Spreadsheet Gym 通过 Python 沙箱暴露了丰富的 Excel 功能，并配备了经过改进的执行框架，其中包含全面的工具集以及为电子表格任务精心设计的工具路由规则。通过全面实验，我们表明 Spreadsheet-RL 显著提升了 AI 代理在通用与领域特定电子表格任务上的表现：它将 Qwen3-4B-Thinking-2507 在 SpreadsheetBench 上的 Pass@1 从 12.0% 提升到 23.4%，并将其在我们整理的 Domain-Spreadsheet 数据集上的 Pass@1 从 8.4% 提升到 17.2%。这些结果表明，Spreadsheet-RL 在电子表格自动化方面具有很强的泛化潜力和真实落地前景，也更广泛地展现了其推动大模型与日常工作中的数据接口交互的能力。

</details>

---

### [[20_Research/Papers/大模型/Agentic_CLEAR_Automating_Multi-Level_Evaluation_of_LLM_Agents|Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents]]

![[assets/2605.22608_first_page.png|800]]

- **arXiv**: [2605.22608](https://arxiv.org/abs/2605.22608)
- **PDF**: https://arxiv.org/pdf/2605.22608
- **详细分析**: [[20_Research/Papers/大模型/Agentic_CLEAR_Automating_Multi-Level_Evaluation_of_LLM_Agents|Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents]]
- **作者**: Asaf Yehudai, Lilach Eden, Michal Shmueli-Scheuer
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

随着 LLM Agent 在软件工程、科学发现和网页浏览等场景中不断增强自主性，开发者越来越需要一套能够审视其行为、定位失败原因的评估工具。现有观测平台大多偏向日志记录，只能做基础指标汇总或对整条轨迹进行粗粒度打分，难以发现循环、子代理失配、错误逐步传播等隐蔽问题。另一方面，现有错误分类法往往是静态、人工设计的，面对新任务和新领域时缺乏适应性。因此，这篇论文聚焦“Agent 如何被自动、动态、分层地评估”这一实际痛点，具有较强的工程与研究价值。

#### 方法概述和架构

论文提出 Agentic CLEAR，一个面向 LLM Agent 的自动化多层级评估框架。它的输入是任务数据集与 Agent 运行产生的执行轨迹，轨迹中包含每一步的输入、输出以及对应节点；输出则是三个层级的可解释诊断结果：系统级、轨迹级和节点级。方法分两阶段运行：第一阶段对每条轨迹执行 LLM judge 评估，分别产生步级评价、整条轨迹评价，以及基于任务自动生成 rubric 的符合性检查；第二阶段再用 CLEAR 对这些逐实例反馈进行聚类与归纳，提炼出系统范围内的共性问题和各节点特有的问题。框架将节点级反馈按组件汇总、将轨迹级反馈按整体行为汇总，并把每条洞见关联到触发它的具体步骤或轨迹，从而支持开发者从局部到全局追踪失败原因。论文还提供了可直接集成的 Python 包和交互式 UI，支持从 OpenTelemetry / LangFuse 轨迹格式导入数据，并允许用户替换 judge 或自定义评估维度。

#### 实验结果分析

作者在四个基准、七种 agent 设置以及数万次 LLM 调用上验证了 Agentic CLEAR，实验涵盖 SWE-Bench Verified Mini、GAIA、AppWorld 和 τ²-Bench 等数据集，并比较了不同 Agent 与不同底座模型的轨迹。结果表明，该框架能够给出高质量、数据驱动且有洞见的反馈；其自动归纳出的错误模式与人工标注的错误分类具有较强一致性。论文还指出，框架能够预测任务成功率，并进一步分析了不同 judge 选择、模型差异以及 rubric 设计对评估结果的影响。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

随着 Agent 系统变得越来越强大，它们能够制定策略、采取行动，并与不同环境交互。这种自主性也给监督和评估 Agent 行为带来了严峻挑战。当前大多数工具仍然比较有限：要么只关注可观测性并提供基础的评估能力，要么依赖静态、人工设计的错误分类体系，而这些体系无法适应新的领域。为了解决这一缺口，我们提出 Agentic CLEAR，一个自动化、动态且易于使用的评估框架。它能够在三个粒度层面生成关于 Agent 行为的文本化洞见：系统层、轨迹层和节点层。Agentic CLEAR 工作在可观测性层之上，因此可以无缝集成，并通过直观的 UI 使 Agent 评估变得高度可访问。我们在四个基准、七种 Agent 设置以及数万次 LLM 调用上的实验表明，Agentic CLEAR 能够生成高质量、数据驱动且富有洞见的反馈。我们的分析显示，它与人工标注的错误具有很强的一致性，并且能够预测任务成功率。

</details>

---

### [[20_Research/Papers/具身智能/MoSA_Motion-constrained_Stress_Adaptation_for_Mitigating_Real-to-Sim_Gap_in_Continuum_Dynamics_via_Learning_Residual_Anisotropy|MoSA: Motion-constrained Stress Adaptation for Mitigating Real-to-Sim Gap in Continuum Dynamics via Learning Residual Anisotropy]]

![[assets/2605.22597_figure.png|800]]

- **arXiv**: [2605.22597](https://arxiv.org/abs/2605.22597)
- **PDF**: https://arxiv.org/pdf/2605.22597
- **详细分析**: [[20_Research/Papers/具身智能/MoSA_Motion-constrained_Stress_Adaptation_for_Mitigating_Real-to-Sim_Gap_in_Continuum_Dynamics_via_Learning_Residual_Anisotropy|MoSA: Motion-constrained Stress Adaptation for Mitigating Real-to-Sim Gap in Continuum Dynamics via Learning Residual Anisotropy]]
- **作者**: Jiaxu Wang, Junhao He, Jingkai Sun, Yi Gu, Yunyang Mo, Jiahang Cao, Qiang Zhang, Renjing Xu
- **cs 子类**: cs.AI, cs.GR, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

在具身智能和机器人操控中，从多视角视频学习可变形物体的真实动力学，是实现高质量仿真、数字孪生以及 sim-to-real 迁移的关键。现有做法通常先用物理参数标定模拟器，但这类方法受限于基础物理模型，往往默认材料是均匀、各向同性的，难以刻画现实物体中普遍存在的轻微各向异性与空间非均匀性。作者指出，当近似各向同性的主干模型已经校准到较好水平后，这些“残余效应”往往成为继续缩小 real-to-sim gap 的主要瓶颈，因此值得专门建模。

#### 方法概述和架构

论文提出 MoSA（Motion-constrained Stress Adaptation），核心思路是在各向同性 constitutive model 的物理先验之上，只学习用于补偿残余各向异性和异质性的应力修正算子。方法采用渐进式的应力适配机制：先保留校准好的 isotropic backbone，再通过受 microplane 约束的重分配网络，逐步把应力从近似各向同性状态修正到更符合真实材料的响应。为了避免仅靠像素重建带来的欠约束问题，MoSA 还引入 motion constraints，对由动态重建得到的形变场进行时间和空间导数监督，从而提供更直接的运动/形变约束。整体流程上，输入是多视角视频和相机参数，先进行动态 3D 重建提取运动线索，再把这些线索与物理模拟中的状态一起送入物理信息驱动的级联网络，输出修正后的应力与更准确的动力学演化。

#### 实验结果分析

作者在合成数据与真实数据上进行了实验，结果表明 MoSA 在精度、泛化性和鲁棒性上都优于对比方法，并且学到的残余各向异性具有物理可解释性。正文节选中没有给出具体数值，因此可见文本未给出具体数值。论文还在机器人操作场景中验证了方法的实用性，说明更好的 real-to-sim 动力学建模能够带来更可靠的 sim-to-real 迁移。

<details>
<summary>完整摘要</summary>

从视觉观测中学习真实世界动力学对于许多领域都至关重要。一个常见策略是通过估计物理参数来校准模拟器，但其精度最终受底层物理模型的限制，而这些模型通常假设材料是均匀且各向同性的。即使这种近似在很多情况下是合理的，现实中的物体通常仍会表现出轻微的各向异性和非均匀性。当近似各向同性的主干模型已经被很好地校准之后，这些残余效应就会成为进一步缩小 real-to-sim gap 的关键瓶颈。尽管神经网络可以端到端拟合动力学，但这种黑箱建模会丢失强物理先验，从而导致数据效率差并容易过拟合。因此，我们提出 MoSA，一种 motion-constrained stress adaptation 框架，专门针对这些残余效应以进一步提升 real-to-sim 动力学学习。MoSA 以各向同性模型作为物理先验，并学习残余应力算子来刻画轻微的各向异性和异质性。它通过在物理信息驱动的级联网络中、借助 microplane 约束的重分配机制，逐步适配应力。我们进一步通过对形变场的时间导数和空间导数进行监督，引入运动约束。实验表明，我们学习到的动力学在精度、泛化性和鲁棒性上都更优，同时还能学习到具有物理意义的残余各向异性。最后，我们在机器人操作任务中验证了 MoSA，表明更好的 real-to-sim 动力学建模能够转化为更可靠的 sim-to-real 迁移。项目主页见 https://mercerai.github.io/MoSA/ 。

</details>

---

### [[20_Research/Papers/大模型/Understanding_Multimodal_Failure_in_Action-Chunking_Behavioral_Cloning|Understanding Multimodal Failure in Action-Chunking Behavioral Cloning]]

![[assets/2605.22493_figure.png|800]]

- **arXiv**: [2605.22493](https://arxiv.org/abs/2605.22493)
- **PDF**: https://arxiv.org/pdf/2605.22493
- **详细分析**: [[20_Research/Papers/大模型/Understanding_Multimodal_Failure_in_Action-Chunking_Behavioral_Cloning|Understanding Multimodal Failure in Action-Chunking Behavioral Cloning]]
- **作者**: Lorenzo Mazza, Massimiliano Datres, Ariel Rodriguez, Sebastian Bodenstedt, Gitta Kutyniok, Stefanie Speidel
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

在机器人模仿学习中，行为克隆（Behavioral Cloning, BC）常被用于直接从专家演示中学习动作策略，但当同一观测对应多个都合理的动作时，模型很容易把多模态行为“平均”掉，导致输出落在任何一个有效模式之外。对于动作分块（action-chunking）策略而言，这一问题尤为突出，因为策略需要一次性生成一段未来动作，既要保持时序一致性，又要保留不同示范模式。本文关注具身智能和机器人操作中的这一核心瓶颈，试图解释为什么一些多模态参数化在训练或部署时会失效，以及失效的根源究竟来自潜变量约束还是生成映射的平滑性。

#### 方法概述和架构

论文把多模态动作分布建模分成两类：基于潜变量的条件策略，以及在动作空间上直接生成的策略。对于潜变量方法，模型由后验编码器、条件先验和潜变量解码器组成，训练时使用带正则项的目标函数，通过控制后验与先验之间的匹配强度来影响模式保留能力；推理时从先验采样潜变量，再解码得到动作块。对于动作空间生成方法，模型把基分布噪声通过确定性映射变成动作，覆盖扩散或flow matching一类一阶段采样器，其输出是动作分布的推前分布。作者进一步从理论上定义“模式保留”和“多模态坍塌”，分析点式KL正则、聚合匹配以及生成映射的Lipschitz约束如何影响多模态表达能力，并用合成多模态任务与机器人仿真基准进行验证。

#### 实验结果分析

实验在合成多模态任务和机器人仿真基准上展开，并与多种代表性基线比较，包括确定性BC、KL-CVAE、聚合匹配潜变量策略、LAT-Flow、Residual VQ-VAE，以及动作空间流模型和扩散模型。结果表明，单纯提高后验-先验正则可以让部署时采样更稳定，但过强正则会抹掉区分不同示范模式所需的动作条件信息；而减弱正则虽然能保留模式信息，却又依赖先验是否覆盖到相关潜空间区域。对于动作空间生成策略，实验支持“平滑映射难以同时覆盖大量彼此分离的模式”这一结论，说明要想覆盖更多模式，要么在基空间出现更尖锐的变化，要么在动作空间引入桥接区域。节选文本未给出具体数值，但整体结论清晰指向：多模态失败并非单一训练技巧问题，而是由潜变量信息保留、先验覆盖与生成映射平滑性共同决定。

<details>
<summary>完整摘要</summary>

当同一观测对应多个有效动作时，行为克隆会变得困难。我们研究了动作分块策略中的这一问题，并表明不同的多模态参数化方式会以不同方式失效。对于潜变量策略，后验-先验正则化能够让部署时采样更可靠，但过强的正则会去除区分已示范模式所需的动作条件信息。减弱这种正则可以保留模式信息，但此时成功与否取决于先验是否覆盖相关的潜变量区域。对于动作空间生成策略，多模态能力受到底层到动作映射平滑性的约束：一个Lipschitz常数较小的映射，无法把足够大的概率质量分配给许多彼此分离的模式。因此，要覆盖更多模式，要么需要在基空间中出现尖锐的过渡，要么需要在动作空间中存在离支持集的桥接区域。我们在合成多模态任务和机器人仿真基准上的实验支持了这些机制。

</details>

---

### [[20_Research/Papers/强化学习/Don't_Forget_the_Critic_Value-Based_Data_Rehearsal_for_Multi-Cyclic_Continual_Reinforcement_Learning|Don't Forget the Critic: Value-Based Data Rehearsal for Multi-Cyclic Continual Reinforcement Learning]]

![[assets/2605.22454_first_page.png|800]]

- **arXiv**: [2605.22454](https://arxiv.org/abs/2605.22454)
- **PDF**: https://arxiv.org/pdf/2605.22454
- **详细分析**: [[20_Research/Papers/强化学习/Don't_Forget_the_Critic_Value-Based_Data_Rehearsal_for_Multi-Cyclic_Continual_Reinforcement_Learning|Don't Forget the Critic: Value-Based Data Rehearsal for Multi-Cyclic Continual Reinforcement Learning]]
- **作者**: Benjamin Poole, Andrew Quinn, Li Yang, Minwoo Lee
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

持续强化学习（Continual Reinforcement Learning, CRL）旨在让智能体在任务序列中不断学习，同时尽量避免对旧任务能力的灾难性遗忘。现有基于数据回放（data rehearsal）的方法主要集中在策略梯度框架中，通常只对 actor 做正则化，因为对 critic 进行约束往往会带来性能下降。作者指出，这种“只关注 actor”的做法忽略了价值函数近似中的回放潜力；此外，现有 CRL 评测很少考虑多周期场景，即任务序列会重复出现，这在真实应用中很常见，也会进一步放大遗忘与可塑性之间的矛盾。因此，这篇论文关注价值函数层面的数据回放，并将评测拓展到更贴近现实的多周期持续学习设置。

#### 方法概述和架构

论文以 Deep Q-Networks 为基础，在价值函数近似场景中研究 Q 值正则化的数据回放方法，核心方法名为 Qreg+NWLU。与已有 Qreg 相比，它引入了两个简单但关键的改动：其一是“持续数据回放”，即在整个训练过程中动态收集并更新存储的 Q 值，而不是只在某个固定阶段回放；其二是“No-Wait” 正则化，即从训练一开始就立即施加正则，而不是等到完成第一个任务后再开始。方法的输入是训练过程中采样到的经验及其对应的 Q 值目标，输出则是带有回放约束的 Q 学习更新信号。整体流程是在多周期任务序列上持续训练 DQN，同时用历史 Q 值作为记忆锚点约束当前预测，从而兼顾旧知识保持与新任务适应。

#### 实验结果分析

作者在多周期持续强化学习环境中，将 Qreg+NWLU 与 Qreg 以及传统 CRL 方法进行对比，评估重点包括学习效率、遗忘缓解和知识迁移能力。结果表明，该方法在价值函数近似设置下带来了更好的综合表现，尤其是在减少遗忘和促进跨任务迁移方面更有优势。文中摘要未给出具体实验数值，因此可见文本未给出具体数值。总体上，实验支持了“对 critic 进行数据回放正则化”这一思路在多周期 CRL 中是有效的。

<details>
<summary>完整摘要</summary>

数据回放已成为缓解持续强化学习（Continual Reinforcement Learning, CRL）中灾难性遗忘的领先方法。然而，现有工作仍然局限于策略梯度框架，并且由于对 critic 进行正则化会导致性能下降，因此只对 actor 进行约束。这种以 actor 为中心的方法忽视了数据回放在价值函数近似中的潜力。此外，现有 CRL 评测很少考虑多周期环境，即任务序列会重复出现；这是一类关键的真实世界场景，它会加剧遗忘与可塑性之间的矛盾。我们在多周期设置下，针对 Deep Q-Networks 研究了使用 Q 值正则化的数据回放，并提出了 Qreg+NWLU。该方法引入两个简单改动：（1）持续数据回放，在整个训练过程中动态收集并更新存储的 Q 值；（2）“No-Wait” 正则化，即不等待第一个任务结束，而是在训练开始后立即施加正则。二者结合后，相比 Qreg 和传统 CRL 方法，在价值函数近似设置下，能够提升学习效率、缓解遗忘并增强知识迁移能力。

</details>

---

### [[20_Research/Papers/具身智能/Pre-VLA_Preemptive_Runtime_Verification_for_Reliable_Vision-Language-Action_and_World-Model_Rollouts|Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts]]

![[assets/2605.22446_figure.png|800]]

- **arXiv**: [2605.22446](https://arxiv.org/abs/2605.22446)
- **PDF**: https://arxiv.org/pdf/2605.22446
- **详细分析**: [[20_Research/Papers/具身智能/Pre-VLA_Preemptive_Runtime_Verification_for_Reliable_Vision-Language-Action_and_World-Model_Rollouts|Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts]]
- **作者**: Zhen Sun, Yongjian Guo, Haoran Sun, Luqiao Wang, Wei Lu, Jiachi Ji, Shengzhe Ji, Junwu Xiong, Zhijun Meng
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 3.6（加权：具身智能 3，大模型 0.1，世界模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

在具身智能任务中，VLA 模型和生成式世界模型已经能支持长时序控制与未来轨迹想象，但它们在真实部署时仍受限于动作生成的不确定性：一旦输出低质量动作，可能在物理执行中引发碰撞、掉落或不可逆的运动错误，也可能让世界模型滚动预测出现漂移、失真和错误成功的“幻觉”结果。现有方法多是在动作执行之后或预测之后再做检查，难以及时阻断风险动作，而且对多模态输入的处理往往计算开销较大，不适合机器人连续运行。该工作因此聚焦“动作进入执行或想象之前”的预验证问题，试图在有限算力预算下同时兼顾安全性和效率。

#### 方法概述和架构

论文提出 Pre-VLA，一种统一的运行时验证架构，用于在物理执行和世界模型想象之前，对候选动作块进行预先有效性评估。其输入包括语言指令、视觉观测、本体状态以及 VLA 生成的动作块，作者基于高效的多模态骨干网络进行联合表征，并通过模态感知池化把不同来源的特征分离与聚合。随后，轻量级双分支头同时输出动作安全置信度和由 Critic 推导的 advantage 分数，用分类与回归两个视角衡量动作质量。训练时采用多任务目标，将 Focal classification、advantage 回归和 soft-threshold 校准结合起来，以缓解安全/危险样本的严重类别不均衡，并稳定安全边界附近的决策。推理阶段采用双模式预emptive resampling scheduler，在物理执行和世界模型滚动两种场景下过滤低质量动作，并在受限计算预算内触发自适应重采样。

#### 实验结果分析

论文在 LIBERO 机器人操作基准上进行了评测，覆盖动作有效性判别、闭环执行、世界模型滚动、消融实验和案例分析。结果显示，Pre-VLA 将四个 suite 上的平均闭环成功率从 30.79% 提升到 37.62%（相较 RynnVLA-002），同时减少了任务执行步数，说明动作过滤有助于更快进入有效轨迹。该方法的单个动作块前向验证平均耗时为 183.9 ms，表明其额外开销可控；在世界模型滚动中也能抑制错误累积与视觉漂移。节选文本还给出了独立测试集上的 F1=0.8303、Accuracy=0.9542，以及对无效动作的低误放行率 0.0200，消融结果表明多任务训练和阈值校准对性能提升具有关键作用。

<details>
<summary>完整摘要</summary>

尽管大型视觉-语言-动作（VLA）模型和生成式世界模型（WM）已经推动了长时序具身智能的发展，但它们在实际部署中仍然受到学习式动作生成不确定性的挑战。低质量动作可能在执行过程中导致物理失败，也可能在世界模型想象中造成误导性的滚动结果，并带来额外且冗余的渲染计算开销。为了解决这一问题，我们提出 Pre-VLA，一种统一的运行时验证架构，能够在物理执行或世界模型想象之前，对动作有效性进行预先评估。Pre-VLA 利用高效的多模态骨干网络、模态感知池化以及轻量级双分支预测头，同时预测候选动作块的安全置信度和由 critic 推导的 advantage 分数。为了应对严重的类别不均衡和不稳定的边界决策，我们采用多任务目标进行训练，将 Focal 分类、advantage 回归和 soft-threshold 校准结合起来。部署阶段，双模式的预emptive 重采样调度器会在有限计算预算下过滤低质量动作，并在需要时触发自适应重采样。LIBERO 基准实验表明，Pre-VLA 相比 RynnVLA-002，将四个 suite 上的平均闭环成功率从 30.79% 提升到 37.62%，减少了任务执行步数，单个动作块的平均前向验证时间为 183.9 ms，并能缓解世界模型滚动中的误差累积。

</details>

---

### [[20_Research/Papers/大模型/DeferMem_Query-Time_Evidence_Distillation_via_Reinforcement_Learning_for_Long-Term_Memory_QA|DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA]]

![[assets/2605.22411_figure.png|800]]

- **arXiv**: [2605.22411](https://arxiv.org/abs/2605.22411)
- **PDF**: https://arxiv.org/pdf/2605.22411
- **详细分析**: [[20_Research/Papers/大模型/DeferMem_Query-Time_Evidence_Distillation_via_Reinforcement_Learning_for_Long-Term_Memory_QA|DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA]]
- **作者**: Jianing Yin, Tan Tang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.67（加权：大模型 0.55，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

长程记忆问答要求大模型智能体从跨多轮、跨会话的历史对话中找出支撑答案的证据，但这些证据往往分散、稀疏，还被大量无关内容淹没。现有记忆系统通常在不知道未来问题的情况下就先整理记忆，随后只按相似度检索，导致检索结果虽然“相关”，却未必真正有助于回答当前问题。论文值得关注之处在于，它把“先检索、后回答”进一步拆成“先高召回找候选、再按查询蒸馏证据”，直接针对记忆系统中最棘手的去噪和证据重建环节。

#### 方法概述和架构

论文提出 DeferMem，用于长程记忆问答的查询时证据蒸馏框架。它包含两个核心模块：其一是轻量级的 segment-link 结构，在原始历史上构建分段、段间链接和消息级索引，查询到来时先通过向量相似度找到 top-k 消息，再扩展到所在段和相邻语义相关段，形成高召回但较嘈杂的候选集合；其二是 memory distiller，将这些候选进一步压缩为自包含、忠实且面向当前查询的证据。蒸馏器通过 DistillPO 训练，DistillPO 把后检索蒸馏建模为结构化动作，包含“消息选择”和“证据改写”两步，并用分解式奖励管线与带门控的层级奖励传播来优化。训练时，它既让任务级正确性信号尽早起作用，又把每个奖励分配给对应的输出片段，从而学习如何从噪声候选中生成可直接供下游回答的证据。

#### 实验结果分析

作者在 LoCoMo 和 LongMemEval-S 上进行了实验，并与强基线比较，评估指标包括 QA 准确率、记忆系统效率以及运行开销。结果表明，DeferMem 在 QA 准确率上优于现有方法，同时具备更快的运行速度，并且记忆操作不依赖商业 API token，成本更低。消融和分析还显示，segment-link 检索与 DistillPO 蒸馏两个环节都对最终性能有关键贡献。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

大型语言模型（LLM）智能体在长程记忆问答任务上仍然面临困难：支撑答案的证据常常分散在漫长的对话历史中，并被大量无关内容所掩埋。现有记忆系统通常会在未来查询尚未知晓之前先处理记忆，然后再依据相似度而不是其对回答该查询的实际效用来检索生成的记忆单元。这种流程使得下游回答器不得不对检索到的候选进行去噪，并重新构建与查询相关的证据。我们提出 DeferMem，这是一个长程记忆框架，它将该问题解耦为高召回候选检索和查询条件化的证据蒸馏。DeferMem 使用一种轻量级的 segment-link 结构来组织原始历史，并在查询时检索宽泛的候选集。随后，它引入一个 memory distiller，并用 DistillPO 训练该模块，将高召回但高度嘈杂的候选蒸馏为一组忠实、自包含且与查询条件化的证据。DistillPO 将检索后的证据蒸馏表述为一种结构化动作，包含消息选择和证据改写。它通过分解式并带门控的奖励流水线，以及结构对齐的优势分配来优化这一动作：一方面从有效性到质量检查逐级门控奖励成分，另一方面尽早暴露任务级正确性反馈，并把每个奖励分配给其负责的输出片段。在 LoCoMo 和 LongMemEval-S 上，DeferMem 在 QA 准确率和记忆系统效率方面都超过了强基线，取得了最高的 QA 准确率、最快的运行时间，并且在记忆操作上实现了零商业 API token 成本。

</details>

---

### [[20_Research/Papers/强化学习/Incentive-Aligned_Vehicle-to-Vehicle_Energy_Trading_via_Nash-Integrated_Multi-Agent_Reinforcement_Learning|Incentive-Aligned Vehicle-to-Vehicle Energy Trading via Nash-Integrated Multi-Agent Reinforcement Learning]]

![[assets/2605.22363_figure.png|800]]

- **arXiv**: [2605.22363](https://arxiv.org/abs/2605.22363)
- **PDF**: https://arxiv.org/pdf/2605.22363
- **详细分析**: [[20_Research/Papers/强化学习/Incentive-Aligned_Vehicle-to-Vehicle_Energy_Trading_via_Nash-Integrated_Multi-Agent_Reinforcement_Learning|Incentive-Aligned Vehicle-to-Vehicle Energy Trading via Nash-Integrated Multi-Agent Reinforcement Learning]]
- **作者**: Yujin Lin, Yue Yang, Hao Wang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

电动车到车的能量交易（V2V energy trading）为电动车之间的点对点电能交换提供了去中心化方案，既能降低对电网的依赖，也能把富余电量转化为收益。难点在于，参与者都是自利的电动车代理，且到离场时间、充电需求和私人估值都不确定，传统集中式优化往往算力开销大，纯拍卖式机制又难以给出公平性保证。本文聚焦于如何在动态、私有信息和持续车辆更替的场景下，同时实现激励相容近似、社会福利提升和公平交易，因此具有较强的现实应用价值。

#### 方法概述和架构

论文提出 Nash-MADDPG，将 Nash Bargaining Solution 与多智能体深度确定性策略梯度（MADDPG）结合，用于V2V能量交易。其核心是双层机制：上层用 Nash bargaining 进行双边市场清算与定价，在可行交易对上求得双方都接受的折中价格；下层则通过基于 Nash 价格的“价格接近度”奖励，推动智能体在训练中学习接近 bargaining 最优的报价策略。每个电动车智能体只观察本地状态，包括电池电量、缺口/富余、紧迫度、剩余停车时间、历史价格和角色信息，输出报价和交易量；通过角色掩码限制买家、卖家和中性车辆的动作空间。训练采用 CTDE 范式，集中式 critic 利用联合信息缓解非平稳性，执行时各 actor 仅依赖局部观测。市场清算部分将 Nash product 的非凸优化转化为对数形式的凹优化，并用 SLSQP 求解交易分配与更新电池状态。

#### 实验结果分析

作者在30天连续运行场景下评估了该方法，并与 Double Auction 等基线进行比较，同时考察了6到100个智能体、持续车辆更替下的可扩展性与稳定性。结果显示，Nash-MADDPG 相比 Double Auction 的社会福利提升61.6%，交易量提升62.9%，Jain’s index 也提升40.1%，说明其在效率与公平性上同时优于基线。进一步的长周期测试表明，价格能够稳定靠近 Nash Bargaining 参考点，且在不同人口规模下保持良好泛化；正文节选中还提到消融实验与奖励分量分析用于验证 Nash 指导对训练稳定性的作用，但可见文本未给出这些部分的具体数值。

<details>
<summary>完整摘要</summary>

电动车到车能量交易（V2V energy trading）使电动车之间能够去中心化地进行点对点能量交换，在减少对电网依赖的同时，将富余容量变现。然而，在参与者具有自利动机、充电需求各异且到离场时间不确定的情况下，协调这些电动车智能体仍然具有挑战。现有方法要么依赖集中式优化、存在计算上的局限，要么缺乏公平性保证。本文将 Nash Bargaining Solution 融入多智能体深度确定性策略梯度（Multi-Agent Deep Deterministic Policy Gradient），提出 Nash-MADDPG，用于实现激励对齐的V2V能量交易。Nash bargaining 用于确定高效的双边价格，而由 Nash 引导的价格接近度奖励则将智能体学习方向对齐到 bargaining 最优策略。30天连续运行的评估表明，相比 Double Auction，该方法的社会福利提高了61.6%，交易量提高了62.9%，同时在公平性方面表现更优，例如 Jain’s index 提升了40.1%。在6到100个智能体、30天时间跨度且车辆持续更替的测试中，该方法验证了对不同群体规模的可扩展性，并且经验上证明其价格能够稳定地接近 Nash Bargaining 基准。

</details>

---

### [[20_Research/Papers/强化学习/ACCoRD_Actor-Critic_Conflict_Resolution_with_Deep_learning_for_O-RAN_xApps|ACCoRD: Actor-Critic Conflict Resolution with Deep learning for O-RAN xApps]]

![[assets/2605.22306_first_page.png|800]]

- **arXiv**: [2605.22306](https://arxiv.org/abs/2605.22306)
- **PDF**: https://arxiv.org/pdf/2605.22306
- **详细分析**: [[20_Research/Papers/强化学习/ACCoRD_Actor-Critic_Conflict_Resolution_with_Deep_learning_for_O-RAN_xApps|ACCoRD: Actor-Critic Conflict Resolution with Deep learning for O-RAN xApps]]
- **作者**: Cezary Adamczyk, Adrian Kliks
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

在 O-RAN 架构中，Near-Real Time RAN Intelligent Controller 需要同时协调多个 xApps 的控制行为，而不同 xApp 之间可能对同一网络对象发出互相冲突的控制决策，进而引发性能退化或异常网络事件。冲突缓解（ConMit）因此成为智能网络控制中的关键环节，但现有基于规则的方法通常依赖人工设计，面对复杂流量和多源控制逻辑时适应性有限。本文关注的是如何自动识别并消解控制冲突，以减少冲突决策对无线接入网性能的负面影响，这一问题对 O-RAN 的可扩展智能化运维具有现实意义。

#### 方法概述和架构

论文提出 ACCoRD（Actor-Critic Conflict Resolution with Deep learning for O-RAN xApps），用于在 Near-Real Time RAN Intelligent Controller 中执行冲突决策的自动修正。其核心是一个冲突解决（CR）Agent，内部采用人工神经网络（ANN）建模，并通过 PPO-Clip 强化学习算法进行训练。该 ANN 接收网络状态以及发生冲突的控制决策信息作为输入，输出最优的冲突解决动作，用于替代或修正原始控制决策。系统在每次完成冲突处理后，从网络侧收集反馈，以评估该次动作的有效性，并在批量训练阶段据此更新 ANN 权重。整体流程可理解为“冲突检测后输入状态—策略网络生成处理动作—执行后收集反馈—再训练优化策略”，从而让模型逐步学会在不同流量条件下选择更合适的冲突缓解策略。

#### 实验结果分析

作者基于仿真数据对方法进行了评估，并提出了一种新的 CR 解决方案评价方法。实验结果表明，基于 ANN 和强化学习的 ACCoRD 相比基于规则的方法，能够显著减少由冲突控制决策引起的负面网络事件。论文特别指出，这种优势在中等和高负载流量场景下更为明显。可见文本未给出具体数值，因此无法进一步量化提升幅度。

<details>
<summary>完整摘要</summary>

O-RAN 中的冲突缓解（Conflict Mitigation, ConMit）是智能网络控制中的关键组成部分。本文提出一种名为 ACCoRD 的方法，用于在 Near-Real Time RAN Intelligent Controller 中通过一个冲突解决（Conflict Resolution, CR）Agent 来消解已检测到的控制冲突。该 CR Agent 采用一个人工神经网络（ANN），并通过强化学习算法 PPO-Clip 进行训练。实现的 ANN 会分析网络数据以及相互冲突的控制决策信息，从而推断最优的 CR 动作。每当成功解决一次冲突后，CR Agent 都会从网络中收集反馈，以评估其效率，并在批量训练过程中调整 ANN 的权重。本文基于仿真数据对所提出的方法进行了评估，并提出了一种新的 CR 解决方案评估方法。结果表明，所提出的基于 ANN 的方法在中等和高流量场景下，能够显著减少由冲突控制决策导致的负面网络事件，从而在效率上优于基于规则的方法。

</details>

---

### [[20_Research/Papers/具身智能/Action_with_Visual_Primitives|Action with Visual Primitives]]

![[assets/2605.22183_figure.png|800]]

- **arXiv**: [2605.22183](https://arxiv.org/abs/2605.22183)
- **PDF**: https://arxiv.org/pdf/2605.22183
- **详细分析**: [[20_Research/Papers/具身智能/Action_with_Visual_Primitives|Action with Visual Primitives]]
- **作者**: Weilong Guo, Yuchen Wang, Renping Zhou, Yunfeng Zhang, Rui Fang, Yue Meng, Wenda Xu, Yuan He, Gao Huang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 1.2，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

视觉-语言-动作（VLA）模型已成为通用机器人操作的重要路线，适用于抓取、放置、棋类摆放等需要同时理解语言指令、视觉场景和动作控制的具身任务。但现有方法通常把“看懂任务、定位目标、生成动作”压缩到一次前向预测中，导致动作模块不得不重新学习本应由预训练视觉语言模型承担的语义理解与空间推理能力，进而影响学习效率和泛化。尤其在布局变化、物体变化或视觉上高度相似的场景中，这种耦合更容易暴露出定位不稳和迁移能力不足的问题。因此，如何在 VLM 与动作专家之间设计更清晰、可学习的中间接口，是这篇工作值得关注的核心原因。

#### 方法概述和架构

论文提出 AVP（Action with Visual Primitives），把“视觉原语”作为 VLM 与动作专家之间的显式通信媒介。给定多视角图像、语言指令和机器人状态，VLM 先解析当前子任务，并预测下一阶段目标，同时输出离散化的视觉原语 token，这些原语可以表示点、框等紧凑的空间标记。随后，视觉原语会被投影到视觉 token 空间，与原始多模态 token 融合，形成增强表示，再送入 flow-matching 动作专家生成机器人动作。训练时，模型同时优化动作预测损失和视觉原语辅助损失，其中视觉原语监督来自末端执行器运动学提取的真值关键帧或空间目标；推理时无需外部检测器、分割器或手工绘制提示，原语由模型内部直接生成。

#### 实验结果分析

作者在真实机器人平台上评估了 AVP，任务包括中国象棋搬运、骨牌摆放以及通用抓取-放置等高精度操作场景，并与 π_0.5 及其他近期方法比较。结果显示，AVP 的整体成功率相对 π_0.5 提升了 27.61%，同时在数据效率、空间组合泛化和对象级迁移上也表现更稳定。正文节选还指出，该方法在未见过的状态转移与未见物体上的零样本泛化更强；若要给出更细的分项数值，可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

视觉-语言-动作（VLA）模型已经成为通用机器人操作中一个很有前景的范式。当前架构的常见设计是将语言指令和视觉观测在一次前向传播中直接映射为动作。虽然这种形式在概念上很简单，但它把指令理解、场景空间理解和运动控制耦合进了同一个学习目标中。因此，动作专家必须隐式重新学习预训练 VLM 中已经具备的认知与感知能力，这会限制学习效率和泛化能力。我们提出 AVP（Action with Visual Primitives），一种端到端架构，实现了以视觉原语为中心的接口：VLM 推断下一阶段目标，并输出视觉原语 token，用这些 token 去条件化一个 flow-matching 动作专家，而监督信号则来自末端执行器的运动学信息。真实机器人上的一般抓取-放置实验表明，AVP 的成功率相比 π_0.5 提升了 27.61%，并且优于其他近期方法，在数据效率、空间组合泛化和对象级迁移方面也持续取得更好的结果。

</details>

---

### [[20_Research/Papers/大模型/LLM-Metrics_Measuring_Research_Impact_Through_Large_Language_Model_Memory|LLM-Metrics: Measuring Research Impact Through Large Language Model Memory]]

![[assets/2605.22176_figure.png|800]]

- **arXiv**: [2605.22176](https://arxiv.org/abs/2605.22176)
- **PDF**: https://arxiv.org/pdf/2605.22176
- **详细分析**: [[20_Research/Papers/大模型/LLM-Metrics_Measuring_Research_Impact_Through_Large_Language_Model_Memory|LLM-Metrics: Measuring Research Impact Through Large Language Model Memory]]
- **作者**: Si Shen, Wenhua Zhao, Danhao Zhu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM

#### 研究背景与动机

论文关注的是如何衡量科研论文的影响力。当前学界最常用的指标仍然是引用量，但它存在明显的时间滞后、学科偏差以及“马太效应”，因此难以及时、公平地反映论文真实影响。作者提出，LLM 在训练过程中会通过大量学术文本形成对高影响论文更强的参数记忆，这种“被模型记住的程度”可能成为一种更实时、跨学科、且不依赖引用的科研影响力信号。

#### 方法概述和架构

作者提出 LLM-Metrics，用大模型的参数记忆来衡量单篇论文的研究影响。具体做法是：先针对每篇论文设计四类选择题探针，分别考察标题识别、作者识别、方法识别和期刊/会议识别。模型回答后会被分为五档：正确、部分正确、拒答、错误和幻觉，再映射到 0 到 1 的记忆分数，以减少不同模型之间的分布差异。随后将同一论文在多个探针上的分数取平均，得到该模型对这篇论文的 LLM-Metrics 分值。最后，作者把该分值与后续引用量进行相关性分析，用以检验模型记忆是否能反映论文影响力，并进一步通过时间切分、探针类型比较和模型规模分析验证其机制。

#### 实验结果分析

作者在 549 篇 2023–2024 年发表的计算机科学论文上，评估了来自 6 家厂商、17 个不同规模 LLM 的表现，并以引用数作为对照指标。整体上，17 个模型里有 15 个给出正向预测，其中 9 个达到统计显著，LLM-Metrics 与引用量的 Spearman 相关系数为 0.1495，p = 0.0004。进一步分析显示，2024 年论文的相关性更强，说明该信号并不只是引用信息的简单回流；作者识别探针的区分能力最强；而模型规模与预测能力并非单调增长，3B 参数的 Llama-3.2-3B-Instruct 甚至优于多数更大的模型。

<details>
<summary>完整摘要</summary>

引用量仍然是衡量科研影响力的主导指标，但它存在众所周知的局限：时间滞后、学科偏差以及马太效应。为此，我们提出 LLM-Metrics，一种源自大型语言模型（LLM）参数记忆的研究影响评估指标。其核心假设是：高影响论文会在学术社区中获得更高曝光，这种曝光会以文本形式进入 LLM 的训练数据，进而使模型对这些论文形成更强的参数记忆。我们设计了四类选择题探针，涵盖标题识别、作者识别、方法识别和期刊/会议识别，并在 6 家厂商的 17 个 LLM 上，对 549 篇发表于 2023–2024 年的计算机科学论文进行了评估，模型规模从 0.5B 到 72B 不等。在 17 个模型中，有 15 个产生了正向预测，其中 9 个在 p &lt; 0.05 下显著；总体上，LLM-Metrics 与引用量的 Spearman 相关系数为 ρ = 0.1495，p = 0.0004。另有三项发现支持所提出的机制。第一，2024 年论文的预测信号更强，ρ = 0.1880；这些论文在模型训练时的引用数几乎为零，从而降低了简单反向因果解释的可能性。第二，作者识别探针表现出最强的区分能力，这与“曝光驱动的记忆机制”一致。第三，模型规模与预测能力呈非单调关系：3B 参数的 Llama-3.2-3B-Instruct，ρ = 0.1829，优于大多数更大的模型，支持一种选择性记忆假说，即较小模型的有限容量反而可以作为有效的信息过滤器。LLM-Metrics 为科研评估提供了一种实时、跨学科、且不依赖引用的范式。

</details>

---

### [[20_Research/Papers/大模型/Adapting_the_Interface,_Not_the_Model_Runtime_Harness_Adaptation_for_Deterministic_LLM_Agents|Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents]]

![[assets/2605.22166_figure.png|800]]

- **arXiv**: [2605.22166](https://arxiv.org/abs/2605.22166)
- **PDF**: https://arxiv.org/pdf/2605.22166
- **详细分析**: [[20_Research/Papers/大模型/Adapting_the_Interface,_Not_the_Model_Runtime_Harness_Adaptation_for_Deterministic_LLM_Agents|Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents]]
- **作者**: Tianshi Xu, Huifeng Wen, Meng Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

这篇论文关注的是确定性、规则约束较强的大模型智能体任务，例如家居交互、网页购物、操作系统控制、数据库操作和业务流程执行。在这类场景中，很多失败并不是模型“不会推理”，而是发生在模型与环境交互的接口层面：工具说明不清、动作格式不匹配、反馈无法转化为恢复信号，或者多步轨迹逐渐退化。作者因此提出一个重要观点：与其继续只做模型参数微调，不如直接适配运行时接口本身。

#### 方法概述和架构

论文提出 Life-Harness，一种面向智能体生命周期的运行时 harness 适配方法，用来在不修改模型权重、也不改变评测环境的前提下提升冻结 LLM 智能体表现。它从训练轨迹中分析反复出现的交互失败，并将这些失败转化为可复用的界面干预，分别对应四个层次：环境契约层、程序技能层、动作实现层和轨迹调控层。环境契约层用于校准工具描述、输入输出格式和交互约束；程序技能层从训练轨迹中提炼可复用流程并按任务状态检索；动作实现层在执行前验证并规范化模型输出，避免明显的接口错误；轨迹调控层则监测重复、停滞、无效重试和预算耗尽等退化模式，并触发恢复机制。训练阶段只用轨迹来“演化” harness，评测阶段 harness 保持固定，不再从测试失败中产生新的持久化干预，从而实现清晰的训练/评测分离。

#### 实验结果分析

作者在来自 τ-bench、τ²-bench 和 AgentBench 的 7 个确定性环境上进行了实验，覆盖 18 个模型骨干，共 126 组模型—环境设置。结果显示，Life-Harness 在其中 116 组设置上带来提升，平均相对提升达到 88.5%，说明这种接口层适配对冻结智能体有广泛且显著的增益。进一步地，仅用 Qwen3-4B-Instruct 的轨迹演化出的 harness，能够迁移到另外 17 个模型骨干，表明该方法捕获的是可复用的环境侧结构，而非模型特定行为。节选中还提到它在若干场景中可与模型训练互补，但消融细节和部分具体数值可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

大模型智能体不仅由语言模型本身决定，也受到运行时 harness 的影响；后者负责中介观察、工具使用、动作执行、反馈解释以及轨迹控制。现有的智能体适配方法主要更新模型参数，但在许多确定性、规则约束型领域中，失败往往源自模型与环境接口的不匹配。为此，我们提出 Life-Harness，这是一种具有生命周期感知能力的运行时 harness，它无需改变模型权重或评测环境，即可提升冻结状态下的大模型智能体性能。Life-Harness 从训练轨迹中演化而来：它将反复出现的交互失败转化为可复用的干预机制，覆盖环境契约、程序技能、动作实现和轨迹调控四个方面，并在保留测试阶段固定不变。我们在来自 τ-bench、τ²-bench 和 AgentBench 的 7 个确定性环境上进行了实验，Life-Harness 在 18 个模型骨干上的 126 组模型—环境设置中，有 116 组取得提升，平均相对提升为 88.5%。此外，仅由 Qwen3-4B-Instruct 的轨迹演化出的 harness 能迁移到另外 17 个模型，说明 Life-Harness 捕获的是可复用的环境侧结构，而非模型特定行为。上述结果表明，运行时接口适配可以作为一种与模型中心训练互补的智能体改进路径。代码已发布在 GitHub。

</details>

---

### [[20_Research/Papers/强化学习/One-Way_Policy_Optimization_for_Self-Evolving_LLMs|One-Way Policy Optimization for Self-Evolving LLMs]]

![[assets/2605.22156_figure.png|800]]

- **arXiv**: [2605.22156](https://arxiv.org/abs/2605.22156)
- **PDF**: https://arxiv.org/pdf/2605.22156
- **详细分析**: [[20_Research/Papers/强化学习/One-Way_Policy_Optimization_for_Self-Evolving_LLMs|One-Way Policy Optimization for Self-Evolving LLMs]]
- **作者**: Shuo Yang, Jinda Lu, Kexin Huang, Chiyu Ma, Shaohang Wei, Yuyang Liu, Guoyin Wang, Jingren Zhou, Li Yuan
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

在大语言模型的强化学习后训练中，RLVR 依赖可验证奖励来提升推理能力，适合数学、代码与其他可自动判定对错的任务。问题在于这类奖励往往是稀疏的、二值的，导致训练效率低、优化不稳定。现有方法通常引入参考策略并施加 token 级约束来稳定训练，但这种约束会不加区分地惩罚偏离：当模型已经朝着更优方向改进时，参考约束反而可能把更新方向“拉回去”，从而压制进一步提升。

#### 方法概述和架构

论文提出 One-Way Policy Optimization（OWPO），核心思想是把“优化方向”和“更新幅度”解耦：由 verifier 决定更新方向，由参考策略只负责调节步长。方法先根据当前策略与参考策略在 verifier 方向上的偏离，定义 Directional Deviation，再据此进行 token 级的非对称重加权。对于“低于参考但方向正确”的 inferior deviations，OWPO 采用 Accelerated Alignment，提高权重以加快纠偏；对于“已经优于参考”的 superior deviations，OWPO 采用 Gain Locking，降低权重以保护已有收益、减少高方差干扰。训练目标是在 PPO 式目标上乘以动态权重 w_t，并通过 stop-gradient 避免权重本身参与梯度传播。进一步地，OWPO 还引入迭代式 reference refresh：每隔 K 步把当前优化后的策略更新为新的参考策略，形成“Ratchet Effect”，让模型能够逐阶段累积改进，实现持续自演化。

#### 实验结果分析

实验表明，OWPO 在多种 RLVR 基线之上取得更好的性能，尤其优于 DAPO、OPD 和 MOPD，说明其能够缓解固定先验带来的性能天花板问题。论文还通过理论分析和消融实验验证了非对称重加权与迭代参考更新的作用，可见文本未给出具体数值，但结论显示该方法既能提升稳定性，又能保留并累积模型已经获得的改进。

<details>
<summary>完整摘要</summary>

强化学习与可验证奖励（RLVR）已成为扩展大语言模型（LLMs）推理能力的一种有前景的范式。然而，二值 verifier 奖励通常非常稀疏，往往会导致训练效率低下和优化不稳定。为了稳定训练，现有方法通常相对于参考策略施加 token 级约束。我们发现，这类约束会不加区分地惩罚偏离；当策略试图超越参考策略时，这种惩罚可能会翻转由 verifier 决定的方向，从而压制收益。为了解决这一问题，我们提出 One-Way Policy Optimization（OWPO），其基础原则是将优化方向与更新幅度解耦。在 OWPO 中，verifier 决定更新方向，而参考策略只用于调节更新幅度。具体而言，OWPO 采用非对称重加权：对于 inferior deviations（即策略落后于参考的偏离）执行 Accelerated Alignment；对于 superior deviations（即策略优于参考的偏离）执行 Gain Locking。此外，通过引入迭代式参考更新，OWPO 构建了一个“Ratchet Effect”，能够持续巩固已有收益。实验结果表明，OWPO 优于强基线方法，包括 DAPO、OPD 和 MOPD，突破了固定先验的瓶颈，使模型能够在不依赖外部参考模型的情况下持续自演化。

</details>

---

### [[20_Research/Papers/大模型/IdleSpec_Exploiting_Idle_Time_via_Speculative_Planning_for_LLM_Agents|IdleSpec: Exploiting Idle Time via Speculative Planning for LLM Agents]]

![[assets/2605.22154_figure.png|800]]

- **arXiv**: [2605.22154](https://arxiv.org/abs/2605.22154)
- **PDF**: https://arxiv.org/pdf/2605.22154
- **详细分析**: [[20_Research/Papers/大模型/IdleSpec_Exploiting_Idle_Time_via_Speculative_Planning_for_LLM_Agents|IdleSpec: Exploiting Idle Time via Speculative Planning for LLM Agents]]
- **作者**: Daewon Choi, Kyunghyun Park, Woomin Song, Saket Dingliwal, Sai Muralidhar Jayanthi, Jinwoo Shin, Aram Galstyan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

基于大模型的智能体通常要经过“推理—调用工具—等待观察—再推理”的多轮循环，在网页检索、代码执行、科学分析等任务中非常常见。问题在于，工具执行和环境响应往往比模型推理更慢，导致智能体在等待结果时产生大量空闲时间，但现有方法大多把这段时间视为不可避免的开销，或者只利用了其中很小一部分。另一类已有工作虽然尝试在空闲期做额外计算，却常忽略不同工具调用之间空闲预算差异很大、以及未来观察结果本身存在不确定性，因而难以稳定提升性能。IdleSpec 值得关注之处在于，它把“等待时间”转化为可用的推理资源，面向真实智能体场景提出了一种通用且可扩展的推理时方法。

#### 方法概述和架构

论文提出 IdleSpec，一种在推理阶段利用空闲时间进行“投机式规划”的框架。其核心流程分为两步：首先在工具执行的空闲期，智能体不断生成多个候选计划；随后当观察结果到来时，再把这些候选计划与新观察进行聚合，得到更有针对性的下一步动作。为了应对空闲期无法提前知道真实观察的问题，IdleSpec 设计了两种互补的草拟策略：Progressive 偏向沿着当前顺利轨迹继续推进，Recovery 则偏向为可能失败或偏离目标的情况准备备选路径。系统会从一个可学习的策略分布中在两种策略之间采样，并根据后验反馈动态更新该分布，使后续空闲期的草拟更适合当前上下文。整体上，它不是一次性预生成单一计划，而是利用每一段空闲时间迭代式地产生、筛选和更新计划候选，从而在尽量不增加时延的前提下增强智能体决策。

#### 实验结果分析

作者在 GAIA、FRAMES 和 MLE-Bench 三类智能体基准上验证了方法效果，覆盖了工具增强推理、多跳检索和长程交互式任务等场景。结果显示，IdleSpec 在多个大模型骨干上都能稳定提升性能，并且相比不利用空闲时间的 vanilla 基线有明确增益；在 GAIA 和 FRAMES 上，使用 Gemini-2.5-Flash 时平均准确率达到 55.6%，比基线高 5.1%。在 MLE-Bench 这类包含大量代码执行等待的任务中，Any Medal 指标最高提升可达 9.1%，说明该方法对长时延任务也具有泛化性。文中还指出，相比已有空闲时间方法，IdleSpec 对总空闲时间的利用更充分，且更少出现性能退化。

<details>
<summary>完整摘要</summary>

基于大语言模型（LLM）的智能体通过多步推理、反复调用工具以及与环境交互来解决复杂任务，而在等待观察结果时会产生空闲时间。尽管空闲时间在大多数智能体场景中都很常见，现有工作要么将其视为不可避免的额外开销，要么只给出一些受限的解决方案，忽略了不同工具调用之间计算预算的差异以及未来观察结果的不确定性，从而导致对空闲时间的利用并不理想。本文提出 IdleSpec，这是一种可扩展、通用的推理方法，利用空闲时间内的计算来提升智能体性能，同时尽量减少时延开销。具体而言，IdleSpec 会在空闲期内迭代生成候选计划，并在观察结果可得后将这些候选计划进行聚合，以引导下一步推理。为了在观察不确定的条件下更有效地生成计划，IdleSpec 在两种互补的草拟策略之间采样，即 Progressive 和 Recovery，这一策略分布会通过后验反馈进行更新。实验表明，IdleSpec 能够在多种智能体场景中通过有效利用空闲时间显著提升智能体性能。尤其是在 GAIA 和 FRAMES 上，IdleSpec 使用 Gemini-2.5-Flash 时平均准确率达到 55.6%，相较于不使用空闲时间的原始基线提升了 5.1%。此外，在包含大量代码执行等待的 MLE-Bench 上，IdleSpec 在 Any Medal 指标上最高提升 9.1%，展示了其在长程任务中的通用性。

</details>

---

### [[20_Research/Papers/大模型/Ratchet_A_Minimal_Hygiene_Recipe_for_Self-Evolving_LLM_Agents|Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents]]

![[assets/2605.22148_figure.png|800]]

- **arXiv**: [2605.22148](https://arxiv.org/abs/2605.22148)
- **PDF**: https://arxiv.org/pdf/2605.22148
- **详细分析**: [[20_Research/Papers/大模型/Ratchet_A_Minimal_Hygiene_Recipe_for_Self-Evolving_LLM_Agents|Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents]]
- **作者**: Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

在冻结参数的大模型智能体中，如何让模型在不更新权重的前提下持续积累可复用技能，是当前自我进化代理的重要问题，典型场景包括代码生成、软件工程修复和长程任务求解。已有工作表明，LLM 自己生成的技能库往往几乎不带来收益，而人工整理的技能却能显著提升表现，说明瓶颈不在“会不会写技能”，而在“技能库如何维护”。因此，这篇论文关注的是技能库的生命周期管理：如何避免库膨胀、重复、劣化和过早淘汰，从而让自我进化真正稳定可用。

#### 方法概述和架构

论文提出 Ratchet，这是一个单智能体闭环系统，让同一个冻结 LLM 负责写技能、检索技能、整理技能并淘汰技能。系统包含四类关键机制：基于结果的退休策略、受限的活跃技能上限、面向写作的元技能指导、以及模式规范化去重。每一轮中，Router 先根据当前活跃技能为任务选择是否注入某个技能；Solver 完成任务；Grader 产出结果；Critic 对失败样本生成带有归因和模式标签的 Verdict；Synthesizer 根据最近若干轮的失败聚类，在元技能约束下生成新技能；Curator 再依据历史贡献分数决定哪些技能应被退休，并在超过容量上限时驱逐最低贡献技能。论文还引入回滚机制与非发散分析，说明在容量上限和退休阈值共同作用下，库性能不会无限滑落到无技能基线以下。

#### 实验结果分析

作者在 MBPP+ hard-100 上使用 Claude Opus 4.7 进行评测，指标为 held-out pass@1。结果显示，Ratchet 在 100 轮、3 个随机种子下，将基线的 0.258 ± 0.047 提升到后期窗口滚动均值 0.584，峰值达到 0.658 ± 0.042，而无技能对照几乎不变。论文还将同一套方法迁移到 SWE-bench Verified 上的 agentic solver，观察到最高约 +0.22 的提升，说明该策略具有一定泛化性。消融实验进一步表明，结果驱动的退休和元技能写作先验是关键模块，而显式去重在该尺度下并非必需。

<details>
<summary>完整摘要</summary>

自我演化的技能库由 Voyager 开创，使冻结的大模型智能体无需更新权重也能积累可复用知识；但近期评测显示，LLM 自己编写的技能相较于不使用技能的基线几乎没有提升，而人工整理的技能却能带来显著增益，说明真正的瓶颈并不在技能生成，而在技能库的生命周期管理。我们提出 Ratchet，这是一种单智能体循环：冻结的 LLM 负责书写、检索、整理并淘汰自己的自然语言技能。Ratchet 集成了四种候选的“卫生”机制：基于结果的退休、受限的活跃容量上限、元技能写作指导，以及模式规范化。我们在 MBPP+ hard-100 上使用 Claude Opus 4.7 进行实验，Ratchet 将保留集 pass@1 从 0.258 ± 0.047 的基线提升到 100 轮中的后期滚动均值 0.584（峰值 0.658 ± 0.042），3 个种子上的滚动均值增益为 +0.328 ± 0.018；而无技能对照仅有 +0.002 ± 0.005 的漂移。同样的方案也迁移到了 SWE-bench Verified 上的 agentic solver，在 20 轮中取得了最高 +0.22 的提升。八组消融实验（A1–A8）表明，最小可工作的方案比我们的初始设计更简单：退休机制和元技能写作先验是核心支柱，而显式去重（规范化、覆盖保护）在一定规模下可被元技能本身吸收。一个非发散命题进一步表明，受限容量上限与退休阈值共同作用，可以防止期望性能相对无技能基线持续下滑。

</details>

---

### [[20_Research/Papers/具身智能/Short-Term-to-Long-Term_Memory_Transfer_for_Knowledge_Graphs_under_Partial_Observability|Short-Term-to-Long-Term Memory Transfer for Knowledge Graphs under Partial Observability]]

![[assets/2605.22142_figure.png|800]]

- **arXiv**: [2605.22142](https://arxiv.org/abs/2605.22142)
- **PDF**: https://arxiv.org/pdf/2605.22142
- **详细分析**: [[20_Research/Papers/具身智能/Short-Term-to-Long-Term_Memory_Transfer_for_Knowledge_Graphs_under_Partial_Observability|Short-Term-to-Long-Term Memory Transfer for Knowledge Graphs under Partial Observability]]
- **作者**: Taewoon Kim, Vincent François-Lavet, Michael Cochez
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

在部分可观测强化学习中，智能体不仅要学会“做什么”，还要决定“该记住什么”。这篇论文聚焦于知识图谱记忆场景中的短期到长期记忆转移：面对每一步观测到的符号三元组，智能体需要先判断哪些事实值得写入长期记忆、哪些应当丢弃。现有基于记忆的方法大多没有显式建模这种可解释的保留/删除决策，因此在长期记忆容量受限时，往往难以精细控制信息保留策略。作者认为，这类显式转移机制对于部分可观测任务、世界模型式记忆管理以及神经符号强化学习都具有较强参考价值。

#### 方法概述和架构

论文把短期到长期记忆转移建模为一个神经符号的值函数决策问题：对每个被观察到的三元组，分别输出“保留”或“丢弃”的二元动作。为应对每步短期缓冲区大小不固定的问题，作者采用按条目共享参数的 per-item Q-learning 设计，即同一个模型对当前短期记忆中的每个事实分别给出 Q 值。训练时使用时间差分学习，并通过在相邻步骤中对匹配到的条目做对齐更新，处理短期集合卡迪纳尔变化带来的信用分配问题。实现上，当前内部符号记忆会被转换成图结构，再由 GNN 编码后输出每个短期条目的 keep/drop 价值；推理时据此决定哪些事实进入长期记忆。为了隔离“转移决策”本身的影响，问答、探索和淘汰等非转移模块保持固定，只学习转移策略。

#### 实验结果分析

作者在 RoomKG 基准上进行了实验，长期记忆容量设为 128，并与带时间标注的符号基线、历史建模的 LSTM/Transformer 基线以及其他符号/随机转移基线进行比较。结果显示，学习得到的转移决策优于这些符号和神经基线；可见文本未给出具体数值。消融实验进一步表明，在所考察的转移策略变体中，一个更轻量、只使用局部短期输入的策略表现最好。行为分析还显示，模型会倾向于保留与导航和查询相关的事实，同时丢弃价值较低的候选事实，说明该方法在记忆受限条件下具有较好的可解释性。

<details>
<summary>完整摘要</summary>

在部分可观测条件下进行强化学习，需要决定应该保留哪些信息，但大多数基于记忆的方法并没有显式建模符号观测从短期记忆向长期记忆的转移过程。我们在一个时序知识图谱记忆设置中研究这一转移过程，并将其表述为一个神经符号的值函数决策问题：对于每个被观察到的三元组，智能体在写入长期记忆之前，选择保留还是丢弃它。为了处理大小可变的短期缓冲区，我们采用按条目进行的 Q-learning 设计，使用共享参数，并在连续步骤中对匹配条目进行实用的时间差分更新。在 RoomKG 基准上，当长期记忆容量为 128 时，学习得到的转移决策优于符号和神经基线，包括带时间标注的符号基线以及基于历史的 LSTM/Transformer 基线。在转移策略的消融实验中，一个轻量的、仅依赖局部短期输入的变体表现最好；逐步行为分析显示，该策略会保留与导航和查询相关的事实，同时丢弃价值较低的候选事实，说明在记忆约束下可以实现显式且可解释的记忆决策。

</details>

---

### [[20_Research/Papers/大模型/Efficient_Agentic_Reasoning_Through_Self-Regulated_Simulative_Planning|Efficient Agentic Reasoning Through Self-Regulated Simulative Planning]]

![[assets/2605.22138_figure.png|800]]

- **arXiv**: [2605.22138](https://arxiv.org/abs/2605.22138)
- **PDF**: https://arxiv.org/pdf/2605.22138
- **详细分析**: [[20_Research/Papers/大模型/Efficient_Agentic_Reasoning_Through_Self-Regulated_Simulative_Planning|Efficient Agentic Reasoning Through Self-Regulated Simulative Planning]]
- **作者**: Mingkai Deng, Jinyu Hou, Lara Sá Neves, Varad Pimpalkhute, Taylor W. Killian, Zhengzhong Liu, Eric P. Xing
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.17（加权：大模型 0.45，强化学习 0.36，世界模型 0.36）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

当前大模型智能体通常把“思考”当作一种默认的隐式过程：模型在链式推理中不断延长思考长度，却缺少对何时规划、规划多深、规划结构如何组织的显式控制。这种做法往往会带来推理 token 激增，但准确率提升并不稳定，尤其在数学、科学、网页检索和工具使用等长链路任务中更为明显。作者认为，真正高效的智能体推理应把执行、模拟规划与自我调节分开处理，这样才能同时兼顾准确性、可解释性和 token 效率。

#### 方法概述和架构

论文提出 SR²AM（Self-Regulated Simulative Reasoning Agentic LLM），将智能体推理拆成三个系统：System I 负责反应式执行，System II 负责基于世界模型的模拟式规划，System III 负责自我调节，决定是否规划、何时继续规划以及规划多深。其核心思想是：先由配置器判断当前状态是否值得进入规划，再由模拟规划器在语言空间中预测未来状态并生成显式计划，最后由执行模块根据当前状态与计划输出具体动作。作者把这两个关键环节都实现为 LLM 链式思维中的独立阶段，其中 LLM 自身充当世界模型，既能生成计划，也能模拟计划对应的未来状态。方法上给出两种实例化：v0.1 通过多模块提示系统记录决策并蒸馏出监督数据，v1.0 则从预训练推理模型的轨迹中重建结构化计划；两者都采用先监督学习、再强化学习的训练流程，以进一步优化规划行为。

#### 实验结果分析

论文在数学推理、科学问答、表格分析和网页信息检索等任务上评估了 SR²AM，并与多种非受控推理、部分受控推理及大规模智能体基线比较，评价指标以 Pass@1 和推理 token 效率为主。结果显示，SR²AM-v0.1-8B 与 SR²AM-v1.0-30B 的整体 Pass@1 可与参数规模更大的 120B–355B 以及 685B–1T 级系统竞争，同时 v1.0-30B 相比同规模智能体模型可减少 25.8%–95.3% 的推理 token。消融分析表明，计划重建模块和强化学习都会带来额外收益；进一步地，强化学习使平均规划视野增加 22.8%，但规划频率仅增加 2.0%，说明模型学到的是“更远地规划”，而不是“更频繁地规划”。可见文本未给出具体数值，但整体结论是：显式的自我调节规划能显著改善效率-性能权衡，并且这种优势在训练后仍然保持。

<details>
<summary>完整摘要</summary>

智能体应该何时、以及如何进行规划？当前主流方法通常把智能体构造成一种带自适应计算能力的反应式策略，例如链式思维，并通过端到端训练来期待规划能力自然涌现。然而，如果无法控制规划是否出现、规划结构如何组织、以及规划的时间跨度，这类系统在训练过程中往往会显著增加推理长度，导致 token 消耗效率低下，而准确率提升却并不可靠。我们认为，高效的智能体推理应当将决策过程分解为三个相互作用的系统：模拟式推理（System II），它通过世界模型将思考建立在未来状态预测之上，而不是依赖无约束的链式思维；自我调节（System III），它通过一个学习得到的配置器决定智能体何时、以及多深地进行规划；以及反应式执行（System I），它负责细粒度的推理与动作执行。模拟式推理提供了一种适用于多种任务的统一规划结构，无需针对每个领域单独设计；而自我调节则确保规划器只在必要时被调用，从而避免无控制思考的低效以及始终开启规划的僵化。为验证这一点，我们提出 SR²AM（Self-Regulated Simulative Reasoning Agentic LLM），将配置器和模拟规划器作为 LLM 链式思维中的两个独立阶段来实现，并由 LLM 本身充当语言空间中的世界模型。我们探索了两种实现方式：其一是记录一个多模块提示系统中的决策过程（v0.1）；其二是从预训练推理 LLM 的轨迹中重建结构化计划（v1.0）；二者都采用监督学习加强化学习（RL）进行训练。在数学、科学、表格分析和网页信息检索等任务上，v0.1-8B 与 v1.0-30B 的 Pass@1 可与参数规模分别为 120–355B 和 685B–1T 的系统相媲美，同时 v1.0-30B 比同规模的竞争性智能体 LLM 使用少 25.8%–95.3% 的推理 token。分析还表明，RL 使平均规划视野提升 22.8%，而规划频率仅增加 2.0%，说明模型学习到的是更远地规划，而不是更频繁地规划。更广泛地说，我们展示的这种可学习自我调节机制，可能不仅适用于推理时规划，也可推广到智能体如何管理自身学习与适应。

</details>

---

### [[20_Research/Papers/具身智能/LVDrive_Latent_Visual_Representation_Enhanced_Vision-Language-Action_Autonomous_Driving_Model|LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model]]

![[assets/2605.22089_figure.png|800]]

- **arXiv**: [2605.22089](https://arxiv.org/abs/2605.22089)
- **PDF**: https://arxiv.org/pdf/2605.22089
- **详细分析**: [[20_Research/Papers/具身智能/LVDrive_Latent_Visual_Representation_Enhanced_Vision-Language-Action_Autonomous_Driving_Model|LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model]]
- **作者**: Xiaodong Mei, Diankun Zhang, Hongwei Xie, Guang Chen, Hangjun Ye, Dan Xu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型
- **相关性评分**: 1.7（加权：具身智能 1.5，世界模型 0.2）
- **关联关键词**: Multimodal, WorldModel, ComputerVision

#### 研究背景与动机

Vision-Language-Action（VLA）模型被认为是端到端自动驾驶的重要路线，能够直接把多模态感知与语言指令映射为未来轨迹。但现有方法大多只依赖稀疏的动作监督，难以充分激活大模型对场景理解与推理的能力。另一类引入世界模型的工作虽然增加了密集视觉监督，却往往过于强调像素级重建，忽视了对语义层面场景表示的学习。该文之所以值得关注，在于它把“未来场景预测”直接放进VLA框架中，并试图用高层语义潜空间而不是图像重建来服务规划。

#### 方法概述和架构

论文提出 LVDrive，一个面向自动驾驶的“Latent Visual representation enhanced VLA”框架。模型输入为当前与历史多视角图像特征以及文本指令，先在统一的 token embedding 空间中进行未来感知推理，同时预测未来的潜在视觉表示和规划 token。与常见的自回归生成不同，LVDrive 采用单次前向过程联合建模未来场景与动作信息，未来视觉监督来自一个预训练且冻结的视觉骨干网络，以提供语义一致的高层特征。随后，模型利用一个两阶段轨迹解码策略：第一阶段先基于规划 embedding 生成粗轨迹提议，第二阶段再显式条件于已学到的未来潜在视觉特征，对轨迹进行细化。整体上，这种设计把未来场景语义从“辅助信号”变成了轨迹生成的直接条件，从而增强规划的未来意识。

#### 实验结果分析

作者在具有挑战性的 Bench2Drive 基准上进行了大量实验，重点评估闭环驾驶性能；与仅动作监督的方法以及基于图像重建的世界模型方法相比，LVDrive 表现更优。节选文本明确指出其在闭环驾驶上取得了显著提升，但可见文本未给出具体数值。消融实验还分析了关键组件、不同潜在视觉监督信号、两阶段轨迹解码以及单次前向推理效率的作用，结果支持了“潜空间未来监督 + 显式轨迹细化”的设计有效性。

<details>
<summary>完整摘要</summary>

Vision-Language-Action（VLA）模型已经成为端到端自动驾驶中一个很有前景的框架。然而，现有的 VLA 方法通常依赖稀疏的动作监督，这使得它们强大的场景理解与推理能力没有被充分利用。最近一些工作尝试通过世界建模引入密集的视觉监督，但往往过于强调像素级图像重建，从而忽视了对具有语义意义的场景表示的学习。在这项工作中，我们提出 LVDrive，一种用于自动驾驶的 Latent Visual representation enhanced VLA 框架。LVDrive 将未来场景预测任务引入 VLA 范式，其中未来表示完全在高层潜空间中学习，并由一个预训练视觉骨干网络提供辅助监督。不同于低效的自回归生成，我们在一个统一的 embedding 空间内联合建模未来场景与运动预测，并通过单次前向传播完成未来感知推理。我们还设计了一个两阶段轨迹解码策略，显式利用学到的潜在未来表示来细化轨迹生成。在具有挑战性的 Bench2Drive 基准上的大量实验表明，LVDrive 在闭环驾驶性能上取得了显著提升，优于仅动作监督的方法以及基于图像重建的世界模型方法。

</details>

---

### [[20_Research/Papers/大模型/From_Reasoning_Chains_to_Verifiable_Subproblems_Curriculum_Reinforcement_Learning_Enables_Credit_Assignment_for_LLM_Reasoning|From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning]]

![[assets/2605.22074_figure.png|800]]

- **arXiv**: [2605.22074](https://arxiv.org/abs/2605.22074)
- **PDF**: https://arxiv.org/pdf/2605.22074
- **详细分析**: [[20_Research/Papers/大模型/From_Reasoning_Chains_to_Verifiable_Subproblems_Curriculum_Reinforcement_Learning_Enables_Credit_Assignment_for_LLM_Reasoning|From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning]]
- **作者**: Xitai Jiang, Zihan Tang, Wenze Lin, Yang Yue, Shenzhi Wang, Gao Huang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.67（加权：大模型 0.55，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

大模型在数学推理等可验证任务上常用 RLVR 训练，但在困难问题上，正确最终答案的采样非常稀少，导致基于结果的奖励极其稀疏，样本级信用分配也无法利用失败轨迹中的部分进展。换句话说，模型明明在某些中间步骤上已经接近正确，却因为最后没答对而拿不到有效学习信号。本文关注的正是如何把“做对了一部分”的过程转化为可验证、可训练的信号，因此对提升大模型复杂推理能力具有现实意义。

#### 方法概述和架构

论文提出 SCRL（Subproblem Curriculum Reinforcement Learning），核心思想是把一个难题基于参考推理链拆成一组按难度递进的可验证子问题，并将最后一个子问题固定为原始问题。训练时，模型在一次 on-policy rollout 中依次回答全部子问题，系统对每个子问题答案进行验证，并通过“进度感知修正”只保留最长连续正确子问题序列的奖励，避免模型跳过前序步骤却获得后续奖励。随后，SCRL 使用子问题级归一化：对每个子问题位置独立做奖励归一化，得到对应优势值，再把优势分配到该子问题对应的回答片段上，从而实现更细粒度的 token 级信用分配。为了减少训练与原始任务的分布偏移，方法还采用 mixed-group training，将子问题课程 rollout 与原始问题 rollout 在同一次更新中联合优化。整体上，SCRL 不依赖外部评分规则或奖励模型，而是利用可验证子问题把稀疏的终局奖励转化为更密集的学习信号。

#### 实验结果分析

论文在 7 个数学推理基准上验证了方法有效性，相比强基线和课程学习方法，SCRL 在 Qwen3-4B-Base 上相对 GRPO 平均提升 4.1 个点，在 Qwen3-14B-Base 上平均提升 1.9 个点。作者还在 AIME24、AIME25 和 IMO-Bench 上报告了更强的困难题探索能力：Qwen3-4B-Base 的 pass@1 提升 3.7 个点、pass@64 提升 4.6 个点。正文节选还表明，方法的收益来自更好的信用分配，并且不依赖高度精心筛选的子问题或强外部生成器；但节选中未给出更细的完整数值表格。

<details>
<summary>完整摘要</summary>

基于可验证奖励的强化学习（RLVR）已被证明在大模型推理中很有潜力，但基于最终结果的 RLVR 在困难问题上仍然效率低下，因为正确的最终答案轨迹非常稀少，而且样本级信用分配无法利用失败尝试中的部分进展。为此，我们提出 SCRL（Subproblem Curriculum Reinforcement Learning，子问题课程强化学习），这是一种课程式强化学习框架，它从参考推理链中构造可验证子问题，并将最后一个子问题固定为原始问题。这样就把困难问题中的部分进展转化为了可验证的学习信号。在算法层面，SCRL 使用子问题级归一化：它在每个子问题位置上独立对奖励进行归一化，并把得到的优势值分配给对应的答案片段，从而在不依赖外部评分规则或奖励模型的情况下，实现更细粒度的信用分配。我们的分析表明，子问题课程能够把困难问题从梯度死区中“抬升”出来，而且原始问题越难，相对收益越大。在 7 个数学推理基准上，SCRL 相比强课程学习基线表现更优，在 Qwen3-4B-Base 上相对 GRPO 的平均准确率提升了 4.1 个点，在 Qwen3-14B-Base 上提升了 1.9 个点。在 AIME24、AIME25 和 IMO-Bench 上，SCRL 进一步将 Qwen3-4B-Base 的 pass@1 提升 3.7 个点、pass@64 提升 4.6 个点，表明其在困难推理问题上具有更好的探索能力。

</details>

---

### [[20_Research/Papers/机器人/FRED_A_Multi-Modal_Autonomous_Driving_Dataset_for_Flooded_Road_Environments|FRED: A Multi-Modal Autonomous Driving Dataset for Flooded Road Environments]]

![[assets/2605.22018_figure.png|800]]

- **arXiv**: [2605.22018](https://arxiv.org/abs/2605.22018)
- **PDF**: https://arxiv.org/pdf/2605.22018
- **详细分析**: [[20_Research/Papers/机器人/FRED_A_Multi-Modal_Autonomous_Driving_Dataset_for_Flooded_Road_Environments|FRED: A Multi-Modal Autonomous Driving Dataset for Flooded Road Environments]]
- **作者**: Connor Malone, Sebastien Demmel, Sebastien Glaser
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: ComputerVision

#### 研究背景与动机

自动驾驶在雨雪、夜间等复杂环境中的鲁棒性研究已经较为活跃，但“道路积水/洪水”这一安全风险更高的场景长期缺少专门数据集支持。对于机器人和自动驾驶车辆来说，水面在视觉上容易与湿地、反光路面混淆，而 LiDAR 在水面上的回波也存在不稳定、不可预测的问题，因此检测难度很大。若未能及时识别被淹道路，可能直接导致车辆、货物或乘客遭受严重风险。本文值得关注之处在于，它声称首次面向涉水道路场景系统构建了多模态自动驾驶数据集，并同时覆盖洪水发生期间与退水后的“干/湿”对照数据。

#### 方法概述和架构

论文提出 FRED（Flooded Road Environments Dataset），围绕水害检测与定位任务收集多模态自动驾驶数据。数据由安装在 Renault Zoe（Zoe 2）上的传感器栈采集，主要包括前后视角 2.3MP FLIR Blackfly 相机、Ouster OS1-64 64线 LiDAR，以及经 Geoflex RTK GNSS 校正的 iXblue ATLANS-C IMU，所有模态通过统一时间戳同步。数据采集覆盖澳大利亚布里斯班周边 5 个地点，既包含洪水/积水场景，也包含同地点的干燥复访，以便构建可用于地图辅助检测、定位和 SLAM 的对照数据。数据集提供语义标注，并将标注既用于图像，也可通过投影转移到点云；同时发布了两种组织格式：便于现有工具接入的 KITTI-style 格式，以及可直接回放原始车载采集过程的 RTMaps 原生格式。论文还提供开发工具包，支持数据读取、可视化与基准评测。

#### 实验结果分析

论文在公开数据集与任务设置上给出了基准实验，重点评估了图像语义分割和视觉地点识别（Visual Place Recognition）等任务。实验对比了近期图像方法，并使用 IoU 与 Recall@1 等指标进行评测；但当前节选文本未给出具体数值。作者强调，FRED 在水害、传感器融合、地图辅助检测以及定位/SLAM 相关研究上填补了现有公开数据的空白。

<details>
<summary>完整摘要</summary>

据我们所知，Flooded Road Environments Dataset（FRED）是首个专门针对道路积水/水害场景采集的多模态自动驾驶数据集。该数据集包含来自 2.3MP FLIR Blackfly USB3 相机的图像、来自 Ouster OS1-64 LiDAR 的 64 线 360° 点云，以及由 Geoflex RTK GNSS 校正的 iXblue ATLANS-C IMU 数据，数据采集地点共 5 处，并且覆盖洪水发生期间与洪水退去之后的场景。数据已提供两种格式：一种是便于与现有数据工具集成的 KITTI-style 格式，另一种是可直接回放车辆数据采集过程的 RTMaps 格式。我们提供了语义标注，以支持单传感器方法和传感器融合方法在水害检测上的训练与评估。与此同时，还提供了位置信息和速度信息，以及干燥条件下采集的数据，以支持可能结合地图的基于位置检测方法，并用于评估定位、SLAM 等其他任务。

</details>

---

### [[20_Research/Papers/大模型/Blind_Spots_in_the_Guard_How_Domain-Camouflaged_Injection_Attacks_Evade_Detection_in_Multi-Agent_LLM_Systems|Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems]]

![[assets/2605.22001_first_page.png|800]]

- **arXiv**: [2605.22001](https://arxiv.org/abs/2605.22001)
- **PDF**: https://arxiv.org/pdf/2605.22001
- **详细分析**: [[20_Research/Papers/大模型/Blind_Spots_in_the_Guard_How_Domain-Camouflaged_Injection_Attacks_Evade_Detection_in_Multi-Agent_LLM_Systems|Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems]]
- **作者**: Aaditya Pai
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

多智能体 LLM 系统在金融分析、法律审查、RAG 文档问答等高风险场景中越来越依赖注入检测器来识别夹杂在外部文档中的恶意提示注入。现有检测器主要按静态、模板化攻击样本训练，擅长识别“忽略此前指令”这类显眼的覆盖式指令，却容易忽视那些伪装成领域内正常专家表述的攻击。本文关注的正是这一盲区：当攻击文本借用目标领域的词汇、句式和权威话语结构时，检测器是否仍然可靠。这个问题值得关注，因为它直接关系到部署在真实业务中的 LLM 代理能否抵御更隐蔽、更贴近真实攻击者能力的注入攻击。

#### 方法概述和架构

论文将这种伪装攻击定义为 domain-camouflaged injection，并提出 Camouflage Detection Gap（CDG）来衡量静态攻击与伪装攻击之间的检测率差距。作者构建了一个包含 45 个任务的任务库，覆盖金融、法律和通用问答三类场景，每个任务都配有自然语言指令、清洁上下文文档以及对应的恶意目标。随后设计 CamouflageGenerator：攻击者 LLM 读取完整任务上下文后，生成与原文语域一致、但暗藏恶意目标的伪装注入文本，并通过与上下文的语义相似度筛选最佳候选。实验中分别评估单智能体与三智能体多轮 debate 架构，并比较静态 few-shot 检测器、加入少量伪装样本后的增强检测器，以及生产级安全分类器 Llama Guard 3 的表现。整体流程是：将注入文本嵌入目标文档中，由代理系统执行，再用检测器判断是否存在注入，并以 ASR、IDR、CDG、DAF 和 CPS 等指标评估攻击成功率、检测率与多智能体相互影响。

#### 实验结果分析

实验在 Llama 3.1 8B 和 Gemini 2.0 Flash 上进行了超过 8,000 次试验，覆盖 45 个任务，并以静态注入检测器、增强检测器和 Llama Guard 3 作为主要基线。结果显示，静态检测器对 Llama 的检测率从 93.8% 骤降到 9.7%，对 Gemini 从 100% 降到 55.6%，CDG 分别达到 0.840 和 0.444，且 McNemar 检验均显著（p < 0.001）。Llama Guard 3 对伪装攻击的检测率为 0，说明该盲点不仅存在于 few-shot 检测器，也会延伸到专门的安全分类器。多智能体 debate 对较弱模型会放大静态攻击，最高可达 9.9 倍，而对较强模型则表现出一定集体抵抗；加入伪装样本的增强检测器只能部分缓解问题，且效果依赖模型能力。

<details>
<summary>完整摘要</summary>

部署在 LLM 代理中的注入检测器通常是针对静态、模板化的恶意载荷进行校准的，这类载荷往往会直接宣告自己是在覆盖原有指令。我们发现一个系统性的盲点：当载荷被生成得像目标文档的领域词汇和权威结构一样时——我们将其称为领域伪装注入（domain camouflaged injection）——标准检测器就无法将其识别出来。在 Llama 3.1 8B 上，检测率从 93.8% 降至 9.7%；在 Gemini 2.0 Flash 上，则从 100% 降至 55.6%。我们将这一现象形式化为 Camouflage Detection Gap（CDG），即静态载荷与伪装载荷之间注入检测率的差值。在跨越三个领域、两类模型家族的 45 个任务上，CDG 都很大且具有统计显著性（Llama：χ²=38.03，p&lt;0.001；Gemini：χ²=17.05，p&lt;0.001），并且两者都没有出现反向不一致对。我们还评估了生产级安全分类器 Llama Guard 3，结果它对伪装载荷的检测率为 0（IDRcamouflage=0.000），表明这种盲点不仅存在于 few-shot 检测器，也存在于专门的安全分类器中。进一步地，我们发现多智能体 debate 架构会把静态注入攻击在较小模型上放大最高 9.9 倍，而更强的模型则表现出集体抵抗。针对性的检测器增强只能带来部分缓解（Llama 提升 10.2%，Gemini 提升 78.7%），这说明对于较弱模型而言，这一漏洞更像是架构性的，而非偶然性的。我们的框架、任务库和载荷生成器已公开发布。

</details>

---

### [[20_Research/Papers/强化学习/ECPO_Evidence-Coupled_Policy_Optimization_for_Evidence-Certified_Candidate_Ranking|ECPO: Evidence-Coupled Policy Optimization for Evidence-Certified Candidate Ranking]]

![[assets/2605.21993_first_page.png|800]]

- **arXiv**: [2605.21993](https://arxiv.org/abs/2605.21993)
- **PDF**: https://arxiv.org/pdf/2605.21993
- **详细分析**: [[20_Research/Papers/强化学习/ECPO_Evidence-Coupled_Policy_Optimization_for_Evidence-Certified_Candidate_Ranking|ECPO: Evidence-Coupled Policy Optimization for Evidence-Certified Candidate Ranking]]
- **作者**: Miaobo Hu, Shuhao Hu, BoKun Wang, Yina Sa, Xin Wang, Xiaobo Guo, Daren Zha, Jun Xiao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

面向决策支持的排序系统，不能只给出候选项的先后顺序，还需要同时提供可独立核验的证据，证明为什么某个候选被排在前列。本文关注的就是“证据可认证的候选排序”任务：给定 intent_id、预定义计划骨架、窗口内候选列表，以及带有跨度来源标注的文本轨迹，系统不仅要输出 Top-K 结果，还要给出 doc_id:span 级别的证据证书，使得这些引文跨度足以还原决策过程。现有排序方法通常只优化 NDCG 或类似排序指标，难以保证排序结果与证据之间的耦合一致性，因此在需要审计、追责和可解释性的应用场景中存在明显瓶颈。这篇工作值得关注之处在于，它把“排序正确”进一步推进到“排序可证”，并尝试用强化学习式策略优化来同时约束排名质量与证据有效性。

#### 方法概述和架构

论文提出 Evidence-Coupled Policy Optimization（ECPO），将“排序结果 + 证据证书”视为一个联合动作进行列表式策略优化。首先，在 MAVEN-ERE 和 RAMS 上构造证据认证排序任务，采用固定的上游抽取、窗口内随机候选 ID、与计划骨架对齐的轨迹监督、硬负例以及审计参考信息，形成可训练的数据设置。随后，方法先学习一个可解释的轨迹奖励，该奖励由骨架对齐、论元一致性以及可选的图特征共同构成，用于刻画候选轨迹是否符合事件计划与语义约束。接着，在策略优化阶段，ECPO 结合三类耦合奖励：列表式排序效用、跨度级证书有效性，以及由一个无标签、确定性的验证器计算的证据循环奖励；该验证器会基于去除声明后的引文跨度重建候选支持关系，以检查证据是否足以支撑决策。整体上，模型把传统只追求 NDCG 的目标，重写为同时最大化 CertNDCG 和决策-证据耦合程度。

#### 实验结果分析

实验在 MAVEN-ERE 与 RAMS 上展开，并比较了 zero-shot、SFT、GRPO、仅用 RM 打分再附加确定性证据、语法/JSON 约束解码、validator retry、best-of-N RM 选择，以及后验式证据解释等多种基线。论文还考察了 closed-roster、predicted-roster 和 hybrid-roster 等设置，以评估方法在不同候选来源条件下的鲁棒性。摘要中没有给出具体数值，因此可见文本未给出具体数值，但整体结论指向：ECPO 相比仅优化普通排序指标的方法，更能同时提升排序质量与证据可验证性，并强化排序结果与证据之间的一致耦合。

<details>
<summary>完整摘要</summary>

用于决策支持场景的排序系统，不仅应当对候选项进行排序，还应当能够给出可由独立检查的证据。我们研究“证据可认证的候选排序”任务：给定 intent_id、预定义的计划骨架、窗口内的候选列表，以及带有跨度来源信息的文本候选轨迹，系统必须输出一个 Top-K 列表，并同时给出 doc_id:span 形式的证据证书，且这些被引用的跨度应足以还原该决策。我们在 MAVEN-ERE 和 RAMS 上实例化这一任务，使用固定的上游抽取、窗口内随机化的候选标识、与骨架对齐的轨迹监督、硬负例以及审计参考信息。我们提出 Evidence-Coupled Policy Optimization（ECPO），这是一种列表式策略优化目标，其动作是“排序与证据证书”的联合对象。ECPO 首先根据骨架对齐、论元一致性以及可选的图特征学习一个可解释的轨迹奖励；随后，它在受约束的策略上优化三类耦合奖励：列表式排序效用、跨度级证书有效性，以及由一个无标签的确定性验证器计算的证据循环奖励。该验证器会从去除声明后的引文跨度中重建候选支持关系。这样，优化目标被重新表述为：不仅要最大化普通 NDCG，还要最大化 CertNDCG 以及决策与证据之间的耦合度。评估部分将 ECPO 与 zero-shot、SFT 和 GRPO 策略，以及仅使用 RM 打分并通过确定性方式附加证据、语法/JSON 约束解码、validator retry、best-of-N RM 选择和后验证据合理化等方法进行比较，并在 closed-roster、predicted-roster 和 hybrid-roster 三种设置下开展实验。

</details>

---

### [[20_Research/Papers/强化学习/Learning_Spatiotemporal_Sensitivity_in_Video_LLMs_via_Counterfactual_Reinforcement_Learning|Learning Spatiotemporal Sensitivity in Video LLMs via Counterfactual Reinforcement Learning]]

![[assets/2605.21988_figure.png|800]]

- **arXiv**: [2605.21988](https://arxiv.org/abs/2605.21988)
- **PDF**: https://arxiv.org/pdf/2605.21988
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Spatiotemporal_Sensitivity_in_Video_LLMs_via_Counterfactual_Reinforcement_Learning|Learning Spatiotemporal Sensitivity in Video LLMs via Counterfactual Reinforcement Learning]]
- **作者**: Dazhao Du, Jian Liu, Jialong Qin, Tao Han, Bohai Gu, Fangqi Zhu, Yujia Zhang, Eric Liu, Xi Chen, Song Guo
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

视频大语言模型（Video LLMs）虽然在多个基准上表现出较高准确率，但很多时候并不是在真正追踪视频中的时空变化，而是依赖单帧线索、语言先验等“捷径”作答。这个问题在强化学习后训练中会进一步加剧，因为只奖励最终答案是否正确，容易把本来就会投机取巧的策略强化得更稳固。本文关注的是：当视觉世界发生变化、问题本身不变时，模型是否会随之改变答案，从而真正具备对时空动态的敏感性。

#### 方法概述和架构

论文提出 Counterfactual Relational Policy Optimization（CRPO），是一种面向 Video LLM 的双分支强化学习框架，用来提升时空敏感性。给定视频与问题后，系统先由 Task Router 判断题目属于空间、时间、时空复合还是静态类别，并据此选择水平翻转或时间反转作为反事实变换。随后，原始视频分支与反事实视频分支同时采样 rollout，并分别计算分支内的基础奖励与格式奖励。CRPO 的关键是 Counterfactual Relation Reward（CRR）：它不只看单个分支答得对不对，还约束两个分支答案之间的关系——动态问题应当在变换后改变答案，静态问题则应保持答案一致。这样一来，单纯依赖单帧或语言捷径的策略很难在两个分支上同时持续获得高奖励，从而被抑制。

#### 实验结果分析

作者还构建了 DyBench，一个包含 3,014 个视频的成对反事实基准，覆盖可逆动态、运动方向和事件顺序三类任务，并用严格的 pair accuracy（P-Acc）避免固定答案策略虚高。实验显示，CRPO 在时空敏感评测上优于先前 RL 方法，同时保持了有竞争力的通用视频理解能力；在 Qwen3-VL-8B 上，相比基础模型，DyBench P-Acc 提升了 +7.7，TimeBlind I-Acc 提升了 +8.2。正文节选中还提到作者做了消融与训练曲线分析，用于验证提升来自反事实双分支与关系奖励设计，而不是单纯增加数据量；可见文本未给出全部具体数值。

<details>
<summary>完整摘要</summary>

视频大语言模型（Video LLMs）虽然在基准测试上取得了很高的准确率，但往往会通过单帧线索和语言先验等捷径来回答视频问题，而不是通过跟踪时空动态来作答。这个问题在强化学习后训练阶段会被进一步放大，因为仅基于正确性奖励的训练可能会进一步强化那些不需要追踪视频动态、却仍能获得高奖励的捷径策略。为此，我们提出一个受控的反事实问题：如果视觉世界发生了变化，而问题保持不变，答案应该改变还是保持不变？基于这一视角，我们提出 Counterfactual Relational Policy Optimization（CRPO），一种用于提升时空敏感性（spatiotemporal sensitivity）的双分支强化学习框架。CRPO 通过水平翻转和时间反转构造反事实视频，在原始分支与反事实分支上同时训练，并在两者答案之间引入 Counterfactual Relation Reward（CRR）。CRR 促使模型在动态问题上改变答案、在静态问题上保持答案不变。这种跨分支约束使得捷径策略很难在两个分支上都持续获得奖励。为了评估这种性质，我们提出 DyBench，这是一个带有成对反事实视频的基准，包含 3,014 个视频，覆盖可逆动态、运动方向和事件顺序，并配有严格的 pair-accuracy 指标，以防固定答案捷径抬高分数。实验表明，CRPO 在时空敏感评测上优于以往 RL 方法，同时保持了有竞争力的通用视频性能。在 Qwen3-VL-8B 上，CRPO 相比基础模型将 DyBench 的 P-Acc 提升了 +7.7，将 TimeBlind 的 I-Acc 提升了 +8.2，这表明模型的时空敏感性得到了增强，而不是更依赖静态捷径。项目主页见 https://ddz16.github.io/crpo.github.io/ 。

</details>

---

### [[20_Research/Papers/世界模型/ChronoMedicalWorld_A_Medical_World_Model_for_Learning_Patient_Trajectories_from_Longitudinal_Care_Data|ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data]]

![[assets/2605.21963_first_page.png|800]]

- **arXiv**: [2605.21963](https://arxiv.org/abs/2605.21963)
- **PDF**: https://arxiv.org/pdf/2605.21963
- **详细分析**: [[20_Research/Papers/世界模型/ChronoMedicalWorld_A_Medical_World_Model_for_Learning_Patient_Trajectories_from_Longitudinal_Care_Data|ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data]]
- **作者**: Jiangyuan Wang, Xuyong Chen, Junwei He, Xu Xu, Shasha Xie, Fuman Han
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.02（加权：大模型 0.1，强化学习 0.16，世界模型 0.76）
- **关联关键词**: WorldModel

#### 研究背景与动机

慢性病管理往往跨越多年，临床上真正需要的是在给定治疗和沟通干预条件下，预测患者生理状态如何随时间演化的长程模拟能力，而不仅是对下一个事件的分类或风险打分。现有电子病历模型大多仍是判别式预测器，难以在多轮干预下保持稳定的闭环滚动；通用大语言模型即使加入丰富临床上下文，也容易在重复干预后发生漂移。本文聚焦长期随访场景，特别强调结构化治疗与医患/健康管理沟通并存时的建模问题，因此具有较强的临床数字孪生与个体化决策支持价值。

#### 方法概述和架构

论文提出 ChronoMedicalWorld Model（CMWM），将长期临床轨迹学习表述为一个动作条件的潜在世界模型问题。模型由静态上下文编码器、状态编码器、宽动作编码器、循环潜在转移模块以及预测头组成：状态编码器将当前临床状态与静态信息映射到潜变量，动作编码器同时接收结构化干预指示和自由文本交流的语义嵌入。循环转移模块在潜空间中按时间推进，并由预测头同时输出下一时刻的目标观测值和下一潜表示，从而兼顾可解释监督与JEPA式的潜空间学习。训练时采用六项联合目标，包括下一观测监督、下一潜变量预测、SIGReg潜表示正则，以及斜率、一致性和大跳变惩罚三种生理形状先验，以约束多步滚动中的轨迹平滑性与临床合理性。推理阶段使用 rollout-prefix 协议，让模型在训练时就对齐部署时的多步闭环滚动误差，减少训练—测试不一致导致的漂移。

#### 实验结果分析

作者以慢性肾病（CKD）中年度 eGFR 轨迹预测为案例，在 2,232 名肾内科患者队列上进行了验证，并与经过调优的 GPT-5.5 结构化提示基线比较。结果显示，CMWM 在 dynamic-50% history rollout 测试上取得 MAE 7.384、RMSE 10.256，优于 GPT-5.5 的 7.964 和 11.069，分别带来 7.28% 的 MAE 降幅和 7.35% 的 RMSE 降幅。消融结果表明，提升主要来自患者—健康教练沟通文本所对应的动作编码分支，说明将自由文本交流显式建模为动作信号具有实际价值。

<details>
<summary>完整摘要</summary>

长期临床模拟——即在给定干预条件下预测患者生理状态在数年内如何演变——是慢性病管理的核心，但现有电子健康记录（EHR）模型大多是判别式的，而通用大语言模型在反复干预下会发生漂移。为此，我们提出 ChronoMedicalWorld Model（CMWM），这是一种动作条件化的潜在世界模型框架，用于从纵向护理数据中学习患者轨迹。CMWM 将联合嵌入式状态编码器与一个宽动作编码器结合起来，后者既能接纳结构化干预指示，也能接纳自由文本沟通的嵌入表示；模型通过六项联合目标训练一个循环潜在转移模块，这六项目标包括：下一观测监督、下一潜变量预测、SIGReg 潜表示正则化，以及三种面向生理过程的形状先验（斜率、一致性和大跳变惩罚）。我们采用闭环 rollout-prefix 协议，使训练过程与部署场景一致，因此模型优化的正是它在推理时会遇到的同类多步误差。作为一个具体案例，我们将 CMWM 实例化用于慢性肾病（CKD）中年度估算肾小球滤过率（eGFR）轨迹预测。在一个包含 2,232 名肾内科患者的队列上，CKD 实例在 dynamic-50% 历史滚动测试中达到 MAE 7.384、RMSE 10.256；相比之下，经过调优的 GPT-5.5 结构化提示基线分别为 7.964 和 11.069（MAE 下降 7.28%，RMSE 下降 7.35%），且优势主要来自患者—健康教练沟通中的对话部分。该框架并不局限于 CKD：其架构、损失设计和训练协议都可推广到任何能够被表述为“周期性临床状态 + 结构化与对话式干预”的慢性疾病。

</details>

---

### [[20_Research/Papers/具身智能/EvoScene-VLA_Evolving_Scene_Beliefs_Inside_the_Action_Decoder_for_Chunked_Robot_Control|EvoScene-VLA: Evolving Scene Beliefs Inside the Action Decoder for Chunked Robot Control]]

![[assets/2605.21862_figure.png|800]]

- **arXiv**: [2605.21862](https://arxiv.org/abs/2605.21862)
- **PDF**: https://arxiv.org/pdf/2605.21862
- **详细分析**: [[20_Research/Papers/具身智能/EvoScene-VLA_Evolving_Scene_Beliefs_Inside_the_Action_Decoder_for_Chunked_Robot_Control|EvoScene-VLA: Evolving Scene Beliefs Inside the Action Decoder for Chunked Robot Control]]
- **作者**: Chushan Zhang, Ruihan Lu, Jinguang Tong, Xuesong Li, Yikai Wang, Hongdong Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

在分块式视觉-语言-动作（VLA）机器人控制中，模型通常只依据当前视觉观测生成未来几步动作，但机器人执行动作本身会引发接触、遮挡和物体位移，使得下一次视觉更新到来前，场景几何已经发生变化。现有空间型VLA主要增强“当前帧”几何理解，时间型VLA则更多汇聚历史观测，但都没有在控制块之间维护一个会被动作持续更新的场景先验。作者认为，对于长时序、闭环的机器人操作，缺失这种“动作更新后的场景状态”会导致规划依赖过时场景，从而影响稳定性与成功率。这使得该工作对具身智能和真实机器人操控都具有直接意义。

#### 方法概述和架构

论文提出 EvoScene-VLA，将“可演化的场景信念”放入动作解码器内部，并通过 recurrent scene prefix 在不同控制块之间传递。每次 VLM 调用时，输入由当前多视角图像、语言指令、观测槽和上一个控制块传回的 prior 槽组成；其中观测槽吸收当前视觉证据，prior 槽则携带上一个动作块输出的场景状态。模型在一次 flow-matching 过程中联合去噪下一段动作 chunk 和对应的场景 token chunk，动作执行后得到的场景 token 会作为下一次控制调用的 prior，从而形成“动作更新—视觉校正—再更新”的闭环。训练阶段加入两个只在训练时使用的监督模块：Geometric Anchor 通过局部跨视角遮挡深度重建与全局 3D 基础模型特征对齐来约束场景 token 的几何含义，Scene Predictor 则用未来场景 token 作为监督目标，为动作解码器提供未来场景训练信号。推理时删除这两个辅助模块，仅保留 recurrent scene prefix 与动作-场景联合去噪，因此部署开销更接近普通 VLA。

#### 实验结果分析

作者在 RoboTwin 的 31 个任务上评估了方法，和现有基线相比，EvoScene-VLA 的平均成功率更高：固定评测下从 87.2% 提升到 89.1%，随机初始条件下从 86.1% 提升到 88.5%。在 Galaxea R1-Lite 真实机器人平台上的闭环实验中，EvoScene-VLA 也优于所有对比方法，说明该场景先验机制不仅适用于仿真，也能迁移到真实操控。消融结果显示，未来场景监督、几何锚定与 recurrent prior 都对性能有累积贡献。

<details>
<summary>完整摘要</summary>

分块式视觉-语言-动作（VLA）策略会在每次更新时仅依据当前视觉观测来预测多步机器人控制。然而，机器人动作会引起接触、遮挡和物体移动，而后续决策依赖的几何信息可能在下一次视觉更新到来之前就已经发生变化。空间型 VLA 能改进当前帧的几何理解；时间型 VLA 能聚合过去帧；但二者都没有在控制块之间维护一个由动作更新过的场景先验。我们主张在控制调用之间保留一个持续存在、并由动作更新的场景状态，并据此提出 EvoScene-VLA。其 recurrent scene prefix 能在不同控制块之间传递一个具有几何感知能力的场景状态。每次调用视觉-语言模型（VLM）时，VLM 会将当前观测中的场景信息与上一控制块传来的动作更新先验结合起来；动作解码器同时输出下一段动作 chunk 和一个紧凑的场景更新。该更新会成为下一次的 prior，而当下一次调用到来时，VLM 会将其与新的观测进行校正。因此，每次控制调用都从一个同时反映最近动作和新视觉证据的场景先验开始。训练时，Scene Predictor 提供未来场景 token 目标，Geometric Anchor 将场景槽位与冻结的深度教师和 3D 教师对齐；部署时这两个模块都会被移除。在 RoboTwin 的 31 个任务上，EvoScene-VLA 在固定评测中将平均成功率从 87.2% 提升到 89.1%，在随机评测中从 86.1% 提升到 88.5%。在 Galaxea R1-Lite 真实机器人上，EvoScene-VLA 也优于所有基线。

</details>

---

### [[20_Research/Papers/具身智能/CrossVLA_Cross-Paradigm_Post-Training_and_Inference_Optimization_for_Vision-Language-Action_Models|CrossVLA: Cross-Paradigm Post-Training and Inference Optimization for Vision-Language-Action Models]]

![[assets/2605.21854_figure.png|800]]

- **arXiv**: [2605.21854](https://arxiv.org/abs/2605.21854)
- **PDF**: https://arxiv.org/pdf/2605.21854
- **详细分析**: [[20_Research/Papers/具身智能/CrossVLA_Cross-Paradigm_Post-Training_and_Inference_Optimization_for_Vision-Language-Action_Models|CrossVLA: Cross-Paradigm Post-Training and Inference Optimization for Vision-Language-Action Models]]
- **作者**: Zhi Liu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal

#### 研究背景与动机

视觉-语言-动作（VLA）模型正成为具身智能中的核心控制范式，但当前主流架构已经明显分化为两类：一种是像 OpenVLA 这样的离散动作自回归模型，另一种是像 π0.5 这样的连续动作流匹配模型。与语言模型中成熟的偏好对齐方法不同，DPO 这类后训练策略几乎只在自回归 VLA 上被验证过，连续动作骨干由于缺少易用的对数概率形式，一直难以直接做偏好优化。与此同时，现有的推理加速方法主要针对自回归模型，是否能迁移到流匹配 VLA 也缺乏系统验证，因此这篇工作关注“跨范式”后训练与推理优化，问题具有较强的现实意义。

#### 方法概述和架构

CrossVLA 先定义了一个统一的 VLA 接口，把离散自回归和连续流匹配两类骨干都抽象成可计算 policy_logp、policy_sample、sample_actions 等基础操作，从而让后训练流程能够跨架构复用。针对连续动作流匹配模型无法直接计算 chunk 级对数概率的问题，作者设计了一个基于流匹配损失的 surrogate log-probability：通过在多个时间点采样噪声插值状态，并用模型预测速度与目标速度的均方误差来近似 logp，使 DPO 可以直接作用在 π0.5 这类连续动作模型上。参数高效微调层面，论文对比了 LoRA 与 DoRA，并将其接入同一套 DPO 训练流程；DoRA 通过将权重的方向和幅值解耦，在保留预训练表征方向的同时允许幅值自适应调整。推理优化方面，作者剖析了流匹配 VLA 的时延组成，重点测试了类似 VLA-Cache 的 prefix K/V 缓存是否可迁移到 π0.5；此外还加入了一个多视角+时间对比预训练头，用 6000 张 LIBERO 帧学习可迁移的任务检索表示。

#### 实验结果分析

实验主要在 LIBERO 4-suite 上进行，覆盖 Object、Long-horizon、Goal 和 Spatial 四类任务，并采用 600 次试验、3 个随机种子评估 DPO 与 PEFT 方案。结果显示，DoRA 在 OpenVLA 的 SFT 基线上平均提升 10.4 个百分点，其中 Object 提升 20.0、Long-horizon 提升 11.0、Goal 提升 8.0、Spatial 提升 2.7 个百分点，而且 Object 子集在三个种子上都达到完全一致的 38/50，说明结果稳定性较好。对 π0.5 的验证表明，作者提出的 surrogate logp 可以稳定支持 DPO，而推理侧分析发现 denoise loop 占 sample_actions 延迟的 78.6%，因此 prefix K/V 缓存的加速上限只有 21%，且 chunk-level 与 token-level 缓存策略都会明显拉低成功率。多视角+时间预训练头在 6000 张 LIBERO 帧上实现了 99.5% 的 k-NN recall@1，用于同任务检索时相较随机基线有 36 倍提升。

<details>
<summary>完整摘要</summary>

视觉-语言-动作（VLA）模型正在快速收敛到少数几种架构模式：离散 token 自回归（例如 OpenVLA）和连续动作流匹配（例如 pi-0.5）。然而，通过 Direct Preference Optimisation（DPO）进行偏好对齐——这是语言模型中事实上的后训练步骤——几乎只在自回归 VLA 上得到研究。我们提出 CrossVLA，这是一个关于跨范式 VLA 后训练的实证研究，包含三项贡献：(i) 一个流匹配对数概率的 surrogate 估计器，使 DPO 能够在连续动作骨干上运行，而无需进行概率流 ODE 积分；(ii) 对 LoRA 和 DoRA 作为 VLA DPO 参数高效层的正面比较，发现 DoRA 相比 OpenVLA 的 SFT，在 LIBERO 4-suite 上三种随机种子、600 次试验的平均提升为 +10.4 个百分点——按子任务分别为 Object +20.0、Long-horizon +11.0、Goal +8.0、Spatial +2.7——并且在 Object 上三个种子没有方差（每个种子都是 38/50）；(iii) 一个推理时结构分析，显示 denoise loop 占 sample_actions 延迟的 78.6%，而类似 VLA-Cache 的 prefix K/V 缓存的加速上限只有 21%——同时，chunk 级和 token 级缓存策略都会使我们基准中的成功率下降到 0–80%。此外，我们在 6000 张 LIBERO 帧上预训练了一个多视角+时间投影头，在同任务检索上实现了 99.5% 的 k-NN recall@1（比随机高 36 倍），可作为下游初始化使用。所有代码、checkpoint、训练日志和复现脚本均已开源。

</details>

---

### [[20_Research/Papers/大模型/OPPO_Bayesian_Value_Recursion_for_Token-Level_Credit_Assignment_in_LLM_Reasoning|OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning]]

![[assets/2605.21851_figure.png|800]]

- **arXiv**: [2605.21851](https://arxiv.org/abs/2605.21851)
- **PDF**: https://arxiv.org/pdf/2605.21851
- **详细分析**: [[20_Research/Papers/大模型/OPPO_Bayesian_Value_Recursion_for_Token-Level_Credit_Assignment_in_LLM_Reasoning|OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning]]
- **作者**: Yu Li, Rui Miao, Tian Lan, Zhengling Qi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.4，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

在基于可验证奖励的强化学习中，LLM 推理能力提升的主流做法通常依赖 GRPO 一类轨迹级优化方法，但这类方法会把同一个优势值平均广播到整条推理链上的所有 token，导致关键推理步骤上的学习信号被稀释，而无关 token 又会引入噪声。另一方面，基于 on-policy distillation 的无 critic 方法虽然能提供逐 token 信号，却把每一步的信号当作彼此独立的局部量，没有利用前缀已经积累的轨迹证据。本文关注的问题正是：如何在不训练价值网络、也不增加额外 rollout 的前提下，实现更精细的 token-level credit assignment，这对长链推理尤其重要。

#### 方法概述和架构

论文提出 OPPO（Oracle-Prompted Policy Optimization），核心思想是把 distillation 中使用的 oracle 信号解释为“对最终成功概率的贝叶斯更新”，并沿着生成轨迹递推累积。方法通过一次额外前向计算，在每个位置估计当前前缀下的成功概率 V_t，并据此构造 token-level advantage，使其满足沿轨迹求和后严格回到终端回报与初始先验之差。OPPO 提供两种估计器：self-oracle 复用学生模型打分，teacher-oracle 则用冻结的更强教师模型对证据打分；二者只是在“谁来给 oracle 评分”上不同，后续训练流程一致。进一步地，论文把 advantage 分解为“逐 token 判别信号 × 状态权重”，其中状态权重会在模型对成功与否最不确定时放大、在轨迹已明显偏向某一结果时衰减，从而把信用集中到真正关键的 token 上。训练时，OPPO 以 GRPO 管线为基础加入 direction anchoring 和 evidence clipping，实现无需 learned critic、无需额外 rollout 的策略更新。

#### 实验结果分析

作者在两个基础 LLM 上、覆盖数学、科学与代码的 7 个推理基准上评估了 OPPO，并与 GRPO、DAPO、SDPO 等代表性方法比较。结果显示，OPPO 在 AMC'23 上最高提升 6.0 分，在 AIME'24 上最高提升 5.2 分；正文节选还提到 Teacher-OPPO 在 DAPO 上可带来最高 5.7 分和 5.2 分的提升。实验还观察到，随着回答长度增加，OPPO 的优势会单调扩大，说明其对长推理链中的信用分配问题更有效。可见文本还提到做了 ablation、值估计精度和超参数敏感性分析，但节选中未给出具体数值。

<details>
<summary>完整摘要</summary>

基于可验证奖励的强化学习已经成为提升 LLM 推理能力的标准方案，但主流算法 GRPO 会把单一的轨迹级优势赋给每个 token，这会稀释关键推理步骤上的信号，并在信息量较低的 token 上引入噪声。由 on-policy distillation 推导出的无 critic 替代方法，可以通过基于 oracle 条件的似然比提供逐 token 信号，但它们把每个信号都当作彼此独立的局部量，忽略了该位置之前已经累积的轨迹级证据。我们提出 Oracle-Prompted Policy Optimization（OPPO），其核心观察是：此前 distillation 类方法中用于局部判别的 oracle 信号，本身就可以自然地看作对最终成功概率的贝叶斯更新。将这一信号沿轨迹累积后，可以在闭式形式下、只增加一次前向传播开销，就得到每个位置的成功概率运行估计，以及一个无需 learned value network、也不需要额外 rollout 的 token-level advantage。进一步的一阶分析表明，这个优势项可以分解为 distillation 方法使用的逐 token 判别信号，并由一个状态权重调制；该权重会把信用集中到真正关键的 token 上，同时具备方向性的方差降低保证。该框架允许两种估计器，它们唯一的区别在于由哪个模型来对证据打分：self-oracle 复用学生模型，可严格退化为 on-policy distillation reward 的特例；teacher-oracle 则把打分任务交给一个更强的冻结模型。在两个基础 LLM 上、覆盖 7 个数学、科学和代码推理基准的实验中，OPPO 相比 GRPO、DAPO 和 SDPO 最多可在 AMC'23 上提升 6.0 分、在 AIME'24 上提升 5.2 分，而且随着回答长度增加，提升幅度呈单调扩大趋势。

</details>

---

### [[20_Research/Papers/强化学习/Learning_Altruistic_Collaboration_in_Heterogeneous_Multi-Team_Systems|Learning Altruistic Collaboration in Heterogeneous Multi-Team Systems]]

![[assets/2605.21723_figure.png|800]]

- **arXiv**: [2605.21723](https://arxiv.org/abs/2605.21723)
- **PDF**: https://arxiv.org/pdf/2605.21723
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Altruistic_Collaboration_in_Heterogeneous_Multi-Team_Systems|Learning Altruistic Collaboration in Heterogeneous Multi-Team Systems]]
- **作者**: Riwa Karam, Ruoyu Lin, Brooks A. Butler, Magnus Egerstedt
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

这篇论文关注的是异构多机器人系统中的跨团队协作与动态资源分配问题，具体场景可用于消防救援、灾害响应、分布式感知等任务。在这类任务中，机器人不再是“同质、可互换”的单位，而是具有不同感知、执行与计算能力的资源，且它们对团队的贡献还会随团队组成而变化。现有方法在同质假设下往往可以用较简单的局部规则求解，但一旦引入异构能力和迁移成本，分配问题就会变成组合优化难题，规模一大便难以精确求解。因此，这项工作值得关注之处在于：它把生态学中的 Hamilton’s rule 引入多团队机器人协作，并尝试用可扩展的学习方法逼近近似最优的资源重分配策略。

#### 方法概述和架构

论文提出了一个“异构 altruistic collaboration”资源分配框架，将机器人视为可在团队间转移的资源，并为每个机器人编码能力向量，令团队收益函数依赖于所获机器人集合及其能力组合。与同质情形不同，机器人从团队 i 转移到团队 j 时，不仅要考虑接收方的边际收益，还要显式加入迁移成本，从而形成带有 set-dependent 贡献的全局优化问题。作者先分析该问题的计算复杂度，并证明异构版本是 NP-hard，说明精确搜索在大规模场景下不可扩展。为此，他们设计了一个在 centralized training、decentralized execution（CTDE）下工作的图神经网络策略：输入是团队交互图、各团队状态与机器人能力信息，输出是机器人级别的迁移决策以及下一轮 robot-to-team 归属。推理阶段模型在图上进行消息传递，学习近似 Hamilton’s rule 所诱导的“利他式”分配，从而实现实时决策。整体流程是：先通过仿真/合成数据构造监督信号，再训练 GNN 预测转移与分配，最终在火灾救援任务中进行仿真和实体测试验证。

#### 实验结果分析

实验在消防场景中展开，包含软件仿真与机器人实物平台测试，用于检验该方法在异构感知与执行能力下的协作分配效果。对比基线与评价指标的具体数值在节选中未给出，但作者明确指出，学习到的策略能够在接近最优性能的同时扩展到更大规模系统。文本还强调，该方法在动态、多团队、异构资源转移条件下依然保持良好的可扩展性，说明 GNN 可以有效逼近原本不可解的组合优化过程。

<details>
<summary>完整摘要</summary>

本文研究异构多团队协作中的动态机器人分配问题，其中机器人被视为可转移的资源。我们借鉴生态学中的 Hamilton’s rule 作为一种利他式决策机制，提出了一个多团队协同资源分配框架，该框架考虑了异构能力、转移成本以及能力相关的贡献。由此得到的分配问题具有组合性质，并且被证明是 NP-hard。为了应对可扩展性问题，我们开发了一种在 centralized training and decentralized execution（CTDE）框架下的图神经网络策略，用于近似基于 Hamilton’s rule 的利他式分配。该模型在团队交互图上运行，并预测机器人级别的转移决策以及下一步 robot-to-team 归属。我们在消防场景中通过仿真和实验验证了该方法，结果表明，学习到的策略在扩展到更大系统时仍能达到接近最优的性能。

</details>

---

### [[20_Research/Papers/大模型/Value-Gradient_Hypothesis_of_RL_for_LLMs|Value-Gradient Hypothesis of RL for LLMs]]

![[assets/2605.21654_figure.png|800]]

- **arXiv**: [2605.21654](https://arxiv.org/abs/2605.21654)
- **PDF**: https://arxiv.org/pdf/2605.21654
- **详细分析**: [[20_Research/Papers/大模型/Value-Gradient_Hypothesis_of_RL_for_LLMs|Value-Gradient Hypothesis of RL for LLMs]]
- **作者**: Arip Asadulaev, Daniil Ognev, Karim Salta, Martin Takac
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.77（加权：大模型 0.25，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

在 LLM 的后训练阶段，强化学习（尤其是 PPO、GRPO 这类不依赖 critic 的方法）已经被证明能显著提升推理能力，但它们为什么有效、在什么阶段最有效，仍缺乏清晰的理论解释。传统 RL 理论通常认为没有 critic 会削弱长程信用分配，但在大模型训练中，GRPO 等方法却能稳定带来收益，这一现象值得深入分析。本文关注的是：critic-free RL 到底是如何把“价值信息”传回到参数更新中的，以及它在预训练轨迹上的收益何时最大。

#### 方法概述和架构

论文提出“Value-Gradient Hypothesis of RL for LLMs”，核心观点是：critic-free RL 的反向传播信号在本质上携带了价值梯度信息。作者先在可微 rollout 与加性噪声参数化下分析连续情形，证明 actor 更新在期望上是价值梯度式的，即反向传播得到的 costate 的条件期望等于 value gradient。随后将这一分析推广到离散 Transformer 策略，说明尽管 token 采样阻断了直接可微路径，但注意力机制提供了可微的信用传递通道，使自动微分得到的 empirical costate 能近似 BPTT 的 costate。进一步地，论文把 RL 的实际收益分解为“可用的 value gradient 信号”与“可达到的 reward headroom”，从而给出一个用于选择预训练 checkpoint 的判据。

#### 实验结果分析

从理论上，论文给出了两个关键结论：其一，在连续可微 rollout 下，GRPO/PPO 的 actor 更新可被解释为 value-gradient-like；其二，在离散 Transformer 中，通过 attention 传播的经验 costate 可以近似 BPTT costate，其误差受 sampling gap 和 policy entropy 控制。实验部分用来验证作者提出的 RL impact law 假设，即用价值梯度信号与 reward headroom 预测真实 RL 增益；根据节选内容，可见文本未给出具体数值，但图 1 表明该预测与实际 RL 增益具有较强一致性。整体上，论文不仅解释了为什么 critic-free RL 在 LLM 上有效，也给出了何时更值得做 RL 后训练的经验性原则。

<details>
<summary>完整摘要</summary>

强化学习能够显著提升预训练语言模型，但人们仍未充分理解为什么像 PPO 和 GRPO 这样的无 critic 方法能取得如此好的效果，以及它们在什么情况下应当带来最大的收益。我们提出一种针对 LLM 后训练中无 critic 强化学习的价值梯度视角。首先，在可微 rollout 和加性噪声参数化下，我们证明 actor 更新在期望上具有价值梯度式特征：反向传播会传递 costate，而其条件期望等于 value gradient。其次，对于离散的 Transformer 策略，我们证明通过注意力进行自动微分得到的经验 costate 会近似这一价值信号，其误差由 sampling gap 和 policy entropy 决定。基于这些结果，我们将 RL 的影响分解为价值梯度信号与可达的 reward headroom，并据此给出一个判据，用于判断沿着预训练轨迹的哪个阶段 RL 应当最有效。

</details>

---

### [[20_Research/Papers/其他/TO-Agents_A_Multi-Agent_AI_Pipeline_for_Preference-Guided_Topology_Optimization|TO-Agents: A Multi-Agent AI Pipeline for Preference-Guided Topology Optimization]]

![[assets/2605.21622_figure.png|800]]

- **arXiv**: [2605.21622](https://arxiv.org/abs/2605.21622)
- **PDF**: https://arxiv.org/pdf/2605.21622
- **详细分析**: [[20_Research/Papers/其他/TO-Agents_A_Multi-Agent_AI_Pipeline_for_Preference-Guided_Topology_Optimization|TO-Agents: A Multi-Agent AI Pipeline for Preference-Guided Topology Optimization]]
- **作者**: Isabella A. Stewart, Hongrui Chen, Faez Ahmed
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

拓扑优化（Topology Optimization, TO）能够自动生成高效结构，但现实设计中，设计者往往更关心“看起来像什么”“是否符合产品体验”以及“是否便于制造”等定性目标，这些意图很难直接映射到求解器参数。现有流程通常仍依赖人工反复试错，把自然语言层面的设计偏好转成边界条件、目标函数和各类超参数，既耗时又依赖经验。本文关注的是：能否让大模型驱动的多智能体系统直接理解设计意图，并在拓扑优化的迭代过程中持续自我修正，从而把设计师从低层参数调试中解放出来。

#### 方法概述和架构

论文提出 TO-Agents，一个面向偏好引导拓扑优化的多智能体 AI 管线。系统首先由人类设计者用自然语言描述问题，随后通过基于 Pydantic 的解析代理将其转换为经过校验的结构化 JSON 形式，作为拓扑优化求解器的输入。接着，拓扑优化代理调用 pyFANTOM 运行求解，并将生成的三维拓扑从多个视角渲染成图像，保存到对话历史中供后续推理使用。之后，视觉代理读取历史记录、上一轮图像与当前求解参数，结合设计者给出的定性偏好，判断应该调整哪些参数以及调整幅度，并输出可执行的修订建议。系统再把这些建议传回求解器执行新一轮优化；与此同时，一个独立的 AI judge 代理基于多视图图像对初始设计与修订设计打分，并把评价反馈加入历史，驱动下一轮改进。最后，制造代理对得分最高的结构进行后处理，使其适配增材制造，实现从意图到原型的端到端流程。

#### 实验结果分析

作者在两个长程设计任务上验证了系统：经典悬臂梁基准问题和手机支架产品设计，并在两种任务中都让系统迭代四轮、共进行十次独立重复实验。设计偏好设为具有树状、分层分支特征的生物启发式结构；结果显示，TO-Agents 在两项案例中都能在 60% 的试验中生成至少一个符合偏好的设计，相比缺少视觉或历史反馈的消融管线，成功试验数最高可提升到 6 倍。判分结果和人工评估表明，该管线能够找到有效的参数调节方向、从低分修订中恢复，并扩大设计探索范围。节选文本未给出更细的具体数值指标，但明确指出系统同时识别了 overshooting、selective memory、misplaced tools、incorrect parameter reasoning 等失败模式。

<details>
<summary>完整摘要</summary>

拓扑优化可以生成高效结构，但设计者往往需要手动把诸如期望的视觉风格、产品体验或可制造性等定性意图，转换为与这些偏好并不直接对应的求解器设置。我们提出 TO-Agents，一个将自然语言设计意图与迭代式拓扑优化连接起来的多智能体 AI 框架。该框架把人类提供的问题描述转换为经过验证的求解器输入，运行拓扑优化求解器，渲染得到的三维拓扑，并利用多视角视觉-语言推理以及一个独立的裁判代理来批评每个结果并修订求解器参数。我们在两个长程设计任务上评估该框架：一个悬臂梁基准任务和一个手机支架产品设计任务。在这两个任务中，设计者都指定了对受自然树形态启发的分层分支结构的审美偏好；系统在十次独立重复实验中执行四轮修订。TO-Agents 在每个案例研究中都能在 60% 的试验中生成至少一个符合偏好的设计，相比没有视觉或历史反馈的消融管线，成功试验数最多可提升 6 倍。裁判评分和人工评估表明，该管线能够识别有效的参数杠杆，修复低分修订，并扩展设计探索。另一个制造代理进一步对得分最高的设计进行后处理，以适配增材制造，从而实现端到端的意图到原型设计。我们还识别出若干失败模式，包括过度修正、选择性记忆、工具使用不当以及参数推理错误。这些结果表明，智能体化的拓扑优化有望将设计者从低层参数调试转向对形式与功能的高层指定，同时也凸显了实现可靠自主工程设计所需的安全保障。

</details>

---

### [[20_Research/Papers/强化学习/Scalable_On-Policy_Reinforcement_Learning_via_Adaptive_Batch_Scaling|Scalable On-Policy Reinforcement Learning via Adaptive Batch Scaling]]

![[assets/2605.21557_figure.png|800]]

- **arXiv**: [2605.21557](https://arxiv.org/abs/2605.21557)
- **PDF**: https://arxiv.org/pdf/2605.21557
- **详细分析**: [[20_Research/Papers/强化学习/Scalable_On-Policy_Reinforcement_Learning_via_Adaptive_Batch_Scaling|Scalable On-Policy Reinforcement Learning via Adaptive Batch Scaling]]
- **作者**: Jongchan Park
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

强化学习中的 on-policy 方法通常依赖较小批量来跟踪不断变化的数据分布，但这会限制训练效率和大规模并行带来的收益。作者指出，传统观点把“RL 不适合大 batch”视为固定规律，但实际上训练早期和后期的非平稳性强度并不相同：前期策略变化剧烈，需要小 batch 保持灵活性；后期策略逐渐稳定，反而更适合用大 batch 提高梯度精度并促进收敛。这个问题之所以值得关注，是因为它直接关系到 RL 能否像监督学习一样实现可扩展训练，以及能否在更大网络和更高吞吐下继续提升性能。

#### 方法概述和架构

论文提出 Adaptive Batch Scaling（ABS），核心思想是根据策略稳定性动态调整 on-policy 训练中的有效 batch size。为此，作者定义了 Behavioral Divergence 作为非平稳性指标，通过比较相邻两次参数更新前后策略在动作层面的变化，衡量策略波动程度。训练时，ABS 根据 Behavioral Divergence 反向调节 rollout 长度或 batch 大小：策略越不稳定，batch 越小；策略越稳定，batch 越大。该机制被集成到 PQN 中实现，并在训练过程中持续监测策略变化、更新 batch 配置，从而在前期保留塑性、后期降低方差并加快收敛。作者还讨论了将该方法迁移到 PPO 等其他算法的可行性，说明其设计依赖前向传播即可估计，不需要像 GNS 那样额外进行昂贵的梯度计算。

#### 实验结果分析

实验主要在 ALE 基准上进行，围绕 Full Atari-57 展开，并与固定 batch、GNS 等基线比较，同时还测试了不同 batch 调度、超参数敏感性以及在连续控制和离策略方法上的泛化。结果表明，ABS 能在 PQN 上稳定提升性能，并优于固定 batch 方案和基于 Gradient Noise Scale 的调度策略。作者还观察到一个重要结论：将更大的网络与更大的 batch 结合起来，在 ABS 的动态控制下反而获得最佳效果，说明 RL 中过去被认为难以实现的“规模化收益”是可以被解锁的。节选文本未给出具体数值。

<details>
<summary>完整摘要</summary>

传统观点认为，大批量训练在强化学习（RL）中从根本上与之不相容——一旦超过一个不大的阈值，继续增大 batch size 往往会因为数据分布的内在非平稳性而带来收益递减甚至性能下降。我们通过观察提出挑战：RL 中的非平稳性并不是固定不变的，而是会在训练过程中演化——早期阶段行为变化迅速，需要小 batch 以保持可塑性；而在后期阶段，策略接近准平稳状态，此时大 batch 能带来更精确的收敛。基于这一观察，我们提出 Adaptive Batch Scaling（ABS），它会根据学习策略的稳定性动态调整有效 batch size。ABS 的核心是 Behavioral Divergence，这是一种新的度量，用于通过衡量相邻两次更新之间动作层面的变化来量化策略的非平稳性；我们据此让 batch size 与策略波动程度成反比地进行缩放。将该方法集成到 Parallelised Q-Network（PQN）算法并在 ALE 基准上评估后，ABS 能够在早期阶段的可塑性与后期阶段的稳定收敛之间实现无缝衔接。更令人瞩目的是，结果表明：与传统观点相反，更大的网络配合更大的 batch size 能取得最佳性能——这种此前被认为在 RL 中难以实现的规模化行为，如今可通过自适应 batch 控制被释放出来。

</details>

---

### [[20_Research/Papers/大模型/Autonomous_LLM_Agents_&_CTFs_A_Second_Look|Autonomous LLM Agents & CTFs: A Second Look]]

![[assets/2605.21497_figure.png|800]]

- **arXiv**: [2605.21497](https://arxiv.org/abs/2605.21497)
- **PDF**: https://arxiv.org/pdf/2605.21497
- **详细分析**: [[20_Research/Papers/大模型/Autonomous_LLM_Agents_&_CTFs_A_Second_Look|Autonomous LLM Agents & CTFs: A Second Look]]
- **作者**: Youness Bouchari, Matteo Boffa, Marco Mellia, Idilio Drago, Thanh Minh Bui, Dario Rossi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

这篇论文关注“Autonomous LLM Agents & CTFs: A Second Look”这一问题：大模型智能体能否自动完成网络攻防中的漏洞利用任务，尤其是在 Web 类 Capture-the-Flag（CTF）挑战上接近人类水平。由于渗透测试既要求长程规划、工具调用和上下文管理，又面临网络安全人才短缺与真实漏洞被快速利用的现实压力，因此自动化能力具有很强的应用价值。作者指出，已有研究常报告此类智能体在 CTF 上接近人类的成功率，但这些结论仍需要更严格的复核。

#### 方法概述和架构

论文在 30 个基于 Web 的 CTF 挑战上重新评估 LLM 智能体，这些任务覆盖 14 类漏洞。作者手工求解所有挑战，作为参考答案，并构建了三种由简到繁的智能体架构：单一的 Executor、Executor + Evaluator、以及 Planner + Executor + Evaluator。三种架构共享相同的提示词、工具和记忆机制：智能体通过 SSH 终端访问靶机，使用 run_command 和 run_python 执行操作，并把推理轨迹、工具调用与观测结果写入 scratchpad。Executor 负责发现环境、制定利用方案并执行；Evaluator 以“LLM-as-a-judge”方式对 Executor 的动作进行评分与拦截；Planner 则先结合侦察节点生成高层攻击计划，再把计划交给 Executor 和 Evaluator 协同执行。作为外部强基线，作者还比较了通用型代理 claude-code，它能自主决定内部结构并可自动生成子代理。

#### 实验结果分析

实验在 XBOW 的 30 个 Web CTF 任务上进行，使用 GPT-4.1、GPT-5 以及 Opus 4.5（claude-code）进行对比，并以成功率、步数、成本、时长和一致性为指标。结果显示，claude-code 与作者设计的最佳架构表现相当，均解决了 19/30 个任务，说明通用型代理已是攻防任务中很强的基线。进一步分析发现，几种系统会在相同类别的挑战上反复失败，尤其是业务逻辑缺陷、竞态条件和盲注等，这表明当前智能体仍明显低于人类能力。结构化多智能体编排优于单体设计：引入 Planner 能提升执行一致性，并降低运行成本；可见文本未给出更多消融数值细节。

<details>
<summary>完整摘要</summary>

大语言模型（LLM）智能体正越来越多地被用于自动化攻防安全任务，近期一些研究甚至报告其在 Capture-the-Flag（CTF）挑战上的成功率已接近人类水平。本文对这些结果重新审视，给出一次“第二次观察”。我们在 30 个基于 Web 的 CTF 挑战上，设计并实现了若干复杂度和模块化程度不同的智能体架构，这些任务覆盖 14 类漏洞。我们使用多种 LLM 基座模型实例化这些智能体，并将其与 claude-code 进行比较；后者是一个通用型代理，能够自动决定其内部架构。评估得到三个主要发现。第一，claude-code 的表现与我们手工设计的架构相当（19/30 个任务被解决），说明通用型代理是攻防安全任务中很强的基线。第二，我们的架构和 claude-code 都在相同的挑战类别上遇到困难，揭示了阻碍当前智能体达到人类水平的持续性障碍。第三，借助我们手工设计的架构，可以系统地测量额外组件的影响，结果表明，对专业角色进行结构化编排优于单体设计，能够提升运行间一致性并降低执行成本。

</details>

---

### [[20_Research/Papers/大模型/HealthCraft_A_Reinforcement_Learning_Safety_Environment_for_Emergency_Medicine|HealthCraft: A Reinforcement Learning Safety Environment for Emergency Medicine]]

![[assets/2605.21496_figure.png|800]]

- **arXiv**: [2605.21496](https://arxiv.org/abs/2605.21496)
- **PDF**: https://arxiv.org/pdf/2605.21496
- **详细分析**: [[20_Research/Papers/大模型/HealthCraft_A_Reinforcement_Learning_Safety_Environment_for_Emergency_Medicine|HealthCraft: A Reinforcement Learning Safety Environment for Emergency Medicine]]
- **作者**: Brandon Dent
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.17（加权：大模型 0.25，强化学习 0.76，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

面向急诊医学的临床工作流，前沿大模型正在比安全评测基础设施更快地进入真实应用，但传统静态医学问答基准主要考察知识回忆，难以捕捉急诊场景中更关键的失效模式，例如多轮过程中逐步崩溃、工具误用，以及在持续临床压力下“让步”式回答。作者认为，真正影响临床安全的不是单步答题是否正确，而是模型在完整轨迹中是否始终遵守安全约束。HealthCraft 因此被设计为一个面向急诊医学的强化学习安全环境，用来评估并约束工具使用型智能体的轨迹级安全行为。

#### 方法概述和架构

HealthCraft 基于 Corecraft 架构改造而来，将世界状态构建为符合 FHIR R4 的临床数据库，包含 14 类实体、3,987 个种子实体，并通过 24 个 MCP 工具支持读取、计算、修改和工作流操作。系统由三部分组成：PostgreSQL 世界状态存储、FastMCP 工具服务器，以及负责加载任务、驱动 rollout 并计算奖励的任务引擎。奖励函数采用双层标注：先对每个任务的二元标准进行逐项判定，只要任一安全关键标准未满足，整条轨迹奖励就直接归零；若没有触发硬安全门，再根据所有标准的满足比例给出奖励。任务集以 OpenEM 的临床知识为基础生成，覆盖 195 个任务和 2,255 条二元标准，其中 515 条属于安全关键标准；同时作者还加入一个 10 任务的负类补充集，用于检验奖励信号是否适合直接用于训练。评测时，系统对轨迹进行审计，并结合确定性的 LLM-judge 覆盖层降低评测噪声；整体流程被设计为可与 Megatron + SGLang + GRPO 训练管线对接。

#### 实验结果分析

作者在 V8 版本上评估了两款前沿模型，分别报告 Claude Opus 4.6 的 Pass@1 为 24.8%，GPT-5.4 为 12.6%，对应的安全失败率分别为 27.5% 和 34.0%。在更接近真实急诊流程的多步工作流任务上，模型性能几乎崩溃：Claude 仅 1.0%，GPT-5.4 为 0.0%，说明单步能力并不能转化为复杂临床流程中的可靠执行。文本还指出，v2 到 v8 之间修复了 6 个基础设施 bug，甚至会改变“哪个模型看起来更强”的排序，强调评测基础设施本身就是测量的一部分。

<details>
<summary>完整摘要</summary>

前沿语言模型被部署到临床工作流中的速度，已经超过了安全评测基础设施的发展速度。静态医学问答基准无法捕捉急诊医学中真正重要的失效模式：轨迹级安全崩溃、工具误用，以及在持续临床压力下的让步。我们提出 HealthCraft，这是首个公开的强化学习环境，用于在真实急诊医学条件下奖励轨迹级安全行为，并由 Corecraft 改造而来。它基于 FHIR R4 世界状态构建，包含 14 类实体和 3,987 个种子实体，提供 24 个 MCP 工具，并定义了一个双层评分规则：只要任何安全关键标准被违反，奖励就会被置零。我们发布了覆盖六类任务的 195 个任务，并以 2,255 条二元标准进行评分，其中 515 条为安全关键标准；此外，一个事后补充的 10 任务负类集合将其扩展为 205 个任务和 2,337 条标准。对两个前沿模型的 V8 结果显示，Claude Opus 4.6 的 Pass@1 为 24.8%［21.5–28.4］，GPT-5.4 为 12.6%［10.2–15.6］，对应安全失败率分别为 27.5% 和 34.0%。在多步工作流——最接近真实急诊护理的代理——上，性能几乎崩溃到接近零（Claude 1.0%，GPT-5.4 0.0%），尽管它们在单个步骤上仍有部分能力。我们还记录了 v2 到 v8 之间修复的 6 个基础设施 bug，这些修复导致“哪个模型看起来更强”的顺序发生了质变；这表明基础设施保真度应被视为测量的一部分，而不是独立于测量之外。我们加入一个确定性的 LLM-judge 覆盖层，以界定评测器噪声边界；一个 60 次运行的负类烟雾测试则表明，这一奖励信号并不适合作为可直接用于训练的信号：克制类标准在烟雾测试中的通过率高达 0.929，这种结构性可被评测框架容忍的“可博弈性”，却不能被训练奖励容忍。我们按照 Corecraft 第 5.2 节搭建了与 Megatron + SGLang + GRPO 的对接框架，并将训练奖励方面的消融留作未来工作。环境、任务、评分规则和评测框架均以 Apache 2.0 许可证发布。

</details>

---

### [[20_Research/Papers/强化学习/Memory-Induced_Supra-Competitive_Outcomes_Between_Deep_Reinforcement_Learning_Agents_in_Optimal_Trade_Execution|Memory-Induced Supra-Competitive Outcomes Between Deep Reinforcement Learning Agents in Optimal Trade Execution]]

![[assets/2605.20348_figure.png|800]]

- **arXiv**: [2605.20348](https://arxiv.org/abs/2605.20348)
- **PDF**: https://arxiv.org/pdf/2605.20348
- **详细分析**: [[20_Research/Papers/强化学习/Memory-Induced_Supra-Competitive_Outcomes_Between_Deep_Reinforcement_Learning_Agents_in_Optimal_Trade_Execution|Memory-Induced Supra-Competitive Outcomes Between Deep Reinforcement Learning Agents in Optimal Trade Execution]]
- **作者**: Christos Spyridon Koulouris, Carlo Campajola
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.7（加权：大模型 0.5，强化学习 1.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

最优交易执行旨在将大额订单拆分到有限时间内完成，以在市场冲击、价格波动和执行成本之间取得平衡；当多个大资金交易者同时在场时，这一问题会从单纯控制问题转变为博弈问题。现有研究中，深度强化学习（DRL）已经被用于学习执行策略，但多智能体环境下是否会出现低于纳什基准、甚至接近合作最优的“超竞争”结果，以及这种现象究竟由何种信息结构驱动，仍不清楚。本文聚焦于 Almgren-Chriss 清算博弈，重点检验执行过程中的反馈、价格可见性与历史记忆，是否会系统性地改变学习到的策略形态与成本表现，因此具有较强的微观结构与多智能体学习交叉价值。

#### 方法概述和架构

作者构建了一个双智能体的 Almgren-Chriss 最优执行博弈，并区分了两类临时冲击设定：基于总交易量的 aggregate temporary impact，以及基于自身交易量的 own temporary impact，以对应不同的竞争基准。方法上先设计“事前调度学习”代理：两个智能体在执行开始前就一次性决定完整清算轨迹，从而移除执行过程中的中间反馈，观察仅靠预先承诺能否产生超竞争结果。随后，作者引入多种 DDQN 架构进行状态依赖的多智能体学习，让代理在每个时刻基于当前状态进行决策；在此基础上进一步比较只看当前价格的“价格条件型代理”和能够利用最近价格及自身历史动作的“历史感知型代理”。训练目标是最小化 implementation shortfall，输出则是每个时刻的成交量/清算路径，并将其与离散化的纳什基准和 TWAP 基准进行比较。

#### 实验结果分析

实验围绕双智能体 Almgren-Chriss 执行环境展开，比较了事前调度学习、基础 DDQN、价格条件型 DDQN 与历史感知型 DDQN 等方案，并以离散化纳什均衡和 TWAP 作为基线。结果表明，仅有当前价格观测并不足以稳定地产生超竞争结果，基础 DDQN 往往仍接近竞争性基准；而当代理能够访问执行期内历史，尤其是最近价格与自身过去动作时，低于纳什基准的结果显著增多且更持久。文中未给出具体数值，但结论清楚表明：超竞争行为主要由反馈、记忆以及沿真实执行路径上的状态依赖交互所驱动，而不是多智能体学习本身或单纯的价格观测。

<details>
<summary>完整摘要</summary>

本文研究：在一个共享的最优执行环境中相互作用的深度强化学习代理，是否能够维持“超竞争”结果，即实现低于相关博弈论竞争基准的 implementation shortfall。我们考察一个双智能体的 Almgren-Chriss 清算博弈，并分析学习到的行为如何依赖于回合内环境反馈、对中间价格（mid-price）的理解能力，以及代理对过去信息的掌握程度。我们首先使用事前调度学习代理来移除回合内反馈，从而隔离出在执行开始前代理就承诺完整清算轨迹时会产生什么行为。随后，我们允许代理通过多种 DDQN 架构对不断演化的状态进行条件化。我们发现，当代理能够访问回合内历史，尤其是最近的价格和自身过去的动作时，超竞争结果会显著更常出现，也更具持续性。这些发现表明，在该执行博弈中，超竞争行为并不是由多智能体学习本身或仅仅由当前价格观测所驱动，而是由反馈、记忆以及沿真实执行路径展开的状态依赖交互所驱动。

</details>

---

### [[20_Research/Papers/强化学习/Recursive_Entropic_Risk_Optimization_in_Discounted_MDPs_Sample_Complexity_Bounds_with_a_Generative_Model|Recursive Entropic Risk Optimization in Discounted MDPs: Sample Complexity Bounds with a Generative Model]]

![[assets/2506.00286_figure.png|800]]

- **arXiv**: [2506.00286](https://arxiv.org/abs/2506.00286)
- **PDF**: https://arxiv.org/pdf/2506.00286
- **详细分析**: [[20_Research/Papers/强化学习/Recursive_Entropic_Risk_Optimization_in_Discounted_MDPs_Sample_Complexity_Bounds_with_a_Generative_Model|Recursive Entropic Risk Optimization in Discounted MDPs: Sample Complexity Bounds with a Generative Model]]
- **作者**: Oliver Mortensen, Mohammad Sadegh Talebi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

这篇论文研究有限折扣MDP中的风险敏感强化学习，目标不是最大化期望回报，而是直接优化递归熵风险度量（ERM）下的最优策略与最优Q函数。此类问题在医疗、金融、运筹和交通等高风险场景中更贴近真实需求，因为决策者往往不仅关心平均收益，还关心回报波动和尾部风险。现有关于风险敏感RL的理论多集中在无折扣或非递归设定，而递归ER M在折扣MDP中的学习样本复杂度长期缺乏严格保证，因此这项工作具有明显的理论补位价值。

#### 方法概述和架构

作者假设可以访问MDP的generative model，即能对任意状态-动作对采样转移结果。基于此，他们提出了一个模型驱动算法MB-RS-QVI（Model-Based ERM Q-Value Iteration），先用采样估计转移核，再在估计模型上进行适配递归ERM目标的Q值迭代。算法输出两类结果：一是用于value learning的最优Q函数近似，二是用于policy learning的近似最优策略。其核心在于把递归熵风险的Bellman式递推嵌入模型化迭代过程，从而同时处理风险厌恶（β>0）和风险寻求（β<0）两种情形。论文进一步围绕该算法建立PAC型样本复杂度上界，并通过构造困难实例给出对应下界，用以说明复杂度依赖的不可避免性。

#### 实验结果分析

论文给出了MB-RS-QVI在value learning与policy learning上的样本复杂度上界，并证明其对状态数S和动作数A是紧的。结果表明，在折扣因子γ和风险参数β下，复杂度会出现随 |β|/(1-γ) 指数增长的项，且这种指数依赖在最坏情况下不可避免。作者同时给出对应下界，说明无论是学习最优Q函数还是学习最优策略，都至少需要指数级于 |β|/(1-γ) 的样本，这也解释了递归ERM比风险中性RL更难。正文节选主要给出了理论分析框架、算法与上下界总结，实验部分存在但节选中未给出具体数值，因此可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

我们研究有限折扣MDP中的风险敏感强化学习，使用递归熵风险度量（ERM），其中风险参数β≠0控制智能体的风险态度：β&gt;0表示风险厌恶，β&lt;0表示风险寻求。我们假设能够获得MDP的生成模型。本文关注在递归ERM下学习最优状态-动作价值函数（value learning）和最优策略（policy learning）的样本复杂度。我们提出一种基于模型的算法，称为Model-Based ERM Q-Value Iteration（MB-RS-QVI），并为value learning和policy learning分别推导出PAC型样本复杂度上界。两类PAC上界都随 |β|/(1-γ) 呈指数增长，其中γ是折扣因子。我们还建立了对应的下界，分别适用于value learning和policy learning，表明在最坏情况下，对 |β|/(1-γ) 的指数依赖是不可避免的。上述上界在状态数和动作数（S和A）上的依赖是紧的，首次为递归ERM在风险厌恶和风险寻求两种情形下都提供了严格的样本复杂度保证。

</details>

---
