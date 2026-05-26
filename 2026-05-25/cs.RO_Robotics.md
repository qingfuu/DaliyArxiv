# cs.RO | Robotics | 2026-05-25

#arxiv #ComputerScience

**论文数**: 16

### [[20_Research/Papers/强化学习/Robotic_Strawberry_Harvesting_with_Robust_Vision_and_Deep_Reinforcement_Learning_based_Sim-to-Real_Control|Robotic Strawberry Harvesting with Robust Vision and Deep Reinforcement Learning based Sim-to-Real Control]]

![[assets/2605.23863_figure.png|800]]

- **arXiv**: [2605.23863](https://arxiv.org/abs/2605.23863)
- **PDF**: https://arxiv.org/pdf/2605.23863
- **详细分析**: [[20_Research/Papers/强化学习/Robotic_Strawberry_Harvesting_with_Robust_Vision_and_Deep_Reinforcement_Learning_based_Sim-to-Real_Control|Robotic Strawberry Harvesting with Robust Vision and Deep Reinforcement Learning based Sim-to-Real Control]]
- **作者**: Al Bashir, Shao-Yang Chang, Partho Ghose, Prem Raj, Chen-Kang Huang, Azlan Zahid
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 4.5（加权：具身智能 1.2，强化学习 1.8，机器人 1.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

草莓采摘是高价值设施农业中的典型具身操作任务，但果实小、遮挡多、叶茎背景复杂，导致视觉分割、三维定位和机械臂控制都很难稳定完成。现有方案往往依赖通用分割器、IK 或传统运动规划器，在密集果串和环境扰动下容易出现 mask 不准、目标点抖动和轨迹不平滑等问题。本文聚焦“感知—控制”闭环采摘系统，尝试用任务定制视觉与仿真训练的强化学习控制，降低真实硬件试错成本并提升温室场景下的鲁棒性。

#### 方法概述和架构

论文提出一个面向草莓采摘的闭环机器人系统，整体由 RGB-D 感知、三维目标生成、仿真训练控制和 ROS 真实机器人执行四部分组成。感知端使用 HRAttnEdge-YOLO26-seg，对 YOLO26-seg 进行改造：加入 stride-4 的高分辨率 P2 分支、在分割路径上引入注意力机制，并通过带边缘监督的原型学习模块增强实例分割边界质量。模型先对图像中的草莓做实例分割，再结合深度信息和相机内参，把 mask 中心映射为平滑后的三维目标点。控制端在 Isaac Lab 中训练一个目标条件化的 PPO 策略，输入目标信息，输出 UR10e 机械臂的平滑关节位置命令；推理时将策略部署到真实 UR10e 上执行接近与采摘动作。最后通过 ROS 将视觉、目标更新、机械臂运动和末端夹爪采摘流程串联成完整闭环。

#### 实验结果分析

实验在自采数据集和公开数据集上评估了视觉模型，并与多种方法对比；论文报告该模型在分割性能上比对比方法提升约 10% 到 14%，为整体表现最佳。控制部分在受控的室内测试中，与基于 IK 的 MoveIt 基线相比，PPO 控制器的运动更稳定、动态上更平滑。温室实测中，系统共采摘 281 个草莓，达到 96.6% 的到达成功率、91.3% 的抓取并拉取成功率，以及 84.3% 的整体采摘成功率。

<details>
<summary>完整摘要</summary>

本研究提出了一种闭环机器人草莓采摘系统，结合了鲁棒视觉模块、在仿真中训练的深度强化学习（DRL）控制，以及基于 ROS 的真实机器人执行。对于感知部分，我们提出 HRAttnEdge-YOLO26-seg，这是一种改进的 YOLO26-seg 架构，它引入了高分辨率 P2 分支、分割路径注意力以及边缘监督的原型学习，以提升在杂乱场景中的实例分割能力。对于控制部分，我们在 Isaac Lab 中训练了一个目标条件化的 Proximal Policy Optimization（PPO）策略，使其为 UR10e 机械臂生成平滑的关节位置命令，并将其部署到 UR10e 机器人上，用于目标果实的接近与采摘。这种基于仿真的方法减少了对硬件的依赖，降低了开发成本，并允许在真实部署前进行可扩展的策略训练，而无需大量物理试验。所提出的视觉模型在所有评估方法中表现最佳。在自采集数据集和公开数据集上，该模型在分割性能方面提升了 10% 到 14%。在受控的内部测试中，PPO 控制器相比基于逆运动学（IK）的 MoveIt 基线，表现出更稳定且动态上更平滑的运动。在温室试验中，所提出的集成系统共采摘了 281 个草莓，实现了 96.6% 的到达成功率、91.3% 的抓取并拉取成功率以及 84.3% 的整体采摘成功率。这些结果表明，面向任务的感知与仿真训练的 PPO 相结合，可以作为传统依赖规划器的机械臂到达控制的一种实用且资源高效的替代方案，从而在复杂农业环境中实现可靠的闭环机器人采摘。

</details>

---

### [[20_Research/Papers/强化学习/Point_Tracking_Improves_World_Action_Models|Point Tracking Improves World Action Models]]

![[assets/2605.23856_figure.png|800]]

- **arXiv**: [2605.23856](https://arxiv.org/abs/2605.23856)
- **PDF**: https://arxiv.org/pdf/2605.23856
- **详细分析**: [[20_Research/Papers/强化学习/Point_Tracking_Improves_World_Action_Models|Point Tracking Improves World Action Models]]
- **作者**: Jiarui Guan, Wenshuai Zhao, Yue Pei, Ziliang Chen, Arno Solin, Juho Kannala
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

在机器人操作与具身智能中，策略不仅要理解当前画面，还要预测物体、接触和遮挡等动态变化，以便在长时序任务中做出可靠控制。现有基于像素的 world-action model 往往把运动与光照、纹理、背景等无关因素纠缠在一起，导致学到的表示对视觉分布变化、遮挡和出画面运动不够鲁棒。论文关注的核心问题是：如何把动作无关视频中的“未来状态”设计得更适合控制，而不是只追求像素重建。该工作因此值得关注，因为它尝试用显式点轨迹把“可控运动”从外观噪声中解耦出来。

#### 方法概述和架构

论文提出 JOPAT（JOint Pixel-And-Track World-Action Model），把未来视觉潜变量、2D 点轨迹及其可见性、以及机器人动作，统一放进一个去噪扩散 Transformer 中联合建模。输入是当前的 RGB 观测窗口，编码器先得到全局条件特征，再注入到各个 DiT block；模型同时对动作 token、未来视觉 latent token 和轨迹 token 做联合去噪。轨迹部分以当前帧为参考，在图像上采样网格点，并用现成点跟踪器生成未来多个时刻的二维轨迹与可见性标签；随后将轨迹按空间网格重排，采用“track-as-video”的方式做 3D 卷积式 patch 化编码。训练时，JOPAT 用统一的生成目标学习多模态未来状态；推理时则在同一共享序列中同时预测动作和未来状态，使动作生成直接与想象中的轨迹和视觉变化交互。

#### 实验结果分析

论文在 LIBERO 的 40 个仿真操作任务上验证了方法效果，JOPAT 平均成功率达到 97.8%，并在该基准上取得新的 SOTA。作者还在真实世界的 LeRobot 任务上进行了实验，结果表明该方法相较于纯像素基线更稳健，尤其在长时序、遮挡、物体交互和出画面运动相关任务上优势更明显。消融实验进一步说明，联合像素与点轨迹建模比单独使用任一模态更有效，而显式预测轨迹可见性对遮挡和不完整观测场景尤其关键。

<details>
<summary>完整摘要</summary>

机器人策略学习可以从能够刻画环境动力学的 world-action model 中受益，但像素级预测会把动力学与光照、纹理等无关因素纠缠在一起，使学习到的表示容易受到与任务无关的视觉变化影响。为此，我们提出 JOPAT，一种 JOint Pixel-And-Track World-Action Model，它在一个去噪扩散 Transformer 中同时预测潜在视觉观测、带可见性标注的 2D 点轨迹以及动作。其关键思想在于：轨迹为运动提供了显式表示，能够捕捉长时序动力学，并且在遮挡或部分出画面运动时依然保持鲁棒性，因此比单独建模像素外观更有用。在 LIBERO 和真实世界的 LeRobot 任务上，JOPAT 都优于基于像素的基线方法，其中在涉及遮挡、物体交互和出画面运动的长时序任务上提升最为显著。

</details>

---

### [[20_Research/Papers/具身智能/Instrumentation_for_Imitation_Learning_Enhancing_Training_Datasets_for_Clothes_Hanger_Insertion|Instrumentation for Imitation Learning: Enhancing Training Datasets for Clothes Hanger Insertion]]

![[assets/2605.23847_figure.png|800]]

- **arXiv**: [2605.23847](https://arxiv.org/abs/2605.23847)
- **PDF**: https://arxiv.org/pdf/2605.23847
- **详细分析**: [[20_Research/Papers/具身智能/Instrumentation_for_Imitation_Learning_Enhancing_Training_Datasets_for_Clothes_Hanger_Insertion|Instrumentation for Imitation Learning: Enhancing Training Datasets for Clothes Hanger Insertion]]
- **作者**: Remko Proesmans, Thomas Lips, Francis wyffels
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

这篇论文聚焦于机器人服装操作中的“衣架插入”任务，即让机器人将衣架顺利穿入T恤领口并完成悬挂。此类柔性物体操作对感知和控制要求高，但仅依赖视觉往往难以准确判断衣架是否被衣物遮挡、插入是否到位等关键状态。作者认为，将传感器直接集成到物体中进行 instrumentation，可在训练阶段提供更丰富的状态信息，从而缓解具身智能中数据需求高、学习效率低的问题。

#### 方法概述和架构

论文提出一种用于 imitation learning 的 instrumentation 方法：在标准衣架内部集成4个 TCRT5000 反射式红外传感器，作为额外状态输入。机器人系统由双 UR5e 机械臂组成，左臂固定持有T恤，右臂执行衣架插入动作，并通过 Gello 进行遥操作采集数据。策略采用 Diffusion Policy，输入包括双相机图像、机器人关节状态、左侧夹爪开合状态，以及可选的衣架传感器读数；输出为右臂关节位置和左夹爪开合动作。作者分别训练仅视觉策略和带 instrumentation 的策略，并进一步将 instrumented expert 的成功 rollout 以及难例重采样结果加入训练集，形成增强数据集，再训练一个不依赖传感器的 vision-only student 策略。

#### 实验结果分析

实验基于180条遥操作演示，比较了不同数据规模下的 instrumented policy 与 vision-only policy。结果表明，使用 instrumentation 的策略在成功率上比纯视觉基线高出14–25 个百分点，并表现出更强的任务意识。更重要的是，黑箱 imitation learning 策略会在训练中自动学会优先利用传感器信号，即使没有显式指导。通过将 instrumented expert 的 rollout 加入训练集，vision-only student 策略的表现可达到与 instrumented expert 相当，并超过原始 vision-only 策略；可见文本未给出具体数值，但论文明确展示了该数据增强策略的有效性。

<details>
<summary>完整摘要</summary>

大型行为模型已经改变了机器人操作领域，但高昂的数据需求迄今阻碍了类似视觉语言模型那样的革命。我们认为，instrumentation，即在物体中集成传感器，可以提供极其有价值的状态信息，并促进机器人操作的高效学习。本文提出了用于衣架插入任务的 instrumentation imitation learning。我们使用180条遥操作演示，分别在有无 instrumentation 数据的情况下训练 diffusion policy。结果显示，利用 instrumentation 的策略相比仅视觉策略高出14–25 个百分点，并且表现出更强的任务意识。关键的是，一个黑箱 imitation learning 策略无需显式指导就能学会优先利用 instrumentation 信号。此外，通过将 instrumented “expert” 策略的 rollout 作为额外数据增强遥操作训练集，可以让一个仅视觉的 “student” 策略达到与 instrumented expert 相当的性能，并超过原始仅视觉策略。这些发现表明，instrumentation 是增强机器人操作 imitation learning 的一种很有前景的策略。数据集已在 Zenodo 上公开。

</details>

---

### [[20_Research/Papers/机器人/SFG-ROS_A_Resource-Aware_Framework_for_Dense_Multi-Agent_Perception|SFG-ROS: A Resource-Aware Framework for Dense Multi-Agent Perception]]

![[assets/2605.23832_figure.png|800]]

- **arXiv**: [2605.23832](https://arxiv.org/abs/2605.23832)
- **PDF**: https://arxiv.org/pdf/2605.23832
- **详细分析**: [[20_Research/Papers/机器人/SFG-ROS_A_Resource-Aware_Framework_for_Dense_Multi-Agent_Perception|SFG-ROS: A Resource-Aware Framework for Dense Multi-Agent Perception]]
- **作者**: Constantin Blessing, Elias Geiger, Jakob Häringer, Dennis Grewe, Markus Enzweiler
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.4，机器人 1.3）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

在多机器人协同感知中，异构机器人车队需要频繁交换高密度传感器流与状态信息，才能支持实时协作、巡检和物料流转等任务。现有 ROS 2 虽然是机器人中间件的事实标准，但在多机密集部署时容易出现网络拥塞、命名空间冲突以及大规模传感数据分发带来的计算开销过高等问题。尤其是在 LiDAR、双目深度相机等高带宽传感器场景下，默认的发现机制和重复解压流程会迅速成为系统瓶颈，因此这项工作聚焦于“资源受限条件下的密集多智能体感知”这一非常实际的问题。

#### 方法概述和架构

论文提出 SFG-ROS，一个面向动态车队部署的资源感知型多智能体软件框架。其核心是“本地原始、全局压缩”的通信范式：机内局部处理保留原始数据流，而跨机器人通信则通过压缩后的全局桥接域传输。方法上，框架首先用基于 FQN 的命名与路由 schema，将高频的机内流量和跨机流量分离，并借助 Fast DDS Router 只转发特定主题、服务与 TF 相关消息，从而限制全局网络流量。其次，它引入按需集中解码流水线，在需要多个订阅者消费同一高带宽数据时，由中心节点统一解压，再通过轻量级 IPC 分发，避免每个订阅者重复解压。最后，框架还提供硬件无关的容器化部署流水线，可动态适配不同加速器与异构平台，把开发环境和可直接上现场的零接触部署连接起来。

#### 实验结果分析

论文在由轮式与足式机器人组成的车队上进行了实验，传感器包括 LiDAR 和双目深度相机，验证了系统在密集多机器人感知场景中的可行性。结果显示，SFG-ROS 能将网络流量限制为 𝒪(1) 级别，并且相较标准 ROS 2，通过用轻量级 IPC 替代重复解压，使每个订阅者的 CPU 扩展惩罚降低了 72.3%，同时保持较低时延。文中还强调框架以宽松许可证公开发布，但节选文本未给出更细的消融或泛化数值。

<details>
<summary>完整摘要</summary>

部署由异构机器人组成的多智能体车队以开展协同感知，需要稳健的数据交换机制和可扩展的软件架构。然而，标准 ROS 2 实现通常会在跨设备分发密集传感器流时遭遇网络拥塞、命名空间冲突以及严重的计算开销。为了解决这些瓶颈，我们提出 SFG-ROS，这是一个面向动态车队部署、并且具有资源感知能力的多智能体软件框架。SFG-ROS 通过三项主要贡献来应对这些挑战。第一，基于 schema 的流量路由使用程序化的完全限定名（FQN）命名规则和定向的 Fast DDS 路由，将高频的机内流量与全局网络隔离。第二，按需的集中式解码流水线可自动卸载高带宽传感器数据的解压任务，消除本地消费者节点之间重复处理带来的开销。最后，一个与硬件无关的容器化流水线能够动态适配异构加速器，实现从开发环境到零接触、可直接上现场执行的无缝衔接。我们使用配备 LiDAR 和双目深度相机的轮式与足式机器人车队对该框架进行了评估。实验结果表明，SFG-ROS 可将网络流量限制为 𝒪(1)；并且通过用轻量级 IPC 替代重复解压，相比标准 ROS 2 将每个订阅者的 CPU 扩展惩罚降低了 72.3%，同时保持了较低时延。最后，我们以宽松许可证发布了 SFG-ROS，可通过 iis-esslingen.github.io/sfg-ros 获取。

</details>

---

### [[20_Research/Papers/强化学习/Direct_Dynamic_Retargeting_for_Humanoid_Imitation_Learning_from_Videos|Direct Dynamic Retargeting for Humanoid Imitation Learning from Videos]]

![[assets/2605.23762_figure.png|800]]

- **arXiv**: [2605.23762](https://arxiv.org/abs/2605.23762)
- **PDF**: https://arxiv.org/pdf/2605.23762
- **详细分析**: [[20_Research/Papers/强化学习/Direct_Dynamic_Retargeting_for_Humanoid_Imitation_Learning_from_Videos|Direct Dynamic Retargeting for Humanoid Imitation Learning from Videos]]
- **作者**: Constant Roux, Ludovic De Matteïs, Armand Jordana, Valentin Guillet, Nicolas Mansard, Olivier Stasse, Philippe Souères
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

人形机器人从单目视频演示中学习动作，是一种可扩展的技能获取方式，尤其适合复杂的行走、平衡和操作任务。但人类与机器人在身体尺寸、肢体比例、质量分布、关节约束和动力学能力上存在明显差异，直接把人类视频动作迁移到机器人上往往会产生不可执行或效果较差的轨迹。现有方法通常先做几何重定向，再做动力学修正，这种两阶段流程会引入“几何偏置”，把搜索空间限制在不理想的中间结果附近，导致最终轨迹次优。本文之所以值得关注，在于它试图绕过这一中间投影步骤，直接从视频生成物理可行的人形机器人参考轨迹，并进一步服务于后续强化学习训练。

#### 方法概述和架构

论文提出 Direct Dynamic Retargeting（DDR），将重定向问题直接定义在任务空间中，而不是先求几何上最接近的人体姿态。其输入是从单目视频中提取的人体关键点轨迹，作者采用 VideoMimic 的 SMPL 解析流程得到包含躯干、肩部、手和脚等关键点的时序表示。DDR 在物理仿真器中使用基于采样的 MPC 求解器，结合 Cross-Entropy Method（CEM）直接优化机器人控制序列，使输出轨迹同时满足动力学可行性和接触序列约束。与 Geometric Retargeting（GR）和 Indirect Dynamic Retargeting（IDR）不同，DDR 不再依赖中间的 IK/几何参考，而是直接最小化机器人轨迹关键点与人类参考之间的距离。随后，作者还将这些物理可行的参考轨迹用于强化学习中的模仿训练，以便学习到更稳定、可迁移的闭环策略。

#### 实验结果分析

实验在多种动态动作上比较了 DDR、GR 和 IDR 等基线，评估了轨迹可行性、接触序列、脚部打滑、成功率以及参考跟踪误差等指标。结果显示，DDR 在示范跟踪精度和物理一致性上优于现有方法，说明绕开几何偏置确实能带来更优的动态重定向效果。作者还验证了：当把 DDR 生成的物理可行参考交给 RL 代理训练时，训练收敛更快，最终在敏捷动作和平衡动作上的执行效果也更好。文中还提到可在 Unitree H1-2 上实现零样本 sim-to-real 部署；但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

从单目视频演示中进行模仿学习，为向人形机器人教授复杂技能提供了一种可扩展的方法。然而，将人类动作转换为人形机器人动作，需要克服显著的形态差异。标准方法通常依赖几何重定向或间接动力学重定向流程。我们发现，这些中间的运动学投影会引入几何偏置，限制搜索空间，并产生次优的动态行为。本文提出 Direct Dynamic Retargeting（DDR），这是一种新颖的单阶段框架，能够直接从专家视频生成高保真、动力学可行的轨迹。DDR 将问题表述在任务空间中，并在物理仿真器内利用基于采样的模型预测控制（MPC）求解器，从而原生地优化复杂的接触序列，同时缓解输入漂移问题。实验表明，绕开几何偏置后，DDR 在演示跟踪精度上优于当前最先进的基线方法。此外，我们还证明，向强化学习智能体提供这类物理可行的参考轨迹，可以加快训练收敛，并提升敏捷和平衡行为的最终执行效果。源代码将公开发布。

</details>

---

### [[20_Research/Papers/强化学习/Vision-Based_Agile_Landing_on_Turbulent_Waters|Vision-Based Agile Landing on Turbulent Waters]]

![[assets/2605.23717_figure.png|800]]

- **arXiv**: [2605.23717](https://arxiv.org/abs/2605.23717)
- **PDF**: https://arxiv.org/pdf/2605.23717
- **详细分析**: [[20_Research/Papers/强化学习/Vision-Based_Agile_Landing_on_Turbulent_Waters|Vision-Based Agile Landing on Turbulent Waters]]
- **作者**: Dimosthenis Angelis, Leonard Bauersfeld, Davide Scaramuzza, Evangelos Boukas
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: RL

#### 研究背景与动机

无人机在海上搜救、巡检和监视等任务中非常实用，但其续航有限，常常需要依靠海上船舶或浮动平台进行回收降落。海况恶劣时，机体与甲板都会发生耦合运动，若还要求系统显式估计平台状态并依赖规则化视觉标志或通信信息，落地难度会进一步上升。本文关注的是：在湍流海面上，如何仅凭机载视觉与自身状态，实现多旋翼无人机对移动海上平台的敏捷自主降落。

#### 方法概述和架构

论文提出一种基于强化学习的视觉引导降落方法 Vision-Based Agile Landing on Turbulent Waters。策略网络的输入包括无人机自身状态（姿态、线速度、角速度）、前后两个时刻的下视相机图像中提取的稀疏局部特征，以及上一时刻动作，用于隐式推断平台相对运动。视觉分支并不直接依赖固定目标，而是使用关键点及其描述子构成的共享归一化特征接口，因此可在不同本地特征提取器之间零样本迁移。策略输出滚转、俯仰、偏航和总推力指令，再由传统低层姿态控制器跟踪执行。训练阶段在仿真中用合成关键点和随机归一化描述子进行学习，环境中的平台运动被建模为沿 heave、roll、pitch、yaw 的正弦激励；奖励函数同时包含接近平台、保持目标在视野中、动作平滑、近平台姿态/速度对齐以及成功/失败终止项。

#### 实验结果分析

作者在高保真仿真和真实世界中都验证了该方法，并与一类先进的 MPC 基线进行比较。结果显示，在相当于“Very Rough”海况的平台运动下，所提方法优于 MPC 基线；真实实验中还使用了两种不同的局部特征提取器完成机载自主降落。文中强调该方法在不依赖显式平台状态表示的前提下，实现了湍流海面上敏捷多旋翼降落，据可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

开放海域条件下，无人机在海上船舶上的自主降落极具挑战，因为飞行器与降落平台之间存在耦合运动。本文提出一种基于强化学习的方法，用于多旋翼无人机在移动海上平台上的自主降落，且不需要显式的平台状态信息。该方法结合多旋翼自身状态测量与局部视觉特征——即从降落表面提取的关键点及其对应描述子——来预测姿态和推力指令，这些指令再由传统低层控制器进行跟踪。策略在仿真中使用合成关键点及随机生成的归一化描述子进行训练，从而可以零样本部署到搭载不同局部特征提取器的无人机上。我们在一个逼真的模拟器中评估该方法，结果表明它在对应“Very Rough”海况的平台运动下优于当前最先进的模型预测控制（MPC）基线。最后，我们进行了大规模真实世界实验，展示了使用两种不同局部特征提取器的机载自主降落。就我们所知，这是首个在湍流海面上实现海上平台敏捷多旋翼降落、且不依赖显式平台状态表示的方法。

</details>

---

### [[20_Research/Papers/具身智能/TactileReflex_Noise-Statistics-Driven_Vision-Tactile_Reflex_Control_for_Force-Sensitive_Manipulation|TactileReflex: Noise-Statistics-Driven Vision-Tactile Reflex Control for Force-Sensitive Manipulation]]

![[assets/2605.23568_figure.png|800]]

- **arXiv**: [2605.23568](https://arxiv.org/abs/2605.23568)
- **PDF**: https://arxiv.org/pdf/2605.23568
- **详细分析**: [[20_Research/Papers/具身智能/TactileReflex_Noise-Statistics-Driven_Vision-Tactile_Reflex_Control_for_Force-Sensitive_Manipulation|TactileReflex: Noise-Statistics-Driven Vision-Tactile Reflex Control for Force-Sensitive Manipulation]]
- **作者**: Ziyan Feng, Yulong Fu, Zheng Li, Yuxin He, Jieji Ren, Lujia Wang, Jinni Zhou, Yudong Zhong, Qiang Nie
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.9，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

在抓取装有液体的薄壁易变形容器（如一次性塑料杯）时，机器人需要在极小的力窗口内实时调节夹持力：力太小会打滑掉落，力太大又会造成不可逆挤压变形。这类任务对视觉或传统力控都很苛刻，因为容器透明、壁薄且负载会随液体流动不断变化。论文关注的是如何在不依赖外部力标定和人工调参的前提下，实现稳定、可解释、可直接插入现有操作流水线的安全抓取控制，因此具有较强的机器人落地价值。

#### 方法概述和架构

论文提出 TactileReflex，一种基于“噪声统计驱动标定”的视觉触觉反射控制方法。系统使用双侧 MC-Tac 视觉触觉传感器，从触觉图像中提取三个图像级代理量：剪切强度 S_y、接触强度 F_n 和压力中心 C，并以此作为闭环控制信号。控制流程先通过短暂的静置保持与卸载协议，统计传感器自身噪声分布，再用分位数阈值自动确定所有控制门限，避免外部力传感器标定和经验调参。运行时，系统按优先级串联三个反射通道：最高优先级的力保护通道限制接触强度，其次是防滑通道抑制剪切滑移，最后是自适应释放通道在负载减小时放松夹持；各通道直接基于对应代理量闭环，推理频率约为 12 Hz。

#### 实验结果分析

实验在真实机器人平台上验证了该方法的有效性，包括阈值标定与信号验证、三通道必要性的消融实验，以及动态倒水任务。结果显示，跨材料标定能够实现 100% 真阳性率和 0% 假阳性率的滑移检测；在消融实验中，只有完整三通道系统才能避免容器发生不可逆变形，成功率为 5/5，而部分配置最多仅 1/5。动态倒水任务中，固定力度基线因位姿漂移在 10 次尝试中全部失败，而 TactileReflex 在两种水量设置下取得 9/10 成功。

<details>
<summary>完整摘要</summary>

操控装有液体的易碎可变形容器，例如一次性塑料杯，需要在极其狭窄的力范围内实时自适应夹持力：力不足会导致打滑，而力过大则会使薄壁发生不可逆变形。现有方法难以胜任这类对力敏感的操作任务。为此，我们提出一种基于噪声统计的标定驱动反射控制范式，并结合视觉触觉传感：通过分析传感器的内在噪声特性（采用简短的静置保持与卸载流程），我们可以直接推导出所有控制器阈值，从而避免外部力标定、试错式人工调参以及针对特定材料的物理模型。基于这一范式，我们进一步提出 TactileReflex——一种三通道闭环控制器，它从双视觉触觉传感器中提取三个图像级代理量：剪切强度 S_y、接触强度 F_n 和压力中心 C，并以约 12 Hz 的频率驱动优先级反射通道，实现防滑抑制、负载自适应释放和力保护。每个通道都直接围绕其对应代理量，并通过噪声推导的阈值闭环控制。消融实验表明，只有完整的三通道系统才能防止容器发生不可逆变形（5/5 成功，而部分配置最多仅 1/5）。在动态倒水任务中，固定力度基线由于位姿漂移在 10 次尝试中全部失败，而 TactileReflex 在两种水量下实现了 9/10 的成功率。作为一个自包含且可解释的控制器，TactileReflex 可以作为即插即用的安全层，置于更高层的操作流水线之下，包括无触觉反馈的 VR 远程操控和视觉-语言-动作（VLA）策略。

</details>

---

### [[20_Research/Papers/具身智能/Semantically_Structured_Mixture-of-Experts_for_Compositional_Robotic_Manipulation|Semantically Structured Mixture-of-Experts for Compositional Robotic Manipulation]]

![[assets/2605.23477_figure.png|800]]

- **arXiv**: [2605.23477](https://arxiv.org/abs/2605.23477)
- **PDF**: https://arxiv.org/pdf/2605.23477
- **详细分析**: [[20_Research/Papers/具身智能/Semantically_Structured_Mixture-of-Experts_for_Compositional_Robotic_Manipulation|Semantically Structured Mixture-of-Experts for Compositional Robotic Manipulation]]
- **作者**: Chengyu Deng, Guanqi Chen, Yizhou Chen, Zejia Liu, Zhiwen Ruan, Guanhua Chen, Jia Pan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

在机器人操作中，基于扩散模型的策略已经能实现较高精度的动作生成，但一旦扩展到多任务、长流程和多阶段操作，模型就会面临“效果、泛化、效率”三者难以兼顾的瓶颈：高性能模型计算开销大，而轻量模型又常常难以在不同任务间稳定迁移。现有 Mixture-of-Experts（MoE）虽能通过稀疏激活提高推理效率，但很多路由方法只依赖噪声或潜变量统计，没有显式利用操作任务天然的“技能组合”结构，容易把可复用行为切碎到不同专家中。本文之所以值得关注，在于它试图把机器人操作中的语义技能结构直接引入路由机制，从而同时提升可解释性、参数效率与跨任务组合泛化能力。

#### 方法概述和架构

论文提出 Semantically Structured Mixture-of-Experts Diffusion Policy（SMoDP），用于组合式机器人操作。整体流程分为两部分：首先利用 VLM 在离线阶段自动把示范轨迹切分为带语义的技能片段，技能以动词-名词对形式表示，如“抓起红杯子”，从而获得训练时的技能监督；推理时不再调用 VLM。其次，模型加入一个轻量级的在线技能预测器，它根据当前多模态观测和语言指令预测即将执行的技能，再据此把动作 chunk 路由给对应的专家子网络进行扩散去噪。为了让路由更加稳定，作者设计了双重对比学习：一方面通过跨模态对齐把观测表示与语言定义的技能语义拉近，另一方面通过同模态对比约束，让语义相近、功能相关的技能产生一致的路由分布，促进专家复用与一致性。训练时，SMoDP同时优化行为克隆式的扩散策略目标、技能预测和路由正则；推理时只需技能预测器与 MoE 路由器即可完成高效控制。

#### 实验结果分析

实验部分在多任务基准 LIBERO-10 和 LIBERO-90 上评估了模型，并与代表性的扩散策略和 MoE 基线进行比较，重点关注多任务性能与参数效率。作者还在真实机器人任务以及任务迁移设置中验证了方法的效果，包括从 LIBERO-90 迁移到 LIBERO-10、以及从 LIBERO-OBJECT/GOAL 迁移到 LIBERO-GOAL-OOD 的组合泛化。结果表明，SMoDP 在多任务基准上优于对比方法，同时参数利用更高效；消融实验也支持语义路由、双对比对齐和技能抽象对性能的贡献。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

基于扩散模型的策略已经为精确机器人操作建立了新的标准，但它们面临一个关键的可扩展性瓶颈：高性能模型计算代价高昂，而轻量化替代方案往往难以在多样化的多任务环境中泛化。Mixture-of-Experts（MoE）架构通过只激活部分参数，为提升效率提供了一个很有前景的方向。然而，现有 MoE 路由机制通常依赖低层级噪声或潜变量统计，忽视了操作任务的组合性结构。这会把可复用行为分散到不同专家中，限制模型的可解释性与可迁移性。为此，我们提出用于组合式机器人操作的语义结构化 MoE 扩散策略（Semantically Structured Mixture-of-Experts Diffusion Policy, SMoDP），该框架将专家专长建立在语义化的任务结构之上。SMoDP 借助一个轻量级的、在推理阶段使用的技能预测器，并用来自 Vision-Language Models（VLMs）的离线标注进行监督，从而将动作 chunk 路由给专门对应特定行为阶段的专家。为了确保稳健的分配，我们提出了一种双重对比对齐策略：其一是在跨模态层面，将多模态观测与语言定义的技能语义对齐；其二是在同模态层面，约束视觉上不同但功能相关的行为具有一致的路由分布。我们的方法在多任务基准上优于代表性的扩散和 MoE 基线，并显著提升了参数效率，同时还能通过参数高效微调，将已学技能组合迁移到新任务上。项目主页：https://deng-cy20.github.io/SMoDP/

</details>

---

### [[20_Research/Papers/具身智能/Droneulator_A_Portable_UAV_Simulator_for_Agricultural_Workflows_with_RotorPy_and_Godot_4|Droneulator: A Portable UAV Simulator for Agricultural Workflows with RotorPy and Godot 4]]

![[assets/2605.23386_figure.png|800]]

- **arXiv**: [2605.23386](https://arxiv.org/abs/2605.23386)
- **PDF**: https://arxiv.org/pdf/2605.23386
- **详细分析**: [[20_Research/Papers/具身智能/Droneulator_A_Portable_UAV_Simulator_for_Agricultural_Workflows_with_RotorPy_and_Godot_4|Droneulator: A Portable UAV Simulator for Agricultural Workflows with RotorPy and Godot 4]]
- **作者**: Jacob Swindell, Michael Lowen, Marija Popovic, Riccardo Polvara
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 2.0（加权：具身智能 0.3，强化学习 0.2，机器人 1.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

农业场景中的 UAV 研究同时需要逼真的三维果园环境、足够可信的飞行动力学，以及能够直接对接 ROS 2、PX4 和强化学习工具链的中间件支持，但现有模拟器往往只覆盖其中一部分能力。对于树冠巡检、障碍物周边局部规划和数字孪生数据采集等任务，实地测试成本高、约束多，因此一个可移植、易部署且能兼顾感知、控制与学习的统一模拟平台尤其重要。本文聚焦这一缺口，尝试把农业 UAV 的三类典型工作流放进同一套可落地的仿真栈中。

#### 方法概述和架构

论文提出 Droneulator，一个结合 RotorPy 与 Godot 4 的可移植 UAV 仿真架构，其中 RotorPy 负责多旋翼动力学，Godot 4 负责三维场景渲染与传感器生成。系统将动力学循环打包为独立可执行程序，并由 Godot 以子进程方式启动，从而减少主机环境依赖；状态、姿态与控制指令通过 WebSocket 进行交换。感知侧使用三相机配置输出 RGB、深度和语义分割图，同时结合 RotorPy 的里程计、TF 和相机信息，经过基于 Zenoh 的管线发布为 ROS 2 兼容格式。控制侧同时支持 PX4 SITL 以及轻量级 WebSocket 命令通道，前者用于与现有 ROS 2/PX4 工具链联动，后者支持定点巡航和强化学习中的连续速度控制。作者还把系统封装为跨平台、低依赖的部署结构，使仿真器可以在不同开发机器上直接运行。

#### 实验结果分析

作者在 x86 Linux 桌面机上，对 Droneulator 的三类农业工作流做了定量验证：基于 COLMAP 的树木尺度三维重建、基于 EGO-Planner 的树冠障碍物局部规划，以及自定义 Gymnasium 环境中的闭环强化学习。测得 Zenoh 到 ROS 2 桥接的端到端时延较低：里程计均值约 0.45 ms，RGB 约 5.65 ms，深度约 17.06 ms，满足 30 Hz 更新需求。重建实验显示，随着采样视角从 18 提升到 54 张，稠密点数显著增加且重投影误差下降，但收益存在边际递减；规划实验中，5 次 EGO-Planner 运行均能绕开中央树障碍并到达目标，最小障碍物间距约为 0.28 m。

<details>
<summary>完整摘要</summary>

农业 UAV 研究需要能够集成逼真的三维场景、高保真车辆动力学和机器人中间件，同时还要便于在异构开发机器上实际部署。为此，我们提出 Droneulator，一种将 RotorPy 用于多旋翼动力学、Godot 4 用于渲染与传感器生成的可移植 UAV 仿真架构。Droneulator 同时提供基于 PX4 的控制接口和一个轻量级 WebSocket 命令通道，并通过基于 Zenoh、与 ROS 2 兼容的管线发布同步的视觉流和状态流。这样的集成使得同一套系统无需修改仿真基础设施，就能支持面向巡检的数据采集、ROS 2/PX4 本地规划以及强化学习实验。我们对当前系统在三类农业 UAV 工作流上进行了定量验证：使用 COLMAP 进行树木尺度图像采集与三维重建、使用 EGO-Planner 在树冠障碍物周围进行局部规划，以及通过自定义 Gymnasium 环境进行闭环强化学习。实验结果表明，该仿真器能够维持低时延感知，在不同采集密度下支持面向重建的数据采集，执行绕开树冠障碍物的无碰撞局部规划，并支持基于深度感知的稳定策略训练，用于具备障碍物感知的导航。总体而言，这些结果表明，Droneulator 有潜力在一个可部署的统一栈中同时支撑农业 UAV 的巡检、规划与学习任务。

</details>

---

### [[20_Research/Papers/机器人/Signal_Temporal_Logic_Motion_Planning_via_Graphs_of_Convex_Sets|Signal Temporal Logic Motion Planning via Graphs of Convex Sets]]

![[assets/2605.23240_figure.png|800]]

- **arXiv**: [2605.23240](https://arxiv.org/abs/2605.23240)
- **PDF**: https://arxiv.org/pdf/2605.23240
- **详细分析**: [[20_Research/Papers/机器人/Signal_Temporal_Logic_Motion_Planning_via_Graphs_of_Convex_Sets|Signal Temporal Logic Motion Planning via Graphs of Convex Sets]]
- **作者**: Yu Chen, Ancheng Hou, Mingyang Feng, Xiao Yu, Xiang Yin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.6，机器人 1.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

在机器人任务与运动规划中，除了要保证轨迹在几何和动力学上可执行，还常常需要满足“在什么时候到达哪里、持续多久、按什么顺序完成”等高层逻辑与时序约束。Signal Temporal Logic（STL）正适合描述这类需求，但现有基于时间离散化的 STL 规划方法通常会变成规模庞大的混合整数优化问题，在长时域任务和高维机器人系统上难以扩展。另一方面，Graphs of Convex Sets（GCS）擅长生成平滑连续轨迹并具有较好的可扩展性，但此前主要用于避障、到达-规避等经典规划任务，对 STL 这类富时序逻辑约束的支持有限。因此，如何把 STL 的形式化时序约束与 GCS 的连续轨迹优化优势结合起来，是本文关注的核心问题。

#### 方法概述和架构

本文提出一种基于“时序自动机 + GCS”的 STL 运动规划框架。首先，将 STL 规格表示为 timed automaton，用以编码任务的逻辑结构、时间区间和进度状态；随后对配置空间进行凸分解，并把自动机状态与机器人所处凸区域联合起来，构造一个同时记录“任务进展”和“区域占用”的联合转移系统。基于该联合系统，作者把 STL 规划问题重写为 GCS 上的最短路径问题：图中的路径选择决定离散任务顺序，而每条边上的凸约束则用于连接相邻凸区域并满足运动约束。求解后，路径会直接诱导出一条连续时间的 Bézier-spline 轨迹，同时满足 STL 规格、平滑性要求和速度上界。除了通用框架外，论文还针对一个具有代表性的 STL 片段设计了紧凑的 timed-automaton 构造方法，通过模板化的原子时序模式和布尔组合减少自动机规模。

#### 实验结果分析

作者在低维基准、3D 四旋翼、30-DoF 人形机器人，以及 UR-3 机械臂硬件实验上验证了方法有效性，表明该框架可以处理较复杂的 STL 运动规划任务并生成可直接执行的平滑轨迹。实验覆盖了二维/三维仿真、高维人形机器人以及真实机器人平台，展示了方法对不同维度与任务复杂度的适应能力。与相关 STL 规划思路相比，该方法兼顾了形式化任务满足与连续轨迹平滑性；但从给出的节选来看，可见文本未给出具体数值结果。

<details>
<summary>完整摘要</summary>

本文研究在 Signal Temporal Logic（STL）规格约束下的连续时间运动规划问题。目标是在满足高层逻辑与时序要求的同时，生成平滑的机器人轨迹，并遵守低层运动约束。为此，我们提出了一种将 timed automata 推理与 Graphs of Convex Sets（GCS）相结合的高效框架。首先，将 STL 规格表示为一个 timed automaton，然后将其与配置空间的凸分解耦合，形成一个联合转移系统，用以同时编码任务进展和区域占用。基于该联合转移系统，我们把 STL 运动规划问题重新表述为 GCS 上的最短路径问题，其解会诱导出一条平滑的 Bézier-spline 轨迹，从而满足 STL 规格、平滑性要求以及速度约束。我们证明了所提表述的正确性，并分析了其计算复杂度，表明在 timed automaton 和凸分解固定后，凸松弛对配置空间维度和 Bézier 阶数具有多项式规模的扩展性。我们进一步针对一个表达能力较强的 STL 片段，利用专门的模板和布尔组合开发了紧凑的 timed automaton 构造方法。数值实验包括低维基准任务、3D 四旋翼、30-DoF 人形机器人，以及在 UR-3 机械臂上的硬件实验，结果表明该方法能够高效求解复杂的 STL 运动规划问题，并生成平滑、可执行的轨迹。

</details>

---

### [[20_Research/Papers/具身智能/$π_0$-EqM_Equilibrium_Matching_for_Closed-Loop_Vision-Language-Action_Control|$π_0$-EqM: Equilibrium Matching for Closed-Loop Vision-Language-Action Control]]

![[assets/2605.23128_figure.png|800]]

- **arXiv**: [2605.23128](https://arxiv.org/abs/2605.23128)
- **PDF**: https://arxiv.org/pdf/2605.23128
- **详细分析**: [[20_Research/Papers/具身智能/$π_0$-EqM_Equilibrium_Matching_for_Closed-Loop_Vision-Language-Action_Control|$π_0$-EqM: Equilibrium Matching for Closed-Loop Vision-Language-Action Control]]
- **作者**: Huanming Liu, Congsheng Xu, Jianmin Ji, Yao Mu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

在具身智能和机器人操作中，Vision-Language-Action（VLA）模型已经成为重要范式，因为它能把视觉观测和语言指令直接映射为动作，并具备较强的任务泛化能力。但现有许多基于 flow-matching 的动作解码器通常采用固定采样步数，在闭环控制里会带来两个问题：不同状态其实需要不同计算量，而且相邻控制周期之间存在强时间相关性，却难以有效复用上一步的迭代结果。本文值得关注之处在于，它把“推理深度”从实现细节提升为策略设计的一部分，并尝试用一种时间无关的平衡求解视角重构 VLA 动作生成。

#### 方法概述和架构

论文提出 π_0-EqM，用 Equilibrium Matching（EqM）解码器替换 π_0 中原有的 flow-matching 动作专家，同时保持上游 VLA 表征与条件接口不变。EqM 将动作块生成建模为迭代求平衡：输入为当前时刻的多模态条件 c_t（图像、语言、状态等），输出为一个动作块 A_t，而不是单步动作；训练时用演示动作与高斯噪声构造插值样本，学习一个时间无关的条件向量场，使真实动作块成为稳定平衡点。推理时通过 Nesterov 加速的迭代更新去求解 f_θ(A; c_t)=0，并以归一化残差作为停止准则，从而实现自适应推理深度。由于 EqM 不依赖固定噪声/时间轴，作者进一步设计了跨控制周期的 warm-start：把上一个动作块的前半段复用到当前初始化中，后半段重新采样，以利用闭环中的时序连续性。论文还给出了局部势能下降和收缩性分析，用于解释残差阈值停止和 warm-start 为什么能减少迭代步数。

#### 实验结果分析

实验在 19 个任务的 RoboTwin 上进行，对比原始 π_0 与 π_0-EqM，并使用匹配的 300 步推理预算；结果显示 EqM 将平均成功率从 40.4% 提升到 50.2%，在 19 个任务里有 12 个任务提升。作者还在 LIBERO 的多个子集上验证了方法，整体表现与基线相当或略优，其中 LIBERO-10 的提升最明显，说明该方法对更长时序任务更有帮助。阈值扫描进一步发现，残差下降与任务成功之间并非单调对应，存在任务相关的“stationarity-executability gap”；可见文本未给出该部分的完整数值细节。

<details>
<summary>完整摘要</summary>

目前，Vision-Language-Action（VLA）模型因其在任务泛化方面的巨大潜力，已经成为机器人操作中最常用的范式。尽管如此，许多用于 VLA 控制的生成式 flow-matching 动作解码器通常采用固定的采样步数进行部署，这限制了其在不同状态下按需分配计算，以及在控制周期之间进行时间复用的能力。为此，我们提出 π_0-EqM：在保持上游 VLA 结构不变的前提下，用一个 Equilibrium Matching（EqM）解码器替换 π_0 中的 flow-matching 专家。在匹配的 300 步预算下，π_0-EqM 在 RoboTwin 的 19 个任务上将平均成功率从 40.4% 提升到 50.2%，并在 LIBERO 上保持有竞争力，其中在 LIBERO-10 上的提升最为明显，达到 87.0%。两组阈值扫描结果揭示了残差与成功率之间存在任务相关的非单调关系，我们将其称为“stationarity-executability gap”。这些结果表明，在迭代式 VLA 控制中，推理深度本身就是策略设计的一部分，并引入了一种基于能量的 VLA 视角，可能为未来跨任务、跨形体的可组合动作生成研究提供启发。

</details>

---

### [[20_Research/Papers/机器人/Four_Simple_Proprioceptive_Estimators_for_Legged_Robots|Four Simple Proprioceptive Estimators for Legged Robots]]

![[assets/2605.23100_figure.png|800]]

- **arXiv**: [2605.23100](https://arxiv.org/abs/2605.23100)
- **PDF**: https://arxiv.org/pdf/2605.23100
- **详细分析**: [[20_Research/Papers/机器人/Four_Simple_Proprioceptive_Estimators_for_Legged_Robots|Four Simple Proprioceptive Estimators for Legged Robots]]
- **作者**: Frank Dellaert, Chiyun Noh, Varun Agrawal, Ayoung Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

腿式机器人通常依赖 IMU 做高频惯性导航，但消费级 IMU 噪声较大，纯惯性积分会快速漂移。与此同时，机器人足端与环境的间歇接触能提供强几何约束，用来抑制漂移，因此如何把“惯性信息 + 足端接触”稳定结合，是腿式机器人本体感知定位的关键问题。本文值得关注之处在于，它不是单纯追求更复杂的系统，而是系统性比较了四种由简到繁、可复现的估计器实现，便于后续研究和工程复用。

#### 方法概述和架构

论文提出了四种逐步增强的 proprioceptive state estimator，核心状态都包含姿态、位置、速度以及 IMU bias，并把足端接触建模为导航系中的临时地标。第一种方法是基于 Hartley 等人的 contact-aided invariant EKF，但将接触更新改为事件驱动：只在 touchdown 发生或距离上次更新超过一定时间时才进行接触校正。第二种方法保留同样的预测模型，但把顺序式 measurement update 替换为一个小型 factor graph，对当前时刻的 prior、多个接触因子以及可选高度先验做一次联合优化。第三种方法进一步把这个局部图扩展成 fixed-lag smoother，在短时间窗口内保留最近历史，并将 foothold 显式作为导航系变量。第四种方法在 smoother 中让 IMU bias 也随时间演化，用 Markov chain 描述偏置轨迹，从而得到更灵活的时变偏置模型。作者还提供了 GTSAM 版本和 ROS2 兼容实现，便于直接复现与集成。

#### 实验结果分析

实验部分将这四个 GTSAM 变体与已有腿式-IMU 里程计方法进行比较，评估场景和数据集在节选中已提及，但可见文本未给出具体数值。作者重点分析了事件驱动接触更新、局部图更新、fixed-lag smoother 以及时变 bias 建模等设计带来的差异。文中明确指出，事件驱动的接触更新在实验中表现更好，相比高频接触更新出现了更少的漂移。整体结论是：在不使用关节角直接作为测量的前提下，利用足端接触与惯性信息的简单组合，已经能够构建出一套清晰、模块化且更易复现的腿式机器人本体感知估计器。

<details>
<summary>完整摘要</summary>

腿式机器人携带 IMU，但由于消费级 IMU 噪声较大，惯性解会随时间漂移。然而，足端会与环境发生间歇接触，这一信息可用于减轻漂移。本文构建了一系列逐步增强的腿式机器人状态估计器来利用这一点。在所有方法中，浮动基座状态都由姿态、位置、速度以及 IMU 偏置组成。为了建模足端接触，我们从 Hartley 等人提出的接触辅助 invariant EKF 出发，不过将接触更新频率降低。随后，我们用一个小型 factor graph 替换测量更新。最后，我们把同样的因子转化为 fixed-lag smoother，并引入基于接触阶段的 foothold 表示，同时考虑 IMU 偏置是否随时间演化。为了促进 proprioceptive legged odometry 的可复现性和进一步研究，这四个变体都已在 GTSAM 中实现，同时我们还提供了一个 ROS2 兼容版本。

</details>

---

### [[20_Research/Papers/机器人/UfM_Uncertainty_from_Motion_for_DNN_Depth_Estimation_Using_Gaussians|UfM*: Uncertainty from Motion* for DNN Depth Estimation Using Gaussians]]

![[assets/2605.23098_figure.png|800]]

- **arXiv**: [2605.23098](https://arxiv.org/abs/2605.23098)
- **PDF**: https://arxiv.org/pdf/2605.23098
- **详细分析**: [[20_Research/Papers/机器人/UfM_Uncertainty_from_Motion_for_DNN_Depth_Estimation_Using_Gaussians|UfM*: Uncertainty from Motion* for DNN Depth Estimation Using Gaussians]]
- **作者**: Soumya Sudhakar, Sertac Karaman, Vivienne Sze
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

在机器人和具身智能场景中，单目深度DNN常被用来替代笨重、耗电的LiDAR或主动双目传感器，但模型在噪声输入和分布外场景下容易失准，若缺少可靠的不确定性估计，部署到安全关键系统时风险很高。现有不确定性方法要么依赖集成、采样等多次前向推理，计算和存储开销大，要么只基于单帧图像，无法利用机器人视频流中“同一三维区域跨视角预测应一致”这一关键信息。本文值得关注之处在于：它把“跨视角深度预测不一致”直接作为不确定性信号，并且试图在单次推理、后处理、低内存的约束下实现这一点。

#### 方法概述和架构

论文提出 UfM*（Uncertainty from Motion*），用于单目深度估计的不确定性计算。其核心思路是：先对当前帧做一次深度DNN推理，再把当前视角与历史视角中的几何信息用紧凑的3D高斯混合表示起来，而不是维护昂贵的点云。随后，算法在图像平面中寻找当前帧与过去帧之间的高斯对应关系，并通过比较对应高斯之间的距离来度量跨视角分歧。为了把这种紧凑的3D高斯表示转成逐像素的不确定性，作者进一步使用高斯混合回归，从而为每个深度像素输出密集的不确定性图。整体流程可以后处理地接在任意单目深度模型之后，不需要修改网络结构或重新训练；同时，它还可与aleatoric不确定性联合使用，也可单独作为不确定性估计器。

#### 实验结果分析

作者在 ScanNet 的100个分布外序列上评估了方法，并与 ensemble、BatchEnsembles、MC-Dropout、evidential、aleatoric 等基线进行比较。结果显示，UfM* 与 aleatoric 不确定性结合后，相比 ensemble 的 ECE 可提升24%到28%，同时仅消耗约3%的能量和0.02%的内存。系统演示表明，该方法在搭载 Arm Cortex-A76 CPU 的微型受限机器人上，对224×224图像仅需63 mJ，且能以30 FPS实时运行。节选中还指出，方法在分布外场景与消融实验中均表现稳定，可见文本未给出更细的具体数值。

<details>
<summary>完整摘要</summary>

对可靠的不确定性估计而言，它对于将单目深度深度神经网络（DNN）部署到安全关键机器人系统中至关重要。传统的不确定性方法，例如集成方法和基于采样的方法，需要对每张图像进行多次推理，因此会带来显著的计算和内存开销。此外，仅从单张图像预测的不确定性，无法衡量同一三维区域在不同视角下预测结果之间的分歧。我们提出 Uncertainty from Motion*（UfM*），这是一种不确定性估计算法，它通过使用紧凑的高斯混合模型比较前一视图与当前视图，从而高效地测量多视角分歧，并且每张图像只需要一次DNN推理。使用高斯来计算多视角分歧，不仅比先前使用点云的方法在计算和内存上更加高效，还能通过在三维空间区域层面衡量分歧来改进不确定性估计。将 UfM* 与 aleatoric 不确定性结合后，与 ensemble 相比，期望校准误差（ECE）可改善24%到28%，同时在100个分布外的 ScanNet 序列上仅消耗3%的能量和0.02%的内存。我们还展示了 UfM* 在224×224图像上仅消耗63 mJ，并能在搭载于一台能量受限的微型机器人上的 Arm Cortex-A76 CPU 上以30 FPS实时运行，这表明：使用高斯来衡量多视角分歧，可以为资源受限的机器人系统提供高效的不确定性估计。

</details>

---

### [[20_Research/Papers/强化学习/PIMbot_A_Self-Adaptive_Attack_Framework_for_Adversarial_Manipulation_of_Multi-Robot_Reinforcement_Learning|PIMbot: A Self-Adaptive Attack Framework for Adversarial Manipulation of Multi-Robot Reinforcement Learning]]

![[assets/2605.23027_figure.png|800]]

- **arXiv**: [2605.23027](https://arxiv.org/abs/2605.23027)
- **PDF**: https://arxiv.org/pdf/2605.23027
- **详细分析**: [[20_Research/Papers/强化学习/PIMbot_A_Self-Adaptive_Attack_Framework_for_Adversarial_Manipulation_of_Multi-Robot_Reinforcement_Learning|PIMbot: A Self-Adaptive Attack Framework for Adversarial Manipulation of Multi-Robot Reinforcement Learning]]
- **作者**: Zexin Li, Ziliang Zhang, Hyoseung Kim, Cong Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.3，大模型 0.1，强化学习 0.8，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

多机器人协作中的强化学习已经能在逃离房间、囚徒困境、围捕/运输等社交困境任务中学习出有效协同，但这类系统往往依赖通信、奖励设计和各智能体的行为假设，一旦出现误通信、投机行为或对抗性机器人，协作就可能迅速失效。论文关注的核心问题是：在多机器人强化学习里，攻击者如何利用奖励通道和动作选择来操纵群体结果。由于这类研究直接暴露了多机器人协作系统的脆弱性，因此对具身智能、机器人安全和多智能体强化学习都很有参考价值。

#### 方法概述和架构

论文提出 PIMbot，一个面向多机器人强化学习的自适应攻击框架，专门用于在社会困境场景中操纵系统结果。它包含两条互补的操纵路径：一是奖励通道的激励操纵，通过篡改、注入或抑制激励信号来改变其他智能体的回报结构；二是策略操纵，通过攻击者自身的动作选择影响环境交互和他人决策。框架还设计了一个在线的自适应多目标控制器，用于在“提升攻击者自身收益”和“破坏团队协作”之间动态权衡。整体流程是：攻击者根据当前观测与交互状态，同时生成奖励侧和动作侧的操纵信号，再由自适应控制器调整两种手段的权重，从而在不同阶段切换更隐蔽或更激进的攻击模式。论文还将这一机制形式化为多目标优化问题，以保证在在线更新时能够维持稳定的折中关系。

#### 实验结果分析

实验在 Gazebo 多机器人仿真环境中进行，并在 Escape Room、Iterated Prisoner’s Dilemma、Stag Hunt 等典型 MARL 社交困境任务上验证了方法有效性，同时还与多种 SOTA MARL 算法做了扩展比较。结果表明，PIMbot 能显著降低任务成功率、破坏协作稳定性，并且两种操纵手段结合时效果更强；不过节选文本未给出具体数值。论文还在 NVIDIA Jetson Orin Nano 的真实嵌入式平台上做了案例研究，用于量化系统开销并验证其在真实受限硬件上的可行性。

<details>
<summary>完整摘要</summary>

近期研究已经表明，强化学习在多机器人协作中具有很大潜力，尤其是在社交困境场景下，机器人需要在自利与集体收益之间进行权衡。然而，环境因素如误通信以及对抗性机器人会影响协作，因此有必要研究多机器人通信如何被操纵以获得不同结果。本文提出 PIMbot，一个通过两种互补手段来操纵结果的框架：(i) 对奖励通道进行激励操纵；(ii) 对智能体自身动作进行策略操纵。一个自适应多目标控制器以在线方式平衡这两种手段。我们的工作在近期多智能体强化学习社交困境中引入了一种新的操纵方法，这类方法使用独特的奖励函数进行激励。借助我们提出的 PIMbot 机制，一个机器人能够有效操纵社交困境环境。全面的实验结果表明，我们的方法在 Gazebo 仿真的多机器人环境中表现有效。此外，在 NVIDIA Jetson Orin Nano 上进行的真实嵌入式设备案例研究量化了系统成本，并验证了 PIMbot 在真实自主嵌入式系统场景中的有效性，超越了纯仿真设定。综合来看，这些结果将 PIMbot 定位为一种严格的压力测试工具，可用于揭示多机器人协作任务中的关键脆弱性。

</details>

---

### [[20_Research/Papers/机器人/Verified_Task-Space_Motion_Planning_Under_Joint-Space_Constraints|Verified Task-Space Motion Planning Under Joint-Space Constraints]]

![[assets/2605.22991_figure.png|800]]

- **arXiv**: [2605.22991](https://arxiv.org/abs/2605.22991)
- **PDF**: https://arxiv.org/pdf/2605.22991
- **详细分析**: [[20_Research/Papers/机器人/Verified_Task-Space_Motion_Planning_Under_Joint-Space_Constraints|Verified Task-Space Motion Planning Under Joint-Space Constraints]]
- **作者**: Hanjiang Hu, Changliu Liu, Yebin Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Security

#### 研究背景与动机

在机器人任务空间规划中，规划器通常直接在笛卡尔空间生成运动，再通过逆运动学映射到关节空间；但真实机械臂受关节角度变化、速度和力矩等约束，任务空间中看似很小的一步，可能在关节空间里已经越界。现有 Bug2 等反应式规划器往往使用固定步长，且对关节限位不敏感，当 Jacobian 处于病态或接近奇异时，容易出现关节裁剪、轨迹漂移，甚至无法到达目标。该工作关注的是如何在每一步规划时给出“可证安全可达”的任务空间步长上界，因此对具身智能和在线机器人规划都很有现实意义。

#### 方法概述和架构

论文提出了一种基于 SOS 的可验证任务空间运动规划方法，核心目标是在当前关节配置下，计算满足关节位移约束时“可证可达”的最大笛卡尔超矩形。方法先在当前构型附近对逆运动学进行二阶多项式近似，用该近似把任务空间位移与关节位移之间的关系显式写成二次形式。随后利用 S-procedure 将“超矩形内所有点都满足关节位移上界”这一条件转化为一个小规模半定规划，求解得到认证半宽 λ*。由于该二次结构具有特殊性，作者还给出一个等价的二分搜索实现，可在亚毫秒级完成证书计算。最后，将这一可达性证书作为 Bug2 的在线可行性过滤器：每步根据局部运动学条件自适应调整笛卡尔步长，并通过多项式 IK 完成关节更新，从而保证每一步都不违反关节限制。

#### 实验结果分析

实验在 94 个对抗性场景上进行，覆盖 6 组不同的关节限位设置，并与普通 Bug2 进行对比。结果显示，SOS 认证版 Bug2 实现了 0 次关节限位违规，且目标到达率达到 100%；而标准 Bug2 在 6%–11% 的步骤中会违反关节限位，并且在最多 18% 的场景中无法到达目标。正文节选还强调了该认证与二分实现的推理开销很低，可见文本未给出具体数值，但说明其可用于在线规划。

<details>
<summary>完整摘要</summary>

反应式任务空间规划器（如 Bug2）通常采用固定的笛卡尔步长，并且不会感知机械臂的关节角度限位。当 Jacobian 条件数较差时，即使很小的笛卡尔步进也可能要求超过允许范围的关节变化；将关节裁剪到其限位会导致轨迹跟踪漂移，甚至完全无法到达目标。为了解决这一问题，我们在每个规划步骤中计算在关节位移约束下“可证可达”的最大笛卡尔超矩形。我们利用逆运动学的二阶多项式近似以及 S-procedure，构建了一个小规模半定规划，其解给出认证半宽 λ*。利用二次结构，我们还设计了一个等价的二分搜索过程，能够在亚毫秒时间内完成认证。将该证书集成到 Bug2 中后，得到的规划器可以根据局部运动学条件自适应调整步长。在覆盖 6 组关节限位设置的 94 个对抗性场景统计评测中，SOS 认证规划器实现了 0 次关节限位违规和 100% 的目标到达率；相比之下，标准 Bug2 在 6%–11% 的步骤中违反关节限位，并在最多 18% 的场景中无法到达目标。

</details>

---

### [[20_Research/Papers/机器人/Remote_Teleoperation_of_Endovascular_Intervention_Robots_A_Systematic_Review|Remote Teleoperation of Endovascular Intervention Robots: A Systematic Review]]

![[assets/2605.22889_figure.png|800]]

- **arXiv**: [2605.22889](https://arxiv.org/abs/2605.22889)
- **PDF**: https://arxiv.org/pdf/2605.22889
- **详细分析**: [[20_Research/Papers/机器人/Remote_Teleoperation_of_Endovascular_Intervention_Robots_A_Systematic_Review|Remote Teleoperation of Endovascular Intervention Robots: A Systematic Review]]
- **作者**: Xingyu Chen, Yinchao Yang, Nikola Fischer, Harry Robertshaw, Benjamin Jackson, Mohammad Shikh-Bahaei, Christos Bergeles, Thomas C Booth
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

这篇论文聚焦于血管内介入机器人（endovascular intervention robots）的远程遥操作问题，核心任务是在远距离条件下完成导管和导丝的精准导航，以支持取栓、支架植入等高时效性操作。该方向的临床价值很明确：一方面可减少医生在介入手术中暴露于X射线下的时间，缓解长时间穿戴防护铅衣带来的肌肉骨骼负担；另一方面有望把高水平血管介入能力扩展到地理偏远或专家稀缺地区。作者特别强调，像急性缺血性卒中的机械取栓这类“分秒必争”的场景，对远程介入机器人提出了更高要求，因此非常值得系统梳理现有证据与技术瓶颈。

#### 方法概述和架构

本文采用PRISMA规范进行系统综述，检索了PubMed、IEEE Xplore和Scopus三个数据库，时间截至2025年3月19日。检索式围绕“远程/遥操作/远程手术/电信通信”与“血管内/神经血管/导管/导丝/介入”等关键词组合构建，并限定为2010年及以后发表的英文原始研究。纳入标准要求研究必须涉及血管内机器人介入中的远程导管或导丝操作；仅讨论运动学、末端跟踪或与真实介入流程无关的台架精度测试则被排除，且距离小于100米的近场遥操作也不纳入。最终从2501篇初始结果中筛得16篇研究，并提取了机器人平台、遥操作距离、通信方式、实验场景、成功率与时延等信息。方法学质量评估使用了QUADAS-2和ROBINS-I，但由于纳入研究异质性较大，未进行meta分析。

#### 实验结果分析

结果表明，纳入的研究覆盖了机械式和电磁式驱动的多种远程血管内机器人平台，所能实现的遥操作距离最长可达7000公里。随着通信基础设施的增强，网络时延可维持在临床可接受范围内，约为30–163毫秒；在小规模人体试验中，初步结果显示程序成功率可达100%，但大部分证据仍来自动物实验或仿体模型。总体来看，可见文本未给出统一的头对头基线对比与消融结果，但作者的结论是该技术具备降低职业风险、扩大急症介入可及性和优化资源配置的潜力；同时，未来需要在低中收入国家开展研究，并通过多中心临床试验验证其安全性、有效性与泛化能力。

<details>
<summary>完整摘要</summary>

远程机器人辅助的血管内介入为降低临床医生的辐射暴露和体力负担、并将专业血管治疗扩展到地理上更偏远的地区，提供了一种很有前景的方案。尽管近年来已有进展，远程操作的血管内介入仍然研究不足，尤其是在机械取栓这类时间高度敏感的干预中更是如此。本综述旨在评估远程操作血管内机器人系统的证据，涵盖技术可行性、通信基础设施以及临床结局；同时识别研究空白与未来方向。按照PRISMA指南，共有16项研究符合纳入标准，初始检索结果为2501篇。我们发现，由机械或电磁系统驱动的远程操作导管和导丝，能够在最远7000公里的距离上完成导航。在通信基础设施足够稳健的情况下，网络时延可保持在临床可接受范围内（30–163毫秒）。尽管小规模人体试验中的初步结果显示程序成功率为100%，但大多数证据仍来自动物模型或仿体模型。总体而言，这些发现表明，远程操作的血管内介入可以降低职业风险，扩大患者对紧急介入治疗的可及性，并优化资源配置。未来研究应在低收入和中等收入国家开展，以证明其在更广泛地理范围内的可及性；最终还需要多中心临床试验，在不同临床场景中验证其安全性、有效性和泛化能力。

</details>

---
