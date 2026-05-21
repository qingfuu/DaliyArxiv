# cs.RO | Robotics | 2026-05-20

#arxiv #ComputerScience

**论文数**: 23

### [[20_Research/Papers/具身智能/CEER_Compliant_End-Effector_and_Root_Control_as_a_Unified_Interface_for_Hierarchical_Humanoid_Loco-Manipulation|CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation]]

![[assets/2605.19981_figure.png|800]]

- **arXiv**: [2605.19981](https://arxiv.org/abs/2605.19981)
- **PDF**: https://arxiv.org/pdf/2605.19981
- **详细分析**: [[20_Research/Papers/具身智能/CEER_Compliant_End-Effector_and_Root_Control_as_a_Unified_Interface_for_Hierarchical_Humanoid_Loco-Manipulation|CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation]]
- **作者**: Xinyuan Luo, Xingrui Chen, Xunjian Yin, Hongxuan Wu, Boxi Xia, Zhuoqun Chen, Jinzhou Li, Boyuan Chen, Xianyi Cheng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

人形机器人虽然已经在行走与动态运动上取得不错进展，但在接触丰富、时间跨度长的操作任务中仍然存在明显瓶颈。此类任务不仅要求稳定的全身控制和顺应性，还需要一种便于高层规划器直接调用的任务接口，而不是依赖难以跨机器人迁移的关节空间轨迹。本文关注的正是人形机器人在日常环境中的“走—抓—搬—放”一体化能力，因此提出一种更适合层级规划与模块化集成的控制抽象，具有较强的系统研究价值。

#### 方法概述和架构

论文提出 CEER（Compliant End-Effector and Root Control），将根部运动与末端执行器位姿统一到一个 EE-root 任务空间中，作为人形 loco-manipulation 的低层执行接口。作者先用一个具备阻抗式顺应行为的全身运动跟踪 teacher policy 进行训练，teacher 接收关节空间参考以及外力、模拟状态等特权信息，以学习稳定的全身控制能力。随后通过 teacher–student 框架蒸馏出 student policy，使其只依赖 EE-root 命令和本体感知信息，就能输出底层关节动作。系统层面上，论文进一步搭建三层层级架构：高层由语言或任务管理器选择任务，中层由可插拔的行走与操作技能产生统一的 EE-root 指令，低层由 CEER 将这些指令转换为可执行的全身控制。这样一来，不同规划器和技能模块都可以通过同一接口接入，而无需重新训练底层策略。

#### 实验结果分析

作者在仿真与真实机器人上评估了 CEER 的控制与系统效果。实验显示，该方法可实现 3.3 cm 的末端执行器跟踪精度，并且相较基线具有明显更低的 jerk，说明其在接触操作中更平稳。真实机 teleoperation 实验表明，CEER 能支持稳定的接触丰富操作；在房间尺度的单物体 loco-manipulation 仿真任务中，最高成功率达到 70%。从节选内容看，未给出更完整的基线列表与消融细节，因此可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

尽管人形机器人已经在运动能力方面取得了令人印象深刻的进展，但接触丰富且长时程的操作仍然是一个主要瓶颈。操作本质上具有强接触特性，要求稳定的相互作用需要具备顺应性的全身控制；同时，操作任务的多样性和长时程特征又更适合模块化、兼容规划器的接口，而不是关节空间跟踪。为此，我们提出 CEER，一种顺应性的末端执行器—根部（EE-root）控制抽象，用于层级规划框架中的模块化人形 loco-manipulation。CEER 在一个由根部运动指令和末端执行器位姿目标定义的、可解释的任务空间中，实现了具备顺应感知的全身控制，并支持与异构高层规划器即插即用地集成。我们采用 teacher–student 框架，将一个通用的运动跟踪控制器蒸馏为一个只接收 EE-root 指令的低层策略。进一步地，我们构建了一个层级系统，通过 EE-root 接口集成异构规划器和任务模块，使得无需重新训练底层全身策略即可完成多种操作任务。仿真和实机实验表明，CEER 的末端执行器跟踪精度达到 3.3 cm，同时相较基线显著降低了 jerk；在遥操作下可实现稳定的接触丰富操作；在房间尺度环境中的模拟单物体 loco-manipulation 任务上，成功率最高可达 70%。这些结果表明，顺应性的 EE-root 控制为人形 loco-manipulation 提供了一种实用抽象，能够实现多样技能的模块化、可扩展集成。

</details>

---

### [[20_Research/Papers/具身智能/TravExplorer_Cross-Floor_Embodied_Exploration_via_Traversability-Aware_3-D_Planning|TravExplorer: Cross-Floor Embodied Exploration via Traversability-Aware 3-D Planning]]

![[assets/2605.19958_figure.jpg|800]]

- **arXiv**: [2605.19958](https://arxiv.org/abs/2605.19958)
- **PDF**: https://arxiv.org/pdf/2605.19958
- **详细分析**: [[20_Research/Papers/具身智能/TravExplorer_Cross-Floor_Embodied_Exploration_via_Traversability-Aware_3-D_Planning|TravExplorer: Cross-Floor Embodied Exploration via Traversability-Aware 3-D Planning]]
- **作者**: Han Zheng, Zhe Chen, Yudong Huang, Haoran Liu, Jinghao Wang, Ming Yang, Tong Qin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

零样本目标导航（ZSON）旨在让机器人在未知环境中根据开放词汇目标去寻找物体，适合“找灭火器”“找椅子”这类真实服务与巡检任务。但现有方法大多仍建立在二维平面地图和单楼层假设上，在真实建筑里，一旦涉及楼梯、平台、跨层重叠空间，这种表示就会失效。TravExplorer 关注的正是“跨楼层具身探索”这一更贴近现实的难题：机器人不仅要找目标，还要理解哪些表面可通行、如何跨楼层连通，以及如何在视野受限时持续完成探索。

#### 方法概述和架构

TravExplorer 以统一的三维体素地图为核心，同时维护占据结构层与可通行支撑面层，用来区分墙体、家具等障碍物与地面、楼梯、平台等机器人可落脚区域。系统先从连通的可通行支撑面中提取“可通行前沿”，并结合面向视场（FOV-aware）的主动感知策略，补全楼梯等区域因观测不完整导致的连通性缺失。语义部分采用轻量级引导模块，将在线开放词汇分割得到的概率实例地图与快速图文匹配得到的空间价值图对齐，从而减少大模型推理延迟，并把目标相关线索与可达区域联系起来。在规划层面，系统通过层次化规划器对对象假设、可通行前沿和楼梯地标进行目标感知的前沿巡游，再利用踏点引导的三维搜索和垂直约束的局部轨迹优化，生成可执行的跨楼层运动。整体流程是“感知—更新地图—语义引导—全局巡游—三维路径搜索—局部优化—执行反馈”闭环运行。

#### 实验结果分析

作者在 HM3D 和 MP3D 上进行了 4,195 个仿真回合实验，并与代表性的 ObjectNav 基线对比，结果显示 TravExplorer 能稳定取得更优表现。除此之外，论文还在 Unitree Go2 上完成了 50 次真实机器人实验，验证了其在单楼层和跨楼层室内环境中的开放词汇目标搜索能力。节选文本未给出具体数值，但明确表明该方法在无需先验地图、无需人工干预的条件下仍能保持较强泛化能力。

<details>
<summary>完整摘要</summary>

零样本目标导航（ZSON）在未见环境中的开放词汇目标搜索方面展现出良好前景，但现有大多数系统仍局限于平面表示和单楼层假设。在真实建筑中，这些假设已不再适用，因为导航往往涉及楼层、楼梯、平台以及垂直重叠空间。本文提出 TravExplorer，一种将零样本语义引导与具备可通行性意识的三维规划相结合的跨楼层具身探索框架。TravExplorer 维护一个统一的体素地图，用于区分占据结构与机器人可到达的支撑表面，并从连通的支撑表面中提取可通行前沿，这些支撑表面包括地面、楼梯和平台。进一步地，面向视场的主动感知策略用于解决跨楼层穿越过程中的不完整观测问题。为降低语义推理延迟，系统设计了一个轻量级引导模块，将在线开放词汇分割得到的概率实例地图与快速图文匹配得到的空间价值图进行对齐。基于这些几何与语义记忆，层次化规划器会围绕对象假设、可通行前沿和楼梯地标执行目标感知的前沿巡游，并通过踏点引导的三维搜索以及垂直约束的局部轨迹优化，生成可执行的跨楼层运动。作者在 HM3D 和 MP3D 上进行了 4,195 个仿真回合实验，结果表明该方法相较代表性的 ObjectNav 基线具有稳定优势。随后在 Unitree Go2 上开展的 50 次真实世界实验进一步验证了该方法无需先验地图或人工干预即可在单楼层与跨楼层室内环境中完成开放词汇目标搜索。代码将发布于 https://github.com/wuyi2121/TravExplorer 。

</details>

---

### [[20_Research/Papers/具身智能/RoHIL_Robust_Human-in-the-Loop_Robotic_Reinforcement_Learning_Against_Illumination_Variations|RoHIL: Robust Human-in-the-Loop Robotic Reinforcement Learning Against Illumination Variations]]

![[assets/2605.19924_figure.png|800]]

- **arXiv**: [2605.19924](https://arxiv.org/abs/2605.19924)
- **PDF**: https://arxiv.org/pdf/2605.19924
- **详细分析**: [[20_Research/Papers/具身智能/RoHIL_Robust_Human-in-the-Loop_Robotic_Reinforcement_Learning_Against_Illumination_Variations|RoHIL: Robust Human-in-the-Loop Robotic Reinforcement Learning Against Illumination Variations]]
- **作者**: Shuoqin Zhang, Yixin Xiong, Xiru Gao, Kai Liu, Ke Wang, Xichuan Zhou, Zhe Hu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.5（加权：具身智能 0.6，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

在人机协同强化学习（HIL-RL）的真实机器人操作中，系统往往只能在训练时所在的工作台上取得很高成功率，一旦机器人被移到几米外、灯具位置或窗光变化后的新工作台，视觉分布就会明显偏移，策略性能随之崩溃。对于需要反复部署到不同工位的工业场景来说，若每个工作台都重新收集示范并重新进行HIL训练，成本过高且不具可扩展性；而直接在光照变化数据上微调，又容易引发灾难性遗忘，导致原工作台性能下降。因而，如何在不增加真实机器人交互的前提下，让已训练好的HIL策略对光照变化保持鲁棒，同时不忘掉源工作台能力，是这篇论文关注的核心问题。

#### 方法概述和架构

论文提出 RoHIL，一个面向光照变化的离线微调框架，目标是在不进行额外真实机器人交互的情况下，把单次源工作台的 HIL-SERL 训练结果迁移到新的照明条件。第一步，利用世界模型式图像重光照模块，对源工作台轨迹中的视觉帧在多个虚拟 HDRI 环境下重新合成，从而生成光照多样化的训练观测，但保留原始动作、奖励和终止信号不变。第二步，引入 Illumination-Retention Replay（IRR），在回放时交替混合“重光照适应样本”和“原始光照保留样本”，以维持源工作台的 Bellman 覆盖并缓解遗忘。第三步，再加入 anchored Bellman–actor 正则项，用冻结的源策略作为锚点，分别约束 critic 的表示漂移和 actor 的策略漂移，使模型既能适应新光照又不偏离原策略。整体流程是：先收集源工作台 HIL 数据，再离线生成多光照视图，随后通过带 IRR 的 SAC 式更新与锚定正则进行微调，最终输出对跨工作台照明变化更稳健的策略。

#### 实验结果分析

作者在四个真实机器人操作任务上验证了 RoHIL，包括 RAM 插入、USB 插入、断路器拨动和桌面擦拭，并与标准 HIL-RL 及若干相关基线进行比较。结果表明，在显著的跨工作台光照变化下，常规 HIL-RL 会明显失效，而 RoHIL 能在移位光照环境中显著提升成功率，同时尽量保持源工作台性能不下降。消融实验还分析了锚定目标函数、IRR 的原始/重光照混合比例以及各组件组合的作用，整体结论支持“IRR + 锚定正则”的联合设计优于单独使用任一模块。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

人机协同强化学习系统在训练所在的工作台上通常能够达到几乎完美的成功率，但当同一机器人被移动到几米外、由于新的灯具位置和窗外光照变化导致视觉输入分布发生偏移的工作台时，性能会迅速崩溃。为每个工作台重新收集示范并重新运行 HIL 与实际部署需求不相符；而直接在光照偏移数据上进行微调，又会触发对源工作台的灾难性遗忘。为弥合这一跨域差距，我们提出 RoHIL，这是一个不需要额外真实机器人交互的离线微调框架。RoHIL 结合了三部分：(i) 一个基于世界模型的图像重光照器，它在多个虚拟 HDRI 环境下重新合成源工作台轨迹的视觉流，而动作和奖励保持真实不变；(ii) Illumination-Retention Replay（IRR），一种数据层面的抗遗忘机制，它将重光照后的适应转移与原始光照的保留转移交错采样，以维持源工作台的 Bellman 覆盖；(iii) 一个锚定的 Bellman–actor 正则项，用于约束表示和策略相对源工作台原始策略的漂移。在四个真实机器人操作任务中，面对显著的跨工作台照明变化，RoHIL 在标准 HIL-RL 崩溃的场景下显著提升了移位光照条件下的表现，同时保留了源工作台性能，消除了针对每个新工作台和新环境重新收集数据并重新训练的需要。

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Action_Residuals_Real-World_Robot_Policy_Steering_via_Bottleneck_Latent_Reinforcement_Learning|Beyond Action Residuals: Real-World Robot Policy Steering via Bottleneck Latent Reinforcement Learning]]

![[assets/2605.19919_figure.png|800]]

- **arXiv**: [2605.19919](https://arxiv.org/abs/2605.19919)
- **PDF**: https://arxiv.org/pdf/2605.19919
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Action_Residuals_Real-World_Robot_Policy_Steering_via_Bottleneck_Latent_Reinforcement_Learning|Beyond Action Residuals: Real-World Robot Policy Steering via Bottleneck Latent Reinforcement Learning]]
- **作者**: Dongjie Yu, Kun Lei, Zhennan Jiang, Jia Pan, Huazhe Xu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.5（加权：具身智能 0.6，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

机器人操作中的模仿学习预训练策略已经能较好复现复杂动作，但在真实部署时仍常因执行误差、演示数据覆盖不足以及分布偏移而失败，因此通常还需要在线强化学习继续改进。现有轻量级后训练方法多直接在动作空间做残差修正，但这种做法容易产生噪声大、结构性弱的探索，既影响样本效率，也可能带来不稳定甚至不安全的行为。本文关注“强化学习应如何在不破坏预训练能力的前提下高效微调机器人策略”这一问题，提出了一个更结构化的中间接口来进行在线适应。

#### 方法概述和架构

论文提出 Z-Perturbation Reinforcement Learning（ZPRL），核心思想是在冻结预训练策略主体的前提下，不直接改动作或权重，而是在一个紧凑的瓶颈潜变量上做 RL 扰动。离线训练阶段，作者给模仿策略插入一个可即插即用的变分信息瓶颈（VIB）模块，从观测嵌入中提取与任务相关的潜变量接口；这个潜变量再经过解码后，作为冻结动作生成器的条件输入。在线微调阶段，基础策略参数保持不变，RL 只学习对该瓶颈潜变量的残差扰动，从而把探索从低层动作命令转移到更有结构的潜空间。文中将该方法实例化到 flow-matching 策略上，并在仿真和真实机器人任务中验证其效果。

#### 实验结果分析

作者在 8 个仿真任务和 4 个真实世界操作任务上评估了 ZPRL，并与强基线后训练方法比较。结果显示，ZPRL 在样本效率和最终性能上都优于对照方法；在真实世界的 4 个任务上，相比模仿基线，平均成功率提升了 33.7%。此外，ZPRL 相比动作残差方法表现出更平滑、更一致的探索行为，说明瓶颈潜变量接口能更好地约束在线 RL 的更新方向。具体消融与部分指标数值在节选文本中未完整给出。

<details>
<summary>完整摘要</summary>

预训练模仿策略已经成为机器人操作的重要基础，但它们通常仍需要在线改进，以克服执行误差、数据集覆盖有限以及部署环境不匹配等问题。因此，一个核心问题是：在离线预训练之后，强化学习应如何对策略进行自适应。现有的轻量级方法通常直接在动作空间中施加残差修正，但这往往会导致噪声较大且结构性较差的探索。在这项工作中，我们提出 Z-Perturbation Reinforcement Learning（ZPRL），一种通过紧凑的瓶颈潜变量来引导预训练策略的方法，而不是通过策略权重或输出动作来进行调节。在离线训练阶段，我们为策略增加一个可即插即用的变分信息瓶颈（VIB）模块，从观测嵌入中提取一个与任务相关的潜变量接口。在在线微调阶段，基础策略保持冻结，RL 只学习对该潜变量的残差扰动，其解码后的表示作为条件输入到冻结的动作生成器中。我们将 ZPRL 实例化在 flow-matching 策略上，并在 8 个仿真任务和 4 个真实世界任务上进行评估。跨越不同的操作场景，ZPRL 在样本效率和最终性能上都优于强力的后训练基线。在真实世界中，ZPRL 相比模仿基础策略，在四个任务上的平均成功率提升了 33.7%，同时相较于动作残差方法表现出更平滑的探索行为。这些结果表明，一个紧凑、与任务对齐的瓶颈潜变量，可以作为在线 RL 适应的有效接口。更多视频可见：https://manutdmoon.github.io/ZPRL/。

</details>

---

### [[20_Research/Papers/机器人/DAG-Based_QoS-Aware_Dynamic_Task_Placement_for_Networked_Multi-Stage_Control_Pipelines|DAG-Based QoS-Aware Dynamic Task Placement for Networked Multi-Stage Control Pipelines]]

![[assets/2605.19887_figure.png|800]]

- **arXiv**: [2605.19887](https://arxiv.org/abs/2605.19887)
- **PDF**: https://arxiv.org/pdf/2605.19887
- **详细分析**: [[20_Research/Papers/机器人/DAG-Based_QoS-Aware_Dynamic_Task_Placement_for_Networked_Multi-Stage_Control_Pipelines|DAG-Based QoS-Aware Dynamic Task Placement for Networked Multi-Stage Control Pipelines]]
- **作者**: Thien Tran, Jonathan Kua, Thuong Hoang, Minh Tran, Yuemin Ding, Jiong Jin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

这篇论文面向网络化多阶段控制流水线中的任务放置问题，具体场景是具身智能/机器人中的视觉伺服与感知-规划-控制闭环。作者指出，随着 Physical AI 负载变重，机器人本体上的感知与规划计算越来越吃紧，而把感知任务静态卸载到边缘侧又会在工业实时网络下引入抖动与时延风险。现有自适应任务放置方法往往只处理单个流水线阶段，且缺少对多阶段 DAG 结构、任务切换开销以及闭环 QoS 的统一建模，因此很值得关注。

#### 方法概述和架构

论文提出 DAG-Based QoS-Aware Dynamic Task Placement（DTP）框架，把四阶段感知-感知/理解-规划-控制流水线建模为有向无环图（DAG），并显式区分硬绑定在机器人上的前后两端阶段与可迁移的中间阶段。系统为每个任务定义可放置节点集合、计算开销和节点利用率，为任务边定义通信时延，并据此计算端到端时延。决策层以窗口为单位收集 95 分位端到端时延、截止期违约率、机器人/边缘 CPU 利用率等指标，构造包含切换惩罚的多目标代价函数 J_k。随后在三个可解释候选放置方案（完全本地、静态卸载、混合）中做最小化搜索，并通过 hysteresis（Δ_min）与最小驻留窗口数（N_min）抑制频繁抖动。算法在边缘节点上运行，既能基于离线 profiling 估计非当前放置方案的 QoS，也支持在线仿真/保守估计来更新比较结果。

#### 实验结果分析

从正文节选可见，这篇工作目前属于 WiP（Work-in-Progress），重点给出的是理论框架、定性分析以及两阶段验证路线图，而非完整的最终实验结论。作者计划在离散事件仿真和硬件在环（HIL）环境中验证该 DTP 策略，并与 LOC、SO 以及此前的 ATP 基线进行比较，指标包括尾部时延、deadline violation rate 和资源利用率等。节选中明确强调了设计目标是将 V_D 控制在 5% 以内，但可见文本未给出具体数值结果。

<details>
<summary>完整摘要</summary>

当前的 Physical AI（PAI）高度依赖闭环视觉伺服流水线，其中的感知与规划阶段由于机器人上嵌入了复杂模型，可能在本体侧变得计算密集。在实践中，对于基于标准工业网络、且对时延高度敏感、精度要求极高的工业场景来说，将感知任务静态卸载到现场边缘并不合适。这凸显了工业自动化中控制-通信-计算（3C）协同设计的重要性：单体式本地执行会使 AI 加速的机器与机器人硬件饱和，而静态边缘卸载会让控制回路暴露在网络抖动之下。现有自适应任务放置（ATP）控制器可以在一定程度上缓解这一问题，但它们通常基于二元阈值规则只迁移流水线中的单个阶段，缺少多阶段模型，也没有对放置切换显式建模代价。本文作为一篇 Work-in-Progress（WiP）论文，提出了一种基于有向无环图（DAG）的、面向服务质量（QoS）的动态任务放置（DTP）框架，用于网络化机器人中的感知-理解-规划-控制流水线。该流水线被形式化为一个 DAG，并带有任务级与节点级属性，用于描述计算开销、通信时延以及可行放置集合；在一个小而可解释的候选集合（完全本地、静态卸载、混合）上，基于窗口的代价函数将尾部端到端时延、截止期违约率、硬件利用率和汉明距离形式的切换惩罚结合起来，同时带有迟滞机制与最小驻留时间约束的 DTP 算法，用于限制放置抖动。本文还给出了理论框架、结构化定性分析，以及分两阶段的仿真加硬件在环验证路线图。

</details>

---

### [[20_Research/Papers/机器人/Justifying_bio-inspired_robotics_research_A_taxonomy_of_strategies|Justifying bio-inspired robotics research: A taxonomy of strategies]]

![[assets/2605.19840_figure.png|800]]

- **arXiv**: [2605.19840](https://arxiv.org/abs/2605.19840)
- **PDF**: https://arxiv.org/pdf/2605.19840
- **详细分析**: [[20_Research/Papers/机器人/Justifying_bio-inspired_robotics_research_A_taxonomy_of_strategies|Justifying bio-inspired robotics research: A taxonomy of strategies]]
- **作者**: Margaret J. Zhang, Justin Ting, Talia Y. Moore
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

生物启发机器人研究常常被笼统地贴上“bio-inspired”标签，但不同工作在目标、方法和贡献上差异很大，导致读者和资助方很难判断其价值与适用边界。尤其在机器人领域，研究者有时只是借用了生物中的某种能力作为设计目标，有时则是直接复现生物机制、形态或感知外观，这些路径混在一起容易引发“看起来像生物但缺乏实质贡献”的质疑。本文关注的正是如何为生物启发式机器人研究建立更清晰的论证框架，使研究者能够更准确地说明自己的设计动机、预期贡献和适合的学术/资助场景。

#### 方法概述和架构

论文采用综述与分类学构建的方法，对生物启发式机器人研究的常见策略进行系统归纳，并提出一套动机—贡献导向的 taxonomy。作者将相关工作划分为若干类别，包括任务型生物启发、机制型生物启发、还原式仿生、感知型仿生、机器人实验平台、bioexploitation 和 backspiration 等，并说明这些类别在“对生物的参与程度”和“对科学/工程的贡献”两个维度上的差异。每一类都给出其典型定义、适合的研究问题、可能的贡献形式，以及更匹配的发表、展示和资助渠道。文中还进一步讨论了类别之间的重叠关系，以及 bio-inspired spinoffs、复合类比、bio-inspired algorithms 和 neuromorphic robotics 等相关方向，帮助研究者把自己的工作放入更合适的语境中。

#### 实验结果分析

这篇论文的主要产出不是实验性能提升，而是一套可操作的分类体系和判别思路，用于解释不同生物启发策略各自的价值边界。节选文本中未给出具体数值实验结果，因而无法报告定量指标。作者强调，该 taxonomy 有助于减少术语使用上的模糊性，缓解读者对“生物启发”贡献预期与实际成果之间的不匹配。

<details>
<summary>完整摘要</summary>

在人类历史的大部分时间里，我们并没有系统地思考如何以及为何将自然世界的某些特征融入设计之中。缺乏系统化方法导致了动机与方法上的不一致，使得预测或评估生物启发式设计的成功变得困难。这种预期与结果之间的不匹配，可能会让读者认为某个生物启发式设计只是表面化、薄弱或不完整的，进而产生失望。机器人领域尤为如此，因为与某个生物系统的相似性本身就可能是构建机器人的核心动机。为了帮助机器人研究者为其特定的生物启发方法提供论证，也为了帮助资助项目管理者辨别不同生物启发方法的价值，本文提出了一套针对生物启发式设计动机的分类体系，并描述了不同方法可能带来的潜在重要贡献。

</details>

---

### [[20_Research/Papers/具身智能/KIO-planner_Attention-Guided_Single-Stage_Motion_Planning_with_Dual_Mapping_for_UAV_Navigation|KIO-planner: Attention-Guided Single-Stage Motion Planning with Dual Mapping for UAV Navigation]]

![[assets/2605.19703_figure.jpg|800]]

- **arXiv**: [2605.19703](https://arxiv.org/abs/2605.19703)
- **PDF**: https://arxiv.org/pdf/2605.19703
- **详细分析**: [[20_Research/Papers/具身智能/KIO-planner_Attention-Guided_Single-Stage_Motion_Planning_with_Dual_Mapping_for_UAV_Navigation|KIO-planner: Attention-Guided Single-Stage Motion Planning with Dual Mapping for UAV Navigation]]
- **作者**: Dexing Yao, Haochen Li, Junhao Wei, Yifu Zhao, Yanxiao Li, Jiahui Xu, Jinxuan Hu, Lele Tian, Baili Lu, Zikun Li, Xu Yang, Sio-Kei Im...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

该工作面向狭窄、墙体密集环境中的无人机自主飞行，例如室内导航、狭长走廊穿行和工业设施巡检。在这类场景下，规划器既要保持低时延，又要满足严格的安全与运动学约束。传统基于优化的规划方法虽然成熟，但常受制于地图构建带来的延迟，并且在复杂障碍中容易陷入局部最优；端到端学习方法虽然更快，却往往难以从原始深度图中提取精细几何信息，也缺少硬性的动力学与避障约束，因此在贴近墙壁飞行时更容易发生不可预测碰撞。

#### 方法概述和架构

作者提出 KIO-planner，一种注意力引导的单阶段轨迹规划框架，直接以当前深度图和无人机运动状态作为输入，输出一组候选运动原语及其置信度。方法首先在感知骨干网络中嵌入 CBAM，通过通道注意力和空间注意力联合强调墙面边缘、窄通道和可通行区域，从而增强深度图几何特征的提取能力。随后引入 Dual Mapping 机制：其一用 tanh 将网络输出映射到无人机的速度、加速度和位置等物理边界内，并据此解析生成五次多项式轨迹；其二将候选轨迹投影回当前深度图像素空间，利用确定性的 Geometric Safety Shield 逐点检查轨迹是否违反安全半径，从而在不融合全局地图的情况下拒绝不安全轨迹。整体训练采用无监督的 OBVP 形式，损失由平滑性、安全性和引导项组成，推理时则是单阶段前向计算，避免了显式建图与复杂优化。

#### 实验结果分析

作者在高保真仿真环境中进行了大量实验，场景重点覆盖高密度墙体和狭窄约束空间，并与当前最优基线进行了对比。结果显示，KIO-planner 可支持最高 3.0 m/s 的高速导航，推理时延约为 24 ms，轨迹也更加平滑，控制代价降低 28.4%。最重要的是，Dual Mapping 将最坏情况下的障碍物最小距离从 0.48 m 提升到 0.76 m，说明其安全裕度显著增强。正文节选中还提到包含消融实验与轨迹可视化分析，但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

在墙体密集、空间受限的环境中实现自主无人机飞行，需要在严格安全约束下进行低时延且可靠的运动规划。传统基于优化的规划器会受到建图时延影响，在穿越密集结构障碍时也容易陷入局部最优。与此同时，现有端到端学习方法难以从原始深度图中提取细粒度几何特征，并且缺少硬性的运动学约束，导致在靠近墙面时更容易发生不可预测的碰撞。为了解决这些问题，我们提出 KIO-planner，一种注意力引导的单阶段轨迹规划框架。首先，我们在感知骨干网络中引入 Convolutional Block Attention Module（CBAM），使模型能够自适应地聚焦于关键结构边缘和可通行空间。其次，我们提出一种新的 Dual Mapping 机制，由物理边界激活和位于深度像素空间中的确定性 Geometric Safety Shield 组成，以在不进行全局地图融合的情况下约束运动学可行性并保证无碰撞飞行。大量高保真仿真实验表明，KIO-planner 能够在最高 3.0 m/s 的速度下实现高机动导航。与最先进基线相比，KIO-planner 具有更低的推理时延（约 24 ms），并生成明显更平滑的轨迹，使控制代价降低 28.4%。最值得注意的是，我们的 Dual Mapping 将最坏情况下的安全裕度（即到障碍物的最小距离）从 0.48 m 显著提升到 0.76 m，从而在高度受限环境中实现更快、更平滑且更安全的导航。

</details>

---

### [[20_Research/Papers/机器人/Multi-Session_Ground_Texture_SLAM_in_Low-Dynamic_Environments|Multi-Session Ground Texture SLAM in Low-Dynamic Environments]]

![[assets/2605.19701_figure.jpg|800]]

- **arXiv**: [2605.19701](https://arxiv.org/abs/2605.19701)
- **PDF**: https://arxiv.org/pdf/2605.19701
- **详细分析**: [[20_Research/Papers/机器人/Multi-Session_Ground_Texture_SLAM_in_Low-Dynamic_Environments|Multi-Session Ground Texture SLAM in Low-Dynamic Environments]]
- **作者**: Kyle M. Hart, Brendan Englot
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

这篇论文关注的是低动态环境中的多会话 Ground Texture SLAM，即机器人仅依赖地面纹理进行定位与建图，并且需要跨多个时段长期运行。与传统依赖墙面、建筑等外部特征的视觉 SLAM 不同，这类系统常用于仓库、空旷道路等外部特征稀缺的场景，因此更依赖地面纹理本身。现实中地面会因磨损、修补、天气或季节变化而逐步改变，导致跨会话重定位和回环检测更容易误判，这正是该工作试图解决的核心瓶颈。

#### 方法概述和架构

论文在 Hart 等人此前的地面纹理视觉 SLAM 系统上做扩展，围绕跨会话回环检测设计了三种方法。第一种方法使用 Kullback-Leibler Divergence（KLD）比较当前观测与第一会话基线图像的颜色直方图差异，并将 KLD 作为相似度偏置来放大或缩小回环因子的协方差，从而调节回环置信度。第二种方法通过已估计位姿和相机视场预测两帧之间的视觉重叠，先筛掉明显不可能形成回环的候选对。第三种方法利用成对图像联合强度直方图的对称性作为相似度指标，同样用于修正回环可信度。整个流程以下视单目彩色相机图像为输入，先做 ORB 特征提取与地面投影，再进行里程计估计和回环候选筛选，最后把估计变换及其协方差写入因子图完成优化。

#### 实验结果分析

实验在多会话、低动态变化的地面纹理场景中进行，作者还专门构建了一个包含跨会话地面变化和高精度 motion capture 位姿真值的数据集用于评测。论文比较了三种方法对轨迹估计精度的影响，并进一步分析了 KLD 方法的作用机制；从摘要和正文节选可见，KLD 方案效果最好。实验还包含对计算时间与回环置信度调节效果的分析，但可见文本未给出具体数值。总体上，结果表明利用地面外观变化来抑制错误回环，是提升长期地面纹理 SLAM 稳定性的有效方向。

<details>
<summary>完整摘要</summary>

SLAM 社区已经提出了越来越多适用于多会话运行的系统，这些系统面向低动态变化的作业环境，例如表面磨损、天气现象或季节变化等会影响建图的场景。这类系统使机器人能够在这些环境中实现长期运行。与此同时，针对“唯一可用的建图特征只有地面纹理”的场景，研究兴趣也在增长。不过，这类地面纹理系统尚未针对多会话、低动态变化环境进行专门设计。本工作考察了三种不同技术在这种多会话低动态地面纹理环境中对轨迹估计精度的影响。在这三种方法中，使用 Kullback-Leibler Divergence 作为相似度评分，并作为影响回环闭合置信度的偏置时，效果最好。我们对这三种方法进行了分析，并进一步深入研究了 Kullback-Leibler Divergence 的影响。此外，我们还为机器人社区引入了一个数据集，其中包含跨会话图像，地面在不同会话之间发生变化，同时还提供了用于评测的高精度位姿信息。

</details>

---

### [[20_Research/Papers/具身智能/D-CLING_Prior-Preserving_Depth-Conditioned_Fine-Tuning_for_Navigation_Foundation_Models|D-CLING: Prior-Preserving Depth-Conditioned Fine-Tuning for Navigation Foundation Models]]

![[assets/2605.19690_figure.png|800]]

- **arXiv**: [2605.19690](https://arxiv.org/abs/2605.19690)
- **PDF**: https://arxiv.org/pdf/2605.19690
- **详细分析**: [[20_Research/Papers/具身智能/D-CLING_Prior-Preserving_Depth-Conditioned_Fine-Tuning_for_Navigation_Foundation_Models|D-CLING: Prior-Preserving Depth-Conditioned Fine-Tuning for Navigation Foundation Models]]
- **作者**: Shintaro Nakaoka, Takayuki Kanai, Kazuhito Tanaka
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

导航基础模型（Navigation Foundation Models, NFM）依赖大规模跨具身数据预训练，已经能在多种场景中实现较强的泛化，但一旦进入新环境或新相机配置，仍容易出现避障不佳、到达目标不准等问题。直接用少量数据做域内微调时，还会破坏预训练阶段学到的先验知识，导致轨迹多样性下降和灾难性遗忘。本文关注的是：如何在适配新场景几何信息的同时，尽量保留大模型原有的导航能力，因此具有较强的现实机器人落地价值。

#### 方法概述和架构

论文提出 D-CLING，一种面向 NFM 的“先验保留式”深度条件微调方法，思路受到 ControlNet 启发。其核心做法是在冻结的预训练 RGB 主干旁边，复制出一个可训练分支，并通过零初始化的残差路径注入深度信息，让模型在中间层逐步学习几何线索。输入上，模型同时接收 RGB 历史帧、目标图像以及对应的深度图；输出则是短时域的动作分布/航点序列，用于导航控制。训练时保留原始 NoMaD 的 RGB 分支参数不变，只更新深度分支及其残差注入路径；推理时两条分支的特征按层融合，从而在不完全重写策略的前提下实现对新环境几何的适配。

#### 实验结果分析

实验基于 NoMaD 这一导航基础模型，在真实机器人导航场景中与零样本 NoMaD、RGB 微调模型以及常见的 RGB-D 早融合微调方案进行比较。结果表明，D-CLING 在长时程导航中能更稳健地完成目标到达，并显著减少碰撞与人工干预。作者还做了离线评估与消融分析，显示该方法不仅能适配微调数据分布，还能在微调域之外保持甚至进一步提升动作预测能力；具体数值在节选文本中未给出。

<details>
<summary>完整摘要</summary>

导航基础模型（NFM）基于大规模跨具身数据训练，已经在多种场景中展现出很强的泛化能力。对 NFM 进行域内微调可以高效校准其视觉-运动策略，并有望在新场景中进一步提升性能。然而，微调后的模型仍然会出现避障能力较差、无法正确到达给定目标等问题。此外，使用少量数据更新模型时，往往会侵蚀预训练先验，从而削弱预训练带来的泛化能力。结果是，微调反而会降低模型在鲁棒且精确导航方面的能力。本文提出一种新的微调方法，旨在在新环境或新相机配置等场景下，既充分利用大规模预训练，又能高效学习新设定。具体而言，受 ControlNet 启发，我们通过零初始化的残差路径，将一个可训练的、由预训练骨干复制得到的分支接入 NFM，从而学习几何线索。这样的设计使模型能够高效获取域内几何信息，同时保留预训练知识中的多种行为能力。尽管方法简单，我们在真实世界导航上的综合评估表明，该方法能以极少的碰撞和最少的人为干预，实现稳健的长时程导航。此外，离线分析表明，所提出的方法不仅能保持微调数据集上的动作预测能力，还能进一步提升其在该数据集之外的表现，为面向通用导航的持续学习提供了关键启示。项目主页：https://toyotafrc.github.io/DCLING-Proj/

</details>

---

### [[20_Research/Papers/具身智能/RoVLA_Multi-Consistency_Constraints_for_Robust_Vision-Language-Action_Models|RoVLA: Multi-Consistency Constraints for Robust Vision-Language-Action Models]]

![[assets/2605.19678_figure.png|800]]

- **arXiv**: [2605.19678](https://arxiv.org/abs/2605.19678)
- **PDF**: https://arxiv.org/pdf/2605.19678
- **详细分析**: [[20_Research/Papers/具身智能/RoVLA_Multi-Consistency_Constraints_for_Robust_Vision-Language-Action_Models|RoVLA: Multi-Consistency Constraints for Robust Vision-Language-Action Models]]
- **作者**: Jingzhou Luo, Yifan Wen, Yongjie Bai, Xinshuai Song, Yang Liu, Liang Lin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 2.1，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

在具身智能和机器人操作中，Vision-Language-Action（VLA）模型需要同时理解视觉观测、自然语言指令并生成连续动作，适用于抓取、放置、操作等复杂任务。然而，现有方法在面对视角变化、背景/光照扰动、同义改写指令以及多种扰动叠加时往往表现脆弱，说明模型仍然依赖训练分布中的浅层相关性，而没有真正学到任务语义、环境状态与动作生成之间稳定的对应关系。作者因此关注一个核心问题：如何在端到端 VLA 策略内部显式加入“不变性”约束，以提升机器人在开放环境中的鲁棒性与泛化能力。

#### 方法概述和架构

论文提出 RoVLA，一个带有多重一致性约束的鲁棒 VLA 框架。其整体采用双系统架构：上层由预训练 VLM 作为语义提取器，编码自然语言指令与多视角图像；下层由基于 DiT 的连续动作生成器执行条件 flow matching，输出未来一段动作 chunk。RoVLA 在训练中引入三类互补约束：Instructional Consistency（IC）要求语义等价的指令改写对应一致的策略 grounding；Evolutionary Consistency（EC）约束动作生成过程中不同演化阶段的动作意图保持连贯；Observational Consistency（OC）则在视觉和本体状态施加目标扰动前后，要求模型预测保持一致，从而增强对观测变化的鲁棒性。推理阶段不额外引入复杂后处理，仍沿用标准双系统骨架，并通过若干步去噪生成动作。

#### 实验结果分析

作者在 LIBERO-Plus、RoboTwin 2.0 以及真实机器人操作任务上进行了实验，并与强基线方法对比；结果表明 RoVLA 在总体性能上持续优于现有方法，同时在任务变化与观测扰动下展现出更强鲁棒性。正文节选中还提到进行了消融实验和定性分析，用于验证 IC、EC、OC 三种一致性约束的贡献，但可见文本未给出具体数值。整体结论是，多一致性学习能够有效缓解 VLA 模型对表面相关性的依赖，提升开放环境中的泛化与稳定控制能力。

<details>
<summary>完整摘要</summary>

视觉-语言-动作（VLA）模型在具身操作中已经展现出很强的性能，但在视觉观测变化、指令的同义改写以及复合扰动下仍然十分脆弱。这一局限表明，现有方法仍然高度依赖训练分布中的浅层相关性，而不是学习任务语义、环境状态与动作生成之间稳定的耦合关系。尽管近期一些工作通过更大规模训练、后训练适配或增强预测建模来提升鲁棒性，但它们很少在端到端策略内部显式施加面向不变性的“一致性”约束。为了解决这一问题，我们提出 RoVLA，一个带有多重一致性约束的鲁棒视觉-语言-动作框架。RoVLA 在三种互补变换下强制保持一致性：指令语义、轨迹演化和观测扰动。具体而言，Instructional Consistency（IC）通过对语义等价的指令改写保持稳定的任务 grounding；Evolutionary Consistency（EC）在动作生成过程中维持连贯的动作意图；Observational Consistency（OC）则通过在目标扰动前后约束一致预测，提升模型对视觉和本体感觉扰动的鲁棒性。通过在训练过程中显式建模这些不变性，RoVLA 减少了对表面相关性的依赖，并提升了鲁棒性和泛化能力。在 LIBERO-Plus、RoboTwin 2.0 以及真实世界操作任务上的实验表明，RoVLA 持续优于强基线方法，并在各种任务和观测变化下展现出更优的鲁棒性。这些结果证明了多一致性学习对于鲁棒具身控制的有效性。代码将在 https://github.com/HCPLab-SYSU/RoVLA 发布。

</details>

---

### [[20_Research/Papers/具身智能/FlyMirage_A_Fully_Automated_Generation_Pipeline_for_Diverse_and_Scalable_UAV_Flight_Data_via_Generative_World_Model|FlyMirage: A Fully Automated Generation Pipeline for Diverse and Scalable UAV Flight Data via Generative World Model]]

![[assets/2605.19600_figure.png|800]]

- **arXiv**: [2605.19600](https://arxiv.org/abs/2605.19600)
- **PDF**: https://arxiv.org/pdf/2605.19600
- **详细分析**: [[20_Research/Papers/具身智能/FlyMirage_A_Fully_Automated_Generation_Pipeline_for_Diverse_and_Scalable_UAV_Flight_Data_via_Generative_World_Model|FlyMirage: A Fully Automated Generation Pipeline for Diverse and Scalable UAV Flight Data via Generative World Model]]
- **作者**: Jinhan Li, Xijie Huang, Zhaoqi Wang, Yijin Wang, Weiqi Ge, Qiyi He, Mo Zhu, Fei Gao, Yuze Wu, Xin Zhou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 大模型
- **相关性评分**: 2.6（加权：具身智能 0.6，大模型 0.1，世界模型 0.8，机器人 1.1）
- **关联关键词**: LLM, Multimodal, EmbodiedAI

#### 研究背景与动机

在航空视觉-语言导航（VLN）中，训练数据长期受限于“规模、丰富性、真实感”难以同时兼得：真实飞行数据采集昂贵且难扩展，仿真数据又常因场景简化而存在明显视觉鸿沟。对于无人机这类高自由度平台，轨迹生成还必须满足动力学可行性，否则即便数据量大，也难以直接用于真实部署。FlyMirage 正是针对“自动生成高质量、可扩展、具真实感的无人机飞行数据”这一痛点展开，值得关注之处在于它把大模型、生成式世界模型和自动化规划串成了一条端到端的数据生产线。

#### 方法概述和架构

FlyMirage 是一个全自动的航空 VLN 数据生成流水线，整体分为三个阶段：世界生成、场景标注和导航采集。首先，系统用 LLM 作为环境设计器，根据预设的场景层级体系生成结构化的场景描述，再结合文本生成图像，输入生成式世界模型 Marble 1.1 Plus，合成为高保真的 3D Gaussian Splatting（3DGS）场景。随后，系统在仅有 3DGS 表征、缺少训练图像和语义标注的情况下，使用 Boxer 做开放词表目标检测与 3D 边界框估计，并通过迭代式相机绕场景中心探索来补充远处目标的观测，从而提升标注质量。接着，基于这些场景标注自动生成导航目标，再引入一个考虑无人机动力学约束的轨迹规划器，产生可真实飞行的 UAV 轨迹。整个流程可以单命令批量运行，把场景设计、渲染、标注与轨迹生成串联为可持续扩展的自动化生产管线。

#### 实验结果分析

作者在该工具链上自动生成了 500 个不同场景，并产出 5 万条导航轨迹，覆盖从室内到室外的多种环境。论文强调，相比现有 VLN 数据集，FlyMirage 在可扩展性、观测保真度以及轨迹物理可执行性方面更有优势；同时，其数据生成成本也显著低于人工建模或人工飞行采集方案。基于当前节选，可见文本未给出具体性能数值、下游任务指标或详细消融结果，但已明确其目标是为下一代具身导航模型提供大规模开放数据。

<details>
<summary>完整摘要</summary>

在视觉-语言导航（VLN）领域，航空数据集在规模、多样性和真实感的综合能力上仍然有限，往往要么依赖昂贵的真实场景，要么受限于视觉表现较弱的仿真环境。为了解决这些挑战，我们提出 FlyMirage：一个面向航空 VLN 的高可扩展、全自动数据生成流水线。我们的方法将大语言模型（LLM）用作环境设计器，以提升场景多样性，并结合生成式世界模型，将这些设计实例化为高保真的 3D Gaussian Splatting（3DGS）场景。为了大幅减少人工劳动并保证飞行数据的可行性，FlyMirage 自动化完成场景探索与语义信息获取，并进一步集成了一个动力学可行的规划器，用于生成无人机（UAV）轨迹。利用这套工具链，我们生成了一个大规模、多样化且具备照片级真实感的航空 VLN 数据集，其中包含动力学可行的飞行轨迹，旨在支持下一代具身导航模型的发展。

</details>

---

### [[20_Research/Papers/具身智能/PAPO-VLA_Planning-Aware_Policy_Optimization_for_Vision-Language-Action_Models|PAPO-VLA: Planning-Aware Policy Optimization for Vision-Language-Action Models]]

![[assets/2605.19580_figure.png|800]]

- **arXiv**: [2605.19580](https://arxiv.org/abs/2605.19580)
- **PDF**: https://arxiv.org/pdf/2605.19580
- **详细分析**: [[20_Research/Papers/具身智能/PAPO-VLA_Planning-Aware_Policy_Optimization_for_Vision-Language-Action_Models|PAPO-VLA: Planning-Aware Policy Optimization for Vision-Language-Action Models]]
- **作者**: Peizheng Guo, Jingyao Wang, Changwen Zheng, Wenwen Qiang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 4.0（加权：具身智能 2.7，强化学习 0.8，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

视觉-语言-动作模型（VLA）正在成为语言驱动机器人操作的重要路线，但在真实具身任务中，要让策略“稳定可靠”仍然很难。根本原因在于，机械臂操作是一个闭环过程：每一步动作都会改变环境状态，并影响后续观测与决策，因此局部看起来合理的动作，并不一定能导向最终成功。作者指出，VLA 在执行时实际上同时扮演“规划者”和“执行者”两种角色，而现有优化方法往往没有显式区分哪些动作更像任务转折点、哪些只是连续执行细节，这使得提升策略可靠性存在明显空白。

#### 方法概述和架构

本文提出 PAPO-VLA（Planning-Aware Policy Optimization for VLA models）。方法首先从密集轨迹中识别“规划动作”：一方面利用动作变化来发现执行意图发生切换的位置，另一方面结合轨迹结果筛掉那些虽然突变但并不真正有助于成功的动作。随后，方法用因果充分性与因果必要性来估计每个规划动作对任务成功的重要性，即考察“保留这个动作是否有助于后续执行走向成功”以及“扰动这个动作是否会让结果变差”。最后，作者将得到的重要性权重注入 GRPO 的 advantage 估计中，使更关键的规划动作在优化时获得更强的梯度强调，同时仍保留轨迹级反馈对整条轨迹的约束。整体流程是：采样多条候选轨迹并计算轨迹级奖励，再定位规划动作、评估其因果重要性，最后在 GRPO 式策略优化中进行规划感知的加权更新。

#### 实验结果分析

根据摘要和正文节选，作者在多个基准上验证了 PAPO-VLA 的有效性，并与现有 VLA 后训练/优化方法进行了比较。实验设置覆盖多个机器人操作基准，且还包含消融实验与案例可视化，用于分析规划动作识别、因果重要性估计以及规划感知优势估计各模块的贡献。可见文本未给出具体数值，但整体结论是：显式关注规划动作后，VLA 策略在任务成功相关的优化上更有效，且方法具有稳定的经验收益与泛化表现。

<details>
<summary>完整摘要</summary>

视觉-语言-动作（VLA）模型在语言指导的机器人任务中展现出很有前景的能力。然而，要让 VLA 策略变得可靠仍然具有挑战性，因为操作任务是通过闭环交互完成的，其中每个动作都会影响后续执行。为分析这一问题，我们重新审视了 VLA 策略在执行过程中的作用，并认为 VLA 策略同时充当两种角色：一种是规划者，它做出面向任务的决策并改变执行方向；另一种是执行者，它通过密集的连续动作来实现这些决策。这一视角表明，要提升 VLA 的可靠性，需要特别关注规划动作。现有优化方法可以模仿动作或改进完整轨迹，但通常不会显式识别规划动作，也不会衡量它们对任务成功的重要性。为了解决这一问题，我们提出了面向 VLA 模型的规划感知策略优化方法 PAPO-VLA。PAPO-VLA 首先通过联合考虑动作变化和轨迹结果来识别规划动作，然后通过因果充分性和因果必要性来估计其重要性，最后将这种重要性融入 GRPO 的 advantage 估计中。这样，越重要的规划动作会获得越强的优化强调，而整条轨迹仍然会通过轨迹级反馈得到优化。多个基准上的实验表明，PAPO-VLA 是有效的。

</details>

---

### [[20_Research/Papers/具身智能/Self-assembling_Modular_Aerial_Robot_for_Versatile_Aerial_Tasks|Self-assembling Modular Aerial Robot for Versatile Aerial Tasks]]

![[assets/2605.19431_figure.png|800]]

- **arXiv**: [2605.19431](https://arxiv.org/abs/2605.19431)
- **PDF**: https://arxiv.org/pdf/2605.19431
- **详细分析**: [[20_Research/Papers/具身智能/Self-assembling_Modular_Aerial_Robot_for_Versatile_Aerial_Tasks|Self-assembling Modular Aerial Robot for Versatile Aerial Tasks]]
- **作者**: Junichiro Sugihara, Masaki Kitagawa, Jinjie Li, Yunong Li, Takuzumi Nishio, Kei Okada, Moju Zhao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

多旋翼无人机擅长三维机动与狭窄空间穿行，尤其是小型机体在避障与穿越复杂环境方面表现出色；但面向高空作业和物理交互的无人机往往需要更大的机体和更高推力，以获得稳定的操控能力。由此带来一个长期矛盾：灵活机动与强力操控往往难以兼得。本文关注的是如何让空中机器人既能像小型无人机一样灵活飞行，又能在需要时自组织成更强大的空中操作平台，因此具有很强的机器人与具身智能价值。

#### 方法概述和架构

作者提出了一种名为 LEGION 的可重构模块化空中机器人系统，每个模块两端都带有带关节的对接接口，支持空中端到端自组装。系统仿照蚂蚁的自组织协同行为，单体状态下保持灵活机动，组装后则形成可 артиculated 的空中操纵器，以执行推、拉、旋转、抓取和搬运等任务。为实现可靠空中对接，论文设计了磁-机械混合式可拆卸对接机构，并配合鲁棒的空中对接规划方法，在对接过程中使用状态机管理“对准—接近—装配”三个阶段。针对组装后飞行时模块间受力受矩的耦合问题，作者进一步提出了接触力矩的估计与控制方法，使各模块协同维持零间隙锁定并完成形态切换。整个系统依赖机载传感器完成定位与外力矩估计，推理/控制均为去中心化执行，模块之间通过共享接触 wrench 信息实现协同控制。

#### 实验结果分析

实验表明，LEGION 可以在空中实现多个模块的自主对接，并在组装后进行重构与再次分离；正文节选中给出了三模块空中组装、变形和分离的完整演示。作者还展示了在仅使用机载感知的情况下进行 20 次连续对接实验，全部成功，且在 GNSS-denied 森林环境中也能完成室外自重构，说明方法具备较强的鲁棒性与泛化能力。文中同时报告了接触力矩在对接后迅速收敛至目标值、组装态下飞行稳定性可维持，以及可扩展到更多模块的仿真结果；但对于部分对比与消融设置，节选文本未给出完整基线与全部数值。

<details>
<summary>完整摘要</summary>

多旋翼空中机器人在三维空间机动方面表现优异，近期进展使其能够在拥挤和受限环境中灵活导航，尤其是小型机体更具优势。相比之下，面向高空作业的平台通常需要更大的尺寸，以提供足够的高推力，从而实现稳定的环境物理交互。然而，这些相互冲突的设计需求长期以来造成了灵活导航与稳健空中操作之间的权衡。为此，我们提出了 LEGION units，一种可重构的模块化空中机器人，能够在飞行中自组装以执行协同操作，其灵感来源于蚂蚁形成的自组织群体。每个单元都保持灵巧的机动性，同时其两端带有关节的对接接口使得多个单元可以首尾相连，自组装成空中操纵器。我们证明，多个单元能够在飞行中自主对接；一旦锁定，它们通过控制接触力和力矩，维持零间隙的互锁结构，从而即使在室外也能实现可靠聚合与关节化运动。我们进一步证明，自重构能力使系统能够在灵活的单体飞行与协同的关节式操作之间进行形态切换，同时实现空中操作的核心原语，包括推动、拉动、旋转、抓取与搬运。LEGION 的自组织能力使空中机器人，尤其是在群体场景中，能够从被动观察者转变为环境中的主动参与者，从而拓展空中物理交互的应用范围。

</details>

---

### [[20_Research/Papers/机器人/Neuromorphic_Control_of_a_Flapping-Wing_Robot_on_Resource-Constrained_Hardware|Neuromorphic Control of a Flapping-Wing Robot on Resource-Constrained Hardware]]

![[assets/2605.19430_figure.png|800]]

- **arXiv**: [2605.19430](https://arxiv.org/abs/2605.19430)
- **PDF**: https://arxiv.org/pdf/2605.19430
- **详细分析**: [[20_Research/Papers/机器人/Neuromorphic_Control_of_a_Flapping-Wing_Robot_on_Resource-Constrained_Hardware|Neuromorphic Control of a Flapping-Wing Robot on Resource-Constrained Hardware]]
- **作者**: Rim El Filali, Chenrui Feng, Chao Gao, Weibin Gu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

扑翼微型飞行器（FWMAV）兼具高机动性和较好的气动效率，适合在狭窄、复杂环境中执行任务，但其飞行控制极其困难，主要受限于强非线性、强耦合且时变的动力学，以及严格的尺寸、重量和功耗（SWaP）约束。本文聚焦一只不到30克的蝴蝶仿生扑翼机器人，目标是在低成本、资源受限的ESP32微控制器上实现完全机载、闭环的自主飞行控制。现有学习式控制方法多依赖常规ANN，推理开销较高，不利于在这类极小型平台上实现实时、低功耗部署，因此这项工作值得关注。

#### 方法概述和架构

论文提出一种分层的神经形态控制方法，将机载控制拆分为“状态估计”和“控制决策”两个轻量级SNN模块。第一个SNN直接从IMU等原始传感反馈中估计姿态相关状态，第二个SNN则结合这些估计值、陀螺仪读数以及外部给定的目标姿态，输出对控制量的修正。该控制量不是直接作用于推力或力矩，而是调制一个Central Pattern Generator (CPG) 的偏置项，通过改变左右翼的平均拍振位置来产生俯仰与航向控制。整个系统采用模仿学习训练，并以CUBA-LIF脉冲神经元构建循环SNN；同时，作者还开发了Espikify工具，将PyTorch定义的SNN转换为可在ESP32上运行的C代码，以实现亚毫秒级推理和较小内存占用。

#### 实验结果分析

实验在一台基于ESP32-S3的不到30克蝴蝶仿生扑翼机器人上进行，验证了完全机载、闭环、无系缆飞行的可行性，能够稳定跟踪俯仰角和航向角。与同硬件上的ANN基线相比，SNN控制器的推理延迟降低了36%（从1059 μs降至680 μs），功耗降低了18%（从0.033 W降至0.027 W）。作者还强调，这被认为是首次在FWMAV上实现完全机载的神经形态自主飞行控制；可见文本未给出更详细的消融或跨场景泛化数值。

<details>
<summary>完整摘要</summary>

扑翼微型飞行器（FWMAV）具有出色的机动性和气动效率，但由于其非线性动力学以及严格的尺寸、重量和功耗（SWaP）约束，机载控制面临巨大挑战，这一点在一只重量不到30克的蝴蝶仿生机器人上尤为典型。为此，我们提出一种分层神经形态控制框架，使其能够在一款广泛可得、资源受限的ESP32微控制器上实现完全机载的闭环飞行，其单价约为5美元。具体而言，我们在机载端部署了两个轻量级Spiking Neural Networks (SNN)：一个用于从原始传感反馈中进行状态估计，另一个通过调制用于翼部驱动的Central Pattern Generator (CPG) 来完成控制。系统采用模仿学习进行训练，在真实世界的无系绳飞行中实现了稳定的俯仰角和航向角跟踪。实验结果进一步表明，与传统Artificial Neural Network (ANN) 基线相比，基于SNN的控制器在推理时将延迟降低了36%（1059 μs降至680 μs），功耗降低了18%（0.033 W降至0.027 W），证明了无需专用硬件也可以实现基于脉冲计算的方案。就我们所知，这项工作首次展示了FWMAV完全机载的神经形态自主飞行控制，凸显了SNN在严格SWaP约束下实现高能效自主性的潜力。

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Waypoints_Dual-Heatmap_Grounding_for_Cross-Embodiment_Semantic_Navigation|Beyond Waypoints: Dual-Heatmap Grounding for Cross-Embodiment Semantic Navigation]]

![[assets/2605.19420_figure.jpg|800]]

- **arXiv**: [2605.19420](https://arxiv.org/abs/2605.19420)
- **PDF**: https://arxiv.org/pdf/2605.19420
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Waypoints_Dual-Heatmap_Grounding_for_Cross-Embodiment_Semantic_Navigation|Beyond Waypoints: Dual-Heatmap Grounding for Cross-Embodiment Semantic Navigation]]
- **作者**: Kaijie Yun, Yue Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

这篇论文关注的是具身机器人在视野内根据自然语言或图像提示进行语义导航的任务，例如“去沙发旁边”“看向电视”或“根据人物图片靠近指定的人”。现有方法往往直接回归单个确定性航点，但这种做法会把本来存在的空间不确定性压缩成一个点，容易把目标落到不可通行的物体中心，从而在真实执行中失败。作者认为，语义理解与物理可达性之间存在明显鸿沟，因此值得研究一种既能表达语义意图、又能兼顾可达性的导航表示。

#### 方法概述和架构

论文提出 Beyond Waypoints 的双热力图语义导航框架，用来替代单点航点回归。模型以当前第一人称 RGB 观测和交错的文本/图像多模态指令为输入，输出两张同分辨率热力图：导航热力图 H_nav 和朝向热力图 H_fac。H_nav 用于表示可通行区域中的“可停靠位置”概率，避免把目标落在物体中心；H_fac 则用于表达最终朝向约束，指导机器人面向目标对象或用户。方法上采用 VLM 主干、视觉语言交叉注意力模块以及轻量级密集解码器，三者串联后并行预测两张热力图。推理时，热力图可被视为可微的语义势场，再与下游局部规划器和碰撞代价结合，选择既符合语义又满足运动学约束的执行点。为支撑训练，作者还构建了一个完全自动化、由基础模型辅助的合成数据生成流程，并建立了仿真评测基准。

#### 实验结果分析

实验在仿真环境中进行，并在不同机器人形态上验证，包括 Jetbot、H1 和 Aliengo。对比的是可比的 8B 基线模型，论文报告该方法取得了当前最优表现；但可见文本未给出具体数值。作者还做了特征融合研究和跨机器人形态验证，结果显示显式预测热力图能显著提升 AR（Affordance Rate），说明把目标放在可执行的自由空间中比回归单点更稳健。

<details>
<summary>完整摘要</summary>

将开放式语义指令落地为物理上可执行的局部目标，是人机交互中的一个基础难题。现有导航框架通常回归确定性的航点，但这种刚性的形式会抹平空间不确定性，而且经常把目标指向不可通行的物体中心，导致严重的执行失败。本文聚焦于更贴近实际的视野内语义导航场景，即机器人接收简洁、交错的多模态提示（文本与图像）。为弥合抽象语义意图与物理可达性之间的差距，我们提出一个统一的视觉语言框架，放弃单点回归，转而采用双热力图表示。我们的框架预测一个导航可供性热力图，用于刻画连续的可达区域，并结合一个朝向热力图来表达方向约束。这些密集输出天然可作为可微的语义势场，与下游局部规划器无缝集成。为支持这一范式，我们构建了一个完全自动化、由基础模型辅助的合成数据流水线，并建立了一个完整的仿真基准。大量实验表明，相比可比的 8B 基线，我们的框架取得了最先进的性能。更重要的是，特征融合研究以及在多种机器人形态（Jetbot、H1、Aliengo）上的仿真实验表明，显式热力图预测可以显著提升 Affordance Rate（AR）。通过将目标可靠地放置在可执行的自由空间中，我们的方法有效缓解了点回归的脆弱性，为安全的跨具身语义导航提供了一条可迁移的路径。

</details>

---

### [[20_Research/Papers/具身智能/RoboJailBench_Benchmarking_Adversarial_Attacks_and_Defenses_in_Embodied_Robotic_Agents|RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents]]

![[assets/2605.19328_figure.png|800]]

- **arXiv**: [2605.19328](https://arxiv.org/abs/2605.19328)
- **PDF**: https://arxiv.org/pdf/2605.19328
- **详细分析**: [[20_Research/Papers/具身智能/RoboJailBench_Benchmarking_Adversarial_Attacks_and_Defenses_in_Embodied_Robotic_Agents|RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents]]
- **作者**: Doguhuan Yeke, Yanming Zhou, Leo Y. Lin, Hongyu Cai, Antonio Bianchi, Z. Berkay Celik
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.3，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

具身智能中的 Vision-Language Models 正被用于机器人、自动驾驶等物理平台，能够根据视觉场景理解自然语言指令并执行动作，但这也让模型暴露在真实世界的安全攻击面之下。此前关于具身系统的越狱攻击与防御研究，多依赖临时构造的数据集和有限指标，往往只关注攻击是否成功，却忽略了防御后系统是否仍能正确执行正常任务这一“安全—可用性”权衡。由于缺少统一的威胁模型、后果分类和评测流程，现有结果难以横向比较，也不利于后续攻击与防御研究的可复现推进，因此 RoboJailBench 这一基准工作具有较强的现实意义。

#### 方法概述和架构

论文提出 RoboJailBench 作为具身机器人越狱攻击与防御的标准化评测框架，整体由三部分组成。第一部分是安全分类体系：作者结合 ISO 安全标准、机器人法规/规范以及真实事故报告，构建出 18 类适用于具身智能的安全违规后果标签。第二部分是 intent contrast 数据管线：针对每张场景图像，同时构造一对语义对立但都与物理环境相关的目标，即 benign goal 和 adversarial goal，用来同时衡量系统的安全性与任务可执行性。第三部分是统一评测流程：框架支持接入新的攻击方法和防御方法，并用标准化指标计算攻击表现与防御后的 utility。基于该框架，作者新建了 taxonomy-balanced 的 RJB-Instructions 数据集，并对 5 个已有数据集进行了扩增，同时整合 4 种攻击与 2 种防御方法，在主流具身 VLM 上进行评测。

#### 实验结果分析

实验在多种具身数据集与主流 embodied VLM 上展开，覆盖机器人操作、接触丰富操作、长程推理、机器人问答以及自动驾驶等场景；其中既评估了原始基线表现，也评估了攻击与防御在统一指标下的效果。结果表明，现有攻击和防御在不同数据集上的表现差异较大，且只看攻击成功率会掩盖防御对正常指令执行能力的影响。作者进一步展示了基于统一 taxonomy 和 intent contrast 设计的评测方式能够更全面地刻画安全风险与任务能力的权衡。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

近期 Vision-Language Models（VLMs）的进展促进了一类新的具身 AI 系统的发展，这类系统将这些模型集成到物理平台中，例如机器人和自动驾驶车辆，以便在多样环境中理解视觉场景并执行自然语言指令。此前已有研究提出了面向具身 AI 的越狱攻击与防御方法，但它们的评测依赖临时构造的数据集、有限的指标，并且过度强调攻击成功，而忽视了安全性与遵循正常指令能力之间的权衡。现有基准和评测框架要么面向传统的聊天式模型，要么聚焦于具身 AI 的非对抗安全评估；二者都无法捕捉具身 AI 系统中越狱攻击所需的对抗风险、输入、后果以及评测标准。为此，我们提出 RoboJailBench，它由三个核心部分组成。首先，我们基于 ISO 标准、监管规则以及已记录事件建立了一个安全分类体系，由此得到具身 AI 中 18 类安全违规后果。其次，我们引入一个 intent contrast 数据集管线，通过为现有数据集增加成对的对抗目标与正常目标来同时衡量安全性与可用性。最后，我们提供一个持续演进的仓库，其中包含标准化指标以及用于评估和接入新的攻击与防御方法的统一流程。基于这一基准，我们构建了一个新的、在 taxonomy 上保持平衡的数据集，并对 5 个现有数据集进行了扩增。我们整合了 4 种攻击和 2 种防御方法，并在领先的具身 VLM 上评估了它们的表现。该基准提供了首个用于具身 AI 越狱攻击的标准化评测框架，并支持未来研究。我们已发布代码、数据集和相关产物，并维护一个排行榜：https://purseclab.github.io/benchmark-for-robotics-security。

</details>

---

### [[20_Research/Papers/机器人/PRISM-SLAM_Probabilistic_Ray-Grounded_Inference_for_Scale-aware_Metric_SLAM|PRISM-SLAM: Probabilistic Ray-Grounded Inference for Scale-aware Metric SLAM]]

![[assets/2605.19257_figure.png|800]]

- **arXiv**: [2605.19257](https://arxiv.org/abs/2605.19257)
- **PDF**: https://arxiv.org/pdf/2605.19257
- **详细分析**: [[20_Research/Papers/机器人/PRISM-SLAM_Probabilistic_Ray-Grounded_Inference_for_Scale-aware_Metric_SLAM|PRISM-SLAM: Probabilistic Ray-Grounded Inference for Scale-aware Metric SLAM]]
- **作者**: Eunsoo Im
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

单目SLAM在机器人与具身智能中很重要，因为它只依赖RGB相机即可完成定位和建图，但长期面临绝对尺度不可观测、轨迹尺度漂移以及动态场景下跟踪不稳的问题。近年来视觉基础模型提供了较强的零样本深度先验，但现有方法往往把这些深度结果当作确定性真值直接融合，忽略了预测不确定性和帧间尺度不一致，容易引发优化不稳定。作者关注的核心问题是：如何在不依赖后验尺度校正的情况下，把基础模型先验真正转化为可部署的、实时的米制SLAM输出。

#### 方法概述和架构

PRISM-SLAM 是一个面向单目RGB输入的实时贝叶斯SLAM框架，将视觉基础模型先验嵌入结构化因子图中进行概率融合。系统采用异步多进程架构：前端负责高频几何跟踪，后端并行进行 DA3 深度/不确定性提取、尺度恢复、图优化和回环闭环。方法的关键是引入 Plücker Ray-Distance Factor，用射线-距离约束把单目观测锚定到全局一致的度量坐标系，从优化层面让尺度变得可识别。为抑制动态物体干扰，作者从深度时序一致性中构造经验不确定性代理，并设计 Dynamic Scene Uncertainty Gating（DSUG）对不可靠区域进行软降权，而不是使用硬语义分割掩码。为了弥补前后端异步带来的时间差，系统还使用对数域尺度自适应滤波器持续输出正尺度反馈，并利用 ViT 特征进行回环与全局度量 BA，从而输出稳定的度量轨迹和地图。

#### 实验结果分析

论文在 TUM RGB-D 和 7-Scenes 上进行了评测，并报告了严格 SE(3) 评价下的轨迹误差。结果显示，PRISM-SLAM 的度量 SE(3) ATE 几乎与其经过 oracle 对齐后的 Sim(3) 误差一致，说明系统已经能在运行时直接给出可部署的米制轨迹。正文节选还显示其可在仅 RGB 输入下达到 30 FPS，并且相较于依赖后验尺度校正的同类方法，验证了真实度量尺度恢复的可行性；可见文本未给出具体数值对比和消融结果细节。

<details>
<summary>完整摘要</summary>

单目SLAM长期以来受困于尺度歧义以及动态环境中的跟踪失败。尽管近年来视觉基础模型（VFM）提供了令人瞩目的零样本深度先验，但若直接、天真地将这些确定性预测进行融合，就会忽略预测不确定性以及帧间尺度不一致的问题。为此，我们提出 PRISM-SLAM，这是一个实时框架，它将VFM先验严格整合进结构化贝叶斯因子图中，以实现具备尺度感知、度量一致的定位与建图。具体而言，我们引入 Plücker Ray-Distance Factor，用以将单目观测锚定到绝对空间中的全局一致度量坐标系中；该设计通过使度量尺度在 Fisher 意义下可识别，从数学上解决了尺度漂移问题。为了应对环境动态性，我们从时间深度一致性中推导出经验不确定性代理，并构建了 Dynamic Scene Uncertainty Gating（DSUG）机制。这种软门控方法可以概率性地降低动态干扰项的权重，而无需承担传统语义分割掩码带来的高计算开销。通过采用多进程架构异步处理 VFM 推理与几何跟踪，PRISM-SLAM 仅使用RGB输入即可在30 FPS下提供经过验证的度量输出，从而弥合了基础模型与真实机器人应用之间的鸿沟。在 TUM RGB-D 和 7-Scenes 基准上，PRISM-SLAM 所达到的度量 SE(3) Absolute Trajectory Error（ATE）几乎与其经过 oracle 对齐的 Sim(3) 误差一致。这表明，该系统能够在无需任何事后尺度校正的情况下，提供可直接部署的度量轨迹，并实现稳健的度量SLAM。

</details>

---

### [[20_Research/Papers/机器人/Graph_Neural_Planning_and_Predictive_Control_for_Multi-Robot_Communication-Constrained_Unlabeled_Motion_Planning|Graph Neural Planning and Predictive Control for Multi-Robot Communication-Constrained Unlabeled Motion Planning]]

![[assets/2605.19209_figure.png|800]]

- **arXiv**: [2605.19209](https://arxiv.org/abs/2605.19209)
- **PDF**: https://arxiv.org/pdf/2605.19209
- **详细分析**: [[20_Research/Papers/机器人/Graph_Neural_Planning_and_Predictive_Control_for_Multi-Robot_Communication-Constrained_Unlabeled_Motion_Planning|Graph Neural Planning and Predictive Control for Multi-Robot Communication-Constrained Unlabeled Motion Planning]]
- **作者**: Manohari Goarin, Yang Zhou, Giuseppe Loianno
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

多机器人无标签运动规划要求在机器人与目标未预先绑定的情况下，同时完成目标分配与安全轨迹生成，常见于协同搬运、仓储、搜索救援和巡检等场景。现有基于GNN的分散式方法虽然可扩展，但往往建立在简化动力学和仿真假设上，忽略了真实部署中的非线性动力学、执行器约束以及通信延迟等关键问题。本文聚焦“通信受限”条件下的多机器人无标签规划，强调将学习型高层决策与可验证的安全控制结合起来，因此具有较强的工程落地价值。

#### 方法概述和架构

论文提出一个分层式GATP-NMPC框架，其中高层使用Graph ATtention Planner（GATP）进行协同规划，低层使用分散式Nonlinear Model Predictive Controller（NMPC）执行轨迹跟踪。GATP以每个机器人局部观测和通信图为输入，基于注意力机制聚合邻居信息，输出未来时间窗内的中间子目标，而不是直接输出速度命令，从而降低对动力学建模的依赖。NMPC接收GATP给出的子目标，结合机器人非线性动力学、控制输入限制和安全约束，生成平滑且碰撞安全的控制轨迹。整个系统以较低频率重规划：GATP根据机器人状态变化持续更新子目标，NMPC则在本地进行在线优化与执行。作者还实现了ROS 2上的分散式机载推理流程，使该方法可直接部署到真实四旋翼平台。

#### 实验结果分析

作者在仿真中对10台四旋翼进行了验证，任务包括圆形编队和区域覆盖，并与常见的GCN类方法做了对比，同时分析了不同队伍规模下的覆盖泛化表现；可见文本未给出具体数值。实验还考察了通信延迟对系统性能的影响，结果显示该方法在200 ms以内的延迟下仍具有较强鲁棒性。进一步地，论文在真实世界中使用4台四旋翼进行部署，展示了分散式机载推理的可行性，并报告了推理时间与通信时延；消融结果表明，注意力机制相比传统图卷积更有利于覆盖性能与泛化能力。

<details>
<summary>完整摘要</summary>

多机器人无标签运动规划问题要求在为机器人与目标同时完成分配的同时，生成安全轨迹，是许多协作任务中的核心问题。近年来，Graph Neural Network 方法提供了可扩展的分散式解决方案，但它们依赖简化动力学和仿真环境，忽视了真实部署中的关键挑战，例如动态可行性和通信约束。为了解决这些问题，我们提出一个分层框架，将Graph ATtention Planner（GATP）与分散式Nonlinear Model Predictive Controller（NMPC）结合起来。GATP通过多机器人协作提供中间子目标，NMPC则在非线性动力学和执行器约束下保证安全性。我们在仿真和真实四旋翼实验中评估了该框架。得益于注意力机制和极少的通信需求，我们展示了对更大规模队伍更好的泛化能力、对最高200 ms通信延迟的鲁棒性，以及通过分散式机载推理实现的实际可行性。

</details>

---

### [[20_Research/Papers/具身智能/CLUE_Adaptively_Prioritized_Contextual_Cues_by_Leveraging_a_Unified_Semantic_Map_for_Effective_Zero-Shot_Object-Goal_Navigation|CLUE: Adaptively Prioritized Contextual Cues by Leveraging a Unified Semantic Map for Effective Zero-Shot Object-Goal Navigation]]

![[assets/2605.19206_figure.png|800]]

- **arXiv**: [2605.19206](https://arxiv.org/abs/2605.19206)
- **PDF**: https://arxiv.org/pdf/2605.19206
- **详细分析**: [[20_Research/Papers/具身智能/CLUE_Adaptively_Prioritized_Contextual_Cues_by_Leveraging_a_Unified_Semantic_Map_for_Effective_Zero-Shot_Object-Goal_Navigation|CLUE: Adaptively Prioritized Contextual Cues by Leveraging a Unified Semantic Map for Effective Zero-Shot Object-Goal Navigation]]
- **作者**: Taeyun Kim, Alvin Jinsung Choi, Dasol Hong, Hyun Myung
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

零样本目标导航（ZSON）要求机器人在陌生环境中，仅凭语言目标与视觉观测找到指定物体，是具身智能与服务机器人中的基础难题。此类任务不仅要识别“目标是什么”，还要推断“目标通常在哪里”，因此房间语义和邻近物体等上下文线索都很关键。现有方法往往把房间线索和物体线索一视同仁，没有根据目标类别的不同自适应调整它们的重要性，容易导致探索效率低、定位不准。

#### 方法概述和架构

本文提出CLUE（Adaptively Prioritized Contextual Cues by Leveraging a Unified Semantic Map for Effective Zero-Shot Object-Goal Navigation），核心是构建一个统一的语义价值地图来融合目标线索、房间线索和物体线索。首先，方法用VLM为当前观测与目标类别计算目标物体分数，并将其写入语义地图；随后分别提取上下文房间分数和上下文物体分数，其中房间分数反映目标与特定房间类型的关联，物体分数则反映目标与共现物体之间的空间/语义关系。为了决定更偏重哪类线索，CLUE在离线阶段通过LLM查询目标与房间类型的常识关联，并用该关联分布的归一化熵作为自适应权重：熵低则更强调房间线索，熵高则更强调物体线索。最终，三类分数被融合到统一语义价值地图中，机器人沿着最有希望的前沿区域进行粗到细式探索，并通过多视角验证候选目标位置以提高鲁棒性。整个过程不依赖在线LLM推理，从而降低了执行时延和计算开销。

#### 实验结果分析

论文在HM3D仿真环境上进行了系统评估，并进一步在真实世界的Clearpath Jackal平台上验证了方法可行性。与多种zero-shot ObjectNav基线相比，CLUE在SR和SPL两个指标上都取得了更好的表现，说明其既更容易找到目标，也能以更短路径完成任务。文中还进行了消融实验与资源分析，可见文本未给出具体数值，但结果支持了“自适应融合上下文线索”和“离线LLM常识提取”这两项设计的有效性。

<details>
<summary>完整摘要</summary>

零样本目标导航（ZSON）是机器人领域一项具有挑战性的问题，它要求系统同时理解语言和视觉观测。来自房间和物体的上下文线索至关重要，但它们的相对重要性取决于目标：有些物体与特定房间类型强相关，而另一些则更适合通过附近共现物体来预测。现有方法忽视了这种差异，导致探索过程低效且不准确。为此，我们提出CLUE，一种新的导航框架，它通过利用从离线大语言模型（LLM）中提取的常识知识，自适应地平衡房间线索与物体线索的使用。通过借助LLM估计目标与房间类型之间的关联，智能体会对可预测性更强的物体优先使用房间线索，而对与房间关联较弱的物体优先使用物体线索。我们的框架构建了一个统一的语义价值地图，将这两类上下文信息整合起来，并根据目标的歧义程度进行自适应加权，以指导探索。结合多视角验证和由上下文线索驱动的探索策略，CLUE实现了鲁棒且高效的导航。大量仿真与真实环境实验表明，我们的方法在成功率（SR）和成功路径加权长度（SPL）上都持续优于当前最优基线，证明了其在真实导航任务中的有效性与实用性。

</details>

---

### [[20_Research/Papers/具身智能/CosFly_Plan_in_the_Matrix,_Fly_in_the_World|CosFly: Plan in the Matrix, Fly in the World]]

![[assets/2605.19120_figure.jpg|800]]

- **arXiv**: [2605.19120](https://arxiv.org/abs/2605.19120)
- **PDF**: https://arxiv.org/pdf/2605.19120
- **详细分析**: [[20_Research/Papers/具身智能/CosFly_Plan_in_the_Matrix,_Fly_in_the_World|CosFly: Plan in the Matrix, Fly in the World]]
- **作者**: Hanxuan Chen, Xiangyue Wang, Songsheng Cheng, Ruilong Ren, Jie Zheng, Shuai Yuan, Tianle Zeng, Hanzhong Guo, Binbo Li, Kangli Wang, Ji Pei
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

无人机在复杂户外环境中进行动态目标跟踪时，不仅要持续感知目标，还要同时满足避障、视角保持和导航指令理解等要求，这使得任务天然适合与具身智能、大模型相结合。现有真实世界无人机数据集往往规模有限、采集成本高且存在安全风险，而且多只提供RGB视频和框级标注，缺少深度、语义分割以及自然语言导航指令，难以支撑多模态模型训练。作者因此关注如何通过仿真生成可控、可扩展、带丰富标注的空中跟踪数据，并为无人机轨迹规划与多模态感知提供统一基础。

#### 方法概述和架构

论文提出CosFly，一个面向空中跟踪的箱结构规划与多模态仿真流水线，并配套发布CosFly-Track数据集。整个系统由7个步骤组成：先将3D世界离线导出为3D网格，再进行网格清理与简化，将复杂环境转化为适合规划的结构化障碍表示。随后分别批量生成行人轨迹和无人机轨迹，其中无人机轨迹支持两种规划范式：传统的两阶段TA*+Smooth，以及将多项跟踪约束统一到一个目标中的MuCO一阶段梯度优化。得到轨迹后，系统在CARLA中渲染同步的多模态数据，包括RGB、深度图和语义分割，并附带6-DOF位姿标注与自然语言导航指令。流水线还支持固定FOV的可配置缩放、质量检查，以及通过教师-学生流程生成图像字幕，从而把规划结果、视觉观测和语言描述连接成完整训练样本。

#### 实验结果分析

作者在CARLA上构建并验证了CosFly-Track首批公开版本，包含250条经过验证的轨迹和约10万张渲染图像，且每张图像都带有完整的6-DOF无人机位姿标注。正文节选显示，论文还对TA*+Smooth与MuCO两种轨迹规划范式、渲染质量与数据保真度、固定FOV缩放能力等进行了基线实验和分析；但可见文本未给出具体数值。整体结论是，该流水线能够稳定地产生跨城市、高速公路、乡村、森林和海岸城镇等多场景的多模态空中跟踪数据，为动态目标跟踪、无人机导航和多模态感知提供了可扩展基础。

<details>
<summary>完整摘要</summary>

我们提出CosFly，一种用于空中跟踪的箱结构规划与多模态仿真流水线，并同时发布CosFly-Track，这是一个面向动态目标跟踪的大规模无人机数据集，覆盖城市中心、高速公路、乡村景观、森林和海岸城镇等多种环境。当前在CARLA上的实现中，CosFly提供了一个模块化的7步构建流程：先将复杂三维世界转换为用于规划的结构化障碍表示，再将生成的轨迹投影回多模态传感器数据，包括RGB图像、高精度深度图和语义分割掩码，并配套自然语言导航指令。该流水线的一项关键特性是支持可配置的固定FOV缩放级别（每条轨迹只采样一次FOV并在整条轨迹中保持不变），通过相机内参调整来模拟不同焦距。整个流程覆盖从3D地图导出、网格简化、行人与无人机轨迹规划、多模态渲染与6-DOF位姿标注，到质量检查以及教师-学生式字幕生成的完整链路。我们分析了两种用于空中目标跟踪的轨迹规划范式：一种是传统的两阶段流程，包含前端候选生成和后端精修；另一种是直接基于梯度的形式，将多个跟踪约束统一优化到单一目标中。公开发布的CosFly-Track包含250条经过验证的轨迹以及约10万张渲染图像，并带有完整的6-DOF无人机位姿标注（位置x、y、z以及姿态yaw、pitch、roll）。总体而言，该流水线与数据集为地空协同研究建立了可扩展基础，支持动态目标跟踪、无人机导航以及跨多种环境的多模态感知。

</details>

---

### [[20_Research/Papers/具身智能/Distributionally_Robust_Control_via_Stein_Variational_Inference_for_Contact-Rich_Manipulation|Distributionally Robust Control via Stein Variational Inference for Contact-Rich Manipulation]]

![[assets/2605.19029_figure.png|800]]

- **arXiv**: [2605.19029](https://arxiv.org/abs/2605.19029)
- **PDF**: https://arxiv.org/pdf/2605.19029
- **详细分析**: [[20_Research/Papers/具身智能/Distributionally_Robust_Control_via_Stein_Variational_Inference_for_Contact-Rich_Manipulation|Distributionally Robust Control via Stein Variational Inference for Contact-Rich Manipulation]]
- **作者**: Hrishikesh Sathyanarayan, Victor Vantilborgh, Harish Ravichandar, Tom Lefebvre, Ian Abraham
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

接触丰富（contact-rich）的机器人操作任务，如抓取、推滑、在手内调整姿态等，往往同时受到质量分布、摩擦系数、惯性和接触模式变化等不确定因素影响，控制策略需要在复杂物理交互中保持稳定与可靠。现有数据驱动方法通常依赖大量训练样本和算力，在样本有限时性能会明显退化；而传统基于模型的控制虽然高效、可解释，但对任务相关不确定性的表达能力不足，容易在接触场景中表现保守或失效。因此，如何在不依赖大规模训练的前提下，让模型式控制更好地“知道该对哪些不确定性敏感”，是这项工作值得关注的核心原因。

#### 方法概述和架构

论文提出一种基于 Stein variational inference 的分布鲁棒控制方法，称为 SV-DRO（Stein Variational Distributionally Robust Control）。其核心思路是把机器人操作中的参数不确定性建模为一个任务相关的后验分布，而不是固定的最坏情况或静态先验分布。方法首先在 MPC/滚动优化框架下，使用带接触的动力学与代价函数对轨迹进行前向 rollout；随后通过 Stein variational gradient descent（SVGD）从先验参数粒子出发，迭代更新粒子分布，使其向“对当前任务最敏感”的参数区域移动。这样得到的粒子集合构成一个可并行计算的非参数不确定性近似，控制器再基于这些粒子对应的轨迹损失进行分布鲁棒优化。与传统 DRO 相比，它不是对全局最坏情况一味保守，而是将不确定性重塑到真正影响任务成败的方向上，从而在保持性能的同时提高鲁棒性。

#### 实验结果分析

论文在多种接触丰富的操作任务上验证了方法，包括 in-hand dynamic positioning 和 bimanual Push-T，并进一步展示了连续滚动实验中的稳定表现。作者将其与现有的模型式 DRO 方法、集成式最坏情况控制等基线进行比较，结果显示在广泛参数不确定性下鲁棒性最高可提升 3 倍。节选中没有给出具体的实验表格数值与指标细节，因此可见文本未给出具体数值；但整体结论明确表明，该方法在不牺牲任务性能的前提下显著增强了接触操作的可靠性。

<details>
<summary>完整摘要</summary>

可靠的机器人操作需要控制策略能够准确表征并适应来自接触丰富交互的不确定性。现代数据驱动方法通常依赖大规模训练和计算来缓解不确定性，但在训练样本数量有限时性能会显著下降。相比之下，经典基于模型的控制器计算效率高且更可靠，但其对任务相关不确定性的表达能力有限，可能削弱其在接触丰富交互中的表现。本文提出通过更灵活的不确定性建模来扩展模型式操作控制的能力，在保持性能的同时精确适应不确定性。我们将操作问题表述为一个分布鲁棒控制优化问题，并提出一种基于 Stein variational inference 的新型确定性形式，在显式建模任务敏感参数不确定性的同时保持性能。由此得到的控制器能够更好地感知任务对不确定性的敏感性，从而在不牺牲性能的前提下获得更高可靠性。实验结果表明，在广泛的参数不确定性下，所提方法在多种接触丰富的操作任务上鲁棒性最高可提升 3 倍，并优于现有的模型式控制方法。

</details>

---

### [[20_Research/Papers/机器人/Probabilistic_Recursively_Feasible_Motion_Planning_Under_Uncertain_Environments|Probabilistic Recursively Feasible Motion Planning Under Uncertain Environments]]

![[assets/2605.19015_figure.png|800]]

- **arXiv**: [2605.19015](https://arxiv.org/abs/2605.19015)
- **PDF**: https://arxiv.org/pdf/2605.19015
- **详细分析**: [[20_Research/Papers/机器人/Probabilistic_Recursively_Feasible_Motion_Planning_Under_Uncertain_Environments|Probabilistic Recursively Feasible Motion Planning Under Uncertain Environments]]
- **作者**: Hyeontae Sung, Hyeongchan Ham, Junyoung Park, Kai Ren, Heejin Ahn
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

在不确定、时变环境中进行安全运动规划，尤其是自动驾驶中的避障与变道，需要规划器在每一步都保持可行，否则一旦未来安全区域发生变化，就可能出现“当前可行、下一步不可行”的递归可行性丧失。现有基于MPC的方法虽然能在单步上施加安全约束，但对动态障碍物的未来分布传播刻画不足，往往依赖过于保守的最坏情况假设，或者需要较强且在实践中不稳定的分布收缩假设。本文值得关注之处在于，它不是简单加安全裕度，而是尝试从“预测分布如何随时间一致地演化”这一角度，给出带概率保证的递归可行规划条件。

#### 方法概述和架构

论文提出了 Probabilistic Recursively Feasible Model Predictive Control（PRF-MPC）框架，用于在随机动态障碍物存在时实现带概率保证的递归可行规划。作者先把其他交通参与者的轨迹预测建模为高斯随机变量，并提出“理想预测器”的两个性质：一是真实分布一致性，即预测样本应服从真实运动分布；二是条件不变性，即在相同条件状态下，不同预测时刻的条件分布应一致。基于这些性质，论文推导了未来时刻轨迹预测分布的闭式均值与协方差表达，从而可以在规划时显式刻画未来安全集的演化。随后，作者构造带概率裕度的安全约束，使得当前规划步的安全集以高概率包含未来规划步的安全集，从而在缩时域MPC中概率性保证递归可行。整体流程上，输入为当前自车状态与障碍物预测分布，输出为满足安全约束的控制序列；推理时通过滚动优化不断更新，并利用未来分布传播结果来修正安全边界。

#### 实验结果分析

作者在车道变换场景中进行了仿真验证，并与现有方法的递归可行性表现进行了对比。结果表明，所提方法能显著提升递归可行性，且相比依赖强假设的先前充分条件，更能在实际预测分布下保持稳定。正文节选中还指出，已有方法在规划时域增大时，其条件满足率会急剧下降，而PRF-MPC能够维持较高的RF rate；但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

在不确定、时变环境中进行安全运动规划具有挑战性，因为安全区域会在不同规划步之间不可预测地变化，常常导致递归可行性丧失。本文提出一种概率递归可行模型预测控制（PRF-MPC）框架，以指定概率保证递归可行性。我们引入理想预测器应满足的性质，以确保分布一致性，并利用这些性质推导未来时刻预测轨迹的均值与协方差的闭式表达。基于这一分析，我们构建了安全约束，使当前安全集在高概率下包含未来时刻的安全集，从而以概率方式保证递归可行性。针对车道变换场景的仿真结果表明，所提方法显著提升了递归可行性。

</details>

---

### [[20_Research/Papers/机器人/Adversarial_Stress_Testing_of_SPARK_Humanoid_Safety_Filters|Adversarial Stress Testing of SPARK Humanoid Safety Filters]]

![[assets/2605.19009_figure.png|800]]

- **arXiv**: [2605.19009](https://arxiv.org/abs/2605.19009)
- **PDF**: https://arxiv.org/pdf/2605.19009
- **详细分析**: [[20_Research/Papers/机器人/Adversarial_Stress_Testing_of_SPARK_Humanoid_Safety_Filters|Adversarial Stress Testing of SPARK Humanoid Safety Filters]]
- **作者**: Saurav Ghosh, Abdou Sow, Luke Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Security

#### 研究背景与动机

人形机器人在真实环境中部署时，需要同时满足高维身体动力学、复杂碰撞约束以及与人和障碍物近距离共存的安全要求，因此安全过滤器成为机器人控制中的关键组件。现有方法虽然能在标准基准上给出不错的平均分，但并不能充分揭示它们在障碍物密集、感知有噪声或信息延迟等更困难场景下的失效模式。本文围绕 SPARK 人形机器人安全过滤基准，重点关注“名义性能好”是否真的意味着“足够鲁棒”，因此具有很强的工程和部署价值。

#### 方法概述和架构

此外，他们还将障碍物数量改为 5、15 和 30，以评估障碍拥挤度对安全行为的影响，并用目标距离、最小环境距离与碰撞步数来衡量安全性与任务效率之间的权衡。

#### 实验结果分析

作者还指出，在感知噪声和传感器延迟条件下，安全行为会发生明显变化，说明仅依赖名义 benchmark 分数不足以评估人形机器人自主系统的真实鲁棒性。

<details>
<summary>完整摘要</summary>

人形机器人由于身体维度高、碰撞约束多，并且必须在接近人和障碍物的环境中运行，因此很难安全部署。安全过滤器通过在名义控制动作可能违反避障约束时对其进行修改来提供帮助。然而，名义基准分数并不能充分展示这些过滤器在更困难环境中的行为。本文通过复现与压力测试研究 SPARK 人形机器人安全过滤器的鲁棒性。我们在 MuJoCo 中复现了 SPARK 的基准案例 G1SportMode_D1_WG_SO_v1，并在受控随机种子下评估 RSSA、RSSS、SSA、CBF、PFM 和 SMA。我们还构建了一个后处理流水线，将 SPARK 原始日志转换为目标跟踪、最小距离和碰撞步数等指标。结果显示，某些方法能够更紧密地跟踪目标，而另一些方法则更有效地减少碰撞步数。进一步的压力测试表明，当障碍物变得拥挤、距离估计存在噪声、或障碍物信息出现延迟时，安全行为会发生变化。这些发现表明，人形机器人的自主系统应当超越名义性能进行评估，并使用能够揭示部署前失效模式的指标。

</details>

---
