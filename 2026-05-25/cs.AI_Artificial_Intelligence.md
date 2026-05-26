# cs.AI | Artificial Intelligence | 2026-05-25

#arxiv #ComputerScience

**论文数**: 40

### [[20_Research/Papers/大模型/SkillOpt_Executive_Strategy_for_Self-Evolving_Agent_Skills|SkillOpt: Executive Strategy for Self-Evolving Agent Skills]]

![[assets/2605.23904_figure.png|800]]

- **arXiv**: [2605.23904](https://arxiv.org/abs/2605.23904)
- **PDF**: https://arxiv.org/pdf/2605.23904
- **详细分析**: [[20_Research/Papers/大模型/SkillOpt_Executive_Strategy_for_Self-Evolving_Agent_Skills|SkillOpt: Executive Strategy for Self-Evolving Agent Skills]]
- **作者**: Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang...
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

当前大模型智能体的“技能”通常依赖人工编写、一次性生成，或在反馈下进行较松散的自我修订，这些方式都不像深度学习中的参数优化那样可控、可复现，也难以稳定地优于初始版本。论文关注的是：当模型权重被冻结时，如何把面向任务的流程性知识做成可训练、可验证、可复用的外部文本状态，用于工具调用、文档处理、数学推理和具身决策等智能体场景。作者指出，现有方法往往优化提示词或系统配置，而不是把“技能文档”本身当作可持续训练的对象，因此在跨模型、跨执行环境迁移时常不够稳健。

#### 方法概述和架构

论文提出 SkillOpt，一种面向智能体技能的可控文本空间优化器。其输入是冻结的目标模型、初始技能文档、任务轨迹与打分结果，输出则是更新后的单个技能文档 best_skill.md。方法流程分为前向与反向两步：前向阶段先让目标模型在训练集上执行 rollout，收集成功/失败轨迹、工具调用、观察信息与最终得分；反向阶段由一个独立的优化器模型对这些轨迹做分批反思，生成结构化的 add/delete/replace 编辑建议。SkillOpt 通过“文本学习率预算”限制每次最多应用的编辑数，并将候选编辑经过验证集门控，只有当验证分数严格提升时才接受更新；同时保留被拒绝编辑作为负反馈，配合 epoch 级别的 slow/meta update 以维持长程稳定性。整个过程不改变目标模型权重，部署时也不额外增加推理调用。

#### 实验结果分析

作者在六个基准、七个目标模型和三种执行方式（直接对话、Codex、Claude Code）上评估了 SkillOpt，覆盖 52 个“模型-基准-执行环境”组合。结果显示，SkillOpt 在全部 52 个组合上都达到最好或并列最好，并且在各个单项设置上都优于人写技能、一次性 LLM 技能、Trace2Skill、TextGrad、GEPA 和 EvoSkill 等基线。以 GPT-5.5 为例，SkillOpt 相比无技能版本分别在直接对话、Codex 智能体循环和 Claude Code 环境中带来显著提升；消融实验也表明，受限编辑、验证门控、拒绝编辑缓冲和 slow/meta update 都对稳定优化有关键作用。转移实验进一步显示，优化后的技能文档可以跨模型规模、跨执行环境以及跨相近基准继续发挥效果。

<details>
<summary>完整摘要</summary>

当今的智能体技能通常是手工编写、一次性生成，或者通过松散控制的自我修订来演化的——这些方式都不像深度学习中的优化器那样在技能层面进行训练，也都无法在反馈下稳定地优于其初始状态。我们认为，技能应该被训练为冻结智能体的外部状态，并采用与权重空间优化相同的纪律，以保证可复现性。SkillOpt 是据我们所知首个系统化、可控的文本空间智能体技能优化器：一个独立的优化器模型将带评分的 rollout 转化为对单个技能文档的有界增删改编辑，并且只有当某次编辑严格提升留出验证集分数时才会被接受。文本形式的学习率预算、被拒绝编辑缓冲区以及按 epoch 进行的慢更新/元更新，使技能训练保持稳定，同时在部署时不增加任何推理阶段的模型调用。我们在六个基准、七个目标模型和三种执行框架（直接对话、Codex、Claude Code）上进行评估，SkillOpt 在全部 52 个被评估的（模型，基准，框架）组合中均达到最好或并列最好，并且在每个组合上都优于人类技能、一次性 LLM 技能、Trace2Skill、TextGrad、GEPA 和 EvoSkill。以 GPT-5.5 为例，它将无技能状态下的平均准确率在直接对话中提升了 23.5 个百分点，在 Codex 智能体循环中提升了 24.8 个百分点，在 Claude Code 中提升了 19.1 个百分点。进一步的迁移实验表明，经过优化的技能工件在跨模型规模、跨 Codex 与 Claude Code 执行环境，以及迁移到相近数学基准而无需进一步优化时，仍然能够保留其价值。

</details>

---

### [[20_Research/Papers/强化学习/Any2Any_Efficient_Cross-Embodiment_Transfer_for_Humanoid_Whole-Body_Tracking|Any2Any: Efficient Cross-Embodiment Transfer for Humanoid Whole-Body Tracking]]

![[assets/2605.23733_figure.png|800]]

- **arXiv**: [2605.23733](https://arxiv.org/abs/2605.23733)
- **PDF**: https://arxiv.org/pdf/2605.23733
- **详细分析**: [[20_Research/Papers/强化学习/Any2Any_Efficient_Cross-Embodiment_Transfer_for_Humanoid_Whole-Body_Tracking|Any2Any: Efficient Cross-Embodiment Transfer for Humanoid Whole-Body Tracking]]
- **作者**: Ming Yang, Tao Yu, Feng Li, Hua Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

人形机器人中的 whole-body tracking（WBT，整机身轨迹跟踪）是实现高保真动作模仿、遥操作和后续 loco-manipulation 的关键基础能力，但这类模型通常需要海量动作数据与大规模仿真算力才能从头训练。由于不同人形机器人的关节数量、连杆结构、传感接口和动力学特性并不一致，WBT 策略往往强烈依赖源机器人构型，直接迁移到新平台效果不稳定。论文关注的问题很实际：能否在尽量少的数据和计算下，把一个已经训练好的 WBT 专家快速迁移到新的 humanoid 上，这对于新机器人平台的快速部署很有价值。

#### 方法概述和架构

论文提出 Any2Any，一种面向人形机器人跨本体迁移的参数高效后训练范式。方法先做 kinematic alignment：将源机器人与目标机器人的观测布局和关节级输入/输出空间对齐，使预训练策略在结构上能够被目标机器人复用。随后进行 dynamics adaptation：仅在对动力学最敏感的模块中插入轻量级 PEFT 组件，如 LoRA 或 adapter，并冻结其余主体参数，以尽量保留源策略学到的运动先验。整体流程是先通过对齐解决“能不能用”的结构问题，再通过局部微调解决“用得准不准”的动力学差异问题。方法基于 actor-critic + PPO 的 WBT 策略结构，适用于不同骨干网络，并以目标机器人的少量数据和少量训练开销完成迁移。

#### 实验结果分析

作者在多个源-目标转移对上验证了 Any2Any，覆盖两种预训练 WBT backbone 和四种目标 humanoid 构型，并与从头训练及其他基线进行了比较。实验表明，该方法能显著加速收敛、降低训练成本，同时获得有竞争力甚至更优的轨迹跟踪性能。尤其值得注意的是，使用仅约 1% 的计算和数据，相比完整训练即可将预训练在 Unitree G1 上的 Sonic 模型成功迁移到 LimX Oli 和 LimX Luna。文中还进行了结构组件和数据/算力预算的消融分析，显示局部适配与 kinematic alignment 的组合是跨本体转移有效性的关键。

<details>
<summary>完整摘要</summary>

整机身轨迹跟踪（WBT）模型已经成为人形机器人的关键基础，可使机器人以高保真方式模仿多样化动作。然而，从零开始训练此类模型需要大规模数据和计算，这使得在新的人形平台上快速部署的成本非常高。这引出了一个自然问题：预训练的 WBT 模型能否以最小化适配的方式跨本体迁移？为回答这一问题，我们提出 Any2Any，这是一种能够仅用少量数据和算力，将现有 WBT 专家高效迁移到新的人形本体上的范式。Any2Any 首先在源人形与目标人形之间进行运动学对齐，使输入和输出空间对齐，从而让预训练的源策略能够在目标本体上被合理复用。随后，Any2Any 通过在选定的、对动力学变化敏感的模块中施加轻量级参数高效微调（PEFT）组件来进行动力学适配，在保留有用行为先验的同时，针对目标机器人进行定向调整。大量针对多个 humanoid 平台和不同预训练 backbone 的实验表明，与从头训练相比，Any2Any 显著加快了收敛并降低了训练成本，同时实现了具有竞争力或更优的轨迹跟踪性能。尤其值得注意的是，在仅使用完整训练所需 1% 的计算和数据的情况下，Any2Any 成功将预训练于 Unitree G1 的 Sonic 模型迁移到了 LimX Oli 和 LimX Luna。上述结果表明，预训练的 WBT 专家可以在不同本体之间被高效复用，为在新机器人上可扩展地部署人形整机身控制提供了一条可行路径。

</details>

---

### [[20_Research/Papers/大模型/MemAudit_Post-hoc_Auditing_of_Poisoned_Agent_Memory_via_Causal_Attribution_and_Structural_Anomaly_Detection|MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection]]

![[assets/2605.23723_figure.png|800]]

- **arXiv**: [2605.23723](https://arxiv.org/abs/2605.23723)
- **PDF**: https://arxiv.org/pdf/2605.23723
- **详细分析**: [[20_Research/Papers/大模型/MemAudit_Post-hoc_Auditing_of_Poisoned_Agent_Memory_via_Causal_Attribution_and_Structural_Anomaly_Detection|MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection]]
- **作者**: Zhewen Tan, Yilun Yao, Huiyan Jin, Wenhan Yu, Guoan Wang, Mengyuan Fan, liang lu, Feng Liu, Xiangzheng Zhang, Duohe Ma, Tong Yang, Lin Sun
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

随着大模型智能体开始依赖持久化记忆来保存历史交互、检索示例并支持长程任务执行，记忆机制也随之成为新的安全薄弱点。攻击者可以通过普通交互把恶意记录写入智能体记忆，之后这些记录会在检索时持续影响推理与行动，造成延迟且隐蔽的行为操控。现有防护多是在线过滤或输出拦截，但当有害行为已经发生后，仍缺少一种能事后定位“到底是哪条记忆导致了问题”的审计方法，因此这项工作很值得关注。

#### 方法概述和架构

论文提出 MemAudit，一个用于记忆增强型 LLM 智能体的事后因果审计框架。它针对一次已发生的有害事件 e=(q*, y*, R*)，从两条互补路径给记忆打分：一条是反事实记忆影响分数 CMIS，通过把某条记忆从检索/存储中移除并重放事件，观察有害输出的变化来衡量其因果贡献；另一条是记忆一致性图上的结构异常分数 CAS，把每条记忆放到全局记忆图中，结合语义相似度与自然语言推理的矛盾/蕴含关系，识别与周边结构明显不一致的记忆。随后，方法将归一化后的 CMIS 与 CAS 按权重 α 融合成 detoxification score，对可疑记忆排序。最终系统输出的是一个待删除/待清理的记忆子集，用于在不依赖毒化标签的情况下对记忆库进行后处理净化。

#### 实验结果分析

作者在真实的事后审计设定下，使用 MINJA 这种“仅通过查询交互完成记忆注入”的攻击进行评估，并分别在 QA 与推理型智能体场景中测试。结果表明，MemAudit 在两类任务上都能显著降低攻击成功率：QA 场景中从 70% 降到 0%，RAP 场景中从 83.3% 降到 0%。正文节选还提到作者做了组件消融、融合权重消融和污染分析，以验证因果信号与结构信号的互补性；更细的实验设置和各项对比数值在节选中未完全展开。

<details>
<summary>完整摘要</summary>

大模型智能体越来越依赖持久化记忆来存储历史交互、检索相关示例，并提升长程任务执行能力。然而，这种记忆机制也带来了现实中的安全漏洞：攻击者可以通过普通交互向智能体记忆中注入恶意记录，而这些记录之后又会被检索出来，进而影响智能体的推理与行动。现有防御主要聚焦在线干预，例如提示过滤或输出拦截，但它们并不能解决一个事后问题：当有害行为已经被观察到时，究竟是哪一条已存储的记忆应当为其负责。为此，我们提出 MemAudit，一个面向记忆增强型 LLM 智能体的事后因果记忆审计框架。该框架结合两种互补信号：（1）反事实记忆影响分数，用于衡量每条记忆对有害输出的因果贡献；（2）记忆一致性图，用于识别整个记忆库中结构上异常的记忆。我们在 MINJA 攻击下评估 MemAudit。MINJA 是一种仅通过查询的记忆注入攻击，恶意记录不是直接修改记忆库，而是通过正常的智能体交互生成并写入记忆。我们在问答和推理型智能体两类场景中进行实验，结果显示，在真实的事后审计设定下，MemAudit 能显著降低攻击成功率：QA 场景中的攻击成功率从 70% 降至 0%，RAP 场景中的攻击成功率从 83.3% 降至 0%。

</details>

---

### [[20_Research/Papers/大模型/OnePred_Next-Query_Prediction_via_Recursive_Intent_Memory_in_Multi-Turn_Conversations|OnePred: Next-Query Prediction via Recursive Intent Memory in Multi-Turn Conversations]]

![[assets/2605.23668_figure.png|800]]

- **arXiv**: [2605.23668](https://arxiv.org/abs/2605.23668)
- **PDF**: https://arxiv.org/pdf/2605.23668
- **详细分析**: [[20_Research/Papers/大模型/OnePred_Next-Query_Prediction_via_Recursive_Intent_Memory_in_Multi-Turn_Conversations|OnePred: Next-Query Prediction via Recursive Intent Memory in Multi-Turn Conversations]]
- **作者**: Jiangwang Chen, Bowen Zhang, Zixin Song, Jiazheng Kang, Xiao Yang, Da Zhu, Guanjun Jiang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.65（加权：大模型 0.45，强化学习 0.2）
- **关联关键词**: LLM, RL

#### 研究背景与动机

LLM 对话系统虽然已经广泛应用于多轮交互，但整体上仍然是“被动式”的：只有在用户发出新问题后才开始响应。下一查询预测的目标，是仅根据前文对话提前推测用户接下来会问什么，这不仅能用于主动推荐后续问题，还能支持检索预取、推理链路预热和系统路由，从而降低感知延迟。现有方法面临明显的效率—效果权衡：直接拼接全部历史会导致上下文长度和 token 成本随轮次线性增长，而只保留最新一轮又会丢失跨轮的关键信息。本文之所以值得关注，在于它把问题聚焦到“如何压缩出对预测真正有用的意图轨迹”，并为该任务构建了专门基准。

#### 方法概述和架构

论文提出 OnePred，用递归更新的意图记忆作为跨轮上下文的唯一载体，而不再直接读取完整原始历史。每一轮中，模型只输入上一轮记忆 m_{t-1} 和当前用户—助手对话 (q_t, r_t)，再输出更新后的记忆 m_t；该记忆被限制在固定 token 上限内，从机制上控制每轮推理成本。作者设计了一个两阶段强化学习训练流程：第一阶段使用全历史输入训练模型先学会“预测什么”，第二阶段去掉历史访问，仅保留记忆链路训练模型学会“压缩什么”，使记忆逐步变成面向预测的意图链。为了支撑评测，论文还构建了 NQP-Bench，包含来自私有部署日志、WildChat 和 ShareChat 的多个子集，并采用 5 分制的意图相关性评分来衡量生成预测与真实下一查询的匹配程度。

#### 实验结果分析

实验在 NQP-Bench 及其不同子集上，与多种基线和不同模型规模进行对比，评测重点包括预测质量与推理效率。结果显示，OnePred 在所有基线上都保持了更好的预测表现，同时每轮 token 消耗相比全历史输入最高可减少 22 倍。论文还报告了消融分析和长度分组实验，结论是两阶段训练具有互补增益，且随着对话变长，OnePred 的优势进一步扩大。

<details>
<summary>完整摘要</summary>

尽管大语言模型（LLM）对话系统每天处理数以百万计的多轮对话，它们本质上仍然是被动式的：只有在用户输入查询后才进行响应。迈向主动交互的关键一步，是下一查询预测，即仅根据前文对话来预判用户接下来会提出什么问题。该任务的进展受限于缺乏专门基准，以及一个根本性的效率—质量权衡：天真地拼接完整对话历史会带来随长度线性增长的 token 消耗，而只截断到最近一轮又会丢失关键的跨轮上下文。我们的核心洞察是：准确预测并不需要重新读取原始历史；只需跟踪用户在不同主题、未解决需求和兴趣转移中的演化意图轨迹即可。为此，我们提出 OnePred，它维护一个递归更新的记忆作为唯一的跨轮上下文，使每轮成本与对话长度无关。我们通过一个两阶段强化学习流程训练模型：第一阶段教模型“预测什么”，第二阶段教模型“压缩什么”，将记忆塑造成面向预测的意图链。为建立严格的测试平台，我们引入了 NQP-Bench，覆盖三个不同子集。实验表明，与全历史输入相比，OnePred 在每轮 token 消耗上最多可减少 22 倍，同时在预测质量上持续优于所有基线，并且在更长的对话上收益更大。我们的代码已公开发布于 https://github.com/ZBWpro/OnePred。

</details>

---

### [[20_Research/Papers/大模型/One_Policy,_Infinite_NPCs_Persona-Traceable_Shared_RL_Policies_for_Scalable_Game_Agents|One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents]]

![[assets/2605.23652_figure.png|800]]

- **arXiv**: [2605.23652](https://arxiv.org/abs/2605.23652)
- **PDF**: https://arxiv.org/pdf/2605.23652
- **详细分析**: [[20_Research/Papers/大模型/One_Policy,_Infinite_NPCs_Persona-Traceable_Shared_RL_Policies_for_Scalable_Game_Agents|One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents]]
- **作者**: Yoosung Hong
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.6，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

面向生活模拟类游戏，系统往往需要在同一世界里同时驱动数百到数千个 NPC，而且每个角色都应表现出稳定、可区分的人格，还要能被设计师用自然语言直接控制。现有行为树、逐角色强化学习、无监督技能发现和逐步调用 LLM 的方案，分别在人格一致性、可控性、零样本泛化或实时推理速度上存在明显短板。本文关注的正是“如何用一个共享策略支持大量、可追踪人格的 NPC”这一游戏 AI 的核心扩展瓶颈，因此具有较强的工程与研究意义。

#### 方法概述和架构

论文提出 pcsp（Persona Conditioned Shared Policy），把“每个 NPC 只编码一次人格、之后由共享策略在每一步条件化使用”作为基本思路。具体做法是：先用冻结的 Qwen3-0.6B-Embedding 将自由文本人格描述编码成向量，再通过一个低秩人格投影层把高维语义嵌入压缩到更适合控制的低维表征。随后，单个共享 RL 策略 π(a|s, e_p) 接收环境状态和人格向量作为输入，作者采用 FiLM 或拼接方式将人格信号注入多层 MLP 策略网络与价值网络中。训练时联合使用 PPO、人格轨迹一致性约束 InfoNCE，以及 KL 多样性正则，其中 InfoNCE 用来保证“从轨迹中还能反推出人格”，而 KL 项则鼓励不同人格之间形成可分离的行为差异。推理阶段，LLM 只需对每个 NPC 计算一次人格嵌入，之后由轻量策略实时执行，从而把语言控制和帧级动作决策分离开。

#### 实验结果分析

作者在一个包含 300 个 persona 的生活模拟基准上验证了方法，指标包括零样本 persona 识别、语义-行为对齐以及推理速度。结果显示，pcsp 在组合式零样本 persona 识别上最高可达到随机水平的 17 倍，语义与行为之间的 Spearman 相关系数约为 0.73，并且相比 LLM-as-policy 基线推理速度快 22 倍。消融实验表明，InfoNCE 轨迹一致性项是关键组件：去掉后，零样本 persona 识别会直接退化到接近随机。作者还在 Melting Pot 2.4.0 的多个社会博弈场景，以及 UE5 商业引擎部署中验证了跨环境泛化与实时性；可见文本未给出所有分项实验的完整数值，但明确指出方法能够在引擎内维持低故障率并复现人格条件化效应。

<details>
<summary>完整摘要</summary>

在一个包含 300 个 persona 的生活模拟基准上，pcsp 在未见职业的组合式零样本 persona 识别上最高达到随机水平的 17 倍，语义-行为对齐的 Spearman ρ 约为 0.73，并且推理速度比 LLM-as-policy 基线快 22 倍。生活模拟游戏需要数百到数千个非玩家角色（NPC），这些角色既要表现出彼此不同且稳定的人格，又要能通过设计师编写的自然语言进行控制。现有方法在人格一致性、可控性、零样本泛化或实时推理等约束上都存在不足，例如手工行为树、逐角色强化学习、无监督技能发现，以及逐步调用 LLM 的控制方式都难以同时满足这些要求。我们提出 pcsp（Persona Conditioned Shared Policy），这是一种由冻结的 LLM 自由文本人格嵌入条件化的单一强化学习策略。pcsp 将“每个 NPC 只编码一次人格”、低秩人格投影、神经人格条件化，以及 PPO + InfoNCE 一致性 + KL 多样性 的训练目标结合在一起。在三个 pcsp-d（原 Mini-Inzoi）实验设置中，包括一个更丰富的 20 动作 v3 词汇体系，消融实验表明 InfoNCE 轨迹一致性目标是不可或缺的：去掉它后，即使任务奖励保持不变甚至有所提升，零样本 persona 识别也会坍缩到随机水平。对三个 Melting Pot 2.4.0 基底——覆盖 commons-pool、public-good 和 dyadic-matrix 社会困境（commons_harvest__open、clean_up、prisoners_dilemma_in_the_matrix__repeated）——的外部验证进一步确认，我们在第 III 节提出的方法能够在多智能体策略环境中产生 persona 条件化的行为分化；同时，一致性损失的消融会使“轨迹到 persona 的检索”在每个基底上都退化到随机，但 pairwise action-KL 仍保持不变或甚至增大。我们区分两种留出评估：组合式零样本（在训练 persona 空间覆盖范围内、未见过的职业 × 原型交叉组合，属于第 1 层和第 3 层的设定）与词汇扩展留出（新的 persona token，其嵌入位于训练嵌入的凸包内，但训练时从未出现；在这一设定下，第 2 层仍然失败，top-1 为 0，我们将其作为一个开放问题报告）。将冻结的第 1 层检查点部署到 UE5 后，在 64 个并发 agent 的实时运行中复现了引擎内人格条件化消融实验，故障率为 1.7%，而对留出的零样本人格的泛化故障率为 0.04%，说明亚帧级推理特性和消融结构在商业游戏引擎中仍然成立。这些结果表明，共享 RL 策略可以支持可扩展、实时、人格条件化的 NPC 控制，而轨迹可追踪性是该方法的核心。

</details>

---

### [[20_Research/Papers/强化学习/Understanding_Goal_Generalisation_in_Sequential_Reinforcement_Learning|Understanding Goal Generalisation in Sequential Reinforcement Learning]]

![[assets/2605.23565_figure.png|800]]

- **arXiv**: [2605.23565](https://arxiv.org/abs/2605.23565)
- **PDF**: https://arxiv.org/pdf/2605.23565
- **详细分析**: [[20_Research/Papers/强化学习/Understanding_Goal_Generalisation_in_Sequential_Reinforcement_Learning|Understanding Goal Generalisation in Sequential Reinforcement Learning]]
- **作者**: Jason Ross Brown, Edward James Young
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

强化学习智能体在训练分布之外常会表现出意料之外但仍然“有目标性”的行为，尤其是在多阶段、顺序式训练之后，这类行为更难预测。随着现实中的RL系统和前沿大模型越来越多地经过预训练、微调、RLHF或其他强化学习阶段，如何从训练历史推断其在新环境中的偏好与目标，已经成为安全性与可靠性的重要问题。本文聚焦“目标泛化”这一更基础的问题：给定一个智能体的训练流水线，能否预测它在未见环境中的行为会如何形成和迁移。

#### 方法概述和架构

作者在一个可控的迷宫导航任务中研究顺序强化学习：智能体需要在不同训练阶段依次学习追逐特定颜色和形状的目标物体。实验覆盖100多个训练流水线，并在250多个分布外环境中评估，环境中包含成对物体，观察智能体先选择哪一个。为了刻画行为，他们先把每个对象的偏好压缩为一个标量分数，并用Boltzmann-rationality描述任意两对象之间的选择概率。随后提出 latent policy gradients 方法：把智能体的“目标/偏好”看作少量潜变量，这些变量在训练中按梯度方式演化；演化方向由训练目标的高奖励信号决定，同时通过一个简单的“潜变量到行为”的映射模型来模拟最终会诱导出怎样的分布外偏好。该方法的输入是训练流水线及其阶段设置，输出是对分布外偏好函数的预测，并通过与真实评估得到的偏好分布比较来拟合。

#### 实验结果分析

作者在迷宫任务上构建了108个基础智能体，并进一步扩展到190种训练流水线、共298个智能体，在276个分布外评估环境中检验其偏好结构。结果显示，分布外偏好并非随机，而是具有一致性；更显著的特征更容易主导学习与泛化，而且早期阶段学到的目标会持续存在，并对后续阶段的新目标形成抑制或强化作用。latent policy gradients 在预测分布外行为方面表现出较强准确性，并能泛化到未见过的训练流水线类型；正文节选中未给出具体数值，因此这里只能概括其整体效果。

<details>
<summary>完整摘要</summary>

强化学习智能体在训练分布之外常会表现出非预期的目标导向行为，但我们目前仍缺乏一种原则性的理解：这类智能体将如何基于其训练历史泛化到新的环境。我们针对按顺序在一个或多个任务上训练的智能体来研究这一问题。我们考察了100多个顺序训练流水线，并在250多个分布外环境中评估其行为。我们发现，显著特征会驱动泛化，而训练早期学到的目标会持续存在，并影响后来获得的目标。为解释这些现象，我们提出了 latent policy gradients，这是一种方法，用于预测某个训练流水线可能诱发何种分布外行为。该方法依据一个简单的潜变量到行为映射模型，模拟低维潜变量在训练过程中的演化；这些潜变量的变化遵循一种原则：在训练目标上获得高回报。该方法具有较强的预测精度，能够泛化到未见过类型的训练流水线，并且具备可解释性。我们的研究表明，尽管分布外强化学习智能体的行为依赖于整个训练流水线，但这种依赖背后存在可捕捉的结构，这为从发展式视角理解目标泛化奠定了基础。

</details>

---

### [[20_Research/Papers/强化学习/ARMS_Automatic_Reward_Shaping_for_Sparse-Reward_Multi-Agent_Reinforcement_Learning|ARMS: Automatic Reward Shaping for Sparse-Reward Multi-Agent Reinforcement Learning]]

![[assets/2605.23562_figure.png|800]]

- **arXiv**: [2605.23562](https://arxiv.org/abs/2605.23562)
- **PDF**: https://arxiv.org/pdf/2605.23562
- **详细分析**: [[20_Research/Papers/强化学习/ARMS_Automatic_Reward_Shaping_for_Sparse-Reward_Multi-Agent_Reinforcement_Learning|ARMS: Automatic Reward Shaping for Sparse-Reward Multi-Agent Reinforcement Learning]]
- **作者**: Elie Abboud, Oren Gal
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

多智能体强化学习（MARL）在协同控制、路径规划、资源分配等任务中很有潜力，但稀疏奖励会让多个智能体同时学习变得极其困难：一方面信号太弱，另一方面策略联动带来明显的非平稳性，使得奖励设计更敏感。传统奖励塑形虽然能加速学习，但在多智能体场景里不能只追求短期优化，还必须尽量保持原问题的博弈结构，避免把纳什均衡“改没了”。因此，如何在稀疏奖励 MARL 中自动学习出既密集又不破坏策略结构的塑形奖励，是这篇工作最值得关注的点。

#### 方法概述和架构

论文提出 ARMS（Automatic Reward-shaping in Multi-agent Systems），这是一个面向 MARL 的自监督自动奖励塑形框架。其核心思路是：从环境给出的稀疏回报出发，通过轨迹排序学习一个更稠密的塑形奖励信号，而不是人工设计奖励。与单智能体中常见的轨迹排序理论不同，ARMS 先从博弈论角度重写策略不变性：它用“在固定对手策略下的条件最优响应”来刻画每个智能体的策略空间，并证明在满足一定条件时，排序等价的塑形奖励能保持各智能体的 best-response 集合，从而保持纳什均衡集合。训练流程上，ARMS 在策略学习与奖励学习之间交替进行：策略网络用当前塑形奖励更新，奖励网络则利用采样到的轨迹及其稀疏环境回报进行监督式排序学习；同时，塑形参数在多个智能体之间共享，以提高效率并增强一致性。

#### 实验结果分析

实验在一个部分可观测的多智能体路径规划网格世界中进行，并使用 IPPO 和 MAPPO 作为基础算法，考察了不同奖励稀疏程度和智能体数量下的表现。结果显示，ARMS 能显著提升采样效率，且随着奖励更稀疏、智能体更多，优势更加明显；同时它还能泛化到未见过的环境设置。论文还观察到一个 MARL 特有的失败模式：在探索不足时，策略—奖励的耦合会导致振荡式学习和次优循环行为；增加探索后，这一问题会得到缓解并使训练更稳定。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

稀疏奖励是多智能体强化学习（MARL）中的主要瓶颈之一，因为多个智能体同时学习会引入非平稳性，使奖励设计变得尤其棘手。奖励塑形可以加速学习，但在多智能体场景中，它必须保持问题的博弈结构，而不仅仅是改善短期优化。我们提出 ARMS（Automatic Reward-shaping in Multi-agent Systems），这是一个用于 MARL 的自监督奖励塑形框架，它通过轨迹排序从稀疏环境奖励中学习密集的塑形信号。由于单智能体中的轨迹排序保证不能直接迁移到 MARL，我们从条件最优响应的角度重新表述策略不变性，并证明在满足某些条件时，使用塑形奖励可以在固定对手策略下保持每个智能体的 best-response 集合，进而保持纳什均衡集合。基于这一视角，ARMS 在策略学习和奖励学习之间交替进行，并在多个智能体之间共享塑形参数以提高效率。我们在一个部分可观测的多智能体路径规划领域中的实验表明，ARMS 在奖励越来越稀疏、智能体数量不断增加时能够提升采样效率，并能泛化到未见过的环境；同时还揭示了一个 MARL 特有的失败模式：有限探索与耦合的策略—奖励动态会诱发振荡行为。增加探索可以缓解这一现象并稳定学习。据我们所知，ARMS 是首个由博弈论中的均衡保持结果所驱动设计的、用于 MARL 的自动奖励塑形框架。

</details>

---

### [[20_Research/Papers/具身智能/PathNavigate_A_Training-Free_Pathology_Agent_with_Surprise-Guided_Scan_and_Shared_Slide_Memory_for_Whole-Slide_Image_VQA|PathNavigate: A Training-Free Pathology Agent with Surprise-Guided Scan and Shared Slide Memory for Whole-Slide Image VQA]]

![[assets/2605.23559_figure.png|800]]

- **arXiv**: [2605.23559](https://arxiv.org/abs/2605.23559)
- **PDF**: https://arxiv.org/pdf/2605.23559
- **详细分析**: [[20_Research/Papers/具身智能/PathNavigate_A_Training-Free_Pathology_Agent_with_Surprise-Guided_Scan_and_Shared_Slide_Memory_for_Whole-Slide_Image_VQA|PathNavigate: A Training-Free Pathology Agent with Surprise-Guided Scan and Shared Slide Memory for Whole-Slide Image VQA]]
- **作者**: Chunze Yang, Qidong Liu, Wenjie Zhao, Yue Tang, Jiusong Ge, Di Zhang, Jiashuai Liu, Lei Wu, Junbo Lu, Ni Zhang, Xian Wu, Zeyu Gao...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

全切片病理图像问答（WSI-VQA）要求系统在亿像素级切片中，依据临床自然语言问题快速定位稀疏但关键的高分辨率证据，本质上是一个极端上下文下的视觉搜索问题。现有方法大致分为两类：一类是监督式病理多模态大模型或智能体，虽然能把定位与推理学进模型，但往往依赖任务专用标注和重新训练，部署灵活性有限；另一类是训练无关的病理智能体，虽然无需重训，但常采用“先问后搜”的候选生成方式，容易错过问题中未明确提及、却对诊断至关重要的形态学线索。本文值得关注之处在于，它试图在不训练核心模型的前提下，引入更符合病理医生习惯的“先扫描、再检索、后读出”流程，以提升证据定位的完整性与推理效率。

#### 方法概述和架构

作者提出 PathNavigate，一个训练无关的病理智能体，整体流程由扫描（scan）、搜索（search）和读出（readout）三阶段组成。首先，系统在低倍切片上运行 Shared Online Memory，用冻结的病理特征构建每张切片自己的在线状态，并通过重建误差的梯度范数定义“惊奇度（surprise）”，从而得到一张切片级的异常区域分布图。接着，Surprise-Guided Scan 先依据惊奇度筛出候选 ROI 池，再在该池内结合问题条件下的 PLIP 相关性进行高倍目标重排，避免问题先验直接覆盖掉切片本身的异常结构。最后，Evidence Readout and QA 从高倍区域提取局部证据，并把同一个在线记忆作为切片级上下文输入给冻结的判别/回答模块，完成最终答案生成。整体上，该方法不更新主干视觉语言模型，只在测试时通过小型在线记忆和检索路由来完成证据导航与答案聚合。

#### 实验结果分析

作者在 WSI-VQA 和 SlideBench-BCNB 上进行了实验，与现有监督式与训练无关基线进行了比较；从摘要和正文节选可知，该方法在答案准确率、证据选择可解释性以及系统效率方面都有提升。论文还通过核心组件消融与系统级效率分析验证了“先扫描、再搜索、后读出”的设计确有收益。可见文本未给出具体数值，但结果表明，惊奇度驱动的候选生成比单纯依赖问题相关性更稳健，且能减少推理时的额外脚手架与开销。

<details>
<summary>完整摘要</summary>

全切片图像视觉问答（WSI-VQA）将病理学表述为一个极端上下文搜索问题：要回答一个开放形式的临床问题，系统必须首先在严格的检查预算下穿行于一张亿像素级切片，定位稀疏的高分辨率证据。现有方法大致分为两类：i）监督式病理多模态大语言模型（MLLM）和智能体可以把定位与推理吸收到学习模块中，但它们通常将导航与任务专用监督和重训练耦合在一起，限制了实用性；ii）训练无关的病理智能体通过保持核心模型冻结来避免这类成本，但通常采用“先问题后搜索”的设计，即主要根据与问题相关的程度构建初始候选集。这可能会遗漏问题中未被命名、但决定答案的关键形态学特征，并迫使系统在推理阶段引入更重的脚手架。为解决这一挑战，我们提出 PathNavigate，这是一种围绕“扫描-搜索-读出”流程构建的训练无关病理智能体。在与问题匹配之前，PathNavigate 先利用一个共享的在线记忆模块，对冻结的病理特征在当前切片的低倍视图上进行扫描，生成一个切片特定的“惊奇场”，从而标记出异常区域池。随后，它只在该区域池内施加问题条件下的 PLIP 相关性，选择高倍搜索目标。最后，它提取局部高倍证据，并使用冻结的 perceptor-adjudicator 结构完成回答，同时复用同一个在线记忆作为切片级上下文。在 WSI-VQA 和 SlideBench-BCNB 上的实验表明，所提出的扫描-搜索-读出设计提升了答案准确率，并以更高效率生成了更可解释的证据选择轨迹。代码已在线公开。

</details>

---

### [[20_Research/Papers/强化学习/Goal-Conditioned_Agents_that_Learn_Everything_All_at_Once|Goal-Conditioned Agents that Learn Everything All at Once]]

![[assets/2605.23551_figure.png|800]]

- **arXiv**: [2605.23551](https://arxiv.org/abs/2605.23551)
- **PDF**: https://arxiv.org/pdf/2605.23551
- **详细分析**: [[20_Research/Papers/强化学习/Goal-Conditioned_Agents_that_Learn_Everything_All_at_Once|Goal-Conditioned Agents that Learn Everything All at Once]]
- **作者**: Michael Matthews, Matthew Jackson, Michael Beukman, Thomas Foster, Alistair Letcher, Scott Fujimoto, Cédric Colas, Jakob Foerster
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

目标条件强化学习（GCRL）希望智能体能够根据不同目标执行可切换、可泛化的策略，适合导航、机器人控制和复杂游戏环境中的多任务学习。但在一条轨迹中，绝大多数观测信息都会在只针对当前命令目标做 on-policy 更新时被浪费掉。虽然“all-goals learning”可以让每个转移同时服务于所有目标、最大化数据复用，但朴素的目标重标记会随着目标数线性膨胀，计算成本过高，难以扩展到大目标集。本文因此关注如何在不牺牲效率的前提下，把“每一步都对所有目标学习”的想法真正做大规模化。

#### 方法概述和架构

论文提出 Learning Everything all at Once（LEO），核心思路是把原本“输入状态和目标、输出单个目标下动作价值/策略”的网络，改写成“输入状态、一次性输出所有目标对应的结果”的网络。对于离散动作的 Q 学习，模型不再对每个目标单独重标记并前向计算，而是直接输出形状为“目标数 × 动作数”的 Q 值张量，从而用一次前向传播完成全目标并行更新。这样训练时只需要普通的转移三元组（s, a, s'），即可在所有目标上同时计算损失；推理时则通过索引命令目标对应的输出选择动作。作者进一步指出，LEO 在某些任务上可能因 late fusion 带来表示瓶颈，于是提出 Dual LEO：同时训练一个 LEO 网络和一个常规 goal-conditioned（UVFA 风格）学生网络，并让 LEO 作为教师，通过策略/价值蒸馏或价值插值向学生提供更精细的指导。论文还将该思路扩展到连续控制场景，以验证其通用性。

#### 实验结果分析

实验主要在目标条件 CraftaxGC 基准和若干连续控制环境上进行，并与常规 goal-conditioned 方法、HER 以及其他基线比较。结果显示，LEO 在 CraftaxGC 上显著优于其他方法，在连续控制任务上也能与现有基线竞争。计算效率方面，作者报告相较于朴素的 all-goals relabelling，LEO 的吞吐提升超过 250 倍，同时在 CraftaxGC 上相对常规单目标学习仅带来约 34% 的速度损失。进一步实验表明，将 LEO 作为教师的 Dual LEO 往往比单独使用 LEO 或单独使用 goal-conditioned 网络表现更好；可见文本未给出更细的具体数值。

<details>
<summary>完整摘要</summary>

一个目标条件强化学习智能体在环境中探索时，会在整条轨迹中看到大量信息；但如果只针对被命令的目标进行 on-policy 更新，其中大部分信息都会被丢弃。all-goals learning 的做法是：把每一个转移都拿来针对每一个目标做 off-policy 学习，从而让智能体尽可能提取信息。不过，采用朴素重标记时，这种方法通常在计算上不可行。本文提出一种解决办法：让网络一次性联合输出针对所有目标的价值和动作，从而在单次前向传播中高效、并行地完成全目标更新。我们将这一过程称为 Learning Everything all at Once（LEO）。实验表明，LEO 在目标条件 Craftax 上显著优于其他方法，在连续控制环境中也能与现有基线相媲美，同时相较于 all-goals relabelling 实现了超过 250 倍的加速。我们还进一步证明，当把 LEO 作为教师网络而不是直接 actor 使用时，它还能变得更强。我们希望，借助在大规模上解锁 all-goals learning，LEO 能成为复杂环境下强化学习实践者的有用工具。我们的代码已开源。

</details>

---

### [[20_Research/Papers/强化学习/Precise_SDE-Consistent_Stochastic_Sampling_for_RL_Post-Training_of_Flow-Matching_Models|Precise: SDE-Consistent Stochastic Sampling for RL Post-Training of Flow-Matching Models]]

![[assets/2605.23522_figure.png|800]]

- **arXiv**: [2605.23522](https://arxiv.org/abs/2605.23522)
- **PDF**: https://arxiv.org/pdf/2605.23522
- **详细分析**: [[20_Research/Papers/强化学习/Precise_SDE-Consistent_Stochastic_Sampling_for_RL_Post-Training_of_Flow-Matching_Models|Precise: SDE-Consistent Stochastic Sampling for RL Post-Training of Flow-Matching Models]]
- **作者**: Jade Zou, Tao Huang, Weijie Kong, Junzhe Li, Yue Wu, Qi Tian, Jiangfeng Xiong, Jianwei Zhang, Liefeng Bo, Zhao Zhong
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

在扩散模型和flow-matching生成器中，强化学习后训练已成为提升提示词对齐和感知质量的重要手段，尤其适用于图像生成等视觉任务。对于在线RL而言，原本确定性的采样轨迹必须改写为随机策略，通常需要把反向时间ODE替换为SDE；此时采样器不再只是推理细节，而是策略本身的一部分，会直接影响探索强度、去噪稳定性和奖励优化效果。现有方法在低步数采样场景下往往面临两难：噪声加得不够，探索不足、优化缓慢；噪声加得过多，又会导致轨迹不稳定，甚至偏离真实数据分布。因此，这篇工作值得关注，因为它把“随机采样器设计”提升为RL后训练中的关键问题，并针对探索与离散化一致性给出系统分析与新解法。

#### 方法概述和架构

论文提出 Precise，一种面向flow-matching模型RL后训练的SDE一致随机采样器。作者将采样器设计拆成两个耦合部分：一是噪声注入日程，用于平衡探索与稳定性；二是少步数下的离散化转移规则，用于忠实近似目标逆向SDE。针对前者，方法基于logSNR分析推导出随时间变化的探索强度，让噪声在模型更容易回到数据流形的位置更强、在容易破坏轨迹稳定的位置更弱。针对后者，Precise不再冻结速度或score，而是冻结“干净潜变量的后验均值”并据此推导闭式转移，从而保持去噪轨迹的SDE一致性，避免标准Euler类采样器带来的额外离散噪声。整体流程是：输入当前噪声状态后，模型预测去噪方向与后验统计量，采样器按Precise规则完成一步逆向更新，再在RL训练中把该随机轨迹作为策略 rollout 进行奖励优化。

#### 实验结果分析

作者在 Stable Diffusion 3.5 Medium 和 FLUX.2 Klein 4B Base 上评估了 Precise，并与先前用于Flow-GRPO、Dance-GRPO等RL后训练流程的随机采样器进行比较。结果显示，Precise 在PickScore、HPSv2.1等对齐指标上达到新的最优水平，同时为了达到前人方法在域内表现的最佳值，所需墙钟训练时间减少了13.1%到53.2%。消融实验还表明，探索日程和新的冻结后验均值近似都对性能有明显贡献，且该方法对超参数和NFE变化较为鲁棒。可见文本未给出更多具体数值，但整体结论明确指向：Precise在低步数、在线RL的高成本场景下更稳定、更高效。

<details>
<summary>完整摘要</summary>

强化学习（RL）已成为提升扩散和flow-matching生成器中提示词对齐与感知质量的有效方法。将在线RL应用于flow matching的关键步骤，是把确定性的采样轨迹转变为随机策略，通常做法是用随机微分方程（SDE）替代反向时间常微分方程（ODE）。控制探索行为和去噪动力学的随机采样器因此成为策略的一部分，其设计会显著影响奖励优化性能。我们将采样器设计拆解为两个相互依赖的部分：选择合适的随机探索强度，以及在RL所使用的小步数条件下，对由此产生的SDE进行忠实离散化。针对第一部分，我们分析了去噪过程中探索与稳定性之间的内在张力，并推导出一个兼顾二者的SDE日程。针对离散化挑战，我们通过一个玩具例子说明，现有采样器可能偏离flow-matching过程，要么引入过多离散化噪声，要么依赖无法保证收敛到数据分布的启发式规则。为解决这些问题，我们提出 Precise，这是一种兼顾有效探索与稳定性的新随机采样器。关键地，Precise 通过一种新的近似方式保持去噪轨迹的SDE一致性：冻结干净潜变量的后验均值，从而解决标准采样器中的过量噪声问题。大量实验表明，这一形式能够带来更快、更稳定的RL奖励优化，在获得更优对齐分数（例如PickScore、HPSv2.1）的同时，相比先前采样器达到最佳域内性能所需的墙钟训练时间减少了13.1%–53.2%。

</details>

---

### [[20_Research/Papers/大模型/CoSPlay_Cooperative_Self-Play_at_Test-Time_with_Self-Generated_Code_and_Unit_Test|CoSPlay: Cooperative Self-Play at Test-Time with Self-Generated Code and Unit Test]]

![[assets/2605.23491_first_page.png|800]]

- **arXiv**: [2605.23491](https://arxiv.org/abs/2605.23491)
- **PDF**: https://arxiv.org/pdf/2605.23491
- **详细分析**: [[20_Research/Papers/大模型/CoSPlay_Cooperative_Self-Play_at_Test-Time_with_Self-Generated_Code_and_Unit_Test|CoSPlay: Cooperative Self-Play at Test-Time with Self-Generated Code and Unit Test]]
- **作者**: Zhangyi Hu, Chenhui Liu, Tian Huang, Jindong Li, Yang Yang, Jiemin Wu, Zining Zhong, Menglin Yang, Yutao Yue
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.77（加权：大模型 0.25，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

近年来，基于可验证奖励的强化学习（RLVR）和测试时扩展（TTS）显著提升了大模型代码生成能力，但这类方法往往依赖昂贵的真实单元测试（GT UTs）。一旦缺少 GT UTs，现有 TTS 方法的效果就会明显下降，而直接使用模型自行生成的单元测试又容易带噪声，甚至与错误代码错误耦合。本文关注的核心问题是：在没有真实标注测试的情况下，如何同时提升候选代码与单元测试本身的质量，从而实现更可靠的测试时代码生成。

#### 方法概述和架构

论文提出 CoSPlay（Cooperative Self-Play at Test-Time），这是一个无需 GT、无需训练的测试时框架，通过“代码-单元测试”协同自博弈来共同优化二者。首先，系统会探索多样化的解题思路，并分析潜在失败模式，从而生成更具区分性的单元测试想法。随后，利用代码-单元测试执行矩阵中的双向通过计数信号，迭代地剪枝或修复弱代码，同时刷新或替换不可靠的单元测试，使两个候选池相互促进、共同进化。最后，当多个代码在最高通过数上打平时，框架不再仅依赖测试通过率，而是从输出一致性最大的簇中选择最终代码，因为正确代码通常会在相同输入上给出一致输出，而错误代码更容易分歧。

#### 实验结果分析

作者在四个具有挑战性的基准上评估了 CoSPlay。以 Qwen2.5-7B-Instruct 为底座时，CoSPlay 将平均 BoN 从 22.1% 提升到 33.2%，并将单元测试准确率从 14.6% 提升到 78.3%，效果达到或超过了 RLVR 模型 CURE-7B。将该方法进一步应用到 CURE-7B 上，还能额外带来 5.7% 的 BoN 提升。实验同时表明，CoSPlay 可迁移到不同 backbone，并在相近 token 预算下优于现有 GT-free TTS 基线，且随着预算增大仍持续收益。

<details>
<summary>完整摘要</summary>

近年来，带有可验证奖励的强化学习（RLVR）和测试时扩展（TTS）通过可执行验证推动了大模型代码生成的发展。然而，真实单元测试（GT UTs）仍然是一个瓶颈：当前最先进的 RLVR 方法在训练时需要它们，而现有的 TTS 方法如果没有它们就会失去竞争力。这促使我们思考一种不依赖 GT 的测试时扩展（GT-free TTS）：现有方法直接使用自生成单元测试来细化和筛选代码候选。然而，这些单元测试往往噪声较大，或者会与错误代码产生虚假耦合；与此同时，没有可靠代码，又无法验证单元测试本身的质量。因此，关键挑战在于如何同时改进二者。为此，我们提出 CoSPlay，这是一种无需 GT、无需训练的框架，通过协同自博弈共同提升代码与单元测试。它首先探索多样化的解题思路，并识别潜在的失败模式，以生成更具区分性的单元测试思路。随后，它利用来自代码-单元测试执行矩阵的双向通过计数信号，迭代地剪枝或修复弱代码，并刷新或替换不可靠的单元测试，使两个候选池共同进化。最后，当多个代码在最高通过计数上并列时，它从最大的输出一致性簇中选择最终代码，因为正确代码在相同输入上应当一致，而错误代码往往会发散。在四个具有挑战性的基准上的实验表明，CoSPlay 在 Qwen2.5-7B-Instruct 上将平均 BoN 从 22.1% 提升到 33.2%，并将单元测试准确率从 14.6% 提升到 78.3%，达到或超过了 RLVR 模型 CURE-7B。将其应用到 CURE-7B 上，还能进一步提升 5.7% 的 BoN。CoSPlay 也可泛化到多种不同骨干模型，并在可比的 token 预算下优于 GT-free TTS 基线，在预算继续增大时仍能带来持续收益。这些结果表明，CoSPlay 为在没有任何 GT 数据的情况下实现有竞争力的代码生成提供了一种可扩展的推理策略。

</details>

---

### [[20_Research/Papers/世界模型/Learning_Individual_Dynamics_from_Sparse_Cross-Sectional_Snapshots|Learning Individual Dynamics from Sparse Cross-Sectional Snapshots]]

![[assets/2605.23470_first_page.png|800]]

- **arXiv**: [2605.23470](https://arxiv.org/abs/2605.23470)
- **PDF**: https://arxiv.org/pdf/2605.23470
- **详细分析**: [[20_Research/Papers/世界模型/Learning_Individual_Dynamics_from_Sparse_Cross-Sectional_Snapshots|Learning Individual Dynamics from Sparse Cross-Sectional Snapshots]]
- **作者**: Christian Lagemann, Kai Lagemann, Steven L. Brunton, Sach Mukherjee
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.52（加权：强化学习 0.16，世界模型 0.36）
- **关联关键词**: WorldModel, Systems

#### 研究背景与动机

很多真实世界问题都依赖个体级动态预测，例如个体衰老、疾病进展、疫情传播或工程系统退化，但这类任务通常需要同一对象的密集纵向追踪数据。现实中更常见的是极端稀疏甚至完全横截面的快照数据，每个个体可能只有1到3个时间点观测，这使得恢复连续时间的个体轨迹成为一个病态逆问题。现有方法要么依赖密集序列、难以适用于稀疏场景，要么只建模总体分布迁移而丢失个体动力学，因此这篇工作试图打破“序列模型”和“横截面方法”之间的二分法，具有较强的方法论价值。

#### 方法概述和架构

论文提出 CADENCE（Contextual Archetypes and Diffusion ENCodings for Dynamics Estimation），其核心思想是把稀疏快照与个体静态上下文结合起来，以恢复连续个体轨迹。方法分为两阶段：第一阶段使用基于 score 的双射 PF-ODE 编码器，将高维观测映射到潜空间，并通过概率流的可逆结构消除空间上的非唯一性；第二阶段用 Soft Mixture-of-Experts（SMoE）路由器根据个体上下文生成动态参数混合权重，再由这些权重去条件化神经 ODE 的向量场。输入包括单次观测、观测时间和静态上下文，输出是个体在未来时刻的连续轨迹预测；训练时仅使用极稀疏的横截面快照及其上下文结构。作者还给出一套可识别性理论：在若干结构假设下，个体动力学参数与路由函数可以联合可识别，并据此推导出与架构对应的最小实现形式。

#### 实验结果分析

论文在覆盖物理系统、流行病学、生态学以及真实生物数据的一系列基准上验证 CADENCE，节选中未给出具体数值，但结论是该方法在仅用极稀疏快照训练的情况下，性能可匹配甚至超过使用密集完整轨迹训练的 SOTA 序列模型。实验还包括轨迹恢复、子群路由、高维与真实世界随机动力学等任务，并报告了消融实验，用于验证 PF-ODE 编码器、SMoE 路由和解耦训练策略各自的作用。作者进一步强调，该框架在计算上也更高效，训练复杂度可从空间与时间双重迭代的乘积形式降低到仅随时间迭代增长。

<details>
<summary>完整摘要</summary>

预测一个动力单元如何随时间演化——例如个体如何衰老、疫情如何传播，或物理系统如何退化——通常需要密集的纵向跟踪。当只有极其稀疏、甚至完全横截面的数据可用时，推断个体化、连续时间的轨迹在根本上是病态的。现有方法迫使我们在严格的二选一之间做出妥协：序列模型（如 latent ODE）需要密集的纵向数据，而横截面方法（如最优传输、基于 flow matching 的方法）只能映射总体分布，从而丢失个体动力学。本文表明，这一二分法可以被打破。我们提出 CADENCE，一个原则性的概率框架，通过将潜在动力学锚定到静态的个体级上下文中，从孤立快照中恢复连续的个体轨迹。我们给出了针对单时间点轨迹推断的新可识别性保证。通过结合基于 score 的空间编码器（可逆的 Probability Flow ODE）以消除微分同胚歧义，以及 Soft Mixture-of-Experts（SMoE）路由器，我们证明了个体动力学参数与路由函数可以联合可识别。在一组覆盖物理系统到真实生物数据的基准实验中，CADENCE 仅在带有上下文结构的极稀疏快照上训练，却能达到或超过在密集、完整轨迹数据上训练的最新序列模型的性能。

</details>

---

### [[20_Research/Papers/强化学习/Reflex_Reinforcement_Learning_with_Reflection_Symmetry_Exploitation_in_State-Based_Continuous_Control|Reflex: Reinforcement Learning with Reflection Symmetry Exploitation in State-Based Continuous Control]]

![[assets/2605.23415_figure.png|800]]

- **arXiv**: [2605.23415](https://arxiv.org/abs/2605.23415)
- **PDF**: https://arxiv.org/pdf/2605.23415
- **详细分析**: [[20_Research/Papers/强化学习/Reflex_Reinforcement_Learning_with_Reflection_Symmetry_Exploitation_in_State-Based_Continuous_Control|Reflex: Reinforcement Learning with Reflection Symmetry Exploitation in State-Based Continuous Control]]
- **作者**: Shuai Zhen, Yifan Zhang, Yuling Wang, Yanhua Yu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

强化学习在连续控制任务中表现出色，但往往需要大量环境交互，样本效率仍然是核心瓶颈。现有利用对称性的研究大多集中在基于图像的RL以及旋转对称（如SO(2)），而对状态向量输入的连续控制任务、尤其是反射对称的利用还比较少。本文关注行走、机械控制等常见的左右对称场景，希望用更符合物理规律的方式把“镜像状态”纳入学习过程，从而减少采样成本并提升最终策略质量，因此具有较强的实用意义。

#### 方法概述和架构

论文提出 Reflex，一个面向状态空间连续控制的反射对称增强学习范式，可同时接入 on-policy 与 off-policy 算法。作者将反射分为两类：轴向反射和双侧反射，并为状态、动作中的不同物理量设计了对应的变换规则，例如欧式向量、伪向量、角度变量和不变标量分别采用不同映射。基于G-invariant MDP的形式化，论文证明了在反射对称环境中最优价值函数与最优策略应满足对称性，并据此构造对称一致性正则项。具体实现上，Reflex分别与PPO和SAC结合：训练时利用原始样本及其镜像样本进行约束，使策略在原状态与反射状态下输出一致或对应的动作分布；推理阶段仍使用标准策略网络，不额外增加复杂推断流程。

#### 实验结果分析

作者在OpenAI Gym和DeepMind Control的一系列连续控制任务上评估了Reflex，并与标准PPO、SAC等基线比较。实验显示，Reflex在多个环境中都优于基础方法，同时提高了样本效率；正文还提到做了消融实验、不同设置下的对比，以及将方法迁移到TD3上的可用性验证。可见文本未给出具体数值，但整体结论是：反射对称正则不仅能加快学习，还能提升最终回报，并且对 on-policy/off-policy 均有效。

<details>
<summary>完整摘要</summary>

强化学习长期以来都面临样本效率较差的问题。缓解这一问题的一种有前景的途径，是利用群不变马尔可夫决策过程（G-invariant MDP）。现有相关工作主要集中在基于图像的RL以及如SO(2)这样的旋转对称性，而对基于状态的RL和反射对称性的探索相对不足。本文聚焦于基于状态的连续控制任务，通过引入 Reflex 来利用反射对称性；Reflex 是一种可无缝整合到 on-policy 和 off-policy RL 算法中的范式。我们形式化了两类反射——轴向反射和双侧反射，并刻画了它们各自的变换。基于对保持对称性的最优价值函数与策略的理论分析，Reflex 通过有原则的对称正则机制，将反射对称性融入策略学习。我们将 Reflex 与 PPO 和 SAC 结合，并在一系列 OpenAI Gym 和 DeepMind Control 基准上进行评估，结果表明其性能优于标准基线，同时提升了样本效率。代码已开源于 https://github.com/TonyStark042/Reflex 。

</details>

---

### [[20_Research/Papers/大模型/When_Planning_Fails_Despite_Correct_Execution_On_Epistemic_Calibration_for_LLM-Based_Multi-Agent_Systems|When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems]]

![[assets/2605.23414_figure.png|800]]

- **arXiv**: [2605.23414](https://arxiv.org/abs/2605.23414)
- **PDF**: https://arxiv.org/pdf/2605.23414
- **详细分析**: [[20_Research/Papers/大模型/When_Planning_Fails_Despite_Correct_Execution_On_Epistemic_Calibration_for_LLM-Based_Multi-Agent_Systems|When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems]]
- **作者**: Zehao Wang, Shilong Jin, Zhao Cao, Lanjun Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

基于大模型的多智能体系统已被广泛用于复杂推理、工具调用和长程任务执行，但实际部署中依然容易失败。本文指出一种不同于“执行出错”的隐蔽失效：即使每一步动作都正确执行，系统仍可能因为在规划阶段错误判断“当前计划是否可行”而无法完成任务。这类问题在信息不断更新的过程中还会动态变化，早先的误判可能被新信息掩盖，随后又反复出现，因此值得专门研究。

#### 方法概述和架构

本文提出 Epistemic Planning Calibration Agentic Workflow（EPC-AW），目标不是直接验证某个计划是否可行，而是判断该计划在不同信息条件下是否仍然得到支持。EPC-AW 包含两个核心模块：Information-consistency-based Plan Selection（IPS）和 Consistency-guided Epistemic State Refinement（CESR）。IPS 在每一轮规划时，让多个具有不同信息视角的智能体对候选计划进行评估，优先选择那些跨智能体评估更稳定、对信息扰动不敏感的计划，从而把“信息一致性”作为规划阶段的校准信号。CESR 则跨轮次工作，它记录规划智能体本轮本地选择与 IPS 选中计划之间的差异，将这些差异视为先前的认知失配证据，并写入持久记忆以约束后续规划。整个流程在规划、执行、诊断与记忆更新之间形成闭环：规划器生成候选计划，执行器完成动作并获得新证据，诊断器利用跨智能体一致性评估与历史差异来修正后续的认知状态，直到满足停止条件后输出最终答案。

#### 实验结果分析

作者在六个 LLM-based multi-agent 基准上进行了实验，并与多种失败修复/规划重试/状态回滚类基线比较，评价重点是 system-level success。结果显示，EPC-AW 的平均系统成功率提升了 9.75%，说明它不仅能缓解执行层错误，更能针对规划阶段的认知失配带来稳定收益。论文还报告了消融实验、跨模型骨干泛化以及时间和 token 开销分析；从节选可见，具体数值未完全展开，但整体结论是 IPS 与 CESR 均对性能提升有贡献。

<details>
<summary>完整摘要</summary>

基于大模型的多智能体系统即使在规划动作被正确执行时也可能失败，因为智能体在评估计划可行性时可能会误判自身知识，这一现象我们称为规划中的认知失配。与执行错误不同，认知失配在规划阶段是隐蔽的，因为生成的计划可能保持自洽且可执行，却没有任何可观察到的错误；这种失配也具有动态性，因为新的信息会改变可行性判断，进而可能掩盖过去的失配信号，并导致其随时间再次出现。为解决这一问题，我们提出 Epistemic Planning Calibration Agentic Workflow（EPC-AW），它不直接验证计划是否可行，而是评估计划在不同信息条件下是否仍然受到支持。EPC-AW 采用基于信息一致性的计划选择策略，挑选那些在不同智能体之间评估结果稳定的计划；同时引入一致性引导的认知状态细化机制，利用过去的差异指导未来规划，从而随时间自适应地进行校准。实验表明，EPC-AW 能将系统级成功率平均提升 9.75%。代码已在公开仓库中提供（https://github.com/wzhSteve/EPC-AW）。

</details>

---

### [[20_Research/Papers/大模型/Metacognition_as_Reward_Reinforcing_LLM_Reasoning_via_Knowledge_and_Regulation_Signals|Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals]]

![[assets/2605.23384_first_page.png|800]]

- **arXiv**: [2605.23384](https://arxiv.org/abs/2605.23384)
- **PDF**: https://arxiv.org/pdf/2605.23384
- **详细分析**: [[20_Research/Papers/大模型/Metacognition_as_Reward_Reinforcing_LLM_Reasoning_via_Knowledge_and_Regulation_Signals|Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals]]
- **作者**: Sirui Chen, Lei Xu, Yuying Zhao, Yutian Chen, Yu Wang, Beier Zhu, Hanwang Zhang, Shengjie Zhao, Chaochao Lu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: LLM, RL

#### 研究背景与动机

近年来，基于强化学习的训练方法显著提升了大模型的推理能力，但现有奖励设计仍主要依赖两类思路：一类是基于可验证结果的奖励，能够通过可执行检查或标准答案给出最终结果信号，但对中间推理过程的指导较弱；另一类是将自然语言规则作为奖励，能够评价推理质量与任务遵循性，却往往需要针对每个样本单独设计规则，人工成本较高。对于需要稳定提升复杂推理质量的 LLM 而言，如何同时覆盖结果与过程、且不依赖繁琐的实例级奖励设计，是一个值得关注的问题。

#### 方法概述和架构

论文提出 Metacognition-as-Reward（MaR）框架，用“元认知”思想来构造强化学习奖励信号，将推理过程拆解为两个通用维度：元认知知识和元认知调节。前者用于识别与任务相关的关键信息，强调模型是否覆盖了应关注的知识点；后者用于规划和调整推理过程，强调模型是否以合理方式组织、修正与推进推理。方法上，MaR 会把模型生成的 rollout 显式组织成这些元认知组件，并在轨迹级别同时计算任务知识覆盖、调节忠实度以及最终答案正确性等奖励。训练时，模型不是只对最终答案进行优化，而是对整条推理轨迹施加奖励，从而把反馈延伸到中间推理步骤。

#### 实验结果分析

作者在 22 个基准上进行了实验，结果表明 MaR 能稳定提升模型表现，较基础模型最高提升 7.7%，较原始 DAPO 最高提升 11.0%。在更强模型对比中，Qwen3.5-9B + MaR 在总体平均表现上超过了 GPT-OSS-120B，并在若干单项基准上优于更强模型。过程级分析显示，MaR 还能明显改善推理过程质量；此外，在域外数据集上，MaR 训练后的模型平均也优于对应基础模型。

<details>
<summary>完整摘要</summary>

近期的强化学习方法已显著提升了大模型的推理能力。现有奖励设计主要遵循两种范式：（1）基于可验证奖励的强化学习（RLVR），通过可执行检查或标准答案来获得结果信号，但对中间推理行为的指导有限；（2）将评估细则作为奖励（RaR），通过自然语言规则来评估推理质量和任务遵循性，超越了仅检查最终答案的方式，但通常需要针对具体样本设计专门规则，并付出大量设计成本。为解决这些问题，我们提出 Metacognition-as-Reward（MaR），这是一种受元认知启发的强化学习框架，通过两个通用的过程维度来引导大模型推理：i）元认知知识，用于识别与任务相关的信息，而无需手工设计实例级规则；ii）元认知调节，用于规划和调整推理过程，从而提供超越最终答案结果的奖励引导。MaR 将模型 rollout 组织为显式的元认知组件，并在任务知识覆盖、调节忠实度以及最终答案正确性上进行轨迹级奖励优化。借助这种方式，MaR 将奖励反馈扩展到推理轨迹，同时又将奖励信号锚定在通用的元认知维度上。对 22 个基准的实验表明，MaR 能持续提升模型性能，较基础模型最高提升 7.7%，较原始 DAPO 最高提升 11.0%。值得注意的是，Qwen3.5-9B + MaR 在总体平均表现上缩小了与前沿模型的差距，不仅在总体平均上超过了 GPT-OSS-120B，还在若干单项基准上优于更强的模型。进一步的过程级分析表明，其推理过程质量也得到了显著提升。MaR 还具备域外泛化能力，在域外数据集上，经过 MaR 训练的模型平均也优于对应的基础模型。

</details>

---

### [[20_Research/Papers/具身智能/Curriculum_reinforcement_learning_with_measurable_task_representation_learning|Curriculum reinforcement learning with measurable task representation learning]]

![[assets/2605.23372_first_page.png|800]]

- **arXiv**: [2605.23372](https://arxiv.org/abs/2605.23372)
- **PDF**: https://arxiv.org/pdf/2605.23372
- **详细分析**: [[20_Research/Papers/具身智能/Curriculum_reinforcement_learning_with_measurable_task_representation_learning|Curriculum reinforcement learning with measurable task representation learning]]
- **作者**: Yongyan Wen, Siyuan Li, Mingjian Fu, Yiqin Yang, Xun Wang, Peng Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

课程强化学习（Curriculum Reinforcement Learning, CRL）旨在让智能体通过一系列由易到难的任务逐步积累知识，最终解决更具挑战性的目标任务，在导航、机器人控制等场景中具有重要价值。现有CRL研究一类侧重于任务排序，另一类尝试自动生成课程，其中基于插值的方法通常依赖任务空间中可度量的相似性，并假设任务之间可以用“距离”连续连接。本文指出，在复杂导航等任务中，原始任务空间往往具有非欧氏特性，直接插值会破坏这种假设，因此值得研究一种能够学习“可测量任务表示”的自动课程生成方法。

#### 方法概述和架构

论文提出了一种基于可测量任务表示学习的自动课程生成方法，核心思路是先把难以直接度量的任务空间映射到潜在空间，再在潜在空间中构造课程。具体地，作者使用变分自编码器（VAE）结构编码任务中的奖励信息和状态转移信息，使得每个任务被表示为一个潜变量嵌入。该表示被设计为满足任务相似性可测量：在潜在空间中距离较近的两个嵌入，应对应奖励模式和状态转移都更相似的任务。基于学到的任务表示，方法进一步生成逐步更接近目标任务的新任务，从而形成自动课程；训练时先学习任务表示，再据此在潜在空间中推进课程生成，推理时则按生成的中间任务序列逐步训练智能体。

#### 实验结果分析

作者在多种具有挑战性的导航任务上评估了该方法，并将其与基于插值和基于GAN的自动课程强化学习方法进行对比。实验结果表明，该方法整体上优于现有SOTA的插值式CRL和生成对抗网络式CRL基线。正文节选中未给出具体数值、数据集名称或消融结果，因此只能确认其在复杂导航场景中表现更强，具体提升幅度可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

在课程强化学习（Curriculum Reinforcement Learning, CRL）中，智能体会沿着一系列任务（即课程）逐步积累知识，而学习过程的目标是利用这些积累的知识最终解决一个具有挑战性的目标任务。早期的CRL工作主要关注候选任务的排序，而近期研究开始探索自动生成课程。在丰富的CRL文献中，基于插值的CRL范式是重要组成部分之一，它通常通过在任务空间中、借助有意义的距离度量（即能够衡量任务相似性）在初始任务分布与目标任务分布之间进行插值，从而自动生成中间任务。然而，在具有挑战性的导航任务中，非欧氏的上下文（任务）空间会使这一假设失效。为了在复杂任务中实现自动课程生成，我们提出了一种基于可测量任务表示学习的新型自动课程生成方法。为了更好地衡量相似性，我们提出将任务空间转换到潜在空间。通过一种编码奖励和状态转移的变分自编码器结构，我们获得了具有任务相似性度量属性的潜在任务表示，即两个接近的任务嵌入在奖励和状态转移意义上对应两个相似的任务。基于所学习到的任务表示，我们进一步开发了一种自动课程生成方案，能够有效生成越来越接近目标任务的新任务。我们在多种具有挑战性的导航任务上评估了该方法，实验结果表明，所提出的方法优于基于插值和生成对抗网络的SOTA CRL方法。

</details>

---

### [[20_Research/Papers/具身智能/Score-Based_One-step_MeanFlow_Policy_Optimization|Score-Based One-step MeanFlow Policy Optimization]]

![[assets/2605.23365_figure.png|800]]

- **arXiv**: [2605.23365](https://arxiv.org/abs/2605.23365)
- **PDF**: https://arxiv.org/pdf/2605.23365
- **详细分析**: [[20_Research/Papers/具身智能/Score-Based_One-step_MeanFlow_Policy_Optimization|Score-Based One-step MeanFlow Policy Optimization]]
- **作者**: Kyungyoon Kim, Donghyeon Ki, Hee-Jun Ahn, Byung-Jun Lee
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.82（加权：具身智能 0.3，强化学习 1.36，世界模型 0.16）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

在连续动作强化学习中，传统高斯策略虽然简单，但往往只能表达单峰分布，难以刻画真实控制任务里常见的多峰动作结构。扩散模型和流匹配策略更有表达力，但推理时需要多步去噪，在线强化学习中这会带来显著的训练与采样开销。本文关注如何把这类生成式策略进一步压缩为单步生成，同时保留对高价值动作模式的建模能力，因此具有较强的实用意义，尤其适用于具身智能和机器人控制场景。

#### 方法概述和架构

论文提出 Score-Based One-step MeanFlow Policy Optimization（SOM），将 MeanFlow 的单步生成思想引入在线强化学习。核心思路是：不再依赖目标分布样本来构造 MeanFlow 的目标速度场，而是直接从 Q 函数出发，把负 Q 视为能量函数，通过 score estimation 估计目标分布的梯度。具体做法是结合 iDEM 风格的蒙特卡洛 score 估计器与 probability flow ODE，得到一个指向高价值动作区域的目标速度场。训练时采用 actor-critic 结构，actor 学习 MeanFlow 风格的速度网络，critic 提供 Q 函数并持续更新；推理时只需一次网络前向即可从噪声生成动作。作者还讨论了归一化与重标定、critic 更新以及 Best-of-N 评估等实现细节，以保证在线训练稳定性。

#### 实验结果分析

实验主要在 MuJoCo 运动控制基准上进行，并与以扩散模型、流匹配和其他生成式策略为基础的在线 RL 方法比较。结果显示，SOM 在仅单步生成的情况下达到了最先进的控制性能，同时训练和推理时间都显著低于需要多步去噪的基线。文中还在 bandit 环境上分析了模式覆盖与对不完美 critic 的鲁棒性，并做了若干消融实验；可见文本未给出具体数值，但结论表明该方法在多峰动作建模与在线效率之间取得了较好平衡。

<details>
<summary>完整摘要</summary>

扩散模型和流匹配已经成为强化学习中表达能力很强的策略类别，但它们依赖多步去噪，在推理阶段带来较大的计算开销，这在在线强化学习中尤其成问题。MeanFlow 提供了一种有前景的替代方案，它学习一个平均速度场，只需一次网络评估即可将噪声映射到数据。然而，MeanFlow 通常需要来自目标分布的样本来构造其目标速度场，而在线强化学习中无法获得这类样本。为此，我们提出 Score-Based One-step MeanFlow Policy Optimization（SOM），一种 actor-critic 算法：它通过 score estimation 和 probability flow ODE，直接从 Q 函数构造目标速度场，从而将概率质量集中到高价值模式上。在完全在线的强化学习设定中，SOM 仅用单步生成就在运动控制任务上取得了最先进的性能，并且与以往基于扩散和流匹配的策略相比，显著降低了训练和推理时间。

</details>

---

### [[20_Research/Papers/大模型/XWind_A_Cross-site_Router_for_Large_Language_Model_Inference_Serving_at_Renewable_Energy_Farms|XWind: A Cross-site Router for Large Language Model Inference Serving at Renewable Energy Farms]]

![[assets/2605.23348_figure.png|800]]

- **arXiv**: [2605.23348](https://arxiv.org/abs/2605.23348)
- **PDF**: https://arxiv.org/pdf/2605.23348
- **详细分析**: [[20_Research/Papers/大模型/XWind_A_Cross-site_Router_for_Large_Language_Model_Inference_Serving_at_Renewable_Energy_Farms|XWind: A Cross-site Router for Large Language Model Inference Serving at Renewable Energy Farms]]
- **作者**: Tella Rajashekhar Reddy, Atharva Deshmukh, Liangcheng Yu, Chaojie Zhang, Mike Shepperd, Rohan Gandhi, Anjaly Parayil, Srinivasan Iyengar, Ajay Manchepalli, Debopam Bhattacherjee
- **cs 子类**: cs.AI, cs.DC, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

大模型推理需求正在快速增长，但电网扩容慢、成本高、远距离输电还有额外损耗，而许多风电等可再生能源却在发电地附近缺少就地负载，导致清洁电力无法被充分利用。本文关注的是如何把大模型推理算力部署到风电场等可再生能源场站旁边，在不完全依赖传统数据中心供电的情况下，形成一种补充型 AI 基础设施。作者提出这一方向值得关注，是因为它同时面对算力扩张、能源约束和电网压力三重矛盾，并且面向的是占据主导地位的推理负载，而非较少数的训练任务。

#### 方法概述和架构

论文提出 AI Greenferencing 作为部署范式，即把模块化 AI 计算节点放到风电场等可再生能源来源附近。为了在风力波动下稳定服务推理请求，作者设计了 XWind，一个轻量、反应式、与具体工作负载无关的跨站点推理路由器。XWind 只依赖三类实时信号：推理延迟、KV-cache 利用率和队列深度；系统会据此动态配置各站点并把请求分发到更合适的站点。架构上，XWind 与站点本地控制器 XW-Slc 协同工作，后者负责在局部电力紧张时基于在线遥测重配站点；跨站点路由器则接收这些状态并执行跨站点重路由，从而绕开电力不足的站点。

#### 实验结果分析

作者在一个真实的 64-GPU A100 测试床上进行了评估，测试床模拟了三个由风能供电的站点，并使用 Azure 生产流量轨迹进行实验。实验比较了 XWind 与多个基线方案，包括功率限额、GPU 空转等，也与作者提出的另一种更强竞争方案对比。结果显示，XWind 的 P99 端到端延迟最高可降低 52%，相较于功率限额和 GPU 空转等基线最高可降低 98%。文中还强调该方法在不同工作负载类型、负载水平和 GPU 代际上都保持了稳定收益；更细的数值和消融细节在节选中未给出具体数值。

<details>
<summary>完整摘要</summary>

AI 用电需求正以前所未有的速度增长，而电网往往已显老化，难以跟上这一增长。电网扩建需要高额资本支出，而且长距离输电会带来损耗；与此同时，在能源源头却存在大量可再生能源，只是尚未与需求匹配。本文提出一种互补型 AI 基础设施部署模式——AI Greenferencing，即把模块化 AI 计算部署到可再生能源来源附近，重点面向风电，从而扩展 AI 的部署范围，为可再生能源站点形成本地的、计量表后负载，并帮助缓解公用电力系统日益加重的压力。我们的可行性分析表明，在距 Azure 数据中心 50 ms 网络往返时间范围内，存在 890+ GW 的风电容量；同时，通过按站点“右尺寸化”部署，并利用风能在空间上的互补性，整体机群利用率可以与传统部署方式保持相当。为了在风力不断变化的条件下处理推理请求，我们构建了 XWind，它是一个轻量、反应式、与工作负载无关的 AI 推理路由器，仅使用实时信号——推理延迟、KV-cache 利用率和队列深度——来动态配置各站点并分配请求。在一个真实的 64-GPU A100 测试床上进行评估时，该测试床模拟了三个风电供能站点并使用 Azure 生产流量轨迹，XWind 相比最强竞争方案（也是我们提出的思路）将 P99 端到端延迟最多降低 52%，相比功率限额和 GPU 空转等基线最多降低 98%，且在不同工作负载类型、负载水平和 GPU 代际上都保持一致收益。

</details>

---

### [[20_Research/Papers/具身智能/Sparse_Compositional_Flow_Matching_by_geometric_assembly_from_motion_primitives|Sparse Compositional Flow Matching by geometric assembly from motion primitives]]

![[assets/2605.23341_figure.png|800]]

- **arXiv**: [2605.23341](https://arxiv.org/abs/2605.23341)
- **PDF**: https://arxiv.org/pdf/2605.23341
- **详细分析**: [[20_Research/Papers/具身智能/Sparse_Compositional_Flow_Matching_by_geometric_assembly_from_motion_primitives|Sparse Compositional Flow Matching by geometric assembly from motion primitives]]
- **作者**: Yan Tang, Yuanbo Tang, Tingyu Cao, Shaolun Huang, Yang Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

具身智能中的轨迹生成，面向的是机械臂、水下机器人、移动机器人等实体系统可执行的动作序列，是规划、控制和技能迁移的重要基础。然而，现有扩散、VAE 和 flow matching 等生成模型往往把轨迹当作逐点生成的稠密信号来建模，容易忽略轨迹内部天然存在的分段结构与复用片段，导致样本效率不高、可解释性也较弱。论文关注的核心问题是：能否把轨迹生成改写为“少量运动原语的组合与放置”，并直接在物理轨迹空间中完成，而不是先在潜空间组合、再事后解码回轨迹。

#### 方法概述和架构

作者提出 Sparse Compositional Flow Matching，将轨迹视为在共享时间轴上对有限运动原语库进行稀疏放置的结果。第一部分是 Motion-Primitive Dictionary Learning：每个原语原子都带有可学习的长度掩码和起始指示，使其自身就对应一段形状稳定、可直接复用的轨迹片段，而不是依赖卷积输出间接表示。第二部分是 Structural Sparse Flow Matching with Geometric Constraints：模型生成一个二值的原语-时间放置矩阵，并通过 duration-aware tokenization 建模原语持续时间。训练时，字典学习和 flow matching 共享同一个放置变量，前者用它重构真实轨迹，后者把它作为生成目标；同时加入可微的几何约束，显式惩罚相邻原语拼接处的空间不连续和时间断裂。推理时，模型先采样放置矩阵，再由原语字典按时间轴拼接成完整轨迹，从而实现可解释的组合式轨迹生成。

#### 实验结果分析

论文在 Open X-Embodiment 和 3DMoTraj 两个具身轨迹数据集上进行了验证，覆盖了机器人操作与 3D 水下轨迹等场景。结果显示，该方法达到当前最优性能，并将 FDE/ADE 比例从约 1.8 降到 1.07，说明生成轨迹的终点误差与整体轨迹误差更加平衡。相较最强基线，ADE 提升 19.2%，FDE 提升 21.0%。从文中给出的分析看，随着任务复杂度上升，该方法的性能增益更明显；但节选中未给出更细的消融数值。

<details>
<summary>完整摘要</summary>

具身轨迹，如机器人机械臂、水下航行器和移动机器人的可执行运动序列，是具身智能的基础输出。现代生成模型通常把它们当作稠密、整体的信号，逐点生成，以拟合复杂的高维后验，却没有对数据中的潜在结构进行建模；这与结构化生成模型文献长期指出的样本效率不足问题是一致的。我们认为，采用组合式的潜在结构是自然选择：许多具身任务共享重复出现的运动片段，这些片段可以被显式表示为一个有限的、可复用的运动原语库；同时，组合单元天然与子任务边界对齐，有利于任务分解。然而，现有的组合式生成器通常在潜空间中进行组合，并依赖事后解码来把采样到的单元映射回真实轨迹片段。我们则通过 flow matching 框架，直接在物理轨迹空间中进行组合，并设计了两个相互耦合的模块。Motion-Primitive Dictionary Learning 为每个字典原子配备可学习的长度掩码和二值起始指示，使得原子本身就是原语，并可在被放置到任意位置时原样复用。Structural Sparse Flow Matching with Geometric Constraints 则通过考虑持续时间的 tokenization 生成一个二值放置矩阵，并使用可微的几何损失，在相邻原语拼接处约束空间连续性和时间连续性。在 Open X-Embodiment 和 3DMoTraj 上，该框架取得了当前最优精度，并将 FDE/ADE 比例从约 1.8 降至 1.07；相较最强基线，ADE 提升 19.2%，FDE 提升 21.0%。

</details>

---

### [[20_Research/Papers/大模型/Human-in-the-Loop_Multi-Agent_Ventilator_Decision_Support_with_Contextual_Bandit_Preference_Learning|Human-in-the-Loop Multi-Agent Ventilator Decision Support with Contextual Bandit Preference Learning]]

![[assets/2605.23320_figure.png|800]]

- **arXiv**: [2605.23320](https://arxiv.org/abs/2605.23320)
- **PDF**: https://arxiv.org/pdf/2605.23320
- **详细分析**: [[20_Research/Papers/大模型/Human-in-the-Loop_Multi-Agent_Ventilator_Decision_Support_with_Contextual_Bandit_Preference_Learning|Human-in-the-Loop Multi-Agent Ventilator Decision Support with Contextual Bandit Preference Learning]]
- **作者**: Sijia Li, Xiaoyu Tan, Qixing Wang, Weiyi Zhao, Chen Zhan, Teqi Hao, Xuemin Wang, Lei Gu, Roland Eils, Xihe Qiu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.6，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

机械通气调参是 ICU 中典型的高风险序贯决策任务，需要随着患者肺力学、气体交换、血流动力学和镇静状态的变化不断调整呼吸机设置，同时还要满足安全边界与不同临床医生的个性化操作风格。传统规则系统难以在异质患者和非平稳病程中实现个性化泛化，而端到端强化学习或单一大模型方案又往往难以控制、审计和解释。因而，如何把临床可审查的协作流程、可追踪证据链和个体化偏好学习结合起来，是这篇工作值得关注的核心原因。

#### 方法概述和架构

论文提出 VDSS（Ventilator Decision Support System），一个人类在环的多智能体呼吸机决策支持框架。系统将决策拆分为多个模块化代理：波形分析、异常检测、治疗阶段/目标推断、Hold/Adjust 门控、策略选择、模式选择、参数规划、反思修订和病历总结，并通过契约驱动的结构化接口与确定性安全检查连接，保证生成式推理始终受设备和安全约束。输入包括当前床旁状态、呼吸机设置、短期上下文、长期记忆，以及可用时的压力/流量波形；输出则是可执行的模式与参数调整建议、面向临床医生的解释摘要和可审计的轨迹记录。交互过程中，系统在每轮候选方案后等待医生接受或拒绝，若被拒绝则由 Reflect Agent 将反馈转成局部重规划约束，只回退到最小必要的决策层以减少无效迭代。偏好学习部分使用 contextual bandit 做在线自适应：在每个调整周期结束后，以上一次被临床医生最终接受的方案、完整交互轨迹和周期级偏好信号更新个体化偏好状态，从而引导后续推荐更贴合不同医生的调参习惯。

#### 实验结果分析

作者在回顾性 ICU 轨迹回放场景下进行评估，数据来自多中心 ICU 队列，包含 1309 条结构化记录和 7447 条呼吸机设置条目，覆盖 13 种通气模式。实验比较了不同 backbone 下的直接单模型生成与 VDSS 流程，并使用 next-step replay 误差指标（如 MSE、R²）以及专家对 100 个周期的 1–5 分评分进行评估。结果显示，VDSS 在重放精度和临床可接受性上均优于直接生成基线，去掉波形证据或偏好上下文都会带来性能下降，说明两者都对稳定推荐和可解释性有贡献。节选文本中给出了部分数值例子，但对全部实验结果的具体数值并未完整展示。

<details>
<summary>完整摘要</summary>

呼吸机决策支持需要进行序贯决策，以跟踪不断变化的生理状态和疾病轨迹，同时还要满足安全边界并适配不同临床医生的个性化调参风格。基于规则的方法很少能够泛化到个性化场景，端到端强化学习或单一大语言模型系统也仍然难以控制和审计。我们提出了 Ventilator Decision Support System（VDSS），一种人类在环的多智能体框架，它通过契约驱动的结构化接口协调模块化决策组件，并生成可追踪的证据供审查。VDSS 使用 contextual bandit 进行在线偏好自适应，在每个调整周期结束时根据临床医生最终接受的决策更新其个体化偏好，并据此指导后续推荐。结构化的拒绝反馈会触发针对性的重规划，以减少无效迭代并提升交互稳定性。基于回顾性 ICU 轨迹回放与专家审阅的实验表明，该系统能够提高推荐的可接受性，并减少达到可接受方案所需的交互轮数，从而支持可临床部署的人机协作。

</details>

---

### [[20_Research/Papers/大模型/Parallel_Context_Compaction_for_Long-Horizon_LLM_Agent_Serving|Parallel Context Compaction for Long-Horizon LLM Agent Serving]]

![[assets/2605.23296_figure.png|800]]

- **arXiv**: [2605.23296](https://arxiv.org/abs/2605.23296)
- **PDF**: https://arxiv.org/pdf/2605.23296
- **详细分析**: [[20_Research/Papers/大模型/Parallel_Context_Compaction_for_Long-Horizon_LLM_Agent_Serving|Parallel Context Compaction for Long-Horizon LLM Agent Serving]]
- **作者**: Musa Cim, Burak Topcu, Chita Das, Mahmut Taylan Kandemir
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

长链路 LLM agent 在多轮任务中会不断累积对话历史，最终超过模型上下文窗口，因此必须通过上下文压缩来保留关键信息。现有做法通常依赖 LLM 直接对整段历史做同步摘要，但这类摘要天然有信息损失，而且随着上下文变长，输出长度和保留内容会出现明显波动，导致代理在不同运行中的记忆不稳定。与此同时，同步压缩会阻塞推理流程，往往带来数十秒级的等待，成为长任务 agent 服务中的主要瓶颈。

#### 方法概述和架构

论文提出 Parallel Context Compaction，用并行方式替代传统的整段顺序压缩。具体做法是：当对话长度超过阈值后，先对当前历史做快照，再按固定块大小切分成多个连续 block；随后为每个 block 构造带有目标块标记的压缩提示，并通过 vLLM 并发发送给模型。各 worker 共享逐步扩展的前缀，同时将当前目标块放在提示末尾，以兼顾前缀缓存利用和跨块上下文可见性。所有 block 的摘要完成后，按块顺序拼接成压缩后的历史，替换原始快照继续供 agent 使用。该设计还允许操作者通过 block 数量对摘要体积进行更细粒度、可预测的控制，并可针对不同 block 做更有针对性的提示工程。

#### 实验结果分析

作者在 HotpotQA 多跳问答和 LoCoMo 长上下文对话上评估了该方法，并覆盖了四个 backbone：Llama-3.1-8B、Llama-3.3-70B、gpt-oss-20B、gpt-oss-120B，横跨 8B 到 120B、稠密与 MoE、推理与非推理模型。实验在 vLLM、prefix caching 和 chunked prefill 的服务环境下进行，比较对象是顺序同步压缩基线，关注端到端 wall time、压缩吞吐量和摘要体积等指标。结果显示，在相同压缩解码量下，并行压缩可降低端到端耗时并提升吞吐；同时，节选文本还表明顺序压缩中摘要长度与输入长度、提示详细程度之间关系很弱，且存在明显的 run-to-run 不稳定性。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

长链路 LLM agent 会不断累积对话历史，最终超过模型的上下文窗口。通过基于 LLM 的摘要进行上下文压缩可以保持对话长度受控，但这种摘要本质上会丢失信息，而且同步调用会让 agent 推理停顿数十秒。此外，由于提示中的长度约束大多会被忽略，操作者无法对摘要体积进行细粒度控制；随着上下文增长，模型生成的输出 token 数量以及保留下来的信息都会在不同运行之间大幅波动，使得 agent 所保留的知识在跨运行时不可预测。我们提出面向长链路 agentic 流程的并行压缩（parallel compaction），并在 HotpotQA 多跳问答和 LoCoMo 长上下文对话基准上，将其与顺序同步基线进行对比，覆盖了四种骨干模型，参数规模从 8B 到 120B，既包含稠密架构也包含 MoE 架构，同时包含推理型与非推理型模型。并行压缩让操作者能够对摘要体积进行细粒度且可预测的控制，并且可以针对不同 block 设计更有针对性的提示。与相同压缩解码量下的顺序基线相比，它降低了端到端 wall time，并提升了压缩吞吐量。

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Microcanonical_Graph_Ensemble_with_Assortativity_Constraints|Reinforcement Learning for Microcanonical Graph Ensemble with Assortativity Constraints]]

![[assets/2605.23285_figure.png|800]]

- **arXiv**: [2605.23285](https://arxiv.org/abs/2605.23285)
- **PDF**: https://arxiv.org/pdf/2605.23285
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Microcanonical_Graph_Ensemble_with_Assortativity_Constraints|Reinforcement Learning for Microcanonical Graph Ensemble with Assortativity Constraints]]
- **作者**: Hoyun Choi, Junghyo Jo, Deok-Sun Lee
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

网络结构如何决定功能，是复杂网络研究中的基础问题，常通过在给定约束下生成随机图来构造对照组。现有 ERGM 等规范系综方法通常只是在期望意义上满足约束，单个样本仍会围绕目标波动，容易引入系综伪影。相比之下，微正则系综要求每个样本都严格满足硬约束，但除固定度序列外，如何高效采样一直较为困难。本文聚焦于 assortativity（度相关性）约束下的图生成，具有较强的方法学价值，也可为网络渗流、同步、传播和鲁棒性等研究提供更精确的零假设模型。

#### 方法概述和架构

论文提出 Deep Microcanonical Graph Generator（DMGG），把图生成建模为强化学习中的马尔可夫决策过程。其输入是一个已随机化的初始图，输出是在保持度序列不变的前提下，通过一系列 rewiring 操作逐步逼近目标 assortativity 的新图。训练阶段使用 PPO 学习策略网络，奖励信号直接来自当前 assortativity 与目标值之间的偏差，因此不需要监督数据集，也不需要为每个目标单独调参。推理阶段，策略网络为候选边重连动作打分，并选择最能推动图朝目标方向移动的操作，直到满足 |ρ−ρ*|<ε 的硬约束。作者还将其与基于 Metropolis-Hastings 的 ERGM 进行了对比，强调 DMGG 是一种“策略引导搜索”而非随机接受-拒绝采样。

#### 实验结果分析

实验在不同规模、稀疏度和拓扑上评估了 DMGG，包括训练时的 WS、ER、BA，以及测试时更广泛的 ER、SBM、RGG、CL、HK、BA 等图模型；对比基线主要是 ERGM，指标包括 assortativity 分布、标准差、生成效率以及构型多样性。结果显示，DMGG 能在更短的重连步数内稳定达到目标 assortativity，生成速度至少快一个数量级。与 ERGM 相比，DMGG 生成的 assortativity 分布更集中、更接近硬约束，同时仍保持较好的配置多样性；节选文本未给出具体数值，但作者还指出其可作为精确零模型，用于分离 clustering coefficient 等次级观测量的影响。

<details>
<summary>完整摘要</summary>

网络结构如何决定功能，是一个基础性问题，而这一问题可以通过对结构属性进行精确控制的图系综来研究。规范系综方法通常被表述为指数随机图模型（ERGM），它们只在期望意义上施加约束，因此单个实现会围绕目标值波动。相对地，微正则系综会对约束进行逐个样本的严格施加，但除固定度序列之外，实际可用的采样方法一直难以实现。本文提出 Deep Microcanonical Graph Generator（DMGG），这是一个强化学习（RL）框架，它通过保持度序列不变的边重连操作，将任意给定图精确变换为具有指定 assortativity 的图；assortativity 描述的是相邻节点度之间的相关性。与依赖 ERGM 中熵主导的 Metropolis-Hastings 动力学不同，DMGG 采用策略引导搜索，最大化改变 joint-degree matrix，从而无需穷尽式参数调优，并且在保持构型多样性的同时，生成速度至少提升一个数量级。由于 DMGG 能够泛化到不同的图规模、稀疏度和拓扑结构，它提供了精确的零模型，使得可以定量分离诸如 clustering coefficient 之类的次级可观测量。这些结果表明，RL 是一种实用且强大的硬约束图生成范式，并为在摆脱系综伪影的条件下研究结构—功能关系开辟了新途径。

</details>

---

### [[20_Research/Papers/具身智能/ChainFlow-VLA_Causal_Flow_Planning_with_Vision-Language_Models|ChainFlow-VLA: Causal Flow Planning with Vision-Language Models]]

![[assets/2605.23270_figure.png|800]]

- **arXiv**: [2605.23270](https://arxiv.org/abs/2605.23270)
- **PDF**: https://arxiv.org/pdf/2605.23270
- **详细分析**: [[20_Research/Papers/具身智能/ChainFlow-VLA_Causal_Flow_Planning_with_Vision-Language_Models|ChainFlow-VLA: Causal Flow Planning with Vision-Language Models]]
- **作者**: Xiyang Wang, Xinlin Wang, Tingguang Zhou, Gong Chen, Xingtai Gui, Zhi Xu, Xiaolei Wu, Feiyang Tan, Hangning Zhou, Mu Yang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.3，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

端到端自动驾驶需要同时处理时序因果推理和全局轨迹一致性，但现有方法往往只能兼顾其一：自回归模型擅长建模交互相关的时间依赖，却容易在逐步解码中累积误差；扩散模型虽然更利于全局优化，却缺少显式因果约束，在交互复杂和安全敏感场景中稳定性不足。作者指出，更深层的问题在于，已有方法通常把因果建模与全局优化视为两套彼此分离的范式，缺少统一的概率化轨迹建模方式。该工作因此值得关注，因为它尝试把“先生成、再修正”的规划逻辑与视觉语言模型的语义理解结合起来，面向长尾和歧义场景提升鲁棒性。

#### 方法概述和架构

论文提出 ChainFlow-VLA，将轨迹规划统一为一个“因果生成 + 全局修正”的概率框架。第一阶段 Chain 是自回归轨迹生成器，基于 BEV 风格的驾驶特征和可学习轨迹查询，按时间步迭代预测控制量，并通过自行车运动学模型生成一组具有因果一致性的轨迹候选，从而得到多个离散的运动模式。第二阶段 Flow 是 VLM 引导的残差扩散模块，它不直接重新生成整条轨迹，而是在每个自回归候选轨迹附近建模残差分布，把真实轨迹表示为“AR 候选 + 修正量”，再用扩散式去噪逐步完成修正。VLM 的隐藏状态被作为语义先验注入到残差修正过程中，用来表达路线意图、交通语境和轨迹可行性等高层信息。整体训练目标是学习“候选模式的分布”和“条件残差分布”的联合建模；推理时先由 Chain 产生多模态提案，再由 Flow 在模式条件下做语义约束下的精细调整。

#### 实验结果分析

实验在 NAVSIM v1 基准上验证了该方法，论文报告 ChainFlow-VLA 取得 94.85 的分数，达到并略超人类水平 94.8。作者将其与现有端到端自动驾驶、自回归规划和扩散式规划方法进行比较，结论是该框架在歧义场景和长尾场景中表现更稳健。正文还提到其在排行榜上刷新了当前最优成绩，显示出把因果建模、全局优化与语义引导统一起来的有效性。可见文本表明作者还做了消融实验和定性分析，但节选中未给出具体数值细节。

<details>
<summary>完整摘要</summary>

当前的端到端自动驾驶系统在根本上受限于时序因果推理与全局轨迹一致性之间的不匹配。自回归（AR）模型通过因果分解能够捕捉交互感知的时间依赖关系，但其逐步解码会导致误差累积和全局结构次优。相比之下，扩散模型能够在全局层面优化轨迹，但缺少显式的因果约束，因此在交互复杂和安全关键的场景中并不可靠。这种二分现象揭示了一个更深层的问题：现有方法把因果建模和全局优化当作彼此分离的范式，缺少一种原则性的统一方式将二者纳入同一个轨迹分布中。为此，我们提出 ChainFlow-VLA，在统一的概率框架下将因果生成与全局细化结合起来。我们将规划形式化为一个由 AR 诱导模式组成的混合分布，并学习由 Vision-Language Model（VLM）条件化的、关于这些模式的残差分布。一个自回归生成器（Chain）先产生一组离散的因果轨迹模式，随后由基于扩散的细化器（Flow）利用 VLM 的隐藏状态作为语义先验，在残差空间中进行基于模式的修正，同时保持因果结构不变。这种直接的条件注入方式，可以把高层场景理解无缝融入到细粒度轨迹调整中。实验表明，ChainFlow-VLA 在歧义和长尾场景中实现了稳健规划，在 NAVSIM v1 排行榜上取得了 94.85 的最优分数，达到人类水平（94.8）。代码将开源于 https://github.com/AFARI-Research/ChainFlow-VLA 。

</details>

---

### [[20_Research/Papers/具身智能/6G_Communication_Networks_Enabling_Embodied_Agents_Architecture_and_Prototype|6G Communication Networks Enabling Embodied Agents: Architecture and Prototype]]

![[assets/2605.23263_figure.png|800]]

- **arXiv**: [2605.23263](https://arxiv.org/abs/2605.23263)
- **PDF**: https://arxiv.org/pdf/2605.23263
- **详细分析**: [[20_Research/Papers/具身智能/6G_Communication_Networks_Enabling_Embodied_Agents_Architecture_and_Prototype|6G Communication Networks Enabling Embodied Agents: Architecture and Prototype]]
- **作者**: Lipeng Dai, Luping Xiang, Kun Yang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.5，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

这篇论文关注“具身智能”从算法走向真实世界后的通信问题：机器人、机械臂、远程操作系统等具身体在执行感知—决策—动作闭环时，对时延、可靠性、带宽和确定性的要求，明显高于纯软件智能体。作者指出，现有 5G 方案更多面向被动信息传输，难以充分支撑高精度遥操作、工业协同和大规模机器人集群等场景。随着 6G 被寄予亚毫秒时延、超高可靠、原生智能与通感一体等能力，研究“6G 如何为具身智能体通信赋能”具有很强的现实价值和前瞻意义。

#### 方法概述和架构

论文先从概念层面梳理具身智能体的定义、范围、价值以及与非具身智能体的区别，再分析具身智能体与 6G 的共生关系，说明双方如何互相促进。随后作者提出一个面向人机远程交互的分层通信架构，包含人类意图感知层、基于 O-RAN 的传输层、智能中介层和具身执行层。该架构的核心思路是：先从人的动作/意图侧采集信息，再经 O-RAN 与网络传输到中介平台，由中介层完成任务理解、控制协调与反馈调度，最后驱动实体机器人完成动作闭环。为了验证可行性，论文实现了端到端原型系统，将触觉设备、工业机械臂、中介平台和 5G O-RAN 测试床串联起来，形成从人到机器人再到反馈回人的完整链路。

#### 实验结果分析

实验部分基于一个包含触觉输入、工业机械臂、中介平台和 5G O-RAN 测试床的端到端原型系统展开。作者报告原型能够实现毫秒级时延和稳定闭环运行，说明所提分层架构具备工程落地的可行性。正文节选中未给出具体对比基线、指标表格或消融实验的数值细节，因此可见文本未给出具体数值。总体上，结果支持该架构可作为未来 6G-具身智能研究与产业部署的参考。

<details>
<summary>完整摘要</summary>

具身智能体将智能决策与真实世界中的物理执行相结合，其通信需求远比纯软件智能体更为严格且更具异质性。尽管 6G 有望提供亚毫秒级时延、超高可靠性、原生智能以及通感一体能力，但如何将这些能力用于支撑具身智能体通信的系统性研究仍然有限。本文从概念与工程两个角度，研究面向具身智能体的 6G 赋能通信系统。首先，我们回顾了具身智能体的概念及其具身价值，并明确其与非具身智能体的区别。随后，我们分析了具身智能体与 6G 网络之间的共生关系，强调 6G 的关键能力如何支持人机交互的严格需求。此外，我们还展示了具身智能体在增强通信网络方面的主动作用，包括扩展覆盖、环境感知和对物理世界的理解。基于这些认识，我们提出了一种用于人机远程交互的分层通信架构，包括人类意图感知层、基于 O-RAN 的传输层、智能中介层和具身执行层。为验证其可行性，我们实现了一个端到端原型系统，将触觉设备、工业机械臂、中介平台以及 5G O-RAN 测试床集成在一起。实验结果表明，该系统可实现毫秒级时延和稳定的闭环运行，验证了所提架构的实用性，并为未来 6G-具身智能研究与工业部署提供了参考。

</details>

---

### [[20_Research/Papers/具身智能/Lipschitz_Optimization_for_Formal_Verification_of_Homographies|Lipschitz Optimization for Formal Verification of Homographies]]

![[assets/2605.23203_figure.png|800]]

- **arXiv**: [2605.23203](https://arxiv.org/abs/2605.23203)
- **PDF**: https://arxiv.org/pdf/2605.23203
- **详细分析**: [[20_Research/Papers/具身智能/Lipschitz_Optimization_for_Formal_Verification_of_Homographies|Lipschitz Optimization for Formal Verification of Homographies]]
- **作者**: Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel, Alessio Lomuscio
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

在医疗、自动驾驶、航空航天等安全关键场景中，视觉神经网络不仅要“效果好”，还必须给出可证明的鲁棒性保证。现有形式化验证方法主要集中在像素空间的ℓ_p扰动或仿射变换上，难以覆盖相机位姿变化带来的真实图像形成过程，因此对“相机运动下的鲁棒性”仍缺乏有效验证手段。对于机器人与具身智能中的感知系统而言，视角变化、机位偏移、平面目标的透视畸变都是常见风险，这使得本文工作具有很强的现实价值。

#### 方法概述和架构

论文提出一种面向单应性变换（homography）的形式化验证方法，用于分析3D相机运动扰动下的网络鲁棒性。作者首先在针孔相机和近似平面场景假设下，建立从相机位姿到像素值的闭式映射，将相机的平移、旋转等6自由度扰动转化为参数化单应矩阵。随后，他们分析该映射的连续性与Lipschitz性质，把最近的Lipschitz optimization和分段连续优化思想扩展到非仿射投影变换上，从而为每个像素构造紧的线性上下界。最后，这些像素级界可被接入现有神经网络验证器中，用于传播到模型输出层，判断在给定位姿扰动范围内网络预测是否保持不变。

#### 实验结果分析

实验表明，该方法相较先前工作在实现层面最高可带来89%的速度提升，并将边界紧致度提升最高7%。作者还在VNN-COMP基准上进行评估，发现一些网络对投影视角扰动存在系统性弱点，说明仅依赖ℓ_p或仿射鲁棒性并不足以覆盖真实风险。进一步的跑道可见性分类器案例研究展示了该方法在安全关键场景中揭示相机运动脆弱性的能力。文中节选未给出更细的分任务数值结果，因此只能确认其总体优于基线，但无法补充更多具体指标。

<details>
<summary>完整摘要</summary>

在受监管行业中采用视觉神经网络，需要有形式化的鲁棒性保证，尤其是在医疗、自动驾驶和航空航天等安全关键领域。然而，现有方法仅限于不完备的统计验证，或者仅能处理ℓ_p范数扰动与仿射变换，而这些只覆盖了图像形成过程中的一小部分扰动。特别是，尽管相机运动对于部署许多视觉应用至关重要，但针对相机运动的鲁棒性验证仍然是一个悬而未决的问题。我们提出一种形式化验证方法，目标是针对捕获相机的3D运动扰动进行鲁棒性分析。我们首先建立从相机位姿到像素值的闭式映射。通过分析由此得到的单应性变换的连续性性质，我们证明可以将最新的Lipschitz optimization与分段连续方法扩展到该场景，从而为受扰像素值推导出紧致的线性界。我们的方法适用于具有明显平面结构的场景，例如增强现实中的地面平面、自动驾驶中的道路标线和交通标志，以及机器人操作中的平面工作空间。这使得对投影几何变换的形式化验证首次成为可能，而无需复杂仿真、替代网络或显式图像形成模型。我们验证了实现效果，并展示了相较先前工作最高89%的加速和最高7%的更紧边界。随后，我们在VNN-COMP基准上评估该方法，揭示了模型对投影扰动的系统性弱点。最后，我们在一个安全关键的跑道分类器上展示了真实世界案例，突出相机运动带来的实际脆弱性，并回应了学习模型认证中的一个关键挑战。数据与代码已公开发布于 https://github.com/jeangud/homography-verification 。

</details>

---

### [[20_Research/Papers/大模型/Autonomous_Frontier-Based_Exploration_with_VLM_Guidance|Autonomous Frontier-Based Exploration with VLM Guidance]]

![[assets/2605.23165_figure.png|800]]

- **arXiv**: [2605.23165](https://arxiv.org/abs/2605.23165)
- **PDF**: https://arxiv.org/pdf/2605.23165
- **详细分析**: [[20_Research/Papers/大模型/Autonomous_Frontier-Based_Exploration_with_VLM_Guidance|Autonomous Frontier-Based Exploration with VLM Guidance]]
- **作者**: Aarush Aitha, Avideh Zakhor
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.85（加权：具身智能 0.3，大模型 0.65，机器人 0.9）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

未知且危险环境中的自主机器人探索一直是经典难题，常见的 frontier-based exploration 和 NBV 规划虽然有效，但主要依赖几何启发式，容易做出缺乏全局语境的次优决策。本文关注的是如何让机器人在“看不全、信息不完备”的场景下，更像人一样根据地图结构和视觉线索选择下一步探索方向。作者认为，Vision-Language Models（VLMs）的跨模态推理能力可以弥补传统规划器在高层策略上的不足，因此这一工作值得关注，尤其适合机器人、具身智能与大模型结合的研究方向。

#### 方法概述和架构

论文提出一个“VLM 引导的 frontier-based exploration”流程：底层仍由传统机器人控制栈负责定位、建图和局部导航，高层决策则交给 VLM。系统先用 360° 旋转初始化局部 occupancy map，再从地图中检测 frontier，并把连续的 frontier 聚类成候选目标；随后通过长度阈值和距离阈值过滤掉过小或过远的 frontier，只保留最近的若干个候选。若当前只有一个 frontier，机器人直接导航；若有多个 frontier，则进入 decision point，由系统构造多模态提示，输入包括带路径轨迹与编号标注的俯视地图，以及每个 frontier 对应的视觉图像。VLM（文中使用 Gemini 2.5 Pro）根据地图拓扑、视觉内容和历史对话记录，输出要前往的 frontier 编号及其推理理由，系统再调用 ROS/RTAB-Map 等模块执行路径规划与局部导航。为保证探索完整性，方法还加入了 Decision Point List 用于回溯，以及 frontier blacklisting 机制，用于避免重复尝试不可达或已探索区域。

#### 实验结果分析

作者在 Habitat 与 Matterport3D 搭建的六个室内环境中做了仿真验证，并与现有方法进行比较。结果表明，该方法在地图覆盖率上相较已有基线最高提升可达 24%，说明 VLM 的高层空间推理能有效改善探索效率。正文节选中未给出更细的具体数值，但可见文本未给出完整基线名称与逐项指标明细；同时作者强调该方案无需训练、系统轻量，并且只要有标准传感器和网络连接，就可以较容易迁移到其他机器人平台。

<details>
<summary>完整摘要</summary>

未知且危险环境中的自主机器人探索是一个长期存在的挑战，而借助 Vision-Language Models（VLMs）的高级推理能力，可以显著提升这一能力。我们提出了一种新的探索流水线：由 VLM 执行高层战略决策，指导传统的底层机器人控制栈。在决策点，机器人会生成一个多模态提示，其中包含当前地图以及潜在路径（即 frontiers）的视觉图像。VLM 分析该提示后，选择最有前景的 frontier，用基于上下文的空间推理替代简单的几何启发式方法。我们在六个室内环境的仿真中验证了这一方法，结果显示其相较现有方法，地图覆盖率最高可提升 24%。该流水线轻量、无需训练，并且只要机器人具备标准传感器和互联网连接，就可以很容易迁移部署。

</details>

---

### [[20_Research/Papers/强化学习/Infra-Bayesian_Reinforcement_Learning_Agents_Outperform_Classical_RL_For_Worst-Case_Robustness|Infra-Bayesian Reinforcement Learning Agents Outperform Classical RL For Worst-Case Robustness]]

![[assets/2605.23146_figure.png|800]]

- **arXiv**: [2605.23146](https://arxiv.org/abs/2605.23146)
- **PDF**: https://arxiv.org/pdf/2605.23146
- **详细分析**: [[20_Research/Papers/强化学习/Infra-Bayesian_Reinforcement_Learning_Agents_Outperform_Classical_RL_For_Worst-Case_Robustness|Infra-Bayesian Reinforcement Learning Agents Outperform Classical RL For Worst-Case Robustness]]
- **作者**: Manish Aryal, Faiyaz Azam, Agnivo Banerjee, Sai Sidhanth Manoharan Jayanthi, Allegra Laro, Clément Legentilhomme, Andrew Lin, Florian Lorkowski, Radman Rakhshandehroo, Patric Rommel, Emanuel Ruzak, Nathan Theng...
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

经典强化学习通常假设环境是固定且与智能体策略无关的，但在真实部署中，系统往往会受到人类、其他AI、预测器和机构的影响，环境行为可能随智能体策略变化。更关键的是，在这类非可实现（non-realizable）场景下，智能体的假设空间往往无法覆盖真实世界，传统贝叶斯方法可能给出“高度自信却错误”的后验，从而带来不可靠决策和无界遗憾。本文关注的是 AI 安全和开放世界中的最坏情形鲁棒性问题，因此值得关注。

#### 方法概述和架构

论文实现了一个面向有限输出、无状态决策问题的 Infra-Bayesian Reinforcement Learning（IBRL）原型架构。其核心表示不是单一概率后验，而是一组不精确假设对应的 affine measures（a-measures）/infradistributions：每个 a-measure 由概率部分、缩放系数和偏移项组成，用于把被观测排除的分支价值保留到偏移中。智能体先用 infra-Bayesian conditioning 对这组假设进行更新，再用“最小期望下界”对每个动作/策略进行评估，即在所有允许的评估器中取最坏情形。推理时，智能体选择使最坏情形期望值最大的动作，从而实现 maximin 决策；作者还说明了在退化到单一最小点且仅含经典不确定性的情况下，该架构可恢复普通贝叶斯行为。

#### 实验结果分析

实验主要在带有 Knightian uncertainty 的环境以及 Newcomb’s problem 上验证，比较对象是经典强化学习/决策理论基线。结果显示，IBRL 智能体在最坏情况下的 regret 更低，说明其对模型错配和策略依赖环境更稳健；在 Newcomb’s problem 中，IBRL 智能体选择了被认为最优的策略，而经典决策理论智能体则表现不佳。正文还提到附录中验证了：当假设完全相同且不确定性为经典类型时，infra-Bayesian 代理会退化为普通贝叶斯代理。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

经典强化学习假设智能体与一个固定环境交互，而环境的行为不依赖于智能体的策略。在非可实现（non-realizable）场景中，这一假设会失效：其他参与者可能会预判智能体的行为，尤其是在 AI 安全相关环境中，智能体会与预测器、人类、其他AI智能体以及制度交互。在这类环境里，智能体的模型类无法刻画其所处的世界。在模型错配（misspecification）条件下，经典贝叶斯方法可能产生“高度自信却错误”的后验、不可靠的决策以及无界遗憾，因为可实现性不再成立。Infra-Bayesianism 是一种决策理论框架，它通过区分两类不确定性来解决这些失败：一类是普通概率不确定性，可以合理地选择先验；另一类是 Knightian uncertainty，即没有理由构造此类先验的不确定性。它通过评估动作在最坏情形下的结果，而不是依据后验期望或加权平均来决策。我们提出了首个面向有限输出、无状态决策问题的 infra-Bayesian 强化学习架构的概念验证实现。我们的智能体维护一组不精确假设，使用 infra-Bayesian conditioning 对其更新，并通过最大化最坏情形期望值来选择动作。我们将这一 infra-Bayesian maximin 决策过程应用于一个存在 Knightian uncertainty 的环境，并展示了相比经典强化学习智能体更低的最坏情形 regret。我们还研究了 Newcomb’s problem，并表明 infra-Bayesian 智能体会选择最优策略，优于经典决策理论智能体。我们的结果为构建在模型错配和策略依赖不确定性下仍保持鲁棒性的强化学习智能体迈出了第一步。

</details>

---

### [[20_Research/Papers/强化学习/Classical_State_Preparation_for_Variational_Quantum_Algorithms_via_Reinforcement_Learning|Classical State Preparation for Variational Quantum Algorithms via Reinforcement Learning]]

![[assets/2605.23138_figure.png|800]]

- **arXiv**: [2605.23138](https://arxiv.org/abs/2605.23138)
- **PDF**: https://arxiv.org/pdf/2605.23138
- **详细分析**: [[20_Research/Papers/强化学习/Classical_State_Preparation_for_Variational_Quantum_Algorithms_via_Reinforcement_Learning|Classical State Preparation for Variational Quantum Algorithms via Reinforcement Learning]]
- **作者**: Gino Kwun, Dhanvi Bharadwaj, Gokul Subramanian Ravi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

变分量子算法（VQA）被认为是迈向实用量子优势的重要路径，常见于量子化学、组合优化和机器学习等场景，但其训练过程极易受到 barren plateaus 和大量局部极小值的影响，导致优化缓慢且不稳定。现有的 Clifford 电路热启动方法虽然利用了可经典高效模拟的特性，能够为 VQA 提供初始态，但依赖启发式搜索，在更大的组合空间中往往难以扩展。本文关注的是：如何在不改变原始参数化电路结构的前提下，自动找到更好的经典初始化，从而减少量子迭代开销并提高收敛质量。

#### 方法概述和架构

论文提出 CRiSP（Clifford Reinforcement Learning agent for State Preparation），把离散的 Clifford 前缀选择建模为一个序列决策问题。具体做法是在固定参数化旋转门之前，为每个旋转位置选择一个 Clifford 门作为前缀修饰；当连续参数初始化为 0 时，电路输出状态完全由这些离散前缀决定。智能体使用 Neural-Guided MCTS 进行搜索，并由基于 Transformer 的策略-价值网络提供先验概率与回报估计，网络通过 self-play 训练。环境状态是已选前缀门序列，动作空间是 24 个单比特 Clifford 门，终止时依据电路在目标哈密顿量上的期望能量给出奖励；由于全部由 Clifford 门构成，奖励可通过经典 stabilizer tableau 模拟高效计算。为适配长电路和稀疏奖励，作者进一步引入 curriculum learning，逐步扩展搜索步长/回合长度，让模型先学短视野再过渡到深层电路。

#### 实验结果分析

实验主要在 QAOA 基准上展开，规模最高达到 22 个量子比特、1,370 个参数，并与现有 Clifford 初始化方法进行对比，指标包括 average energy accuracy 和 best-achieved energy accuracy。结果显示，CRiSP 在相同评估预算下平均提升 3.17×，最高可达 45.02×；在最佳能量准确度上平均提升 2.44×，最高可达 16.01×。此外，作者还在 VQE 任务上做了泛化评估，表明该方法具有较好的鲁棒性与迁移能力；消融实验也支持渐进式 curriculum 对长时序任务的有效性。

<details>
<summary>完整摘要</summary>

变分量子算法（VQAs）有望为实用量子优势提供一条路径，但其优化过程受到 barren plateaus 和大量局部极小值的严重阻碍。尽管可经典模拟的 Clifford 电路可以作为 VQA 的热启动手段以加快收敛，现有基于启发式的方法在巨大的组合搜索空间中往往难以扩展。为克服这一瓶颈，我们提出 CRiSP（Clifford Reinforcement Learning agent for State Preparation），一个将离散前缀选择形式化为序列决策问题的框架。CRiSP 采用 Neural-Guided Monte Carlo Tree Search，并由基于 Transformer 的策略网络驱动；该策略网络通过 self-play 训练，从而在固定的参数化旋转门之前插入学习到的 Clifford 门。这使得我们能够仅通过多项式时间的经典 stabilizer 模拟构造高质量初始态，而无需改变底层电路架构。通过引入 curriculum learning 策略，逐步扩展搜索视野，智能体能够有效扩展到深层电路。我们在最多 22 个量子比特、1,370 个参数的 QAOA 基准上进行评估，结果表明，CRiSP 在平均能量准确度上较当前最先进的 Clifford 初始化方法平均提升 3.17×（最高 45.02×），在最佳能量准确度上平均提升 2.44×（最高 16.01×）。对 VQE 任务的评估进一步证明了该框架的鲁棒性和泛化能力。

</details>

---

### [[20_Research/Papers/大模型/Security_of_LLM-generated_Code_A_Comparative_Analysis|Security of LLM-generated Code: A Comparative Analysis]]

![[assets/2605.23091_first_page.png|800]]

- **arXiv**: [2605.23091](https://arxiv.org/abs/2605.23091)
- **PDF**: https://arxiv.org/pdf/2605.23091
- **详细分析**: [[20_Research/Papers/大模型/Security_of_LLM-generated_Code_A_Comparative_Analysis|Security of LLM-generated Code: A Comparative Analysis]]
- **作者**: Srivathsan G Morkonda, Mahmoud Selim, Hala Assal
- **cs 子类**: cs.AI, cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

当前大量软件开发者已经在实际开发流程中使用或计划使用 AI 工具，主要目的是提升开发效率并加快学习新知识。与此同时，LLM 生成代码已经进入真实生产环境，甚至被大型科技公司采用，因此其安全性不再只是理论问题，而是直接影响软件系统的风险暴露。作者指出，围绕 AI 辅助编程的担忧中，代码安全是最核心也最紧迫的问题之一。

#### 方法概述和架构

本文采用实证评估的方法，系统比较 7 个流行 LLM 生成代码的安全性。作者基于既有工作设计了评测流程，尽量模拟开发者在真实使用 LLM 生成代码时的行为方式，以便更贴近实际开发场景。评测输入是由开发者式提示触发的代码生成任务，输出则是各模型生成的代码及其安全漏洞特征。随后，研究对生成代码中的漏洞类型与严重程度进行分析，并比较不同 LLM 的安全表现。

#### 实验结果分析

实验表明，所评估的 7 个 LLM 全部会生成含有漏洞的代码，说明这一问题具有普遍性而非个别现象。更值得关注的是，其中多数漏洞被判定为高危或严重级别，意味着这些代码在真实系统中可能带来较大的安全风险。由于正文节选未提供具体实验设置、数据集名称、基线模型或数值指标，可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

如今，大多数软件开发者都在使用或计划在开发流程中使用人工智能（AI）工具，其首要原因包括提高生产力和加快学习。事实上，LLM 生成的代码目前已经进入生产环境，包括一些大型科技公司。然而，围绕使用 AI 工具生成代码所带来的风险，人们也提出了担忧。本文将注意力聚焦于软件安全风险。我们通过实证方法评估了 7 个流行 LLM 生成代码的安全性。在此基础上，我们沿用并扩展了先前工作，尽量模拟开发者使用 LLM 生成代码时的行为。结果显示，我们评估的 7 个 LLM 都会生成包含漏洞的代码，而且其中大多数漏洞属于严重或高危级别。

</details>

---

### [[20_Research/Papers/具身智能/Dreaming_Smoothly_and_Sample_Efficiently_with_Gradient_Penalized_Latent_Dynamics|Dreaming Smoothly and Sample Efficiently with Gradient Penalized Latent Dynamics]]

![[assets/2605.23089_figure.png|800]]

- **arXiv**: [2605.23089](https://arxiv.org/abs/2605.23089)
- **PDF**: https://arxiv.org/pdf/2605.23089
- **详细分析**: [[20_Research/Papers/具身智能/Dreaming_Smoothly_and_Sample_Efficiently_with_Gradient_Penalized_Latent_Dynamics|Dreaming Smoothly and Sample Efficiently with Gradient Penalized Latent Dynamics]]
- **作者**: Romil V. Sonigra, P. R. Kumar
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 强化学习, 机器人
- **相关性评分**: 2.72（加权：具身智能 0.6，强化学习 0.36，世界模型 1.56，机器人 0.2）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

在模型式强化学习中，世界模型的质量直接决定了“想象”轨迹的可信度与样本效率，尤其是在连续控制、机器人和具身智能任务中更为关键。现有 latent world model（如 DreamerV3）虽然已经能在多种任务上取得不错效果，但并没有显式约束其潜在状态转移的局部平滑性，导致一个重要的归纳偏置没有被充分利用。论文指出，连续控制系统通常满足“相近状态具有相近短期转移行为”的结构先验，将这一先验直接编码进潜在动力学有望减少交互数据需求，因此这项工作值得关注。

#### 方法概述和架构

作者提出 GPLD（Gradient-Penalized Latent Dynamics），作为 DreamerV3 的一种正则化项，用于对后验潜在分布施加行级别的 Jacobian 惩罚，鼓励潜在动力学在局部上更平滑。论文先从离散嵌入状态 MDP 中的邻域有限差分平滑出发，再推到连续状态极限，说明有限差分项在可微条件下会收敛为方向导数，而对方向进行各向同性平均后对应 Frobenius Jacobian 范数。实现上，GPLD 不直接约束整个世界模型，而是作用在 DreamerV3 的后验潜在概率映射上：输入为当前时刻的隐状态和编码器输出，输出是后验离散潜变量的概率表。由于显式计算完整 Jacobian 代价较高，作者使用 Hutchinson 风格的随机探针在输出空间估计每一行的 Frobenius 范数，从而高效近似该正则项。训练时，该正则项与 DreamerV3 原有的重建、奖励、终止预测以及动态/表示 KL 损失共同优化，并引入时间衰减系数控制正则强度。

#### 实验结果分析

论文在 DeepMind Control 的 proprioceptive 任务上验证了方法效果，并在更复杂的 locomotion 环境上观察到更明显的收益；对于更具挑战性的四足机器人任务，GPLD 能更早达到较高回报，并且在更长训练过程中表现出更稳定的后期学习。作者还报告了对高复杂度 proprioceptive locomotion 的更强增益，以及对主要设计选择的消融分析；就节选文本可见内容而言，具体单项实验数值并未完整展开，但文中给出了总体归一化提升。Pixel observation 任务上的收益相对更温和，说明当动力学学习与高维视觉编码强耦合时，局部平滑正则的作用会减弱。

<details>
<summary>完整摘要</summary>

基于模型的强化学习通过学习世界模型来提高样本效率。然而，现有的潜在世界模型（例如 DreamerV3）并没有显式地对其学习到的转移动力学施加局部平滑约束，因此一个有用的转移动力学学习归纳偏置尚未被充分利用。我们提出 GPLD，这是一种用于 DreamerV3 的梯度惩罚潜在动力学正则器，它对后验潜在分布施加按行计算的 Jacobian 惩罚，以鼓励局部平滑的转移学习。我们表明，这一惩罚可以被解释为离散嵌入状态 MDP 中有限差分平滑转移规律在连续潜变量情形下的对应形式，并使用 Hutchinson 风格的随机探针进行高效估计。实验上，在 DeepMind Control 的本体感觉任务中，GPLD 提升了整体样本效率，尤其在更高复杂度的运动控制环境中收益更显著。在更具挑战性的四足机器人任务上，GPLD 更早达到高回报行为，并在更长时间跨度上表现出更一致的后期学习。显式的局部平滑正则化是提升平滑连续控制环境中潜在世界模型的一个简单而有效的方法。GPLD 的代码已发布于 github.com/romils9/gpld-mbrl 。

</details>

---

### [[20_Research/Papers/大模型/DreamerNLplus_Interpretable_Modeling_of_Mental_Health_Dynamics_from_Social_Media_Timelines_using_Hybrid_Rule-Based_and_RAG_Methods|DreamerNLplus: Interpretable Modeling of Mental Health Dynamics from Social Media Timelines using Hybrid Rule-Based and RAG Methods]]

![[assets/2605.23052_figure.png|800]]

- **arXiv**: [2605.23052](https://arxiv.org/abs/2605.23052)
- **PDF**: https://arxiv.org/pdf/2605.23052
- **详细分析**: [[20_Research/Papers/大模型/DreamerNLplus_Interpretable_Modeling_of_Mental_Health_Dynamics_from_Social_Media_Timelines_using_Hybrid_Rule-Based_and_RAG_Methods|DreamerNLplus: Interpretable Modeling of Mental Health Dynamics from Social Media Timelines using Hybrid Rule-Based and RAG Methods]]
- **作者**: Maryia Zhyrko, Daisy Monika Lal, Erik van Mulligen, Lifeng Han
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, ComputerVision, Systems

#### 研究背景与动机

这篇论文面向 CLPsych 2026 shared task，目标是从社交媒体时间线中刻画心理健康状态、检测时间上的变化节点，并生成序列级摘要与动态模式。该问题直接对应心理健康研究中的低资源、弱标注和高噪声场景，既要识别细粒度心理状态，又要捕捉“转变”“恶化”“改善”等跨时间的变化。作者指出，现有方法在分类与回归、局部变化与全局叙事之间往往存在不一致，且语义质量与相似度指标的评估也常常冲突，因此值得关注。

#### 方法概述和架构

论文提出 DreamerNLplus，一个结合规则方法、检索增强生成（RAG）与开源大模型的混合框架，统一处理三类任务。Task 1 采用 Prompt2Predict-DeBERTa 流程：先用 Ollama 进行基于标签定义和证据的 LLM 数据增强，再用 DeBERTa 做 ABCD 子元素分类，最后把分类结果编码成 one-hot 向量输入 Random Forest 回归器，预测自适应/失配评分。Task 2 使用本地部署的 Llama 3.1 进行 few-shot prompting，将当前帖子与前 5 条时间线帖子组成上下文，输出 Switch 和 Escalation 的二元判断及简短理由；同时还构建了一个 XGBoost 基线，融合 TF-IDF、句向量、时间差分特征和若干语言学特征。Task 3.1 同时尝试确定性的规则摘要管线和 few-shot LLM 摘要方法，把 ABCD 标注或文本中的动态关系转写为结构化心理叙事；Task 3.2 则采用 RAG-LLM Signature Mining，先在批内抽取重复出现的 ABCD 动态，再跨批综合为每个方向的一段 90 词左右的动态签名，并用 5–10 个示例序列支撑。整体上，三个任务共享“状态—变化—叙事”的统一建模思路，并强调可解释性与本地部署带来的隐私友好性。

#### 实验结果分析

实验基于 CLPsych 2026 的官方任务设置与时间线社交媒体数据，评估覆盖 Task 1 的分类/回归、Task 2 的变化检测，以及 Task 3 的摘要和模式挖掘。作者报告，Task 1 中系统在子元素分类上排名 22，在 presence 估计上排名 20；并观察到分类性能与回归性能之间存在中等负相关，说明细粒度分类做得更好不一定能带来更准的强度预测。Task 2 中，提交的 LLM 方法综合 F1 达到 0.442，排名第 11，而 XGBoost 版本为 0.327；两者分别表现为高召回低精度与高精度低召回，反映出时间变化信号非常难学。Task 3.1 的官方排名中，基于 few-shot prompting 的提交最终综合表现为第 2，而 Task 3.2 的 RAG 方法在 Improvement 上排名第 1、在 Deterioration 上排名第 3；同时作者指出，CT/CS 与 ROUGE、BERTScore 之间存在明显评价分歧，具体数值在节选文本中未给出。

<details>
<summary>完整摘要</summary>

我们提出 DreamerNLplus，一个用于 CLPsych 2026 shared task 的混合框架，用于从社交媒体时间线中建模心理健康动态。我们的系统覆盖三个任务：心理状态建模、时间变化检测和序列级摘要。对于任务 1，我们结合基于大语言模型的数据增强、DeBERTa 分类以及 Random Forest 回归，实现结构化的状态预测。对于任务 2，我们使用 few-shot prompting，并在本地部署的 Llama 3.1 模型上，利用短期时间上下文检测 Switch 和 Escalation 事件。对于任务 3.1，我们同时探索了确定性的规则式摘要流程和基于 few-shot 的 LLM 方法，官方排名第 2。我们基于 RAG 的方法在任务 3.2 中取得了很强的表现，在 Improvement 上排名第 1、在 Deterioration 上排名第 3，表明其能够捕捉时间线中反复出现的心理变化模式。我们的分析揭示了若干关键挑战，包括分类与回归表现不匹配、时间转移建模困难，以及语义评估指标与相似度评估指标之间的不一致。这些发现凸显了心理健康动态建模的复杂性，并推动未来构建统一评估框架。我们在 https://github.com/4dpicture/CLPsych2026 公开了代码和 prompts。

</details>

---

### [[20_Research/Papers/大模型/Brain-LLM_Alignment_Tracks_Training_Data,_Not_Typology|Brain-LLM Alignment Tracks Training Data, Not Typology]]

![[assets/2605.23032_first_page.png|800]]

- **arXiv**: [2605.23032](https://arxiv.org/abs/2605.23032)
- **PDF**: https://arxiv.org/pdf/2605.23032
- **详细分析**: [[20_Research/Papers/大模型/Brain-LLM_Alignment_Tracks_Training_Data,_Not_Typology|Brain-LLM Alignment Tracks Training Data, Not Typology]]
- **作者**: Dongxin Guo, Jikun Wu, Siu Ming Yiu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

脑-大模型对齐（Brain-LLM alignment）已在英文上被反复验证，但人类语言脑网络在不同语言间具有神经解剖上的普遍性，因此一个关键问题是：这种对齐能否跨语言成立，真正驱动差异的究竟是语言类型学距离，还是训练数据分布。现有研究几乎都聚焦英文，难以区分“英文优势”到底来自英语本身，还是来自模型训练中英语占比更高。本文将这一问题放到中文、英文、法文三语的真实脑成像场景中，具有较强的认知科学与大模型可解释性意义。

#### 方法概述和架构

作者使用 Le Petit Prince 语料对应的 fMRI 数据，覆盖112名参与者在英语、中文和法语条件下的脑反应，并选取7个LLM，涵盖英语主导、中文主导和多语模型。方法上采用encoding model：先从不同层的LLM表示中提取特征，再预测各脑区的fMRI响应，以此评估模型表示与人脑语言活动的对齐程度。为区分训练数据效应与语言类型学效应，作者引入了语言主导训练模型的对照比较，尤其使用与 LLaMA-2-7B 架构和规模匹配的中文主导模型 Baichuan2-7B。进一步地，论文还计算正式的类型学距离指标和tokenization fertility，并在层级、脑区（如IFG与PTL）和跨语言迁移层面分析对齐变化，从而把训练数据组成、结构距离与表示层位置联系起来。

#### 实验结果分析

实验基于 Le Petit Prince 多语言fMRI数据和7个LLM，采用噪声上限归一化的编码性能作为核心指标。结果显示，所谓“英文优势”并非英语本身的固有属性，而主要由训练语言主导性造成：当模型换成中文主导的 Baichuan2-7B 后，对齐梯度完全反转，变为对中文脑数据最好、对英文最差。与此同时，正式类型学距离也会独立影响对齐下降，其中与句法/构式相关的 IFG 区域呈现出比词汇语义相关的 PTL 更陡的类型学梯度；tokenization fertility 还能解释跨语言最优编码层位移的大约60%。

<details>
<summary>完整摘要</summary>

脑-LLM 对齐在英文中已经得到充分证实，但大脑的语言网络在不同语言之间具有神经解剖上的普遍性。那么，这种对齐是否也能跨语言泛化？其变化又由什么因素决定？我们利用来自112名参与者的 fMRI 数据，对英语、中文和法语（Le Petit Prince 语料）进行测试，并比较了7个覆盖英语主导、中文主导和多语架构的 LLM。我们的核心发现是：训练语言的主导性，而非英语作为一种语言的内在属性，决定了对齐模式：一个中文主导模型 Baichuan2-7B（与 LLaMA-2-7B 在架构上匹配）会使梯度完全反转，表现为与中文脑数据对齐最好、与英文最差。除了训练主导性之外，正式的类型学距离也会独立地与对齐退化相关；句法相关脑区 IFG 的类型学梯度比词汇语义相关脑区 PTL 陡 2.3 倍；tokenization fertility 约解释了跨语言最优编码层位移的60%。这些结果表明，表面上的“英文优势”其实是训练数据组成造成的假象，而剩余的差异则反映了集中于句法处理中的真实类型学结构。

</details>

---

### [[20_Research/Papers/大模型/A_Proactive_Multi-Agent_Dialogue_Framework_for_Assessing_Social_Language_Disorder_Traits_in_Autism|A Proactive Multi-Agent Dialogue Framework for Assessing Social Language Disorder Traits in Autism]]

![[assets/2605.22993_figure.jpg|800]]

- **arXiv**: [2605.22993](https://arxiv.org/abs/2605.22993)
- **PDF**: https://arxiv.org/pdf/2605.22993
- **详细分析**: [[20_Research/Papers/大模型/A_Proactive_Multi-Agent_Dialogue_Framework_for_Assessing_Social_Language_Disorder_Traits_in_Autism|A Proactive Multi-Agent Dialogue Framework for Assessing Social Language Disorder Traits in Autism]]
- **作者**: Chuanbo Hu, Minglei Yin, Bin Liu, Wenqi Li, Lynn K. Paul, Shuo Wang, Xin Li
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Agent

#### 研究背景与动机

自闭症谱系障碍（ASD）的临床评估中，社交语言障碍（SLD）相关特征，如回声式重复、代词错位和刻板引用，往往不会在自然对话中直接出现，而是只在特定提问方式下才会被诱发出来。对于结构化访谈而言，这意味着“问什么、怎么问”本身就是影响诊断信息量的关键因素，但这一点在现有自动化评估中常被忽视。本文关注如何借助大模型主动选择更合适的提问策略，以更高效率地暴露这些隐性的语言特征，因此具有明显的临床应用价值。

#### 方法概述和架构

论文提出 TPA（Think, Plan, Ask）多智能体对话框架，用于 ADOS-2 Module 4 的语言评估环节。系统中包含医生智能体、患者智能体和 SLD 特征检测器：医生智能体先在 Think 步骤中判断当前还缺哪些诊断证据，再在 Plan 步骤中从临床上有依据的策略集合里选择最合适的提问策略，最后在 Ask 步骤中生成与该策略和诊断目标一致的定向问题。患者智能体并非简单自由生成，而是基于真实 ADOS-2 临床数据构建，结合概率化的特征触发模型与基于临床片段检索的语言生成器，以模拟不同问题策略下真实患者的语言反应。每一轮对话后，检测到的 SLD 特征会反馈给 TPA Selector，形成持续更新的主动推理闭环，从而逐步缩小诊断缺口。

#### 实验结果分析

作者在 Caltech ADOS Dataset 相关的 484 个对话 episode、35 名患者上进行了评估，并与 6 种对话规划基线及临床真实对话回放进行比较。结果显示，TPA 在所有主要指标上均优于基线，SLD 特征覆盖率达到 82.1%，比由训练有素临床医生进行的真实临床对话自动回放高 16.6 个百分点（65.5%）。在每轮诊断效率方面，TPA 的 AUCC 为 0.628，而对照为 0.458，绝对提升为 +0.170。论文还报告了患者智能体经过三组独立实验验证，能够较好复现真实临床语言特性。

<details>
<summary>完整摘要</summary>

自闭症谱系障碍中的社交语言障碍（SLD）相关特征，包括回声式重复、代词错位以及刻板的媒体引用，通常不会在自然对话中出现，而只会在特定的对话条件下显现出来。在结构化临床评估中，这种“延迟显现”意味着，提问策略的选择是决定一次对话能够获得多少诊断信息的关键因素，但这一点长期以来并未受到足够重视。大语言模型（LLM）能否被引导去主动选择提问策略，从而系统性地诱发这些潜在特征，目前仍然缺乏探索。为此，我们提出 TPA（Think, Plan, Ask），一种主动式多智能体对话框架，并将其应用于自闭症诊断观察量表第二版（ADOS-2）第4模块中的语言评估环节。在该框架中，医生智能体会显式推理哪些特征尚未被观察到，再选择一个临床上有依据的策略并生成针对性问题。患者智能体基于真实 ADOS-2 临床数据构建，使得在不需要真实患者参与的情况下也能进行可重复评估；三项独立实验验证了其与真实患者语言的足够一致性。我们在来自35名患者的484个对话 episode 上对系统进行了评估，结果表明，TPA 在六个竞争性对话规划基线之上，于所有主要指标上均取得更优表现，SLD 特征覆盖率达到82.1%，比由受过训练的临床医生执行的真实临床对话自动回放高16.6个百分点（65.5%），且每轮诊断效率显著更高（AUCC：0.628 对 0.458，绝对提升 +0.170）。这些结果表明，主动式提问策略选择能够显著提升自动化 SLD 特征评估的效率，并对可扩展的 AI 辅助临床筛查具有直接意义。

</details>

---

### [[20_Research/Papers/强化学习/Robots_That_Know_What_to_Ask_Recovering_Misaligned_Rewards_through_Targeted_Explanations|Robots That Know What to Ask: Recovering Misaligned Rewards through Targeted Explanations]]

![[assets/2605.22986_figure.png|800]]

- **arXiv**: [2605.22986](https://arxiv.org/abs/2605.22986)
- **PDF**: https://arxiv.org/pdf/2605.22986
- **详细分析**: [[20_Research/Papers/强化学习/Robots_That_Know_What_to_Ask_Recovering_Misaligned_Rewards_through_Targeted_Explanations|Robots That Know What to Ask: Recovering Misaligned Rewards through Targeted Explanations]]
- **作者**: Helena Merker, Nick Walker, Andreea Bobu
- **cs 子类**: cs.AI, cs.HC, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

在从人类示范中学习奖励函数的机器人任务里，默认前提是示范能够充分覆盖所有关键特征，但现实中人类常因认知负担、动作受限或训练覆盖不足而忽略某些重要维度。这样一来，机器人学到的奖励函数会出现“欠规格化”的空白，部署时可能做出与人类期望不一致甚至不安全的行为。本文聚焦于机器人如何识别自己对哪些特征“不确定”，并主动提出有针对性的问题来补足这些缺失监督，因此很值得具身智能与人机协作方向关注。

#### 方法概述和架构

论文提出 Ambiguity-Sensitive Querying for Reward Learning（ASQ）框架，核心思想是利用示范在不同特征上的方差来判断哪些特征被充分强调、哪些特征可能被欠规格化。方法首先基于初始示范集计算每个特征的轨迹级统计波动，并结合预训练的参考分布，通过贝叶斯模型选择推断哪些特征在示范中获得的监督不足。随后，机器人用自然语言解释自己对这些特征的不确定性，向用户请求专门针对这些特征的纠正性示范。收集到的补充示范会与初始示范合并，并按照特征是否被关注分配不同的理性权重，从而用于恢复更接近真实偏好的奖励参数。整体流程是“检测欠规格化特征—生成解释性查询—获取定向示范—加权重学奖励”，既解决奖励歧义，也让交互更可解释。

#### 实验结果分析

作者在模拟的桌面操作连续 7DoF 机器人任务以及真实 Franka 机器人用户研究中验证了该方法。实验表明，带有特征解释的定向查询比随机提问和被动收集数据更能恢复正确奖励，能够显著减少仅靠不完备示范训练时遗留的歧义。正文节选中没有给出具体数值，但结果明确支持了“先诊断缺失特征、再定向追问”的交互策略优于盲目补数据。

<details>
<summary>完整摘要</summary>

从示范中学习奖励函数时，通常假设示范能够对所有特征——也就是任务相关行为的各个方面——提供充分监督。现实中，示范往往并不完美：由于认知负担或身体动作困难，人类可能会弱化某些特征；或者训练过程未能充分覆盖所有相关情境。在这两种情况下，重要特征都可能被欠规格化，从而导致学到的奖励函数存在歧义，并在部署时出现行为失配。我们提出一个框架，用于检测这类欠规格化特征，并主动请求具有针对性的纠正性示范。我们的关键洞见是：示范会隐式地揭示哪些特征被良好规格化——持续被优化的特征在不同示范之间变化很小，而欠规格化特征则表现出较大波动。我们利用这一统计信号来推断哪些特征可能在示范阶段没有被充分展示。随后，机器人会用自然语言解释其对哪些特征不确定，并请求专门弥补这些缺口的示范。我们在一个模拟的桌面操作领域以及一项使用真实 Franka 机器人的用户研究中评估了该方法。与随机查询和被动数据收集相比，基于解释的定向查询显著提升了奖励恢复效果，减少了原本会在从不完美示范学习中持续存在的歧义。

</details>

---

### [[20_Research/Papers/强化学习/EVE-Agent_Evidence-Verifiable_Self-Evolving_Agents|EVE-Agent: Evidence-Verifiable Self-Evolving Agents]]

![[assets/2605.22905_figure.png|800]]

- **arXiv**: [2605.22905](https://arxiv.org/abs/2605.22905)
- **PDF**: https://arxiv.org/pdf/2605.22905
- **详细分析**: [[20_Research/Papers/强化学习/EVE-Agent_Evidence-Verifiable_Self-Evolving_Agents|EVE-Agent: Evidence-Verifiable Self-Evolving Agents]]
- **作者**: Yamato Arai, Yuma Ichikawa
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Agent, RL

#### 研究背景与动机

面向知识密集型问答的搜索型智能体，不仅要“答对”，还要能够给出可核验的证据支撑答案。现有数据驱动标注成本高，而数据自由的自我演化智能体虽然能自动生成问题并从自身反馈中学习，但如果缺少可验证证据，就可能把流畅却缺乏依据的样本当作训练信号，进而污染整个自生成课程。本文值得关注之处在于，它把“证据可验证性”提升为自我演化搜索智能体的前提，尝试让训练样本从一开始就可审计、可追溯。

#### 方法概述和架构

论文提出 EVE-Agent（Evidence-Verifiable Self-Evolving Agent），是在 proposer–solver 框架上的轻量改造。proposer 不再只生成问题与答案，而是同时生成问题、答案以及一段逐字复制的证据片段，该片段必须来自源文档或检索到的语料。随后，evidence verifier 会比较“只有问题”与“问题+证据”两种情况下 solver 的答案准确率变化，把证据带来的边际提升作为奖励，从而鼓励那些真正有助于回答问题的证据。训练过程中，solver 仍沿用原有搜索工具和优化框架，只是学习在作答时同时输出答案与支撑证据；proposer 则基于证据质量信号更新。整体上，方法不依赖 oracle 答案、人工标注或外部注释，只依赖语料、检索器和模型自身的 rollouts 即可形成可审计训练信号。

#### 实验结果分析

实验在与先前自我演化搜索智能体相同或匹配的设置下进行，对比了此前仅依赖难度奖励的基线。论文报告 EVE-Agent 在 evidence-grounded correctness 上显著优于已有方法，同时也改善了证据质量与答案—证据联合正确性。正文节选未给出具体数值，因此可见文本未给出具体数值。作者还强调，该方法无需更换 backbone model、retriever、search tool 或优化框架，说明收益主要来自奖励设计与证据验证机制本身。

<details>
<summary>完整摘要</summary>

自我演化智能体不应在它们无法自证的样本上进行训练。数据自由的自我演化搜索智能体为构建一种可扩展系统提供了一条可行路径：系统能够自己生成问题、回答问题，并在没有人工标注的情况下，从自身反馈中不断改进。然而，如果缺乏可验证的证据，这一闭环就可能奖励那些流畅却缺乏支撑的样本，从而使自生成课程变成一种不透明且可能不可靠的训练信号。我们认为，对于值得信赖的搜索智能体自我演化而言，证据可验证性是前提条件：每个生成实例不仅应包含答案，还应包含一段来源可追溯的文本片段，而且该片段对答案的贡献应当能够被度量。为此，我们提出 EVE-Agent，即 Evidence-Verifiable Self-Evolving Agent，通过对 proposer–solver 框架进行修改来落实这一原则。proposer 生成问题、答案以及逐字的证据片段；随后，evidence verifier 根据在提供该证据前后 solver 答案准确率的边际提升，对该证据进行奖励。这一机制产生了偏向于真正有助于回答问题的证据的训练信号，同时不需要 oracle 答案、人工标签或外部注释。EVE-Agent 保持 backbone model、retriever、search tool 和优化框架不变。实验表明，EVE-Agent 相比先前的自我演化搜索智能体，显著提升了证据支撑正确性。由此得到的课程不仅是自生成的，而且在构造上就是可审计的：每个训练样本都携带一段可检查的源文本片段，用以解释其为何值得信任。

</details>

---

### [[20_Research/Papers/具身智能/Agentic-VLA_Efficient_Online_Adaptation_for_Vision-Language-Action_Models|Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models]]

![[assets/2605.22896_figure.png|800]]

- **arXiv**: [2605.22896](https://arxiv.org/abs/2605.22896)
- **PDF**: https://arxiv.org/pdf/2605.22896
- **详细分析**: [[20_Research/Papers/具身智能/Agentic-VLA_Efficient_Online_Adaptation_for_Vision-Language-Action_Models|Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models]]
- **作者**: Ruofan Jin, Zaixi Zhang
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.5（加权：具身智能 3，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

Vision-Language-Action（VLA）模型被认为是机器人操作的重要路线，能够利用预训练视觉-语言表征把任务指令转化为动作。但现有训练方式主要依赖模仿学习，往往对新环境泛化不足，而且每个任务都需要大量示范，数据采集成本很高。在线自适应虽能一定程度缓解这一问题，但通常受限于稀疏或噪声奖励、随机探索低效，以及跨任务知识难以复用。

#### 方法概述和架构

论文提出 Agentic-VLA，一种用于 VLA 在线自适应的智能训练框架，核心由三个模块组成：Adaptive Reward Synthesis、Language-Guided Exploration 和 Experience Memory。Adaptive Reward Synthesis 会根据任务描述自动将复杂任务分解为若干子目标，并结合模型当前掌握程度动态调整各子目标的奖励权重，从而形成能力感知的课程学习。Language-Guided Exploration 使用 VLM/critic 生成结构化的自然语言探索建议，替代随机试错式探索，引导模型更系统地尝试动作策略。Experience Memory 则按任务语义保存并检索历史任务中已适应好的策略权重，在遇到相似新任务时用于 warm-start。整体训练流程是：先由记忆模块初始化，再在语言引导下与环境交互，由自适应奖励模块评估轨迹并生成奖励，最后用 GRPO 更新策略，并将成功适应的参数写回记忆库。

#### 实验结果分析

论文在 LIBERO 基准上评估 Agentic-VLA，报告了长时程任务提升 +12.3%、1-shot 学习提升 +28.5%，并且在无需任务特定示范的跨任务迁移中，成功率从 0% 提升到 31.2%。与已有在线自适应方法相比，该框架收敛速度提升 2.4 倍。作者还在双臂 RoboTwin 2.0 基准上验证了方法有效性，即使在随机化的 Hard 设置下仍保持优势。文中进一步通过消融和对照实验说明，这些收益主要来自自适应奖励、语言引导探索与经验记忆的组合设计，而非单一组件或随机种子波动。

<details>
<summary>完整摘要</summary>

视觉-语言-动作（VLA）模型通过利用预训练的视觉-语言表征，已经成为机器人操作的一个很有前景的范式。然而，当前的 VLA 训练方法存在两个关键局限：对新环境泛化能力较弱，以及训练效率低、需要大量示范。为此，我们提出 Agentic-VLA，一种智能体式训练框架，能够通过三项关键创新实现 VLA 的高效在线自适应：（1）自适应奖励合成（Adaptive Reward Synthesis），根据 VLA 当前能力与任务复杂度动态生成并调整奖励函数，将复杂任务分解为可学习的子目标，以支持课程学习；（2）语言引导探索（Language-Guided Exploration），由 critic 模型提供结构化指导，进行系统化探索，而不是随机采样；（3）经验记忆（Experience Memory），存储并检索与任务相关的策略权重，用于在相似任务上进行 warm-start 自适应。我们在 LIBERO 基准上评估 Agentic-VLA，取得了显著提升：长时程任务提升 +12.3%，1-shot 学习提升 +28.5%，并且在没有任务特定示范的情况下，将跨任务迁移成功率从 0% 提升到 31.2%。与现有在线自适应方法相比，我们的框架还实现了 2.4 倍更快的收敛速度。除 LIBERO 外，Agentic-VLA 在双臂 RoboTwin 2.0 基准上也保持了优势，包括其随机化的 Hard 设置。上述结果表明，Agentic-VLA 是向真正可持续学习、可在部署中连续适应的 VLA 系统迈出的重要一步。

</details>

---

### [[20_Research/Papers/大模型/How_Far_Will_They_Go_Red-Teaming_Online_Influence_with_Large_Language_Models|How Far Will They Go? Red-Teaming Online Influence with Large Language Models]]

![[assets/2605.22880_figure.png|800]]

- **arXiv**: [2605.22880](https://arxiv.org/abs/2605.22880)
- **PDF**: https://arxiv.org/pdf/2605.22880
- **详细分析**: [[20_Research/Papers/大模型/How_Far_Will_They_Go_Red-Teaming_Online_Influence_with_Large_Language_Models|How Far Will They Go? Red-Teaming Online Influence with Large Language Models]]
- **作者**: Daniel C. Ruiz, Anna Serbina, Ashwin Rao, Emilio Ferrara, Luca Luceri
- **cs 子类**: cs.AI, cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

随着基于大模型的智能体越来越多地参与网络讨论，如何识别并评估它们被用于政治影响操作的能力，已经成为信息完整性问题中的关键一环。现有工作多关注模型固有的政治偏见，往往只给出某个意识形态位置上的“点估计”，却难以回答模型在对抗性提示下究竟还能被推动到多远。该论文面向更贴近真实滥用场景的本地部署开源模型，因为这类模型更符合隐私敏感、算力受限的恶意使用者在社交媒体环境中的操作约束，因此具有较强的现实意义。

#### 方法概述和架构

论文提出一个用于红队测试的经验框架，用来测量大模型的“Overton Window（OW）”，即模型在争议议题上能够稳定表达的政治观点范围，并考察简单自然语言 jailbreak 如何扩展这一范围。作者构造了一个社交媒体生成任务：给定特定政治立场，要求模型生成不超过 280 字符、尽量具有传播性的帖子，再由自动化裁判为输出与目标立场的匹配程度打分。为此，研究手工整理了覆盖 10 个议题、共 90 条立场声明，并在左—右光谱上以 X0 到 X8 的顺序表示不同政治位置。实验中评估了 31 个指令微调开源/开放权重模型，覆盖 10 个模型家族与 5 个来源国家，同时测试 8 种人类可读、低成本的提示式 jailbreak 及其组合。输出流程是：模型根据目标立场生成帖子，裁判模型在 0 到 9 的 Likert 量表上判断其与目标立场的一致性，若明显跑题或拒答则记为 0；裁判模型通过人工标注筛选，最终采用与人工一致性最高的 Qwen3-30B-A3B-Instruct。

#### 实验结果分析

实验表明，开源大模型在政治表达上存在系统性不对称：它们通常更愿意生成偏左翼的社交媒体内容，而不是偏右翼内容。作者还发现，OW 往往与模型规模呈反向关系，即模型越大，其可被稳定表达的政治范围反而越收缩。不同地区/来源模型之间也存在显著差异，尽管开源生态中的地区代表性并不均衡；同时，不同模型家族对 jailbreak 的敏感性差别很大，说明需要按家族组合选择攻击提示。实验基于 30+ 模型、10 个家族和 5 个国家来源，具体数值在节选中未给出。

<details>
<summary>完整摘要</summary>

随着基于大语言模型（LLM）的智能体越来越多地参与网络公共讨论，针对其支持政治影响活动能力进行红队测试，对于信息完整性而言至关重要。为实现这一目标，我们聚焦于本地部署的开源 LLM，而不是仅通过 API 提供的前沿模型，因为前者更符合在社交媒体环境中部署、且注重隐私的恶意行为者的操作约束。我们提出一个经验性的红队测试框架，用于测量 LLM 的 Overton Window（OW），即模型在争议性话题上能够稳定表达的政治观点范围，并量化简单的自然语言 jailbreak 如何扩展这一范围。我们评估了超过 30 个 LLM，覆盖 10 个模型家族和 5 个来源国家。我们发现政治表达能力存在系统性不对称：开源 LLM 通常更愿意生成偏左翼的社交媒体内容，OW 往往随模型规模增大而反向收缩，并且尽管开源生态中的地区代表性并不均衡，不同地区之间仍存在显著差异。jailbreak 的有效性在不同模型家族之间也有明显波动，这促使我们形成了一套识别有效 jailbreak 组合的工作流程。总体而言，我们的结果建立了一个用于审计开源 LLM 政治可操控性的实用框架，并有助于未来研究者设计更强的防御措施，以对抗由 LLM 驱动的信息影响行动。

</details>

---

### [[20_Research/Papers/大模型/PrefBench_Evaluating_Zero-Shot_LLM_Agents_in_Hidden-Preference_Personalized_Pricing_Negotiations|PrefBench: Evaluating Zero-Shot LLM Agents in Hidden-Preference Personalized Pricing Negotiations]]

![[assets/2605.22855_first_page.png|800]]

- **arXiv**: [2605.22855](https://arxiv.org/abs/2605.22855)
- **PDF**: https://arxiv.org/pdf/2605.22855
- **详细分析**: [[20_Research/Papers/大模型/PrefBench_Evaluating_Zero-Shot_LLM_Agents_in_Hidden-Preference_Personalized_Pricing_Negotiations|PrefBench: Evaluating Zero-Shot LLM Agents in Hidden-Preference Personalized Pricing Negotiations]]
- **作者**: Yingjie Lei
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

个性化定价谈判是检验大模型智能体能力的一个很有代表性的场景，因为智能体即使能够输出合法动作、顺利达成交易，也不一定真的会做出有利润的定价决策。其难点在于，买家的支付意愿、讨价还价风格、耐心程度以及是否会放弃交易等关键因素往往是隐藏的，卖方只能看到有限的公开信息和历史对话。作者认为，这类任务比单纯看“能否成交”更能暴露 LLM agent 在利润敏感决策上的短板，因此值得单独建立基准进行评测。

#### 方法概述和架构

论文提出了 PrefBench，一个基于模拟器的隐藏偏好个性化定价谈判基准。每个回合中，系统将一个模拟买家与固定的车辆定制套餐配对，卖方智能体可以观察到公开的人设描述、套餐信息以及谈判历史，但买家的真实估值、耐心、反报价行为和离场决策由潜变量控制并对智能体隐藏。作者设计了面向 LLM 的状态摘要协议，要求智能体在固定的隐私边界内，仅根据摘要信息输出严格 JSON 格式的行动，从而统一约束输入输出接口并便于自动评测。实验中以零样本方式测试多种 LLM 卖方策略，并在 7,500 个 episode 上与启发式参考策略进行比较。

#### 实验结果分析

实验表明，所测试的 LLM 都能较稳定地遵守协议，且成交率都高于 0.99，说明它们在结构化动作输出和维持谈判推进方面表现可靠。可见文本未给出具体数值，但摘要明确指出，尽管成交率很高，这些模型的卖方利润表现仍然较弱：最好的 LLM 平均利润只略高于随机基线，且明显低于同一 episode 流上的简单让步式启发式策略。整体结果说明，遵循格式规范、倾向达成一致，与真正具备利润意识的谈判能力并不等价。

<details>
<summary>完整摘要</summary>

个性化定价谈判是大模型智能体的一个具有挑战性的测试场景，因为成功互动并不意味着一定能做出有利润的决策。卖方可能生成有效动作并完成许多交易，但如果买家的支付意愿和讨价还价特征仍然是隐藏的，其定价仍可能表现很差。本文提出 PrefBench，一个基于模拟器的隐藏偏好个性化定价谈判基准。每个回合都会将一个模拟买家与一个固定的车辆定制套餐配对；卖方可以观察到公开的人设描述、套餐信息以及谈判历史，而潜在的买家变量则决定其估值、耐心、反报价行为和是否放弃交易。PrefBench 通过一种面向 LLM 的状态摘要协议来评估这一场景，该协议将智能体限制为在固定的隐藏信息边界内返回严格的 JSON 动作。我们在 7,500 个 episode 上评测了零样本 LLM 卖方，并与启发式参考策略进行比较。被测试的 LLM 都能可靠地遵循该协议，且成交率超过 0.99，但它们的卖方利润结果仍然较弱：最好的 LLM 平均利润仅略高于随机基线，并远低于在同一 episode 流上运行的一个简单让步式启发式策略。这些结果表明，结构化动作遵循能力和寻求达成一致的行为，可以与较弱的利润敏感型谈判能力同时存在。PrefBench 为评估隐藏买家偏好下的定价智能体行为提供了一个受控基准。

</details>

---

### [[20_Research/Papers/大模型/RAG4Outcome_A_Retrieval-Augmented_Multimodal_Framework_for_Prognostic_Prediction_in_Chronic_Osteomyelitis|RAG4Outcome: A Retrieval-Augmented Multimodal Framework for Prognostic Prediction in Chronic Osteomyelitis]]

![[assets/2605.22833_figure.png|800]]

- **arXiv**: [2605.22833](https://arxiv.org/abs/2605.22833)
- **PDF**: https://arxiv.org/pdf/2605.22833
- **详细分析**: [[20_Research/Papers/大模型/RAG4Outcome_A_Retrieval-Augmented_Multimodal_Framework_for_Prognostic_Prediction_in_Chronic_Osteomyelitis|RAG4Outcome: A Retrieval-Augmented Multimodal Framework for Prognostic Prediction in Chronic Osteomyelitis]]
- **作者**: Daqian Shi, Pei Han, Jishizhan Chen, Yang Wang, Xiaolei Diao, Xianyou Zheng, Pengfei Cheng
- **cs 子类**: cs.AI, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: Multimodal

#### 研究背景与动机

慢性骨髓炎的预后预测非常困难，因为它具有较高复发风险，且术后恢复过程复杂、个体差异大。临床上常依赖人工评分系统进行评估，但这类方法不仅耗时费力，也难以在不同场景中保持一致性与可扩展性。与此同时，真实世界中的影像报告、EHR 记录和随访文本往往彼此异步、缺失且未对齐，给传统多模态学习带来明显挑战。该工作之所以值得关注，在于它尝试用 RAG 将检索证据、专家知识和多模态病历信息结合起来，面向感染管理与术后决策支持提供更可解释的预后预测。

#### 方法概述和架构

论文提出 RAG4Outcome，这是一个用于慢性骨髓炎预后预测的检索增强多模态框架。输入包括 PET-CT 影像报告、结构化手术/诊断记录以及非结构化随访文本，先由模态特定的信息抽取模块分别处理，转成统一的可读文本块与嵌入表示。随后，系统基于专家定义的 12 个预后指标构造结构化提示，并将患者表示送入检索模块，从由指南、知识图谱、术后结局研究和院内经验等组成的领域语料库中召回相关证据。最终，RAG 生成模块结合患者信息与检索到的证据，输出结构化病情总结及预后等级预测（如 excellent、good、fair、poor），同时给出基于证据的解释。该设计强调在不要求严格模态对齐、且可容忍部分缺失数据的情况下完成推理。

#### 实验结果分析

论文在真实世界的匿名慢性骨髓炎患者数据上进行验证，病例随访跨度为 3–6 年，并设置了病例级评估与消融分析。节选中没有给出具体数值，因此可见文本未给出具体数值。作者报告该方法与临床评分系统具有较高一致性，同时能提供更透明、证据支撑的推理过程。消融与定性分析显示，领域检索和专家引导的预后框架有助于提升临床可解释性与结果可靠性。

<details>
<summary>完整摘要</summary>

慢性骨髓炎由于复发风险高、术后恢复轨迹复杂，给预后评估带来了很大挑战。传统评估往往依赖人工评分系统，这限制了其在临床实践中的可扩展性、效率与一致性。此外，临床数据具有异质性，这也给当前需要对齐输入和大量标注数据的多模态学习方法带来了困难。为此，我们提出 RAG4Outcome，一个用于慢性骨髓炎预后预测的检索增强生成（RAG）框架。我们的方法将多模态临床数据整合到统一的预测流程中，所包含的数据类型有 PET-CT 影像报告、结构化的手术与诊断记录，以及非结构化的随访记录。通过结合领域专属检索语料库与专家引导的提示设计，该框架能够生成更具可解释性、以证据为基础且更符合临床实际的预后判断。基于真实世界病例的初步结果表明，该方法具有良好的效果和临床一致性，显示出 RAG4Outcome 在 AI 辅助感染管理和术后决策支持中的潜力。

</details>

---

### [[20_Research/Papers/大模型/LFRAG_Layout-oriented_Fine-grained_Retrieval-Augmented_Generation_on_Multimodal_Document_Understanding|LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding]]

![[assets/2605.22829_first_page.png|800]]

- **arXiv**: [2605.22829](https://arxiv.org/abs/2605.22829)
- **PDF**: https://arxiv.org/pdf/2605.22829
- **详细分析**: [[20_Research/Papers/大模型/LFRAG_Layout-oriented_Fine-grained_Retrieval-Augmented_Generation_on_Multimodal_Document_Understanding|LFRAG: Layout-oriented Fine-grained Retrieval-Augmented Generation on Multimodal Document Understanding]]
- **作者**: Yifan Zhu, Yu Mi, Yue Lu, Yanchu Guan, Zhixuan Chu
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

多模态检索增强生成（RAG）正在成为提升大模型利用外部知识能力的重要范式，尤其适用于视觉信息密集的文档理解任务，例如说明书、报告、表格与版式复杂的扫描文档问答。现有多模态 RAG 系统大多采用页面级粗粒度检索，往往无法捕捉文档中的细粒度语义与版式结构，容易造成检索不准、上下文冗余，进而影响下游生成质量。因此，这篇工作值得关注的原因在于：它尝试把多模态 RAG 从“按页找信息”推进到“按块找信息”，更贴近真实文档理解场景中的检索需求。

#### 方法概述和架构

论文提出 LFRAG（Layout-oriented Fine-grained Retrieval-Augmented Generation），将检索粒度从页面级提升到块级。方法首先进行版面分割，把文档划分为语义相对完整、布局上连贯的细粒度检索单元，以便更准确地表示局部内容。随后设计语义-版式融合编码器，通过 cross-attention 将局部语义与全局上下文结合起来，使检索表示同时包含内容信息和布局信息。在检索阶段，LFRAG 采用块级 late interaction 机制来对查询与文档块做精细对齐，从而提升相关块的召回并减少无关内容。最终，系统将检索到的更精简、更相关的块级上下文输入生成模块，用于多模态文档问答等下游任务。

#### 实验结果分析

作者构建了 LFDocQA 这一大规模基准，包含块级标注，覆盖多种文档类型，用于同时评测多模态文档检索与问答能力。实验在 LFDocQA 上进行，与现有基线相比，LFRAG 在检索任务上取得了最优表现，并在答案准确率上较最佳基线提升了 7.20%。此外，LFRAG 在生成任务中将 token 消耗减少了 73.07%，说明其不仅更准，也更高效。正文节选中未给出更细的消融或跨数据集结果，可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

多模态检索增强生成（RAG）已经成为一种有效范式，能够借助外部知识增强大语言模型（LLMs）。然而，现有多模态 RAG 系统主要依赖页面级的粗粒度检索，难以捕捉视觉丰富文档中的细粒度语义与版式结构，从而降低检索准确性，并在下游任务中引入冗余上下文。为解决这些问题，我们提出 Layout-oriented Fine-grained Retrieval-Augmented Generation（LFRAG），这是一种新的框架，将多模态 RAG 从页面级推进到块级检索。我们通过版面分割构建语义一致的细粒度检索单元，并设计了一个语义-版式融合编码器，通过 cross-attention 将局部语义与全局上下文结合起来。借助块级 late interaction 检索，LFRAG 能够实现查询与内容的精确对齐，并减少下游生成中的无关内容。为实现严格评估，我们构建了 LFDocQA，这是一个大规模基准，包含块级标注，覆盖多种文档类型，旨在以比现有数据集更细的粒度评测多模态文档检索与问答。大量实验表明，LFRAG 在 LFDocQA 上取得了检索任务的最先进性能，在答案准确率上比最佳基线高 7.20%，并在生成任务中将 token 消耗降低 73.07%，验证了 LFRAG 作为一种面向视觉丰富文档的准确且高效的多模态 RAG 框架的有效性。我们的代码和数据集将很快开源。

</details>

---
