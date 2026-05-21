# cs.AI | Artificial Intelligence | 2026-05-20

#arxiv #ComputerScience

**论文数**: 39

### [[20_Research/Papers/大模型/A_Methodology_for_Selecting_and_Composing_Runtime_Architecture_Patterns_for_Production_LLM_Agents|A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents]]

![[assets/2605.20173_first_page.png|800]]

- **arXiv**: [2605.20173](https://arxiv.org/abs/2605.20173)
- **PDF**: https://arxiv.org/pdf/2605.20173
- **详细分析**: [[20_Research/Papers/大模型/A_Methodology_for_Selecting_and_Composing_Runtime_Architecture_Patterns_for_Production_LLM_Agents|A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents]]
- **作者**: Vasundra Srinivasan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

生产环境中的 LLM agent 往往把随机生成的模型输出与确定性的业务系统耦合在一起，但两者之间的“接口”通常没有被当作一等架构对象来设计。论文指出，很多真实故障并不是模型本身坏了，而是运行时架构在状态维护、工作协调、权限控制以及写入前校验这些环节上存在缺口。随着底座模型能力持续提升、单次调用的随机性逐渐下降，决定长期可靠性的关键会越来越转向运行时模式选择与边界设计，因此这篇工作对生产级 agent 架构具有较强的现实价值。

#### 方法概述和架构

作者提出了“随机-确定性边界”（SDB）这一核心概念，将 LLM 输出变成系统动作的过程抽象为四个部分：提议者、验证器、提交步骤和拒绝信号。围绕 SDB，论文把生产级 agent 运行时归纳为三个关注点：协调、状态和控制，并整理出六种可组合的运行时模式，分别覆盖层级委派、散射-聚合加 saga、事件驱动顺序、共享状态机、监督器加门控、以及人类介入。论文进一步给出一个五步选择方法：先判定运行时类型，再选择主干模式，然后补充协调、用控制机制封边，最后按步骤构建并通过验证清单检查。为了便于落地，作者还提出了一套诊断流程，可将生产故障映射到具体模式的薄弱环节，并定义了 replay divergence 这一新故障类型，用来描述 deterministic event log 在模型版本或提示变化后被 LLM 消费时产生的下游分歧。

#### 实验结果分析

论文基于五个工作负载验证了所提方法，覆盖会话式、自主式和长周期三类运行时，并为其中一个 90 天合同续约 agent 提供了可运行参考实现；实验数据来自公共 IBM Telco Customer Churn 数据集。作者还审计了 5 个常用开源 agent 框架中的 21 个 LLM-to-action 调用点，发现其中 19 个显式包含验证与提交逻辑；同时分析了 21 个已公开的 agent 失败复盘，发现 15 个（71%）可归因于边界薄弱，17 个（81%）的修复都在强化验证、提交语义或拒绝信号。节选文本中未给出完整的性能指标数值，但整体结论是：随着模型方差下降，架构模式选择和 SDB 强度会成为影响长期可靠性的更重要杠杆。

<details>
<summary>完整摘要</summary>

生产级大型语言模型（LLM）代理将随机的模型输出与确定性软件系统组合在一起，但这两者之间的边界很少被当作一等架构对象来处理。本文将这一边界命名为“随机-确定性边界”（stochastic-deterministic boundary, SDB）：它是由提议者、验证器、提交步骤和拒绝信号组成的四部分契约，用来规定 LLM 输出如何转化为系统动作。我们认为，SDB 是生产级 agent 运行时中承重性的基础原语。围绕这一原语，我们将 agent 运行时设计组织为三个关注点：协调、状态和控制。本文给出六种可组合运行时模式，分别以不同方式围绕 SDB 组织会话式、自主式和长周期 agent：层级委派、散射-聚合加 saga、事件驱动顺序、共享状态机、监督器加门控，以及人类介入。对于每种模式，我们追溯其分布式系统概念来源，并说明当工作者变为随机性组件时，会发生哪些变化。本文还贡献了一套五步方法，用于选择运行时模式；一套诊断流程，用于将生产故障映射到模式弱点；以及一种名为 replay divergence 的故障模式，即基于 LLM 的 deterministic event log 消费者在模型版本或提示变化后会产生不同的下游输出。一个简化的可靠性分解将每次调用的模型方差与架构动量分离，支持这样一个观点：随着模型方差降低，模式选择和 SDB 强度会成为长期可靠性中越来越关键的杠杆。我们将该方法应用于五个工作负载，并提供了一个针对 90 天合同续约 agent 的可运行参考实现。

</details>

---

### [[20_Research/Papers/具身智能/Probing_Embodied_LLMs_When_Higher_Observation_Fidelity_Hurts_Problem_Solving|Probing Embodied LLMs: When Higher Observation Fidelity Hurts Problem Solving]]

![[assets/2605.20072_figure.png|800]]

- **arXiv**: [2605.20072](https://arxiv.org/abs/2605.20072)
- **PDF**: https://arxiv.org/pdf/2605.20072
- **详细分析**: [[20_Research/Papers/具身智能/Probing_Embodied_LLMs_When_Higher_Observation_Fidelity_Hurts_Problem_Solving|Probing Embodied LLMs: When Higher Observation Fidelity Hurts Problem Solving]]
- **作者**: Oussama Zenkri, Oliver Brock
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

这篇论文关注具身智能中的闭环问题求解：让大模型作为机器人“认知中枢”，在真实环境里边观察、边行动、边更新判断，完成带有隐藏约束的序列机械任务。作者指出，现有评测往往只看最终成功率，但在具身场景中，成功或失败可能同时受到感知误差、动作反馈噪声和推理缺陷影响，因此很难据此判断模型到底是真的会解题，还是“碰巧”表现不错。文章之所以值得关注，在于它提出了一个反直觉现象：更高保真度的观测未必带来更好表现，甚至可能让模型更差。

#### 方法概述和架构

论文以 Lockbox 机械锁箱作为诊断任务，这是一个由多个二元关节组成、依赖关系隐藏且需要按顺序推理的实体谜题。作者在真实机器人系统中测试 LLM 代理，分别给模型提供三种观测通道：RGB 图像、RGB-D 图像，以及直接给出所有关节状态的符号化真值观测。每一步交互中，机器人执行模型选定的关节操作，再把新的观测回传给模型，形成闭环决策流程；整个试验在固定初始状态下进行，并限制最多 20 步。为了进一步解释现象，作者还在模拟环境中系统性地扰动模型对动作结果的感知，通过随机翻转“观测到的动作结果”来控制噪声强度，并考察噪声如何改变成功率与行为模式。

#### 实验结果分析

在真实机器人 Lockbox 实验中，GPT o1 在三种输入模态下的表现呈现反直觉趋势：RGB 输入最好，RGB-D 居中，而提供“更准确”的符号真值状态反而最差。作者还发现，human-inspired strategy 在所有模态下都优于 GPT o1，且以更少交互步数达到 100% 成功；相比之下，GPT o1 的最高成功率为 80%，但不同模态下达到该结果所需步数不同，说明仅看最终成功率会掩盖效率差异。模拟实验进一步表明，适度噪声反而有利于解题：当感知结果以约 40% 的概率被翻转时，成功率达到峰值，相比无噪声基线提高了 2.85 倍。作者将这种收益与“重复动作循环”减少联系起来，说明噪声可能打断了模型的低效循环行为；可见文本未给出更完整的消融细节。

<details>
<summary>完整摘要</summary>

大型语言模型（LLM）正越来越多地被提议作为机器人系统中的认知组件，但其不透明的决策过程使得在闭环具身任务中难以解释成功或失败。遵循经验式 AI 方法论，我们通过改变代理可获得的信息并测量由此引起的行为变化，从行为层面研究具身 LLM 代理。我们使用 Lockbox 这一具有隐藏相互依赖关系的顺序机械谜题，在真实机器人系统中分别以 RGB、RGB-D 和真值符号化观测评估 LLM，并结合受控仿真来探测其行为。结果出人意料：代理在原始 RGB 输入下表现最好，而在完美的真值观测下表现最差。在仿真中，我们通过随机翻转感知到的动作结果来探究这一现象，发现适度噪声会提升性能，并在 40% 的翻转概率处达到峰值，相比无噪声基线，成功率提高了 2.85 倍。进一步分析表明，这种收益与重复动作循环的减少有关。这些发现说明，仅用成功率不足以评估 LLM，因为测得的性能可能反映的是感知误差与推理失败之间的相互作用，而不一定代表稳健的问题求解能力。

</details>

---

### [[20_Research/Papers/大模型/Towards_LLM-Assisted_Architecture_Recovery_for_Real-World_ROS~2_Systems_An_Agent-Based_Multi-Level_Approach_to_Hierarchical_Structural_Archi|Towards LLM-Assisted Architecture Recovery for Real-World ROS~2 Systems: An Agent-Based Multi-Level Approach to Hierarchical Structural Architecture Reconstruction]]

![[assets/2605.20055_figure.png|800]]

- **arXiv**: [2605.20055](https://arxiv.org/abs/2605.20055)
- **PDF**: https://arxiv.org/pdf/2605.20055
- **详细分析**: [[20_Research/Papers/大模型/Towards_LLM-Assisted_Architecture_Recovery_for_Real-World_ROS~2_Systems_An_Agent-Based_Multi-Level_Approach_to_Hierarchical_Structural_Archi|Towards LLM-Assisted Architecture Recovery for Real-World ROS~2 Systems: An Agent-Based Multi-Level Approach to Hierarchical Structural Architecture Reconstruction]]
- **作者**: Dominique Briechle, Raj Chanchad, Tobias Geger, Ruidi He, Dhruv Jajadiya, Dhruv Kapadiya, Andreas Rausch, Meng Zhang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，大模型 0.8，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

在 ROS 2 机器人系统中，系统结构、节点组合关系、命名空间、重映射以及 launch 文件引导的运行时装配，往往分散隐含在源码、launch 与配置等多个工件里，缺少统一且可维护的架构模型。对于协作机械臂、传感器和控制器高度耦合的真实系统，传统只关注节点级连接的恢复方法，难以还原多层次的层级结构与子系统边界。本文之所以值得关注，是因为它将大模型引入 ROS 2 架构恢复，并专门针对“分层结构重建”这一长期难点做了系统化改进。

#### 方法概述和架构

作者在先前的 blueprint-guided LLM-assisted architecture recovery pipeline 基础上，提出一种基于 agent 的多层级分阶段恢复方法。方法首先保留一个 UML 风格的蓝图作为目标架构词汇表，用来约束 LLM 可生成的元素与关系，避免自由生成带来的幻觉和结构不一致。随后，系统不再直接从原始仓库材料一次性合成完整架构，而是先抽取原子级 ROS 节点及其本地通信接口，再进一步构建 launch 依赖与节点实例等中间表示。接着，利用这些中间层证据显式表达 launch 文件包含关系、节点实例化、命名空间传播、重映射与子系统组合，再由 LLM 在约束下逐层合成更高层级的系统架构。论文还强调了提示词重设计与 prompt-contract 机制，通过更细粒度、可控的上下文注入，提升结构生成的一致性、可追溯性和可控性。

#### 实验结果分析

作者在一个真实世界的自动积木拆解 ROS 2 系统 BrickByBrick 上评估该方法，该系统包含协作机械臂、深度相机、输送带以及异构 ROS 2 工件，集成复杂度明显高于前一版实验案例。实验表明，相比此前工作，这种分阶段恢复策略在结构一致性、可扩展性和鲁棒性方面都有提升。文中还指出，该方法在更复杂的 launch 驱动集成场景下仍面临挑战，尤其是动态集成语义的恢复；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

显式的软件架构模型是用于沟通、分析和演化复杂软件密集型系统的重要工件。然而，在基于 ROS 2 的机器人系统中，结构性的（解）组合与集成语义往往只是隐式地编码在源码和 launch 文件等分布式工件中，因此恢复层级化架构尤其困难。现有方法主要聚焦于节点级实体和通信连线，而对跨多个抽象层级的层级结构性（解）组合恢复支持有限。本文在我们此前提出的、面向 ROS 2 系统的 blueprint-guided LLM-assisted architecture recovery pipeline 基础上做了两项主要增强：（1）改进提示设计，以提高架构合成的一致性和可控性；（2）提出一种基于多层中间架构表示的分阶段恢复策略，将原子 ROS 节点列表和 launch 文件依赖纳入其中，从而支持在多个抽象层级上进行结构受约束的重建。我们在一个真实世界的自动化产品拆解系统上评估了该方法，该系统基于协作机械臂并包含异构 ROS 2 工件。与我们之前的工作相比，本次研究的案例集成复杂度更高、功能更丰富。结果表明，该方法在结构一致性、可扩展性和恢复鲁棒性方面均有所提升，同时也揭示了在大规模 ROS 2 系统中恢复动态集成语义仍然存在的挑战。

</details>

---

### [[20_Research/Papers/强化学习/When_Critics_Disagree_Adaptive_Reward_Poisoning_Attacks_in_RIS-Aided_Wireless_Control_System|When Critics Disagree: Adaptive Reward Poisoning Attacks in RIS-Aided Wireless Control System]]

![[assets/2605.20037_figure.png|800]]

- **arXiv**: [2605.20037](https://arxiv.org/abs/2605.20037)
- **PDF**: https://arxiv.org/pdf/2605.20037
- **详细分析**: [[20_Research/Papers/强化学习/When_Critics_Disagree_Adaptive_Reward_Poisoning_Attacks_in_RIS-Aided_Wireless_Control_System|When Critics Disagree: Adaptive Reward Poisoning Attacks in RIS-Aided Wireless Control System]]
- **作者**: Deemah H. Tashman, Soumaya Cherkaoui
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.02（加权：大模型 0.1，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

这篇论文聚焦于RIS辅助的认知无线电网络中的深度强化学习控制问题：智能体需要同时优化SU发射功率和RIS相位，以提升次用户的长期传输速率，并满足对主用户干扰约束。与通常只考虑性能提升不同，作者关注训练阶段的安全性，指出奖励投毒会直接误导SAC的价值估计，尤其在高不确定、高影响力状态下更危险。现有奖励攻击多依赖固定时序或探索触发，缺少对学习状态和模型不确定性的自适应利用，因此在真实无线控制场景中的鲁棒性评估并不充分。这使得该工作对强化学习安全、RIS控制与无线智能体部署都具有较强参考价值。

#### 方法概述和架构

论文提出Disagreement-Guided Reward Poisoning（DGRP）攻击，用于针对SAC智能体的训练过程进行隐蔽式奖励污染。其核心触发信号是双评论家Q1和Q2在当前状态-动作对上的“critic disagreement”，即两者输出差值；当该差值超过滚动窗口内的分位数阈值时，该步被视为高不确定、高杠杆状态。攻击者并不修改观测或动作，只在满足条件后以概率p触发，并在奖励进入归一化前减去一个有界扰动δ，从而让训练用奖励偏离真实环境奖励。方法采用长度为w的滚动缓冲区自适应更新阈值，因此能够随着学习动态自动调节攻击敏感度，保持稀疏且难检测。整体流程是：读取SAC双评论家输出→计算不一致度→与分位数阈值比较→按概率注入奖励偏置→影响Q值更新和策略梯度，最终将策略引向次优动作。

#### 实验结果分析

实验在带RIS的认知无线电环境中进行，以SAC作为被攻击对象，并与周期性时序攻击、探索触发攻击等基线进行比较，评价目标包括次用户速率、RIS带来的性能增益和传输质量。结果表明，DGRP会显著削弱RIS通常带来的性能提升，并持续造成比基线更大的性能损伤。作者还分析了关键攻击参数对学习过程的影响，说明攻击强度和触发频率会改变训练退化程度。可见文本未给出具体数值，但结论明确支持“基于评论家分歧的自适应攻击比传统固定规则攻击更具破坏性”。

<details>
<summary>完整摘要</summary>

奖励投毒攻击对基于学习的无线控制系统构成了显著风险。基于这一点，我们在一个由可重构智能表面（RIS）辅助的软演员-评论家（SAC）智能体上，提出了一种基于分歧引导的奖励投毒（Disagreement-Guided Reward Poisoning, DGRP）自适应攻击。在认知无线电网络（CRN）环境中，SAC智能体的任务是通过同时优化次用户（SU）发射机的传输功率和RIS相位移，最大化次用户的长期速率。DGRP会在SAC双评论家出现显著分歧时对奖励进行破坏，尤其是在高杠杆、高不确定性的状态下，从而导致价值估计失真，并将策略引导到次优动作。我们的结果表明，DGRP会显著削弱RIS通常带来的性能增益，并降低传输质量。我们进一步研究了攻击的关键参数，并确定了它们对学习过程的影响。与周期性时序攻击和探索触发式基线相比，DGRP始终造成更大的破坏，这表明在评估RIS辅助网络中深度强化学习（DRL）的鲁棒性时，有必要将考虑评论家分歧的威胁纳入评估框架。

</details>

---

### [[20_Research/Papers/具身智能/World-Ego_Modeling_for_Long-Horizon_Evolution_in_Hybrid_Embodied_Tasks|World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks]]

![[assets/2605.19957_figure.png|800]]

- **arXiv**: [2605.19957](https://arxiv.org/abs/2605.19957)
- **PDF**: https://arxiv.org/pdf/2605.19957
- **详细分析**: [[20_Research/Papers/具身智能/World-Ego_Modeling_for_Long-Horizon_Evolution_in_Hybrid_Embodied_Tasks|World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks]]
- **作者**: Zuyao Lin, Jianhui Zhang, Peidong Jia, Xiaoguang Zhao, Shanghang Zhang, Xingyu Chen
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.4（加权：具身智能 1.5，世界模型 0.4，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

具身世界模型是机器人智能的重要基础，能够预测环境未来变化，用于规划、合成数据和策略学习。但现有方法往往把场景演化与机器人自身动作、意图、接触交互混在同一预测流中，难以区分“世界”的持续场景规律与“ego”的任务驱动动态。这个问题在长时程、尤其是导航与操作交织的混合具身任务中会更明显，容易出现时序不一致和指令对齐变弱。因而，本文关注的是如何为长链路具身预测建立更合理的“世界—ego”分解方式。

#### 方法概述和架构

论文提出 World-Ego Modeling 这一概念框架，将未来演化显式拆分为世界与ego两部分，并从三种视角定义二者边界：基于运动、基于语义、基于意图。作者进一步比较了三类解耦策略，包括后解耦、前解耦和完整解耦，用来分析不同分离程度对长时程预测的影响。基于此，论文实例化出 World-Ego Model（WEM），其由两阶段组成：先用一个视觉-语言状态预测器，从初始观测、历史视频和多轮指令中推断出分离的世界状态与ego状态；再由视频生成器结合当前局部条件、当前指令及两类状态生成下一段视频。生成器内部采用串联-并行混合专家（CP-MoE）扩散结构，并通过角色条件注意力、路由与反路由等机制，让不同专家分别承担世界与ego相关的预测职责。为支撑评测，作者还构建了 HTEWorld，面向混合导航-操作任务的长时程世界建模基准，包含大规模视频片段、细粒度动作标注和多轮评测轨迹。

#### 实验结果分析

实验在 HTEWorld 上验证了 WEM 的有效性，结果表明它在该基准上取得了最先进表现，并且在现有仅操作类基准上也保持了有竞争力的结果。论文还对世界—ego 边界定义和解耦方式做了设计研究，说明不同边界与不同解耦策略会显著影响性能，其中语义边界配合完整解耦效果最好。可见文本未给出具体数值，但作者明确指出其在混合导航-操作的长时程回滚生成上优于同等训练数据下的以往方法。整体上，结果支持“先分解、再生成”的建模思路比单流式预测更适合长时程具身场景。

<details>
<summary>完整摘要</summary>

世界模型在具身智能中被广泛研究，但它们通常把世界与ego的演化预测放在同一条单一生成流中：其中，世界负责捕捉持久的、与指令无关的场景规律，ego则负责捕捉以机器人为中心、受指令条件控制的动态。这种 world-ego 纠缠会导致长时程具身场景下性能下降，尤其是在导航与操作行为交错出现的混合任务中更为明显。本文提出 World-Ego Modeling 这一新的概念范式，将未来演化分解为世界与ego两个组成部分。我们从三个视角定义 world-ego 边界，即基于运动、基于语义和基于意图的视角，并分析了三种解耦策略：后解耦、前解耦和完整解耦。进一步地，我们将这一范式实例化为 World-Ego Model（WEM），它是一种统一的具身世界模型，将隐式的分离式 world-ego 规划器与串联-并行混合专家（CP-MoE）扩散生成器结合起来。为了支持严格评测，我们还构建了 HTEWorld，这是首个面向长时程世界建模、覆盖混合导航-操作任务的基准，提供了 12.5 万个视频片段（超过 450 万帧）及细粒度动作标注，以及 300 条多轮评测轨迹（超过 2000 条指令）。大量实验表明，WEM 在 HTEWorld 上取得了最先进的性能，同时在已有的仅操作类基准上也保持了竞争力。

</details>

---

### [[20_Research/Papers/机器人/Robotics-Inspired_Guardrails_for_Foundation_Models_in_Socially_Sensitive_Domains|Robotics-Inspired Guardrails for Foundation Models in Socially Sensitive Domains]]

![[assets/2605.19940_figure.png|800]]

- **arXiv**: [2605.19940](https://arxiv.org/abs/2605.19940)
- **PDF**: https://arxiv.org/pdf/2605.19940
- **详细分析**: [[20_Research/Papers/机器人/Robotics-Inspired_Guardrails_for_Foundation_Models_in_Socially_Sensitive_Domains|Robotics-Inspired Guardrails for Foundation Models in Socially Sensitive Domains]]
- **作者**: Rebecca Ramnauth, Drazen Brscic, Brian Scassellati
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

基础模型正越来越多地被用于教育、心理健康和照护等社会敏感场景，这些场景中的失败往往不是一次性错误，而是会在长时间交互中逐步累积并受上下文强烈影响。现有 guardrail 方法更多是在训练阶段对齐、提示约束、解码限制或事后审核，主要提供的是经验性的风险降低，而不是可在运行时强制执行的行为保证。论文关注的核心问题是：当模型作为持续交互系统的一部分时，如何把“安全”从单轮输出质量，提升为对整段交互轨迹的实时控制。这个问题在机器人与具身智能中已有成熟的约束控制思路，因此值得借鉴到 foundation models 的社会交互安全中。

#### 方法概述和架构

论文将基础模型的守护机制重构为“运行时行为控制”问题，并借用机器人中的安全集合、不变式、运行时 shielding、lookahead、fallback 和分层控制等技术概念。作者提出 Grounded Observer 框架，将系统拆分为基础模型（base）和观察器（observer）：base 负责生成候选动作或回复，observer 根据外部指定的约束对这些候选进行评估。系统通过特征提取与行为表征，把对话状态和动作映射为可检查的运行时表示，并用覆盖规则（overlay rules）表达行为约束，例如是否越界、是否偏离目标角色或是否进入不适当的交互模式。若候选动作不满足约束，框架可在运行时执行过滤、纠正、重生成或重定向，从而把控制点放在推理阶段而非重新训练模型。该框架还讨论了约束刚性、容错性、分层推理以及可扩展性，支持为不同任务配置不同观察器和不同强度的 overlay。

#### 实验结果分析

论文没有给出统一的量化基准结果；从节选可见，作者在三个真实部署场景中验证了框架：small talk、入户 autism therapy，以及学校中的行为降温/去激化。实验对比的重点不是单一数值指标，而是观察运行时干预是否能在交互轨迹中抑制系统漂移到不期望的行为模式，同时保持对不同社会情境的适应性。文本强调，该框架在这些场景中都能通过运行时介入降低失控风险，但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

基础模型正越来越多地被部署到教育、心理健康和照护等社会敏感领域，在这些场景中，失败往往是累积性的，并且高度依赖上下文。现有的 guardrail 方法——从训练阶段对齐，到提示、解码约束以及事后审核——主要提供的是经验性的风险降低，而不是可强制执行的行为保证；而且它们大多把安全看作单个输出的属性，而不是把交互轨迹作为整体来处理。我们将 guardrail 重新定义为对交互轨迹进行运行时行为控制的问题，并借鉴机器人领域中对不确定闭环系统实施约束的正式构念。基于这一思路，我们提出 Grounded Observer 框架，并将其应用于三个真实部署场景：small talk、入户 autism therapy，以及学校中的行为降温/去激化。在不同场景中，该框架都能在运行时进行干预，抑制系统漂移到不良交互 რეჟიმ，同时适应多样的社会情境。我们进一步讨论了该框架的扩展方向，并提出了迈向更强保证的研究路径。

</details>

---

### [[20_Research/Papers/大模型/PEEK_Context_Map_as_an_Orientation_Cache_for_Long-Context_LLM_Agents|PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents]]

![[assets/2605.19932_first_page.png|800]]

- **arXiv**: [2605.19932](https://arxiv.org/abs/2605.19932)
- **PDF**: https://arxiv.org/pdf/2605.19932
- **详细分析**: [[20_Research/Papers/大模型/PEEK_Context_Map_as_an_Orientation_Cache_for_Long-Context_LLM_Agents|PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents]]
- **作者**: Zhuohan Gu, Qizheng Zhang, Omar Khattab, Samuel Madden
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

大模型智能体正在越来越多地面对长上下文、且会反复出现的外部环境，例如文档语料库、代码仓库等。在这类重复访问同一上下文的任务中，现有方法通常只保留智能体的历史轨迹、对原始材料的被动访问能力，或任务层面的通用策略，却没有显式保存关于“这个上下文本身”的可复用定位知识。作者认为，真正关键的是上下文里有哪些内容、如何组织、哪些实体/常量/Schema 在历史上最有用等这种“定向知识”，因此提出值得关注的 PEEK。

#### 方法概述和架构

PEEK 将可复用的上下文定向知识缓存为一个固定大小的“context map”，并把它放入智能体提示词中，使智能体能够持续“窥见”外部上下文。该 map 不是静态生成的，而是由一个可编程的缓存策略持续维护，包含三个模块。Distiller 负责从推理时信号中提取可迁移的知识；Cartographer 负责把这些知识翻译成结构化编辑；Evictor 则基于优先级管理，保证整体 token 预算固定不变。三个模块串联起来后，系统在每次调用时都能根据新的交互经验更新 context map，再把更新后的 map 作为长期记忆反馈给后续的智能体推理。

#### 实验结果分析

在长上下文推理和信息聚合任务上，PEEK 相比强基线提升了 6.3%–34.0%，同时减少了 93–145 次迭代，并且相较于当前最先进的 prompt-learning 框架 ACE，成本降低到 1.7–5.8 倍更少。 在 context learning 任务上，PEEK 的 solving rate 和 rubric accuracy 分别提升了 6.0%–14.0% 和 7.8%–12.1%，且成本比 ACE 低 1.4 倍。 这些收益还可泛化到不同语言模型与不同智能体架构，包括生产级编码智能体 OpenAI Codex，说明 context map 对于重复性外部上下文任务具有通用价值。

<details>
<summary>完整摘要</summary>

大型语言模型（LLM）智能体正越来越多地在长而且反复出现的外部上下文中运行，例如文档语料库和代码仓库。在多次调用之间，现有方法通常只保留智能体的轨迹、对原始材料的被动访问，或者任务级策略。我们认为，这些方法都没有保留在重复的同一上下文工作负载中最需要的东西：关于反复出现的上下文本身的可复用定向知识，例如上下文包含什么、如何组织，以及哪些实体、常量和 Schema 在历史上最有用。为此，我们提出 PEEK，一种将这种定向知识缓存并维护为 context map 的系统：它是智能体提示词中的一个小而恒定大小的工件，能够让智能体持续“窥见”外部上下文。该 map 由一个可编程缓存策略维护，这个策略包含三个模块：Distiller 负责从推理时信号中提取可迁移知识，Cartographer 负责将其转化为结构化编辑，priority-based Evictor 则负责在固定 token 预算下进行约束。在长上下文推理和信息聚合任务上，PEEK 相比强基线提升了 6.3%–34.0%，同时使用的迭代次数少了 93–145 次，并且相较于最先进的 prompt-learning 框架 ACE，成本降低了 1.7–5.8 倍。在 context learning 任务上，PEEK 的 solving rate 和 rubric accuracy 分别提升了 6.0%–14.0% 和 7.8%–12.1%，且成本比 ACE 低 1.4 倍。这些收益可推广到不同语言模型和不同智能体架构，包括生产级编码智能体 OpenAI Codex。综合来看，这些结果表明，context map 能帮助长上下文 LLM 智能体以更准确、更高效的方式与重复出现的外部上下文交互。

</details>

---

### [[20_Research/Papers/大模型/Prior_Knowledge_or_Search_A_Study_of_LLM_Agents_in_Hardware-Aware_Code_Optimization|Prior Knowledge or Search? A Study of LLM Agents in Hardware-Aware Code Optimization]]

![[assets/2605.19782_first_page.png|800]]

- **arXiv**: [2605.19782](https://arxiv.org/abs/2605.19782)
- **PDF**: https://arxiv.org/pdf/2605.19782
- **详细分析**: [[20_Research/Papers/大模型/Prior_Knowledge_or_Search_A_Study_of_LLM_Agents_in_Hardware-Aware_Code_Optimization|Prior Knowledge or Search? A Study of LLM Agents in Hardware-Aware Code Optimization]]
- **作者**: Dmitry Redko, Albert Fazlyev, Konstantin Sozykin, Maria Ivanova, Evgeny Burnaev, Egor Shvetsov
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

大模型驱动的代码优化与发现系统正在被广泛用于自动生成、改写和调优程序，尤其是在需要根据反馈不断迭代的场景中，如编译器优化、内核生成和硬件感知代码调优。此类系统通常遵循“提出—评估—修订”的循环，但在实际应用中，LLM到底是依赖环境反馈进行搜索，还是更多依赖预训练形成的先验知识，尚不清楚。与此同时，随着LLM agent结构越来越复杂，不同模块对最终优化效果的贡献也难以拆分评估，因此这项研究值得关注。

#### 方法概述和架构

论文通过三组受控实验，系统考察LLM agent在硬件感知代码优化任务中的行为机制。第一组实验是纯黑盒优化，观察模型在只有目标函数反馈时是否会表现出真正的探索式搜索。第二组实验是zero-shot kernel generation，向模型显式提供输入尺寸信息，并比较不同尺寸与不同temperature设置下生成的kernel参数是否会发生变化。第三组实验是带反馈循环的kernel优化，将模型放入多轮“生成—反馈—再生成”的流程中，分别在CUDA和TVM IR两种表示上进行对比，以分析语言表示密度对优化过程的影响。

#### 实验结果分析

实验表明，在纯黑盒优化中，LLM更像是贪心优化器，而不是进行充分探索的搜索器。对于zero-shot kernel生成，显式输入尺寸信息几乎没有可测影响，不同尺寸和temperature下模型最终收敛到相同的kernel参数；当任务变为少见尺寸的kernel优化时，性能会明显下降，且这一现象与所使用的语言无关。带反馈循环的实验进一步显示，CUDA在迭代反馈下性能持续单调改善，而TVM IR则会主动退化，说明当模型处理低密度语言表示时，kernel优化能力会下降。文中未给出具体数值，因此可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

LLM发现与优化系统正越来越多地被应用于各个领域，其核心通常实现为一个“提出—评估—修订”的循环。此类优化或发现过程，是通过对来自环境的反馈进行上下文条件化来推进的。然而，随着现代LLM agent的结构日益复杂，要评估哪些组件贡献最大，以及这种探索会在何时、以何种方式失败，变得十分困难。我们通过三组受控实验回答这些问题。我们的发现是：（1）在纯黑盒优化中，LLM表现为贪心优化器。（2）在zero-shot kernel生成中，提供显式的输入尺寸信息没有可测影响；无论尺寸或temperature如何，模型都收敛到相同的kernel参数，仿佛尺寸指令对它们不可见。此外，当任务变为对不常见kernel尺寸进行优化时，无论使用何种语言，性能都会急剧下降。（3）在带反馈循环的kernel优化中，CUDA在迭代反馈下单调改进，而TVM IR会主动退化，这表明当模型使用低密度语言时，kernel优化会退化。我们的结果表明，在代码优化任务中，LLM高度依赖预训练先验，而不是依赖给定反馈或agent结构。

</details>

---

### [[20_Research/Papers/强化学习/Memory-Augmented_Reinforcement_Learning_Agent_for_CAD_Generation|Memory-Augmented Reinforcement Learning Agent for CAD Generation]]

![[assets/2605.19748_first_page.png|800]]

- **arXiv**: [2605.19748](https://arxiv.org/abs/2605.19748)
- **PDF**: https://arxiv.org/pdf/2605.19748
- **详细分析**: [[20_Research/Papers/强化学习/Memory-Augmented_Reinforcement_Learning_Agent_for_CAD_Generation|Memory-Augmented Reinforcement Learning Agent for CAD Generation]]
- **作者**: Yin Xiaolong, Liu Yu, Shen Jiahang, Lu Xingyu, Ni Jingzhe, Fan Fengxiao, Sang Fan
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.5，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

自动生成 CAD 模型是实现先进制造智能化的核心能力之一，尤其适用于需要高效率、可重复和高一致性的工业设计场景。现有基于大语言模型（LLM）的生成方法，在面对复杂 CAD 模型时往往表现不足，因为这类任务通常包含很长的操作序列、多样的操作类型以及强几何约束，容易出现推理链中断。与此同时，缺少有效的错误纠正机制，也会导致生成过程在中途偏离设计意图。这使得面向复杂 CAD 生成的强化学习与记忆增强方法具有较高关注价值。

#### 方法概述和架构

本文提出一种用于 CAD 生成代理的记忆增强强化学习框架。该框架首先将底层几何内核封装为结构化工具链，供智能体在生成过程中调用，从而把“理解设计意图—全局规划—执行—多维验证”组织成闭环流程。系统设计了双轨记忆模块，包括案例库与技能库：前者保存可复用的历史设计实例，后者沉淀可调用的操作技能与策略。为避免检索到语义相似但几何上不可行的错误样例，论文提出动态效用检索算法，并将强化学习引入检索策略与行为策略优化，使智能体能够在推理过程中自我修正并持续演化。整体上，模型的输入是设计目标与当前生成状态，输出是可执行的 CAD 操作序列及对应的几何结果。

#### 实验结果分析

实验结果表明，该方法在复杂 CAD 模型生成任务上显著提升了生成成功率和几何一致性。论文摘要中未给出具体实验数据、数据集名称或基线模型细节，可见文本未给出具体数值。整体结论显示，记忆增强与强化学习结合后，智能体能够更有效地规避“检索陷阱”，并减少由错误案例引发的几何不可行问题。

<details>
<summary>完整摘要</summary>

自动生成计算机辅助设计（CAD）模型是实现先进制造智能化的核心技术。现有基于大语言模型（LLM）的生成方法在处理复杂 CAD 模型时往往表现不足，这类模型通常具有长操作序列、多样操作类型和强几何约束，主要原因在于推理链会中断，且缺乏有效的错误纠正机制。为了解决这一问题，本文提出一种面向 CAD 生成智能体的记忆增强强化学习框架。该框架将底层几何内核封装为可由智能体调用的结构化工具链，并构建了一个由设计意图理解、全局规划、执行和多维验证组成的闭环机制。与此同时，框架还设计了由案例库和技能库组成的双轨记忆模块，并提出一种动态效用检索算法。通过将强化学习引入检索与策略优化，智能体能够有效避免“检索陷阱”，即那些在语义上相似但在几何上不可行的示例，从而在无需额外大规模标注数据的情况下实现在线自我纠正与持续演化。实验结果表明，该方法在复杂 CAD 模型生成任务上显著提升了成功率和几何一致性。

</details>

---

### [[20_Research/Papers/大模型/EngiAI_A_Multi-Agent_Framework_and_Benchmark_Suite_for_LLM-Driven_Engineering_Design|EngiAI: A Multi-Agent Framework and Benchmark Suite for LLM-Driven Engineering Design]]

![[assets/2605.19743_figure.png|800]]

- **arXiv**: [2605.19743](https://arxiv.org/abs/2605.19743)
- **PDF**: https://arxiv.org/pdf/2605.19743
- **详细分析**: [[20_Research/Papers/大模型/EngiAI_A_Multi-Agent_Framework_and_Benchmark_Suite_for_LLM-Driven_Engineering_Design|EngiAI: A Multi-Agent Framework and Benchmark Suite for LLM-Driven Engineering Design]]
- **作者**: Gioele Molinari, Florian Felten, Soheyl Massoudi, Mark Fuge
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.3（加权：大模型 1.3）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

大模型智能体正在被用于工程设计，但工程设计往往同时包含仿真、检索、制造准备和长流程编排，现有评测框架难以覆盖这类多智能体系统的真实复杂性。尤其在工程场景中，模型不仅要会调用工具，还要能在多轮流程中保持数值精度、处理条件分支，并把检索到的参数可靠地传递给后续仿真或训练步骤。本文之所以值得关注，是因为它把“工程设计智能体”从单点工具调用推进到端到端工作流、检索增强与HPC编排的统一评测。

#### 方法概述和架构

论文提出了 EngiAI，一个基于 LangGraph 的多智能体参考系统，以及与之配套的 EngiBench 风格评测套件。整个系统采用监督者-专家式架构：中央 supervisor 先解析用户意图，再把任务路由给七个专门智能体中的相应模块，每个模块以独立状态机形式运行并调用各自工具。七个智能体覆盖工程设计、信息检索、基础设施与制造相关能力，能够串联起拓扑优化、文档检索、HPC 作业编排和3D打印控制。评测套件包含三部分：其一是工作流基准，设置七种提示风格，分别考察直接工具使用、语义消歧、条件分支、工作记忆和派生计算等认知需求；其二是RAG基准，通过门控评分把“是否检索到正确资料”与“是否正确选参”分离，避免模型凭参数记忆蒙对；其三是HPC基准，评估在 SLURM 集群上完成端到端机器学习训练流程的编排能力。

#### 实验结果分析

作者在两个 EngiBench 问题上、使用四种 LLM 后端进行了测试。结果显示，商用模型在 Beams2D 上的平均任务完成率达到 96%–97%，而开源 4B 参数模型约为 55%–78%，体现出明显的代际差距。最难的是条件分支类任务，在 Photonics2D 上任务完成率降至 20%–53%；RAG 门控实验中，带检索时得分接近 1.0，而不检索时接近 0，说明评测设计确实能隔离检索贡献。HPC 编排中，不同模型的长流程稳定性差异明显：有的模型可在全部运行中完成所有步骤，而另一些仅有 50% 的成功率，可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

大型语言模型（LLM）智能体正日益被应用于工程设计任务，但现有评测框架并不能充分覆盖将仿真、检索和制造准备结合起来的多智能体系统。我们提出了一个包含三个评测维度的基准套件：（1）工作流基准，设置七种提示风格，针对不同认知需求——包括直接工具使用、语义消歧、条件分支以及工作记忆任务；（2）Retrieval-Augmented Generation（RAG）基准，采用门控评分，将检索对参数选择的贡献单独隔离出来；（3）High Performance Computing（HPC）基准，评估在 SLURM 集群上进行端到端机器学习训练编排的能力。与此同时，我们提出 EngiAI，这是一个基于 LangGraph 的多智能体系统（MAS）参考实现，通过监督者式架构协调七个专门智能体，将拓扑优化、文档检索、HPC 作业编排和3D打印机控制整合在一起，以落实该基准套件。在四种 LLM 后端和两个 EngiBench 任务上，商用模型在 Beams2D 上的平均任务完成率达到96%–97%，而开源4B参数模型达到55%–78%，并呈现出清晰的代际提升。条件分支被证明是最具挑战性的，在 Photonics2D 上，条件风格的任务完成率下降到20%–53%。RAG 门控结果确认了带检索时的得分几乎完美（约为1.0），而不使用检索时几乎为零，验证了评测设计的有效性。在HPC编排任务中，一个模型在100%的运行中完成了全部流水线步骤，而另一个模型下降到50%，说明在长时间运行的工作流中，多步指令遵循能力会退化。

</details>

---

### [[20_Research/Papers/大模型/Formal_Skill_Programmable_Runtime_Skills_for_Efficient_and_Accurate_LLM_Agents|Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents]]

![[assets/2605.19604_figure.png|800]]

- **arXiv**: [2605.19604](https://arxiv.org/abs/2605.19604)
- **PDF**: https://arxiv.org/pdf/2605.19604
- **详细分析**: [[20_Research/Papers/大模型/Formal_Skill_Programmable_Runtime_Skills_for_Efficient_and_Accurate_LLM_Agents|Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents]]
- **作者**: Xi Zhang, Meijun Gao, Yuntian Zhao, Xinyu Tan, Yilun Yao, Feiyu Wang, Yanshu Wang, Dingsiyi, Tong Yang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

大模型智能体正越来越多地进入真实工作空间，例如软件工程、办公自动化、研究辅助和运营决策等场景，这要求模型不仅“会想”，还要“会做”。现有的技能和工具虽然能把单个动作做得结构化，但常常把工作流状态、策略约束和完成条件留在技能之外，导致流程依赖长提示词、执行约束弱、恢复状态隐式且容易出错。本文关注的正是如何把可复用的代理能力从“文本式说明”升级为可执行、可约束、可复用的运行时对象，因此具有较强的工程与研究价值。

#### 方法概述和架构

论文提出 Formal Skill 这一运行时原生的技能抽象，用 JSON 元数据与动作模式描述模型可见接口，再用可靠的 Python 执行器负责具体动作落地。其核心还包括由 hooks 统筹的控制逻辑、Formal Skill 路由机制，以及技能局部运行时状态，用来记录阶段、证据、门控条件和恢复上下文。作者将该抽象实现为开源事件驱动运行时 FairyClaw，使技能以可执行、可观测、可组合的方式运行。推理时，模型在单步规划器与受控动作空间中选择操作，hooks 在模型调用与工具调用边界上检查策略、过滤工具可见性并决定是否允许继续或结束任务。整体上，系统把重复的流程文本替换为状态机与可执行策略，从而把“技能”从提示词变成了运行时合同。

#### 实验结果分析

作者在 Harness-Bench 上对 FairyClaw 进行了评测，与 6 种代理运行时/框架进行比较，指标为平均总体分数和 token 消耗。结果显示，FairyClaw 在保持很强竞争力的平均得分的同时，显著减少了 token 使用；文中给出的总量为 7.35M tokens、平均每任务 49.0K tokens，且相较其他 5 个运行时平均低约 48%。在那些更能体现 Formal Skill 作用的任务上，FairyClaw 表现尤为突出。节选文本未给出更细的消融数值，但明确指出 Formal Skill 在技能相关任务行为上带来优势。

<details>
<summary>完整摘要</summary>

大型语言模型（LLM）智能体正越来越多地在真实工作空间中运行，在这些场景里，工具与技能决定了模型推理能否转化为可靠行动。现有技能大多仍然停留在非正式层面：Markdown 技能和指令包通常以冗长的自然语言文档来编码流程，而函数调用、Model Context Protocol（MCP）服务器以及框架工具虽然能把单个动作结构化，但往往把工作流状态、策略约束和完成纪律留在技能本身之外。我们提出 Formal Skill，这是一种运行时原生的抽象：它用 JSON 元数据和动作模式、可靠的 Python 执行器、由 hooks 统筹的控制逻辑、Formal Skill 路由以及技能局部运行时状态来表示可复用能力。通过把可复用流程从重复的提示文本迁移到可执行状态机和 hook 策略中，Formal Skill 为智能体提供了一个节省 token 且可强制执行的控制面。我们在 FairyClaw 中实现了这一抽象；FairyClaw 是一个开源的事件驱动运行时，支持可执行、可观测、可组合的 Formal Skills。在 Harness-Bench 上，FairyClaw 在使用显著更少 token 的同时取得了很有竞争力的平均分数，并且在那些能体现 Formal Skill 作用的任务上表现尤为突出。

</details>

---

### [[20_Research/Papers/大模型/A_novel_YOLO26-MoE_optimized_by_an_LLM_agent_for_insulator_fault_detection_considering_UAV_images|A novel YOLO26-MoE optimized by an LLM agent for insulator fault detection considering UAV images]]

![[assets/2605.19595_figure.png|800]]

- **arXiv**: [2605.19595](https://arxiv.org/abs/2605.19595)
- **PDF**: https://arxiv.org/pdf/2605.19595
- **详细分析**: [[20_Research/Papers/大模型/A_novel_YOLO26-MoE_optimized_by_an_LLM_agent_for_insulator_fault_detection_considering_UAV_images|A novel YOLO26-MoE optimized by an LLM agent for insulator fault detection considering UAV images]]
- **作者**: João Pedro Matos-Carvalho, Laio Oriel Seman, Stefano Frizzo Stefenon, Mohammad Khalaf Mohammad Khreasat, Gabriel Villarrubia González
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 1.8（加权：大模型 1，机器人 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

电力线路绝缘子巡检是保障电网可靠运行的重要环节，但传统人工巡检成本高、效率低，且在高空、远距离和复杂地形下存在安全与覆盖问题。近年来，UAV 结合深度学习视觉检测已成为自动化巡检的有效方案，不过绝缘子故障往往只占很小区域，且缺陷类型多样、背景复杂、成像条件变化大，导致检测仍然困难。这篇论文值得关注之处在于，它同时尝试从检测结构和优化流程两方面入手：一方面增强模型对细粒度缺陷的表征能力，另一方面引入 LLM agent 来辅助超参数搜索与实验决策。

#### 方法概述和架构

论文提出 YOLO26-MoE，在 YOLO26 的高分辨率分支中嵌入稀疏 Mixture-of-Experts（MoE）模块，使不同专家子网络能够针对不同绝缘子外观和故障模式进行条件化特征细化，同时保持单阶段检测器的效率。模型输入为 UAV 拍摄的绝缘子图像，输出为故障目标的类别与位置框；MoE 通过门控机制选择性激活部分专家，从而提升对微小、异质缺陷的识别能力。训练阶段不仅包含常规的检测损失，还加入专家平衡相关的辅助损失，以避免少数专家被过度使用或塌缩。论文还设计了一个工具增强的 LLM agent，用于协调超参数优化、最终训练和评估：该 agent 可以调用外部工具、依据实验结果进行语义检索与记忆更新，并按预设协议迭代调整训练配置。整体流程是由 LLM agent 负责搜索与决策，YOLO26-MoE 负责学习与推理，二者结合以降低人工调参成本并提高最终性能。

#### 实验结果分析

作者在 UAV 采集的绝缘子数据集上对 YOLO26-MoE 进行了评估，并与最新的 YOLO 系列模型进行对比。实验结果显示，模型达到 0.9900 mAP@0.5 和 0.9515 mAP@0.5:0.95，整体优于最新版本的 YOLO 基线。正文目录还显示作者进行了超参数研究、与当前 YOLO 模型的基准对比、随机初始化鲁棒性分析以及配对统计比较，不过节选中未给出更多具体消融数值。

<details>
<summary>完整摘要</summary>

电力线路绝缘子的巡检对于保障电网可靠性、避免因绝缘部件损坏或劣化而引发故障至关重要。近年来，无人机（UAV）结合基于深度学习的视觉系统，已成为实现这一过程自动化的有效方案。然而，由于缺陷区域通常较小、故障模式差异较大、背景复杂以及成像条件变化多端，绝缘子故障检测仍然面临挑战。为应对这些问题，本文提出一种优化后的 YOLO26-MoE：这是一种新颖的目标检测架构，它将稀疏 Mixture-of-Experts（MoE）模块集成到 YOLO26 检测器的高分辨率分支中。该改造使模型能够针对细微且多样的故障模式进行自适应特征细化，同时保留单阶段检测框架的效率。超参数优化、最终训练和评估由一个工具增强的 Large Language Model（LLM）agent 协调完成。所提出的模型取得了 0.9900 的 mAP@0.5 和 0.9515 的 mAP@0.5:0.95，优于最新的 YOLO 版本。结果表明，该模型为基于 UAV 的绝缘子故障检测提供了一种有效且可靠的解决方案。

</details>

---

### [[20_Research/Papers/具身智能/SceneCode_Executable_World_Programs_for_Editable_Indoor_Scenes_with_Articulated_Objects|SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects]]

![[assets/2605.19587_figure.png|800]]

- **arXiv**: [2605.19587](https://arxiv.org/abs/2605.19587)
- **PDF**: https://arxiv.org/pdf/2605.19587
- **详细分析**: [[20_Research/Papers/具身智能/SceneCode_Executable_World_Programs_for_Editable_Indoor_Scenes_with_Articulated_Objects|SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects]]
- **作者**: Puyi Wang, Yuhao Wang, Linjie Li, Zhengyuan Yang, Kevin Qinghong Lin, Yangguang Li, Yu Cheng
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.3（加权：具身智能 0.9，机器人 0.4）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

室内场景合成是具身智能、机器人操控和基于仿真的策略评测的重要基础，但对机器人来说，一个“有用”的场景不仅要长得合理，还要明确物体的结构、可动部件和交互方式。现有方法大多把生成结果表示为静态网格，哪怕包含可动对象，其关节与部件语义也通常依赖预先整理好的资产库，因此难以按需生成新的可交互物体。SceneCode 正是针对这一瓶颈提出：把可物理交互的室内场景生成，重新定义为“可执行的世界程序”生成问题。

#### 方法概述和架构

SceneCode 以自然语言提示为输入，先由房间级的 agentic 骨干网络生成结构化户型布局，并在 planner–designer–critic 循环中逐步产生每个对象的 AssetRequest。每个请求包含物体类别、文本描述、目标尺寸、风格上下文、位姿和支撑关系，并被路由到五种代码生成策略之一：WallArt、StaticFurn、SimpleManip、StructManip、Artic，另有 ThinCover 作为薄覆盖类对象的固定模板。随后，系统基于描述与风格生成参考图像，再把 AssetRequest 提升为 ObjectPlan，用于约束部件、几何原语、局部位姿、材质、曲线等结构化信息，从而降低直接生成 Blender 脚本的歧义。接着，系统为每个部件合成 Blender Python 程序，并通过执行引导的修复与迭代完善机制验证代码正确性。最终生成的程序被编译为仿真就绪资产，并导出为 SDF；同时，持久化的 scene-state registry 将对象请求、可执行程序、渲染几何和仿真资产关联起来，使场景成为可追踪、可局部编辑的世界建模过程。

#### 实验结果分析

论文在 30 个自然语言提示上评估了 SceneCode，覆盖卧室、客厅、餐厅、厨房、浴室和地下室等六类室内场景，并与 SceneSmith、HSM、LayoutVLM 以及资产级基线 SAM 3D Objects 对比。结果显示，SceneCode 在场景级语义一致性上表现最好，尤其在物体数量与属性匹配上更优，同时在可导航性、碰撞和不越界等物理相关指标上也更好。人工评测中，受试者普遍认为 SceneCode 比各基线更符合提示；在资产级评测中，它生成了结构更干净、UV/网格可用性更好的物体，并且可导出具有关节信息的仿真资产。

<details>
<summary>完整摘要</summary>

室内场景合成是具身智能、机器人操控和基于仿真的策略评测的基础，其中一个有用的场景不仅要描述环境外观，还要说明物体是如何构造的。然而，现有流程通常把生成内容表示为静态网格，并且可动结构只继承自经过整理的资产库，这限制了对象级可控性，也使得无法按需生成新的可交互资产。为弥补这一缺口，我们将可物理交互的室内场景合成形式化为程序化世界生成，并提出 SceneCode：一个把自然语言提示编译为可执行、代码驱动的室内世界，而不是一组难以解释的网格的框架。首先，房间级 agentic 骨干会把提示转化为结构化的户型布局，并通过 planner–designer–critic 循环输出每个对象的 AssetRequest。随后，每个请求会被路由到五种代码生成策略之一，并转换为合成的、按部件组织的 Blender Python 程序，这些程序再通过执行引导的修复与完善循环进行验证。生成的程序会被编译为仿真就绪资产，并导出为 SDF 以用于物理仿真。一个持久化的场景状态注册表把对象请求、可执行程序、渲染几何和仿真资产连接起来，使场景组装成为一种可追踪、可局部编辑的世界构建过程。我们从场景级合成、对象级资产质量、人工判断以及下游机器人交互等多个方面评估 SceneCode。结果表明，可执行世界程序能够提升室内场景生成对提示的忠实度，生成更干净的网格结构，并产出可直接加载到仿真器中的关节元数据。

</details>

---

### [[20_Research/Papers/具身智能/ARC-RL_A_Reinforcement_Learning_Playground_Inspired_by_ARC_Raiders|ARC-RL: A Reinforcement Learning Playground Inspired by ARC Raiders]]

![[assets/2605.19503_figure.png|800]]

- **arXiv**: [2605.19503](https://arxiv.org/abs/2605.19503)
- **PDF**: https://arxiv.org/pdf/2605.19503
- **详细分析**: [[20_Research/Papers/具身智能/ARC-RL_A_Reinforcement_Learning_Playground_Inspired_by_ARC_Raiders|ARC-RL: A Reinforcement Learning Playground Inspired by ARC Raiders]]
- **作者**: Carlo Romeo, Andrew D. Bagdanov
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 3.42（加权：具身智能 1.2，强化学习 0.96，世界模型 0.16，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

腿式机器人强化学习已经从简单控制任务发展为依赖多组件奖励函数和物理引擎基准的成熟体系，但这些基准中的机体形态大多来自真实商用硬件，形态分布较窄。相比之下，游戏中的NPC不仅需要完成行走控制，还要满足“看起来像游戏角色”的风格约束，且常常具有现实机器人中不存在的奇特肢体结构。本文关注的正是这种“非真实机器人形态 + 风格化运动”的训练场景，尤其适用于具身智能、机器人仿真和游戏AI交叉方向，因此具有较强的研究价值。

#### 方法概述和架构

论文提出 ARC-RL，一个基于 MuJoCo 的连续控制环境套件，包含四种受 ARC Raiders 启发的机器人形态：Queen、Bastion、Tick 和 Leaper。四个环境共享统一的观测模板、动作定义和仿真节奏，观测由姿态位置、速度、接触力和步态相位时钟四部分组成，动作则是归一化的关节力矩控制。作者为不同形态设计了同一套闭式多项奖励函数，只在少量权重和参数上按形态做调整；奖励由目标速度跟踪、生存奖励、相位锁定的步态符合项、动作正则项以及多种安全/姿态惩罚组成，不使用动作捕捉数据。论文还为每种形态手工构造了中央模式发生器（CPG）示范策略，这些策略既可作为固定专家参考，也可作为离线到在线训练的先验数据来源。

#### 实验结果分析

作者在 ARC-RL 上系统比较了标准在线强化学习算法 SAC、SPEQ、SOPE-EO，以及引入先验数据的方法 SACfD、SPEQ-O2O、SOPE。实验重点考察不同方法在多形态差异和动画风格约束下的适应能力，以及先验数据对学习稳定性和样式保持的作用。节选文本未给出具体数值，但可以看出作者的结论指向：该基准能够有效区分不同算法在复杂形态与风格控制上的优劣，并为研究“先验数据 + 在线优化”的混合训练范式提供了统一测试平台。

<details>
<summary>完整摘要</summary>

腿式运动的强化学习已经发展为一套由多组件奖励函数和物理引擎基准构成的成熟体系，而这些基准中的机体形态几乎都直接来源于真实商用硬件。相比之下，游戏中的非玩家角色（NPC）受到风格约束的限制，这种约束在 sim-to-real 机器人研究中并不存在，而且它们通常会采用现实机器人并不具备对应原型的生物或机械生物形态。为此，我们提出 ARC-RL：一个由四个 MuJoCo 连续控制环境组成的套件，这些环境中的机器人形态取材于 ARC Raiders 的机械生物图鉴，包括 18 自由度的高大型六足机器人 Queen、12 自由度的装甲六足机器人 Bastion、18 自由度的紧凑型六足机器人 Tick，以及 12 自由度的四足机器人 Leaper。四种机器人共享统一的观测模板、动作约定、仿真节奏，以及同一个闭式多组件奖励函数；不同形态之间的差异只体现在少量权重和参数上。该奖励函数融合了速度跟踪项、健康生存奖励、相位锁定的步态符合奖励/惩罚对、动作正则项、三类安全惩罚和一个姿态锚定项；整个奖励设计中完全不使用动作捕捉数据。我们还针对每种形态提供了手工设计的中央模式发生器（CPG）示范器，它们既可以作为固定的专家参考，也可以作为离线到在线训练中的先验数据来源。在这个平台上，我们开展了一项受控实验研究，比较标准在线算法（SAC、SPEQ、SOPE-EO）与加入先验数据的方法（SACfD、SPEQ-O2O、SOPE），并分析这些方法如何应对该平台的形态多样性与动画风格约束。源代码已公开，地址为 https://github.com/CarloRomeo427/ARC_RL.git 。

</details>

---

### [[20_Research/Papers/具身智能/CANINE_Coaching_Visually_Impaired_Users_for_Interactive_Navigation_with_a_Robot_Guide_Dog|CANINE: Coaching Visually Impaired Users for Interactive Navigation with a Robot Guide Dog]]

![[assets/2605.19501_figure.png|800]]

- **arXiv**: [2605.19501](https://arxiv.org/abs/2605.19501)
- **PDF**: https://arxiv.org/pdf/2605.19501
- **详细分析**: [[20_Research/Papers/具身智能/CANINE_Coaching_Visually_Impaired_Users_for_Interactive_Navigation_with_a_Robot_Guide_Dog|CANINE: Coaching Visually Impaired Users for Interactive Navigation with a Robot Guide Dog]]
- **作者**: Cunjun Yu, Zishuo Wang, Anxing Xiao, Linfeng Li, David Hsu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

机器人导盲犬有望显著提升视障用户的独立出行能力，但要真正用好这类系统，用户需要掌握细腻的人机协同动作，例如在门口通行、保持与机器人相对位置、理解机器人提示并及时调整身体姿态。现有通用口头指导往往只能说明“该做什么”，却难以告诉用户“为什么失败、该如何改正”，因此学习效率低、重复试错多，也可能形成不安全的操作习惯。本文关注的是具身交互中的“教学”问题，而不仅是“辅助执行”问题，因此具有很强的现实价值。

#### 方法概述和架构

论文提出 CANINE，一个面向机器人导盲犬交互导航的自动化教练系统，通过个性化、可自适应的语音反馈训练用户。系统将复杂协调任务拆成多个子技能，并采用两层决策结构：高层负责“练什么”，低层负责“怎么练”。在高层，CANINE 通过 knowledge tracing 跟踪学习者在各子技能上的隐含熟练度，优先安排最薄弱的技能进行训练，形成课程式调度。 在低层，系统针对每次实践回合观察用户行为，借助基础模型推断错误的潜在原因，例如空间对位不准或误解了机器人提示，再生成定制化的纠正语音。论文将该过程形式化为两个 POMDP：一个用于子技能选择，一个用于子技能内反馈生成；实现上结合 VLM 提取视频中的行为状态、LLM 生成可执行的口头纠错，从而把“观察—诊断—反馈”串成闭环。

#### 实验结果分析

作者在门框通行这一机器人导盲犬交互任务上做了多阶段评估。首先使用蒙眼健视被试作为代理人群进行控制实验，并与通用口头指导基线比较，结果表明 CANINE 能显著提升学习效率和最终导航表现。随后又进行了两周后的保持性测试，显示技能改进能够持续保留；另外的真实视障用户案例研究也验证了方法有效性，并揭示了面向真实部署还需进一步考虑的设计问题。节选内容未给出具体数值，但整体结论一致指向：分层自适应教练优于泛化式指导。

<details>
<summary>完整摘要</summary>

机器人导盲犬能够为视障用户提供导航辅助，显著提升其独立出行能力，但要高效使用这类系统，用户需要掌握细腻的人机协同，而这类能力很难仅靠通用口头说明学会。为了解决这一问题，我们提出 CANINE，一个通过个性化、自适应语音反馈来训练用户与机器人导盲犬进行交互式导航的自动化教练系统。CANINE 将复杂的协同任务分解为多个子技能，并在两个层面上运作。在高层，它通过 knowledge tracing 跟踪学习者在各子技能上的熟练程度，优先安排最薄弱的部分进行训练，从而决定“练什么”。在低层，它通过观察每一次人类练习回合，利用基础模型推断错误的潜在原因，并自适应地生成有针对性的语音纠正，从而决定“怎么练”。在以蒙眼参与者为代理人群的受控研究中，CANINE 相比通用口头指导显著提升了学习效率和最终导航表现。我们还通过一项保持性研究和一项探索性案例研究进一步验证了 CANINE。保持性研究表明，技能提升在两周后仍然保持；案例研究证实了 CANINE 在训练视障用户方面的有效性，同时也揭示了真实部署时还需考虑的额外设计问题。上述结果与受控研究的发现高度一致。

</details>

---

### [[20_Research/Papers/强化学习/Attention-Guided_Reward_for_Reinforcement_Learning-based_Jailbreak_against_Large_Reasoning_Models|Attention-Guided Reward for Reinforcement Learning-based Jailbreak against Large Reasoning Models]]

![[assets/2605.19485_figure.png|800]]

- **arXiv**: [2605.19485](https://arxiv.org/abs/2605.19485)
- **PDF**: https://arxiv.org/pdf/2605.19485
- **详细分析**: [[20_Research/Papers/强化学习/Attention-Guided_Reward_for_Reinforcement_Learning-based_Jailbreak_against_Large_Reasoning_Models|Attention-Guided Reward for Reinforcement Learning-based Jailbreak against Large Reasoning Models]]
- **作者**: Zheng Lin, Zhenxing Niu, Haoxuan Ji, Yuzhe Huang, Haichang Gao
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Security

#### 研究背景与动机

大型推理模型（LRM）通过显式生成逐步推理过程，在数学、逻辑和复杂决策等任务上表现突出，但这种“可见推理轨迹”也带来了额外的安全暴露面。已有研究表明，LRM 相比普通 LLM 更容易遭受越狱攻击，攻击者可能借此诱导模型输出有害内容。论文指出，现有越狱方法往往没有充分利用 LRM 在“输入提示词”和“推理内容”上的差异化行为，因此仍有提升空间，这使得该工作具有较强的安全研究价值。

#### 方法概述和架构

论文提出 Attention-Guided Reward（AGR）算法，用强化学习来生成针对 LRM 的越狱提示词，并把注意力信号显式纳入奖励函数设计。作者首先分析成功与失败越狱样本中的注意力分布，发现成功案例通常在输入提示词中的有害 token 上分配更低注意力，而在推理内容中的有害 token 上分配更高注意力。基于这一规律，AGR 通过线性判别边界刻画“成功越狱”的注意力模式，并将其转化为可优化的奖励目标，从而引导策略网络朝更有效的攻击方向更新。与此同时，论文把信息型、可信度型、关系型、情绪型等多种劝服策略加入动作空间，作为 RL 中可选择的不同提示词改写方式，以提升策略表达能力。整体流程是：输入有害请求后，策略根据当前反馈选择改写动作，生成新的越狱提示；模型输出及其中间推理再被用于计算注意力相关奖励，进而反向优化策略。

#### 实验结果分析

作者在三个基准上、针对五个开源与闭源 LRM 进行了实验，并与已有越狱方法比较，评估指标主要是 ASR（Attack Success Rate）。结果显示，AGR 在攻击成功率上显著优于现有方法，同时在效率和跨模型迁移性上也更强。论文还进行了鲁棒性、消融和案例分析，表明扩展动作空间与引入注意力奖励都对性能提升有稳定贡献；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

大型推理模型（LRM）通过生成结构化的逐步推理内容，展现了处理复杂问题的出色能力。然而，暴露模型的内部推理过程也会带来额外的安全风险；例如，近期研究表明，LRM 比标准 LLM 更容易受到越狱攻击。本文研究了针对 LRM 的越狱攻击，并揭示攻击成功率（ASR）与 LRM 的注意力模式密切相关。具体而言，成功的越狱往往会让模型在输入提示中的有害 token 上分配更低的注意力，而在推理内容中的这些 token 上分配更高的注意力。受此发现启发，我们提出一种新的、面向 LRM 的越狱方法，利用强化学习（RL）提升攻击效果，并将注意力信号显式纳入奖励函数设计。此外，我们引入多样化的劝服策略来丰富 RL 的动作空间，这一做法能够持续提升 ASR。我们在三个基准上，对五个开源和闭源 LRM 进行了大量实验，结果表明我们的方法能够取得显著更高的 ASR，并且在有效性、效率和迁移性方面均优于现有方法。

</details>

---

### [[20_Research/Papers/强化学习/Sampling-Based_Safe_Reinforcement_Learning|Sampling-Based Safe Reinforcement Learning]]

![[assets/2605.19469_figure.png|800]]

- **arXiv**: [2605.19469](https://arxiv.org/abs/2605.19469)
- **PDF**: https://arxiv.org/pdf/2605.19469
- **详细分析**: [[20_Research/Papers/强化学习/Sampling-Based_Safe_Reinforcement_Learning|Sampling-Based Safe Reinforcement Learning]]
- **作者**: Luca Vignola, Bruce D. Lee, Manish Prajapat, Manuel Wendl, Melanie Zeilinger, Andreas Krause, Yarden As
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型, 大模型
- **相关性评分**: 2.02（加权：具身智能 0.3，大模型 0.1，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

强化学习在机器人控制和具身智能中很有潜力，但现实部署时往往同时面临两个难题：样本效率不足，以及训练过程中难以保证安全。特别是在动力学未知或存在不确定性的连续控制场景里，智能体每一次探索都可能带来代价或事故，因此“边学边安全”一直是核心瓶颈。现有安全强化学习方法通常依赖保守的约束收缩或显式探索奖励，前者容易过于悲观，后者又需要复杂调参。本文关注的是如何在连续状态-动作空间中实现既安全又高效的探索，因此具有较强的理论与机器人落地价值。

#### 方法概述和架构

论文提出 Sampling-Based Safe Reinforcement Learning（SBSRL），是一种基于模型的安全强化学习算法。其核心思路不是直接求解对不确定动力学的最坏情况鲁棒优化，而是从动力学后验中采样出有限个可能模型，并要求策略在这些采样模型上同时满足安全约束，从而近似原本不可解的最坏情况问题。算法在每一轮训练中先学习一个带不确定性估计的动力学模型，再基于多个采样动力学进行轨迹展开和约束收紧，输出一个在所有采样模型上都安全的策略。与此同时，SBSRL 不再使用额外的探索奖励，而是把“获取足够信息”直接写成一个约束，通过限制认知不确定性来触发探索；当贪心策略已经足够有信息量时，策略就保持贪心执行。论文还给出了基于高斯过程的理论版本，以及可扩展到深度集成（deep ensemble）的实现，以便适配高维连续控制任务。

#### 实验结果分析

在理论上，作者证明了在正则条件下，SBSRL 以高概率保证学习全过程的安全性，并给出有限时间的样本复杂度界，说明算法能在有限轮次内恢复接近最优的策略。实验上，方法分别在仿真环境和真实机器人硬件上验证，展示了安全且高效的探索能力；同时，论文还在 SafetyGym 和 RWRL 等连续控制基准上评估了可扩展的深度集成版本。正文节选中提到还包含高斯过程实验、探索实验、真实世界的安全 offline-to-online 设定以及额外仿真实验，但可见文本未给出具体数值。整体结论是：基于采样的约束处理能够兼顾安全保证、探索效率和工程可扩展性。

<details>
<summary>完整摘要</summary>

安全探索仍然是强化学习（RL）中的一个根本性挑战，这限制了 RL 智能体在现实世界中的部署。我们提出 Sampling-Based Safe Reinforcement Learning（SBSRL），这是一种基于模型的 RL 算法，它通过在有限个动力学样本上联合施加约束，在整个学习过程中保持安全。该形式化方法近似了对不确定动力学进行最坏情况优化这一不可解问题，并使得在连续域中获得实用的安全保证成为可能。我们进一步提出一种基于约束认知不确定性的探索策略，从而不再需要显式的探索奖励。在正则条件下，我们推导出学习全过程以高概率满足安全性的保证，以及恢复近似最优策略的有限时间样本复杂度界。实验结果表明，SBSRL 能在仿真和真实机器人硬件上实现安全且高效的探索，并且很容易扩展到实用的 deep ensemble 实现，从而可扩展到高维连续控制问题。

</details>

---

### [[20_Research/Papers/大模型/What_and_When_to_Distill_Selective_Hindsight_Distillation_for_Multi-Turn_Agents|What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents]]

![[assets/2605.19447_figure.png|800]]

- **arXiv**: [2605.19447](https://arxiv.org/abs/2605.19447)
- **PDF**: https://arxiv.org/pdf/2605.19447
- **详细分析**: [[20_Research/Papers/大模型/What_and_When_to_Distill_Selective_Hindsight_Distillation_for_Multi-Turn_Agents|What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents]]
- **作者**: Xiaozhe Li, Tianyi Lyu, Yang Li, Yichuan Ma, Peiji Li, Linyang Li, Qipeng Guo, Dahua Lin, Kai Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.6，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

在多轮交互式智能体中，强化学习常常只能得到稀疏的终局奖励，导致长序列里的信用分配非常困难：一次成功或失败信号必须分摊到很多动作上，而真正起关键作用的步骤往往被淹没。现有方法多依赖轨迹级奖励或代理信号，没有充分利用环境在每一步自然产生的反馈，例如报错信息、页面变化、观察结果或参考轨迹。本文值得关注之处在于，它系统研究了多轮智能体中“用什么反馈、在什么时候蒸馏”这两个关键设计问题，并指出更丰富的上下文并不一定更有效。

#### 方法概述和架构

论文提出 SERL（Selective Environment-Reweighted Learning），是一个面向多轮智能体的选择性环境重加权学习框架。其核心思想是：任务奖励只决定更新方向，而环境反馈只用于调整更新发生的位置和强度，从而把“哪里该学、学多强”与“朝哪个方向优化”分离开。作者首先系统比较了五类环境反馈来源，以及两种插入粒度：step-level 和 anchor-level，用于分析不同反馈如何影响动作级信用分配。随后，SERL 通过一个环境条件化的 teacher 对学生轨迹上的动作 token 进行评分，利用有后验信息与无后验信息之间的概率差，将蒸馏信号转换为有界、符号敏感的优势重加权项，再与 GRPO 的目标结合。为了避免泄露学生在决策时不可见的 privileged information，蒸馏只作用于可执行动作片段，推理时不额外引入训练时的后验信息。

#### 实验结果分析

实验在 ALFWorld 和 WebShop 上进行，并与强基线的 RL 方法和蒸馏方法比较。SERL 分别取得 90.0% 和 80.1% 的成功率，整体优于强 RL 与 distillation baseline。作者的分析还表明，真正有效的不是最“丰富”的反馈，而是与动作相关、具备落地语义、且插入在关键位置的反馈；这种组合在稳定性和性能上都更好。节选中未给出更细的消融数值，但文本明确指出其系统性比较了反馈来源与插入粒度的影响。

<details>
<summary>完整摘要</summary>

强化学习可以利用稀疏任务奖励训练大语言模型智能体，但长时程任务中的信用分配仍然是瓶颈：一个成功或失败信号必须分配到许多动作上。现有方法主要依赖轨迹级奖励或代理信号，没有充分利用环境自然产生的逐步反馈。多轮智能体场景尚未得到充分研究，而这类场景中的反馈可以包括错误信息、页面变化、观察结果或参考轨迹。我们系统性地研究了五种反馈来源和两种插入粒度，并提出 SERL，一种选择性的环境重加权学习框架。SERL 使用任务奖励来决定更新方向，而环境反馈只用于调整更新的位置和幅度，从而把注意力集中在关键动作上。SERL 在 ALFWorld 和 WebShop 上分别达到 90.0% 和 80.1% 的成功率，优于强 RL 和蒸馏基线。分析表明，具备落地性、与动作相关、且处于有意义位置的反馈，始终优于不加区分地使用更长或更丰富的上下文。

</details>

---

### [[20_Research/Papers/强化学习/When_the_Majority_Votes_Wrong,_the_Intervention_Timing_for_Test-Time_Reinforcement_Learning_Hides_in_the_Extinction_Window|When the Majority Votes Wrong, the Intervention Timing for Test-Time Reinforcement Learning Hides in the Extinction Window]]

![[assets/2605.19444_figure.png|800]]

- **arXiv**: [2605.19444](https://arxiv.org/abs/2605.19444)
- **PDF**: https://arxiv.org/pdf/2605.19444
- **详细分析**: [[20_Research/Papers/强化学习/When_the_Majority_Votes_Wrong,_the_Intervention_Timing_for_Test-Time_Reinforcement_Learning_Hides_in_the_Extinction_Window|When the Majority Votes Wrong, the Intervention Timing for Test-Time Reinforcement Learning Hides in the Extinction Window]]
- **作者**: Hongxiang Lin, Zhirui Kuai, Erpeng Xue, Lei Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

Test-time reinforcement learning（TTRL）被用于数学推理基准上的自我改进，但它通常把多数投票得到的伪标签当作训练信号。论文指出，这种做法的“提升”常常只是把本来就能做对的问题进一步做尖，而不是带来真实的新能力；更严重的是，一部分原本正确的问题会在训练中被错误答案污染，且一旦多数投票锁定错误答案，这种损害往往不可逆。作者因此关注一个关键问题：模型在什么时机还能被有效干预，避免正确信号被彻底淹没。

#### 方法概述和架构

论文提出 TTRL-Guard，用于监测并干预 TTRL 训练中的“正确答案消亡窗口”。它先在每个问题上跟踪两个无标签状态量：MR（多数答案占比）和 FR（Flip Rate，伪标签翻转率），并据此判断问题是否进入高风险状态。基于这些状态，TTRL-Guard 包含三个协同模块：FRS（Flip-Rate-Aware Reward Scaling）会随 FR 下降对奖励进行重标定，降低不稳定伪标签带来的更新强度；MPS（Minority-Preserving Sampling）保留少数派正确答案的梯度信号，避免其过早被压制；RCSU（Risk-Conditioned Sparse Updatings）则在问题出现极化并形成错误共识时暂停更新。整体流程是在 TTRL 的多数投票伪标签训练框架内，对每个问题进行在线监控，并只对高风险样本施加干预，而对稳定、已掌握的问题尽量保持原始训练行为。

#### 实验结果分析

作者在三种模型（Llama-3.2-3B-Instruct、Qwen2.5-7B-Instruct、Qwen3-4B）和四个数学推理基准（AIME 2024、AIME 2025、AMC、MATH-500）上评估了该方法，并与 TTRL 及相关基线比较，指标主要为 pass@1。结果显示，TTRL-Guard 在 Qwen2.5-7B-Instruct 和 Qwen3-4B 上取得了最佳平均 pass@1；在 AIME 2025 上，相比 TTRL 的相对提升达到 +54%。论文还报告，TTRL-Guard 将 Llama-3.2-3B-Instruct 上“退化问题”的比例从 60.2% 降到 28.0%，显示其不仅提升整体表现，也显著缓解了训练中的负迁移。

<details>
<summary>完整摘要</summary>

测试时强化学习（TTRL）在数学推理基准上借助多数投票作为伪标签信号，报告了显著的准确率提升。我们认为这些提升被系统性地误读了：其中大部分反映的是对原本就可解问题的“锐化”，而非真正的学习；与此同时，被从正确答案污染成错误答案的问题数量多于真正学会的问题，并且一旦多数投票锁定到错误答案，这种损害就不可逆。逐问题跟踪进一步揭示：低能力问题中的正确答案信号会在短暂阶段内活跃，随后被永久压制，我们将这一现象称为“正确答案消亡窗口”（Correct-Answer Extinction Window），并将 Flip Rate（FR）作为其领先指示器。基于此，我们提出轻量框架 TTRL-Guard，包含三个针对该消亡窗口的机制：Flip-Rate-Aware Reward Scaling（FRS）会随着 FR 下降而降低高风险更新的权重；Minority-Preserving Sampling（MPS）保留少数派正确答案的梯度信号；Risk-Conditioned Sparse Updatings（RCSU）在极化问题上暂停更新。跨三种模型和四个基准的实验表明，TTRL-Guard 在 Qwen2.5-7B-Instruct 和 Qwen3-4B 上取得了最佳平均 pass@1，并在 AIME 2025 上相对 TTRL 提升了 +54%。我们的代码和实现细节可在 https://github.com/linhxkkkk/TTRL-Guard 获取。

</details>

---

### [[20_Research/Papers/强化学习/HalluWorld_A_Controlled_Benchmark_for_Hallucination_via_Reference_World_Models|HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models]]

![[assets/2605.19341_figure.png|800]]

- **arXiv**: [2605.19341](https://arxiv.org/abs/2605.19341)
- **PDF**: https://arxiv.org/pdf/2605.19341
- **详细分析**: [[20_Research/Papers/强化学习/HalluWorld_A_Controlled_Benchmark_for_Hallucination_via_Reference_World_Models|HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models]]
- **作者**: Emmy Liu, Varun Gangal, Michael Yu, Zhuofu Tao, Karan Singh, Sachin Kumar, Steven Y. Feng
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.17（加权：大模型 0.25，强化学习 0.16，世界模型 0.76）
- **关联关键词**: RL

#### 研究背景与动机

大模型的“幻觉”一直是核心失败模式，但现有基准往往在摘要、问答、检索增强生成和智能体交互等场景中各自定义不一，导致很难判断某种缓解方法是否能跨场景生效。已有基准要么依赖人工标注和固定参考文本，容易被记忆化影响；要么建立在难以复现的自然观测场景上，缺乏可控性。本文值得关注之处在于，它尝试用一个统一、可复现的“参考世界”来刻画幻觉，从根源上拆解不同类型的错误。

#### 方法概述和架构

论文提出 HalluWorld，一个基于“参考世界”形式化定义的可扩展幻觉评测框架：当模型输出的可观测陈述与参考世界中的真实状态不一致时，即判定为幻觉。作者将参考世界拆分为世界状态、可观测视图和冲突处理策略三部分，并在此基础上构造合成与半合成环境，使得真实标签可由构造过程自动生成，无需人工标注。HalluWorld 覆盖三类环境：网格世界、Chess 和终端任务，分别对应不同的世界复杂度、可观测性、时间变化和信息冲突情形。框架中还设计了五类探针：感知、记忆、因果、 不确定性和复合推理，用来分别测试直接观察、跨时序状态跟踪、前向模拟、拒答能力以及多源信息整合。对于网格世界，作者进一步提供了多种序列化器（Symbolic、Grid、Memory）和关卡编辑/轨迹记录工具，以便独立操控同一世界状态的呈现方式并扩展评测场景。

#### 实验结果分析

作者在网格世界、Chess 和终端任务上评测了多种前沿闭源模型与开源模型，比较维度包括不同探针类型、不同观测条件和不同推理深度；可见文本未给出具体数值。总体结果显示，前沿模型对“直接可见信息”的感知型幻觉已经接近解决，但多步状态跟踪与因果前向模拟仍然困难。仅增加“思考”长度并不能普遍修复这些错误，尤其在终端任务中，模型在何时应当拒答也表现不佳。整体来看，不同探针和不同领域上的失败模式并不一致，说明幻觉并非单一能力缺陷，而是由多种不同机制导致。

<details>
<summary>完整摘要</summary>

幻觉仍然是大语言模型的一个核心失败模式，但现有基准在摘要、问答、检索增强生成和智能体交互等任务中对它的操作化方式并不一致。这种碎片化使得我们不清楚：在某一场景中有效的缓解方法，是否真的能在其他场景中降低幻觉。现有基准要么需要人工标注和固定参考，而这些参考最终可能会被记忆；要么依赖自然环境中的观测，而这些环境通常难以复现或系统性测试。为了研究其根本原因，我们提出 HalluWorld：一个以显式“参考世界”形式化为基础的可扩展基准。在这个定义下，如果模型生成了一个可观测陈述，而该陈述相对于参考世界为假，那么就称其发生了幻觉。在这一视角下，我们构造了合成和半合成环境，其中参考世界被完整指定，模型的视图被严格控制，幻觉标签则可通过构造自动生成。HalluWorld 覆盖网格世界、Chess 和真实感终端任务，使我们能够在受控条件下变化世界复杂度、可观测性、时间变化以及信息冲突策略，并将幻觉拆解为更细粒度的错误类别。我们在这些设置下评测了前沿模型和开源权重模型，发现跨领域存在一致模式：前沿模型对直接观测信息的感知型幻觉几乎已经解决，但多步状态跟踪和因果前向模拟仍然困难，而且通常不能通过增加思考长度来彻底解决。在终端设置中，模型还难以判断何时应该拒答。不同探针类型和不同领域上不均衡的失败画像表明，幻觉来自不同的失败机制，而非单一能力缺陷。我们的结果表明，基于受控参考世界的评测，是衡量并减少现代语言模型幻觉的一条可扩展、可复现的路径。

</details>

---

### [[20_Research/Papers/大模型/RE-VLM_Event-Augmented_Vision-Language_Model_for_Scene_Understanding|RE-VLM: Event-Augmented Vision-Language Model for Scene Understanding]]

![[assets/2605.19329_figure.png|800]]

- **arXiv**: [2605.19329](https://arxiv.org/abs/2605.19329)
- **PDF**: https://arxiv.org/pdf/2605.19329
- **详细分析**: [[20_Research/Papers/大模型/RE-VLM_Event-Augmented_Vision-Language_Model_for_Scene_Understanding|RE-VLM: Event-Augmented Vision-Language Model for Scene Understanding]]
- **作者**: Hanqing Liu, Mingjie Liu, Luoping Cui, Endian Lin, Donghong Jiang, Chuang Zhu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

现有视觉语言模型主要依赖 RGB 图像，在低照度、高动态范围、快速运动等复杂场景下容易因成像退化而误判，导致图像描述和 VQA 的可靠性下降。事件相机能够以微秒级时延记录像素亮度变化，具有高时间分辨率和宽动态范围，在传统帧图像失真时仍能保留运动与边缘信息，因此与 RGB 具有天然互补性。本文关注如何把事件流引入大模型，使其在正常场景和恶劣成像条件下都能稳定进行场景理解，这一问题对自动驾驶、机器人感知和低照度视觉问答都很有价值。

#### 方法概述和架构

论文提出 RE-VLM，这是一个双流 RGB-Event 视觉语言模型，分别用并行的 RGB 编码器和事件编码器提取静态外观与动态变化特征，再通过面向大语言模型的融合模块对齐到语言空间。为缓解 RGB-Event-Text 标注稀缺，作者设计了图驱动的数据生成流程：先把同步的 RGB 与事件流分别转换为可验证的场景图，再进行降质感知的图融合，最后自动合成 caption 与 QA。事件分支会先把一个时间窗内的事件重建成类似视频的灰度帧序列，再生成事件图；RGB 分支则围绕同步关键帧构建 RGB 图，并显式标注低照、过曝、运动模糊等退化信息。融合阶段根据退化状态进行字段级仲裁：运动、时序和拓扑关系优先依赖事件图，颜色、光源和可读文本优先依赖 RGB 图；若 RGB 严重退化，则不覆盖事件侧结论。训练上采用渐进式策略逐步对齐异构视觉特征与语言，推理时既支持双模态输入，也支持单模态退化输入，从而提升鲁棒性。

#### 实验结果分析

作者构建了两个新数据集 PEOD-Chat 和 RGBE-Chat，并在 captioning 与 VQA 基准上与 RGB-only、event-only 及其他强基线比较。结果表明，RE-VLM 在参数量相近的情况下整体优于现有方法，尤其是在低照、HDR 过渡和快速运动等困难条件下提升更明显。正文节选中的人工审核实验还显示，作者的数据生成流程比 RGB-only 生成基线更可靠，PEOD 样本的 QA 纠错率从 54.2% 降至 18.1%。消融部分还分析了单分支推理和 STAM 模块等设计，说明双流融合与渐进训练对性能提升是关键。

<details>
<summary>完整摘要</summary>

传统视觉语言模型在解释恶劣条件下拍摄的场景时表现不佳，例如低照度、高动态范围或快速运动，因为标准 RGB 图像在这些环境中会退化。事件相机提供了一种互补模态：它以异步方式记录每个像素的亮度变化，具有高时间分辨率和宽动态范围，能够在帧图像失效时保留运动线索。我们提出 RE-VLM，这是首个同时利用 RGB 图像和事件流的双流视觉语言模型，旨在在正常和复杂条件下实现稳健的场景理解。RE-VLM 采用并行的 RGB 与事件编码器，并结合渐进式训练策略，将异构视觉特征与语言对齐。为解决 RGB-Event-Text 监督数据稀缺的问题，我们进一步提出一种图驱动流程，将同步的 RGB-Event 流转换为可验证的场景图，并据此合成描述文本和问答（QA）对。为了开发和评估 RE-VLM，我们构建了两个数据集：PEOD-Chat，面向光照受挑战的场景；RGBE-Chat，覆盖多样化场景。在图像描述和 VQA 基准上，RE-VLM 在参数量相当的情况下，持续优于最先进的 RGB-only 和 event-only 模型，并且在困难条件下提升尤为显著。结果表明，事件增强的视觉语言模型能够在广泛的真实环境中实现更稳健的视觉语言理解。代码和数据集已开源于 https://github.com/bupt-ai-cz/RE-VLM。

</details>

---

### [[20_Research/Papers/具身智能/ContextFlow_Hierarchical_Task-State_Alignment_for_Long-Horizon_Embodied_Agents|ContextFlow: Hierarchical Task-State Alignment for Long-Horizon Embodied Agents]]

![[assets/2605.19314_figure.png|800]]

- **arXiv**: [2605.19314](https://arxiv.org/abs/2605.19314)
- **PDF**: https://arxiv.org/pdf/2605.19314
- **详细分析**: [[20_Research/Papers/具身智能/ContextFlow_Hierarchical_Task-State_Alignment_for_Long-Horizon_Embodied_Agents|ContextFlow: Hierarchical Task-State Alignment for Long-Horizon Embodied Agents]]
- **作者**: Shuhan Guo, Kun Zhang, Haifei Liu, Xingyu Gao, Yongqi Zhang, Yaqing Wang, Quanming Yao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.4，机器人 0.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

长程具身智能任务通常需要将导航、搜索、接近和操作等能力交给不同的专门执行器完成，应用场景包括家庭环境中的物体寻找、路线跟随和移动操作。随着这些局部执行器越来越强，系统的真正瓶颈不再只是单个技能能否完成，而是规划、监控、记忆与执行之间能否持续保持一致的“任务状态”。作者指出，现有系统容易出现阶段误推进、阶段锁定、执行器与上下文不匹配，以及不必要的重规划，这些问题会直接破坏长程任务的稳定性。因此，这篇工作值得关注之处在于：它把注意力从“局部控制是否正确”转向“任务前沿是否对齐”，提出了一个更适合长程具身代理的任务级一致性问题。

#### 方法概述和架构

论文提出 ContextFlow，一个面向长程具身代理的可解释任务状态对齐框架。其核心做法是把每个阶段表示为显式的“阶段契约”，其中包含阶段目标、交接条件、预期证据、兼容执行器类型和阶段状态，用来约束规划器对当前任务前沿的判断。运行时，系统将监测到的观测、执行器状态、进度线索和相关记忆整合为“证据包”，再由规划器基于当前契约和证据包做范围受限的更新，更新类型包括 continue、refine、transfer、promote 和 repair。ContextFlow 还引入了可见对齐面板，把当前阶段、期望证据、实时证据、记忆上下文、执行器状态和计划差异统一展示出来，便于调试与解释。整体流程是：用户指令先被分解为阶段契约，专门执行器负责局部闭环控制，异步监控器持续汇聚运行时信号，最后由规划器根据证据决定是继续当前阶段、细化证据要求、切换执行器、推进任务前沿，还是仅修复未被证据支持的后缀。

#### 实验结果分析

作者在长程具身任务上进行了实验与演示轨迹分析，重点验证了任务状态失配的诊断与缓解能力。正文节选中提到实验覆盖了原生 R2R-CE 评测以及机制敏感的压力测试，并与多个对比系统进行比较，但可见文本未给出具体数值。结果显示，基于证据的范围受限更新能够更好地识别和处理常见的任务状态失败模式，尤其是在阶段锁定、错误交接和局部修复方面表现更稳健。论文还展示了可解释的面板和计划差异，有助于在长程执行中定位问题来源并减少过度重规划。

<details>
<summary>完整摘要</summary>

长程具身代理越来越多地将导航、搜索、接近和操作委托给专门执行器。随着这些执行器不断增强，主要瓶颈从局部技能执行转移到了在规划、监控、记忆和执行之间维持一致的任务前沿。我们研究任务状态失配，这是一种任务级一致性失败：规划器的当前阶段、运行时证据、记忆中的上下文以及被委托的执行器，已经不能共同支持同一个下一步决策。这种失败会导致缺乏支撑的交接、阶段锁定、执行器与上下文不匹配，以及不必要的重规划。我们提出 ContextFlow，一个可检查的对齐框架，它将阶段表示为显式契约，把运行时观测转化为证据包，并应用范围受限的更新，包括 continue、refine、transfer、promote 和 repair。ContextFlow 让专门执行器继续承担局部闭环控制，同时使任务前沿对齐过程显式化且可审计。针对长程具身任务的实验和演示轨迹表明，基于证据的范围受限更新能够诊断并缓解反复出现的任务状态失败。

</details>

---

### [[20_Research/Papers/具身智能/DEFLECT_Delay-Robust_Execution_via_Flow-matching_Likelihood-Estimated_Counterfactual_Tuning_for_VLA_Policies|DEFLECT: Delay-Robust Execution via Flow-matching Likelihood-Estimated Counterfactual Tuning for VLA Policies]]

![[assets/2605.19294_figure.png|800]]

- **arXiv**: [2605.19294](https://arxiv.org/abs/2605.19294)
- **PDF**: https://arxiv.org/pdf/2605.19294
- **详细分析**: [[20_Research/Papers/具身智能/DEFLECT_Delay-Robust_Execution_via_Flow-matching_Likelihood-Estimated_Counterfactual_Tuning_for_VLA_Policies|DEFLECT: Delay-Robust Execution via Flow-matching Likelihood-Estimated Counterfactual Tuning for VLA Policies]]
- **作者**: Yixiang Zhu, Yonghao Chen, Rui Meng, Jingyu Guo, Jiaxiang Zou, Zijie Yang, Taowen Wang, Xinyu Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

视觉-语言-动作（VLA）策略在机器人中常采用异步推理：机器人一边执行上一段动作块，一边等待模型计算下一段动作。然而，在有明显推理延迟时，当前执行的动作块往往基于“过时”的观测，导致预测与执行状态严重错位，尤其在动态环境中会快速累积成轨迹错误。论文指出，这类延迟问题不是简单的运行时鲁棒性问题，而是一个缺少合适偏好监督的训练问题，因此值得专门研究。

#### 方法概述和架构

论文提出 DEFLECT（Delay-Robust Execution via Flow-matching Likelihood-Estimated Counterfactual Tuning），用于对已有异步 VLA 策略做完全离线的后训练增强。其核心做法是：从离线轨迹中构造“新鲜/陈旧”两种反事实条件上下文，并用冻结的参考策略在相同采样噪声下生成一对候选动作块，分别作为偏好与非偏好样本。随后，DEFLECT 在部署时对应的混合条件上下文下，对这两个候选动作块进行打分，并借助 flow-matching 的隐式似然比近似来形成 DPO 风格的偏好优化目标。训练时还加入 SFT 锚点，避免策略退化；推理阶段不增加额外开销，仍沿用原有异步执行流程。

#### 实验结果分析

实验在 Kinetix 和 LIBERO 仿真任务，以及两个真实机器人任务上验证了方法效果。结果显示，DEFLECT 在高延迟区间（5–7 个控制步）相较基线取得了明显提升：在 Kinetix 上成功率提升 +6.4，在迁移到大规模真实 VLA 且延迟最长时提升 +4.6，并且在双臂传送带抓放与反应式 whack-a-mole 任务上也表现稳定。正文节选还提到，naive async 在 Kinetix 上会随延迟增大从 89% 迅速崩溃到不足 1%，而 DEFLECT 能显著扩展可用延迟范围；更多消融、泛化和机制分析在节选中被列出，但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

视觉-语言-动作（VLA）策略通常以异步方式部署：机器人在执行先前预测的一段动作块时，模型同时计算下一段动作。这会造成预测与执行之间的错位：该动作块是基于推理开始前采集的观测条件生成的，但真正执行时物理状态已经在若干控制步内继续变化；在 Kinetix 上，当推理周期覆盖最多 7 个控制步时，朴素的异步滚动执行会从 89% 的成功率骤降到不足 1%。为此，我们提出 DEFLECT，这是一种完全离线的后训练精炼方法，可作为现有异步 VLA 系统的近似即插即用升级：它将“延迟”本身转化为一种无需标签的偏好信号，通过冻结的参考策略构造反事实的“新鲜/陈旧”动作对，并在部署时所对应的条件下，借助隐式的 flow-matching 似然比近似进行评分，全程不需要人工标签、奖励模型或在线试运行。DEFLECT 显著扩展了异步 VLA 控制可用的延迟范围：在高延迟区间（5–7 个控制步）成功率提升 +6.4；迁移到真实规模 VLA 且在最长延迟下提升 +4.6；并且在两个真实机器人任务上也取得了一致改进，分别是双臂传送带抓放任务和反应式 whack-a-mole 任务。

</details>

---

### [[20_Research/Papers/世界模型/PhyWorld_Physics-Faithful_World_Model_for_Video_Generation|PhyWorld: Physics-Faithful World Model for Video Generation]]

![[assets/2605.19242_figure.png|800]]

- **arXiv**: [2605.19242](https://arxiv.org/abs/2605.19242)
- **PDF**: https://arxiv.org/pdf/2605.19242
- **详细分析**: [[20_Research/Papers/世界模型/PhyWorld_Physics-Faithful_World_Model_for_Video_Generation|PhyWorld: Physics-Faithful World Model for Video Generation]]
- **作者**: Pu Zhao, Juyi Lin, Timothy Rupprecht, Arash Akbari, Chence Yang, Rahul Chowdhury, Elaheh Motamedi, Arman Akbari, Yumei He, Chen Wang, Geng Yuan, Weiwei Chen...
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

世界模型希望在真实部署前，为 Physical AI 提供安全、可扩展的仿真环境，而大规模视频生成模型因具备生成多样且逼真未来画面的能力，被视为构建这类仿真器的有前景基础。但现有视频生成模型要真正充当世界模拟器，必须生成“物理上可信”的视频延续，即在延续中保持输入所隐含的物理状态，并符合基本物理规律。当前瓶颈主要在于：一方面帧间时序一致性不足，容易出现背景漂移、运动速度不稳定等问题；另一方面缺少显式的物理约束或监督，导致生成结果可能违背碰撞、重力、反弹等规律。这篇工作值得关注之处在于，它把视频生成与物理可信性评估、强化学习式对齐结合起来，尝试把通用视频模型推向更实用的世界模拟器。

#### 方法概述和架构

论文提出 PhyWorld，一个面向视频生成的物理可信世界模型，采用两阶段后训练策略。第一阶段通过 flow matching 微调，把输入视频作为视频到视频续写的条件信号，在保持颜色、物体外观和运动轨迹稳定的同时，提升时序连续性与延续质量。具体做法是将条件视频、零填充帧和二值 mask 共同编码为条件潜变量，再与噪声潜变量拼接后输入 Wan DiT 进行去噪生成。第二阶段使用基于物理偏好对的 DPO，对模型进行物理规律对齐：先构造带有物理偏好标注的数据，再让模型在更符合物理常识的输出上获得偏好优化。与此同时，作者还构建了一个物理可信性基准，按不同物理定律进行细粒度评分，并使用开源的视频语言判别器对生成结果进行评估，为后续 DPO 提供反馈信号。

#### 实验结果分析

实验在标准视频质量基准 VBench 以及作者自建的物理可信性基准上进行，并与当前强基线比较。结果显示，PhyWorld 的视频一致性平均分达到 0.769，高于或优于现有 SOTA 基线的 0.756 及以下；在物理可信性基准上，平均分达到 3.09，也高于最强基线的 2.99。整体结论是，先做延续一致性增强、再做物理偏好对齐，能同时改善视频质量与物理合理性。节选正文还提到其物理基准包含 250 个 prompt 和按物理定律划分的评分体系；若需要更细的消融或泛化结论，可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

世界模拟器可以为 Physical AI 系统在真实部署前提供安全且可扩展的训练环境。大规模视频生成模型正在成为这类模拟器的一个有前景基础，因为它们能够生成多样且逼真的视觉未来。然而，要将其用作世界模拟器，就需要物理上可信的视频延续，即生成视频能够保留条件输入所隐含的物理状态，并以符合基本物理原理的方式演化。我们提出 PhyWorld，一个面向视频生成的世界模型，旨在通过两阶段后训练生成时间上连贯且物理上可信的场景延续。第一阶段，我们通过 flow matching 微调提升视频到视频的延续能力，鼓励跨帧保持稳定的视觉属性和连贯的运动动力学。第二阶段，我们在物理偏好对上使用 Direct Preference Optimization（DPO），使生成动态与物理原理对齐，引导模型输出更高物理合理性的结果。为了评估 PhyWorld，我们同时使用标准视频质量基准和一个带有按物理定律评分的专门物理可信性基准。实验表明，PhyWorld 提升了视频一致性，在 VBench 上平均得分为 0.769，而最先进基线为 0.756 或更低。PhyWorld 还提升了物理合理性，在我们的物理可信性基准上平均得分达到 3.09，而最强基线为 2.99。这些结果表明，通过对大规模视频生成模型进行包含续写与物理偏好信号的后训练，可以使其更适合作为 Physical AI 的世界模拟器。

</details>

---

### [[20_Research/Papers/大模型/SimGym_A_Framework_for_A_B_Test_Simulation_in_E-Commerce_with_Traffic-Grounded_VLM_Agents|SimGym: A Framework for A/B Test Simulation in E-Commerce with Traffic-Grounded VLM Agents]]

![[assets/2605.19219_figure.png|800]]

- **arXiv**: [2605.19219](https://arxiv.org/abs/2605.19219)
- **PDF**: https://arxiv.org/pdf/2605.19219
- **详细分析**: [[20_Research/Papers/大模型/SimGym_A_Framework_for_A_B_Test_Simulation_in_E-Commerce_with_Traffic-Grounded_VLM_Agents|SimGym: A Framework for A/B Test Simulation in E-Commerce with Traffic-Grounded VLM Agents]]
- **作者**: Han Li, Vibhor Malik, Zahra Zanjani Foumani, Alberto Castelo, Shuang Xie, Ailin Fan, Keat Yang Koay, Yuanzheng Zhu, Meysam Feghhi, Ronie Uliana, Zhaoyu Zhang, Angelo Ocana Martins...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

电商网站的界面改版通常依赖 A/B 测试来判断是否会影响加购和转化，但真实流量被分流后，实验往往需要数周才能达到统计显著，而且一旦新方案表现较差，还会直接伤害用户体验。论文关注的核心问题是：能否在不接触真实买家的情况下，先用合成买家预演界面改动，从而更快、更低风险地筛选候选方案。这个方向之所以值得关注，是因为大模型/VLM 代理已经具备一定的网页操作能力，但此前缺少一个能在真实电商场景中端到端预测 A/B 结果的统一框架。

#### 方法概述和架构

论文提出 SimGym，一个用于电商 A/B 测试模拟的框架，核心是把“真实流量分布”“活浏览器交互”和“结果验证”串成闭环。第一部分是流量驱动的人设生成管线：从商家的生产级点击流中聚类会话、提取商品偏好与购买意图，并汇总买家级行为信号，构造由“买家类型 + 买家意图”组成的合成 persona。第二部分是基于 VLM 的 live-browser 代理：每一步同时读取页面截图和 DOM/accessibility tree，用观察-规划-执行循环在真实网页上完成浏览，并通过 episodic memory 保持会话连续性。第三部分是评估协议：先筛选控制组与处理组对应的真实店铺页面，剔除会混淆 A2C 信号的促销、价格、选品等因素，再比较模拟代理与真实买家的加购变化方向和相关性。整个框架是模块化的，persona 生成、代理架构和评估模块都可替换或扩展。

#### 实验结果分析

作者在某大型电商平台的真实 UI 主题改版 A/B 测试上验证了 SimGym，覆盖多个店铺和商品类别。实验表明，SimGym 代理与真实买家的结果变化具有较强一致性，其中加购变化的方向一致率达到 77%。节选中未给出完整的基线对比与全部消融数值，但论文声称该方法可将实验周期从数周缩短到一小时以内，并且在 persona 生成和记忆管理等模块上做了消融分析。

<details>
<summary>完整摘要</summary>

A/B 测试仍然是评估电商店铺界面修改的黄金标准，但它会分流真实流量、通常需要数周才能达到统计显著性，并且存在损害用户体验的风险。我们提出 SimGym，一个使用在真实浏览器中运行的 VLM 代理来模拟电商店铺 A/B 测试的框架。该框架包含三个关键组成部分：(a) 一个流量驱动的人设生成流程，它从生产级点击流数据中为每个店铺提取买家原型和购买意图；(b) 一个 live-browser 代理架构，它将对视觉信息与浏览器结构化观测的多模态感知、情景记忆以及安全约束结合起来，以便在控制组与处理组店铺之间执行连贯的购物会话；(c) 一个评估协议，它将模拟得到的结果变化与真实买家行为中观察到的变化进行比较。我们在某大型电商平台上针对视觉驱动的 UI 主题改版 A/B 测试验证了 SimGym，覆盖了不同店铺和商品类别。实证结果表明，SimGym 代理与观察到的结果变化具有较强一致性，在真实买家流量中观察到的不同界面变体之间的加购变化上，实现了 77% 的方向一致率。该方法将实验周期从数周缩短到一小时以内，在不让真实买家暴露于候选变体的前提下，实现了快速实验。

</details>

---

### [[20_Research/Papers/具身智能/COBALT_Crowdsourcing_Robot_Learning_via_Cloud-Based_Teleoperation_with_Smartphones|COBALT: Crowdsourcing Robot Learning via Cloud-Based Teleoperation with Smartphones]]

![[assets/2605.19138_figure.png|800]]

- **arXiv**: [2605.19138](https://arxiv.org/abs/2605.19138)
- **PDF**: https://arxiv.org/pdf/2605.19138
- **详细分析**: [[20_Research/Papers/具身智能/COBALT_Crowdsourcing_Robot_Learning_via_Cloud-Based_Teleoperation_with_Smartphones|COBALT: Crowdsourcing Robot Learning via Cloud-Based Teleoperation with Smartphones]]
- **作者**: Ayush Agarwal, Ansh Gandhi, Jeremy A. Collins, Omar Rayyan, Aryan Sarswat, Ranjani Koushik, Masoud Moghani, Ajay Mandlekar, Animesh Garg
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

机器人操作中的模仿学习高度依赖大规模、高质量的人类示范数据，但现实中采集这类数据成本高、效率低，已经成为扩展具身智能能力的关键瓶颈。传统遥操作往往受限于专用硬件、单机单人模式、低可达性和较差的人机交互体验，难以支撑全球化、众包式的数据采集。本文关注的是如何用更低门槛的设备和云端基础设施，把分布式人类操作员高效接入机器人数据收集流程，因此具有很强的工程与研究价值。

#### 方法概述和架构

论文提出 COBALT，一个基于云端的机器人遥操作平台，支持在仿真和真实环境中进行大规模众包数据采集。系统由三部分组成：Client Session Service 负责通过 WebSocket 接收用户设备输入，Teleoperation Service 在向量化仿真环境中并行驱动多个任务实例，Media Service 则通过 WebRTC 提供低延迟视频反馈。系统使用 Redis 作为中心化通信与缓存层，将用户控制命令、渲染帧和会话状态在各服务间异步解耦，从而支持用户随时接入、退出以及单 GPU 上的多用户并发。输入端兼容单/双智能手机、VR 头显、3D 鼠标和键盘，且对双臂任务提供双手机与 VR 控制方式。为了保证数据质量，COBALT 设计了训练课程，先通过校准与评估任务完成用户上手，再结合实时性能指标自动过滤低质量示范，并将示范数据与状态、动作、时间戳等信息一并记录用于离线训练。最后，作者使用收集到的数据训练 imitation learning / behavior cloning 策略，以验证平台和数据集的有效性。

#### 实验结果分析

实验显示，COBALT 能在单 GPU 上支持多个用户并发遥操作，在 20 Hz 交互频率下保持低延迟；文本明确给出可达到每 GPU 最多 8 个并发用户、端到端延迟低于 100 ms，并能在 8 张 GPU 上稳定支撑 256 个模拟客户端。用户研究表明，基于手机的遥操作在表现上与专用硬件相当甚至更优，同时更快、更符合人体工学。作者还在九个国家、五天内用智能手机众包收集了 7500+ 条示范、50+ 小时数据，并用 state-of-the-art imitation learning 算法进行验证；具体数值效果在节选中未完整给出，但结论是数据质量足以支持后续模仿学习。

<details>
<summary>完整摘要</summary>

大规模、高质量示范数据的匮乏，仍然是机器人操作模仿学习规模化的主要瓶颈。我们提出 COBALT，这是一套旨在在仿真和现实世界中都能大规模普及机器人学习的遥操作平台。借助向量化环境，我们构建了可扩展、负载均衡的基础设施，支持多个用户在单个 GPU 上并发遥操作，从而显著降低遥操作成本。操作员可以使用随处可得的设备接入系统，包括单部或双部智能手机、VR 头显、3D 鼠标以及键盘，几乎可从全球任何地点参与。内存数据缓存和高效视频流传输使控制与渲染保持同步，在每个 GPU 最多 8 个并发用户的条件下，系统可维持数十个并发用户以 20 Hz 运行，并将端到端延迟控制在 100 ms 以下。我们还展示了系统的稳定扩展能力：在 8 张 GPU 上可稳定支持 256 个仿真客户端，说明该系统既能在单台服务器内部扩展，也能跨硬件扩展。我们进行了全面的用户研究，表明基于手机的遥操作表现可与专用硬件相当甚至更好，从而实现更快、更符合人体工学的数据采集。为保证数据质量，COBALT 会记录一组实时指标，用于自动过滤低质量示范。我们还证明，结构化的用户训练课程能显著提升数据采集质量。在用户研究结果的指导下，我们利用智能手机在五天内、跨九个国家，众包收集了一个大规模高质量试点数据集，包含 7500+ 条示范（50+ 小时）。最后，我们通过训练最先进的模仿学习算法验证了该数据集的质量。更多信息见 https://cobalt-teleop.github.io/ 。

</details>

---

### [[20_Research/Papers/大模型/POLAR-Bench_A_Diagnostic_Benchmark_for_Privacy-Utility_Trade-offs_in_LLM_Agents|POLAR-Bench: A Diagnostic Benchmark for Privacy-Utility Trade-offs in LLM Agents]]

![[assets/2605.19127_figure.jpg|800]]

- **arXiv**: [2605.19127](https://arxiv.org/abs/2605.19127)
- **PDF**: https://arxiv.org/pdf/2605.19127
- **详细分析**: [[20_Research/Papers/大模型/POLAR-Bench_A_Diagnostic_Benchmark_for_Privacy-Utility_Trade-offs_in_LLM_Agents|POLAR-Bench: A Diagnostic Benchmark for Privacy-Utility Trade-offs in LLM Agents]]
- **作者**: Qiaoyuan Zheng, Yiqu Yang, Qi Gao, Imanol Schlag
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

随着大模型代理逐渐接入用户的私人文档，并代替用户与第三方系统交互，隐私保护与任务完成之间的冲突变得越来越突出。现实场景中，用户会明确哪些信息可以共享、哪些必须保密，但代理还要在第三方系统带有“诱导性”甚至对抗性的提问下，稳定遵守这些意图。现有隐私评测往往只考察单一政策类型或单一攻击方式，缺少对“隐私策略维度”和“攻击策略强度”两个因素的联合诊断，因此难以定位模型到底在何处失去意图遵循能力。这篇工作值得关注之处在于，它把LLM agent 的隐私-可用性权衡做成了可诊断的基准测试，而不仅仅是一个单一分数。

#### 方法概述和架构

作者提出 POLAR-Bench（Policy-aware adversarial Benchmark），构造一个“双模型对话”的评测设定：一个带有隐私策略和任务指令的可信模型，和一个会主动探测任务相关信息与受保护属性的第三方对抗模型进行交互。基准中的每个样本都将源文档中的属性先做类型化标注，分为任务相关、受保护和其他噪声三类，再渲染成自然语言，从而保证隐私与可用性都能通过确定性的集合匹配来评估。POLAR-Bench 在隐私策略轴上设计了5个难度层级，包括字段级显式约束、语义级约束、条件披露、部分/抽象披露以及带冲突目标的复杂策略；在攻击轴上也设计了5类策略，包括单轮直接询问、是/否逐步缩小范围、角色混淆、提示注入和多轮渐进式套话。评测时，系统统计对话中泄露了哪些属性，并分别计算 Privacy 和 Utility，再组合成 Overall Score；同时还生成一个 5×5 的诊断表面，用于观察模型在不同政策与攻击组合下的脆弱点。

#### 实验结果分析

作者在10个领域、7,852个样本上进行实验，并用确定性的集合成员判定来打分，避免依赖主观LLM裁判。结果显示，当前前沿模型整体能很好地隐藏受保护属性，保密率超过99%，同时还能保持较高可用性；但1B到30B参数量级的小型开源模型表现明显更差，这类模型恰恰是用户最常在本地或私有推理环境中作为可信代理部署的规模，最弱的模型会泄露超过一半的受保护信息。论文还指出，该基准能够把模型在不同策略与攻击条件下的失效位置具体定位出来，不过节选中未给出更细的消融或各基线数值，因此可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

随着大模型代理越来越多地能够访问用户的私人数据，并在与第三方系统交互时代表用户行事，隐私与可用性之间的权衡问题也日益突出。用户会定义哪些内容可以共享、哪些内容不应共享，而代理即使面对带有对抗性的第三方系统，也必须稳健地遵循这一意图。我们提出 POLAR-Bench（Policy-aware adversarial Benchmark），其中一个带有隐私策略和任务的可信模型，会与一个第三方模型对话；后者会以对抗方式探测任务相关属性和受保护属性。我们在10个领域和7,852个样本上，通过确定性的集合成员判定来衡量隐私与可用性，并在隐私策略维度与攻击策略维度这两个正交轴上变化，针对每个模型生成一个5×5的诊断表面。实验结果显示出鲜明分化：当前前沿模型能够隐藏超过99%的受保护属性，而1B到30B范围内的小型开源模型——也就是用户最常在本地或通过私有推理运行、作为自身可信代理的那类模型——表现明显更差，最弱的模型会泄露超过一半的受保护属性。因此，POLAR-Bench 能够定位每个模型在意图遵循上的失效位置，为真正重要的隐私对齐问题提供切入口。

</details>

---

### [[20_Research/Papers/机器人/Neural_Operators_for_Design-Space_Surrogate_Modeling_of_Tendon-Actuated_Continuum_Robots|Neural Operators for Design-Space Surrogate Modeling of Tendon-Actuated Continuum Robots]]

![[assets/2605.19104_figure.png|800]]

- **arXiv**: [2605.19104](https://arxiv.org/abs/2605.19104)
- **PDF**: https://arxiv.org/pdf/2605.19104
- **详细分析**: [[20_Research/Papers/机器人/Neural_Operators_for_Design-Space_Surrogate_Modeling_of_Tendon-Actuated_Continuum_Robots|Neural Operators for Design-Space Surrogate Modeling of Tendon-Actuated Continuum Robots]]
- **作者**: Branden Frieden, James M. Ferguson, Alan Kuntz, Varun Shankar
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

连续体机器人能够在狭窄环境中实现灵巧操作，尤其适合微创手术、检测和受限空间作业等场景，但其实时控制与运动规划依赖高精度、低延迟的形状预测模型。传统基于物理的 Cosserat rod 模型虽然精细，但在考虑腱索路由、摩擦与非线性耦合时计算代价较高；而现有学习式方法往往只对训练过的单一机器人结构有效，换个设计参数就需要重新采集数据并训练。本文的价值在于把“不同设计下的腱驱连续体机器人形状预测”重新表述为算子学习问题，从而尝试用一个统一模型覆盖更大设计空间。

#### 方法概述和架构

论文将腱驱连续体机器人（TDCR）的正向建模表述为一个从设计空间到平衡构型空间的算子映射：输入是机器人设计参数与腱张力，输出是沿骨架弧长位置上的三维位置和姿态。作者构建了四种神经算子结构，分别基于 DeepONet 和 FNO，两类架构都用于学习“设计 + 控制输入”到“机器人平衡形状”的函数到函数映射。训练数据由 Cosserat rod 仿真生成，覆盖多个不同设计；推理时，模型可直接根据给定设计参数和腱激励，快速预测整条机器人骨架的构型。文中还讨论了损失函数、数据预处理与训练流程，并给出可复现实验所需的结构细节。整体上，这一流程把传统数值求解的边值问题替换为一次前向网络计算，以支持控制、规划和设计优化。

#### 实验结果分析

实验在仿真数据上验证了四种神经算子模型的效果，比较对象主要围绕不同 DeepONet/FNO 变体及其泛化能力展开。结果表明，这些架构都能较好逼近连续体机器人平衡构型，并且能够对未见过的设计参数保持较好的泛化，而不仅限于训练时的单一机器人。论文还考察了模型参数量、分布外预测和推理时间等方面，显示神经算子在速度与精度之间具有较好的折中。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

连续体机器人能够在受限环境中实现灵巧操作，但要用于实时操控与控制，必须具备准确且高效的模型。传统基于物理的模型计算开销较大，并且可能受到未建模效应的影响而出现误差；而现有基于学习的方法往往只能在其训练所对应的特定机器人上泛化，难以迁移到新的结构设计。我们将腱驱连续体机器人的替代建模问题表述为一个算子学习问题，即学习一个从机器人设计参数和腱驱动输入到最终构型的映射。该表述使得单个训练好的模型能够在大范围的机器人设计类别上泛化。我们提出了四种新的神经算子架构——两种基于 Deep Operator Networks（DeepONets），两种基于 Fourier Neural Operators（FNOs）——并使用仿真数据进行训练，以预测机器人的构型。所有架构都取得了良好的精度，同时能够在不同设计之间实现快速且准确的泛化。我们的结果表明，算子学习为设计空间中的连续体机器人力学提供了一种有效且可泛化的替代模型，可用于手术和工业应用中的快速建模，从而服务于控制、规划与设计优化。

</details>

---

### [[20_Research/Papers/强化学习/RLFTSim_Realistic_and_Controllable_Multi-Agent_Traffic_Simulation_via_Reinforcement_Learning_Fine-Tuning|RLFTSim: Realistic and Controllable Multi-Agent Traffic Simulation via Reinforcement Learning Fine-Tuning]]

![[assets/2605.19033_figure.png|800]]

- **arXiv**: [2605.19033](https://arxiv.org/abs/2605.19033)
- **PDF**: https://arxiv.org/pdf/2605.19033
- **详细分析**: [[20_Research/Papers/强化学习/RLFTSim_Realistic_and_Controllable_Multi-Agent_Traffic_Simulation_via_Reinforcement_Learning_Fine-Tuning|RLFTSim: Realistic and Controllable Multi-Agent Traffic Simulation via Reinforcement Learning Fine-Tuning]]
- **作者**: Ehsan Ahmadi, Hunter Schofield, Behzad Khamidehi, Fazel Arasteh, Jinjun Shan, Lili Mou, Dongfeng Bai, Kasra Rezaee
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.4，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

自动驾驶中的多智能体交通仿真需要同时具备真实性、闭环交互能力和可控性，但现有方法大多依赖监督式开环训练，难以刻画复杂驾驶场景中持续变化的多车交互。即便使用真实轨迹回放，在闭环部署时也会因为智能体不再响应环境而变得不真实，进而产生明显的 sim-to-real gap。论文关注如何在预训练交通仿真模型之上，通过后训练方式把仿真分布对齐到真实驾驶数据，并进一步让生成场景具备目标条件控制能力，因此具有较强的应用价值。

#### 方法概述和架构

作者提出 RLFTSim，一个基于强化学习的微调框架，用于对多智能体交通仿真模型进行闭环对齐。该方法以预训练的仿真模型为基础，在闭环 rollout 上定义奖励，并把 Waymo Open Simulation Challenge 的真实性元指标 RMM 作为优化目标。由于原始 RMM 以 32 条 rollout 为一组进行统计，信号稀疏且方差较大，作者设计了 MLOO（meta-metric leave-one-out）作为低方差、稠密的奖励形式，使每条 rollout 都能参与训练。框架还将 goal conditioning 与 hindsight experience replay 结合，用于蒸馏仿真的可控性：先为部分智能体指定目标，再通过强化学习让模型学会生成满足目标、同时保持真实性的轨迹。整体流程是先用开环模仿学习训练基础模型，再在闭环环境中进行 RL 微调，分别支持 goal-free 的真实性对齐和 goal-conditioned 的可控生成。

#### 实验结果分析

作者在 Waymo Open Motion Dataset 上进行了系统实验，并以 WOSAC 的真实性指标 RMM 及相关仿真评测为主要评价标准。结果表明，RLFTSim 在真实性方面取得了提升，并达到当前最优水平；相较于基于启发式搜索的微调方法，它依靠更稠密、低方差的奖励显著减少了采样需求。论文还展示了该方法在 goal-conditioned 场景下能够有效蒸馏交通仿真的可控性。节选中未给出具体数值，但从实验描述看，作者同时做了奖励设计、目标控制和模型无关性等扩展实验。

<details>
<summary>完整摘要</summary>

监督式开环训练已被广泛用于训练交通仿真模型；然而，它无法捕捉复杂驾驶场景中固有的动态多智能体交互。我们提出 RLFTSim，这是一种基于强化学习的微调框架，通过让仿真 rollout 与真实世界数据分布对齐来提升场景真实性，并提供一种方法，用于蒸馏场景生成中的目标条件可控性。我们在一个预训练的仿真模型之上实现 RLFTSim，设计了一个在真实性与可控性之间取得平衡的奖励函数，并在 Waymo Open Motion Dataset 上进行了全面实验。结果显示，该方法在真实性方面取得提升，并达到了当前最优性能。与其他基于启发式搜索的微调方法相比，RLFTSim 由于提出了低方差且稠密的奖励信号，因此所需样本显著更少；同时，它从设计上直接解决了真实性对齐问题。我们还证明了该方法在通过目标条件蒸馏交通仿真可控性方面的有效性。项目页面见 https://ehsan-ami.github.io/rlftsim 。

</details>

---

### [[20_Research/Papers/大模型/OEP_Poisoning_Self-Evolving_LLM_Agents_via_Locally_Correct_but_Non-Transferable_Experiences|OEP: Poisoning Self-Evolving LLM Agents via Locally Correct but Non-Transferable Experiences]]

![[assets/2605.18930_figure.png|800]]

- **arXiv**: [2605.18930](https://arxiv.org/abs/2605.18930)
- **PDF**: https://arxiv.org/pdf/2605.18930
- **详细分析**: [[20_Research/Papers/大模型/OEP_Poisoning_Self-Evolving_LLM_Agents_via_Locally_Correct_but_Non-Transferable_Experiences|OEP: Poisoning Self-Evolving LLM Agents via Locally Correct but Non-Transferable Experiences]]
- **作者**: Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou, Jie Li
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

记忆增强型大模型智能体依赖反思与自我演化来逐步改进复杂任务表现，已被用于自动驾驶、医疗、代码生成等场景。但这类系统的长期记忆与反思机制也带来了新的安全风险：攻击者不一定需要注入显式恶意内容，只要诱导智能体形成“看似正确、语义合理”的经验，就可能在后续归纳中被过度泛化，进而污染长期记忆。本文关注的正是这种更隐蔽、也更难被安全过滤器发现的攻击面，因此具有较强的现实安全意义。

#### 方法概述和架构

论文提出 Obsessive Experience Poisoning（OEP），一种面向自我演化 LLM 智能体的低权限黑盒攻击。其核心思路是构造“Clean Edge-Cases”：输入在局部上下文中是正确的，但所采用的方法并不具备跨任务可迁移性。随后再加入 Adversarial Consequence Triplet（ACT），即为这些边缘案例配上严重但仍合理的假设性后果，用以放大智能体的风险厌恶倾向。攻击流程分三步：先生成局部正确但不可迁移的解法，再通过 ACT 改写其经验表述，最后经由普通用户级交互送入智能体的反思与记忆整合流程。智能体在验证局部正确性的同时，会过度重视负面后果，将局部经验蒸馏为高优先级但过度泛化的规则，最终在后续任务中出现失败。

#### 实验结果分析

作者在三个领域中评估了 OEP，对象是带记忆和反思机制的智能体，并与现有记忆攻击方法及 LLM auditing 防御进行比较。实验结果显示，OEP 在 GPT-4o 智能体上可取得超过 50% 的 ASR，且在启用审计防御时仍表现出比基线更强的攻击有效性与鲁棒性。文中还做了消融分析，考察了模型骨干、对抗样本比例和 ACT 组件的作用；总体结论是，能力更强的智能体在这种攻击下也可能更脆弱。

<details>
<summary>完整摘要</summary>

记忆增强型大模型（LLM）智能体通过迭代反思和自我演化来解决复杂任务，但这些机制也引入了安全风险。现有的智能体记忆攻击通常需要更高权限或显式恶意内容，因此会被更先进的安全过滤器检测出来。这留下了一个更隐蔽但尚未被充分研究的攻击面：攻击者是否能够诱导智能体生成看似局部正确、语义合理，但在反思过程中会导致有害泛化的经验？我们发现，反思型智能体会受到这类“干净经验”的影响，尤其当这些经验伴随严重但合理的假设性后果时更为明显。基于这一观察，我们提出 Obsessive Experience Poisoning（OEP），这是一种低权限黑盒攻击，不需要直接控制系统提示词或记忆数据库。OEP 通过构造对抗性的干净边缘案例，将局部正确的解法、不可迁移的方法以及严重后果组合在一起，从而使反思过程偏向形成风险规避型规则。在记忆整合阶段，智能体可能过度信任自身生成的反思，并将局部经验提炼为高优先级但过度泛化的规则，导致后续任务失败。跨三个领域的评估表明，OEP 在 GPT-4o 智能体上可实现超过 50% 的 ASR，并且在 LLM 审计防御下优于现有攻击方法。

</details>

---

### [[20_Research/Papers/大模型/Don't_Let_Bandit_Feedback_Pull_Continual_LLM-Recommender_Updates_Off_Target|Don't Let Bandit Feedback Pull Continual LLM-Recommender Updates Off Target]]

![[assets/2605.18899_figure.png|800]]

- **arXiv**: [2605.18899](https://arxiv.org/abs/2605.18899)
- **PDF**: https://arxiv.org/pdf/2605.18899
- **详细分析**: [[20_Research/Papers/大模型/Don't_Let_Bandit_Feedback_Pull_Continual_LLM-Recommender_Updates_Off_Target|Don't Let Bandit Feedback Pull Continual LLM-Recommender Updates Off Target]]
- **作者**: Taesan Kim, Hyeongjun Yun, Jaegul Choo, Chung Park
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

生成式大模型推荐系统（LLM-Rec）在上线后仍需要持续更新，以适应用户兴趣漂移、季节变化以及曝光机制变化带来的分布偏移。现实中的日志并不是完整监督信号，而是由旧策略“塑形”后的上下文 bandit 反馈：只对被曝光的候选项观察到结果，且同时包含相对可靠的正反馈与含义模糊的无响应。直接用这类日志做持续更新，容易把模型带偏到历史曝光偏好上，进一步放大曝光偏差和流行度偏置，因此这个问题很值得关注。

#### 方法概述和架构

论文提出 Anchored Bandit Policy Optimization（ABPO），在 GRPO 的基础上显式处理曝光偏差与反馈歧义。其核心做法是：在每个 rollout group 中把历史策略实际曝光的推荐项作为“锚点”加入组内，使组相对归一化不再只围绕新采样结果，而是围绕真实被曝光的动作校准。针对锚点样本，作者使用 self-normalized inverse propensity scoring（SNIPS）做重加权，以修正旧策略导致的 off-policy 偏差。对于反馈建模，方法将正反馈与无响应非对称处理：正反馈视为较直接的认可信号；无响应则可能来自未观看、位置效应或注意力不足，因此不会简单当作硬负例，而是引入模型输出 token 的置信度作为 self-certainty，对无响应惩罚进行降权。最终，ABPO 通过“锚点校准 + 倾向校正 + 非对称奖励构造”的组合，完成对持续更新目标的稳定优化。

#### 实验结果分析

论文在 Amazon Reviews 和 MovieLens 的五个领域上构造离线 post-deployment bandit 反馈流，并与多种已有的反馈驱动更新基线进行比较，评估指标主要包括推荐准确率和流行度偏置/多样性相关表现。结果显示，ABPO 在更新后能稳定提升推荐准确率，同时比基线更有效地缓解由旧策略引入的曝光偏差。文中还报告了在线 A/B 测试：ABPO 在真实业务中取得了较强的 CTR，并在连续生产更新中表现出逐步提升的趋势。消融与分析部分进一步支持了锚点设计、SNIPS 校正以及对无响应的保守处理对稳定更新的重要性；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

生成式、基于 LLM 的推荐系统（LLM-Rec）在部署后需要持续更新，但上线日志只能提供由策略塑形的上下文 bandit 反馈：只有对先前服务策略曝光过的物品才能观察到结果，这会带来曝光偏差，并形成部分且非对称的信号，其中既包含相对可靠的正反馈，也包含含义模糊的无响应。我们提出 Anchored Bandit Policy Optimization（ABPO）框架，用于 LLM-Rec 的持续更新。该框架将 group-relative policy optimization（GRPO）与对曝光偏差和反馈歧义的显式处理结合起来。具体而言，我们把被曝光的推荐项作为日志锚点插入到每个 GRPO rollout 组中，使组内相对归一化以先前策略实际曝光的动作作为校准基准，而不是仅仅围绕新采样的 rollout 进行校准。由于正反馈和无响应都是通过先前策略的曝光才被观测到的，我们对固定锚点在这两类反馈上都应用 self-normalized inverse propensity scoring，以修正策略不匹配问题。同时，我们对两类反馈的可靠性采取非对称处理：正反馈提供相对直接的认可信号，而无响应仍然是模糊的，因为它可能反映真实的不感兴趣，也可能来自未观测到的外部因素。为避免对模糊无响应施加过于激进的更新，我们利用模型输出 token 的置信度作为无需 verifier 的可靠性信号，用 self-certainty 来缓和其惩罚。我们在 Amazon Reviews 和 MovieLens 的五个领域上验证了该方法，结果表明它在持续更新后能够稳定提升推荐准确率，并且比已有基线更有效地缓解了由先前策略引入的曝光偏差。真实世界的在线 A/B 测试进一步显示，该方法获得了较高的 CTR，并在连续的生产更新中逐步改善，说明其在生产环境中具有良好的实用性。

</details>

---

### [[20_Research/Papers/大模型/To_Call_or_Not_to_Call_Diagnosing_Intrinsic_Over-Calling_Bias_in_LLM_Agents|To Call or Not to Call: Diagnosing Intrinsic Over-Calling Bias in LLM Agents]]

![[assets/2605.18882_figure.png|800]]

- **arXiv**: [2605.18882](https://arxiv.org/abs/2605.18882)
- **PDF**: https://arxiv.org/pdf/2605.18882
- **详细分析**: [[20_Research/Papers/大模型/To_Call_or_Not_to_Call_Diagnosing_Intrinsic_Over-Calling_Bias_in_LLM_Agents|To Call or Not to Call: Diagnosing Intrinsic Over-Calling Bias in LLM Agents]]
- **作者**: Wei Shi, Ziheng Peng, Sihang Li, Xiting Wang, Xiang Wang, Mengnan Du, Na Zou
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

大模型智能体在调用外部工具时，不仅要“会调用”，更要“知道何时不调用”。论文聚焦于 When2Call 这类工具调用门控任务，指出多个模型虽然在“该调用时”的准确率较高，但在“不该调用时”却明显更弱，导致整体表现受限，也会带来额外 API 成本与用户体验下降。作者因此关注一个更深层的问题：这种过度调用究竟是数据或评测造成的表面现象，还是模型内部存在一种固有的调用偏置。

#### 方法概述和架构

论文首先在六个模型上训练并使用 Sparse Autoencoders（SAEs）分析残差流表示，从中恢复与“call / no_call”决策对齐的特征基。随后，作者基于行为标注数据构建了 call 与 no_call 两组特征，并用特征激活差值与方向性 AUROC 对其进行排序和验证，再用逻辑回归探测这些特征是否足以线性预测门控决策。接着，论文将两组特征压缩为一个带符号的激活边际，检验在激活相等时模型是否仍偏向 call，从而形式化提出 Intrinsic Bias Hypothesis（IBH）。最后，作者提出 Adaptive Margin-Calibrated Steering（AMCS），沿 SAE 解码器方向施加闭式反偏移量，对已诊断出的偏置进行因果干预，并比较干预前后模型的调用行为与准确率变化。

#### 实验结果分析

在 When2Call 评测上，六个模型都呈现出“call 准确率高、no_call 准确率低”的一致现象，整体准确率大致落在 55%–70% 区间。基于 SAE 的分析表明，模型只有在 no_call 激活强于 call 激活时才会变得决策中性，这支持了作者提出的内在偏置假设，而不是单纯由激活差值决定。使用 AMCS 抵消该偏置后，五个模型的 no_call 准确率提升了 4–17 个百分点，整体准确率最高提升 5 个百分点，同时对 call 准确率影响很小。

<details>
<summary>完整摘要</summary>

大模型智能体表现出一种稳定的过度调用倾向，即即使在不需要工具的情况下也会调用工具。在 When2Call 基准上，来自三类家族的六个模型都呈现出很高的 call 准确率，但 no_call 准确率明显更低，使得整体准确率落在 55%–70% 之间。我们将这一现象归因于内在偏置假设（Intrinsic Bias Hypothesis, IBH）：call/no_call 决策映射中存在一个与激活无关的调用偏移量，因此即便在激活持平时，模型也会更偏向于 call。借助 Sparse Autoencoders（SAEs），我们恢复了与 call/no_call 决策行为对齐的特征基，并将其归约为一个带符号的激活边际，从而直接估计该偏移量。对所有六个模型的分析都表明，只有当 no_call 的激活超过 call 的激活时，模型才会处于决策中性状态，这与 IBH 一致。随后，我们使用 Adaptive Margin-Calibrated Steering（AMCS）对 IBH 进行因果检验：该方法沿 SAE 解码方向施加一个闭式的反偏移量。抵消诊断出的偏移后，模型的过度调用得到缓解，整体准确率提升，而 call 准确率仅有可忽略的下降。我们的工作将过度调用从一个经验现象重塑为一个可通过机制分析与因果校正处理的对象。代码已开源于 https://github.com/SKURA502/agent-sae/ 。

</details>

---

### [[20_Research/Papers/强化学习/EUPHORIA_Efficient_Universal_Planning_via_Hybrid_Optimization_for_Robust_Industrial_Robotic_Assembly|EUPHORIA: Efficient Universal Planning via Hybrid Optimization for Robust Industrial Robotic Assembly]]

![[assets/2605.18872_figure.png|800]]

- **arXiv**: [2605.18872](https://arxiv.org/abs/2605.18872)
- **PDF**: https://arxiv.org/pdf/2605.18872
- **详细分析**: [[20_Research/Papers/强化学习/EUPHORIA_Efficient_Universal_Planning_via_Hybrid_Optimization_for_Robust_Industrial_Robotic_Assembly|EUPHORIA: Efficient Universal Planning via Hybrid Optimization for Robust Industrial Robotic Assembly]]
- **作者**: Shih-Yu Lai, Chia-Ching Yen, Yang-Ting Shen, Peter Yichen Chen, Yu-Lun Liu, Bing-Yu Chen
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.36，世界模型 0.16，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

建筑施工中的机器人砌块装配面临一个长期瓶颈：一方面，不同几何形态（如穹顶、拱形、曲面墙）之间差异很大，现有规划器往往只能针对单一结构工作，换一个设计就需要重新训练或大量微调；另一方面，很多方法把结构装配顺序和机器人运动规划拆开处理，导致序列上“可行”的方案在执行时可能能耗高、动作别扭，甚至不稳定。对于强调“先仿真、后落地”的建筑机器人场景，这种跨几何泛化与高效执行的同时缺失，直接限制了从数字设计到实体建造的落地能力。

#### 方法概述和架构

本文提出 EUPHORIA，一个用于工业机器人装配的统一规划框架，核心目标是让单一模型在少样本条件下适应未见过的结构拓扑，并同时兼顾结构稳定性、运动效率和 Sim2Real 鲁棒性。方法首先使用基于 Graph Hypernetworks 的 Meta-Geometric Encoder，从少量支持样本中动态生成任务相关的策略参数，实现参数级的少样本适配，而不是依赖传统对比学习式的特征级识别。随后，引入由 SAC 训练的 Physics-Informed Graph Transformer，并设计 Physics-Bias Attention，用 DEM 仿真得到的接触力来调制注意力权重，从而优先关注对结构最关键的连接关系。为了降低执行代价，方法在 SAC 目标中加入 Kinematics-Aware Sequencing，对高能量转移进行惩罚，使结构顺序规划与机器人运动效率联合优化。最后通过可微的 Residual Stability Correction 层，在执行前对粗略装配动作进行残差式修正，以能量-稳定性联合目标进一步弥合仿真到真实的差距。

#### 实验结果分析

论文在建筑机器人装配场景中进行了实验，对比了若干解耦式基线和图强化学习基线，并从装配成功率、能耗、稳定性以及 Sim2Real 鲁棒性等方面进行评估。结果显示，EUPHORIA 在未见过的非标准几何上能够用很少的 few-shot 样本取得更高的成功率，同时相较解耦基线显著降低了能量消耗。消融实验表明，少样本几何编码、物理偏置注意力、运动学感知序列优化以及残差稳定性修正都对最终性能有贡献；不过节选文本未给出具体数值。

<details>
<summary>完整摘要</summary>

建筑施工中的机器人装配存在一个持续性的瓶颈：现有规划器要么高度专用，针对每一种新的几何设计都需要代价高昂的重新训练；要么在运行上效率低下，把结构装配顺序与运动学动作视为两个彼此独立的过程。为此，我们提出 EUPHORIA，一个通过混合优化策略实现通用少样本适应与动态效率的统一框架。为克服“重新训练瓶颈”，我们提出一种基于 Graph Hypernetworks 的元几何编码器：不同于只在特征层面进行识别的标准对比学习，该超网络能够根据极少量支持样本动态生成策略参数，使其无需基于梯度的重新训练即可对复杂拓扑（如穹顶、拱形）进行参数级适配。针对结构推理，我们引入一个通过 Soft Actor-Critic（SAC）训练的物理信息图 Transformer，并设计 Physics-Bias Attention 机制，用来自离散元模型（DEM）仿真的接触力来调制注意力得分，引导规划器优先选择结构上关键的连接。进一步地，我们通过 Kinematics-Aware Sequencing 确保运行效率，其中 SAC 目标会对高能量转移进行惩罚。最后，我们通过 Residual Stability Correction 来弥合 Sim2Real 差距：这是一个可微优化层，在执行前通过最小化联合的能量-稳定性代价，对粗略的装配动作进行微调。实验表明，EUPHORIA 相比解耦式基线显著降低了能耗，并且在仅使用少量 few-shot 样本的情况下，在未见过的非标准几何上取得了最先进的成功率。该方法将元学习、物理信息注意力与残差优化融合为一个统一且泛化能力更强的规划器。

</details>

---

### [[20_Research/Papers/世界模型/Transformers_Linearly_Represent_Highly_Structured_World_Models|Transformers Linearly Represent Highly Structured World Models]]

![[assets/2605.18847_figure.png|800]]

- **arXiv**: [2605.18847](https://arxiv.org/abs/2605.18847)
- **PDF**: https://arxiv.org/pdf/2605.18847
- **详细分析**: [[20_Research/Papers/世界模型/Transformers_Linearly_Represent_Highly_Structured_World_Models|Transformers Linearly Represent Highly Structured World Models]]
- **作者**: Roman Kniazev, Nathanaël Fijalkow
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel

#### 研究背景与动机

这篇论文关注的是：当 transformer 通过顺序推理轨迹学习解题时，是否会在内部形成一个可解释的“世界模型”，以及这个模型的结构是否会反映任务本身的约束结构。作者选择 Sudoku 作为研究对象，因为它不是像 Othello 那样天然按“单元格”分解，而是由行、列、宫这三类重叠子结构共同约束，特别适合检验模型到底是按表面网格，还是按约束代数来组织表示。对于强化学习与可解释性研究来说，这类结论有助于理解模型如何在组合推理任务中形成内部表征，也关系到能否把复杂决策过程拆解为可审计的机制。

#### 方法概述和架构

作者训练了一个 8 层的 decoder-only transformer，在 Norvig 风格的 Sudoku 求解轨迹上学习从线索到推理步骤的序列生成。模型输入是包含题目线索和中间推理操作的 token 序列，重点分析位置是 [clues_end]，即线索结束、模型即将开始输出推理的位置。为了研究内部表示，他们在各层 residual stream 上训练线性探针，分别测试三种表征：按单元格预测数字、按单元格预测候选数、按子结构预测某个数字是否存在于对应行/列/宫中。随后结合 causal intervention、activation patching、direct logit attribution、logit lens 和 attention head decomposition，分析哪些层和哪些头在传播约束信息、以及最终如何把正确数字推到输出层。

#### 实验结果分析

实验基于 sudoku-3m 数据集训练的 2.7M 个谜题，模型在 150K 题的测试集上达到 98.4% 的 per-cell accuracy 和 97.5% 的 per-grid accuracy。线性探针结果显示：单元格级表示只能达到约 0.8 的 top-1 准确率，而子结构级“某数字是否出现在某行/列/宫中”的探针在中间层可实现完美精度，说明模型的内部几何更贴近约束结构而非网格表面结构。进一步的因果消融表明这些子结构方向确实被模型用于预测；注意力头也呈现出按行、列、宫组织的路由模式。论文还识别出一个裸单（naked single）电路：最后一层 MLP 中少量专门神经元会在某个格子只剩唯一候选数时稳定放大该数字；可见文本未给出具体消融数值，但整体结论是该电路稀疏、单义且可完全解释。

<details>
<summary>完整摘要</summary>

transformer 在训练于顺序推理轨迹时，是否会在内部建立底层任务的模型？如果会，这些内部表征的结构是否会镜像领域本身的结构？我们在 Sudoku 求解轨迹上训练了一个 8 层 transformer，并对其内部计算进行了机制分析。我们得到了两个结论。第一，模型构建了一个“子结构世界模型”：它并不是像人类分析者通常预期的那样逐格表示棋盘状态，而是围绕 Sudoku 约束所作用的行、列和宫来组织信息。第二，我们识别出一个裸单电路：最后一个 MLP 层中的一小组专门神经元，每个神经元都会单独检测某个特定格子是否恰好只剩一个数字可填，并可靠地促进该数字被输出。这些发现表明，涌现式世界模型的几何结构由领域的约束代数所塑造，而不是由其表面呈现方式所决定；同时，最终形成的决策电路是稀疏的、单义的，而且完全可解释。更广泛地说，这些结果说明，机制可解释性工具能够恢复 transformer 解决组合推理任务时的端到端算法性描述。

</details>

---

### [[20_Research/Papers/大模型/Precision_Tracked_Transformer_via_Kalman_Filtering,_Kriging_and_Process_Noise|Precision Tracked Transformer via Kalman Filtering, Kriging and Process Noise]]

![[assets/2605.18832_figure.png|800]]

- **arXiv**: [2605.18832](https://arxiv.org/abs/2605.18832)
- **PDF**: https://arxiv.org/pdf/2605.18832
- **详细分析**: [[20_Research/Papers/大模型/Precision_Tracked_Transformer_via_Kalman_Filtering,_Kriging_and_Process_Noise|Precision Tracked Transformer via Kalman Filtering, Kriging and Process Noise]]
- **作者**: Bo Long, Deepak Agarwal, Jelena Markovic-Voronov, Yi Wang, Liuqing Li
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 0.82（加权：大模型 0.3，强化学习 0.16，世界模型 0.36）
- **关联关键词**: LLM, WorldModel

#### 研究背景与动机

Transformer 已经成为现代 AI 的基础组件，但在很多真实场景里，它默认“每个 token 都同样可信”，缺少对不确定性的原则性建模。这在序列推荐中会表现为冷启动用户和稀有物品历史稀疏，在语言模型中会表现为监督噪声、检索噪声以及注意力 sink 等问题。本文关注的是如何把“置信度/精度”显式引入 Transformer，使模型在信号质量不均、数据噪声较强的任务上更稳健，因此与世界模型、大模型和强化学习中的不确定性建模都有关联。

#### 方法概述和架构

论文提出 Bayesian Filtering Transformer（BFT），把标准 Transformer 层重新解释为一个贝叶斯滤波过程：自注意力对应 observe，残差连接对应 update，FFN 对应 predict。核心做法是在注意力中显式引入精度，令 attention 权重变成“相关性 × 可靠性”的 kriging 形式，也就是在 query-key logits 上加上由精度得到的偏置，从而区分高置信与低置信 token。随后，残差更新不再固定等于完整创新，而是通过 Kalman gain 自适应融合当前证据与先验状态；FFN 则像动态模型一样传播隐状态，同时通过 Jacobian 和 process noise 传播精度。观察精度由参数无关的 REML 估计器配合共轭贝叶斯先验获得，整个方法可以作为任意 Transformer 层的即插即用替换，推理和训练流程基本保持原有结构，仅增加精度通道与对应更新。

#### 实验结果分析

实验覆盖三个推荐骨干（SASRec、BERT4Rec、HSTU）和六个标准基准，BFT 在这些架构上都带来显著提升，尤其在冷启动用户和稀有物品上收益最大，符合其“精度追踪”机制的预期。论文还在 TinyLlama-1.1B 的监督微调中验证了鲁棒性：在 SQuAD 的 token-label corruption 噪声监督、以及 NQ-Open 的真实检索干扰场景下，BFT 都优于标准 SFT，并且在噪声更强时优势更明显。节选文本还指出，BFT 适用于不同注意力骨干并具有较低开销，但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

Transformer 是现代 AI 的基础构件，但它并没有对真实应用中普遍存在的不确定性提供原则性的处理：例如，序列推荐中的冷启动 token 只有很少的历史，语言模型中的信号质量参差不齐，以及由无约束 softmax 引起的 attention sink。标准 Transformer 会把每个 token 视为具有相同置信度。我们表明，这种“统一置信”只是我们提出的 Bayesian Filtering Transformer（BFT）的一个退化情形：注意力变为精度加权的 kriging，残差连接变为带自适应增益的 Kalman 更新，FFN 则变为通过 Jacobian 加过程噪声规则传播精度的动力学模型。观测精度来自一个无参数的 Restricted Maximum Likelihood（REML）估计器，并配有共轭贝叶斯先验。BFT 可以以几乎可忽略的额外开销替换任意 Transformer 层。在序列推荐任务上，BFT 应用于三种主流架构后，在六个基准上都取得了显著提升，其中在不确定性最高的冷启动用户和稀有物品上改善最大。在带噪数据上的大语言模型监督微调中，BFT 在两个场景下提升了鲁棒性：噪声监督（问答中的 token-label 破坏）和噪声上下文（带真实 RAG 干扰项的检索增强问答）。一个原则性的改动——恢复精度——就能在经典序列建模与现代 LLM 场景中释放出可观的性能空间。

</details>

---

### [[20_Research/Papers/具身智能/Composition_of_Memory_Experts_for_Diffusion_World_Models|Composition of Memory Experts for Diffusion World Models]]

![[assets/2605.18813_figure.png|800]]

- **arXiv**: [2605.18813](https://arxiv.org/abs/2605.18813)
- **PDF**: https://arxiv.org/pdf/2605.18813
- **详细分析**: [[20_Research/Papers/具身智能/Composition_of_Memory_Experts_for_Diffusion_World_Models|Composition of Memory Experts for Diffusion World Models]]
- **作者**: Sebastian Stapf, Pablo Acuaviva Huertos, Aram Davtyan, Paolo Favaro
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.36，世界模型 0.96）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

世界模型需要根据过去观测预测合理未来，是强化学习中规划与决策的重要基础，尤其在导航和交互任务里，预测结果必须与历史观察保持一致，否则想象出来的轨迹就失去可用性。现有架构存在明显的记忆权衡：Transformer 能保留局部细节，但注意力计算是二次复杂度，长上下文代价过高；循环网络和状态空间模型更省算力，却会把历史压缩进隐藏状态，逐渐丢失细节与长程一致性。作者因此关注如何把“记忆能力”从单一骨干里解耦出来，改为由多个专门专家协同完成，这一思路对长时序世界模型尤其值得关注。

#### 方法概述和架构

论文提出 Composition of Memory Experts for Diffusion World Models，以扩散模型为基础，把不同类型的记忆能力通过对比式产品专家（PoCE）进行组合。整体上，过去历史被拆分为多个子上下文，由不同专家分别建模：短期记忆专家负责捕捉局部细粒度动态，长期记忆专家通过轻量级测试时微调把情景记忆写入外部扩散权重中，空间长期记忆专家则引入几何与空间一致性约束。推理时，各专家对同一个未来样本给出约束，模型不再依赖单一网络记住全部历史，而是在采样阶段把这些专家的分布乘起来，从而得到与过去观测一致的未来预测。为了避免普通产品专家把共享模式过度放大、导致模式坍塌，作者进一步设计了对比机制，用来剥离冗余模式、保留真正与历史一致的部分。方法还强调空间先验的作用，利用位姿或拓扑线索帮助检索与组合，使生成结果在时间和空间上都更稳定。

#### 实验结果分析

作者在模拟和真实世界基准上验证了该方法，涉及 Memory Maze、RECON、RealEstate10K、DeepMind Lab（DMLab-40K）、Minecraft-200K 和 Memory Cards 等数据集。评估重点包括与过去观测帧的一致性、连续观测流的长期一致性、记忆回忆能力以及导航表现；相较于相关基线，方法在这些方面都有改进。正文节选中未给出具体数值，但可以看出作者还做了消融实验，分析了 PoCE、Langevin 修正步数以及不同记忆专家配置的影响。整体结论是：这种专家组合式记忆机制能在不引入二次注意力开销的情况下扩展到更长上下文，并提升时序一致性与导航性能。

<details>
<summary>完整摘要</summary>

世界模型旨在预测与过去观测一致的合理未来，这是强化学习中规划与决策的核心能力。然而，现有架构面临一个根本性的记忆权衡：Transformer 能保留局部细节，但受限于二次复杂度的注意力机制；循环网络和状态空间模型则能更高效地扩展，但会以牺牲历史信息保真度为代价对历史进行压缩。为克服这一权衡，我们提出将“未来—过去一致性”从任何单一架构中解耦出来，转而利用一组专门化专家来实现。我们提出一个基于扩散的框架，通过对比式产品专家（contrastive product-of-experts）形式整合异构记忆模型。该方法实现了三种互补角色：短期记忆专家用于捕捉细粒度的局部动态；长期记忆专家通过轻量级测试时微调，将情景历史存储在外部扩散权重中；空间长期记忆专家则负责约束几何与空间一致性。这样的组合式设计避免了模式坍塌，并能够在不产生二次复杂度开销的前提下扩展到长上下文。在模拟与真实世界基准上，我们的方法提升了时间一致性、对过去观测的回忆能力以及导航性能，确立了一种构建和运行记忆增强扩散世界模型的新范式。

</details>

---

### [[20_Research/Papers/强化学习/PROWL_Prioritized_Regret-Driven_Optimization_for_World_Model_Learning|PROWL: Prioritized Regret-Driven Optimization for World Model Learning]]

![[assets/2605.18803_figure.png|800]]

- **arXiv**: [2605.18803](https://arxiv.org/abs/2605.18803)
- **PDF**: https://arxiv.org/pdf/2605.18803
- **详细分析**: [[20_Research/Papers/强化学习/PROWL_Prioritized_Regret-Driven_Optimization_for_World_Model_Learning|PROWL: Prioritized Regret-Driven Optimization for World Model Learning]]
- **作者**: Ahmet H. Güzel, Jenny Seidenschwarz, Benjamin Graham, Jonathan Sadeghi, Jeffrey Hawke, Jack Parker-Holder, Ilija Bogunovic
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

这篇工作聚焦于动作条件视频世界模型在强化学习中的应用，目标是让模型不仅“看起来像”，还要能在短时序上准确响应动作并支持后续规划。作者指出，现有扩散式世界模型虽然在短期视觉重建上表现很好，但对少见、却对交互和决策极关键的状态转移常常不可靠，而被动示范数据又天然会低估这类高影响样本。因而，提升鲁棒性不能只依赖更多静态数据，而需要主动挖掘模型失败并把失败转化为训练信号。

#### 方法概述和架构

论文提出 PROWL（Prioritized Regret-Driven Optimization for World Model Learning），采用两阶段训练流程：先用 BASALT 人类示范预训练一个基于 diffusion forcing 的动作条件 DiT 世界模型，再进入对抗式课程学习阶段。第二阶段中，一个由 PPO 优化的对抗策略在 KL 约束下尽量贴近行为参考策略，同时主动寻找能暴露世界模型高误差的轨迹；世界模型则不断用这些对抗发现的轨迹进行微调。为避免反复训练已解决样本，作者设计了 PAT（Prioritized Adversarial Trajectory）缓冲区，根据预测误差、动作忠实度和学习进展对轨迹重新排序，只重点采样尚未解决的失败模式。整体上，PROWL 将“发现错误”和“修正错误”闭环连接起来，使对抗探索始终受行为先验约束，尽量避免跑到分布外的投机解。

#### 实验结果分析

实验在 MineRL 框架下进行，使用 BASALT 人类示范、VPT 预训练参考策略，以及与 Phase 1 训练任务不同的持出任务进行评估，基线包括仅用被动数据训练的模型和匹配计算量但不进行对抗探索的 Phase 2 微调基线。结果表明，PROWL 在持出分布外轨迹、对抗发现的失败案例以及更长时域自回归滚动上都优于被动训练与匹配计算基线。论文还观察到：当行为约束较弱时，对抗策略会出现 reward hacking，说明有效的世界模型对抗训练必须平衡“积极发现失败”和“显式行为正则化”。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

现代动作条件视频世界模型在短时域的视觉逼真度上已经表现很强，但在少见、却对交互至关重要的转移上仍然不可靠，而这些转移往往决定下游规划和策略性能。由于被动示范数据会系统性地低估这类高影响场景，要提升鲁棒性，就需要主动诱发模型失败，而不是等待失败自然出现。我们提出一种受 KL 约束的对抗式课程学习方法：训练一个策略去暴露基于扩散的世界模型的高误差轨迹，同时保持与行为分布接近。世界模型随后持续在这些对抗发现的轨迹上进行微调，从而形成一个对抗训练闭环，把稀有失败转化为稳定、接近分布内的训练信号，避免偏离到分布外的投机利用。为了在模型逐步改进时继续对未解决弱点施加训练压力，我们提出 Prioritized Adversarial Trajectory（PAT）缓冲区，它根据预测误差、动作忠实度和学习进展重新排序轨迹，把训练重点放在尚未解决的失败模式上，而不是反复回访已解决的案例。我们在 MineRL 框架中实现了该方法，并在保留的分布外轨迹上进行评估；PROWL 相比仅用被动数据训练的模型提升了鲁棒性，揭示了在行为约束较弱时存在 reward hacking 行为，并表明有效的对抗式世界模型训练关键在于平衡探索性失败发现与显式行为正则化。我们的结果表明，可扩展的世界模型不仅受益于更大的数据集，也受益于选择性生成更有信息量的训练数据。

</details>

---

### [[20_Research/Papers/强化学习/ReCrit_Transition-Aware_Reinforcement_Learning_for_Scientific_Critic_Reasoning|ReCrit: Transition-Aware Reinforcement Learning for Scientific Critic Reasoning]]

![[assets/2605.18799_figure.png|800]]

- **arXiv**: [2605.18799](https://arxiv.org/abs/2605.18799)
- **PDF**: https://arxiv.org/pdf/2605.18799
- **详细分析**: [[20_Research/Papers/强化学习/ReCrit_Transition-Aware_Reinforcement_Learning_for_Scientific_Critic_Reasoning|ReCrit: Transition-Aware Reinforcement Learning for Scientific Critic Reasoning]]
- **作者**: Wanghan Xu, Yuhao Zhou, Hengyuan Zhao, Shuo Li, Dianzhi Yu, Zhenfei Yin, Yaowen Hu, Fengli Xu, Wanli Ouyang, Wenlong Zhang, Lei Bai
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

大语言模型在科学问答中不仅会直接答错，还可能在用户质疑后把原本正确的答案改错，尤其是在化学、生物、地学等需要严谨证据链的推理任务中，这种“被质疑后退化”会带来比单纯答错更严重的风险。现有方法多把问题看成最终答案是否正确，而没有区分“初始正确但被带偏”与“初始错误但被纠正”这两类完全不同的交互行为。本文因此将科学 critic 交互重新定义为跨轮次正确性转移问题，值得关注之处在于它直接瞄准了模型在交互中的稳定性与抗顺从性，而不是只追求单轮准确率。

#### 方法概述和架构

论文提出 ReCrit，一种面向科学 critic reasoning 的 transition-aware 强化学习框架。它把模型在“初始回答”到“critic 回答”的变化分成四个象限：Correction、Sycophancy、Robustness 和 Boundary，并基于这四类转移分别赋予不同奖励。训练时，模型先对科学问题生成 Initial 解，再接收不同态度的 critic 反馈（对立、中性、支持），随后生成 Critic 解；判别器分别判断两次回答是否正确，再用四象限奖励计算训练信号。ReCrit 对“初始错误后被纠正”给予强奖励，对“初始正确后被带偏”给予强惩罚，对“初始正确且保持正确”给予较弱奖励，对“两次都错”仅给予较弱惩罚。为了让多轮交互训练更可扩展，方法还引入动态异步 rollout 和 tail-adaptive completion，让完成较快的样本尽早进入后续 critic 阶段，减少同步等待造成的尾部延迟。

#### 实验结果分析

作者在 ChemBench、TRQA 和 EarthSE 三个科学推理基准上进行了实验，模型规模覆盖 Qwen3.5-4B 和 Qwen3.5-9B，并与多种基线和消融设置比较，评价指标重点是 Critic accuracy（critic 反馈后的准确率）。结果显示，ReCrit 将 Qwen3.5-4B 的平均 Critic accuracy 从 38.15 提升到 51.49，将 Qwen3.5-9B 从 45.40 提升到 55.59，说明方法能稳定改善交互后的最终表现。消融分析表明，仅使用最终答案奖励带来的交互层收益很小，而引入转移感知奖励、象限加权后，训练信号更清晰，Critic 阶段净收益更大；动态异步 rollout 则在质量与吞吐之间提供了更实际的折中。

<details>
<summary>完整摘要</summary>

大型语言模型在 critic 交互中失败的方式，不仅可能是答案本身错误，还可能是在用户批评后放弃了最初正确的科学解法后再给出错误答案。这在科学推理场景中尤其危险，因为用户的批评有时会把一个有效答案带偏成无效答案。我们将 critic 交互表述为跨轮次正确性转移问题，而不是仅仅看最终答案准确率，并识别出三类挑战：转移感知、将有益纠正与有害顺从性（sycophancy）解耦，以及可扩展的 rollout。为此，我们提出 ReCrit，这是一个面向正确性转移的强化学习框架，它将 Initial 到 Critic 的行为分解为四个象限：Correction、Sycophancy、Robustness 和 Boundary。ReCrit 对纠错和稳健性给予奖励，对顺从性给予惩罚，并把持续错误视为较弱的边界信号。为了让交互训练更实用，ReCrit 进一步使用动态异步 rollout 与 tail-adaptive completion 来减少 rollout 等待时间。在 ChemBench、TRQA 和 EarthSE 三个科学推理基准上，ReCrit 将 Qwen3.5-4B 的平均 Critic accuracy 从 38.15 提升到 51.49，将 Qwen3.5-9B 从 45.40 提升到 55.59。消融实验表明，最终答案奖励对交互层提升作用有限，而转移感知奖励与象限加权能够产生更可区分的训练信号，并带来更大的 Critic 阶段净提升。代码已开源在 https://github.com/black-yt/ReCrit 。

</details>

---

### [[20_Research/Papers/大模型/Improving_Retrieval-Augmented_Generation_without_Taxonomy-based_Error_Categorization|Improving Retrieval-Augmented Generation without Taxonomy-based Error Categorization]]

![[assets/2605.18772_first_page.png|800]]

- **arXiv**: [2605.18772](https://arxiv.org/abs/2605.18772)
- **PDF**: https://arxiv.org/pdf/2605.18772
- **详细分析**: [[20_Research/Papers/大模型/Improving_Retrieval-Augmented_Generation_without_Taxonomy-based_Error_Categorization|Improving Retrieval-Augmented Generation without Taxonomy-based Error Categorization]]
- **作者**: Gongbo Zhang, Yifan Peng, Chunhua Weng
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

RAG 通过检索外部知识来增强大模型生成的事实性，已成为降低幻觉的重要路线，但在实际的 agentic RAG 中，系统往往依赖 critic 先判断错误类型，再决定如何修正。问题在于，LLM 生成的 critic 反馈并不总是可靠，错误分类可能与真实失败原因不匹配，进而带来无效甚至有害的纠错。本文关注的核心是：在不依赖细粒度错误分类的前提下，RAG 的纠错与规划能力是否仍然可以被有效提升。

#### 方法概述和架构

论文提出 RePAIR，一种 response-action learning 范式，直接把“有缺陷的 RAG 输出”映射为“可缓解错误的动作计划”，不再显式使用错误 taxonomy，也不依赖外部 critic 的精细监督。方法将 RAG 状态表示为问题、检索文档、初始答案等信息，并把高层操作定义为一个动作集合，例如 Rewrite、Decompose、Retrieval、RefineDoc 和 GenerateAnswer。模型输出的是一个可变长度的操作序列，执行器按顺序应用这些操作，生成修正后的答案，再用 token-level F1 作为奖励。训练上采用两阶段策略：先在 off-policy 阶段利用 oracle 正确性标签和错误推理轨迹进行预热，再在 on-policy 阶段仅依赖推理时可获得的粗粒度正确性估计进行对齐式训练。优化目标使用 DPO，通过候选计划的相对奖励构造偏好对，学习在相同上下文下更优的动作计划。

#### 实验结果分析

作者在 NQ、WoW 和 2WikiMultiHopQA 三个 QA 基准上评估 RePAIR，并与 vanilla RAG、Self-Refine、FLARE、Self-RAG、MetaRAG、RAG-Critic 等方法比较，评价指标为 token-level F1。结果显示，RePAIR 在三个数据集上整体最强，平均 F1 比标准 RAG 提升 3.8 个点，并优于所有基于 critic 的 agentic RAG 方法；同时在 NQ 和 2Wiki 上取得最佳结果，在 WoW 上取得第二名。消融结果表明，单独使用 off-policy 或 on-policy 都不如完整的两阶段训练，说明两阶段设计对稳定性与部署一致性都很重要。

<details>
<summary>完整摘要</summary>

检索增强生成（RAG）通过将生成过程锚定在外部知识上，提高了大语言模型（LLM）输出的事实准确性。近年来，agentic RAG 系统进一步扩展了这一范式，引入 critic 代理来评估模型响应并迭代式地细化输出。然而，现有大多数工作都隐含地假设 critic 反馈是可靠的，并主要关注规划策略，而对错误纠正过程本身的鲁棒性关注不足；这一过程可能受到错误类别不对齐以及纠正措施无效或错误的影响。基于此，我们提出一个假设：RAG 的性能可以在不显式进行错误分类的情况下得到提升。为验证这一点，我们提出 RePAIR，一种 response-action learning 范式，它直接将有缺陷的 RAG 输出映射为可缓解错误的动作计划，而不依赖细粒度的错误 taxonomy 和显式 critic 监督。在多个基准上，RePAIR 都能持续提升 agentic RAG 的性能。

</details>

---
