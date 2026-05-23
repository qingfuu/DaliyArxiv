# cs.CL | Computation and Language | 2026-05-21

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/强化学习/DelTA_Discriminative_Token_Credit_Assignment_for_Reinforcement_Learning_from_Verifiable_Rewards|DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from Verifiable Rewards]]

![[assets/2605.21467_figure.png|800]]

- **arXiv**: [2605.21467](https://arxiv.org/abs/2605.21467)
- **PDF**: https://arxiv.org/pdf/2605.21467
- **详细分析**: [[20_Research/Papers/强化学习/DelTA_Discriminative_Token_Credit_Assignment_for_Reinforcement_Learning_from_Verifiable_Rewards|DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from Verifiable Rewards]]
- **作者**: Kaiyi Zhang, Wei Wu, Yankai Lin
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

在大语言模型的强化学习从可验证奖励（RLVR）中，奖励通常只在整段回答层面给出，但参数更新却发生在 token 层面，因此“哪个 token 该被提高概率、哪个该被压低”这一机制并不清楚。作者指出，现有 sequence-level RLVR 往往把正负优势样本的 token 梯度做加权平均，但这些均值/质心容易被格式化 token 等高频共享模式主导，从而淹没真正有区分度的稀疏信号。这个问题会削弱 RLVR 对推理能力的定向改进，因此值得进一步研究 token 级信用分配如何影响更新方向。

#### 方法概述和架构

论文提出 DelTA（Discriminative Token Credit Assignment），核心思想是从“判别器”视角重写 RLVR 更新：把 policy-gradient 更新看作对 token 梯度向量的隐式线性判别，判断某个候选 token 的概率是上升还是下降。基于这一视角，作者先将标准 sequence-level RLVR 的更新拆分为正优势侧与负优势侧两部分，并分析它们形成的 side-wise centroids（侧别质心）如何决定最终更新方向。DelTA 的关键做法是估计 token 级系数，对更能体现“本侧特征、且区别于另一侧”的 token 梯度赋予更大权重，对共享或判别性较弱的方向降权。随后，这些系数被用于重加权一个 self-normalized 的 RLVR surrogate，从而让正负两侧的有效质心更具对比性，改变最终的策略更新方向。训练时仍保持 critic-free 的 group-relative RLVR 形式，推理阶段无需额外模块，主要改动集中在训练目标中的 token 权重分配与更新构造。

#### 实验结果分析

作者在 7 个数学基准上验证了 DelTA，并与同规模最强基线比较；在 Qwen3-8B-Base 上平均提升 3.26 分，在 Qwen3-14B-Base 上平均提升 2.62 分。论文还报告了代码生成任务、不同骨干模型以及域外评测上的结果，表明 DelTA 具有较好的泛化能力。正文节选中未给出完整的具体实验数值细节，但可以看出作者还系统分析了训练动态、超参数敏感性、设计组件必要性以及 token 权重分布。

<details>
<summary>完整摘要</summary>

强化学习从可验证奖励（RLVR）已经成为提升大语言模型推理能力的核心技术之一。尽管它效果显著，但“回答级奖励”究竟如何转化为“token 级概率变化”，目前仍缺乏清晰理解。本文提出一种关于 RLVR 更新的判别器视角，表明策略梯度的更新方向在隐式上充当了 token 梯度向量上的线性判别器，并据此决定学习过程中哪些 token 概率会被提高或降低。在标准的 sequence-level RLVR 下，这个判别器由正侧与负侧的质心构成，而这些质心来自对 token 梯度向量进行优势加权平均。然而，这种质心构造容易被共享的高频模式主导，例如格式化 token，从而削弱那些稀疏但更具判别性的方向，而这些方向更能区分高奖励响应与低奖励响应。为了解决这一限制，我们提出 DelTA，这是一种判别性 token 信用分配方法，用于估计 token 系数，以放大具有侧别特征的 token 梯度方向，并对共享或判别性较弱的方向降权。这些系数会重新加权一个 self-normalized 的 RLVR surrogate，使得有效的侧别质心更具对比性，从而重塑 RLVR 的更新方向。在 7 个数学基准上，DelTA 在 Qwen3-8B-Base 和 Qwen3-14B-Base 上分别比同规模最强基线平均高出 3.26 分和 2.62 分。进一步在代码生成、不同骨干模型以及域外评测上的结果也表明，DelTA 具有良好的泛化能力。

</details>

---

### [[20_Research/Papers/强化学习/LamPO_A_Lambda_Style_Policy_Optimization_for_Reasoning_Language_Models|LamPO: A Lambda Style Policy Optimization for Reasoning Language Models]]

![[assets/2605.21235_figure.png|800]]

- **arXiv**: [2605.21235](https://arxiv.org/abs/2605.21235)
- **PDF**: https://arxiv.org/pdf/2605.21235
- **详细分析**: [[20_Research/Papers/强化学习/LamPO_A_Lambda_Style_Policy_Optimization_for_Reasoning_Language_Models|LamPO: A Lambda Style Policy Optimization for Reasoning Language Models]]
- **作者**: Zhe Yuan, Yipeng Zhou, Jinghan Li, Xinyuan Chen, Bowen Deng, Zhiqian Chen, Liang Zhao
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

强化学习带有可验证奖励（RLVR）已经成为提升推理语言模型的重要路线，尤其适用于数学、代码和科学问答等可以自动判对错的任务。现有常用的组相对目标（如 GRPO）通常把同一组候选答案压缩成单一标量统计，丢失了候选之间细粒度的关系信息，在稀疏终局奖励下容易出现信用分配不足。对于多个答案仅在推理质量上略有差异的场景，这种损失会更加明显，因此本文值得关注。

#### 方法概述和架构

论文提出 LamPO（Lambda Style Policy Optimization），用“Pairwise Decomposed Advantage”替代传统的组内标量优势。具体做法是：对同一提示词采样得到的一组回答，计算任意两两回答之间的奖励差，并结合旧策略下两者序列对数概率差构造一个置信感知权重，用于调节每一对比较的贡献。LamPO 仍然保持 PPO/GRPO 风格的无 critic、剪切更新结构，即用新的 pairwise 优势替换原来的组优势来计算 token 级策略目标。若存在参考解，方法还会加入一个轻量的基于 ROUGE-L 的稠密辅助奖励，以缓解奖励稀疏问题。整体训练流程是：按组生成候选回答、计算终局奖励和序列分数、在组内做两两比较得到 PDA、再结合 KL 正则进行参数更新。

#### 实验结果分析

实验在 Mixture-of-Thoughts 训练数据上进行，并在 AIME24、AIME25、MATH-500 和 GPQA-Diamond 上评测，使用 Qwen3-1.7B、Qwen3-4B 和 Phi-4-mini，与 CoT、GRPO、DAPO、GSPO、SimpleRL-Zoo、PRIME、RLPR 等基线比较。结果显示 LamPO 在三种骨干模型上都稳定优于 GRPO，并且在多个基准上取得最佳成绩，说明两两关系建模比仅用组均值更能提升推理学习效果。节选中的消融还表明，温度参数和稠密辅助奖励会影响性能，但可见文本未给出完整消融数值。

<details>
<summary>完整摘要</summary>

带有可验证奖励的强化学习（RLVR）已成为提升推理语言模型的有效范式，适用于数学、代码以及科学问答等任务。然而，广泛使用的组相对目标（例如 GRPO）会用标量统计量来概括每个采样组，因此丢弃了候选响应之间细粒度的关系信息。这会削弱在稀疏终局奖励下的信用分配，尤其是在多个生成解仅在推理质量上略有差异时更为明显。为此，我们提出 LamPO，一种 Lambda Style Policy Optimization 方法，用“Pairwise Decomposed Advantage”替代标量组优势。LamPO 在每个响应组内聚合两两奖励差，并用基于序列对数概率差计算的置信感知权重对每次比较进行调制，同时保留了 PPO 风格优化中无 critic 和剪切更新的结构。当存在参考解时，我们进一步加入一个轻量级的基于 ROUGE-L 的稠密辅助奖励，以减轻奖励稀疏问题。在 AIME24、AIME25、MATH-500 和 GPQA-Diamond 上，结合 Qwen3-1.7B、Qwen3-4B 和 Phi-4-mini 的实验表明，LamPO 相比 GRPO 以及近期 RLVR 变体始终表现更好，训练动态更稳定，样本效率也更高。

</details>

---

### [[20_Research/Papers/具身智能/MemGym_a_Long-Horizon_Memory_Environment_for_LLM_Agents|MemGym: a Long-Horizon Memory Environment for LLM Agents]]

![[assets/2605.20833_figure.png|800]]

- **arXiv**: [2605.20833](https://arxiv.org/abs/2605.20833)
- **PDF**: https://arxiv.org/pdf/2605.20833
- **详细分析**: [[20_Research/Papers/具身智能/MemGym_a_Long-Horizon_Memory_Environment_for_LLM_Agents|MemGym: a Long-Horizon Memory Environment for LLM Agents]]
- **作者**: Wujiang Xu, Yu Wang, Kai Mei, Kaiqu Liang, Zhenting Wang, Mingyu Jin, Han Zhang, Shi-Xiong Zhang, Wenyue Hua, Sambit Sahu, Dimitris N. Metaxas
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.25（加权：大模型 1.05，强化学习 0.2）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

大模型智能体在代码修复、网页操作、深度检索和工具调用等长时程任务中，必须持续决定哪些观察、工具输出和中间结论需要保留、压缩或遗忘，这种“执行中的记忆形成”比静态长上下文回忆更接近真实应用。现有记忆评测大多集中在多轮对话中的个人信息保留，较少衡量智能体在真实环境交互中动态形成记忆的能力，因此训练出来的记忆系统往往难以迁移到编码和网页导航等场景。与此同时，现有长程智能体基准通常只看最终任务成功率，难以区分记忆、推理、检索和工具使用各自的影响，导致记忆方法的迭代成本高、评估也不够可解释。这篇工作值得关注的原因在于，它试图把“记忆能力”从复杂智能体任务中单独拎出来评测，并把评测结果直接转化为可训练信号。

#### 方法概述和架构

作者提出 MemGym，一个面向长时程智能体记忆的统一评测与训练环境。该框架把五个评测轨道统一到同一套记忆接口之下，分别覆盖 tau2-bench 这类工具调用对话、MEMGYM-DR 深度研究搜索、SWE-Gym 与 MEMGYM-CODEQA 编码任务，以及 WebArena-Infinity 的计算机使用任务。核心设计是把记忆模块显式插入到策略模型的上下文构造流程中，在每一步由 memory manager 先压缩或整理上下文，再交给 agent 生成动作，然后由环境执行 step，并记录压缩事件、遗忘内容和元数据。为了让不同记忆策略可比较，MemGym 报告的是“memory-isolated”分数，即在固定推理模型下比较有无记忆时的性能差值，从而尽量剥离推理、检索和工具能力的干扰。

#### 实验结果分析

实验在五个环境上统一评估多种记忆家族和无记忆对照，覆盖 17 个（轨道，策略）组合；文本可见部分未给出完整成绩表，但强调该设置能够把记忆收益与其他能力分离，便于横向比较不同策略。作者还构造了可控长度的 MEMGYM-DR 和 MEMGYM-CODEQA 合成流水线，并通过逐阶段消融验证其确实测试的是目标记忆通道，而不是参数记忆泄漏或无关干扰。为降低编码环境评测成本，论文训练了 MemRM，一个基于 Qwen3-1.7B、采用 QLoRA 微调的轻量奖励模型，在 SWE-Gym 的独立同分布划分上达到 AUROC 0.985，用亚秒级分类调用替代昂贵的 Docker 完整回放。整体结论是：MemGym 可以把原本难以系统研究的长程智能体记忆问题，变成可统一评测、可对比、也可用于后续训练闭环优化的任务。

<details>
<summary>完整摘要</summary>

记忆是大模型智能体在长时程任务中运行时的一项核心能力。现有记忆基准主要评估多轮聊天场景中对个性化信息的保留，忽视了智能体在长时间执行过程中动态形成记忆的过程。因此，这些基准所产生的记忆系统在编码和网页导航等更真实的智能体环境中迁移效果较差。我们提出 MemGym，这是一个面向智能体记忆的基准，它将已有的智能体 gym 和我们自建的、以记忆为基础的流水线统一到一个记忆—推理接口之下。MemGym 覆盖五条评测轨道，分属四类智能体场景：工具调用对话（tau2-bench）、多轮深度研究搜索（MEMGYM-DR）、编码（SWE-Gym 和 MEMGYM-CODEQA）以及计算机使用（WebArena-Infinity）。MemGym 报告的是记忆隔离分数，它将记忆表现与推理、检索和工具使用能力解耦，因此可以在不受这些干扰因素影响的情况下对记忆策略进行排序。我们为 MEMGYM-CODEQA 和 MEMGYM-DR 设计的合成流水线具有长度可控、每个阶段都经过消融验证，并且与下游场景高度一致。为了使编码环境上的评测在学术上可负担，我们训练了 MemRM，这是一个轻量级奖励模型（在 QLoRA 下微调的 Qwen3-1.7B），它把压缩质量打分为一个快速的标量输出，用以替代完整的 Docker 回放。

</details>

---

### [[20_Research/Papers/强化学习/Auto-Dreamer_Learning_Offline_Memory_Consolidation_for_Language_Agents|Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents]]

![[assets/2605.20616_figure.png|800]]

- **arXiv**: [2605.20616](https://arxiv.org/abs/2605.20616)
- **PDF**: https://arxiv.org/pdf/2605.20616
- **详细分析**: [[20_Research/Papers/强化学习/Auto-Dreamer_Learning_Offline_Memory_Consolidation_for_Language_Agents|Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents]]
- **作者**: Chongrui Ye, Yuxiang Liu, Yu Wang, Haofei Yu, Yining Zhao, Ge Liu, Julian McAuley, Jiaxuan You
- **cs 子类**: cs.CL
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.55（加权：大模型 0.75，世界模型 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

语言智能体越来越多地被用于一串彼此相关的任务，而不是单次孤立交互，因此记忆系统不仅要“记住”，还要把经历过的内容提炼成可复用的知识、流程和环境先验。现有的检索增强记忆与结构化记忆方法，通常把“写入”和“整理”放在同一个在线流程里，导致模型只能基于当前会话局部更新，难以跨会话发现重复模式、抽象共享策略或清理冗余条目。作者借鉴互补学习系统理论，提出将快速经验积累与慢速跨会话整合分离，这使得该工作对语言智能体的长期记忆设计具有代表性。

#### 方法概述和架构

论文提出 Auto-Dreamer，一个用于语言智能体记忆的离线整合器。系统采用“双时间尺度”设计：在线由固定的 writer 从每个会话中快速写入分类型记忆条目；离线由 Auto-Dreamer 读取一个被选中的工作区域及其带溯源关系的原始轨迹，把该区域视为只读证据，并通过受限的工具调用检索条目、检查来源轨迹，最后综合生成一组更紧凑的替代记忆。其核心操作是 region rewriting：不是原地编辑单条记忆，而是用新生成的 replacement set 整体替换旧区域，从机制上鼓励抽象、去重、矛盾消解与选择性遗忘。训练时，模型使用 GRPO 优化，以端到端任务表现为主要奖励，并加入基于随机掩码的反事实效用项，用来区分真正“有用”的记忆与冗余记忆；任务智能体、检索器、writer 和记忆 schema 在训练中保持固定，从而突出离线整合器本身的作用。

#### 实验结果分析

作者在 ScienceWorld 上训练 Auto-Dreamer，并在 ScienceWorld、ALFWorld、WebArena 上进行评估，同时还考察了固定银行整合与消融设置。实验显示，Auto-Dreamer 在 ScienceWorld 上比最强基线高 7 个点，同时活跃记忆库规模小 12 倍；在未重新训练的 ALFWorld 与 WebArena 上也保持领先，其中 ALFWorld 上记忆量比最强基线少 6 倍。正文节选还指出，离线区域重写本身就能提升已有记忆库的质量，而反事实效用项能够抑制冗余记忆、不过度牺牲任务性能；可见文本未给出更多具体数值。

<details>
<summary>完整摘要</summary>

语言智能体正越来越多地在一系列相关任务上运行，但现有记忆系统仍难以把累积经验转化为可复用知识。检索增强和结构化记忆方法可以有效记录每个会话中的观察结果，但它们往往把记忆获取与整合耦合在同一个在线过程中，导致智能体缺少跨会话的全局视角，难以发现重复模式、抽象共享流程或删除冗余条目。受互补学习系统理论启发，我们提出 Auto-Dreamer，一个用于语言智能体记忆的学习式离线整合器。Auto-Dreamer 将快速的逐会话记忆获取与缓慢的跨会话整合解耦。给定一个类型化记忆库中的选定工作区域，整合器把该区域视为只读证据，对其进行有界的工具调用，以检查条目及其与原始轨迹相连的溯源信息，并合成一组新的、紧凑的替代条目，用于跨会话抽象并取代原区域。我们使用 GRPO 训练 Auto-Dreamer，并以端到端智能体性能作为奖励信号，从而学习如何整合由快速在线经验获得的记忆。仅在 ScienceWorld 轨迹上训练后，Auto-Dreamer 在 ScienceWorld 上比固定式、强化学习训练式以及提示式记忆基线高出 7 分，同时使用的活跃记忆库比最强基线小 12 倍；在未重新训练的情况下，它在留出的 ALFWorld 和 WebArena 上也继续保持领先——在 ALFWorld 上使用的记忆量比最强基线少 6 倍。

</details>

---
