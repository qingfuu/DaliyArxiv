# cs.RO | Robotics | 2026-05-22

#arxiv #ComputerScience

**论文数**: 25

### [[20_Research/Papers/强化学习/N3P_Accelerated_Automated_Parking_via_a_Learning-Based_Naturalistic_Three-Stage_Scheme|N3P: Accelerated Automated Parking via a Learning-Based Naturalistic Three-Stage Scheme]]

![[assets/2605.22722_figure.png|800]]

- **arXiv**: [2605.22722](https://arxiv.org/abs/2605.22722)
- **PDF**: https://arxiv.org/pdf/2605.22722
- **详细分析**: [[20_Research/Papers/强化学习/N3P_Accelerated_Automated_Parking_via_a_Learning-Based_Naturalistic_Three-Stage_Scheme|N3P: Accelerated Automated Parking via a Learning-Based Naturalistic Three-Stage Scheme]]
- **作者**: Yifan Xue, Toktam Mohammadnejad, Faizan M Tariq, Sangjae Bae, David Isele, Yosuke Sakamoto, Nadia Figueroa, Jovin D'sa
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.0（加权：具身智能 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: Agent, RL

#### 研究背景与动机

自动泊车需要在狭窄、复杂且充满障碍物的环境中生成既满足车辆运动学约束、又能避障的路径，这在真实停车场景中非常考验规划效率与可靠性。现有广泛使用的 Hybrid A* 虽然稳健，但计算开销较高，往往难以满足低时延需求；而强化学习方法虽然推理快，却容易受训练分布限制，在长时程几何约束下不够可靠，容易产生次优轨迹。本文之所以值得关注，是因为它试图把“人类司机先找一个中间准备位再完成泊车”的自然策略引入自动规划，从而在保证可行性的同时显著加速泊车。

#### 方法概述和架构

论文提出 N3P（Naturalistic Three-Stage Parking）三阶段泊车框架，把复杂泊车拆解为“准备—接近—泊入”三个子问题。第一步先对停车环境做抽象，只保留与动作选择最相关的几何信息，包括车道宽度、车位宽度、死胡同深度以及泊车类型等，以减少环境多样性带来的建模难度。第二步使用离线学习得到的 preparatory pose selector，根据抽象后的环境预测一个中间准备位，该准备位既要能从当前初始状态到达，又要便于后续与目标车位之间形成平滑连接。第三步在在线执行时，先用图搜索或优化式规划器（文中重点集成 Hybrid A*）从当前位姿规划到准备位，再用解析的 Reeds-Shepp 路径从准备位直接泊入最终目标位姿。整体上，N3P 不是完全端到端生成整条路径，而是把学习模块用于“选中间位”，把传统规划器保留在关键的可行性与安全性环节，从而兼顾速度与可靠性。

#### 实验结果分析

作者在垂直泊车和平行泊车场景中，将 N3P 与 Hybrid A* 结合，并与若干 Hybrid A* 变体以及基于 Transformer 的 RL 基线 HOPE 进行比较。实验表明，加入 N3P 后的 Hybrid A* 规划速度提升超过 80%，同时在成功率和轨迹质量上优于 RL 基线，生成的路径更短、换挡次数更少。论文还指出，在多数情况下，该方法的规划时间可与基线相当或更低；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

自动泊车需要在受限环境中进行高效路径规划，同时保证车辆运动学可行性并避免碰撞。Hybrid A* 被广泛采用，但计算开销较大；强化学习（RL）方法则缺乏可靠性，并且常常难以处理长时程的几何约束，导致轨迹次优。我们提出 N3P，一种快速的、基于学习的三阶段自动泊车框架。通过引入一个中间的准备位，并利用学习模块预测该准备位，N3P 将泊车动作分解为更简单的子问题，从而降低计算复杂度并加速路径生成。我们通过将该框架与 Hybrid A* 算法结合进行验证。对垂直泊车和水平泊车场景的实验表明，N3P 增强的 Hybrid A* 规划速度提升超过 80%。与 RL 基线相比，它在成功率和轨迹质量方面也更优，生成的轨迹更短、换挡次数更少，并且在大多数情况下实现了相当或更低的规划时间。

</details>

---

### [[20_Research/Papers/机器人/TriSweep_A_Four-Drone_Swarm_Framework_for_Electromagnetic_Side-Channel_Analysis|TriSweep: A Four-Drone Swarm Framework for Electromagnetic Side-Channel Analysis]]

![[assets/2605.22709_figure.png|800]]

- **arXiv**: [2605.22709](https://arxiv.org/abs/2605.22709)
- **PDF**: https://arxiv.org/pdf/2605.22709
- **详细分析**: [[20_Research/Papers/机器人/TriSweep_A_Four-Drone_Swarm_Framework_for_Electromagnetic_Side-Channel_Analysis|TriSweep: A Four-Drone Swarm Framework for Electromagnetic Side-Channel Analysis]]
- **作者**: Eric Yocam, Varghese Vaidyan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

传统电磁侧信道分析通常默认攻击者需要将探头贴近目标设备，这一假设低估了空中平台带来的新威胁。随着小型无人机、低成本软件无线电和轻量化低噪声前端的普及，攻击者有可能在0.25–1.5 m的悬停距离内对嵌入式微控制器实施非接触式窃听。论文关注的核心问题是：如何利用多无人机协同，把原本依赖近距离探头的EM侧信道分析扩展到远距离、非接触、且面向遮蔽实现的攻击场景。

#### 方法概述和架构

TriSweep 是一个面向EM侧信道分析的四无人机仿真框架：Drone A（Anchor）负责全频段观测，Drone B（Mask Probe）专门采集掩码寄存器装载泄漏，Drone C（Cipher Probe）专门采集掩码后的 SubBytes 输出泄漏，Drone D（Accumulator）则在地面/静止位置汇聚三路信息并完成后续分析。系统先通过目标检测与定位、协同重定位和时钟同步，使三架采集无人机在空间与时间上对齐到可组合的状态；随后 Drone D 对多路 IQ 信号进行相干叠加，以获得约4.8 dB 的信噪比增益。针对第一阶掩码防护，框架进一步对 B、C 两路泄漏做居中乘积，实现二阶掩码抵消，从而把分散在不同时间窗口的泄漏事件转化为可联合利用的特征。实验流程上，作者使用ASCAD公开数据集做离线剖面训练，并在仿真中结合自由空间路径损耗与噪声模型评估不同悬停距离、不同抖动条件下的攻击效果；此外还引入基于交叉相关的轨迹对齐，以缓解无人机悬停振动造成的时间偏移。

#### 实验结果分析

论文在三套真实 ANSSI ASCAD 数据集上评估了 TriSweep，包括 ATmega8515 的 masked AES-128 以及 50/100-sample 去同步变体。结果显示，在主数据集、0.25 m 悬停距离下，四无人机系统的模拟 key rank 达到 18±1.7（五次随机种子统计），相比单无人机基线有显著改善。对于 100-sample 抖动变体，使用剖面轨迹交叉相关对齐后，单无人机 rank 从 89 降至 21，说明该方法能抵消一定程度的悬停振动影响。作者还报告 Drone D 上的两通道 CNN 收敛到 0.454 的损失，明显优于随机基线 5.545，并且在去同步数据集上进一步提升了排名表现。

<details>
<summary>完整摘要</summary>

电磁（EM）侧信道分析传统上默认攻击者使用静止、近距离探头，这一威胁模型低估了空中对手的能力。TriSweep 是一个仿真框架，用于设计并评估一种四无人机蜂群架构，在0.25–1.5 m距离上对嵌入式微控制器实施自主、远距离的EM侧信道分析。三个具有空间分工的采集无人机——Anchor（全频段采集）、Mask Probe（采集掩码寄存器装载泄漏）和Cipher Probe（采集掩码后的 SubBytes 输出泄漏）——将数据传送给一架静止的 Accumulator 无人机；后者执行相干合并（带来+4.8 dB 的SNR增益），并通过对两路空间分离泄漏流的居中乘积实现二阶掩码抵消。作者使用三套真实的 ANSSI ASCAD 数据集进行评估，包括 ATmega8515 masked AES-128 以及 50/100-sample 的去同步变体。结果表明，该框架在主 masked 数据集、0.25 m 距离下可达到模拟 key rank 18±1.7（五次种子统计）。通过剖面轨迹的交叉相关对齐，100-sample 抖动变体上的单无人机排名可从89降至21，说明该方法能够补偿无人机悬停振动带来的影响。Accumulator 中的双通道 CNN 收敛到0.454的损失（而随机基线为5.545），并提升了去同步数据集上的排名。需要说明的是，本文尚未制造任何实体硬件，原型构建是下一步计划。

</details>

---

### [[20_Research/Papers/机器人/Symmetries_Here_and_There,_Combined_Everywhere_Cross-space_Symmetry_Compositions_in_Robotics|Symmetries Here and There, Combined Everywhere: Cross-space Symmetry Compositions in Robotics]]

![[assets/2605.22639_figure.png|800]]

- **arXiv**: [2605.22639](https://arxiv.org/abs/2605.22639)
- **PDF**: https://arxiv.org/pdf/2605.22639
- **详细分析**: [[20_Research/Papers/机器人/Symmetries_Here_and_There,_Combined_Everywhere_Cross-space_Symmetry_Compositions_in_Robotics|Symmetries Here and There, Combined Everywhere: Cross-space Symmetry Compositions in Robotics]]
- **作者**: Loizos Hadjiloizou, Rodrigo Pérez-Dattari, Noémie Jaquier
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

机器人在机械结构和任务设定上往往同时存在多种对称性，例如双臂互换、场景旋转、任务目标等价等。这些对称性如果被正确利用，可以让策略从少量样本推广到更大范围的等价状态，从而提升样本效率和泛化能力。现有方法通常只处理单一空间中的单一种对称性，未能把配置空间和任务空间中的对称性联合起来建模，因此在复杂操作任务中仍存在泛化不足的问题。

#### 方法概述和架构

本文提出 cross-space symmetry compositions，用于学习同时对多个对称性保持等变的机器人策略。方法的核心是利用前向运动学映射的微分几何结构，在配置空间与任务空间之间传递对称性：一方面把配置空间中的对称性“下传”到任务空间，另一方面把任务空间中的对称性“上提”到配置空间。作者将这一过程表述为群作用、等变性以及黎曼子浸没条件下的统一建模问题，并据此构建可在公共表示空间中组合多个对称性的表示。随后，这些被转移到同一空间的对称性可以通过直积或半直积进行系统组合，从而形成对策略网络或控制策略的联合等变约束。整体流程是：先识别机器人结构与任务中的对称性，再判断其是否能经由前向运动学转移，最后在统一空间中完成组合并用于策略学习。

#### 实验结果分析

作者在仿真与真实机器人实验中验证了该框架，实验对象是双臂机器人，任务包括仿真中的字母绘制以及真实世界操作。对比结果表明，将多种对称性联合利用后，策略的泛化能力优于只利用单一对称性的基线。正文节选中未给出具体数值，但结论明确指出：同时编码结构对称性与任务对称性，能在未见过的旋转、反射及其组合变化下保持更稳定的执行能力。

<details>
<summary>完整摘要</summary>

机器人在其机械结构和任务性质上会呈现出丰富多样的对称性。尽管许多机器人问题同时包含多种对称性，现有方法通常将它们分开处理，未能发挥其组合带来的潜力。本文提出 cross-space symmetry compositions，一种用于学习机器人策略的框架，使策略能够在配置空间和任务空间中同时对多个对称性保持等变。借助前向运动学映射的微分几何结构，我们既可以把对称性从配置空间传递到任务空间，也可以把对称性从任务空间提升到配置空间，从而使这些对称性能够在统一表示空间中进行组合。我们在双臂机器人上的仿真与真实世界实验中验证了该框架，结果表明，联合利用多个对称性可以带来更好的泛化能力。

</details>

---

### [[20_Research/Papers/机器人/SE3Kit_A_Lightweight_Python_Library_for_Specialized_Geometric_Primitives_in_Robotics|SE3Kit: A Lightweight Python Library for Specialized Geometric Primitives in Robotics]]

![[assets/2605.22633_first_page.png|800]]

- **arXiv**: [2605.22633](https://arxiv.org/abs/2605.22633)
- **PDF**: https://arxiv.org/pdf/2605.22633
- **详细分析**: [[20_Research/Papers/机器人/SE3Kit_A_Lightweight_Python_Library_for_Specialized_Geometric_Primitives_in_Robotics|SE3Kit: A Lightweight Python Library for Specialized Geometric Primitives in Robotics]]
- **作者**: Daniyal Maroufi, Omid Rezayof, Farshid Alambeigi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

机器人软件生态中，刚体位姿与坐标变换库很多，但同时满足“轻量”和“数学上严格”的工具却很少。对于嵌入式控制、快速原型验证和教学场景，PyTorch 依赖过重的 PyPose、SpatialMath 这类框架，以及面向通用科学计算但缺少机器人语义的 SciPy，都存在不够贴合的问题。作者认为，机器人在处理 SE(3) 与 SO(3) 这类几何原语时，需要一个依赖极少、又能严格遵守流形与李群数学性质的专用库，因此提出 SE3Kit。

#### 方法概述和架构

SE3Kit 是一个纯 Python、仅依赖 NumPy 的机器人几何原语库，面向 SE(3) 和 SO(3) 上的高效运算。其核心模块包括统一的姿态表示接口，可在旋转矩阵、四元数与欧拉角之间一致转换，并显式处理四元数标量前/标量后等常见歧义。库中还实现了李群/李代数运算，特别是指数映射与对数映射，用于速度、力螺旋等向量在不同坐标系之间的转换与优化。与此同时，SE3Kit在内部强制流形约束，避免旋转矩阵因数值误差偏离正交性，从而适合确定性机器人流程。整体上，它将核心几何操作封装为轻量级组件，输入为常见位姿与帧变换数据，输出为满足 SE(3)/SO(3) 约束的几何结果。

#### 实验结果分析

论文主要通过生态对比和需求分析说明 SE3Kit 的定位，而不是给出大规模基准测试；可见文本未给出具体数值。作者将其与 SciPy、SpatialMath、PyPose、tf2_py 和 transformations.py 等工具比较，强调 SE3Kit 在依赖规模、部署体积、数学范围和机器人专用功能上的折中更适合嵌入式与研究场景。文中还指出，该库已经被若干机器人与医疗机器人相关研究工作使用，说明其具备实际项目中的可用性与复用价值。

<details>
<summary>完整摘要</summary>

Python 机器人生态面临一个问题：虽然有很多用于刚体变换的库，但真正同时满足轻量化与数学严格性的库却很少。本文提出 SE3Kit，一个轻量级 Python 库，用于在特殊欧几里得群 SE(3) 和特殊正交群 SO(3) 上进行高效运算。与现有框架不同，像 SpatialMath、PyPose 这类库通常需要较重的依赖链，而 SciPy 这类通用工具又缺少机器人领域特有的功能；SE3Kit 正是为了填补两者之间的空白而设计。它面向嵌入式部署、快速原型开发和教育应用，同时保持严格的数学实现。SE3Kit 提供纯 Python、仅依赖 NumPy 的李群运算实现，不引入深度学习或可视化软件带来的额外开销。

</details>

---

### [[20_Research/Papers/机器人/Branch-Stochastic_Model_Predictive_Control_for_Motion_Planning_under_Multi-Modal_Uncertainty_with_Scenario_Clustering|Branch-Stochastic Model Predictive Control for Motion Planning under Multi-Modal Uncertainty with Scenario Clustering]]

![[assets/2605.22600_first_page.png|800]]

- **arXiv**: [2605.22600](https://arxiv.org/abs/2605.22600)
- **PDF**: https://arxiv.org/pdf/2605.22600
- **详细分析**: [[20_Research/Papers/机器人/Branch-Stochastic_Model_Predictive_Control_for_Motion_Planning_under_Multi-Modal_Uncertainty_with_Scenario_Clustering|Branch-Stochastic Model Predictive Control for Motion Planning under Multi-Modal Uncertainty with Scenario Clustering]]
- **作者**: Zekun Xing, Ramkrishna Chaudhari, Marion Leibold, Dirk Wollherr, Martin Buss
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

自动驾驶中的运动规划需要同时处理周围车辆在“意图层面”和“轨迹层面”的多模态不确定性，例如同一辆车可能左转、直行或并线，而每种意图下的具体轨迹又存在随机波动。现有最坏情况鲁棒方法虽然安全，但往往过于保守；SMPC能够通过机会约束降低对轨迹不确定性的保守性，但对意图不确定性仍然要求跨所有意图都满足约束，因此依旧偏保守。对于多车高速场景来说，这种保守性和场景组合爆炸会显著拖慢求解速度，因此如何兼顾安全、实时性与不过度保守，是这篇工作值得关注的核心问题。

#### 方法概述和架构

论文提出 Branch-Stochastic Model Predictive Control（B-SMPC）框架，将SMPC与分支式规划结构结合：先用BMPC式的分支结构表示不同周围车辆意图对应的多条候选规划，再在每条分支上用机会约束显式处理轨迹不确定性。具体来说，输入为多模态轨迹预测器给出的各车辆多个预测模式及其概率、名义轨迹和协方差，输出为AV在有限时域内的可执行控制序列与对应分支轨迹。为控制多车场景下的组合复杂度，作者设计了基于高层机动规划的场景聚类：先为每个场景用轻量级机动规划器生成高层机动（包括目标车速与目标横向位置），再将产生相似机动决策的场景合并成簇，从而减少分支数量。与此同时，论文还提出基于DTW距离的自适应分支时刻计算，用场景相似度来决定何时从共享控制切换为分支控制，把“何时承诺到单一路径”的时机推迟到意图不确定性足够降低之后。整体流程是：多模态预测→场景组合→聚类压缩→机会约束优化→在线滚动重规划。

#### 实验结果分析

作者在具有挑战性的高速公路仿真场景中验证了方法效果，重点比较了安全性、保守性和实时计算性能。实验表明，所提B-SMPC相较于基线方法能够更安全地处理多模态不确定性，同时减少不必要的保守行为，并且保持实时可用的求解速度。可见文本未给出具体数值，但节选显示论文还进行了定性与定量分析，以及与不同场景处理策略的对比和消融。

<details>
<summary>完整摘要</summary>

自动驾驶的运动规划必须同时考虑周围车辆在意图和轨迹两个层面上的多模态不确定性。以最坏情况方式处理不确定性可以保证鲁棒性，但往往会带来过度保守。Stochastic Model Predictive Control（SMPC）通过机会约束降低了轨迹层面的保守性，但在意图不确定性上仍然保守，因为约束必须对所有意图都成立。本文提出一种将SMPC与分支结构相结合的新方法，使规划器能够针对不同的可能意图生成不同轨迹，同时在轨迹不确定性下保持安全。我们进一步提出一种新的场景聚类方法，依据高层决策相似性合并预测场景，从而保证实时可计算性。此外，本文还提出自适应分支时刻计算，在意图不确定性尚未充分减小时推迟分支决策。针对具有挑战性的高速公路场景的仿真研究表明，所提方法提升了安全性，降低了保守性，并实现了实时计算性能。

</details>

---

### [[20_Research/Papers/机器人/Quantifying_Full-Body_Immersion|Quantifying Full-Body Immersion]]

![[assets/2605.22521_figure.png|800]]

- **arXiv**: [2605.22521](https://arxiv.org/abs/2605.22521)
- **PDF**: https://arxiv.org/pdf/2605.22521
- **详细分析**: [[20_Research/Papers/机器人/Quantifying_Full-Body_Immersion|Quantifying Full-Body Immersion]]
- **作者**: Alihan Bakir, Ekrem Yüksel, Fabio Zuliani, Neil Chennoufi, Francesco Bruno, Jamie Paik
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

虚拟现实和具身交互正在从“看见和听见”走向“身体参与”，但现有系统大多只覆盖视听沉浸或局部触觉，难以把整个人体的运动、受力与环境动态统一起来。对于滑雪、划船、远程操控、共享仿真等任务，单点式触觉设备在尺度、可扩展性和多用户协同方面都存在明显瓶颈。该论文关注的核心问题是：如何把“全身参与”的沉浸体验变成可测量、可比较、可扩展的工程系统，因此具有较强的机器人与具身智能交叉价值。

#### 方法概述和架构

论文提出 MIROS（Multi-scale Interactive Reconfigurable Origami Surface）平台，用模块化机器人表面单元构建可扩展的全身沉浸环境。系统从三个层次定义沉浸：视听沉浸、物理沉浸和全身沉浸（FBI），其中 FBI 通过平台在空间中分布式地输出力、形状和运动反馈，让用户身体与虚拟环境发生动态耦合。每个 MIROS 模块具有 3 自由度，采用分层控制结构：底层通过编码器、力/电流等反馈闭环控制执行器，上层将真实动作或虚拟角色的加速度、位置和姿态映射为平台的参考指令。论文还设计了两种工作模式：一是“反馈渲染”，把真实或模拟运动转成平台运动以复现物理事件；二是“交互模式”，用户对平台施力，系统据此计算虚拟环境响应并再反馈给用户。为量化 FBI，作者提出一个与任务无关的平台级沉浸指数，基于真实场景、无物理反馈仿真和带 MIROS 反馈的条件下，提取活动相关子指标的四分位范围，构造雷达图多边形，再用其对应的质心和回转半径形成等效回转圆，最后用交并比定义沉浸度。

#### 实验结果分析

论文在滑雪和划船两类实验中验证方法：前者代表高加速度动态，后者代表较平缓的姿态变化；实验包括真实动作、无反馈仿真和 MIROS 平台反馈三种条件。结果表明，平台能较好跟踪所需加速度信号，并使用户动作更接近真实场景，例如在滑雪任务中，使用平台时的重心轨迹和膝关节变化更符合真实滑雪特征。作者据此说明其沉浸指数能够区分不同反馈条件下的身体行为差异。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

人类正处在又一次数字革命的前沿，现实世界与虚拟世界之间的界限正在消融，这正在重塑我们感知和与周围环境交互的方式。在这一背景下，我们提出一种面向沉浸式虚拟体验的变革性范式，其核心是全身动力学交互。我们的方案将沉浸重新定义为三个不同层次：视听沉浸，用于捕捉感官真实感；物理沉浸，提供触觉反馈；以及全身沉浸（FBI），使动态的身体交互能够无缝融入虚拟环境。该创新的核心是一个可扩展、可分布式的平台，它基于受自然自适应设计启发的模块化机器人表面单元。这些单元能够在任意尺度上渲染沉浸式环境，从私密的个人体验到大规模的多人场景，并可在实时交互中动态适应用户行为。该模块化系统将力、形状和运动反馈分布到整个空间中，复制环境的物理特性，并通过 FBI 带来更深层次的参与感。通过结合可扩展性、适应性和动态物理交互，这一框架弥合了现实与虚拟之间的鸿沟。它提供了一种前所未有的沉浸程度，使用户能够以全身参与的方式与虚拟空间进行共生式交互。这项工作不仅推进了沉浸式技术的发展，也重新定义了人类与虚拟环境的共存方式，为人—环境融合的新纪元奠定了基础。

</details>

---

### [[20_Research/Papers/机器人/Terminal_Constraint_Model_Predictive_Control_for_Image-Based_Visual_Servoing_of_UAVs_with_Kalman_Filter-Based_Moment_Loss_Compensation|Terminal Constraint Model Predictive Control for Image-Based Visual Servoing of UAVs with Kalman Filter-Based Moment Loss Compensation]]

![[assets/2605.22443_figure.png|800]]

- **arXiv**: [2605.22443](https://arxiv.org/abs/2605.22443)
- **PDF**: https://arxiv.org/pdf/2605.22443
- **详细分析**: [[20_Research/Papers/机器人/Terminal_Constraint_Model_Predictive_Control_for_Image-Based_Visual_Servoing_of_UAVs_with_Kalman_Filter-Based_Moment_Loss_Compensation|Terminal Constraint Model Predictive Control for Image-Based Visual Servoing of UAVs with Kalman Filter-Based Moment Loss Compensation]]
- **作者**: X. Wang, Y. Cao, W. L. W. Leong, Y. R. Tan, S. Huang, S. H. R. Teo, C. Xiang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: ComputerVision

#### 研究背景与动机

这篇论文面向无人机的图像引导控制任务，尤其是室内、林地和城市峡谷等 GPS 不稳定或不可用环境下的自主导航与穿越。作者指出，传统 IBVS 虽然能直接在图像平面上做闭环控制，但在接近目标时容易受到输入和状态约束影响而失去稳定性；在大机动飞行中，基于图像矩的视觉特征还可能出现间歇性丢失，导致控制中断。因此，如何在满足物理约束的同时保持视觉伺服的连续性与稳定性，是这项工作要解决的核心问题。

#### 方法概述和架构

论文提出了一个用于 IBVS 的 Terminal Constraint Model Predictive Control（TC-MPC）框架，并结合基于 Kalman filter 的图像矩预测补偿机制。方法首先将图像矩构造为视觉状态，建立其与无人机机体速度和偏航角速度之间的离散线性化误差动力学，并在 MPC 中显式优化未来多个时刻的视觉误差和控制量。随后，优化目标加入终端代价与终端状态约束，用以增强递推可行性、收敛性和闭环稳定性，同时把相机视场约束与无人机速度/角速度上限统一写入约束条件。另一方面，当图像因模糊、遮挡或快速运动导致部分矩特征短时缺失时，Kalman filter 会根据历史观测预测视觉状态，从而为 MPC 提供连续的状态输入并维持控制链路。在线执行时，系统在每个采样周期更新状态、构建二次规划并由 Gurobi 求解，取最优控制序列的首个控制量下发给 PX4 飞控。

#### 实验结果分析

论文在真实时间的无人机视觉伺服实验中验证了方法有效性，场景包括四旋翼的视觉伺服与自主门穿越任务。对比基线和消融分析在节选中未完整展开，因此可见文本未给出具体数值，但作者明确声称该方法能够在约束条件下保持更好的收敛行为和闭环稳定性，并在视觉特征短时丢失时维持控制连续性。实验结果支持了终端约束 MPC 结合 Kalman filter 的设计在真实飞行中的实用性。

<details>
<summary>完整摘要</summary>

图像式视觉伺服（IBVS）通过直接调节图像空间误差，为无人机提供了一种高效的视觉引导控制范式。然而，传统 IBVS 控制器容易受到两个关键问题的影响：一是在输入和状态约束下，接近目标时闭环稳定性会下降；二是在激烈机动时，基于图像矩的视觉特征可能间歇性丢失，从而导致控制失效。为解决这些挑战，本文提出了一种用于 IBVS 的终端约束模型预测控制（TC-MPC）框架，并结合基于 Kalman filter（KF）的状态预测机制。TC-MPC 将终端状态约束和终端代价显式引入 IBVS 误差动力学之中，从而在控制和状态约束下保证递推可行性、改善收敛行为并提升闭环稳定性。与此同时，Kalman filter 在短时视觉退化期间预测图像矩的时序演化，使控制器在部分矩测量不可用时仍能保持控制连续性。所提出的方法已通过实时无人机视觉伺服实验得到验证。

</details>

---

### [[20_Research/Papers/具身智能/How_can_reasoning_capability_empower_the_AI_copilot_robot_in_endoscopic_surgery|How can reasoning capability empower the AI copilot robot in endoscopic surgery]]

![[assets/2605.22322_figure.png|800]]

- **arXiv**: [2605.22322](https://arxiv.org/abs/2605.22322)
- **PDF**: https://arxiv.org/pdf/2605.22322
- **详细分析**: [[20_Research/Papers/具身智能/How_can_reasoning_capability_empower_the_AI_copilot_robot_in_endoscopic_surgery|How can reasoning capability empower the AI copilot robot in endoscopic surgery]]
- **作者**: Guankun Wang, Long Bai, Hongliang Ren
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.9，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

本文聚焦内镜手术中的AI copilot机器人，尤其是基于 Vision-Language-Action（VLA）模型的术中辅助决策与动作生成问题。与通用机器人不同，内镜手术面临软组织形变不可预测、视野受血液或烟雾遮挡、多器械协同复杂以及术者认知负担高等挑战，使得仅依赖模式匹配的策略难以稳定工作。作者指出，若能将“推理能力”引入AI copilot，机器人就有望从被动执行者转变为能理解手术意图、融合多模态线索并推断组织动态的认知协作者，因此具有较强的研究价值。

#### 方法概述和架构

这篇文章本质上是一篇面向内镜手术AI copilot的观点/综述型论文，围绕“推理增强VLA”提出系统性设计思路。作者将AI copilot定义为处于 LoA 2-3 的任务级/监督式自治助手，并用 Generate、Execute、Monitor、Select 四个 DoA 功能来刻画其能力边界：系统在术者监督下生成低层运动目标、监测组织与工具状态、执行受安全约束的局部动作，并仅在预设安全边界内做有限选择。方法上强调多模态感知与不确定性感知融合：将术前 CT/MRI、术中 EUS/OCT、形状感知、EM 跟踪和力代理等信息与内镜视频结合，构建概率化的手术环境表征，在遮挡或风险变化时动态调整各模态权重。进一步地，作者提出推理驱动的 VLA 结构：第一个 VLA 模型根据高层语言指令和手术视频进行多步推理，输出与场景对齐的低层机器人运动目标；这些推理结果再与额外多模态信息一起输入第二个 VLA 模型，由其作为运动策略专家，将目标转化为具体的位姿、速度等运动学变化。论文还讨论了链式推理、反思式学习和强化学习式适应如何帮助模型在术中持续修正判断，并将不确定性传播到更保守、更可解释的动作约束中。

#### 实验结果分析

由于该文为综述与前瞻性分析，节选文本中没有给出统一的实验指标、具体数值结果或完整基准对比，因此可见文本未给出具体数值。作者主要通过若干代表性任务场景说明推理能力的价值，例如内镜黏膜下剥离中的牵引-剥离协同、止血过程中的出血点定位与双器械协作、以及在血液/烟雾遮挡下的风险推断。文中同时指出，推理增强可提升复杂场景下的泛化、鲁棒性和不确定性处理能力，但其部署仍受实时性、边缘算力和可靠性验证约束。

<details>
<summary>完整摘要</summary>

推理能力已显著推动通用领域中的复杂逻辑推断与机器人决策。然而，其在人工智能（AI）copilot机器人中的潜力，尤其是在基于 Vision-Language-Action（VLA）模型实现的内镜手术场景中，仍未被充分探索。有效的推理应当使AI copilot机器人能够整合多模态线索、理解手术意图，并推断隐藏的组织动态，从而减轻术中的不确定性以及外科医生的认知负担。若实现得当，推理驱动的自治能力可将AI copilot机器人从被动执行者转变为认知协作者，在临床实践中提升精度、安全性与可持续性。

</details>

---

### [[20_Research/Papers/具身智能/Spatial_Memory_for_Out-of-Vision_Manipulation_in_Vision-Language-Action|Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action]]

![[assets/2605.22283_figure.png|800]]

- **arXiv**: [2605.22283](https://arxiv.org/abs/2605.22283)
- **PDF**: https://arxiv.org/pdf/2605.22283
- **详细分析**: [[20_Research/Papers/具身智能/Spatial_Memory_for_Out-of-Vision_Manipulation_in_Vision-Language-Action|Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action]]
- **作者**: Pengteng Li, Weiyu Guo, He Zhang, Tiefu Cai, Xiao He, Yandong Guo, Hui Xiong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 2.1，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

在视觉-语言-动作（VLA）机器人中，很多方法默认任务相关物体始终处于相机视野内，因此一旦目标移出当前画面，就容易退化为被动、脆弱的反应式行为。这个问题在真实操作中非常常见，例如目标物体被遮挡、机器人头部转动后暂时离开视野，或需要多步、双臂协同去寻找并抓取初始不可见的物体。本文值得关注之处在于，它直接针对“视野外操控（out-of-vision manipulation）”这一当前VLA系统的结构性短板，尝试让机器人具备跨视角、可持续的空间记忆。

#### 方法概述和架构

论文提出 SOMA（Spatial Memory for Out-of-Vision Manipulation），核心思想是把机器人感知从“当前帧驱动”改造成“记忆驱动”。首先在 Spatial Memory Construction 阶段，机器人用可移动头部相机对场景进行扫描，结合目标检测、视觉特征提取和几何先验，把多视角观测融合为统一的空间-语义记忆。随后在 Dynamic Memory Refinement 阶段，系统在交互过程中持续吸收新观测，并通过相似度加权融合保持全局一致性，避免记忆随时间漂移或失真。最后在 Contextual Memory Retrieval 阶段，模型根据语言指令从空间记忆中检索与任务相关的区域，并把这些上下文线索送入基于 DiT 的动作解码器生成可执行动作。整体流程中，输入包括当前观测、机器人状态、语言指令和噪声动作序列，输出是面向下一步操控的动作片段；在目标初始不可见时，系统会先主动扫描建图，再进入带记忆的操作阶段。

#### 实验结果分析

作者在5个自设计的真实世界视野外操控任务上评估了 SOMA，任务包含多步操作和双臂场景，目标物体在初始时不可见。实验表明，SOMA 不仅提升了任务成功率，还带来了更不同的操作行为模式，例如更快定位目标、更少的视角搜索，以及在部分可观测条件下接近一次抓取成功。论文还在 RoboCasa GR1 和 SimplerEnv 上做了补充实验，验证了该记忆设计在传统完全可观测设置下的有效性。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

我们提出 SOMA，即用于 Vision-Language-Action（VLA）模型的空间记忆框架，面向视野外操控（out-of-vision manipulation）。现有大多数 VLA 隐式地假设任务相关物体始终可见，一旦目标离开相机视野，系统就会表现得脆弱且偏向反应式。SOMA 通过为 VLA 配备一种持久的空间记忆来解决这一局限，该记忆由可移动头部相机获取的多视角观测构建而成，从而使模型能够超越当前视觉视锥进行推理。该框架由三个部分组成：空间记忆构建（Spatial Memory Construction），通过扫描将角度维度上的观测聚合为统一的空间-语义表示；动态记忆细化（Dynamic Memory Refinement），用于维持随时间变化的全局一致性；以及上下文记忆检索（Contextual Memory Retrieval），在操控过程中激活与指令相关的空间线索。我们在5个具有挑战性的真实世界视野外操控任务上评估 SOMA，这些任务包括多步和双臂场景，且目标物体在初始时不可见。实验结果表明，SOMA 不仅提升了任务成功率，还诱导出定性上不同的操控行为：在部分可观测条件下，目标定位更快、视角搜索更少，并且几乎可以一次性完成抓取。进一步在 RoboCasa GR1 和 SimplerEnv 上的实验也验证了 SOMA 的记忆设计在常规完全可观测设置下同样有效。代码将很快公开。

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Pixels_Learning_Invariant_Rewards_for_Real-World_Robotics_From_a_Few_Demonstrations|Beyond Pixels: Learning Invariant Rewards for Real-World Robotics From a Few Demonstrations]]

![[assets/2605.22123_figure.png|800]]

- **arXiv**: [2605.22123](https://arxiv.org/abs/2605.22123)
- **PDF**: https://arxiv.org/pdf/2605.22123
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Pixels_Learning_Invariant_Rewards_for_Real-World_Robotics_From_a_Few_Demonstrations|Beyond Pixels: Learning Invariant Rewards for Real-World Robotics From a Few Demonstrations]]
- **作者**: Tengye Xu, Yangting Sun, Ziju Shen, Guanqi Chen, Zhen Fu, Chen yizhou, Hua Chen, Jia Pan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

在真实机器人操作中，奖励函数往往需要适应物体实例、摆放位置和相机视角的频繁变化，但现有基于视觉的奖励模型容易记住训练时的像素分布，离开实验室设定后就难以泛化。对于开世界操作任务来说，如何只凭少量示范就学到既能提供稠密引导、又不会改变原任务最优策略的奖励函数，是具身智能与强化学习中的关键难题。本文关注的正是这一点：从少量演示中提炼出任务层面的不变性，而不是对表面视觉特征做拟合，因此具有较强的现实应用价值。

#### 方法概述和架构

论文提出 FLORA（Flow-based Language-driven Offline Reward Adaptation）框架，用于从最少五个示范中学习不变的符号化奖励函数。整体方法由三部分组成：Flow-Generator 先从原始图像中提取与任务相关的运动流，作为比像素更稳健的状态表征；符号潜势函数在此基础上刻画任务进度、阶段结构与物理约束；PBRS-MS 模块则将该潜势函数转化为基于潜势的奖励塑形信号，以保证最优策略不变，避免 reward hacking。训练流程是离线完成的：外层通过 LLM 反思来搜索离散的程序结构，内层用 Bayesian Optimization 优化连续参数，二者构成混合符号-数值的双层优化。推理时，模型直接从实时图像流输出稠密奖励，可用于后续强化学习。

#### 实验结果分析

作者在 8 个 Meta-World 任务和 3 个 Franka 操作任务上验证了方法的有效性，重点比较了过程对齐能力和策略 rollout 排序能力；相较基线，FLORA 表现更强，可见文本未给出具体数值。进一步在三个真实世界的分布外实验中，学到的同一个奖励函数能够零样本泛化到位置、视角和物体变化，说明其对开放世界任务具有较好的复用性。文中还做了消融实验，考察了 Flow-Generator、符号函数、示范数量、子任务标签、PBRS-MS 模块以及混合优化策略的贡献。

<details>
<summary>完整摘要</summary>

为机器人强化学习设计能够超越受控实验室环境的奖励函数，一直是一个根本性挑战。在开世界操作问题中，同一个任务可能因为物体实例、摆放位置和相机视角不同而呈现出大量变体。近期基于视觉的奖励模型往往会记住特定的像素分布，无法在训练条件之外泛化。为解决这一问题，我们提出一个框架，仅用少至五个示范即可学习具有不变性的符号奖励函数。其核心思想是从视觉特征拟合转向发现行为不变性：即在不同视觉呈现下保持不变的任务级属性。该框架包含两个相互耦合的组件：其一是结构化奖励建模，用于编码任务级策略和物理约束，同时保持最优策略不变性；其二是混合符号-数值过程，用于在无需在线交互的情况下，从示范中蒸馏这些不变性。我们在八个 Meta-World 任务和三个 Franka 操作任务上的实验表明，与基线相比，该方法在过程对齐和策略 rollout 排序能力上更强，并能加速下游策略学习。三个真实世界的分布外实验进一步表明，同一个学到的奖励可以零样本泛化到位置、视角和物体变化，从而使单一奖励表示能够在实践中复用于多种任务变体。

</details>

---

### [[20_Research/Papers/机器人/Industrial_Dual-Arm_Box_Handling_via_Online_Inertial_Estimation_and_Convex_Wrench_Optimization|Industrial Dual-Arm Box Handling via Online Inertial Estimation and Convex Wrench Optimization]]

![[assets/2605.22021_figure.png|800]]

- **arXiv**: [2605.22021](https://arxiv.org/abs/2605.22021)
- **PDF**: https://arxiv.org/pdf/2605.22021
- **详细分析**: [[20_Research/Papers/机器人/Industrial_Dual-Arm_Box_Handling_via_Online_Inertial_Estimation_and_Convex_Wrench_Optimization|Industrial Dual-Arm Box Handling via Online Inertial Estimation and Convex Wrench Optimization]]
- **作者**: Kenzhi Iskandar Wong, Lin Yang, Qian Ying Lee, Domenico Campolo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

在工业机器人箱体搬运中，箱子和包裹的质量、质心位置往往在作业前并不明确，但这些惯性参数会直接影响稳定起吊所需的力与力矩平衡。若接触力/力矩分配不当，容易出现打滑、掉落、姿态偏移或过度挤压等问题。相比依赖特定夹持条件的夹爪或吸盘，双臂摩擦搬运更适合多种包装场景，但也更依赖对接触wrench的精确调控，因此这项工作值得关注。

#### 方法概述和架构

论文提出了一套面向未知惯性参数箱体的双臂摩擦搬运框架，核心是“在线惯性估计 + 凸优化wrench分配 + 离线轨迹修正”。首先在离线阶段，作者用DMP和基于黑盒优化/CEM的仿真搜索对目标轨迹做细化，以尽量减少箱体与环境的非期望接触，同时保持接近示范轨迹。随后在在线阶段，通过测得的接触wrench与机器人运动学信息，逐步估计箱体质量和质心位置。最后将双臂接触力与扭矩分配写成带椭球形摩擦极限面约束的SOCP问题，在满足力矩平衡与摩擦可行性的前提下最小化接触代价；执行时再通过笛卡尔阻抗控制与wrench反馈把优化结果落地到真实机器人上。

#### 实验结果分析

作者在真实双臂机器人系统上进行了实验，覆盖不同质心配置的箱体搬运场景。结果表明，该方法能够在质量和质心未知的情况下完成稳定起吊，并保持摩擦接触稳定，避免滑移、掉落与过度挤压。正文节选中还强调了三维搬运时接触扭矩的重要性，以及离线轨迹修正对减少环境碰撞的作用；但可见文本未给出具体数值指标。

<details>
<summary>完整摘要</summary>

工业机器人物体搬运中经常需要处理箱子和包裹，而它们的质量和质心通常在事先并不知道。这些不确定性会影响稳定起吊所需的力—力矩平衡，若接触wrench调节不当，可能导致打滑、物体掉落、姿态偏差或过度挤压。本文提出了一种面向未知惯性参数物体的、考虑摩擦约束的双臂箱体搬运框架。该方法可根据测得的接触wrench在线估计物体的质量和质心，并在椭球形摩擦极限面约束下，通过二阶锥规划（SOCP）计算满足摩擦可行性的接触力与扭矩。文中还加入了一个离线轨迹细化阶段，用于在存在几何约束时减少不希望出现的物体—环境接触。通过将摩擦可行性作为硬约束，并在可行域内最小化接触代价，该框架无需把防滑和避免过度挤压作为两个分别调参的目标，也能实现稳定起吊。真实双臂机器人在不同质心配置下的实验表明，该方法能够在维持稳定摩擦接触的同时，搬运具有未知惯性参数的物体。

</details>

---

### [[20_Research/Papers/具身智能/TacO_Benchmarking_Tactile_Sensors_for_Object_Manipulation|TacO: Benchmarking Tactile Sensors for Object Manipulation]]

![[assets/2605.21976_figure.png|800]]

- **arXiv**: [2605.21976](https://arxiv.org/abs/2605.21976)
- **PDF**: https://arxiv.org/pdf/2605.21976
- **详细分析**: [[20_Research/Papers/具身智能/TacO_Benchmarking_Tactile_Sensors_for_Object_Manipulation|TacO: Benchmarking Tactile Sensors for Object Manipulation]]
- **作者**: Anya Zorin, Zilin Si, Myungsun Park, Junsung Park, Alexiy Buynitsky, Sachin Bhadang, Taejun Park, Sohee John Yoon, Yong-Lae Park, Oliver Kroemer, Zeynep Temel, Michael T. Tolley...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

视觉模仿学习已经能让机器人完成不少操作任务和高层语义推理，但在抓取、重新定向、插入等接触密集型操作中，单靠视觉仍然不够。虽然普遍认为触觉能显著提升操作性能，但不同触觉传感器到底适合哪些任务，现有研究几乎没有给出经验性指导。对于做具身智能和机器人操作系统设计的研究者来说，如何在性能、成本、易集成性和材料特性之间权衡选择传感器，是一个非常现实的问题。

#### 方法概述和架构

论文提出 TacO，一个面向机器人操作的触觉传感器基准评测框架，核心是把“传感器好不好”转化为“带该传感器训练出的操作策略有多好”。作者基于 ACT（Action Chunking Transformers）搭建模仿学习管线，将腕部和第三视角 RGB 图像、机器人本体感知以及触觉观测共同作为输入，输出分块动作序列并以滚动时域方式执行。实验覆盖四种触觉模态、六种具体传感器，包括视觉式、磁式、电阻式和振动式传感器；针对不同模态分别设计编码器，如原始读数的 MLP 编码、触觉图像的卷积/ResNet 编码，以及音频信号的 mel-spectrogram 表征。论文为每个任务和每种传感器都训练一套独立策略，并同时训练“带触觉”和“仅视觉”两类策略，用同一数据比较触觉贡献。除此之外，作者还做了跨传感器分析，用于区分性能提升究竟来自触觉信号本身，还是来自传感器材料、外形和安装方式等 embodiment 因素。

#### 实验结果分析

作者在三个真实机器人任务上评测：未知质量的抓放、物体重新定向和插接插入，并在两所机构、不同机器人平台上复现实验，以增强结论可靠性。结果表明，触觉并非在所有任务中都同样有用，其收益强烈依赖于传感器模态、材料属性和具体任务；例如空间分辨率、剪切力感知能力和触觉表征方式都会影响策略表现。文中还进行了传感器重复性分析和开源硬件套件评估，可见文本未给出具体数值，但明确显示该基准不仅比较了模态优劣，也帮助解释了为何某些传感器在特定接触操作中更合适。

<details>
<summary>完整摘要</summary>

基于视觉的演示学习已经在机器人执行操作任务和进行高层语义推理方面取得了显著成功，但对于复杂的、接触密集型的操作任务仍然不够。尽管人们普遍认同触觉感知能够提升操作能力，但目前并没有关于哪类触觉传感器最适合哪类操作任务的经验性指导。本文针对机器人操作任务，对触觉传感器进行了系统化、任务驱动的评测，并提出了一个基于操作策略表现来选择和评估传感器的框架。我们分别针对四种不同模态的触觉传感器训练了独立的操作策略，这四种模态包括视觉式、声学式、磁式和电阻式；评测覆盖三项任务：未知质量物体的抓放、物体重新定向以及插头插入。对于每项任务，我们分析了空间分辨率、剪切力感知、触觉表征方式等传感器属性，以及材料本身的摩擦特性如何影响任务表现。结果表明，触觉感知并不是以同样方式对所有任务都普遍有益，其有效性会强烈依赖于传感器模态、材料属性以及具体的操作任务。所有触觉传感器、代码、数据和硬件搭建都将在项目网站上公开。

</details>

---

### [[20_Research/Papers/机器人/A_Visitation_Grid_for_Complete_Coverage_Foraging_in_Robot_Swarms|A Visitation Grid for Complete Coverage Foraging in Robot Swarms]]

![[assets/2605.21947_figure.jpg|800]]

- **arXiv**: [2605.21947](https://arxiv.org/abs/2605.21947)
- **PDF**: https://arxiv.org/pdf/2605.21947
- **详细分析**: [[20_Research/Papers/机器人/A_Visitation_Grid_for_Complete_Coverage_Foraging_in_Robot_Swarms|A Visitation Grid for Complete Coverage Foraging in Robot Swarms]]
- **作者**: Qi Arturo Gonzalez, Yifeng Gao, Li Zhang, Qi Lu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

在大规模、未知环境中，让机器人群协同搜集离散且稀疏的资源，是群体机器人中的典型难题，常见于搜救、排雷、化学泄漏检测和入侵探测等场景。现有许多 swarm foraging 方法更关注在有限时间内尽可能多地收集资源，而不是把“最后少量残余资源”也高效收完；但研究表明，任务后期往往消耗了总时间的很大一部分。本文聚焦于这一“末期收集效率低”的瓶颈，试图用轻量级的空间记忆减少重复访问，从而提升近乎完全收集与完全收集的能力。

#### 方法概述和架构

论文提出 Grid-Based Complete Foraging Algorithm（GCFA），核心是一个由轻量级中心服务器维护的访问网格。未知搜索区域首先被划分为网格，服务器根据机器人上报的位置，累计每个网格的访问次数，形成全局的探索密度估计。机器人在每次新的觅食任务中，并不直接全局搜索，而是在当前位置附近的 3×3 网格邻域内，按照“访问次数更少者优先”的概率规则选择下一搜索区域，以此将探索偏向低访问区域，同时保留随机性。机器人端只维护一个容量很小的本地 FIFO 队列，周期性记录最近位置，并在返回中心时一次性上传给服务器；机器人之间不需要直接通信，推理阶段依赖服务器下发的目标区域和本地自主搜索。该设计显式兼顾了有限存储、有限计算与可扩展性。

#### 实验结果分析

作者在仿真中将 GCFA 与经典的中心式群体觅食算法 CPFA 进行比较，评估了不同资源数量、不同场景以及任务后期收集阶段的表现。结果显示，GCFA 在多种设置下都能稳定优于 CPFA；在总体收集时间上最高减少 33%，在任务最后阶段的收集效率提升超过 48%。节选文本强调该方法在资源稀少、接近收尾的阶段优势尤为明显，说明基于访问次数的网格记忆能够有效缓解重复访问问题。

<details>
<summary>完整摘要</summary>

大规模未知环境中稀疏资源的完全收集仍然是自主机器人群面临的一个挑战。以往研究表明，总任务时间中相当大的一部分消耗在收集的最后阶段，此时只剩下少量随机分散的资源。因此，许多现有的机器人群觅食算法（搜索与收集）更关注在有限时间窗口内收集大部分资源，而不是提升末期阶段收集全部资源的效率。我们提出一种基于网格的随机觅食策略，显式减少重复访问并加速后期收集。未知搜索区域被划分为一个网格地图，由一个轻量级中心服务器维护。为了保证可扩展性，机器人和服务器都在有限的存储与计算约束下运行。服务器根据机器人上报的位置更新网格级别的访问计数，从而得到全局探索密度估计。对于每一次新的觅食任务，机器人会从局部 3×3 邻域中的网格里，以较低访问计数为偏好的概率方式选择下一搜索区域，这样既能将探索引导到访问较少的区域，又能保持随机性。大量仿真实验表明，所提出的策略始终优于经典的中心式基线觅食算法 CPFA。与 CPFA 相比，该方法最多可将总收集时间减少 33%，并在任务最后阶段将收集效率提升 48% 以上。这些结果表明，该策略具有鲁棒性、灵活性和可扩展性，适用于机器人群在资源受限条件下进行接近完全和完全的资源收集，并可作为随机群体觅食方法的一般性增强模块。

</details>

---

### [[20_Research/Papers/具身智能/Learning_to_Evolve_Multi-modal_Interactive_Fields_for_Robust_Humanoid_Navigation_in_Dynamic_Environments|Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments]]

![[assets/2605.21935_figure.png|800]]

- **arXiv**: [2605.21935](https://arxiv.org/abs/2605.21935)
- **PDF**: https://arxiv.org/pdf/2605.21935
- **详细分析**: [[20_Research/Papers/具身智能/Learning_to_Evolve_Multi-modal_Interactive_Fields_for_Robust_Humanoid_Navigation_in_Dynamic_Environments|Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments]]
- **作者**: Peifeng Jiang, Hong Liu, Jin Jin, Wenshuai Wang, Xia Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

人形机器人在家庭、办公室等人类环境中执行导航时，往往不是“走到附近”就结束，而是要进一步到达一个适合抓取、操作且安全的终端姿态，这对场景记忆的可靠性提出了更高要求。现有语义建图和场景图方法通常默认相机轨迹稳定、环境静态，且对物体几何的刻画较粗，难以直接应对人形机器人行走带来的视角抖动、感知模糊以及环境中物体被移动、增删后的变化。作者认为，这类问题会同时导致语义定位失真和交互姿态不安全，因此很值得关注。

#### 方法概述和架构

论文提出 Multi-modal Interactive Field（MIF），将人形机器人场景记忆拆分为三个相互协作的场：Appearance Field、Spatial Field 和 Geometry Field。Appearance Field 基于带置信度的 semantic 3D Gaussian Splatting，对每个高斯原语估计可靠性，用于抑制步态抖动带来的模糊与错误融合，并生成更稳定的语义渲染结果。Spatial Field 通过稳定重感知后的视图构建拓扑化的场景图，同时计算多模态 discrepancy score，用来区分“行走引起的伪变化”和“真实环境变化”，只对局部不一致区域进行更新。Geometry Field 则在接近目标时按需选择更合适的视角，利用 Flow Matching 进行对象级网格重建，并在此基础上做 Interaction Pose Safety（IPS）验证，以检查终端交互姿态是否满足碰撞避免、可达性与稳定性要求。整个系统在感知—适应闭环中运行：先稳住外观表示，再形成空间记忆，最后补足交互所需几何并反向驱动导航调整。

#### 实验结果分析

作者在真实动态办公室中，使用 Unitree-G1 人形机器人进行了实验，并与静态 scene-graph memory 等基线对比。结果显示，在非静态环境下，MIF 的 relocation success 从 12% 提升到 94%，同时通过特征蒸馏将语义记忆占用减少了 91.4%，说明它更适合在线部署。论文还报告了在鲁棒语义 grounding、交互安全几何重建以及动态 map-reality mismatch 自适应方面的实验，整体表明该方法能同时缓解感知抖动和场景变化带来的问题。可见文本未给出更多具体数值细节。

<details>
<summary>完整摘要</summary>

面向人形机器人的安全操作式导航，需要一种在运动引起的感知失真、环境变化以及交互层面的几何安全约束下仍然可靠的场景记忆。现有语义建图和场景图系统难以直接应用于这一场景，因为它们通常假设相机轨迹稳定、环境静态，或者物体几何较为粗糙。为此，我们提出 Multi-modal Interactive Field（MIF），这是一个面向人形机器人的系统，将带置信度感知的语义 3D Gaussian Splatting、由差异触发的空间记忆更新，以及面向任务的几何重建整合到一个闭环感知—适应管线中。MIF 由三个场耦合而成：其一是具有不确定性感知能力的 3DGS Appearance Field，用于抑制步态引起的模糊；其二是维持拓扑记忆的 Spatial Field；其三是支持操作前 Interaction Pose Safety（IPS）的 Geometry Field。我们引入了一个 discrepancy detection score，用于区分由运动引起的伪正变化与持续存在的真实变化，并且只更新局部不一致区域。在真实动态办公室中的 Unitree-G1 人形机器人实验表明，与静态 scene-graph memory 相比，MIF 在非静态环境中的重定位成功率从 12% 提升到 94%；同时，通过特征蒸馏，其语义记忆占用减少了 91.4%，从而更适合在线实用部署。

</details>

---

### [[20_Research/Papers/强化学习/Auction-Consensus_Algorithm_with_Learned_Bidding_Scheme_for_Multi-Robot_Systems|Auction-Consensus Algorithm with Learned Bidding Scheme for Multi-Robot Systems]]

![[assets/2605.21932_figure.png|800]]

- **arXiv**: [2605.21932](https://arxiv.org/abs/2605.21932)
- **PDF**: https://arxiv.org/pdf/2605.21932
- **详细分析**: [[20_Research/Papers/强化学习/Auction-Consensus_Algorithm_with_Learned_Bidding_Scheme_for_Multi-Robot_Systems|Auction-Consensus Algorithm with Learned Bidding Scheme for Multi-Robot Systems]]
- **作者**: Jose Rodriguez, Constantine Tarawneh, Sven Koenig, Wenjie Dong, Qi Lu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.2，强化学习 0.4，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

多机器人任务分配（MRTA）是分散式多智能体系统中的核心问题，机器人团队需要在通信受限的条件下协同分配并执行任务，同时尽量优化全局目标。现有的拍卖-一致性方法，尤其是CBBA，具有可扩展、可分布执行和收敛性明确等优点，但其依赖人工设计的贪婪评分函数，往往会导致次优分配。本文值得关注之处在于，它尝试用学习到的竞价策略替代传统启发式打分，同时保留分散式协调结构，以兼顾性能与可部署性。

#### 方法概述和架构

论文提出一种带学习竞价机制的拍卖-一致性算法，用神经网络竞价器替换CBBA中的确定性出价函数。每个机器人基于自身局部可观测信息构造部分观测，再输入到策略网络，输出对各任务的标量竞价；这些竞价用于本地任务选择和路径插入。整体流程仍保留CBBA的两阶段结构：先进行任务构建与自分配，再通过一致性阶段交换赢标信息并消解冲突。训练阶段采用CTDE范式，actor只接收局部观测，critic利用全局信息；奖励通过与MILP求得的全局最优解接近程度来塑形。策略训练使用PPO，并比较了 Neural Additive Model、LSTM 和 Set Transformer 等多种网络结构。

#### 实验结果分析

实验在不同规模的机器人群体上进行，评估学习型竞价策略相较经典CBBA的任务分配质量；可见文本未给出具体数值。结果显示，学习到的竞价策略能够在保持分散式执行的前提下提升解质量。论文同时考察了多种神经网络架构，说明该思路具有一定的模型可替换性与规模扩展能力。

<details>
<summary>完整摘要</summary>

多机器人任务分配（MRTA）是分散式多智能体系统中的核心挑战：机器人团队必须在通信受限的条件下协同分配并执行任务，同时优化全局性能目标。拍卖-一致性算法（如Consensus-Based Bundle Algorithm, CBBA）提供了可扩展的分散式协调机制，并且具有可证明的收敛性，但其依赖人工设计的贪婪评分函数，常常导致次优的任务分配。本文提出一种增强学习的拍卖-一致性框架，将CBBA中的确定性竞价机制替换为通过强化学习训练得到的神经竞价策略。在“集中训练、分散执行”（CTDE）范式下，智能体仅根据部分局部观测计算任务竞价，同时保留标准的拍卖与一致性阶段以实现分散协调。该竞价策略使用PPO进行训练，奖励函数通过与混合整数线性规划求得的全局最优解的接近程度来塑形。论文评估了多种神经网络结构，包括 Neural Additive Model、LSTM 和 Set Transformer。不同规模群体的实验结果表明，学习到的竞价策略在保持分散执行能力的同时，可优于经典CBBA的解质量。该方法展示了将强化学习与经典分布式协调算法结合的有效性，为高质量分散式多机器人任务分配提供了一条可扩展路径。

</details>

---

### [[20_Research/Papers/机器人/Non-Contact_Vibration-Based_Damage_Detection_of_Civil_Structures_Using_a_Cost-Effective_Autonomous_UAV|Non-Contact Vibration-Based Damage Detection of Civil Structures Using a Cost-Effective Autonomous UAV]]

![[assets/2605.21914_figure.jpg|800]]

- **arXiv**: [2605.21914](https://arxiv.org/abs/2605.21914)
- **PDF**: https://arxiv.org/pdf/2605.21914
- **详细分析**: [[20_Research/Papers/机器人/Non-Contact_Vibration-Based_Damage_Detection_of_Civil_Structures_Using_a_Cost-Effective_Autonomous_UAV|Non-Contact Vibration-Based Damage Detection of Civil Structures Using a Cost-Effective Autonomous UAV]]
- **作者**: Javier Becerril, Maximiliano Vargas, Jennifer Herrera, Joanna Gutierrez, Jorge Rios, Mohsen Amjadian, Constantine Tarawneh, Jinghao Yang, Qi Lu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

结构健康监测中，利用振动特征识别建筑、桥梁等民用结构的损伤是一类重要任务，但传统加速度计等接触式传感器需要安装、布线和维护，面对大型或难以到达的结构时可扩展性较差。基于视觉的非接触测量可以避免接触式布设带来的限制，而无人机又进一步提升了对高空、危险或无法长期部署区域的巡检灵活性。该论文关注的是：如何在GPS受限环境下，借助低成本自主无人机稳定获取结构振动视频，并从中提取固有频率变化来判断损伤。

#### 方法概述和架构

论文提出了一种基于非接触振动测量的结构损伤检测方案，核心是用自制低成本自主 UAV 搭载相机采集结构视频，再通过视觉运动跟踪提取位移时程。系统采用单目视觉跟踪选定测点的位移变化，而不是做全场DIC，从视频中恢复振动信号后再进入频域分析，识别固有频率及其偏移。无人机平台由飞控、伴随计算机、下视光流传感器和前视相机构成，前视相机用于采集结构振动视频，AprilTag 用于在无GPS室内环境中完成自动对准与姿态保持，保证相机始终朝向被测框架。实验上，作者在实验室缩尺一层框架结构上进行测试，通过电动振动台施加谐波/扫频激励与自由振动条件，并在健康与模拟损伤状态下采集数据。数据源包括两部智能手机、USB相机和自研 UAV，同时用接触式加速度计与有限元模型作为参考，对比各平台提取的位移时程和频域结果。

#### 实验结果分析

实验结果表明，所有平台都能成功捕捉结构的基频及其在模拟损伤后的频率偏移，说明该非接触方法对损伤识别有效。自研 UAV 由于平台扰动和传感限制，误差略高，约为 5.7% 左右，但仍能可靠检测由损伤引起的频率变化。与商用无人机系统相比，该平台在保持相近巡检性能的同时显著降低了成本；不过节选文本未给出更完整的数值对比和详细基线指标。

<details>
<summary>完整摘要</summary>

本文提出一种利用自主定制的低成本无人机开展结构振动型损伤检测的非接触方法。该方法通过基于视觉的运动跟踪，从视频记录中提取振动信号，以识别表明结构劣化的固有频率变化。研究以实验室尺度的框架结构为对象，在健康状态和模拟损伤状态下进行评估，其中损伤通过增加质量的方式引入。所提出的系统通过一项多平台实验研究进行验证，实验平台包括两部高分辨率智能手机、一台USB相机，以及一架自制低成本无人机；该无人机搭载机载相机和基于 AprilTag 的自主对准系统，可在无GPS环境中运行。研究将提取到的位移时程在频域内进行分析，并与接触式加速度计测量结果以及有限元模型进行比较。实验结果显示，所有平台都能成功捕捉到基频及其因损伤引起的偏移。尽管由于平台扰动和传感限制，无人机的误差略高，约为5%–6%，但它仍能可靠检测出损伤导致的频率变化。与商用无人机系统相比，所提出的平台以显著更低的成本实现了相当的巡检性能。这些结果表明，低成本自主无人机为结构健康监测提供了一种实用、灵活且可扩展的解决方案，尤其适用于接触式传感难以实施的场景。研究结果也支持未来部署多架协同无人机，以进一步提升巡检覆盖范围和鲁棒性。

</details>

---

### [[20_Research/Papers/机器人/Higher_Order_Reasoning_for_Collaborative_Communicationless_Mobile_Robot_Operations|Higher Order Reasoning for Collaborative Communicationless Mobile Robot Operations]]

![[assets/2605.21901_figure.png|800]]

- **arXiv**: [2605.21901](https://arxiv.org/abs/2605.21901)
- **PDF**: https://arxiv.org/pdf/2605.21901
- **详细分析**: [[20_Research/Papers/机器人/Higher_Order_Reasoning_for_Collaborative_Communicationless_Mobile_Robot_Operations|Higher Order Reasoning for Collaborative Communicationless Mobile Robot Operations]]
- **作者**: Jonathan Reasoner, Nicola Bezzo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

在多机器人协作任务中，搜索、救援、侦察等场景往往要求机器人在未知环境中尽快发现并完成共享任务，但现实中通信并不总是可用，常见的集中式或依赖持续信息交换的协同策略因此难以直接落地。该工作关注“无通信”条件下的协同问题，尤其面向通信受限、被干扰或不希望暴露通信的场景。论文值得关注之处在于，它尝试用高阶认知推理替代显式通信，让机器人通过推断“我知道你知道什么”来实现隐式协同。

#### 方法概述和架构

论文提出一个基于动态认识逻辑（DEL）的长时域估计—规划—协同框架，用于无通信多机器人任务发现与完成。每个机器人维护三类状态：自身位姿、关于团队知识的认识状态，以及对其他机器人行为的预测状态，并将后两者用 belief/empathy particles 表示。系统先通过贝叶斯更新将局部观测与既有认识状态融合，再在预测时域内传播一阶信念、二阶同理心以及更高阶的“我认为你认为第三方如何行动”的粒子。随后，机器人用深度受限的行为树搜索在若干行为原语中做选择，包括探索、完成任务、主动接触/引导队友前来以及改良探索策略。低层执行由一个考虑时间变化目标的 MPPI 控制器完成，用于在部分可观测条件下规划拦截、靠近和轨迹调整，并把高层认知推理与连续运动控制连接起来。

#### 实验结果分析

论文在仿真和实体机器人实验中验证了该框架，相比一阶基线，任务完成时间持续下降。实验设置包含未知任务发现、队友引导与等待协同等情形，结果表明高阶推理能让机器人更早选择有利于全队的行为，例如主动去接应距离更远的队友，或在预期队友到达的时刻等待汇合。正文节选中未给出具体数值，但作者强调该方法在多种场景下都表现出更好的鲁棒性与长时域协同能力。

<details>
<summary>完整摘要</summary>

在无通信环境中，多机器人系统必须在缺乏许多协同策略所依赖的持续信息交换的条件下运行。本文提出一种新的动态认识规划框架，通过机器人之间的高阶推理实现隐式协同和长时域规划。该方法使机器人能够形成并传播高阶信念粒子，利用贝叶斯推断更新世界信念，并通过一个能够预判队友可能决策的行为树来选择动作。一个考虑时间因素的模型预测路径积分（MPPI）控制器将这些推理结果整合到低层执行中，使机器人能够在部分可观测条件下规划拦截并自适应调整轨迹。所提出的框架在仿真和实体实验中进行了评估，与一阶基线相比，它始终能够缩短任务完成时间，表明认识逻辑可以作为通信受限领域中鲁棒协同的坚实基础。

</details>

---

### [[20_Research/Papers/机器人/OCELOT_Odometry_and_Contact_Estimation_for_Legged_Robots|OCELOT: Odometry and Contact Estimation for Legged Robots]]

![[assets/2605.21863_figure.png|800]]

- **arXiv**: [2605.21863](https://arxiv.org/abs/2605.21863)
- **PDF**: https://arxiv.org/pdf/2605.21863
- **详细分析**: [[20_Research/Papers/机器人/OCELOT_Odometry_and_Contact_Estimation_for_Legged_Robots|OCELOT: Odometry and Contact Estimation for Legged Robots]]
- **作者**: Emre Girgin, Cagri Kilic
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

腿式机器人在复杂、非结构化地形中的机动性优于轮式平台，但其里程计估计更困难，因为系统只能依赖机载惯性、关节和接触等本体感觉信息来推断机身位姿。现有腿式里程计通常通过“脚处于支撑且静止”这一假设做零速度更新，但真正的难点在于如何准确判断足端是否真的接触地面、是否发生了打滑。本文之所以值得关注，是因为它针对“接触判定不准导致里程计漂移”的核心瓶颈，提出了一个专门用于识别并抑制滑移影响的完整方案。

#### 方法概述和架构

作者提出 OCELOT，一个基于 Error-State EKF（ESEKF）的腿式机器人里程计管线，仅使用固定在机身上的 IMU、关节编码器和足端力传感器作为输入。系统首先用 IMU 进行状态传播，再在检测到支撑足时执行零速度更新，以修正位姿漂移。核心创新是一个“接触检测+不确定性量化”模块：对每只脚并行运行两个检测器，其中一个是由力信号驱动、经 GMM 引导的去抖动 FSM，用于确认足端是否存在物理接触；另一个是在估计足端速度上进行的 kinematic-based GLRT，用于判断该足是否在运动学上足够静止。随后，两个检测器输出的连续质量分数被融合，生成接触质量与自适应测量协方差，用来动态调节滤波器对每次零速度更新的信任程度；若检测到低质量接触或疑似滑移，则自动增大协方差并降低其影响，最后再通过 innovation gating 进一步剔除离群观测。

#### 实验结果分析

作者采集了一个多模态四足数据集，共 29 段序列，覆盖室内外多种地形，包括 concrete、grass、pebble 和 rock，总里程约 2.4 km，并将方法与仅本体感觉和外部感知方法进行了对比。实验表明，该方法在易滑地形上仍能保持较稳健的里程计估计，能够有效识别并抑制打滑带来的误差传播。正文节选还显示作者做了 FSM、GLRT 与协方差量化相关的消融/对比实验，但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

腿式机器人面临的一个重要挑战，是仅依靠机载本体感觉传感器实现准确里程计估计。在本研究中，我们提出了一套完整的腿式里程计管线，基于 Error-State EKF（ESEKF），且完全依赖本体感觉数据：机身固定 IMU、关节编码器和力传感器；滤波器的状态由被判定为静止支撑的足进行校正。我们的核心贡献是一个融合接触检测与不确定性量化的模块，能够显式识别并拒绝滑移。该模块对每只脚并行运行两个检测器：1）一个由力信号驱动、经 Gaussian Mixture Model（GMM）引导的去抖动 Finite State Machine（FSM），用于确认物理接触；2）一个基于运动学的 Generalized Likelihood Ratio Test（GLRT），作用于估计得到的足端速度。两个估计器输出的连续质量分数会被融合，用于判断该足是否既受力又在运动学上静止，并作为每次接触的一个不确定性信号。为了验证我们的方法，我们采集了一个多模态数据集，共 29 段序列，覆盖室内和室外的多种地形，例如混凝土、草地、鹅卵石和岩石，总长度为 2.4 km。我们将所提方法与本体感觉方法和外部感知方法都进行了基准比较。结果表明，该方法能够提供准确的里程计估计，并且在易发生滑移的环境中表现出较强鲁棒性。我们还将代码和可实时运行的 ROS2 软件包以开源形式共享。

</details>

---

### [[20_Research/Papers/机器人/Analytical_and_Experimental_Force_Analysis_of_a_Soft_Linear_Pneumatic_Actuator|Analytical and Experimental Force Analysis of a Soft Linear Pneumatic Actuator]]

![[assets/2605.21836_first_page.png|800]]

- **arXiv**: [2605.21836](https://arxiv.org/abs/2605.21836)
- **PDF**: https://arxiv.org/pdf/2605.21836
- **详细分析**: [[20_Research/Papers/机器人/Analytical_and_Experimental_Force_Analysis_of_a_Soft_Linear_Pneumatic_Actuator|Analytical and Experimental Force Analysis of a Soft Linear Pneumatic Actuator]]
- **作者**: Mohammed Abboodi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

软套筒执行器（soft sleeve actuators, SSAs）近年来被用于可穿戴和辅助机器人系统，因为它们可以在保持柔顺性的同时，贴合肢体曲面并减少对外部绑带和传动结构的依赖。然而，这类执行器的输出力如何随伸长变化、外部负载如何影响力输出，以及轴向刚度在其中扮演什么角色，现有解释仍然不足。对于面向机器人与具身智能的人机交互和可穿戴助力场景，弄清这类软气动执行器的力学机理具有直接价值，因此这篇工作值得关注。

#### 方法概述和架构

本文围绕一类线性软套筒执行器（LSSA）建立了准静态解析模型，用来描述其净轴向力。模型将输出力分解为两部分：由端盖与折叠壁在内部气压作用下产生的贡献，以及由轴向刚度带来的反向力。为刻画这种关系，作者把内部压力、投影受压面积、折叠壁几何形状、轴向位移以及经实验拟合得到的轴向刚度关系纳入同一个分析表达式中。随后，作者设计了规定伸长实验和静态载荷实验，用实测数据验证模型对执行器响应的预测能力。

#### 实验结果分析

实验表明，在 125 kPa 条件下，LSSA 的输出力会随着伸长显著下降：从零伸长时约 112 N，逐步降至 40 mm 伸长时接近 0。静态加载会延迟可测力的产生，并降低整体输出，尤其在低压和中等压力下更为明显。结果说明，LSSA 的力生成并不是单一由压力决定，而是由压力、几何形状、位移、外部载荷与轴向刚度共同耦合控制；可见文本未给出具体基线对比数值。

<details>
<summary>完整摘要</summary>

软套筒执行器（SSAs）近年来被开发为一种用于可穿戴和辅助机器人系统的气动驱动方案。通过将驱动结构集成到类似袖套的几何形态中，这类执行器能够在保持与肢体形状表面贴合性的同时，减少对外部附着层和传动机构的依赖。然而，SSAs 的力生成行为仍然缺乏充分解释，尤其是输出力在伸长过程中的变化、外部载荷的影响，以及轴向刚度的机械作用。本文对一种线性软套筒执行器（LSSA）进行了解析与实验力学分析。作者建立了一个准静态解析模型，将净轴向力表示为由端盖和折叠壁在压力作用下产生的贡献，并减去与轴向刚度相关的力。该模型考虑了内部压力、投影压力面积、折叠壁几何、轴向位移以及通过实验拟合得到的轴向刚度关系。研究采用规定伸长实验和静态载荷实验来评估执行器响应。在 125 kPa 下，执行器产生的力从零伸长时约 112 N 下降到 40 mm 伸长时几乎为零。静态载荷会延迟可测力的产生，并降低力输出，尤其是在低压和中等压力条件下更为明显。结果表明，LSSA 的力生成受压力、几何、位移、载荷和轴向刚度的耦合作用所支配。

</details>

---

### [[20_Research/Papers/具身智能/Safe_and_Steerable_Geometric_Motion_Policies_for_Robotic_Dexterous_Manipulation|Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation]]

![[assets/2605.21811_figure.png|800]]

- **arXiv**: [2605.21811](https://arxiv.org/abs/2605.21811)
- **PDF**: https://arxiv.org/pdf/2605.21811
- **详细分析**: [[20_Research/Papers/具身智能/Safe_and_Steerable_Geometric_Motion_Policies_for_Robotic_Dexterous_Manipulation|Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation]]
- **作者**: Albert Wu, Riccardo Bonalli, Thomas Lew, C. Karen Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

灵巧操控要求机器人同时处理来自不同几何空间的目标与约束，例如在配置空间中控制关节运动、在SE(3)中跟踪末端位姿、以及在欧氏空间中满足障碍物与安全边界。现有数据驱动方法虽然灵活，但往往缺乏可验证安全性，且一旦超出训练分布就可能失效；而轨迹优化方法虽然能显式处理约束，却通常计算开销大、易陷入局部最优，不适合高频在线控制。已有PBDS具备良好的几何一致性，但安全约束是软约束、且缺少高层策略的在线可控接口，因此难以直接用于需要“既安全又可引导”的灵巧操控场景。

#### 方法概述和架构

论文提出 Safe Pullback Bundle Dynamical Systems（SafePBDS），在保持PBDS几何一致性的基础上，引入可证安全的控制机制。其核心是“pullback CBF”构造：先在任务流形上定义安全条件，再通过任务映射把这些条件拉回到配置流形上，最终在加速度层形成线性约束并进入二次规划求解。第二个关键模块是任务流形动作接口，允许高层策略在选定任务流形上注入低维残差动作；当动作输入为0时系统退化为原本的自治行为，而任意输入下安全性仍由约束保持。整体流程是在每个控制步中，将自治动力学、任务目标、安全约束与外部动作共同输入约束QP，输出一个安全的配置流形加速度作为控制指令。

#### 实验结果分析

作者在模拟和23自由度的Franka Panda–Allegro Hand平台上验证了方法有效性。硬件实验中，SafePBDS在20个家用物体、120次试验上实现了92.5%的灵巧抓取成功率；在通过一维动作实现“排除任意一根手指”的3指抓取消融实验中，3个物体、36次试验的成功率达到94.4%。此外，该方法还支持模型驱动的、全驱动的 palm-down in-hand reorientation，在不同物体重量和手腕运动条件下，双向均实现超过360°的偏航旋转。正文节选还显示，作者通过S^2双积分系统和7自由度机械臂实验验证了图表不变性、任务流形度量影响、安全恢复以及动作接口等性质；若需更细的对比基线与数值，节选中未给出具体数值。

<details>
<summary>完整摘要</summary>

机器人灵巧操控需要持续协调定义在异构几何空间上的目标与约束：例如，一个由ℝ^7配置流形控制的机器人，可能需要在SE(3)上跟踪末端执行器位姿，同时还要在ℝ中满足障碍物避让边界。我们提出 Safe Pullback Bundle Dynamical Systems（SafePBDS），这是一种几何一致的框架，能够根据任意任务流形上的目标与安全要求，计算出最优且可证安全的配置流形加速度。SafePBDS建立在先前将预定义任务流形动力系统组合起来以生成自主运动的工作基础之上。它的第一个创新是 pullback control barrier function 构造，将任务流形上的安全条件转换为配置流形加速度上的线性约束。第二个创新是任务流形动作接口，它允许高层策略注入低维残差运动；当输入为零时可恢复自主行为，而在任意输入下都能保持安全性。这使得高层策略能够高效引导探索，而精细运动生成则交由自主行为完成。我们在仿真环境以及23自由度的Franka Panda–Allegro Hand平台上验证了SafePBDS。在灵巧抓取任务中，SafePBDS在20个家用物体、120次试验上取得了92.5%的成功率。借助动作接口，该方法可以通过一个一维动作在抓取时排除四根手指中的任意一根，并在3个物体、36次试验上实现94.4%的三指抓取成功率。SafePBDS的高效规划与安全保证还使其能够首次实现模型驱动、全驱动的 palm-down 手内重定向，在不同物体重量和手腕运动条件下，双向偏航旋转均超过360°。演示视频与更多细节见：https://tml.stanford.edu/safe-pbds

</details>

---

### [[20_Research/Papers/机器人/Mind_the_Gaps_Multi-Robot_Feedback-Driven_Ergodic_Coverage_in_Unknown_Environments|Mind the Gaps: Multi-Robot Feedback-Driven Ergodic Coverage in Unknown Environments]]

![[assets/2605.21719_figure.png|800]]

- **arXiv**: [2605.21719](https://arxiv.org/abs/2605.21719)
- **PDF**: https://arxiv.org/pdf/2605.21719
- **详细分析**: [[20_Research/Papers/机器人/Mind_the_Gaps_Multi-Robot_Feedback-Driven_Ergodic_Coverage_in_Unknown_Environments|Mind the Gaps: Multi-Robot Feedback-Driven Ergodic Coverage in Unknown Environments]]
- **作者**: Thales Costa Silva, Nora Ayanian
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

多机器人自适应覆盖是一个典型的动态采样任务，机器人团队需要在环境中不断调整位置，以便持续收集数据并优先覆盖高信息区域。这类问题常见于环境监测、搜索救援、海洋与空气污染追踪等场景，但难点在于：环境中的“重要区域”往往事先未知，而且会随时间变化，导致机器人分配和路径规划都变得困难。现有 ergodic search 方法虽然能让机器人轨迹在统计意义上匹配目标分布，从而兼顾探索与利用，但通常依赖已知或预先设定的目标分布，难以处理未知先验环境。

#### 方法概述和架构

论文提出了一种面向未知环境的反馈驱动 ergodic coverage 方法，核心思想不是改造 ergodic 轨迹优化本身，而是在线构造并更新其目标分布。方法中，机器人利用传感器采样环境中的信息函数，并为每个机器人维护一个基于 basis function 的参数化环境模型，用在线更新的参数 \hat{a}_i 估计空间信息分布 \hat{\phi}_i(x)。随后，算法将该估计转化为 ergodic search 的目标空间信息分布，使机器人轨迹在时间平均意义上与环境信息密度相匹配。控制律会根据实时反馈不断修正目标分布，从而让机器人优先访问高信息区域，同时仍保留对低密度区域的覆盖。作者假设环境静态或变化速度慢于机器人运动，并用该假设保证在线估计和轨迹优化可以形成闭环。

#### 实验结果分析

论文在仿真中验证了该方法的有效性，实验包括静态高斯分布和时变高斯分布两类场景，用于检验算法对未知分布和缓慢变化环境的适应能力。与传统 ergodic coverage 相比，该方法能够更好地根据实时反馈调整采样资源分配，提升覆盖效率。节选文本未给出具体数值指标，因此无法报告定量提升幅度。作者还指出，该在线自适应目标分布在静态环境下能够收敛到目标过程，说明方法具有一定稳定性与泛化潜力。

<details>
<summary>完整摘要</summary>

本文研究多机器人自适应覆盖问题，即机器人团队通过持续调整位置来进行动态采样，从而在环境中收集数据。该任务具有较高挑战性，尤其是在需要随着时间变化将机器人高效分配到新的采样位置时。Ergodic search 方法通过保证机器人轨迹的时间平均空间分布与环境信息的空间分布一致，从而优化机器人轨迹。尽管这类方法在给定目标分布时能够促进有效探索，但它们通常无法处理环境中未知的先验分布。为克服这一限制，我们提出一种自适应覆盖策略，利用来自环境模型的实时反馈，根据未知条件调整机器人的采样行为。我们的方法在传统 ergodic 轨迹优化基础上进行了增强：通过基于环境参数模型构建目标空间信息分布，并在线更新该模型来实现这一点。该策略假设环境是静态的，或者相对于机器人运动而言变化较慢。我们的框架使机器人能够动态优先关注高兴趣区域，提高覆盖效率，为单个智能体合成有效控制策略，并在未知先验分布的场景中优化资源使用。我们通过仿真验证了该方法，结果表明其在提升覆盖能力和资源分配效率方面是有效的。

</details>

---

### [[20_Research/Papers/具身智能/Motion_Design_for_Grasp-Based_Dynamic_Locomotion_in_Microgravity|Motion Design for Grasp-Based Dynamic Locomotion in Microgravity]]

![[assets/2605.21704_figure.png|800]]

- **arXiv**: [2605.21704](https://arxiv.org/abs/2605.21704)
- **PDF**: https://arxiv.org/pdf/2605.21704
- **详细分析**: [[20_Research/Papers/具身智能/Motion_Design_for_Grasp-Based_Dynamic_Locomotion_in_Microgravity|Motion Design for Grasp-Based Dynamic Locomotion in Microgravity]]
- **作者**: Chaerim Moon, Joohyung Kim, Justin K. Yim
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

微重力环境中的移动任务常依赖分散且不规则分布的锚点，例如空间站外部巡检、在轨装配以及小行星表面操作等场景。与地面行走不同，这类任务不能依赖持续的支撑接触，机器人需要通过多肢体抓握在三维空间中完成锚点到锚点的转移，而且还要同时处理接触稳定性与整机动力学耦合带来的风险。现有研究多采用准静态假设，或者将基座运动与摆动肢体严格分阶段处理，难以覆盖时间敏感、能量受限的动态移动需求。因此，这篇论文值得关注之处在于，它系统讨论了微重力下基于抓握的动态步态设计问题，并尝试给出可操作的运动规划原则。

#### 方法概述和架构

论文提出了一个面向多肢体机器人在微重力环境中执行抓握式动态移动的参数化规划框架，重点研究步态模式、步长、移动速度和名义姿态等设计变量。首先，作者从动力学可行性和运动学可行性两方面建立约束：前者用6D合力矩空间或可行wrench多面体刻画接触不脱离时可承受的整体作用，后者强调浮动基座会改变各肢体可达锚点集合，因此需要通过基座轨迹来维持与环境的几何关系。其次，规划架构分为高层、中层和低层三层：高层根据给定步长选择候选锚点并自适应确定目标基座位姿；中层生成基座的6D时间轨迹和末端执行器的分段摆动轨迹，并通过摆动顺序、相位重叠和摆动时长等互肢参数实现全身协调；低层则通过逆运动学与插值把规划结果转为关节命令。最后，摆动轨迹被拆分为释放、后撤、转运、接近和抓握五个阶段，以五次多项式平滑连接，并在基座轨迹中使用具有C2连续性的速度规划来抑制冲击性动量变化。

#### 实验结果分析

作者在基于物理的仿真中评估了两种代表性的四足机器人形态，并比较了不同步态顺序、步长与速度、名义姿态及形态差异对动态抓握移动性能的影响。实验指标主要围绕稳定性和执行器需求展开；节选内容中可见文本未给出具体数值。结果表明，扩大可行接触wrench空间能够提升移动性能，而降低由基座和肢体运动引起的冲击性整机动力学变化也能显著改善稳定性与控制负担。论文还指出，接触配置选择和全身协调策略需要共同设计，才能更好地适配微重力下的动态抓握移动。

<details>
<summary>完整摘要</summary>

微重力环境中的移动通常依赖于稀疏且不规则分布的锚点，因此有必要采用多肢体的基于抓握的移动方式。在这种场景下，只有在耦合的动力学与运动学约束下，同时对锚定交互和全身协调进行精细调节，动态移动才是可行的。本文针对需要通过6D肢体操作来与候选锚点建立接触的微重力多肢体机器人系统，提出了基于抓握的动态移动设计洞见。研究考察的设计参数包括步态模式、步长、移动速度以及名义姿态。为支持这些参数的变化并评估相应的移动性能，本文提出了一个可参数化的运动规划框架，并从稳定性与执行器需求两个方面进行评价。实验采用两种代表性的四足机器人形态，并在基于物理的仿真中进行测试。结果表明，扩大可行接触wrench空间并减弱冲击性的全身动力学，有助于提升移动性能。这些发现为多肢体系统在微重力中的接触配置选择与全身协调策略提供了依据。

</details>

---

### [[20_Research/Papers/强化学习/Closed-Loop_Sim-to-Real_Reinforcement_Learning_for_Deformable_Microfiber_Shape_Control|Closed-Loop Sim-to-Real Reinforcement Learning for Deformable Microfiber Shape Control]]

![[assets/2605.21688_first_page.png|800]]

- **arXiv**: [2605.21688](https://arxiv.org/abs/2605.21688)
- **PDF**: https://arxiv.org/pdf/2605.21688
- **详细分析**: [[20_Research/Papers/强化学习/Closed-Loop_Sim-to-Real_Reinforcement_Learning_for_Deformable_Microfiber_Shape_Control|Closed-Loop Sim-to-Real Reinforcement Learning for Deformable Microfiber Shape Control]]
- **作者**: Alessandro Amici, Houari Bettahar, Veeti Jaakkola, Quan Zhou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，强化学习 0.8，机器人 0.3）
- **关联关键词**: RL, Systems

#### 研究背景与动机

这篇论文聚焦于表面接触下的微尺度纤维操控，具体任务是让柔性 microfiber 在双夹爪微操作系统中实现目标形状控制。这类任务在显微装配、微纳制造和生物样本处理等场景中很有价值，但由于微尺度下的表面力、界面作用和摩擦难以精确建模，传统基于模型的控制方法与常规 sim-to-real 学习都很难稳定落地。论文值得关注之处在于，它尝试用一个简化仿真环境训练策略，再依靠真实系统中的闭环视觉反馈来补偿仿真与现实的差异，从而减少对精确物理建模和现实域适配的依赖。

#### 方法概述和架构

作者提出一种 closed-loop sim-to-real reinforcement learning 方法用于 microfiber 形状控制。训练阶段完全在一个简化的、无摩擦的几何仿真器中进行，学习目标是形状调节策略而不是精确建模接触动力学。部署阶段，策略被直接迁移到真实的双夹爪微操作系统上，以 40 Hz 的频率运行，并利用实时视觉观测持续评估当前纤维形状与目标形状之间的偏差。系统根据闭环反馈迭代修正操作结果，也就是说，仿真中未显式建模的表面交互效应不是在训练时被消除，而是在执行时通过观测—动作循环被逐步补偿。该方法没有进行额外重训练或 domain adaptation，而是依靠任务相关误差在闭环内可观测、可修正这一前提完成 sim-to-real 迁移。

#### 实验结果分析

实验以 silk microfibers 作为测试对象，在 24 种不同初始配置下验证了策略性能，平均逐点形状误差为 270 ± 80 μm。进一步地，在 9 个样本上覆盖三种纤维直径（50、80、120 μm）与三种操控长度（10、15、20 mm）的所有组合时，同一策略无需重新训练或调参即可达到亚毫米级最终形状误差。结果表明，在任务相关的仿真—现实差异能够被闭环系统观测并纠正的前提下，单一仿真训练策略可以稳定迁移到真实微操控场景。

<details>
<summary>完整摘要</summary>

由于微尺度下的表面和界面相互作用难以被准确建模，自动化的接触式微操作具有很大挑战性，这限制了传统基于模型的控制以及 sim-to-real 学习的应用。我们提出一种用于表面上 microfiber 形状控制的 closed-loop sim-to-real reinforcement learning（RL）方法。其核心思想是在一个简化的无摩擦仿真器中训练几何形状调节策略，并在部署时依靠实时视觉反馈，迭代修正未建模表面相互作用所带来的实际效果。一个完全在仿真中训练得到的 RL 策略被直接迁移到真实的双夹爪微操作系统上，并以 40 Hz 运行，无需重新训练或进行域适配。以 silk microfibers 为测试对象，该策略在 24 种不同初始配置下实现了 270 ± 80 μm 的平均逐点形状误差。在 9 个样本上，覆盖三种纤维直径（50、80 和 120 μm）以及三种被操控长度（10 mm、15 mm 和 20 mm）的所有组合时，同一策略在无需重新训练或重新调参的情况下实现了亚毫米级的最终形状误差。这些结果表明，只要 sim-to-real 不匹配中与任务相关的影响能够在闭环反馈中被观测并校正，那么在简化仿真器中学到的策略就能够在真实表面接触条件下实现可重复的 microfiber 形状调控。

</details>

---

### [[20_Research/Papers/机器人/Distributed_Multi-Coverage_for_Robot_Swarms|Distributed Multi-Coverage for Robot Swarms]]

![[assets/2605.21686_figure.png|800]]

- **arXiv**: [2605.21686](https://arxiv.org/abs/2605.21686)
- **PDF**: https://arxiv.org/pdf/2605.21686
- **详细分析**: [[20_Research/Papers/机器人/Distributed_Multi-Coverage_for_Robot_Swarms|Distributed Multi-Coverage for Robot Swarms]]
- **作者**: Mariem Guitouni, Aaron T. Becker
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

在无人机/机器人集群用于巡检、环境监测和基础设施检查时，单点覆盖很脆弱：一旦部分机器人失效，关键资产就可能失去监控。因此，任务不只是“覆盖到”，而是要让每个资产被多台机器人冗余覆盖，而且不同资产的重要性还可能对应不同的覆盖次数需求。现有最优方法多依赖集中式整数规划，需要全局位置与通信、全局计算和统一调度，在大规模、弱通信、易故障的真实部署中难以落地。

#### 方法概述和架构

论文提出一种面向机器人集群的分布式多重覆盖算法，支持本地感知、本地通信、无全局协调。方法分为三个阶段：首先通过探索阶段，机器人用结构化网格初始化并结合 Lloyd 算法在工作空间内分散，尽量发现全部资产；随后在优化阶段，每个机器人仅基于自身、邻居以及局部感知到的资产信息，统计局部覆盖计数，并用最小边界圆和边际代价来决定由哪台机器人接管某个覆盖不足的资产；若某资产仍未满足需求，则通过局部交换和确定性冲突消解继续推进。最后在精炼阶段，机器人在已满足覆盖要求的前提下进行邻居间资产转移，减少过覆盖并降低总感知成本。整个流程的输入是资产集合、每个资产的覆盖需求 κ(p)、机器人数量与局部通信/感知半径，输出是每台机器人最终的位置、感知半径以及其负责覆盖的资产集合。

#### 实验结果分析

作者在静态与动态场景下对该方法进行了实验评估，并与集中式求解思路进行对比，重点考察收敛行为、性能表现以及对环境变化的适应性。结果显示，该分布式方法能够在仅依赖局部信息的情况下逐步满足多重覆盖约束，并在精炼阶段减少冗余覆盖；同时也讨论了与集中式最优解相比，在最优性、可扩展性和适应性之间的权衡。节选中未给出具体数值结果，但可以看出该方法更适合大规模、通信受限或部分失效的实际部署。

<details>
<summary>完整摘要</summary>

部署于监视、环境监测和基础设施检查任务中的自主无人机集群，即使在机器人发生故障的情况下，也必须保持对关键资产的可靠覆盖。这就需要多重覆盖：每个资产都应由多台机器人同时观测以提供冗余，而且不同资产的重要性对应不同的覆盖需求。尽管近期工作已经通过整数规划以最优方式解决了集中式问题，但实际部署存在一些必须采用分布式方案的约束：机器人之间的通信范围有限、机载计算能力限制了全局规划，而且局部故障不应导致整个任务中止。我们提出了一种面向机器人集群的分布式多重覆盖算法，该算法仅依赖本地感知、本地通信，并且不需要全局协调。

</details>

---

### [[20_Research/Papers/具身智能/Flying_Together_Human-Guided_Immersive_Shared_Control_for_Aerial_Robot_Teams_in_Unknown_Environments|Flying Together: Human-Guided Immersive Shared Control for Aerial Robot Teams in Unknown Environments]]

![[assets/2605.21680_figure.png|800]]

- **arXiv**: [2605.21680](https://arxiv.org/abs/2605.21680)
- **PDF**: https://arxiv.org/pdf/2605.21680
- **详细分析**: [[20_Research/Papers/具身智能/Flying_Together_Human-Guided_Immersive_Shared_Control_for_Aerial_Robot_Teams_in_Unknown_Environments|Flying Together: Human-Guided Immersive Shared Control for Aerial Robot Teams in Unknown Environments]]
- **作者**: Lou De Bel-Air, Luca Morando, Ruitao Chen, Keru Wang, Benjamin Jarvis, Charbel Toumieh, Yang Zhou, Ken Perlin, Dario Floreano, Giuseppe Loianno
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

多无人机在搜救、巡检和环境探测中具有更强的覆盖能力与鲁棒性，但在未知、狭窄且结构化程度低的环境里，纯自主导航往往难以及时响应突发情况，也不容易捕捉操作者临时提出的目标。相比单机遥操作，面向多机团队的共享控制更难：既要保持队形协同与避障，又要让人类能够实时介入并引导机器人去往感兴趣区域。本文值得关注之处在于，它把VR/MR交互、用户在环规划和多机协调整合到同一闭环中，试图解决“自主性”和“人类意图”难以兼顾的问题。

#### 方法概述和架构

论文提出一个面向空中机器人团队的沉浸式共享控制框架 Flying Together，核心是基于VR的双向交互界面与实时规划/控制链路。系统上层由用户通过VR中的迁移点或交互标记输入意图，底层将该输入转化为用户力场 F_usr，并送入“用户在环”的 motion-primitive 规划器。该规划器在局部3D voxel map 内进行搜索，以预计算的 motion primitives 组成连续、可行且无碰撞的轨迹，并通过代价函数同时平衡控制代价、障碍惩罚和用户对轨迹方向的偏好。规划输出再与自适应阻抗/导纳控制器耦合，使操作者能够实时影响团队行为，同时保证轨迹平滑与动力学可执行。多机器人层面，系统还通过分布式协调机制处理队形凝聚、速度一致性、轨迹跟踪和障碍规避；同时支持真实与仿真无人机混合运行，并通过低时延通信把机器人状态即时反馈到VR界面。

#### 实验结果分析

从正文描述看，实验验证是在未知/受限环境中的多无人机导航场景下进行，并展示了包含一台真实无人机和两台仿真无人机的混合现实实验。对比结果表明，所提出的共享控制能够改善障碍物规避、维持智能体间距，并降低操作者工作量，说明该方法在沉浸式人机在环多机器人导航中具有可行性与优势。节选内容中未给出具体数值、具体基线名称或消融实验的量化结果，因此可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

尽管自主多机器人系统能够实现安全且协调的导航，但在非结构化环境中，它们往往难以及时适应未预见的情况，也难以捕捉操作者驱动的目标。我们提出一种基于虚拟现实（VR）的共享控制框架，面向在受限且未知环境中运行的无人机团队，用于实现实时、由用户引导的探索。该方法的核心是一种新的、用户引导的、基于 motion primitive 的规划器，它能够在持续融合操作者输入的同时，计算连续且无碰撞的轨迹。该规划器与导纳控制器相结合，使操作者能够灵活影响团队行为，并引导无人机前往自主规划器可能忽略的兴趣区域。系统支持真实无人机与仿真无人机的混合现实运行，并实现了双向的 VR 接口，允许操作者通过迁移点引导机器人团队，同时立即获得团队状态的视觉反馈。实验结果表明，共享控制能够提升障碍规避能力、保持机器人间距，并降低操作者工作量，证明了这种沉浸式、人类在环的多机器人导航方式的可行性及其优势。

</details>

---
