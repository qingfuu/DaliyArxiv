# cs.LG | Machine Learning | 2026-05-25

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/大模型/LLM-driven_design_of_physics-constrained_constitutive_models_two_agents_are_better_than_one|LLM-driven design of physics-constrained constitutive models: two agents are better than one]]

![[assets/2605.23754_figure.png|800]]

- **arXiv**: [2605.23754](https://arxiv.org/abs/2605.23754)
- **PDF**: https://arxiv.org/pdf/2605.23754
- **详细分析**: [[20_Research/Papers/大模型/LLM-driven_design_of_physics-constrained_constitutive_models_two_agents_are_better_than_one|LLM-driven design of physics-constrained constitutive models: two agents are better than one]]
- **作者**: Marius Tacke, Matthias Busch, Kian Abdolazizi, Jonas Eichinger, Kevin Linka, Roland Aydin, Christian Cyron
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

本研究关注如何用大模型自动生成满足物理约束的本构模型，用于描述材料在载荷作用下的变形与响应，这类模型广泛服务于软组织、橡胶等材料的仿真与工程分析。传统方法通常依赖连续介质力学、机器学习和科学编程的多年积累，门槛高、开发周期长；而现有单智能体LLM流程虽然能“按需生成”模型，却缺少系统性的物理校验，容易产出违反热力学、一致性或稳定性约束的结果。因而，如何让LLM不仅会“写模型”，还会“自检模型是否物理可信”，是这篇工作值得关注的核心问题。

#### 方法概述和架构

作者提出首个面向本构模型生成的多智能体LLM方案，采用“Creator + Inspector”的分工架构。Creator代理根据数据提出候选本构模型，目标是尽量贴合实验或合成数据；Inspector代理则对每个候选模型逐项审查9类物理约束，一旦发现违规，就将模型退回给Creator继续修改。该流程以 constitutive artificial neural networks (CANNs) 为实现载体，即让LLM生成可执行的本构网络形式，再由Inspector做物理合法性审核，形成“生成—审查—再生成”的闭环。作者分别使用 Claude Opus 4.7 和 Kimi K2.5 作为底座模型，并在脑组织、实验橡胶和合成橡胶三个基准上测试。推理阶段只有通过Inspector检查的模型才会被导出，从而将“模型可用性”从单纯的拟合精度扩展到物理约束满足程度。

#### 实验结果分析

实验表明，在加入Inspector后，导出的模型中真正满足全部物理约束的比例显著提升：对于 Opus，从91%提升到100%；对于 Kimi，则从37%提升到56%。与此同时，模型的拟合精度基本保持在基线水平附近，并且在未见过的加载路径上表现出较强泛化能力。文中还比较了不同消融设置、Inspector判定可靠性以及迭代修正效果，结论是多智能体分工能更稳定地筛出物理可接受的模型，可见文本未给出具体数值细节。

<details>
<summary>完整摘要</summary>

开发能够刻画材料在载荷作用下如何变形的本构模型，传统上需要在连续介质力学、机器学习和科学编程方面积累多年的专门经验。近期，大语言模型（LLM）已被证明能够降低这一门槛，因为它们可以按需生成本构模型，但现有的单智能体流程缺少系统性的检查，无法保证生成模型满足基本物理定律。为弥补这一缺口，我们提出首个基于LLM的多智能体本构模型生成方法：Creator智能体根据数据提出候选模型，Inspector智能体则针对九项物理约束逐一审查每个提案，并在发现任何违反时将其退回以便进一步修改。我们以 constitutive artificial neural networks (CANNs) 为例展示这一思想，并在脑组织、实验橡胶和合成橡胶上进行基准测试，同时使用两种不同的LLM底座（Claude Opus 4.7 和 Kimi K2.5）。加入Inspector后，导出的模型中真正满足全部物理约束的比例，对于 Opus 从91%提升到100%，对于 Kimi 从37%提升到56%；与此同时，模型精度几乎不低于基线，并且在未见过的加载路径上展现出显著的泛化能力。综合来看，这些生成模型既具有物理有效性，又保持了很高的准确性，并且能够可靠地对训练数据之外进行外推——这些特性使其可直接用于实际应用。将生成与审查分离，因此把LLM驱动的本构建模转变成一个真正可信的过程。该范式刻意保持技术无关性，并会随着LLM能力的提升自动扩展，为自动化、物理感知的模型发现提供了一条很有前景的路径。

</details>

---

### [[20_Research/Papers/强化学习/SeedER_Seed-and-Expand_Retrieval_from_Knowledge_Graphs|SeedER: Seed-and-Expand Retrieval from Knowledge Graphs]]

![[assets/2605.23753_first_page.png|800]]

- **arXiv**: [2605.23753](https://arxiv.org/abs/2605.23753)
- **PDF**: https://arxiv.org/pdf/2605.23753
- **详细分析**: [[20_Research/Papers/强化学习/SeedER_Seed-and-Expand_Retrieval_from_Knowledge_Graphs|SeedER: Seed-and-Expand Retrieval from Knowledge Graphs]]
- **作者**: Hamed Shirzad, Frederik Wenkel, Dominique Beaini, Danica J. Sutherland, Emmanuel Noutahi
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

知识图谱（KG）能够以关系结构丰富地表示知识，适合支撑复杂问答、知识增强检索和推理等任务，但其结构往往不规则，直接做检索很困难：一方面，围绕种子节点做邻域扩展时，候选子图会迅速膨胀；另一方面，纯稠密向量检索又难以处理多跳、组合式查询。现有基于智能体的图搜索方法表达能力较强，但在大规模检索场景中通常代价过高，不利于实际部署。SeedER 关注的正是“如何在控制扩展成本的同时，尽可能找到与查询相关的图节点”，因此具有较强的应用价值。

#### 方法概述和架构

论文提出 SeedER（Seed-and-Expand Retrieval）检索框架，将检索过程拆成“种子选择”和“受控扩展”两步。首先，系统通过轻量级的稠密检索与实体检索，先挑选出一小组核心种子节点，作为后续图搜索的起点。随后，SeedER 使用一个感知图结构的扩展策略，在强化学习训练下，基于当前已选节点与查询信息，选择性地向外扩展图中的候选节点。这样做把全局推理分解为可复用的局部决策，从而在推理时能够逐步发现相关节点，并显式控制每一步的扩展预算。整体上，该方法的输出是一个紧凑但覆盖度更高的候选集合，可作为知识密集型推理系统的第一阶段检索器。

#### 实验结果分析

从摘要可知，作者从理论上分析了稠密检索在组合式图查询上的局限，并从组合泛化与图约束子模优化两个角度说明 SeedER 的优势。实验上，SeedER 在若干强基线之上显著提升了召回率，同时保持候选集规模紧凑，说明其更适合作为大规模知识图谱检索的前置模块。可见文本未给出具体数值，也未提供正文节选中的数据集名称和完整实验设置，但结论明确指向其在高召回、低扩展成本之间取得了更好的平衡。

<details>
<summary>完整摘要</summary>

知识图谱（KG）为关系知识提供了丰富的表示，但其不规则结构使检索变得困难：以自我中心子图为基础的扩展会快速增长，而稠密嵌入方法又难以处理多跳的组合式查询。现有基于智能体的图探索方法虽然表达能力强，但在大规模检索中往往代价过高。我们提出 SeedER（Seed-and-Expand Retrieval），一种显式利用知识图谱结构、通过迭代式低成本扩展实现检索的框架。SeedER 首先通过轻量级的稠密检索和实体检索，种下一个紧凑的核心节点集合，然后借助一个经过强化学习训练的、具备图感知能力的策略对该集合进行选择性扩展。该设计将全局推理分解为可复用的局部决策，使系统能够在严格控制扩展成本的同时，高效发现与查询相关的节点。我们从组合式图查询上的理论局限出发，展示了稠密检索的限制，并从组合泛化与图约束子模优化两个角度建立了 SeedER 的优势。实验上，SeedER 在保持候选集合紧凑的同时，相比强稠密基线和图增强基线显著提升了召回率，使其成为知识密集型推理系统中有效的第一阶段检索器。

</details>

---

### [[20_Research/Papers/强化学习/Learning_Kernel-Based_MDPs_from_Episodic_Preferential_Feedback|Learning Kernel-Based MDPs from Episodic Preferential Feedback]]

![[assets/2605.23650_figure.png|800]]

- **arXiv**: [2605.23650](https://arxiv.org/abs/2605.23650)
- **PDF**: https://arxiv.org/pdf/2605.23650
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Kernel-Based_MDPs_from_Episodic_Preferential_Feedback|Learning Kernel-Based MDPs from Episodic Preferential Feedback]]
- **作者**: Nikola Pavlovic, Sattar Vakili, Qing Zhao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

在强化学习和世界模型场景中，智能体往往拿到的不是精确数值奖励，而是“两个轨迹哪个更好”这类偏好式反馈，这与人类标注、RLHF、机器人控制和推荐系统中的真实交互方式更一致。现有偏好强化学习很多集中在 bandit 或 tabular/linear MDP 设定，往往要么难以扩展到更一般的非线性环境，要么计算上不可行。本文关注 episodic kernel MDP 中仅依赖偏好反馈的学习问题，试图解决“只有每个 episode 一个二元比较信号，如何仍然学到接近最优策略”的理论难题，因此具有较强的基础研究价值。

#### 方法概述和架构

论文研究的是 episodic kernel MDP：每个 episode 中，学习器从同一初始状态出发执行两条策略，最终只收到一个二元偏好标签，标签由 Bradley–Terry–Luce 模型刻画，取决于两条轨迹累计但不可直接观测的回报差。方法上，作者在核函数假设下同时建模奖励与转移，并用基于偏好的价值估计器来从轨迹级比较中恢复价值信息。算法核心包括：用 regularized kernel logistic regression 从偏好中学习奖励成分；用带 Gaussian process 扰动的随机轨迹探索实现 episode 级探索；再结合针对价值函数类的置信集与 covering 论证来构造乐观/不确定性边界。整个流程是：每轮生成两条候选策略并收集偏好标签，更新核化估计器与置信集，再据此选择下一轮探索策略；推理时输出的是在当前置信集下更优的策略。作者还特别调节正则项和覆盖网格参数，以同时控制偏差、方差和复杂度。

#### 实验结果分析

论文给出了首个适用于 kernel MDP 偏好反馈、且对 Matérn kernels 能保证次线性 regret 的算法，并证明其累计 regret 随 episode 数 K 次线性增长，意味着学到的策略价值会收敛到最优策略。作者同时指出该算法可以在关于 K 的多项式时间内实现，因此相较于以往依赖大规模 policy search 的偏好强化学习方法更具可操作性。文中从理论上分析了覆盖数、估计器范数和高斯过程扰动的复杂度控制，但节选部分未给出具体实验数值；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

人类反馈往往以偏好而非经过标定的数值奖励形式出现，这推动了基于偏好反馈的强化学习，也称为基于人类反馈的强化学习（RLHF）。本文对 episodic kernel MDP 中仅依赖偏好的学习进行了严格的理论研究。在每个 episode 中，学习器从同一初始状态出发执行两条策略，并接收一个二元标签，表示哪条轨迹更受偏好；这一过程由 Bradley–Terry–Luce 链接函数对累计（不可观测）奖励差进行建模。在对奖励函数和转移函数采用基于核的假设下（这是最适合理论分析、且最一般的模型之一），我们构建了适用于 episode 结束时比较的偏好型价值估计方法与置信集。我们证明了高概率 regret 上界，其增长速度相对于 episode 数是次线性的，从而意味着所学习策略的价值会收敛到最优策略的价值。

</details>

---

### [[20_Research/Papers/机器人/How_Many_Training_Samples_Are_Needed_for_the_Inverse_Kinematics_Solutions_by_Artificial_Neural_Networks|How Many Training Samples Are Needed for the Inverse Kinematics Solutions by Artificial Neural Networks]]

![[assets/2605.23583_figure.png|800]]

- **arXiv**: [2605.23583](https://arxiv.org/abs/2605.23583)
- **PDF**: https://arxiv.org/pdf/2605.23583
- **详细分析**: [[20_Research/Papers/机器人/How_Many_Training_Samples_Are_Needed_for_the_Inverse_Kinematics_Solutions_by_Artificial_Neural_Networks|How Many Training Samples Are Needed for the Inverse Kinematics Solutions by Artificial Neural Networks]]
- **作者**: Dong-Won Lim
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

逆运动学（IK）是机器人运动规划与控制中的基础问题，直接决定机械臂能否从目标末端位姿反推出可执行的关节角。传统几何法、代数法和 Jacobian 法虽然经典，但在结构建模、奇异位形和参数调校方面都存在局限。近年来，ANN 因具备较强的函数逼近能力和较高的计算效率，被用于学习 IK 映射，但一个关键问题始终没有清楚回答：到底需要多少训练样本，才能让基于 ANN 的 IK 求解既可靠又高效。本文因此聚焦“样本量—精度”关系，对机器人具身智能中的数据效率问题具有直接参考价值。

#### 方法概述和架构

本文研究的是基于前馈神经网络的 IK 近似求解方法，输入为末端执行器在笛卡尔空间中的位置/坐标，输出为对应的关节角。作者先从统计学习与逼近理论出发，建立训练样本数 n 与近似误差之间的关系，并引入带反馈的误差计算：通过正运动学（FK）将网络输出的关节角重新映射回末端位姿，再与目标输入比较得到误差。方法上，论文使用带 ReLU 隐层和线性输出层的前馈 ANN，对不同规模的关节—位置配对样本进行训练，并分析其收敛性、泛化能力以及误差随采样密度变化的规律。为了刻画样本覆盖程度，作者进一步推导了基于 Lipschitz 连续性的上界，并提出与采样间距相关的误差度量，用来说明样本增多后模型效率为何会出现饱和。整体流程是：生成机械臂关节—位置对数据，训练 ANN 学习 IK 映射，推理时由目标末端位姿直接预测关节角，再经 FK 验证预测误差。

#### 实验结果分析

实验在一个 3-DOF 机械臂仿真上进行，比较了不同训练样本规模下的 ANN-I K 求解效果；从正文可见，评估重点包括误差、收敛和泛化表现。结果表明，训练样本数超过 125 后，模型效率与近似精度的提升不再明显，说明继续增加样本带来的收益有限。论文还强调其理论推导与具体网络结构无关，因而具有一定的通用性；但节选中未给出与具体基线方法对比的详细数值，可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

逆运动学（IK）在机器人运动规划与控制中起着关键作用。机器臂的 IK 求解可以通过几何法、代数法或 Jacobian 法等传统方式完成，但这些方法各有缺点。由于人工神经网络（ANN）具有良好的泛化能力和计算效率，已成为逼近 IK 解的一种有前景的替代方案。这种方法本质上只用少量为 IK 问题求解而记录的末端执行器样本进行训练。然而，一个根本性问题仍然存在：需要多少训练样本才能获得可靠且准确的 IK 预测？本研究探讨了训练数据规模与基于 ANN 的 IK 求解器精度之间的数学关系。以一个关节式机器人机械臂为例，我们生成不同数量的关节—位置对来训练前馈神经网络，并评估其精度、收敛性和泛化能力。结果表明，训练样本超过 125 后，并未进一步提升模型效率这一与采样规模相关的近似精度指标，从而为数据效率提供了有价值的见解。本文为优化 ANN 方案的数据规模提供了实践指导，有助于在真实机器人应用中平衡计算成本与模型精度。

</details>

---

### [[20_Research/Papers/大模型/Push_Your_Agent_Measuring_and_Enforcing_Quantitative_Goal_Persistence_in_Long-Horizon_LLM_Agents|Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents]]

![[assets/2605.23574_figure.png|800]]

- **arXiv**: [2605.23574](https://arxiv.org/abs/2605.23574)
- **PDF**: https://arxiv.org/pdf/2605.23574
- **详细分析**: [[20_Research/Papers/大模型/Push_Your_Agent_Measuring_and_Enforcing_Quantitative_Goal_Persistence_in_Long-Horizon_LLM_Agents|Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents]]
- **作者**: Yuandao Cai, Yuzhang Zhu, Liyou Gao, Wensheng Tang, Shengchao Qin
- **cs 子类**: cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

长链路大模型智能体在搜索、收集证据、处理数据和操作仓库时，往往能做出很多看似合理的局部动作，但仍可能在目标数量尚未完成时过早停止。对于这类“必须凑够 N 个有效结果才算完成”的任务，真正的难点不只是单步能力，而是能否持续维护已验证进度，直到外部验收条件被满足。作者指出，传统最终成功率容易掩盖重复工作、重复提交、虚假完成和进度漂移等问题，因此有必要单独研究“定量目标持续性”（QGP）。这项工作值得关注，因为它把智能体可靠性从“会不会做”推进到“能不能一直做到做完”。

#### 方法概述和架构

论文提出 Quantitative Goal Persistence（QGP）作为评测目标，核心定义是：智能体是否会持续工作，直到外部验证器确认至少 N 个不同且有效的工作单元。基于这一设定，作者构建了 PushBench，一个面向可审计进度的基准框架，包含两类任务：QGP-RepoScan 用于仓库工件检索，QGP-DataOps-lite 用于带验证器的工作单元处理。框架中的每个任务都明确给出目标、计数阈值、预算和验证规则，所有已接受项都由验证器记录，从而把重复提交、虚假完成、过早停止和报告计数错误都转化为可直接测量的失败模式。论文还设计了两类持久性控制器：StateQGP 通过维护已提交标识、重复搜索页和完成资格等外显状态来支持检索任务；UnitQGP 则跟踪待处理、已尝试和已通过的单元，用于约束带验证器的工作单元任务。除此之外，作者还比较了被动式控制、验证器门控控制和记忆型基线，并进一步做了编码风格与黑盒前沿智能体评测，以检验这些进度约束在更真实场景中的泛化能力。

#### 实验结果分析

实验在仓库扫描和数据操作两类任务上进行，比较了状态跟踪控制器、标准控制器、验证器门控控制器以及记忆型基线，并使用成功率、重复提交、虚假完成和进度偏移等指标评估。结果显示，在仓库检索任务中，StateQGP 在匹配设置下可达到 69%–78% 的成功率，同时消除了重复提交；在工作单元任务中，UnitQGP 可达到 25%–50% 的成功率，而标准控制器和完成门控控制器在该设置下一个任务实例都无法完成。黑盒前沿模型 Claude Code（Sonnet 4.6）与 Codex CLI（gpt-5.4）在 50 个工件的任务上表现较好，但当目标提升到 100 个工件时，每种条件下都只剩 9 个任务中的 3 个成功。整体结论是：定量目标会暴露出不同于局部任务能力的可靠性瓶颈，关键不只是做对一步，而是要维持经验证的进度并且只在任务真正完成后停止。

<details>
<summary>完整摘要</summary>

长链路语言智能体可以完成许多看似合理的局部工具调用，但在请求的数量实际上尚未完成时，仍可能无法持续推进。我们将这一差距定义为定量目标持续性（Quantitative Goal Persistence，QGP）：即智能体是否会一直工作，直到外部验证器确认已有足够多的不同有效条目。PushBench 将这一问题转化为一个基准，用于仓库工件收集和带验证器的工作单元评测，因此重复工作、重复提交、虚假完成和进度漂移都能够被直接测量，而不是被最终成功标志所掩盖。在配对控制器比较中，状态跟踪型检索控制器可达到 69%–78% 的成功率，并且消除了重复提交；在某些设置下，标准控制器与完成门控控制器无法完成任何任务实例，而背包跟踪型工作单元控制器可达到 25%–50% 的成功率。对前沿黑盒智能体的评测显示，Claude Code（Sonnet 4.6）和 Codex CLI（gpt-5.4）在 50 个工件的任务上可以解决很多实例，但在 100 个工件时，每种条件下都降至 9 个任务中的 3 个成功。结果表明，定量目标考验的是一种不同于局部任务能力的可靠性要求：智能体必须维持经验证的进度，并且只能在请求的工作真正完成后停止。

</details>

---

### [[20_Research/Papers/世界模型/Learning_partially_observed_systems_with_neural_Hamiltonian_ordinary_differential_equations|Learning partially observed systems with neural Hamiltonian ordinary differential equations]]

![[assets/2605.23510_figure.png|800]]

- **arXiv**: [2605.23510](https://arxiv.org/abs/2605.23510)
- **PDF**: https://arxiv.org/pdf/2605.23510
- **详细分析**: [[20_Research/Papers/世界模型/Learning_partially_observed_systems_with_neural_Hamiltonian_ordinary_differential_equations|Learning partially observed systems with neural Hamiltonian ordinary differential equations]]
- **作者**: Sunniva Meltzer, Sølve Eidnes, Alexander Johannes Stasik
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.52（加权：强化学习 0.16，世界模型 0.36）
- **关联关键词**: WorldModel, Systems

#### 研究背景与动机

《Learning partially observed systems with neural Hamiltonian ordinary differential equations》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When learning dynamical systems from data, embedding physical structure can constrain the solution space and improve generalization, but many physics-informed models assume access to the full system state. This limits their use in partially observed settings, where some state variables are completely unobserved and must be inferred without direct supervision. Here, we present neural Hamiltonian ordinary differential equations (NHODE), a framework that combines Hamiltonian neural networks (HNNs) with neural ordinary differential equations (neural ODEs) to learn partially observed dynamical systems from data. The Hamiltonian structure enforces energy conservation by construction, while the neural ODE framework enables a flexible training procedure that allows the loss to be defined only on observed variables. We also incorporate additional physical constraints through symmetry-aware coordinate transformations and separable energy formulations. The framework is evaluated on systems of increasing complexity, from linear and nonlinear mass-spring systems to the chaotic three-body problem. Across all examples, increasing the amount of embedded physical structure improves the accuracy and long-horizon stability of the predictions. Even in the most challenging regimes, the NHODE framework captures both observed and latent dynamics, whereas purely data-driven baselines become unstable.

</details>

---

### [[20_Research/Papers/强化学习/WMAttack_Automated_Attack_Search_for_Adversarial_Evaluation_of_World-Model_Agents|WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents]]

![[assets/2605.23220_figure.png|800]]

- **arXiv**: [2605.23220](https://arxiv.org/abs/2605.23220)
- **PDF**: https://arxiv.org/pdf/2605.23220
- **详细分析**: [[20_Research/Papers/强化学习/WMAttack_Automated_Attack_Search_for_Adversarial_Evaluation_of_World-Model_Agents|WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents]]
- **作者**: Zhixiang Guo, Siyuan Liang, Shi Fu, Cheng Guo, Andras Balogh, Mark Jelasity, Dacheng Tao
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.12（加权：大模型 0.4，强化学习 0.16，世界模型 0.56）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

世界模型正越来越多地被用作决策代理，但它们在对抗扰动下是否稳定、是否容易被“小预算攻击”击穿，仍缺少系统性的自动化评估方法。现有做法要么依赖人工调参，容易因攻击过弱而高估鲁棒性；要么进行穷举搜索，但由于每个候选配置都要经过闭环 rollout 和潜在动力学计算，代价极高。该论文关注的是如何在有限评估预算下，自动找到更强的攻击配置，从而更真实地暴露 world-model agents 的脆弱性，这一问题对安全评测与鲁棒性研究都很重要。

#### 方法概述和架构

论文提出 WMAttack，将 world-model agent 的对抗评估建模为一个有限预算下的攻击配置搜索问题。攻击配置不仅包含攻击类型，还包括扰动预算、优化步数、重启次数、自适应步长参数、随机种子和资源分配规则等。方法由两个核心模块组成：RGAR（Representation-Guided Attack Retrieval）和 SCAS（Self-Correcting Attack Search）。其中，RGAR 会先根据新任务/新模型的表示特征，从历史攻击记忆中检索与其表示相似、且曾经有效的配置，作为搜索的 warm start；SCAS 则在每轮评估后，利用 reward 下降、动作不稳定性、运行时间和 rollout 波动等反馈，持续修正攻击提议分布，把搜索概率逐步集中到更高效的攻击区域。整体流程是先初始化再迭代优化：RGAR 负责缓解冷启动，SCAS 负责在有限预算内自适应放大高价值攻击配置的采样概率，从而提高搜索效率与攻击强度。

#### 实验结果分析

作者在 Atari 和 DeepMind Control（DMC）任务上验证了 WMAttack，并与随机搜索及 Claudini 风格的自动攻击搜索基线进行了比较。结果显示，WMAttack 能持续找到更强的攻击，在 DreamerV3 Atari 上将归一化 reward drop 从 0.497 提升到 1.034，在 DMC 上从 0.319 提升到 0.682。消融实验进一步表明，RGAR 能提高初始候选质量，SCAS 能在固定评估预算下提升最终攻击效用；此外，论文还报告了跨模型泛化实验（如 DreamerV2、TD-MPC2、IRIS），整体结论是该方法具有较好的迁移能力。

<details>
<summary>完整摘要</summary>

尽管世界模型作为决策代理的使用日益增长，但由于缺乏专门的自动化评估方法，它们的对抗鲁棒性仍缺少系统研究。攻击评估面临一个关键障碍：它既要准确又要高效；过弱的手工调参攻击会高估鲁棒性，而穷举式超参数搜索的成本又高得难以承受，因为每个候选方案都需要通过学习到的潜在动力学进行闭环 rollout。为此，我们提出 WMAttack，这是一种用于世界模型代理对抗评估的自动化攻击搜索框架。WMAttack 将鲁棒性评估形式化为一个有限预算下的攻击配置搜索问题，所搜索的对象包括攻击族、扰动预算、优化步数、重启次数以及资源分配规则等。为了提高搜索准确性，Self-Correcting Attack Search（SCAS）利用 reward 下降、动作不稳定性、运行开销和 rollout 波动的反馈来细化攻击提议分布。为了提高搜索效率，Representation-Guided Attack Retrieval（RGAR）从表示相似的任务中检索有效的历史配置，为未见过的环境提供 warm start。我们给出了一个理论解释：当提议分布把概率质量转移到高效用攻击上时，提议细化能够改进有限预算搜索。我们在 Atari 和 DeepMind Control 任务上验证了该方法，WMAttack 相比所评估的基线持续发现更强的攻击，在 DreamerV3 Atari 上将归一化 reward drop 从 0.497 提升到 1.034，在 DMC 上从 0.319 提升到 0.682。消融实验进一步表明，RGAR 提高了初始候选质量，而 SCAS 在固定评估预算下提升了最终攻击效用。

</details>

---

### [[20_Research/Papers/强化学习/Pure_Exploration_for_a_Good_Policy_in_Reinforcement_Learning_with_Bandit_Feedback|Pure Exploration for a Good Policy in Reinforcement Learning with Bandit Feedback]]

![[assets/2605.23182_figure.png|800]]

- **arXiv**: [2605.23182](https://arxiv.org/abs/2605.23182)
- **PDF**: https://arxiv.org/pdf/2605.23182
- **详细分析**: [[20_Research/Papers/强化学习/Pure_Exploration_for_a_Good_Policy_in_Reinforcement_Learning_with_Bandit_Feedback|Pure Exploration for a Good Policy in Reinforcement Learning with Bandit Feedback]]
- **作者**: Zitian Li, Wang Chi Cheung
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

这篇工作研究的是强化学习中的纯探索问题，但关注点不再是寻找“最优策略”，而是找出一个“足够好”的策略：只要某个策略的期望回报超过预设阈值 μ0，就认为满足目标。这样的设定更贴近很多实际场景，例如医疗决策、云资源调度和投资策略筛选，往往只需要验证方案是否达到基准线，而不一定要找出全局最优。现有纯探索研究主要集中在 Best Policy Identification (BPI) 或 ε-PI，直接应用到阈值式目标时会遇到阈值未知、下界不适配等问题，因此这篇论文提出了新的 Good Policy Identification (GPI) 方向，值得关注。

#### 方法概述和架构

作者将 GPI 形式化为固定置信度问题：算法需要在置信度至少 1-δ 的前提下，要么输出一条期望回报不低于 μ0 的策略，要么在不存在此类策略时输出 None。为此提出了 BEE-GPI（Balanced Exploration-Exploitation for Good Policy Identification），它按阶段运行，每一阶段先进行自适应探索，用来估计转移概率 P 和初始分布 p，并尝试给出候选策略。随后算法进入分支判断：若当前信息已足够则直接终止，若候选策略还未完成验证则进入利用/评估阶段，否则继续下一阶段。整体上，BEE-GPI 将“探索”和“策略验证”耦合起来，并且利用 early-stopping 的 BPI 子程序作为 oracle 以提高样本效率。

#### 实验结果分析

论文给出了 BEE-GPI 在正实例和负实例上的样本复杂度上界，并证明其对 GPI 问题是近乎最优的。尤其在正实例中，样本复杂度中 log(1/δ) 的系数为 O(H^2/(V*-μ0)^2)，且不再显式依赖状态空间和动作空间大小，这一点相较 BPI 设定有明显区别。作者还建立了下界结果，说明 1/(V*-μ)^2 这一项是必要的，实验部分也验证了方法的效率；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

纯探索在分集强化学习中的研究主要集中于最佳策略识别（Best Policy Identification, BPI），其目标是在高置信度下识别一条（近）最优策略。受现实场景启发，在很多应用中只要“足够好”的策略即可，我们研究另一类目标——Good Policy Identification (GPI)。对于给定的奖励阈值 μ0，GPI 只要求：如果确实存在某条策略的单回合期望回报至少为 μ0（即正实例），就识别出这样一条策略；如果不存在这样的策略（即负实例），则输出 None。我们在固定置信度设定下形式化 GPI 问题，要求输出以至少 1-δ 的概率正确，并希望最小化期望样本复杂度，即为得到输出所探索的期望回合数。我们提出了一种新算法 BEE-GPI，并针对正实例和负实例推导了具有理论保证的样本复杂度上界。值得注意的是，对于正实例，我们上界中 log(1/δ) 的系数为 O(H^2/(V*-μ0)^2)，其中 H 是回合长度，V* 是单回合最优期望回报；该系数在其他方面不依赖动作空间和状态空间大小，这与 BPI 中的样本复杂度形成鲜明对比。我们进一步给出下界结果，表明 BEE-GPI 近乎最优，同时也说明了 1/(V*-μ)^2 项的必要性。数值实验进一步验证了我们方法的有效性。

</details>

---

### [[20_Research/Papers/大模型/PACE_Two-Timescale_Self-Evolution_for_Small_Language_Model_Agents|PACE: Two-Timescale Self-Evolution for Small Language Model Agents]]

![[assets/2605.23019_figure.png|800]]

- **arXiv**: [2605.23019](https://arxiv.org/abs/2605.23019)
- **PDF**: https://arxiv.org/pdf/2605.23019
- **详细分析**: [[20_Research/Papers/大模型/PACE_Two-Timescale_Self-Evolution_for_Small_Language_Model_Agents|PACE: Two-Timescale Self-Evolution for Small Language Model Agents]]
- **作者**: Chen Ling, Pei Chen, Albert Guan, Jiaming Qu, Shayan Ali Akbar, Madhu Gopinathan, Erwin Cornejo
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

在生产环境中部署语言模型智能体，往往需要大量算力和人工反复调参，包括提示词、解析器、校验器以及其他控制组件。现有自我演化方法虽然有望减少人工干预，但多数默认能够调用很强的前沿模型来诊断失败、提出修改并判断更新是否有效，这一假设在资源受限的小语言模型场景下并不稳健。本文聚焦冻结的小语言模型智能体，讨论在不更新模型权重、也不依赖前沿模型教师的情况下，能否实现可靠的自我进化，因此具有较强的实际部署价值。

#### 方法概述和架构

论文提出 PACE（Prompt And Control Logic Evolution），核心思想是用“两时间尺度”协调低风险的提示词优化与高风险的控制逻辑更新。系统首先在固定控制逻辑下反复进行 prompt evolution，通过失败分析、手工扰动、反思式改写和交叉组合等方式生成提示词候选，并在小批训练集上以准确率与 token 成本的权衡进行筛选。当前一阶段的提示词收益开始饱和后，控制器再进入 constrained control-logic evolution：由小模型提出受限的结构性修改，例如解析、验证、重试、路由或采样策略的调整。这里采用“先提案、后验证”的机制，结构更新只有在留出验证集上优于当前方案且满足资源预算时才会被提交；每次接受更新后，再回到提示词优化阶段继续迭代。整体上，PACE 的输出不是单一最终解，而是一个在提示词与控制逻辑之间动态切换、并通过验证门控的自适应推理策略。

#### 实验结果分析

作者在 4 个受控基准上、3 个冻结 SLM 骨干上进行了实验，模型规模从 4B 到 14B；基准包括 MMLU、IFEval、HotpotQA、MGSM，另有 tau-bench 作为多轮工具调用案例。与 vanilla SLM 智能体以及更强的单模式演化基线相比，PACE 在全部 12 组“骨干模型—基准”组合上都取得最佳结果；相对 vanilla SLM 的提升最高达到 +9.2%，相对单模式演化基线的提升最高达到 +5.4%。文中还给出 tau-bench 案例研究，显示 PACE 能进一步提升多轮工具使用成功率；消融与分析也支持其“两阶段切换+验证门控”的设计，但节选中未给出更细的具体数值。

<details>
<summary>完整摘要</summary>

在生产环境中部署语言模型智能体，通常需要投入大量算力和人工精力来调试提示词、解析器、验证器以及智能体流水线中的其他组件。自我演化提供了一种有前景的替代方案，但现有大多数框架都假设可以访问前沿模型，这些模型能够可靠地诊断失败、提出修改建议，并评估自己更新是否有效。本文研究在资源受限条件下，冻结的小语言模型（SLM）是否能够作为有效的自我演化智能体。我们提出 PACE（Prompt And Control Logic Evolution），一种两时间尺度框架，用于协调低风险的提示词改进与高风险的控制逻辑更新。PACE 会在固定控制逻辑下演化提示词，直到提示词层面的收益趋于饱和；随后再考虑受限的控制逻辑更新，并通过留出验证来决定是否接受。作者在 3 个冻结的 SLM 骨干模型上进行了实验，模型规模从 4B 到 14B，并在 4 个受控基准上评估。结果显示，PACE 在全部 12 组骨干模型—基准组合上都取得了最佳性能，相比原始 SLM 智能体，最高可获得 +9.2% 的相对提升；相比更强的单模式演化基线，最高可获得 +5.4% 的相对提升。tau-bench 的案例研究进一步表明，PACE 能提升多轮工具使用的成功率，优于原始方法和仅提示词演化的方法。这些结果说明，即使不更新模型权重、也不依赖前沿模型教师，冻结 SLM 仍然可以实现可靠的智能体自我演化；其关键收益并不在于某一种最终求解器模式，而在于能够自主、经过验证地发现适合任务的推理策略。

</details>

---

### [[20_Research/Papers/机器人/Active_Sensing_Subserves_Task-Level_Control|Active Sensing Subserves Task-Level Control]]

![[assets/2605.22988_figure.png|800]]

- **arXiv**: [2605.22988](https://arxiv.org/abs/2605.22988)
- **PDF**: https://arxiv.org/pdf/2605.22988
- **详细分析**: [[20_Research/Papers/机器人/Active_Sensing_Subserves_Task-Level_Control|Active Sensing Subserves Task-Level Control]]
- **作者**: Andrew Lamperski, Debojyoti Biswas, Eric S. Fortune, John Guckenheimer, Kathleen Hoffman, Noah J. Cowan
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

这篇论文关注机器人与具身智能中的“主动感知”问题：系统并非只依赖静态传感器读数，而是通过自身运动来主动塑造感知反馈，从而完成控制任务。作者指出，传统观点往往把主动感知理解为“为了获取信息而移动”，例如降低不确定性；但在真实生物系统中，主动感知可能并不是信息目标驱动，而是任务级反馈控制的必然产物。由于生物传感器常具有适应性，且传感与运动紧密耦合，工程系统若仍沿用经典的估计—控制分离范式，往往难以复现动物那种鲁棒而灵巧的行为，因此这项工作对机器人感知与控制设计具有启发意义。

#### 方法概述和架构

论文以控制理论为主线，提出“主动感知服务于任务级控制”的解释框架，并将其形式化到含适应性传感器的闭环控制系统中。作者从弱电鱼的跟踪任务出发，构建了一个简化的二阶模板模型：状态由位置和速度组成，控制输入对应鱼体节点位置偏移；同时加入一个适应性传感模型，使传感器输出近似为刺激的时间导数，从而体现对恒定或缓慢变化信号的抑制。基于该模型，论文分析了在几何与动态感知约束下，单纯依赖任务目标的闭环控制为何会自然诱发自发运动，这些运动并非直接完成任务，而是用于改善可观测性并维持稳定控制。进一步地，作者从动物数据中归纳出“探索—利用”两种行为模式：探索模式通过较强动态运动主动塑造感知反馈，利用模式则通过较慢的补偿运动直接逼近任务目标；系统在两种模式间快速切换，形成一种模式切换控制策略。论文还将这一策略与工程中的 persistent excitation 和 separation principle 对比，强调在适应性传感器条件下，传统分离设计往往不再适用。

#### 实验结果分析

从生物学证据与数学理论两方面看，论文支持了“主动感知由控制需求涌现”的观点，而不仅仅是信息获取驱动。作者在弱电鱼 refuge tracking 任务及跨物种时间序列重分析中发现，动物会在离散时间段内切换探索与利用两种模式，这与主动感知行为的经验特征一致。文中还指出，在仿真中，这种模式切换策略相较于经典 persistent excitation 方法能够带来更低的 tracking error 和更少的控制能量；但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

主动感知通常被定义为为了获取信息而付出的能量消耗，通常表现为运动。本文提出，依赖适应性传感器、运动与感知之间的耦合，以及任务级控制三者结合在一起，必然会催生主动感知运动的出现。换言之，主动感知并不是由感知目标所驱动，例如最小化对系统状态的不确定性，而是任务级控制所必需的。我们认为“主动感知服务于控制”这一假设，既得到生物体经验数据的支持，也得到数学理论的支持。值得注意的是，主动感知行为常常以离散时间段的形式出现，并与目标导向行为交替进行。这表明动物会在两种具有不同控制策略的行为模式之间切换：一种是“探索”模式，动物通过动态运动来塑造感知反馈；另一种是“利用”模式，动物通过更缓慢的补偿性运动直接实现任务目标。依赖适应性传感器、主动感知以及模式切换的这种反馈控制策略，在生物系统中极为普遍，但在工程系统中并不常见。尽管由最先进的传感器、执行器和机械设计构成的工程系统，在最大力输出、精度和速度等“代价函数”上可能优于动物，但动物仍然能够稳定而优雅地完成行为，而这目前仍是工程系统难以企及的，这说明现有控制系统仍不充分。用控制理论语言表达的这些洞见，可能对改进机器人感知与控制至关重要。

</details>

---

### [[20_Research/Papers/大模型/MARGIN_Runtime_Confidence_Calibration_for_Multi-Agent_Foundation_Model_Coordination|MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination]]

![[assets/2605.22949_figure.png|800]]

- **arXiv**: [2605.22949](https://arxiv.org/abs/2605.22949)
- **PDF**: https://arxiv.org/pdf/2605.22949
- **详细分析**: [[20_Research/Papers/大模型/MARGIN_Runtime_Confidence_Calibration_for_Multi-Agent_Foundation_Model_Coordination|MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination]]
- **作者**: Joss Armstrong
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

在多智能体大模型系统中，协调器需要在多个 agent 的回答之间选择最可信的结果，而常见做法是直接依据各 agent 自报的置信度进行加权或路由。问题在于，大模型的置信度往往并未校准，甚至在困难任务上会出现“越不确定却越自信”的反转现象，导致协调器更容易选错答案。现有温度缩放、Platt scaling、直方图分箱等设计时校准方法只是在离线数据上学一个固定修正，遇到分布漂移就会明显失效。因而，如何在不访问模型内部、不中断部署流程的前提下，对多智能体置信度进行运行时校准，成为这篇论文值得关注的核心问题。

#### 方法概述和架构

论文提出 MARGIN（Multi-Agent Runtime Grading via Incremental Normalisation），一种面向多智能体基础模型协调的在线置信度校准方法。它把每个 agent 的置信度按区间分桶，对“agent-置信度区间”分别维护校准因子，并根据任务流中不断到来的真实结果持续更新，而不是依赖离线验证集。更新机制采用对称的 EWMA（指数加权移动平均），以同时追踪最新分布变化并抑制噪声；在冷启动阶段再结合 Bayesian shrinkage blending，避免样本过少时估计过于不稳定。方法输入是 agent 的预测、其自报置信度以及最终是否正确的反馈，输出是校准后的置信度权重，可直接用于多智能体选择、投票或路由。整套流程不需要 logits、权重或额外训练，超参数只有 3 个且作者给出稳健默认值。

#### 实验结果分析

作者在 19 个基础模型、8 个基准和 5 万余条观测上评估了 MARGIN，覆盖代码生成、问答和数学等任务。结果显示，在明显分布漂移下，MARGIN 的校准误差显著低于最优的设计时基线，ECE 可降低 3–6 倍；在中等漂移下也大致能把最优基线的误差减半。对于多智能体选择，原始自报置信度在困难基准上的成对判别能力低于随机水平，而 MARGIN 可将其修正到明显高于随机的区间，并在 4 个基准中的 3 个上超过“始终选择最优模型”的 oracle。消融实验还表明，对称更新明显优于非对称更新，支持作者关于非策略性 agent 应使用对称校准的理论分析。

<details>
<summary>完整摘要</summary>

随着基础模型 agent 越来越多地部署到多智能体环境中，协调器必须决定应当信任哪一个 agent 的回答。标准做法是按 agent 自报的置信度进行加权，但近期证据表明，基础模型的置信度存在系统性失配，并且在困难任务上与准确率呈反相关。设计时校准方法（如 temperature scaling、Platt scaling、histogram binning）无法解决这一问题，因为它们是在留出数据上拟合一个固定修正，在分布漂移下会退化。我们提出 MARGIN（Multi Agent Runtime Grading via Incremental Normalisation），这是一种在线校准方法，它从任务流本身学习每个 agent、每个置信度区间的校准因子，无需模型访问、无需留出数据、无需重新训练。MARGIN 使用对称的指数加权移动平均，并结合 Bayesian shrinkage 融合，只有 3 个超参数且默认值稳健。基于 19 个基础模型、8 个基准和 5 万余条观测，MARGIN 在分布漂移条件下达到比最佳设计时基线低 3–6 倍的校准误差。在多智能体选择中，原始口头置信度在困难基准上的成对判别结果甚至低于随机水平（45–56%）。MARGIN 完全纠正了这一问题，将成对判别提升到 70–89%，并在 4 个基准中的 3 个上超过了“始终选择最佳模型”的 oracle。六个形式化命题刻画了该方法的收敛性、跟踪速度，以及对非策略性 agent 来说对称更新的最优性，所有理论预测都得到了实验验证。

</details>

---

### [[20_Research/Papers/大模型/From_Residuals_to_Reasons_LLM-Guided_Mechanism_Inference_from_Tabular_Data|From Residuals to Reasons: LLM-Guided Mechanism Inference from Tabular Data]]

![[assets/2605.22897_figure.png|800]]

- **arXiv**: [2605.22897](https://arxiv.org/abs/2605.22897)
- **PDF**: https://arxiv.org/pdf/2605.22897
- **详细分析**: [[20_Research/Papers/大模型/From_Residuals_to_Reasons_LLM-Guided_Mechanism_Inference_from_Tabular_Data|From Residuals to Reasons: LLM-Guided Mechanism Inference from Tabular Data]]
- **作者**: Mohammad R. Rezaei, Rahul G. Krishnan
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

科学类表格数据建模常常面临一个两难：一方面需要较高的预测精度，另一方面又希望模型能够解释“为什么会这样”。现有的统计学习模型在结构化数据上表现强，但通常是黑箱；而常见可解释方法更多回答“哪些特征重要”，却难以进一步说明特征如何交互、以及如何在迭代中修正解释。本文关注的是如何让大模型不直接从零预测目标值，而是围绕基础模型的“残差”去补足其遗漏的结构，从而同时获得更好的预测与更接近机制的解释，这一点对科学发现、生物医药和社会经济等场景都很有价值。

#### 方法概述和架构

论文提出 Multi-Agent Residual In-Context Learning（MARICL）。其核心思路是先用一个基础模型（如线性回归、XGBoost 等）负责主预测，再计算训练样本上的残差，挑选高残差样本作为大模型的上下文输入，让 LLM 只回答“基础模型缺了什么”。MARICL 由多个 agent 组成：编码器 agent 从高残差样本中归纳结构化假设，解码器 agent 将假设转换为可执行的修正项和对应自然语言描述；随后通过多轮 textual gradient optimization，让模型依据批评反馈不断修正公式。最终，系统把多个修正项按与查询样本相关的权重进行聚合，并加到基础模型输出上，形成最终预测；分类任务中则将基础模型概率与修正后的类别分布按权重融合。

#### 实验结果分析

作者在九个覆盖科学、生物医学、社会经济和合成数据的基准上评估 MARICL，结果显示它在所有数据集上都能稳定优于对应基础模型。文中还在 Cell-Free Protein 数据集上做了跨批次冻结公式实验：在相同试剂协议下，冻结后的修正公式无需再训练、也无需再次调用 LLM，就能在超过 92% 的情况中提升预测；而跨到不同协议时则会系统性失效，说明学到的不是批次噪声，而是与生化机制一致的可泛化结构。节选内容还显示，作者进行了消融与合成数据实验来检验数据驱动修正与先验知识的贡献，可见文本未给出所有细节数值。

<details>
<summary>完整摘要</summary>

科学应用中的机器学习长期面临一个持续挑战：如何同时实现预测与理解。统计模型在结构化数据上表现出色，但通常是黑箱；而现有可解释性方法大多偏于“检查式”分析：它们回答“哪些特征重要？”，却无法说明特征如何相互作用，也不能在与人的理解共同迭代的过程中不断修正解释。若直接让 LLM 预测目标值，它必须搜索整个输出空间；因此我们改为用基础模型作为预测锚点，并向 LLM 提出一个更窄的问题：这个模型遗漏了什么。我们提出 Multi-Agent Residual In-Context Learning（MARICL），这是一个具备代理式推理能力的框架：其中的 LLM agent 分析基础模型在哪里失败，结合上下文中的高残差样本去假设缺失结构，并通过多轮文本梯度优化生成显式的修正项。我们在九个基准上进行了实验，覆盖科学、生物医学、社会经济和合成场景，MARICL 在所有数据集上都能稳定优于其基础模型。为了检验这些修正到底反映真实结构还是仅仅是批次噪声，我们在 Cell-Free Protein 数据集的一个实验批次上冻结学到的公式，并将其应用到未见批次上，整个过程不重新训练、也不再调用 LLM。在相同试剂协议内，这些冻结公式在超过 92% 的情况下提升了预测；而在不同协议下，它们会系统性失败。其成功边界与生化机制而非批次数量一致，提供了机制泛化的直接证据。

</details>

---

### [[20_Research/Papers/大模型/FuRA_Full-Rank_Parameter-Efficient_Fine-Tuning_with_Spectral_Preconditioning|FuRA: Full-Rank Parameter-Efficient Fine-Tuning with Spectral Preconditioning]]

![[assets/2605.22869_figure.png|800]]

- **arXiv**: [2605.22869](https://arxiv.org/abs/2605.22869)
- **PDF**: https://arxiv.org/pdf/2605.22869
- **详细分析**: [[20_Research/Papers/大模型/FuRA_Full-Rank_Parameter-Efficient_Fine-Tuning_with_Spectral_Preconditioning|FuRA: Full-Rank Parameter-Efficient Fine-Tuning with Spectral Preconditioning]]
- **作者**: Yequan Zhao, Ruijie Zhang, Liyan Tan, Niall Moran, Tong Qin, Zheng Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

大模型在预训练后，通常需要通过全参数微调或LoRA等参数高效微调来适配下游任务，但这两类方法都没有显式利用预训练权重已经形成的谱结构。论文指出，来自小规模微调数据的噪声梯度可能扰动预训练得到的稳健特征，进而损害泛化与遗忘控制。在强化学习、数学推理、视觉指令微调等场景中，这一问题会直接影响最终性能，因此该工作试图回答：能否在保持参数与显存效率的同时，让微调过程更符合预训练表示的几何结构。

#### 方法概述和架构

作者提出FuRA（Full-Rank Adaptation），核心思想是把每个线性层的更新限制在预训练权重的谱空间中，同时保留全秩更新能力。具体做法是将权重矩阵分解为块张量列车形式 W = LSR，其中大核心L由预训练后的分块SVD基底固定不训练，训练只发生在紧凑核心R以及分块奇异值S上。这样一来，更新会被预训练列空间预条件化，既能抑制偏离预训练特征空间的噪声方向，又不会像低秩方法那样受限于秩上限。论文还给出QFuRA的4-bit量化版本，在量化权重场景下复用同样的谱预条件设计。整体流程上，训练时仅优化少量参数并保持推理开销接近LoRA；与直接对SVD参数化做全量训练相比，FuRA在计算与内存上更可落地。

#### 实验结果分析

作者在LLaMA-2-7B、LLaMA-3-8B的常识推理SFT、数学强化学习以及LLaVA-1.5-7B的视觉指令微调上验证FuRA，比较对象包括Full FT、LoRA、DoRA等方法。结果显示，FuRA在多个设置下都优于Full FT，并在LLaMA-3-8B常识推理任务上带来+1.37的提升；在数学RL和VLM任务上也取得稳定增益。量化版本QFuRA同样超过QLoRA。文中还指出FuRA在可训练参数占比不足2%的情况下，无需任务特定的秩调参，仍能取得更好的准确率、显存和步时效率。

<details>
<summary>完整摘要</summary>

全参数微调（Full FT）和LoRA等参数高效微调方法在引入权重更新时，并未考虑预训练阶段建立的谱结构。因此，来自有限微调数据的噪声梯度可能扰动预训练得到的稳健特征。我们认为，谱预条件化是缺失的关键要素：将每个权重矩阵通过其全秩奇异值分解（SVD）进行重新参数化，并冻结一个奇异基底，可以将更新约束在预训练的列空间中，从而形成一种预条件化优化方案；在相同可训练参数量下，它优于不受约束的Full FT。在这一洞见基础上，我们提出FuRA（Full-Rank Adaptation），一种基于块张量列车分解 W = LSR 的高效全秩适配框架，其中大的核心L固定为预训练的分块SVD基底，而只优化紧凑核心R和分块奇异值S。该设计同时提供了全秩的谱预条件化、完整的全秩更新表达能力，并实现了与LoRA相当的参数、显存和步时效率。FuRA在多种设置下都稳定优于Full FT，包括LLM微调（在LLaMA-3-8B常识推理上提升+1.37）、LLM数学强化学习，以及VLM的视觉指令微调。此外，其4-bit量化版本QFuRA也优于QLoRA。代码已公开于 https://github.com/olokevin/FuRA-NIPS 。

</details>

---
