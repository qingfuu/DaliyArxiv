# cs.LG | Machine Learning | 2026-05-22

#arxiv #ComputerScience

**论文数**: 15

### [[20_Research/Papers/具身智能/Remember_to_be_Curious_Episodic_Context_and_Persistent_Worlds_for_3D_Exploration|Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration]]

![[assets/2605.22814_figure.png|800]]

- **arXiv**: [2605.22814](https://arxiv.org/abs/2605.22814)
- **PDF**: https://arxiv.org/pdf/2605.22814
- **详细分析**: [[20_Research/Papers/具身智能/Remember_to_be_Curious_Episodic_Context_and_Persistent_Worlds_for_3D_Exploration|Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration]]
- **作者**: Lily Goli, Justin Kerr, Daniele Reda, Alec Jacobson, Andrea Tagliasacchi, Angjoo Kanazawa
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

在稀疏奖励、长时程的3D环境探索中，智能体往往必须先主动探索，才能学到后续有用的行为，典型场景包括室内导航、目标搜索和复杂交互任务。现有基于好奇心的强化学习虽然能通过“预测误差”提供内在奖励，但在真实感较强的3D场景里容易陷入局部循环：智能体反复回到旧区域，却因为世界模型“遗忘”而再次获得新奇奖励。本文值得关注之处在于，它把探索失败的根源明确归结为“缺少空间持久性”和“缺少情节上下文”，并尝试用一个持续更新的世界模型配合带记忆的策略来解决这一问题。

#### 方法概述和架构

论文提出的核心思路是“持久世界 + 情节记忆”的好奇心探索框架：训练时使用在线3D重建作为持续的世界模型，推理时则只依赖RGB序列进行动作决策。具体来说，世界模型采用在线3D Gaussian Splatting（3DGS）不断吸收观测并渲染下一视角，用重建结果与真实观测之间的差异构造内在奖励，差异越大表示该视角越新奇。智能体侧使用基于Transformer的序列策略，把过去的RGB观测与动作编码为情节上下文，通过因果时序注意力和全局线性注意力记忆模块决定下一步相机动作。训练阶段，策略在好奇心奖励驱动下进行 on-policy RL；测试阶段不需要显式地图、深度或定位信息，只需输入RGB流即可行动。作者还加入了阶段性随机行为注入，用来帮助智能体穿过已见区域并发现新的分支路径。

#### 实验结果分析

实验在HM3D上以纯好奇心方式训练，并与基于RL的主动建图方法比较；结果显示该方法在室内场景探索上优于这些基线。论文还报告了零样本泛化到Gibson以及AI生成的3D世界，表明方法不仅适用于训练场景，也能迁移到分布外环境。进一步的任务微调实验包括 apple picking 和 image-goal navigation，显示该端到端策略在少量下游奖励微调后优于从头训练的基线。正文节选中提到若将持久记忆人为截短，探索能力会显著下降，可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

探索是学习有用行为的前提，尤其是在稀疏奖励、长时程任务中，3D环境更是如此。基于好奇心的强化学习通过让智能体根据其世界预测模型与现实之间的不一致来获得内在奖励，从而应对这一问题。然而，将这种内在动机迁移到复杂、照片级真实感环境仍然很困难，因为智能体会陷入局部循环，并在重访遗忘状态时获得新的奖励。在这项工作中，我们证明这种失败源于缺少空间持久性和情节上下文。我们表明，有效的好奇心需要一个持续存在并不断更新的世界模型，以及一个保持情节轨迹历史、能够朝新奇区域导航的智能体。我们通过在线3D重建作为持久世界模型，并将策略参数化为对RGB观测的序列模型以维持情节上下文，实现了这一点。该设计使得训练期间能够有效探索，而部署时智能体又只需使用RGB帧即可导航。在HM3D上仅通过好奇心训练后，我们的智能体优于基于RL的主动建图基线，并能零样本泛化到Gibson和AI生成的世界。我们的端到端策略还能够高效适配下游任务，例如 apple picking 和 image-goal navigation，且优于从头训练的基线。视频结果见：https://recuriosity.github.io/。

</details>

---

### [[20_Research/Papers/强化学习/A_note_on_convergence_of_Wasserstein_policy_optimization|A note on convergence of Wasserstein policy optimization]]

![[assets/2605.22622_first_page.png|800]]

- **arXiv**: [2605.22622](https://arxiv.org/abs/2605.22622)
- **PDF**: https://arxiv.org/pdf/2605.22622
- **详细分析**: [[20_Research/Papers/强化学习/A_note_on_convergence_of_Wasserstein_policy_optimization|A note on convergence of Wasserstein policy optimization]]
- **作者**: David Šiška, Yufei Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

Wasserstein Policy Optimization（WPO）是近年来用于连续动作空间强化学习的一类新算法，核心思想是把策略更新看作 Wasserstein 梯度流，从而直接在策略分布空间中优化随机策略。相比传统策略梯度方法，WPO在经验上表现不错，但其在连续状态、连续动作环境中的收敛理论一直不够完整。本文关注的问题是：在熵正则化马尔可夫决策过程（MDP）框架下，WPO 是否能够保证收敛，以及收敛速度能否达到线性级别。这篇工作值得关注之处在于，它试图用严格的数学分析为 WPO 的可解释性和理论可靠性补上关键一环。

#### 方法概述和架构

作者将问题放在熵正则化 MDP 中讨论，设状态空间为有限离散集合、动作空间为欧氏空间，并引入带 KL 正则项的长期回报/代价目标。首先通过 Bellman 方程写出正则化最优价值函数和最优策略的闭式形式，再把策略类限制在相对于参考测度可积的马尔可夫策略上。接着，论文把策略演化建模为 Wasserstein 梯度流对应的连续性方程，并利用 value function 对策略的 flat derivative 来确定流的驱动方向。具体地，若选择使能量下降最快的方向，策略密度演化会转化为包含 Q 函数梯度、参考分布势函数梯度以及扩散项的 Fokker-Planck 型方程。作者进一步借助均值场分析、能量耗散和局部 log-Sobolev 不等式，建立该梯度流的收敛性质。

#### 实验结果分析

本文给出的核心理论结论是：在足够光滑解存在等技术假设下，WPO 在熵正则化 MDP 框架中应当具有线性收敛性质，价值函数会以指数速度逼近全局最优值。作者证明了沿梯度流轨迹能量单调耗散，并建立了沿流成立的局部 log-Sobolev 不等式，这是推出线性收敛的关键工具。节选内容主要是理论分析，没有给出实验数据集、基线方法或具体数值结果；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

Wasserstein Policy Optimization（WPO）是一种近期提出的强化学习算法，它利用 Wasserstein 梯度流来优化连续动作空间中的随机策略。尽管其在实验上表现出较强效果，但在连续状态和连续动作环境中，WPO 的理论收敛性质尚未被完整建立。本文指出：在熵正则化马尔可夫决策过程框架下，WPO 具有线性收敛性。为此，我们借助近期关于使用 log-Sobole 不等式分析梯度流收敛的均值场理论进展。假设梯度流方程存在足够光滑的解，我们证明沿该流能量会单调耗散，并建立一个局部 log-Sobole 不等式。最终，这些性质使我们能够论证价值函数会以线性速度收敛到全局最优解。

</details>

---

### [[20_Research/Papers/强化学习/Factored_Diffusion_Policies_Compositionally_Generalized_Robot_Control_with_a_Single_Score_Network|Factored Diffusion Policies:Compositionally Generalized Robot Control with a Single Score Network]]

![[assets/2605.22596_figure.png|800]]

- **arXiv**: [2605.22596](https://arxiv.org/abs/2605.22596)
- **PDF**: https://arxiv.org/pdf/2605.22596
- **详细分析**: [[20_Research/Papers/强化学习/Factored_Diffusion_Policies_Compositionally_Generalized_Robot_Control_with_a_Single_Score_Network|Factored Diffusion Policies:Compositionally Generalized Robot Control with a Single Score Network]]
- **作者**: Sayan Mitra, Ege Yuceel, Noah Giles, Abhishek Pai
- **cs 子类**: cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

机器人控制任务通常由多个因素共同决定，例如要抓取的物体、需要避开的障碍、目标颜色或赛道几何等。若为每一种因素组合都收集专家演示，数据需求会随着因素数量呈组合爆炸式增长，代价极高。本文关注如何让一个控制策略在只见过部分因素组合的情况下，仍能泛化到未见过的组合任务，因此具有很强的实际价值。

#### 方法概述和架构

论文提出 Factored Diffusion Policies：用一个共享的 diffusion policy 网络建模动作分布，并通过“按因素置空 token”的 dropout 训练，让模型分别学到各个因素的条件修正项。推理时，将无条件 score 与各因素对应的 score 修正项做加性组合，得到组合后的 score，从而在单个网络内实现可组合泛化。作者的关键假设是：在给定动作—观测对后，各任务因素近似条件独立；在这一假设下，组合 score 可以近似真实联合 score，并给出有界误差。方法还把 score 层面的误差继续传递到反向采样 ODE 和闭环跟踪控制器，构造了 trajectory-tube certificate，用于保证闭环轨迹仍落在可控的状态管道内。

#### 实验结果分析

作者在无人机竞速任务上验证了方法，包括基于状态的多门赛道组合任务，以及基于视觉的单门穿越任务。结果显示，在多门赛道上，factored policy 对未见过的 held-out 门组合通过率达到 90%，与 oracle 持平，而 K-network 组合基线则降到 3%。在视觉单门穿越中，该方法可零样本迁移到未见过的场地，成功率提升 11.7 个百分点，撞毁率降低 2.4 倍。论文还报告了 certificate 与泛化界的一致性，并指出参数共享是性能提升的关键。

<details>
<summary>完整摘要</summary>

机器人任务通常由一组因素来指定，例如要抓取的物体、要避开的障碍、目标的颜色等等。若为每一种因素取值组合都收集专家演示，所需数据量会随着组合数目呈组合爆炸式增长。我们提出 factored diffusion policies：使用一个共享的 diffusion 网络，并通过按因素的 null-token dropout 训练，使其在推理时的 score 能够按因素加性分解。在“给定动作—观测对后，各因素近似条件独立”的条件下，这种组合可以以有界的统一误差近似真实的联合 score，从而将训练任务预算从因素卡迪纳尔数的乘积降为其和。我们还构造了 trajectory-tube certificate：把这一 score 层面的误差界，经由反向时间采样 ODE 和一个具有收缩性的跟踪控制器，串联到闭环状态轨迹管道中；该管道半径可以分解为一个 ODE 灵敏度常数与逐因素的 score 误差预算。不同于将多个独立训练网络进行组合的控制领域 compositional-diffusion 方法，我们只使用一个共享网络。无人机竞速实验验证了该泛化界与证书的有效性：在基于状态的多门赛道任务上，factored policy 在未见过的门组合上通过率达到 90%，与 oracle 持平，而 K-network 组合基线则崩溃到 3%；在基于视觉的单门穿越任务上，该方法可零样本迁移到未见过的场地，成功率提升 11.7 个百分点，撞毁率降低 2.4 倍。

</details>

---

### [[20_Research/Papers/大模型/GraphFlow_A_Graph-Based_Workflow_Management_for_Efficient_LLM-Agent_Serving|GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving]]

![[assets/2605.22566_figure.png|800]]

- **arXiv**: [2605.22566](https://arxiv.org/abs/2605.22566)
- **PDF**: https://arxiv.org/pdf/2605.22566
- **详细分析**: [[20_Research/Papers/大模型/GraphFlow_A_Graph-Based_Workflow_Management_for_Efficient_LLM-Agent_Serving|GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving]]
- **作者**: Ao Li, Shangpeng Yang, Fahao Chen, Tianheng Xu, Peng Li, Zhou Su
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

LLM-based agent 在复杂任务上越来越依赖“workflow”来提供结构化的步骤约束，例如多步规划、工具调用和长链路执行。现有 workflow-assisted agent serving 系统大多依赖预定义模板或浅层语义匹配，只能在固定仓库里检索整套流程，难以捕捉任务与操作之间的深层关系，也不擅长泛化到未见过的新任务。与此同时，agent 推理过程中的 KV cache 往往按 workflow 粒度分别维护，不同 workflow 之间共享的操作会被重复存储，造成明显的内存浪费。本文值得关注之处在于，它把“工作流管理”和“高效 serving”统一到一个图结构里，同时解决了流程构造的灵活性和状态复用的系统开销。

#### 方法概述和架构

论文提出 GraphFlow，一个基于图的 workflow 管理框架，其核心表示是 wGraph：把多个 workflow 中的原子操作及其依赖关系统一到一个有向无环图中，每个节点对应一个原子操作。在线服务时，GraphFlow 先根据用户任务构造 task-conditioned graph，即在 wGraph 上加入一个虚拟任务节点，并与所有操作节点建立双向连接，以注入任务语义。随后，基于 GNN 对任务节点与操作节点进行联合编码，再通过 MLP 将图表示解码为一个与当前任务匹配的连通子图，作为动态生成的 workflow。除了流程生成，GraphFlow 还设计了 topology-aware state management：把每个操作的 KV 状态拆成与上下文无关的基础部分和少量与拓扑相关的残差部分，从而在不同 workflow 间复用共享状态。系统还引入 path pruning，删除 wGraph 中无效或不可达的路径，避免状态空间膨胀，并使 KV 管理只覆盖有效执行轨迹。整体流程可分为离线构建与训练、在线生成与推理两阶段，前者准备 wGraph 和基础状态，后者按任务动态实例化 workflow 并高效复用缓存。

#### 实验结果分析

作者在 5 个基准数据集上评测了 GraphFlow，覆盖数学推理、复杂问答和代码生成等任务，并在多种 backbone LLM 上验证其效果。结果显示，GraphFlow 相比现有 SOTA 方法平均提升约 4.95 个百分点，同时将 KV cache 内存占用降低约 4 倍。论文还报告了消融实验与敏感性分析，用于验证 workflow 生成模块和状态管理模块的贡献；从节选内容看，相关细节以图表和附录补充为主，可见文本未给出具体数值。整体结论是：图结构化的 workflow 管理不仅能提升任务执行质量，也能显著缓解 agent serving 的内存瓶颈。

<details>
<summary>完整摘要</summary>

基于大语言模型（LLM）的智能体在复杂任务上展现出很强的推理与执行能力，尤其是在结构化指令，也就是所谓工作流的引导下表现更为突出。然而，现有的工作流辅助智能体服务系统通常依赖预定义模板和浅层匹配机制，这限制了它们捕捉深层语义关系以及泛化到此前未见任务的能力。为了解决这些问题，我们提出一种新的工作流管理范式：使用统一的图来表示工作流，称为 wGraph，其中每个节点对应一个原子操作。wGraph 作为共享底座，可以动态实例化出面向具体任务的工作流。在 wGraph 的基础上，我们进一步提出 GraphFlow，这是一个通过两项关键设计将工作流高效整合进智能体服务的系统。首先，自适应工作流生成会根据任务语义和约束要求，基于 wGraph 动态构建工作流。其次，工作流状态管理利用 wGraph 的结构高效管理 Key-Value（KV）缓存，从而减少智能体服务过程中的重复计算。跨五个基准数据集的大量实验表明，GraphFlow 一致优于现有最先进方法，平均性能提升约 4.95 个百分点，同时内存占用约降低 4 倍。

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_learning_for_ion_shuttling_on_trapped-ion_quantum_computers|Reinforcement learning for ion shuttling on trapped-ion quantum computers]]

![[assets/2605.22463_figure.png|800]]

- **arXiv**: [2605.22463](https://arxiv.org/abs/2605.22463)
- **PDF**: https://arxiv.org/pdf/2605.22463
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_learning_for_ion_shuttling_on_trapped-ion_quantum_computers|Reinforcement learning for ion shuttling on trapped-ion quantum computers]]
- **作者**: Maximilian Schier, Lea Richtmann, Christian Staufenbiel, Tobias Schmale, Daniel Borcherding, Michèle Heurs, Bodo Rosenhahn
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

离子俘获量子计算通常采用模块化芯片，不同区域分别负责存储、态制备和门操作，量子门执行前必须先把离子在这些区域之间搬运，这一过程称为 ion shuttling。随着离子数增多，如何为给定电路规划最优搬运顺序会迅速变成高维组合优化问题，精确求解难以在可接受时间内完成。现有编译器主要依赖启发式规则，虽然可扩展，但往往难以达到最优，且对芯片结构变化的适应性有限。因此，本文将强化学习引入离子搬运优化，具有较强的系统设计与量子编译应用价值。

#### 方法概述和架构

论文把 ion shuttling 建模为一个顺序决策问题，并采用 PPO 作为核心强化学习算法来学习搬运策略。为了让策略对电路重标号和可交换门重排保持不敏感，作者设计了满足置换不变性与电路等价重排不变性的状态表示，并将电路依赖关系与芯片结构信息编码进输入。训练阶段通过构造带 shaping 的奖励函数，直接鼓励减少搬运步数，同时在训练中生成不同规模、不同结构的任务实例以增强泛化能力。推理阶段，训练好的策略网络接收待执行电路和芯片布局，逐步输出下一步该移动哪些离子、是否执行门操作，从而生成完整的 shuttling 计划。文中还讨论了网络结构、训练流程以及对不同芯片架构的适配方式，并将该方法扩展到 X-chip 与 Q-chip 等不同设计。

#### 实验结果分析

作者在 MQT bench 电路和 quantum volume（QV）电路上进行了实验，并与现有的启发式编译器以及 SAT solver 基线比较。结果表明，该 RL 方法在搬运操作数上最多可减少 36.3%，整体优于当前最先进的启发式方案；对于小规模实例，还能与 SAT solver 的最优解接近。文中进一步展示了该方法可以迁移到不同芯片架构，并通过推理时间扩展性和消融分析说明了若干 RL 设计选择的有效性。具体部分实验数值在节选中未完整给出。

<details>
<summary>完整摘要</summary>

可扩展的离子俘获量子计算通常依赖模块化芯片，这类芯片包含不同功能的区域，例如存储区、态制备区和门执行区。为了执行量子电路，离子必须在这些区域之间运输，这一过程称为 ion shuttling。为了获得可靠的计算结果，必须对这一搬运过程进行优化。然而，随着离子数量增加，这会变成一个高维优化问题，难以高效计算最优解。据我们所知，我们首次展示了将强化学习（RL）用于离子搬运优化。RL 非常适合这类场景，因为它能够通过与问题的直接交互来学习策略。我们证明，所提出的 RL 方法优于当前最先进的启发式技术，搬运操作数最多可减少 36.3%。此外，我们还表明该方法可以很容易地适用于多种芯片架构。我们的方案为在芯片设计阶段研究搬运效率提供了一种通用方法，因此也成为未来更复杂架构中一个高度相关的工具。

</details>

---

### [[20_Research/Papers/强化学习/Target-Aligned_Bellman_Backup_for_Cross-domain_Offline_Reinforcement_Learning|Target-Aligned Bellman Backup for Cross-domain Offline Reinforcement Learning]]

![[assets/2605.22376_figure.png|800]]

- **arXiv**: [2605.22376](https://arxiv.org/abs/2605.22376)
- **PDF**: https://arxiv.org/pdf/2605.22376
- **详细分析**: [[20_Research/Papers/强化学习/Target-Aligned_Bellman_Backup_for_Cross-domain_Offline_Reinforcement_Learning|Target-Aligned Bellman Backup for Cross-domain Offline Reinforcement Learning]]
- **作者**: Wei Liu, Ting Long
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

跨域离线强化学习（CDRL）希望在目标域交互数据很少的情况下，借助源域离线数据提升策略学习效果，适合机器人控制、推荐系统和自动驾驶等难以在线试错的场景。现有方法通常依据源域与目标域转移的“相似度”来筛选或加权数据，但这并不等价于长期回报一致：看起来相近的状态转移，在目标域中可能导致完全不同的结果。正因如此，单纯做转移级别匹配容易把偏差传进 Bellman 更新，进而误导价值估计和策略优化，这也是本文值得关注的核心原因。

#### 方法概述和架构

论文提出 Target-Aligned Bellman Backup（TABB），把源数据是否可迁移的判断标准从“转移是否相似”改为“其 Bellman backup 是否与目标域对齐”。方法首先定义 Target Bellman Mismatch（TBM），用于衡量一个源域转移在目标域 Bellman 备份下的偏差：它比较真实 Bellman target 与目标对齐 Bellman target 的差异。具体实现中，TABB 将状态、状态-动作对编码到共享潜空间，再由目标域预测器根据当前表示预测奖励和下一状态，形成用于计算 TBM 的目标对齐信号。随后，TABB 根据 TBM 对源域转移进行软加权：TBM 小的样本被赋予更高权重，说明它们更能帮助准确估计目标域 Bellman target；TBM 大的样本则被降低权重，以减少负迁移。最后，重加权后的源数据与目标域数据一起用于训练目标策略，使价值学习和策略优化都围绕更可靠的 Bellman 监督展开。

#### 实验结果分析

作者在 6 个环境、16 组数据组合上评估了 TABB，覆盖两类跨域迁移设置，并与多种基于正则化、筛选和样本生成的基线方法比较。实验结果表明，TABB 在这些跨域离线强化学习场景中表现稳定且整体优于已有方法。正文还给出了消融与鲁棒性分析，用于验证 TBM 加权与目标域 Bellman 对齐这两个设计的有效性；不过节选文本未给出具体数值。

<details>
<summary>完整摘要</summary>

跨域离线强化学习（CDRL）旨在利用源域中收集的数据，提升目标域中的策略学习效果。现有工作通常通过衡量源域数据与目标域转移的相似度来评估其可迁移性，并隐式地进行转移级别的筛选：被认为相似的转移会被赋予更高的权重或奖励，而不相似的转移则被降权。然而，转移层面的相似性并不必然意味着长期回报的一致性。即便在视觉或动力学上相似的转移，在目标域中也可能导致显著不同的结果，从而误导策略学习并降低性能。为了解决这一问题，我们重新审视策略学习的基本目标。由于策略优化最终依赖 Bellman target 来评估决策质量，我们提出应当基于源域转移与目标域 Bellman target 的对齐程度来评估其可迁移性，而不是依赖表面的转移相似性。基于这一洞察，我们提出了 Target-Aligned Bellman Backup（TABB），它通过衡量源域数据对目标域中准确 Bellman target 估计的贡献，选择性地利用源域数据。我们在目标域数据极其有限的广泛跨域离线强化学习设置下评估了 TABB。实验结果表明，TABB 能够持续取得强劲表现。

</details>

---

### [[20_Research/Papers/强化学习/Chebyshev_Policies_and_the_Mountain_Car_Problem_Reinforcement_Learning_for_Low-Dimensional_Control_Tasks|Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-Dimensional Control Tasks]]

![[assets/2605.22305_figure.png|800]]

- **arXiv**: [2605.22305](https://arxiv.org/abs/2605.22305)
- **PDF**: https://arxiv.org/pdf/2605.22305
- **详细分析**: [[20_Research/Papers/强化学习/Chebyshev_Policies_and_the_Mountain_Car_Problem_Reinforcement_Learning_for_Low-Dimensional_Control_Tasks|Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-Dimensional Control Tasks]]
- **作者**: Stefan Huber, Hannes Unger, Georg Schäfer, Jakob Rehrl
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.02（加权：大模型 0.1，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

Mountain Car 是强化学习中的经典低维连续控制基准，要求智能体在重力作用下通过来回摆动，把小车推到山顶目标点。这个任务虽然形式简单，但长期以来其连续版本的最优控制解一直未知，导致现有 RL 方法距离最优还有多远并不清楚。论文因此值得关注：它不仅补上了一个持续 36 年的理论空缺，还借此反推出一种更轻量、可解释的策略表示方式。

#### 方法概述和架构

作者先对连续版 Mountain Car 做解析求解，把系统动力学改写为类似受势能约束的形式，从而把最优控制问题拆成动力学分析、无约束损失最小化、以及重新施加边界约束三个步骤。基于对最优控制轨迹“分段单调摆动”的观察，论文进一步提出 Chebyshev policies：用多变量 Chebyshev 多项式来参数化随机策略，作为神经网络策略的直接替代。该策略类被证明是连续策略空间中的稠密类，因此具备通用逼近能力；实现上可像普通 MLP 一样训练，并可无缝接入 PPO、ARS 和 REINFORCE 等算法。训练时，策略网络输出动作分布参数或动作值，推理时直接由 Chebyshev 基函数组合得到动作，因此参数量和计算量都显著降低。

#### 实验结果分析

在连续 Mountain Car 上，作者给出了解析最优控制解，并据此评估了当前 SOTA RL 智能体与最优解之间的差距，发现现代方法仍有较大 regret。使用 Chebyshev policies 后，在 Mountain Car 上相较神经网络策略，regret 降低了 4.18 倍，同时可训练参数减少 277 倍。论文还在 Pendulum 以及真实世界的非线性运动控制测试平台上进行了验证，结果显示 Chebyshev policies 在 PPO、ARS 和 REINFORCE 下都持续优于 MLP 策略。文中还分析了控制轨迹和策略行为差异，并提出了更丰富的 Mountain Car 变体方向；可见文本未给出具体数值细节的消融结果。

<details>
<summary>完整摘要</summary>

我们解析地求解了 Mountain Car 这一强化学习中的经典基准问题，并推导出最优控制解，弥补了 36 年来的一个空白。由此我们揭示出两个令人意外的结论：最优控制实际上相当简单，但现代 RL 智能体与最优性之间仍存在很大差距。受最优控制分析启发，我们从第一性原理提出了 Chebyshev policies，将其作为一种通用的（即稠密的）RL 策略类别。它们可以作为神经网络的即插即用替代方案进行训练，将 regret 降低 4.18 倍，同时所需参数数量减少 277 倍，从而提升样本效率、可解释性和实时能力。我们还在其他 RL 任务上评估了 Chebyshev policies，包括一个真实世界的非线性运动控制测试平台。结果表明，在 PPO、ARS 和 REINFORCE 下，它们都能稳定优于神经网络。我们的研究表明，Chebyshev policies 为低维控制任务提供了一种有吸引力、轻量级的替代方案或补充方案。

</details>

---

### [[20_Research/Papers/强化学习/Kernel-Based_Safe_Exploration_in_Deep_Reinforcement_Learning|Kernel-Based Safe Exploration in Deep Reinforcement Learning]]

![[assets/2605.22207_figure.png|800]]

- **arXiv**: [2605.22207](https://arxiv.org/abs/2605.22207)
- **PDF**: https://arxiv.org/pdf/2605.22207
- **详细分析**: [[20_Research/Papers/强化学习/Kernel-Based_Safe_Exploration_in_Deep_Reinforcement_Learning|Kernel-Based Safe Exploration in Deep Reinforcement Learning]]
- **作者**: Rupak Majumdar, Nikhil Singh, Sadegh Soudjani
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

深度强化学习在机器人控制、经典控制和复杂连续控制任务中表现突出，但一旦部署到真实世界，策略探索可能进入危险状态，带来安全风险。现有安全强化学习方法要么缺少可验证的安全证书，要么依赖大量数据、对系统动力学有较强假设，或者只能处理确定性/低维场景。本文关注的是在未知随机动力学下，如何在持续探索中同时学到高回报策略与可量化的安全保证，因此具有较强的现实部署价值。

#### 方法概述和架构

论文提出 Kernel-Based Safe Exploration（KBSE），核心是把 barrier function 与深度强化学习的策略学习过程同步进行。方法用 reproducing kernel Hilbert space（RKHS）中的 conditional mean embedding（CME）来表示和迭代计算 barrier function，从而把原本难以处理的条件期望约束转化为可求解的线性优化问题。训练过程中，智能体一边采样交互数据、一边更新 barrier；推理时，若检测到当前动作可能违反安全约束，KBSE 会将其修改为安全动作，以限制到达危险状态的概率。整体上，输入是状态-动作交互数据与安全阈值，输出是一个在概率安全约束下的最优控制策略以及对应的安全概率界。

#### 实验结果分析

作者在多个复杂连续控制基准上评估了 KBSE，包括 Gym 经典控制和基于 Mujoco 的环境，并与主流 off-policy safe RL 方法进行了对比。实验表明，KBSE 在奖励累积和安全成本方面均优于基线，同时还能给出基线方法无法提供的策略安全概率估计。文中还指出，随着探索数据增多，所学习的 barrier 能提供更强的概率安全保证；但节选文本未给出具体数值。

<details>
<summary>完整摘要</summary>

安全性一直是深度强化学习算法在真实世界中部署时的核心问题。一个有前景的方向是同时学习 barrier function（障碍函数）和策略，以确保所学策略不会进入危险区域。Barrier 是一个从状态映射到实数的函数：它对初始状态赋予较低值，对危险状态赋予较高值，并且在每次状态转移时其期望值下降；这样的函数可以用于对到达危险状态的概率进行上界估计。以往工作通常直接利用探索数据学习 barrier function，但这类方法要么需要大量数据，要么对系统动力学施加限制。本文表明，kernel embeddings 可以用于在未知动力学的随机系统上、于深度强化学习过程中学习 barrier function。我们提出的算法 kernel-based safe exploration（KBSE）在探索过程中同时学习最优策略和 barrier。Barrier 通过迭代方式计算，并以 conditional mean embeddings 的形式表示；随着探索增加，它们能够提供更好的概率安全保证。探索算法利用所学 barrier function 来识别安全违规；一旦检测到违规，就会介入并将原本不安全的动作修改为安全动作，从而确保探索过程被限制在能够约束到达危险状态概率的动作集合内。我们在若干复杂的连续控制基准上评估了 KBSE。实验结果表明，该算法适合用于合成概率安全、且不会降低奖励累积的控制策略。

</details>

---

### [[20_Research/Papers/大模型/Reinforced_Graph_of_Thoughts_RL-Driven_Adaptive_Prompting_for_LLMs|Reinforced Graph of Thoughts: RL-Driven Adaptive Prompting for LLMs]]

![[assets/2605.22195_figure.png|800]]

- **arXiv**: [2605.22195](https://arxiv.org/abs/2605.22195)
- **PDF**: https://arxiv.org/pdf/2605.22195
- **详细分析**: [[20_Research/Papers/大模型/Reinforced_Graph_of_Thoughts_RL-Driven_Adaptive_Prompting_for_LLMs|Reinforced Graph of Thoughts: RL-Driven Adaptive Prompting for LLMs]]
- **作者**: Manuel Noah Riesen, Peter Alfred von Niederhäusern
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

Graph of Thoughts（GoT）把大模型的推理组织成任意图结构，适合需要分解、汇总和回溯的复杂任务，但其图结构通常需要人工预先设计。这个过程不仅依赖对任务解法的深入理解，也使得系统对任务复杂度和模型输出的不确定性缺乏适应性。本文关注如何用强化学习让 GoT 的“操作图”自动生成，从而降低使用门槛并提升推理流程的灵活性。

#### 方法概述和架构

论文提出 Reinforced Graph of Thoughts（RGoT），用强化学习从人类给定的操作集合中自动构造 GoT 的图结构。作者先定义了一个“纯 GoT 框架”，把任务表示为一组可用操作，操作既可以是提示大模型执行的 prompt operation，也可以是程序化计算的 execution operation，同时还引入用于评估中间结果的 score operation。与原始 GoT 不同，这里将“操作图”和“思维图”分离：前者是受约束的有向无环图（DAG），按层组织，只有一个源点和一个汇点，且通过最大深度、最大宽度以及“分叉截止深度”等约束控制图形增长。RGoT 将图构造过程建模为强化学习问题，状态空间包含图的结构表示，动作空间对应对当前图的扩展、分支或合并等选择；训练后，智能体在推理时根据任务复杂度动态决定如何生成后续操作图，再由该图驱动大模型逐步执行与汇总。

#### 实验结果分析

论文在多个任务上评估了 RGoT，包括 sum list、sort list、intersect set、count keywords 和 merge documents，并与 GoT 相关设置进行对照。实验还包含对不同大模型能力的评估，以及强化学习智能体的表现分析；同时做了消融研究来观察不同超参数和策略配置的影响。总体结论是：在一定约束下，RGoT 能够根据任务复杂度自动构造合适的操作图，说明“自适应图式提示”是可行的。可见文本未给出具体数值，但作者指出该方法在可访问性与适应性上优于静态手工图。

<details>
<summary>完整摘要</summary>

Graph of Thoughts（GoT）是近期面向大语言模型（LLMs）的一类提示范式的广义形式，已被证明对复杂问题求解很有帮助。GoT 通过执行一张操作图，将 LLM 的“思维”结构化为任意图，从而形成真正的 graph of thoughts。最初，这张操作图需要人工手动定义，这要求对待解决问题的解法有深入理解。这样的静态操作图较为僵硬，因此缺乏适应性。我们提出 Reinforced Graph of Thoughts（RGoT），这是一种自动化的 GoT 提示方法，它利用强化学习（RL）从人类定义的操作集合中自适应地生成操作图。结果表明，在某些约束条件下，可以以自动化方式根据任务复杂度自适应地构造操作图。

</details>

---

### [[20_Research/Papers/世界模型/Beyond_Euclidean_Proximity_Repairing_Latent_World_Models_with_Horizon-Matched_Trajectory_Reachability_Metrics|Beyond Euclidean Proximity: Repairing Latent World Models with Horizon-Matched Trajectory Reachability Metrics]]

![[assets/2605.22164_figure.png|800]]

- **arXiv**: [2605.22164](https://arxiv.org/abs/2605.22164)
- **PDF**: https://arxiv.org/pdf/2605.22164
- **详细分析**: [[20_Research/Papers/世界模型/Beyond_Euclidean_Proximity_Repairing_Latent_World_Models_with_Horizon-Matched_Trajectory_Reachability_Metrics|Beyond Euclidean Proximity: Repairing Latent World Models with Horizon-Matched Trajectory Reachability Metrics]]
- **作者**: Liangyu Li, Shengzhi Wang, Qingwen Liu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

这篇论文关注的是基于潜在空间的世界模型在强化学习和机器人规划中的“终端代价”接口问题：模型虽然可能已经学到了足以控制的状态信息，但规划器通常只看预测终点与目标状态的欧氏距离，因而可能被错误的距离度量误导。作者指出，这种做法隐含地假设潜在空间中各维度对“可达性”的权重是正确的，但在复杂地形或长时域任务中，这一假设经常失效。论文以 TwoRoom 导航和 PushT 操作为例，说明瓶颈不一定在世界模型本身，而可能在规划器看到的终端打分方式，因此很值得关注。

#### 方法概述和架构

作者提出 Trajectory Reachability Metrics（TRM），把它作为一个针对固定潜在世界模型的事后终端排序层，而不是重新训练编码器或动力学模型。TRM 训练一个轻量的成对打分头，输入为两个潜在状态的拼接、差分及绝对差分，输出两状态之间的可达性/时间距离分数，用来替代或混合原来的潜在欧氏终端代价。训练监督来自同一轨迹中的状态对，标签是时间间隔，核心设计是采用与规划时域相匹配的、覆盖较广且平衡的采样策略，使学到的度量更适合长时域候选终点排序。推理时，世界模型、候选采样器和优化器保持不变，只替换终端打分函数，从而只修复规划器的接口层。论文还设计了同一候选集上的排序审计与子空间分析，用于验证 TRM 是否真正改变了规划器选择的终点。

#### 实验结果分析

在困难的 TwoRoom 基准上，使用 LeWorldModel（LeWM）进行原始潜在空间规划的成功率只有 7.0%，而加入完整时域 TRM 后成功率提升到 97.0%；随机打乱时间标签的对照实验则保持 0.0%，说明收益来自正确的时序监督。相同方法也将 PLDM 基线从 32.7% 提升到 84.0%（跨三个随机种子），而短时域 TRM 版本在同样的 100,000 对样本预算下只达到 35.0%，表明时域匹配非常关键。作者进一步在 TwoRoom 中给出机制证据：XY 位置几乎可被线性解码（R^2=0.998），但原始 latent MSE 会误排候选；而在 PushT 的 go50/go75 任务上，TRM 风格的任务状态度量在排序和终点距离上也更稳定地优于仅看闭环成功率的做法。

<details>
<summary>完整摘要</summary>

潜在世界模型可以包含控制所需的状态信息，但其终端代价接口可能把规划器暴露给错误的、与决策相关的信息。在常见的潜在 MPC 中，候选动作序列通常按预测终端潜在状态与目标潜在状态之间的欧氏距离排序；这一做法假设原始潜在距离能够正确加权与可达性相关的变量。我们提出 trajectory reachability metrics（TRM），这是一种针对固定潜在世界模型的事后终端排序方法。TRM 从已记录的轨迹结构中训练一个小型成对打分头，并将其作为替代或混合代价；编码器、动力学模型、采样器、优化器以及评估流程都保持不变。其关键设计选择是时域感知监督：度量在覆盖面广、且平衡的时间间隔上训练，以匹配长时域终端候选排序问题。在一个困难的 TwoRoom 基准上，使用 LeWorldModel（LeWM）进行原始潜在规划的平均成功率只有 7.0%，而完整时域的 TRM 可达到 97.0%；打乱时间标签的对照实验则保持在 0.0%。同样的训练方案将 PLDM 基线在三个随机种子上从 32.7% 提升到 84.0%，而短时域 TRM 版本即便在相同的 100,000 对样本预算下也只能达到 35.0%。在 TwoRoom 中，我们还提供了 TRM 起作用的机制证据：XY 位置可以被线性解码，R^2=0.998，但原始 latent MSE 会错误地排序候选；XY 探针对应的行空间只占终端目标 latent MSE 的不到 1%，却承载了大部分候选质量信号；同一候选集选择审计（SCSA）表明，TRM 改善了规划器看到的排序以及最终选中的终点。在 PushT 的 go50/go75 任务上，TRM 风格的任务状态度量比闭环成功率更清晰地改善了 SCSA 排序和所选最终距离，因此在连续操作中更适合作为辅助性的混合代价。TRM 既是面向规划器的修复方法，也是一项机制研究：TRM 用于修复规划接口，而审计则解释了何时以及为何终端可达性度量应该替代或补充原始潜在近邻距离。

</details>

---

### [[20_Research/Papers/机器人/CoRMA_Contrastive_RMA_for_Contact-Rich_Meta-Adaptation|CoRMA: Contrastive RMA for Contact-Rich Meta-Adaptation]]

![[assets/2605.22082_figure.png|800]]

- **arXiv**: [2605.22082](https://arxiv.org/abs/2605.22082)
- **PDF**: https://arxiv.org/pdf/2605.22082
- **详细分析**: [[20_Research/Papers/机器人/CoRMA_Contrastive_RMA_for_Contact-Rich_Meta-Adaptation|CoRMA: Contrastive RMA for Contact-Rich Meta-Adaptation]]
- **作者**: Wentian Wang, Chutong Wen, Hongxu Ma, Wuhao Wang, Zhexiong Xue, Abdul Haseeb Nizamani, Dandi Zhou, Xinhai Sun, Jianqiao Zhu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

接触丰富型装配任务（如 PegInsert、GearMesh、NutThread）在机器人中非常常见，但这类任务对接触时序、摩擦、间隙和卡滞极其敏感，仿真里能成功的策略往往一到真实硬件上就明显退化。现有基于 RMA 的自适应方法虽然能利用“特权信息”做在线适应，但对于以力觉为主的装配场景，直接回归原始仿真参数并不够贴合真实控制所需的接触语义。本文值得关注之处在于，它尝试把“接触发生了什么”抽象成可复用的语义上下文，而不是仅仅拟合几何或动力学参数。

#### 方法概述和架构

论文提出 CoRMA（Contrastive Robotic Motor Adaptation），把 RMA 改造成面向接触丰富装配的上下文式元适应框架。方法的核心是一个 6 维的仿真侧语义接触上下文，分别描述接触起始、侧向接触、引导式过渡、接触方向两个分量以及卡滞/粘滑倾向，这些量只在训练时由仿真提供。系统分三阶段训练：第一阶段在 Isaac Lab / Isaac Sim 中训练带有特权上下文输入的教师策略；第二阶段训练一个因果 Transformer 适配器，利用力、 proprioception 和动作历史在线预测该 6 维上下文；第三阶段在微调与真实部署时移除 oracle 上下文，改为把适配器预测的上下文注入策略。适配器训练同时使用语义回归损失和基于接触力状态的对比学习目标，以便让不同任务中但语义相似的接触历史在表示空间中聚类。整个方法不依赖示范、测试时梯度更新或特权输入，适合在单次 episode 内完成在线适应。

#### 实验结果分析

作者在 Isaac Lab / Isaac Sim 5.0 中的 PegInsert、GearMesh、NutThread 任务以及真实 Marvin 机械臂上评估了 CoRMA，并与 FORGE 系列基线比较。结果表明，尽管部分基线在仿真中成功率很高，但迁移到硬件后会显著退化；CoRMA 在受控目标位姿噪声条件下保留了更高的真实验证成功率。节选文本中未给出具体数值，但整体结论支持“语义接触推断”作为相关装配任务族中的可复用适应接口。作者也指出，当前方法主要验证了同一类装配任务之间的复用，未覆盖更广泛的未见任务泛化与 Real2Sim 标定问题。

<details>
<summary>完整摘要</summary>

我们提出 CoRMA（Contrastive Robotic Motor Adaptation），一种基于上下文的元适应框架，用于改造 RMA 以适应以力为主导的装配任务。CoRMA 不再直接回归原始仿真参数，而是使用一个紧凑的 6 维、仅依赖仿真的语义接触上下文，来描述接触起始、侧向接触、引导式过渡、接触方向以及卡滞情况。一个可部署的因果 Transformer 适配器，通过语义回归和力状态对比目标，从力觉、本体感知和动作历史中在线推断该上下文。部署时，oracle 上下文被移除并替换为推断得到的上下文，从而实现无需示范、无需特权输入、也无需梯度更新的单回合内适应。我们在 Isaac Lab / Isaac Sim 5.0 中的 PegInsert、GearMesh 和 NutThread 任务上，以及真实 Marvin 机械臂上评估了 CoRMA。与在仿真中成功率很高但在硬件上明显退化的 FORGE 基线相比，CoRMA 在受控目标位姿噪声条件下保持了更高且经过验证的真实成功率。这些结果表明，语义接触推断可以作为相关装配任务族中一种可复用的适应接口；而更广泛的未见任务泛化以及 Real2Sim 标定仍是未来工作。

</details>

---

### [[20_Research/Papers/世界模型/stable-worldmodel_A_Platform_for_Reproducible_World_Modeling_Research_and_Evaluation|stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation]]

![[assets/2605.21800_figure.png|800]]

- **arXiv**: [2605.21800](https://arxiv.org/abs/2605.21800)
- **PDF**: https://arxiv.org/pdf/2605.21800
- **详细分析**: [[20_Research/Papers/世界模型/stable-worldmodel_A_Platform_for_Reproducible_World_Modeling_Research_and_Evaluation|stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation]]
- **作者**: Lucas Maes, Quentin Le Lidec, Luiz Facury, Nassim Massaudi, Ayush Chaurasia, Francesco Capuano, Richard Gao, Taj Gillin, Dan Haramati, Damien Scieur, Yann LeCun, Randall Balestriero
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.16，世界模型 0.56）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

世界模型是构建能够进行推理、规划并泛化到训练分布之外的智能体的核心组件，广泛用于强化学习、机器人控制和具身智能等场景。但当前世界模型研究高度碎片化，不同论文往往各自维护代码库、数据管线和评测协议，导致复现困难、比较不公平，也很难判断性能提升究竟来自算法改进还是实现差异。作者指出，现有实践还受到三个关键瓶颈制约：一次性脆弱代码、视频数据加载缓慢，以及缺少统一的泛化基准，因此有必要建立一个可复现、可扩展的统一平台。

#### 方法概述和架构

论文提出 stable-worldmodel（swm），一个面向世界模型研究与评测的开源平台，目标是覆盖从数据采集、模型训练到规划控制和评估的完整流程。平台的核心由三个抽象组成：World 负责统一封装环境交互，支持向量化执行、渲染以及对视觉、几何和物理因素变化的可控干预；Policy 负责把观测或潜在状态映射到动作，包括随机策略、专家策略以及基于世界模型的 MPCPolicy；Solver 则实现单次射击式规划算法，如 CEM、MPPI、梯度下降、投影梯度下降等。数据层基于 Lance 构建，原生支持并可转换 MP4、HDF5 和 LeRobot 数据集，用于缓解视频 I/O 瓶颈并提高随机访问与吞吐效率。模型层提供现代世界模型基线的干净、经过测试的实现，如 DINO-WM、LeWorldModel、PLDM、TD-MPC2 等；推理时，MPCPolicy 会先将观测编码为潜在状态，再调用 Solver 在有限时域内优化动作序列，以最小化预测代价。平台还扩展了多个环境族与任务，并加入可控因素变化，用于系统评估动力学理解、控制性能、表征质量以及分布外泛化能力。

#### 实验结果分析

论文主要展示了 swm 在经典控制、MuJoCo、Atari、机器人以及开放世界环境上的统一评测能力，并提供了带有视觉、几何和物理扰动的零样本泛化测试设置。正文节选中强调，该平台可用于比较不同世界模型基线与规划求解器，并能检验模型在分布内规划与分布外条件下的脆弱性；可见文本未给出具体数值。作者还给出案例研究，分析了规划性能与零样本评测，结论是世界模型在分布偏移下仍然较脆弱，说明仅靠分布内任务成功并不能证明其真正学到了可迁移的动力学。

<details>
<summary>完整摘要</summary>

世界模型是构建能够进行推理、规划并超越训练数据进行泛化的智能体的核心。然而，当前世界模型研究高度碎片化，不同的代码库、数据管线和评测协议阻碍了可复现性与公平比较。现有实践还受到三个关键瓶颈限制：脆弱的一次性代码库、缓慢的视频数据加载，以及缺乏标准化的泛化基准。我们提出 stable-worldmodel（swm），这是一个用于标准化且可复现的世界模型研究与评测的开源平台。它提供了：（1）一个基于 Lance 的高性能数据层，原生支持 MP4、HDF5 和 LeRobot 数据集，并提供转换工具；（2）现代世界模型基线和规划求解器的简洁、经过充分测试的实现；（3）一套广泛的环境与任务，并扩展了可控的视觉、几何和物理变化因素，可用于系统性的仿真内评估，包括动力学理解、控制性能、表征质量以及分布外泛化。通过将完整流程统一到一个可扩展框架中，swm 显著降低了研究开销，并加速了面向可靠世界模型的可信进展。

</details>

---

### [[20_Research/Papers/大模型/Memory-R2_Fair_Credit_Assignment_for_Long-Horizon_Memory-Augmented_LLM_Agents|Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents]]

![[assets/2605.21768_figure.png|800]]

- **arXiv**: [2605.21768](https://arxiv.org/abs/2605.21768)
- **PDF**: https://arxiv.org/pdf/2605.21768
- **详细分析**: [[20_Research/Papers/大模型/Memory-R2_Fair_Credit_Assignment_for_Long-Horizon_Memory-Augmented_LLM_Agents|Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents]]
- **作者**: Sikuan Yan, Ahmed Bahloul, Ercong Nie, Susanna Schwarzmann, Riccardo Trivisonno, Volker Tresp, Yunpu Ma
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.9，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

面向多轮、多会话的记忆增强型 LLM Agent，核心任务是把跨会话的信息持续存入、更新并在后续任务中复用，从而突破有限上下文窗口的限制。这类系统在长期对话、个人助理和持续性任务中很有应用价值，但一旦引入强化学习训练，过去会话里写入、修改或删除记忆的动作会反过来改变未来环境，使不同 rollout 不再处于同一中间记忆状态。这样一来，像 GRPO 这类组相对优化方法默认的“同环境比较”假设被破坏，轨迹级奖励会给长时序记忆操作带来噪声甚至偏置的信用分配信号。因此，如何在长时程、多会话设置下对记忆操作进行公平、稳定且可学习的信用分配，是这篇论文关注的核心问题。

#### 方法概述和架构

论文提出 Memory-R2，核心算法是 LoGo-GRPO，将全局轨迹级优化与局部重放优化结合起来：全局分支保留端到端的长时程奖励学习，局部分支则从相同的中间记忆状态重新采样若干会话，对不同记忆操作结果做更公平的组内比较。系统结构上，作者把记忆构建拆成两个协作角色：事实抽取器负责从当前对话片段中提取关键信息，记忆管理器负责决定插入、更新或删除哪条记忆，两者共享同一个 LLM backbone，并通过不同角色提示词区分功能。为了避免抽取器和管理器输出长度不同带来的训练偏置，方法还采用按步骤归一化的强化学习目标，把一次抽取或一次管理调用视为一个决策步骤来计算重要性比率和优势。训练时，记忆构建被建模为跨 chunk 的多步过程，先在会话内逐块处理，再在跨会话层面用 LoGo-GRPO 做信用分配；同时引入课程学习，把训练会话长度从 8 逐步增加到 16 再到 32，以稳定长时程 RL 优化。

#### 实验结果分析

作者在多会话记忆 Agent 场景中进行了实验，比较对象包括已有的记忆 Agent 基线以及不同骨干模型和答案模块组合；评价指标覆盖 QA 质量、记忆失败率以及推理延迟等。结果显示，Memory-R2 在不同 backbone 上都能带来更好的准确率和更低的推理延迟，并且在较少训练对话的条件下依然具有较强的数据效率。消融分析表明，LoGo-GRPO、共享参数的抽取器-管理器设计以及课程学习都对最终性能有明显贡献。总体上，实验还展示了该方法在不同基准、模型规模与答案 Agent 上的泛化能力；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

记忆增强型 LLM Agent 能够通过跨会话存储、更新和复用信息，使交互超越有限上下文窗口。然而，在多会话环境中使用强化学习训练这类 Agent 具有挑战性，因为记忆会把 Agent 过去的动作变成其未来环境的一部分。一旦不同的 rollout 写入、更新或删除了不同的记忆，它们就不再共享相同的中间记忆状态，这会使轨迹级比较在根本上变得不公平。这违反了 GRPO 等组相对方法背后的一个关键假设，即不同 rollout 是从同一个等效环境中采样得到的。因此，轨迹级奖励会为长时程记忆操作提供噪声很大或带有偏差的信用分配信号。为了解决这一问题，我们提出 Memory-R2，一种面向长时程记忆增强型 LLM Agent 的训练框架。其核心算法 LoGo-GRPO 结合了局部和全局的组相对优化：全局目标保留了来自长时程轨迹级奖励的端到端学习，而局部重放则从相同的中间记忆状态出发，对不同记忆操作结果进行比较，从而得到更公平的组间比较，并为记忆构建提供更精确的监督。除了信用分配之外，Memory-R2 还通过共享参数的协同学习设计联合优化记忆形成与记忆演化，其中事实抽取器和记忆管理器通过角色特定提示词由同一个 LLM backbone 实例化。为了稳定跨多步、长时程的 RL 训练，我们采用渐进式课程学习，将训练时长从 8 个会话逐步增加到 16 个、再到 32 个。综合这些组件，Memory-R2 为长时程多会话场景下的记忆增强型 LLM Agent 提供了一种有效的训练范式。

</details>

---

### [[20_Research/Papers/强化学习/On_the_Sample_Complexity_of_Discounted_Reinforcement_Learning_with_Optimized_Certainty_Equivalents|On the Sample Complexity of Discounted Reinforcement Learning with Optimized Certainty Equivalents]]

![[assets/2605.21763_first_page.png|800]]

- **arXiv**: [2605.21763](https://arxiv.org/abs/2605.21763)
- **PDF**: https://arxiv.org/pdf/2605.21763
- **详细分析**: [[20_Research/Papers/强化学习/On_the_Sample_Complexity_of_Discounted_Reinforcement_Learning_with_Optimized_Certainty_Equivalents|On the Sample Complexity of Discounted Reinforcement Learning with Optimized Certainty Equivalents]]
- **作者**: Oliver Mortensen, Mohammad Sadegh Talebi
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

这篇论文研究的是折扣马尔可夫决策过程中的风险敏感强化学习，目标不再只是最大化期望回报，而是直接优化对回报分布更敏感的风险度量。该问题在医疗、金融、运筹和交通等高风险场景中很重要，因为这些场景往往更关心尾部损失和波动，而不是平均表现。现有大量理论主要集中在风险中性或非递归风险目标上，对递归 OCE（Optimized Certainty Equivalent）这一更适合逐步控制风险的设定，尤其是在折扣 MDP 的样本复杂度上，仍缺乏系统刻画。

#### 方法概述和架构

论文考虑在有生成式模型（generative model）的有限折扣 MDP 中学习递归 OCE 下的最优状态-动作价值函数和最优策略。作者以一类由效用函数 u 定义的 OCE 为核心，研究哪些 u 对应的目标是 PAC 可学习的，并给出完整的可学习性刻画。方法上提出了一个基于模型的算法 MB-OCE-VI，即先利用生成器采样估计转移结构，再在经验模型上进行 OCE 版价值迭代，输出近似最优 Q 函数或策略。论文进一步分析该算法在 value learning 与 policy learning 两类任务上的样本复杂度，并用下界证明其依赖关系在状态-动作空间规模上是紧的。

#### 实验结果分析

论文给出了递归 OCE 强化学习的首批上界与下界结果：对满足特定条件的效用函数，MB-OCE-VI 可达到 PAC 样本复杂度保证；而当效用函数的定义域不是整个实数轴时，相应问题根本不可 PAC 学习。作者还证明了 value learning 和 policy learning 的下界在 S 和 A 的依赖上是紧的，并为更受限的效用类给出了显式体现有效时域 1/(1-γ) 的下界。对 CVaR_τ，论文指出其关于 τ 的正确依赖应为 1/τ^2，相比已有最优状态结果改进了一个 1/τ 的因子；但这一下界在 1/(1-γ) 上仍不是最优。可见文本未给出具体实验数值。

<details>
<summary>完整摘要</summary>

本文研究有限折扣 MDP 中的风险敏感强化学习，并假设可以访问该 MDP 的生成式模型。我们考虑一类称为优化确定性等价（optimized certainty equivalent，OCE）的风险度量，它包含熵风险、CVaR 和均值-方差等重要风险度量。我们的重点是，在递归 OCE 设定下，学习最优状态-动作价值函数（value learning）以及最优策略（policy learning）的样本复杂度。我们给出了与效用函数 u 相对应的 OCE 何时定义出一个 PAC 可学习目标的精确刻画。我们分析了一个简单的基于模型的方法，并推导出 PAC 样本复杂度上界。我们证明，只要 u 的定义域不是整个实数轴，即 dom(u)≠R，那么对应问题就不是 PAC 可学习的。最后，我们分别为 value learning 和 policy learning 建立了相应的下界，证明它们在状态-动作空间规模 SA 上是紧的；对于更受限的一类效用函数，我们进一步导出了显式体现有效时域 1/(1-γ) 的下界。特别地，对于 CVaR_τ，我们证明其关于 τ 的正确依赖是 1/τ^2，这比当前最优方法改进了一个 1/τ 的因子，尽管我们的下界在 1/(1-γ) 上并非最优。

</details>

---

### [[20_Research/Papers/大模型/AutoMCU_Feasibility-First_MCU_Neural_Network_Customization_via_LLM-based_Multi-Agent_Systems|AutoMCU: Feasibility-First MCU Neural Network Customization via LLM-based Multi-Agent Systems]]

![[assets/2605.21560_figure.png|800]]

- **arXiv**: [2605.21560](https://arxiv.org/abs/2605.21560)
- **PDF**: https://arxiv.org/pdf/2605.21560
- **详细分析**: [[20_Research/Papers/大模型/AutoMCU_Feasibility-First_MCU_Neural_Network_Customization_via_LLM-based_Multi-Agent_Systems|AutoMCU: Feasibility-First MCU Neural Network Customization via LLM-based Multi-Agent Systems]]
- **作者**: Penglin Dai, Zijie Zhou, Xincao Xu, Junhua Wang, Xiao Wu, Lixin Duan
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

在微控制器单元（MCU）上部署神经网络，是边缘智能落地的重要方向，适用于智能家居、工业控制、医疗和农业等低功耗、低时延场景。但 MCU 同时受限于 RAM、Flash 和算力，导致模型不仅要“效果好”，还必须真正可部署。现有的模型压缩和硬件感知 NAS 往往依赖代理指标，难以及时发现算子不兼容、内存超限或工具链转换失败等问题，实际开发仍然需要大量人工试错。本文关注的就是“先确保可部署，再谈精度优化”的 MCU 定制问题，因此具有较强的工程实用价值。

#### 方法概述和架构

论文提出 AutoMCU，一个基于 LLM 的多智能体系统，用于在 MCU 约束下自动定制神经网络。系统接收自然语言形式的任务需求和硬件规格，Supervisor 负责调度三个核心模块：Proposal Agent 生成结构化候选网络，Evaluation and Conversion Agent 先调用厂商工具链检查 RAM/Flash 和后端兼容性，Training Agent 只对通过可行性筛选的模型进行训练与评估。整个流程采用闭环迭代：候选架构先被硬件在环机制筛掉不可部署方案，再进行受控训练，最后用后端验证确认是否真的能部署到目标 MCU。论文还设计了状态隔离的多智能体编排机制，使提案、训练、评估和部署阶段通过结构化摘要进行交互，从而提升长流程自动化的稳定性。

#### 实验结果分析

作者在 CIFAR-10 和 CIFAR-100 上、并在严格 MCU 约束下对 AutoMCU 进行验证，与面向 MCU 的 HW-NAS 基线以及 ColabNAS、GENIUS 等 LLM-based NAS 方法做了比较。结果显示，AutoMCU 在保持有竞争力精度的同时，将定制时间缩短到约 1–2 小时，而代表性 MCU-oriented HW-NAS 基线往往需要数百 GPU 小时。论文还在 NAS-Bench-201 上做了对比实验，并进行了消融分析，表明后端可验证的可行性检查、历史反馈和模块化编排有助于提升搜索效率与稳定性。最后，多个 STM32 微控制器上的真实部署进一步证明了方法的实际可用性；若只看节选文本，则具体数值细节未给出。

<details>
<summary>完整摘要</summary>

在微控制器单元（MCU）上部署神经网络对边缘智能至关重要，但由于内存、存储和计算资源极其紧张，这一任务仍然充满挑战。现有方法，如模型压缩和硬件感知神经架构搜索（HW-NAS），往往依赖代理指标、搜索成本高，而且并未真正打通架构设计与已验证部署之间的鸿沟。本文提出 AutoMCU：一种面向 MCU 约束、以可行性优先的、基于大语言模型（LLM）的多智能体系统，用于自动化神经网络定制。给定自然语言形式的任务需求和硬件规格，AutoMCU 会迭代生成结构化架构候选，在训练之前借助厂商工具链反馈筛除不可行设计，在受控协议下评估可行模型，并通过后端支持的部署分析验证其可部署性。AutoMCU 包含两个关键机制：1）硬件在环的架构生成，用于在 RAM 和 Flash 约束下尽早剔除无法部署的候选；2）状态隔离的多智能体调度机制，用于在提案、训练、评估和部署阶段实现稳定协同。基于 CIFAR-10 和 CIFAR-100 的实验表明，在严格 MCU 约束下，AutoMCU 能够取得具有竞争力的准确率，同时将定制时间降低到约 1–2 小时；相比之下，代表性的面向 MCU 的 HW-NAS 基线往往需要数百小时的 GPU 时间。进一步与 NAS-Bench-201 上的 ColabNAS 和基于 LLM 的 NAS 方法 GENIUS 的比较，也证明了 AutoMCU 的有效性与稳定性。对多个 STM32 微控制器的真机部署结果则验证了其在 MCU 规模边缘智能中的实际适用性。

</details>

---
