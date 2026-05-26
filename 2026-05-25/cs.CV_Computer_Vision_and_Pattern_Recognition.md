# cs.CV | Computer Vision and Pattern Recognition | 2026-05-25

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/世界模型/Learning_a_Particle_Dynamics_Model_with_Real-world_Videos|Learning a Particle Dynamics Model with Real-world Videos]]

![[assets/2605.23845_figure.png|800]]

- **arXiv**: [2605.23845](https://arxiv.org/abs/2605.23845)
- **PDF**: https://arxiv.org/pdf/2605.23845
- **详细分析**: [[20_Research/Papers/世界模型/Learning_a_Particle_Dynamics_Model_with_Real-world_Videos|Learning a Particle Dynamics Model with Real-world Videos]]
- **作者**: Chanho Kim, Suhas V. Sumukh, Li Fuxin
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，世界模型 1）
- **关联关键词**: WorldModel

#### 研究背景与动机

这篇论文关注的是：能否仅依靠真实世界视频，学习多物体碰撞与交互的粒子动力学模型，用于世界模型和具身智能中的物理预测。以往这类模型多在仿真环境中训练，因为真实视频里很难获得完整点云、跨帧对应关系和粒子级真值状态，导致从合成数据学到的规律在真实场景中容易出现 sim-to-real 偏差。论文之所以值得关注，是因为它尝试把“可微分渲染监督”与“粒子动力学建模”结合起来，直接从无标注真实视频学习复杂碰撞动力学。

#### 方法概述和架构

作者提出一种基于 Gaussian Splatting 的粒子动力学学习框架，将每个 3D Gaussian 视作带有位置、旋转、尺度、颜色和透明度的粒子表示，并直接在这些稠密 Gaussians 上做动力学预测。模型输入为连续三帧中每个粒子的位移速度、垂直坐标等特征，核心网络采用 PointConv 风格的卷积交互建模，在同一物体内部与跨物体之间交替建模局部作用与碰撞传播。由于真实视频中没有粒子级物体 ID，方法利用多视角 2D 分割掩码和可微渲染贡献度，推断每个 Gaussian 属于哪个物体，再据此组织对象级交互。训练时不依赖粒子级标注，而是通过从预测的未来 Gaussian 状态渲染回图像，与真实视频及多视角掩码进行监督；推理时模型直接递推生成下一时刻的粒子位置与旋转变化，从而得到未来轨迹与渲染结果。

#### 实验结果分析

实验基于作者新收集的真实世界多视角数据集，包含约 500 段视频，覆盖滚球冲撞和立方体堆叠坍塌等复杂多物体交互场景，并与已有方法进行比较。正文节选显示作者还设计了消融实验，分析 Gaussian 轨迹初始化、Gaussian 到物体的分配方式以及多步 rollout 训练等关键模块的作用。可见文本未给出具体数值，但结论是：该方法能够在真实视频上学习非平凡的多物体碰撞动力学，并优于或至少有竞争力地支持从真实世界直接训练世界模型。

<details>
<summary>完整摘要</summary>

数据驱动的物理模拟学习方法，也常被称为世界模型，由于其可微分特性，已成为传统物理模拟器的有前景替代方案。此前研究已在复杂场景中对刚体和非刚体的运动预测取得了令人印象深刻的结果，尤其是在包含多个相互作用物体的情形下。然而，这些模型通常在仿真环境中训练，因为在真实场景中获取完美状态信息非常困难，例如完整的场景点云以及跨时间的点对应关系等。对合成数据的依赖会在 sim-to-real 差距较大时限制其应用范围。本文旨在克服这些限制，提出一种新的框架，可直接从未标注的真实世界视频中训练神经对象动力学模型。具体而言，我们提出学习一种与 Gaussian Splatting 框架兼容的基于粒子的动力学模型，该模型作用于从 Gaussians 派生的稠密粒子（即带有尺度和旋转信息的粒子），并预测它们随时间的位姿和旋转变化。该模型通过渲染监督进行训练，因此无需粒子级标注状态即可从真实世界视频中学习。我们的模型可直接作用于稠密 Gaussians，而不依赖启发式的子采样锚点。为支持这项研究，我们还提出了一个真实世界数据集，包含约 500 段捕捉多样对象交互的视频。

</details>

---

### [[20_Research/Papers/具身智能/ComPose_When_to_Trust_Hands_for_Object_Pose_Tracking|ComPose: When to Trust Hands for Object Pose Tracking]]

![[assets/2605.23523_figure.png|800]]

- **arXiv**: [2605.23523](https://arxiv.org/abs/2605.23523)
- **PDF**: https://arxiv.org/pdf/2605.23523
- **详细分析**: [[20_Research/Papers/具身智能/ComPose_When_to_Trust_Hands_for_Object_Pose_Tracking|ComPose: When to Trust Hands for Object Pose Tracking]]
- **作者**: Jisu Shin, Junoh Lee, JunGyu Lee, Inhwan Bae, Dohyeon Lee, Hokyun Im, Youngwoon Lee, Hae-Gon Jeon
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.9，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

从单目 RGB 视频中恢复被操控物体的 6DoF 姿态轨迹，是具身智能、机器人模仿学习和人机交互中的基础能力，尤其适合将人类演示直接迁移给机器人。现有方法往往依赖深度信息、CAD 模板或其他强外部先验，在真实场景中泛化受限；而在“手拿物体”的场景里，物体又常被手部严重遮挡，即使显式分割也很难稳定跟踪。论文关注的关键问题是：当物体看不清时，是否应该信任手部运动，并将其作为姿态跟踪的补充线索。

#### 方法概述和架构

作者提出 ComPose，一个面向手-物交互场景的 6DoF 物体跟踪框架，输入为 RGB 视频，输出为随时间变化的稳定物体姿态轨迹。方法首先借助 3D foundation model 从视频中恢复跨帧一致的深度/点云等几何信息，并用 SAM3 获取物体掩码，基于点云通过 ICP 估计物体间的相对旋转与初始平移。与此同时，系统还通过手部姿态估计器恢复 21 个手关节的 3D 位置，并利用关节拓扑对应关系通过加权 Procrustes 估计手部运动。ComPose 的核心是一个自适应融合模块：它会预测哪些手关节更有信息量，并学习一个门控参数来决定旋转估计中应更依赖物体几何还是手部线索，同时学习平移残差来修正仅由可见物体区域带来的偏差。为了让输出轨迹更稳定，方法还显式约束旋转与平移的时间一致性，从而在不使用外部平滑器的情况下得到连续、平滑的 3D 轨迹。

#### 实验结果分析

论文在多组实验中验证了 ComPose 的准确性、效率与鲁棒性，重点考察了严重手部遮挡和几何歧义场景下的跟踪表现。作者报告其相较于仅依赖物体几何的基线，在遮挡严重、对称物体等容易退化的情况下更稳定；同时，方法对不同 3D foundation model 也具有较好的可迁移性。进一步地，跟踪得到的平滑轨迹可以直接迁移到下游机器人操作任务中，用于从在线视频中重建人类动作并指导机器人执行。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

从视频中重建物体运动是具身智能和机器人操作中的关键组成部分。尽管已经研究了多种物体姿态跟踪方法，它们通常严重依赖深度数据或 3D 模板等强外部先验，即便使用显式掩码，也仍然会在手部抓握造成的严重遮挡下变得非常脆弱。本文提出 ComPose，一个面向手部感知的 RGB 视频 6DoF 物体跟踪框架。不同于将手仅仅视为遮挡物，我们的方法将手部运动作为物体跟踪的互补线索进行协同利用。具体来说，我们将来自基础模型的物体线索与手部线索结合到一个统一的跟踪管线中，从而随时间恢复多种物体运动。ComPose 会自适应地选择有信息量的手部关节，将物体和手部推导出的线索结合用于运动估计，并利用可见的几何证据以及学习到的修正项来细化最终的物体运动。我们还进一步约束旋转和位移两个维度上的时间一致性，从而在不使用任何外部平滑的情况下，生成稳定的 3D 物体轨迹。大量实验表明，我们的方法具有准确、高效、并且在严重手部遮挡和几何歧义下都很鲁棒。此外，得到的轨迹还可以有效迁移到下游机器人操作任务中，使机器人能够从在线视频里重建人类动作。

</details>

---

### [[20_Research/Papers/强化学习/B-GRTO_Bootstrapped_Group_Relative_Tool_Optimization_for_Referring_Segmentation|B-GRTO: Bootstrapped Group Relative Tool Optimization for Referring Segmentation]]

![[assets/2605.23500_figure.png|800]]

- **arXiv**: [2605.23500](https://arxiv.org/abs/2605.23500)
- **PDF**: https://arxiv.org/pdf/2605.23500
- **详细分析**: [[20_Research/Papers/强化学习/B-GRTO_Bootstrapped_Group_Relative_Tool_Optimization_for_Referring_Segmentation|B-GRTO: Bootstrapped Group Relative Tool Optimization for Referring Segmentation]]
- **作者**: Mario Markov, Stefan Maria Ailuro, Mohammad Mahdi, Luc Van Gool, Danda Pani Paudel
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

Referring segmentation 的目标是根据自然语言指令，从图像中分割出被指代的目标区域，广泛用于开放式视觉交互、机器人、自动驾驶、遥感和医学图像分析等场景。与普通语义分割不同，这类任务既要求像素级定位能力，又要求模型先理解含糊、开放式甚至需要常识推理的提示词。现有基于大视觉语言模型与分割解码器的方案，通常只用强化学习优化“推理策略”，而把分割解码器当作固定工具，忽略了工具本身在跨域和复杂场景下也需要适配这一事实。因此，这篇工作值得关注之处在于，它尝试把强化学习和可微分工具优化统一起来，专门解决“既要会想，也要会分”的联合优化问题。

#### 方法概述和架构

论文提出 B-GRTO（Bootstrapped Group Relative Tool Optimization），包含两个阶段：先做 BTO（Bootstrapped Tool Optimization），再做 GRTO（Group Relative Tool Optimization）。第一阶段利用来自参考策略的 rollout 缓冲区，对分割工具解码器进行离策略预训练，把工具预先对齐到“理论上训练后策略”会需要的行为，以减少后续联合训练时的冷启动问题。第二阶段在 GRPO 的框架内联合训练推理策略和分割工具：策略端仍然使用组相对奖励做更新，而工具端则复用同一批 rollout，通过可微分分割损失的梯度来更新。方法的关键是把工具梯度与策略奖励联系起来，借助 stopgrad 等处理在保持 GRPO 训练形式的同时，把可微分工具反馈纳入强化学习目标。整体上，输入是图像与自然语言指代提示，输出是目标掩码；训练时先预训练工具、再联合优化，推理时则由大模型负责推理选择，分割解码器负责生成最终 mask。

#### 实验结果分析

作者在三个具有挑战性的 referring segmentation 场景上验证了方法，包括 remote sensing segmentation、camouflaged object detection 和 reasoning segmentation。实验对比了纯 GRPO 以及多种领域内方法，结论是 B-GRTO 相比只优化策略的做法有明显提升，并且在部分设置上可以达到或超过专门为该领域设计的 SOTA。正文节选还指出，B-GRTO 在训练预算与性能之间表现出更好的折中：在三类任务中有两类指标占优，另一类也仅有很小幅度下降。可见文本未给出具体数值，但整体结论是：预训练工具再联合强化学习，能显著改善收敛速度、稳定性和最终性能。

<details>
<summary>完整摘要</summary>

分割是计算机视觉中的基础任务，为像素级场景理解提供支撑，也是自动感知、医学图像分析等应用的核心。在复杂的 referring segmentation 中，近期方法通常将大型视觉语言模型与分割解码器配对：前者分析图像和提示词，后者预测目标掩码。尽管强化学习能够提升需要推理的视觉语言系统，但像分割解码器这样的可训练工具通常是用可微分目标单独优化的，而如何将这类目标以严格、合理的方式融入强化学习仍然缺乏深入研究。为此，我们提出 group relative tool optimization（GRTO），这是一个有数学基础的框架，用于联合优化策略与可微分工具使用。GRTO 复用 group relative policy optimization（GRPO）的 rollout 来优化辅助工具目标，使解码器梯度能够补充策略奖励。进一步地，我们推导出 Bootstrapped-GRTO（B-GRTO），这是一种预训练方法，可以以较低成本对工具进行引导式预热，从而带来更快的收敛和更强的性能。在三个具有挑战性的 referring segmentation 设置上，B-GRTO 相比直接使用 GRPO 都取得了显著提升，并且与领域内最先进方法持平或更优。这表明，将强化学习与可微分的辅助目标统一起来，对于需要推理的分割任务具有重要价值。

</details>

---

### [[20_Research/Papers/世界模型/SCOPE_Simulating_Cross-game_Operations_in_Playable_Environments_for_FPS_World_Models|SCOPE: Simulating Cross-game Operations in Playable Environments for FPS World Models]]

![[assets/2605.23345_figure.png|800]]

- **arXiv**: [2605.23345](https://arxiv.org/abs/2605.23345)
- **PDF**: https://arxiv.org/pdf/2605.23345
- **详细分析**: [[20_Research/Papers/世界模型/SCOPE_Simulating_Cross-game_Operations_in_Playable_Environments_for_FPS_World_Models|SCOPE: Simulating Cross-game Operations in Playable Environments for FPS World Models]]
- **作者**: Zizhao Tong, Hongfeng Lai, Zeqing Wang, Zhaohu Xing, Kexu Cheng, Haoran Xu, Zhao Pu, Shangwen Zhu, Ruili Feng, Jian Zhao, Yan Zhang, Hao Tang...
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

第一人称射击（FPS）游戏的交互式世界模型需要在每一帧同时处理高频、重叠的操作信号，并且不能干扰画面中不受这些操作影响的区域，这对现有视频生成式世界模型是一个明显挑战。已有方法通常把动作信号以全局方式注入模型，并且多只在单一游戏标题上训练，因此在FPS这类密集控制输入下容易失效。作者指出，FPS动作具有明显的空间选择性：开火、换弹等离散事件主要影响武器附近的局部区域，而视角与移动等连续信号则主要决定其余场景的稳定生成。基于这一观察，论文值得关注的原因在于它同时解决了“动作如何作用到画面哪里”与“如何跨游戏泛化”两个关键问题。

#### 方法概述和架构

论文提出 SCOPE，并将其作为条件模块插入到预训练视频扩散模型的每个 Transformer block 中。核心思路是把特征重排为“按像素组织的时间序列”，使每个空间位置都能基于局部视觉内容独立判断自己是否处于作用范围内，并据此计算动作响应。对于离散动作，模型使用带视觉查询的交叉注意力，将效果限制在局部 in-scope 区域；对于连续控制，则通过 MLP 融合与时间自注意力建模平滑的视角/运动变化，主要服务于 out-of-scope 区域的生成。整个模块采用零初始化，因此训练从原始视频生成器开始，逐步学习作用范围分离，而不需要分割标注。训练上，模型基于预训练 DiT 和 flow matching 目标，在首帧条件下生成后续视频，并结合动作随机丢弃做 Action-CFG；推理时可通过动作引导增强控制响应。为支撑跨游戏训练，作者还构建了 CrossFPS 数据集，包含 7 个 FPS 游戏、69K 段对齐帧级动作遥测的片段，以及 10 维控制信号。

#### 实验结果分析

实验在 CrossFPS 上评估了动作响应、空间稳定性、视觉质量以及跨游戏泛化能力，并与现有基线进行比较；正文节选中可见文本未给出具体数值。结果表明，SCOPE 能在复杂的多动作控制下保持较强的动作可控性，同时更准确地区分受动作影响的局部区域与应保持稳定的背景区域。作者还报告了消融实验、可扩展性分析以及对未见场景的零样本泛化测试，说明该架构与数据扩展都能持续带来收益。整体上，模型在未见场景中仍能维持较好的视觉质量与动作响应，体现了较强的跨游戏泛化能力。

<details>
<summary>完整摘要</summary>

面向第一人称射击（FPS）游戏的交互式世界模型，必须在每一帧解决高频且相互重叠的控制信号，并且不能扰动不受影响的区域。现有方法通常将动作以全局方式注入，并且只在单一游戏标题上训练，因此在密集的 FPS 输入下会失效。我们观察到，FPS 动作具有空间选择性：诸如开火或换弹等离散事件只影响武器周围的局部区域（即作用范围，scope），而连续的视角与移动信号则决定稳定的周边环境。基于此，我们提出 SCOPE：在一个预训练的视频扩散模型的每个 Transformer block 中插入一个条件模块。该模块将特征重排为按像素组织的时间序列，使每个位置都能根据局部视觉内容计算自身的动作响应，从而在不需要分割标注的情况下，将范围内效果与范围外生成分离开来。我们还提出 CrossFPS，这是第一个带有帧对齐动作遥测的多游戏 FPS 数据集。它包含来自 7 个标题的 69K 段视频片段，以及 10 自由度控制器信号，并经过整理以去除游戏玩法偏置。模型学习到的是通用的视觉到动作映射，而不是特定游戏的模式，因此能够零样本迁移到未见场景。实验验证了其强动作响应、精确的作用范围分离，以及有效的跨游戏泛化能力。

</details>

---

### [[20_Research/Papers/具身智能/IntentionNav_A_Benchmark_for_Intent-Driven_Object_Navigation_from_Implicit_Human_Instruction|IntentionNav: A Benchmark for Intent-Driven Object Navigation from Implicit Human Instruction]]

![[assets/2605.23187_figure.png|800]]

- **arXiv**: [2605.23187](https://arxiv.org/abs/2605.23187)
- **PDF**: https://arxiv.org/pdf/2605.23187
- **详细分析**: [[20_Research/Papers/具身智能/IntentionNav_A_Benchmark_for_Intent-Driven_Object_Navigation_from_Implicit_Human_Instruction|IntentionNav: A Benchmark for Intent-Driven Object Navigation from Implicit Human Instruction]]
- **作者**: Lin Qian, Shijie Li, Sihao Lin, Xuan Zhang, Bangya Liu, Yanran Li, Hujun Yin
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.5（加权：具身智能 2.1，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

现有对象导航基准通常直接告诉智能体要找的类别，例如“微波炉”或“椅子”，但面向真实用户的具身智能更常遇到的是隐含意图式表达，例如“我想加热这份食物”或“屋里有点闷”。这类任务要求机器人先从自然语言意图中推断目标对象，再在场景中找到对应实例，并判断是否已经到达可停靠的位置。论文关注的正是这种“从隐含人类指令中推断目标并完成主动搜索”的场景，因为它更接近人机交互中的真实需求，也更能暴露现有导航系统在目标理解、视觉验证和终点定位上的短板。

#### 方法概述和架构

论文提出 IntentionNav，一个面向意图驱动对象导航的诊断型基准。每个 episode 输入一个自由文本意图、RGB-D 观测和位姿信息，但不提供目标对象名称，要求智能体在主动探索过程中自行推断目标类别并完成导航。基准共包含 500 个意图，覆盖 176 个 Isaac Sim 场景和 64 个目标类别，并将同一意图改写成四种受控的指令风格：正式、自然、口语和情绪化。与此同时，作者还为每个意图标注了四类意图模式：事件脚本、内在状态、物理状态和功能/可供性，从而把“表层措辞变化”和“语义线索类型”这两个维度解耦。该设计使得评测不只看总体成功率，还能分别分析目标推断、语言鲁棒性、邻域可达性以及终点成功。

#### 实验结果分析

作者使用固定的主动导航代理评测了 3 个 VLM，在同一测试环境下考察目标识别、接近目标和最终停靠等指标。结果显示，模型能够在 48.3% 的 episode 中识别出意图对应目标，68.7% 的 episode 能进入目标 2 m 邻域，但真正成功终止仅有 24.9%，而以 1 m 为标准的 grounded success 只有 5.5%。分类型来看，事件脚本类意图的成功率最高，为 28.7%，而物理状态类和可供性类分别只有 19.2% 和 18.5%，说明间接意图仍然是目标选择、视觉确认和终点定位的主要瓶颈。可见文本还表明，基准构建强调严格的场景可回答性和目标唯一性，但节选中未给出更多消融实验的具体数值。

<details>
<summary>完整摘要</summary>

现有对象导航基准通常会直接告诉具身智能体要寻找的对象类别，例如微波炉或椅子。面向人类的具身智能系统经常面对更间接的表达：例如“我需要一些东西来加热这份食物”或“房间里有点闷”。此时，智能体必须推断能够满足需求的对象，找到场景中对应的实例，并判断目标是否已经达成。我们将这一设定定义为意图驱动对象导航，并提出 IntentionNav——一个用于从隐含人类指令中进行主动对象搜索的诊断型基准。每个 episode 提供一个自由文本意图、RGB-D 观测和位姿信息，但不提供目标对象名称。IntentionNav 包含 500 个意图，覆盖 176 个 Isaac Sim 场景和 64 个目标类别。每个意图都被改写为四种受控的指令风格，并标注为四种意图模式之一，从而在相同几何条件下区分表层措辞与语义线索类型。这种成对设计支持对目标推断、语言鲁棒性、邻域可达性和终止成功的分析，而不仅仅是总体成功率。我们使用固定的主动导航代理评测了 3 个 VLM。模型能够在 48.3% 的 episode 中识别出意图所指向的目标，在 68.7% 的 episode 中进入目标 2 m 邻域，但最终成功终止仅为 24.9%，而实现基于场景的 1 m 成功率仅为 5.5%。成功率在事件脚本类意图上最高，为 28.7%，而在物理状态类和可供性类意图上较低，分别为 19.2% 和 18.5%。这表明，间接的人类意图仍然是主动具身搜索中目标选择、视觉验证和终点定位的关键瓶颈。

</details>

---

### [[20_Research/Papers/机器人/Semantic-Aware_Guided_Drone_Exploration_for_Language-Conditioned_3D_Indoor_Mapping|Semantic-Aware Guided Drone Exploration for Language-Conditioned 3D Indoor Mapping]]

![[assets/2605.23160_figure.png|800]]

- **arXiv**: [2605.23160](https://arxiv.org/abs/2605.23160)
- **PDF**: https://arxiv.org/pdf/2605.23160
- **详细分析**: [[20_Research/Papers/机器人/Semantic-Aware_Guided_Drone_Exploration_for_Language-Conditioned_3D_Indoor_Mapping|Semantic-Aware Guided Drone Exploration for Language-Conditioned 3D Indoor Mapping]]
- **作者**: Nitin Vegesna, Avideh Zakhor
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

该工作面向未知三维室内环境中的语言条件探索：机器人接收一个开放词汇文本查询（如“chair”），需要在完成三维建图覆盖的同时，尽快发现所有与查询相关的目标实例。这类任务在家庭服务、仓储巡检和灾后搜救等场景中都很重要，因为机器人既要系统性探索，又要兼顾语义目标搜索。现有方法往往偏向单纯几何覆盖或纯语义搜索，前者可能只是“碰巧”发现目标，后者又容易牺牲地图完整性和路径效率，因此如何平衡覆盖与语义引导是核心瓶颈。

#### 方法概述和架构

论文提出 SAGE（Semantic-Aware Guided Exploration），建立在 FALCON 的体积式前沿探索器之上，用 CLIP 把语言语义注入到三维探索规划中。方法的第一部分是对象中心语义记忆：将 RGB-D 图像块的 CLIP embedding 关联到 TSDF 表面的连通分量，形成可更新的对象级 embedding 存储，而不是维护稠密的逐体素语义地图。第二部分是时间缓存：把最近观测沿视线投影到 free-unknown 边界，为前沿区域提前赋予语义相似度，减少“等靠近后才知道是否相关”的延迟。第三部分是 object frontiers：对高相似度目标直接生成面向目标的候选视点，增强近距离发现能力。第四部分是统一的语义-几何代价函数，在 TSP 与 SOP 两级规划中同时考虑语义相似度、障碍代价和路径长度，并限制语义重权重的影响，从而让语义只重排前沿优先级而不破坏整体覆盖目标。推理时，系统在每个重规划周期更新语义记忆与缓存，再据此输出下一步视点和轨迹。

#### 实验结果分析

实验在 Matterport3D 仿真中展开，并与 FALCON、纯语义消融以及 Finding Things in the Unknown (FTU) 比较，评价重点包括目标发现、覆盖效率和体积吞吐量。结果显示，SAGE 在对象发现上优于 FALCON 和语义-only 消融；相较 FTU，在九组共享的 map-query 配对上完成探索速度提升 9.0 到 25.9 倍，平均加速 13.7 倍，同时体积吞吐量也显著更高。真实机器人实验中，作者在两种环境下进行了 5 次实飞，平台为搭载机载感知与规划、并由离线 CLIP 推理支持的 Modal AI Starling 2 四旋翼；结果表明，FALCON 的探索速度和地图轨迹长度更优，但 SAGE 在对象发现方面更强。

<details>
<summary>完整摘要</summary>

本文提出 Semantic-Aware Guided Exploration（SAGE），一种面向未知三维室内环境的开放词汇探索系统。该系统在保留覆盖导向行为的同时，引入语义线索来重新排序前沿（frontier）的选择优先级。SAGE 以 FALCON 的体积式探索器为基础，并通过四个关键组成部分集成 CLIP：对象中心的 embedding 存储、将最近观测投影到 free-unknown 边界的时间缓存、用于高相似度检测的 object frontiers，以及统一的语义-几何规划代价。该代价函数限制语义重加权的影响范围，从而保证前沿会被优先考虑，但不会牺牲总体覆盖。基于 Matterport3D 的仿真结果表明，SAGE 在对象发现方面优于 FALCON 和纯语义消融方法，覆盖多个 map-query 配对均表现更好。与 Finding Things in the Unknown（FTU）相比，SAGE 在九组共享的 map-query 配对上完成探索的速度快 9.0 到 25.9 倍，平均加速达到 13.7 倍；同时，SAGE 的体积吞吐量也显著高于 FTU。最后，我们在一架配备机载感知与规划、并由离线 CLIP 推理支持的 Modal AI Starling 2 四旋翼上，于两个环境中进行了 5 次真实飞行部署。将 SAGE 与 FALCON 对比后发现，尽管 FALCON 的探索更快、建图轨迹更短，但 SAGE 在对象发现方面优于 FALCON。

</details>

---

### [[20_Research/Papers/大模型/RoboSurg-VQA_A_Multimodal_Benchmark_for_Surgical_Segmentation-Aware_Visual_Question_Answering|RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering]]

![[assets/2605.23068_figure.png|800]]

- **arXiv**: [2605.23068](https://arxiv.org/abs/2605.23068)
- **PDF**: https://arxiv.org/pdf/2605.23068
- **详细分析**: [[20_Research/Papers/大模型/RoboSurg-VQA_A_Multimodal_Benchmark_for_Surgical_Segmentation-Aware_Visual_Question_Answering|RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering]]
- **作者**: Chengyi Zhang, Zi Ye, Ziyang Wang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.6（加权：大模型 0.4，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

在机器人辅助手术和微创手术中，视觉理解不能只依赖分割掩码，还需要回答临床人员关于手术阶段、可见性、伪影、解剖结构和器械状态等问题。现实中的术野常常受到遮挡、烟雾、出血和高光反射影响，导致传统分割基准无法充分反映模型在真实手术场景中的理解能力。作者因此关注一个更贴近临床交互需求的任务：将分割感知能力与视觉问答结合，用统一标准评估多模态模型在复杂术野下的可靠性。

#### 方法概述和架构

论文提出 RoboSurg-VQA，一个面向手术场景的 segmentation-aware VQA 基准。其做法是把多个公开手术分割数据集重构为统一的帧级样本，每个样本同时保留 RGB 图像、分割掩码、数据来源和元信息。对于每一帧，系统配套固定的九类问题，覆盖手术上下文、解剖位置、成像模式/视角、出血/烟雾/遮挡等伪影、图像质量、眩光、对比度、中心遮挡以及烟雾区域等，并使用封闭式答案集合以便统一评测。标注阶段采用受约束的模型辅助生成：先通过限制式提示生成候选答案，再进行自动合法性和一致性检查，随后由人工抽检审核、修正或剔除不可靠样本。推理与评测时，模型需要根据图像和掩码回答固定问题集，输出按问题类型使用 Accuracy、Macro-F1、Coverage、Conditional Accuracy 等指标进行统计。

#### 实验结果分析

作者在两个公开手术分割数据集上构建了一个可运行的基准实例，共 11,480 帧，其中 8,745 帧用于训练、2,735 帧用于测试，并跨三个数据源进行统一评测。实验显示，数据存在明显类别不均衡，单看 Accuracy 会被多数类严重“抬高”，因此论文强调以 Macro-F1 作为更合理的主指标；对带 Unknown 的问题，还需同时报告 Coverage 和条件准确率。通过 sanity baseline 和跨模型一致性检查可以看出，该基准能够有效暴露模型在少数类、可见性与伪影判断上的弱点。可见文本未给出传统端到端 SOTA 数值对比，重点在于基准构建、评测协议和挑战分析。

<details>
<summary>完整摘要</summary>

在机器人辅助手术和微创手术（RMIS/MIS）中，可靠的视觉理解要求的不仅仅是准确的分割掩码：在临床实践中，医生常常会围绕手术上下文、可见性、伪影，以及解剖结构和手术器械是否存在等问题进行提问，而这些问题往往发生在被遮挡、烟雾、出血和高光反射所破坏的退化视野中。我们提出 RoboSurg-VQA，这是一个 segmentation-aware 的视觉问答（VQA）基准，通过将公开的手术分割数据集在统一模式下重新利用而构建。每一帧都配有一组固定的、具有临床动机的问题，覆盖手术上下文、解剖（包括区域）、成像模态/视角、手术伪影、图像质量，以及基本的可见性和空间属性，并采用封闭式答案集合以实现一致评测。为扩大标注规模，我们通过受约束的提示生成候选答案，并结合自动合法性与一致性检查，再辅以人工审核，以提升答案的合理性和标签一致性。我们报告了基准统计信息、sanity baseline，以及在复杂手术条件下常见的评测挑战。代码将发布在 https://github.com/ziyangwang007/Robosurg-VQA 。

</details>

---

### [[20_Research/Papers/具身智能/GEM-4D_Geometry-Enhanced_Video_World_Models_for_Robot_Manipulation|GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation]]

![[assets/2605.22882_figure.png|800]]

- **arXiv**: [2605.22882](https://arxiv.org/abs/2605.22882)
- **PDF**: https://arxiv.org/pdf/2605.22882
- **详细分析**: [[20_Research/Papers/具身智能/GEM-4D_Geometry-Enhanced_Video_World_Models_for_Robot_Manipulation|GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation]]
- **作者**: Kaichen Zhou, Yuzhen Chen, Fangneng Zhan, Hang Hua, Grace Chen, Xinhai Chang, Ao Qu, Yilun Du, Zhuang Liu, Paul Pu Liang, Mengyu Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 3.7（加权：具身智能 1.5，大模型 0.1，世界模型 1，机器人 1.1）
- **关联关键词**: LLM, Robotics, WorldModel

#### 研究背景与动机

视频世界模型正在成为机器人操作的重要基础：给定初始观测和语言指令，模型生成未来视频，随后再从视频中恢复可执行动作，用于真实机器人抓取、插入和规划等任务。但现有方法往往只追求画面逼真，却难以保持跨帧的点级对应关系，导致同一个物体表面点在时间上发生不一致的形变、漂移或深度错误，从而使动作提取失去物理依据。论文聚焦于“看起来真实但不可执行”的核心矛盾，试图把几何一致性真正注入视频世界模型，因此对具身智能和机器人操作都很值得关注。

#### 方法概述和架构

论文提出 GEM-4D（Geometry-Enhanced Video World Models for Robot Manipulation），核心思想是把4D几何基础模型提供的密集对应关系作为训练时监督，而不是把深度、法线或光流直接作为模型输出。方法中包含一个视频生成主干和一个几何分支：主干负责根据初始观测与语言指令生成视频潜变量的速度场，几何分支在训练时读取主干的中间特征，并去预测来自预训练4D几何基础模型的表示，从而把相机运动、深度和物体运动等对应关系蒸馏进主干表征。该几何约束采用非对称耦合：几何分支只“读”主干特征、不反向写回，推理阶段完全移除，因此不增加额外推理开销，保持单流生成架构。论文还设计了一个逆动力学模块，将具有对应一致性的生成视频轨迹转换为可执行的6-DoF末端执行器轨迹，形成从语言指令到机器人动作的完整闭环。

#### 实验结果分析

作者在视频预测与几何一致性两类任务上进行了系统实验，覆盖仿真与真实场景，并与多种视频世界模型和几何相关基线比较。结果显示，GEM-4D 在视频预测和几何一致性指标上都达到SOTA，说明其不仅画面更合理，也更能保持跨帧结构稳定。机器人操作方面，真实环境中的成功率从61%提升到81%，提升幅度明显；文中还报告在RLBench上取得63%–82%的成功率。消融实验进一步验证了几何蒸馏和对应一致性约束对性能提升的关键作用。

<details>
<summary>完整摘要</summary>

视频世界模型可以仅根据一条指令生成逼真的未来画面，但它们往往无法在时间上保持一致的点级运动。结果是，生成的视频虽然看起来合理，却缺少可靠动作执行所需的物理落地性，例如机器人操作就会受到影响。我们提出 GEM-4D，这是一种几何落地的视频世界模型：在训练过程中，将从预训练几何基础模型中蒸馏得到的密集4D对应关系监督注入到视频生成主干中，以解决上述问题。该监督使模型能够在保持单流架构的同时，联合捕获外观信息与几何结构，并且不会增加推理开销。我们进一步引入一个逆动力学模块，将对应一致的视频 rollout 转换为可执行的机器人轨迹，从而能够直接部署到真实与仿真环境中的操作任务。GEM-4D 在视频预测和几何一致性方面都达到了最先进性能，且在仿真和真实场景中均表现优异，并将真实世界机器人操作成功率从61%提升到81%。更多结果见项目页面：https://anonymous-submission-20.github.io/gem.github.io/。

</details>

---
