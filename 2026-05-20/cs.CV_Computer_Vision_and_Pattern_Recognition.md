# cs.CV | Computer Vision and Pattern Recognition | 2026-05-20

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/具身智能/Minimalist_Visual_Inertial_Odometry|Minimalist Visual Inertial Odometry]]

![[assets/2605.19990_figure.png|800]]

- **arXiv**: [2605.19990](https://arxiv.org/abs/2605.19990)
- **PDF**: https://arxiv.org/pdf/2605.19990
- **详细分析**: [[20_Research/Papers/具身智能/Minimalist_Visual_Inertial_Odometry|Minimalist Visual Inertial Odometry]]
- **作者**: Francesco Pasti, Jeremy Klotz, Nicola Bellotto, Shree K. Nayar
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

视觉惯性里程计（VIO）是移动机器人导航中的关键技术，但传统方案通常依赖高分辨率相机，需要采集和处理大量像素，带来明显的算力与能耗开销。对于资源受限平台，尤其是需要长期自主运行的差分驱动机器人，这种“高像素”感知并不理想。本文关注的是平面里程计问题，尝试回答一个更极端的问题：在只保留极少量视觉测量的情况下，能否依然稳定估计机器人的运动轨迹。该工作值得关注之处在于，它把“最小化感知”推进到仅四个视觉测量加一个IMU，并在真实机器人上验证了可行性。

#### 方法概述和架构

论文提出 Minimalist Visual Inertial Odometry：使用4个朝下的光电二极管作为视觉传感单元，每个二极管前放置光学 Gabor mask，让地面纹理在光学域被直接滤波为低维时序信号。作者从频域分析出发，说明传感器随机器人前进时，输出信号中的主频与线速度成正比，因此可以从时序中反推速度大小。为解决单个传感器无法区分运动方向的问题，系统采用两组相位正交的 mask（cos 与 sin）来消除方向歧义，并结合IMU提供的角速度恢复完整平面轨迹。方法上，作者在一个物理可信的模拟器中端到端联合优化 Gabor mask 参数与 Temporal Convolutional Network（TCN）解码器，使网络从四路传感器输出中回归线速度；推理阶段将该速度估计与IMU的yaw rate融合，得到连续位姿轨迹。

#### 实验结果分析

实验在搭载原型传感器的差分驱动机器人上完成，覆盖了多种室内与室外地形，并在无需真实世界微调的情况下与参考真值进行对比。节选中给出的结果显示，系统在87分钟、920米的行驶测试中能较好跟踪真值轨迹，平均ATE为0.34米，平均终点漂移为0.60%。与轮式编码器和IMU融合的基线相比，该方法的ATE和漂移更低，说明极简感知并未明显牺牲里程计精度。除此之外，节选文本未给出更完整的消融细节与全部数值。

<details>
<summary>完整摘要</summary>

视觉惯性里程计（VIO）对于移动机器人导航至关重要，但其通常依赖具有大量像素的相机。采集和处理相机图像需要消耗大量资源。本文提出一种用于平面里程计的极简方法，证明仅凭四个视觉测量值和一个IMU，就可以为差分驱动机器人提供鲁棒的运动估计。我们的核心洞见是：四个朝下的光电二极管通过光学 Gabor mask 感知世界时，其输出信号能够编码速度。基于这一点，我们在一个具有物理基础的模拟器中，联合优化 mask 参数与 Temporal Convolutional Network（TCN）。最终得到的模型能够仅根据光电二极管产生的四路测量解码速度。将这些估计与IMU给出的角速度进行配合，即可得到连续的平面轨迹。我们在安装了原型传感器的差分驱动机器人上验证了该方法。在多样的室内和室外地形上，该系统在没有任何真实世界微调的情况下，均能紧密跟踪参考真值。我们的工作表明，极简感知能够实现高效且准确的平面里程计。

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Binary_Success_A_Diagnostic_Meta-Evaluation_Framework_for_Fine-Grained_Manipulation|Beyond Binary Success: A Diagnostic Meta-Evaluation Framework for Fine-Grained Manipulation]]

![[assets/2605.19986_figure.png|800]]

- **arXiv**: [2605.19986](https://arxiv.org/abs/2605.19986)
- **PDF**: https://arxiv.org/pdf/2605.19986
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Binary_Success_A_Diagnostic_Meta-Evaluation_Framework_for_Fine-Grained_Manipulation|Beyond Binary Success: A Diagnostic Meta-Evaluation Framework for Fine-Grained Manipulation]]
- **作者**: He-Yang Xu, Pengyuan Zhang, Zongyuan Ge, Xiaoshuai Hao, Serge Belongie, Xin Geng, Yuxin Peng, Xiu-Shen Wei
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

在具身智能和机器人操作中，粗粒度的“拿起/放下是否成功”已经不足以衡量真实能力，尤其是在穿针引线、精密插接、按部位抓取等细粒度操作任务里，任务成功取决于语义理解、局部空间感知和受约束控制的协同。现有基准通常把这些能力压缩成二元成功率，容易把“看起来完成了”误判为“真正会操作”，从而掩盖模型在真实部署中的关键短板。本文因此值得关注，因为它不仅指出当前评测可能高估能力，还试图把评测从“排名”转向“诊断”，为后续模型修复提供可操作的方向。

#### 方法概述和架构

作者提出 MetaFine，一个面向细粒度操作的诊断型元评测框架。该框架围绕三条能力轴展开：理解、感知和受控行为，并通过复合任务图将不同外部基准吸收到统一协议下，重构为不同复杂度的诊断场景。对于理解能力，MetaFine 通过控制语义干预，在保持场景不变的情况下替换属性级指令，测试模型是否真的把语言与局部目标对应起来。对于感知能力，框架施加分级的几何扰动和光照等光度扰动，并用成功率及 AUSC 等指标衡量鲁棒性。对于行为能力，MetaFine 将长时序任务拆解为原子技能阶段，分别评估阶段性成功和轨迹平滑性，以定位执行在哪一步失稳。作者还引入混合真机-仿真验证流程，利用少量配对真实回合来校准基于仿真的可扩展评测估计。

#### 实验结果分析

作者在统一条件下评测了 7 种代表性 VLA/操控策略，包括 ACT、DP3、Octo、OpenVLA、OpenVLA-OFT、π0 和 π0.5，任务覆盖抓取部位、按压、旋转、插接等原子技能，以及 peg-in-hole、plug-in-charger、stack-pyramid 等长时序组合任务。结果显示，传统二元成功率会显著夸大能力：在更严格的细粒度约束和扰动下，某些模型的表面能力可出现最高约 70% 的“虚高”。在语义干预实验中，所有被测 VLA 在替换属性指令后都未能正确重定向行为，相关任务上成功率为 0%，表明其并未真正实现可组合的语义落地。正文节选还指出，作者通过视觉编码器的针对性因果干预发现，保留局部空间结构是精密操作的关键瓶颈；但节选中未给出全部实验的具体数值细节。

<details>
<summary>完整摘要</summary>

细粒度操作进入了一个新的阶段：此时全局场景上下文已不足以支持任务完成，成功取决于局部属性落地、高保真空间感知以及遵守约束的运动执行之间的紧密耦合。然而，现有具身智能基准往往把这些能力压缩为二元成功率，这会系统性地高估报告性能，最高可达 70%，并掩盖阻碍真实部署的架构瓶颈。为此，我们提出 MetaFine，一个诊断型元评测框架，它从理解、感知和受控行为三个维度解耦细粒度操作能力。MetaFine 构建在复合任务图之上，能够吸收异构外部基准，并在统一协议下将其重构为不同复杂度的诊断场景。我们使用最先进的视觉-语言-动作（VLA）模型进行评测，结果表明，许多在传统指标下看似表现良好的模型，在不同维度上都存在严重失败，而这些失败在常规指标中是看不见的。通过有针对性的因果干预，我们识别出视觉编码器保持局部空间结构的能力是细粒度精度的关键瓶颈；提升这一能力，可以在不修改下游策略的情况下直接解锁此前无法实现的操作能力。MetaFine 还支持混合真机-仿真验证：通过有限的配对真实世界回合来校准可扩展的仿真估计，从而获得更稳定的物理评测。通过将评测从“排序”转向“诊断”，MetaFine 把基准测试变成了一个可操作的指南针，用于修复支撑真实物理灵巧性的多层能力结构。MetaFine 框架、基准及相关资源将公开发布在项目主页：https://metafine.github.io/。

</details>

---

### [[20_Research/Papers/大模型/AffectVerse_Emotional_World_Models_for_Multimodal_Affective_Computing|AffectVerse: Emotional World Models for Multimodal Affective Computing]]

![[assets/2605.19950_figure.png|800]]

- **arXiv**: [2605.19950](https://arxiv.org/abs/2605.19950)
- **PDF**: https://arxiv.org/pdf/2605.19950
- **详细分析**: [[20_Research/Papers/大模型/AffectVerse_Emotional_World_Models_for_Multimodal_Affective_Computing|AffectVerse: Emotional World Models for Multimodal Affective Computing]]
- **作者**: Bo Zhao, Fanghua Ye, Yixin Ji, Sicheng Zhao, Xiaojiang Peng, Zitong YU
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.1（加权：大模型 0.5，世界模型 0.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

多模态情感计算的目标，是综合视频、音频和文本线索来识别人类情绪，广泛用于人机交互、内容审核、心理健康分析和面试评估等场景。现有多模态大模型往往把情绪识别当作对完整输入的静态融合，容易忽略情绪在时间上的演化，例如情绪升级、缓和以及跨模态冲突。本文关注的价值在于：它把“情绪理解”从静态分类推进到基于部分观察的预测式信念更新，这与世界模型在动态建模中的思想高度契合。

#### 方法概述和架构

论文提出 AffectVerse，基于 Qwen2.5-Omni 构建，并引入 Emotion World Module（EWM）来建模短时域的潜在情绪演化。EWM 由三部分组成：Cross-Modal Temporal Imagination 先基于过去的音视频 token 进行跨模态多步未来表示预测；MAMA（Modality-Aware Multi-step Attention）Belief Aggregation 再把多步想象得到的 token 压缩成少量、带模态意识的 belief token；最后通过 Belief Injection 将这些 belief token 插入到 LLM 隐空间中，用于后续情感推理。训练时，模型把“预测未来表示”作为一种过去条件下的自监督信号，不要求推理阶段访问未来信息，只是迫使当前 belief state 编码对后续情绪变化有预测力。具体流程上，先对视频/音频隐藏状态做瓶颈投影和时间切分，再用独立的跨注意力想象分支进行多步 rollout，随后将视频和音频的想象结果汇入记忆库，经 MAMA 形成 belief token，并与原始上下文交错注入到 Qwen2.5-Omni 中。

#### 实验结果分析

作者在 9 个基准上评估了 AffectVerse，相比其他模型整体至少提升 2.57%。节选中未给出具体数据集名称、指标细节和各基线的完整数值，因此可见文本未给出具体数值。消融实验表明，时间想象、跨模态 rollout 和 belief aggregation 都带来可叠加的收益，说明该方法的增益并非来自单一模块。总体上，实验支持了“用预测式信念状态建模来做情感计算”是一条有效路线。

<details>
<summary>完整摘要</summary>

人类在判断情绪时，会把观察到的多模态线索与对情感状态可能如何演化的预期结合起来进行推断。然而，现有多模态大语言模型（MLLMs）通常把情绪识别视为对完整音视频-文本输入的静态融合，从而使情绪动态被隐式处理。为此，我们提出 AffectVerse，这是一个基于 Qwen2.5-Omni 的模型，并配备 Emotion World Module（EWM），即一个无动作、表示层级的短时潜在情感预测模块。EWM 包含三个模块：1）Cross-Modal Temporal Imagination，利用多步 rollout 从过去的 token 预测未来的视频/音频表示；2）MAMA（Modality-Aware Multi-step Attention）Belief Aggregation，将想象出的 token 压缩为具备模态感知的 belief token；3）Belief Injection，将这些 belief token 注入到 LLM 中用于情感推理。AffectVerse 将未来预测作为一种基于过去条件的自监督信号：它不会替代对已观测历史的建模，也不要求在推理时使用未见信号，但它会迫使当前的 belief state 编码能够预测后续情感变化的转移线索。在 9 个基准上，AffectVerse 相比其他模型至少提升 2.57%；而受控消融实验表明，时间想象、跨模态 rollout 和 belief aggregation 都带来了可叠加的增益。这些结果表明，预测式 belief-state 建模是情感计算中的一种实用替代方案。

</details>

---

### [[20_Research/Papers/具身智能/Aero-World_Action-Conditioned_Aerial_Video_Generation_from_Inertial_Controls|Aero-World: Action-Conditioned Aerial Video Generation from Inertial Controls]]

![[assets/2605.19728_figure.png|800]]

- **arXiv**: [2605.19728](https://arxiv.org/abs/2605.19728)
- **PDF**: https://arxiv.org/pdf/2605.19728
- **详细分析**: [[20_Research/Papers/具身智能/Aero-World_Action-Conditioned_Aerial_Video_Generation_from_Inertial_Controls|Aero-World: Action-Conditioned Aerial Video Generation from Inertial Controls]]
- **作者**: Abdul Mohaimen Al Radi, Kunyang Li, Yuzhang Shang, Mubarak Shah, Yu Tian
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.6，大模型 0.1，机器人 0.2）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

现有基础视频生成模型虽然画面逼真，但主要依赖自然语言条件，难以直接利用机器人和无人机所需的低层控制信号，因此在具身智能中的可用性有限。对于无人机这类在 6-DoF 空间中飞行的系统，轻微的姿态或位移误差都会迅速累积为明显轨迹漂移，使得“动作可控且物理一致”的视频生成尤其困难。论文关注的价值在于：如果能够生成严格遵循惯性控制的航拍视频，就能为无人机智能体提供可扩展、低成本、可控的训练和评测代理。

#### 方法概述和架构

论文提出 Aero-World，将预训练的 image-to-video 扩散模型改造成可由惯性动作控制的航拍视频生成器。方法输入为起始帧和一段 30Hz 的 6 维 IMU 序列，包含三轴线加速度与三轴角速度；输出则是与该动作序列对齐的航拍视频回放。核心上，Aero-World 通过一个 action-token stream 将动作嵌入注入到潜空间扩散 Transformer 中，同时加入一个冻结的 latent-space Physics Probe，用来从生成视频的潜变量中预测惯性状态，并在 LoRA 微调阶段提供可微分的惯性一致性监督。Physics Probe 先在真实视频-IMU 配对数据上独立训练，之后保持冻结；训练生成器时，损失由标准扩散去噪损失和 probe 规则项共同组成，推理时则移除 probe，仅保留动作条件生成。论文还提出 AeroBench 作为评测基准，并用 AAS 衡量动作对齐程度、用 PCR 衡量时间上运动是否稳定。

#### 实验结果分析

论文在 AeroBench 上评估了 Aero-World，并与仅做动作微调的方法以及 AirScape 进行了对比。结果显示，Aero-World 的平均 AAS 从 57.7 提升到 63.6，同时在质量与控制之间取得更优折中：FVD 更低、SSIM 更高、Flow-IMU correlation 也更高，其中对应数值分别为 596.5 vs. 1058.6、0.595 vs. 0.505、0.44 vs. 0.20。节选内容未给出更多消融或泛化的具体数值，但整体结论表明，冻结 Physics Probe 所提供的监督是将预训练视频生成器适配为动作对齐航拍生成器的有效机制。

<details>
<summary>完整摘要</summary>

基础视频模型可以生成视觉上很惊艳的结果，但它们在具身智能中的用途仍然有限，因为这类模型主要基于自然语言训练，而不是低层控制信号。对于航拍飞行而言，这一限制尤其突出，因为运动发生在不受约束的 6 自由度空间中，且自运动的微小误差就可能导致轨迹显著漂移。生成能够遵循细粒度惯性动作的航拍视频，可以为航拍智能体的大规模训练与评测提供支持，作为真实世界数据或高成本仿真数据的可控替代。为解决这一问题，我们提出 Aero-World，一种将预训练的 image-to-video 扩散模型转换为可控航拍视频生成器的方法。Aero-World 通过动作 token 流，将由平移加速度和角速度组成的序列注入预训练的 latent diffusion transformer。一个在真实 video-IMU 配对数据上独立训练、并保持冻结的 latent-space Physics Probe，在 LoRA 微调期间提供可微分的惯性一致性监督，同时避免了代价高昂的视频解码。我们还提出 AeroBench，一个用于评估生成的无人机视频是否遵循低层动作信号的基准。AeroBench 使用 Action Alignment Score（AAS）衡量与指令惯性动作的一致性，并使用 Physical Consistency Rate（PCR）衡量时间上的运动稳定性。在 AeroBench 上，Aero-World 相比仅做动作微调的方法，将平均 AAS 从 57.7 提升到 63.6，并且在质量-控制折中上优于 AirScape，表现为更低的 FVD（596.5 vs. 1058.6）、更高的 SSIM（0.595 vs. 0.505）以及更高的 Flow-IMU correlation（0.44 vs. 0.20）。这些结果表明，冻结的 Physics Probe 监督是一种将预训练视频生成器适配为更符合动作的航拍运动的实用机制。

</details>

---

### [[20_Research/Papers/世界模型/HEAT_Heterogeneous_End-to-End_Autonomous_Driving_via_Trajectory-Guided_World_Models|HEAT: Heterogeneous End-to-End Autonomous Driving via Trajectory-Guided World Models]]

![[assets/2605.19631_figure.png|800]]

- **arXiv**: [2605.19631](https://arxiv.org/abs/2605.19631)
- **PDF**: https://arxiv.org/pdf/2605.19631
- **详细分析**: [[20_Research/Papers/世界模型/HEAT_Heterogeneous_End-to-End_Autonomous_Driving_via_Trajectory-Guided_World_Models|HEAT: Heterogeneous End-to-End Autonomous Driving via Trajectory-Guided World Models]]
- **作者**: Hoonhee Cho, Giwon Lee, Jae-Young Kang, Hyemin Yang, Heejun Park, Kuk-Jin Yoon
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

端到端自动驾驶希望直接从原始传感器输入预测驾驶轨迹或控制动作，避免依赖传统模块化流水线中的显式感知与中间表示。但现有方法通常在单一数据集上表现较好，一旦联合不同城市、不同传感器配置或不同交通模式的异构数据训练，性能就会明显下降，说明多域学习中存在相互冲突的学习信号。该论文关注的问题非常实际：如何让一个统一模型在多个异构自动驾驶域上同时保持稳定性能，而无需针对每个域单独重训。

#### 方法概述和架构

论文提出 HEAT（Heterogeneous End-to-End Autonomous Driving via Trajectory-Guided World Models），核心思路是用“轨迹”而不是“外观”来组织学习。方法分三阶段：第一阶段先预训练一个以轨迹为条件的 world model，把当前视觉特征与未来驾驶轨迹耦合起来，学习动作相关、域无关的潜表示，并用下一时刻的视觉潜变量进行自监督预测。第二阶段对预训练得到的行为表征做 trajectory-guided behavior clustering，将跨数据集样本按规划轨迹相似性聚类，提取 trajectory-guided visual prototypes 和 visual-coupled action memory，作为域无关先验。第三阶段从头训练端到端自动驾驶模型，利用这些先验通过对比学习对齐表征，并用记忆模块细化动作一致性，从而在多域联合训练时减轻域偏置和冲突。整体上，输入是多视角环视图像及其轨迹监督，输出是 BEV 平面上的未来 waypoints。

#### 实验结果分析

作者在 nuScenes、NAVSIM 和 Waymo end-to-end dataset 三个基准上进行联合评估，构建了一个面向异构域的端到端自动驾驶设置。实验结论显示，HEAT 在三个数据集上都比已有方法更强，说明单一统一模型可以在异构数据上实现较好的跨域融合与域内性能保持。正文还强调了该方法在多域泛化和鲁棒性方面的优势，但可见文本未给出具体数值。消融实验与讨论部分表明，trajectory-guided 学习和 world model 对缓解域偏差、提升特征一致性都起到了关键作用。

<details>
<summary>完整摘要</summary>

端到端自动驾驶作为传统模块化流水线的一种有力替代方案，近年来受到广泛关注。它直接将原始传感器数据映射为驾驶动作。尽管近期方法在单域数据集上取得了很强的性能，但当它们在多个异构域上联合训练时，性能会显著下降。然而在实际场景中，自动驾驶系统必须能够在多样化环境中运行，这些环境具有异构分布，包括不同城市、传感器配置和交通模式，而且不能依赖针对特定域的重新训练。这一差距揭示了多域学习中的一个关键挑战：异构域中的域特定变化会引入相互冲突的学习信号，推动模型收敛到一种折中的解，从而使其在各个域上都不是最优。为了解决这一问题，我们提出一种 trajectory-driven 的学习范式，以规划轨迹为中心组织训练，使模型能够捕获与域无关的驾驶意图表征。此外，我们引入一个 world model，在 ego 动作条件下预测未来的潜在特征，从而提升特征一致性并减轻由域引起的偏置。我们在三个基准数据集 nuScenes、NAVSIM 和 Waymo end-to-end dataset 上评估该方法，并展示了其在所有域上相较于现有方法的显著提升。结果表明，可以训练一个统一模型来处理异构数据集，同时在每个域内保持较强性能，这为可扩展的真实世界部署迈出了重要一步。我们将公开代码。

</details>

---

### [[20_Research/Papers/具身智能/SafeAlign-VLA_A_Negative-Enhanced_Safe_Alignment_Framework_for_Risk-Aware_Autonomous_Driving|SafeAlign-VLA: A Negative-Enhanced Safe Alignment Framework for Risk-Aware Autonomous Driving]]

![[assets/2605.19524_figure.png|800]]

- **arXiv**: [2605.19524](https://arxiv.org/abs/2605.19524)
- **PDF**: https://arxiv.org/pdf/2605.19524
- **详细分析**: [[20_Research/Papers/具身智能/SafeAlign-VLA_A_Negative-Enhanced_Safe_Alignment_Framework_for_Risk-Aware_Autonomous_Driving|SafeAlign-VLA: A Negative-Enhanced Safe Alignment Framework for Risk-Aware Autonomous Driving]]
- **作者**: Kefei Tian, Yuansheng Lian, Kai Yang, Xiangdong Chen, Shen Li
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，强化学习 0.4，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

端到端自动驾驶在常规场景中表现良好，但在碰撞、近失误等安全关键长尾场景中仍然容易失效。现有不少 Vision-Language-Action（VLA）自动驾驶方法主要依赖正向专家示范，较少利用负样本，因此对“哪些行为危险、危险边界在哪里”的学习不足。作者认为，将负样本系统性纳入训练，有望让模型不仅学会“怎么开”，还学会“哪些情况不能开、如何纠错”，这对风险感知自动驾驶很有价值。

#### 方法概述和架构

论文提出 SafeAlign-VLA，一个面向风险感知自动驾驶的负样本增强安全对齐框架。整体由三部分组成：基于视觉与语言输入的 VLA 规划主干、用于构造正负配对监督的反事实安全配对模块，以及两阶段后训练策略。首先，模型输入包含多视角相机图像、历史轨迹状态、任务提示和高层驾驶指令，输出既包括语义推理文本，也包括未来轨迹/动作。其次，反事实安全配对会从高风险片段中自动生成结构化安全标签，并通过反事实推理构造对应的“正向替代轨迹”，从而形成正负对照数据。训练上，第一阶段进行负样本增强的监督微调，用于故障反馈与轨迹纠偏；第二阶段采用基于锚点的组相对策略优化（GRPO），把正、负轨迹作为对比锚点来引导采样，并通过组相对优势惩罚高风险行为，进一步优化动作头。

#### 实验结果分析

实验在 NAVSIM 和 DeepAccident 两个基准上验证了该方法。根据摘要给出的结果，SafeAlign-VLA 在 NAVSIM v1 测试集上取得 89.1 PDMS，相比不使用负样本的基线提升 1.3%。在 DeepAccident 上，碰撞率降至 3.36%，同时语言准确率达到 84.2%，风险预测准确率达到 85.8%。整体来看，结果表明负样本增强的安全对齐策略能有效提升自动驾驶在长尾风险场景中的鲁棒性与安全性；正文节选中未给出更多消融细节。

<details>
<summary>完整摘要</summary>

端到端自动驾驶系统在常见场景中表现出色，但在安全关键的长尾场景中仍然面临挑战。由于具备较强的推理能力，Vision-Language-Action（VLA）模型被认为具有潜力。然而，大多数基于 VLA 的方法依赖正向专家示范，很少利用负样本，导致模型对风险行为和安全边界缺乏充分理解。为解决这一问题，我们提出 SafeAlign-VLA，一种统一的负样本增强安全对齐框架，将负样本同时纳入监督学习和强化学习之中。首先，我们设计了反事实安全配对范式，通过反事实推理从高风险场景中生成结构化安全标签以及反事实的正向轨迹。随后采用两阶段训练策略：先进行负样本增强的监督微调，用于故障反馈和轨迹纠正；再进行基于锚点的组相对策略优化，将正负轨迹作为对比锚点来引导采样，并通过组相对优势对高风险行为施加惩罚。我们在 NAVSIM 和 DeepAccident 上进行了实验验证。SafeAlign-VLA 在 NAVSIM v1 测试集上取得 89.1 PDMS，相比不使用负样本的基线提升了 1.3%。在 DeepAccident 上，它将碰撞率降低到 3.36%，同时实现了 84.2% 的语言准确率和 85.8% 的风险预测准确率。结果表明，该负样本增强的安全对齐框架能够有效提升自动驾驶系统的安全性与鲁棒性。

</details>

---

### [[20_Research/Papers/具身智能/SWEET_Sparse_World_Modeling_with_Image_Editing_for_Embodied_Task_Execution|SWEET: Sparse World Modeling with Image Editing for Embodied Task Execution]]

![[assets/2605.19319_first_page.png|800]]

- **arXiv**: [2605.19319](https://arxiv.org/abs/2605.19319)
- **PDF**: https://arxiv.org/pdf/2605.19319
- **详细分析**: [[20_Research/Papers/具身智能/SWEET_Sparse_World_Modeling_with_Image_Editing_for_Embodied_Task_Execution|SWEET: Sparse World Modeling with Image Editing for Embodied Task Execution]]
- **作者**: Yiren Song, Yihan Wang, Xiyao Deng, Zhuoran Yan, Mike Zheng Shou
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.1（加权：具身智能 1.5，世界模型 0.2，机器人 0.4）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

在具身智能与机器人操作中，常见做法是先预测未来视觉状态，再将其转化为动作，从而实现基于视觉的规划与控制。但对于许多操作任务来说，直接生成密集视频不仅计算开销大，而且往往并非必要，因为任务推进通常可以被少量与任务相关的关键视觉状态概括。本文因此关注一个重要问题：图像编辑模型能否作为稀疏的视觉世界模型，用较低成本预测任务级未来状态，而不需要完整的视频展开。

#### 方法概述和架构

作者首先在相同机器人数据设置下，对视频生成模型 Wan2.2 与图像编辑模型 FLUX-Kontext 进行受控对比，用以检验两类生成范式在机器人任务中的适用性。结果表明，图像编辑更适合生成可靠的任务级关键帧，因此论文进一步提出 SWEET，一个一次性的稀疏视觉规划框架。SWEET 通过连续的图像编辑，逐步生成一串与操作过程相关的关键帧，并以语言指令作为条件，必要时还可加入基于箭头的空间引导。随后，一个目标条件扩散动作预测器将相邻的想象关键帧转换为可执行的动作片段。为缓解真实视觉子目标与编辑后子目标之间的分布偏差，方法还引入了混合训练策略，并使用过滤后的编辑目标进行训练。

#### 实验结果分析

作者在 DROID 和 RoboMimic 上进行了实验，评估了关键帧预测以及从关键帧规划到动作执行的完整流程。结果显示，SWEET 在已见与未见场景中都能提升关键帧预测效果，并且能够支撑从顺序关键帧规划到机器人动作执行的端到端管线。与视频生成路线相比，基于图像编辑的方案在视觉保真度和推理成本上更有优势；不过摘要未给出具体数值，因此可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

视觉预测已经成为具身控制中一种很有前景的范式，即先生成未来观测，再将其转化为动作。然而，密集视频生成计算开销很大，而且对于许多操作任务来说往往没有必要，因为这些任务的进展可以由少量与任务相关的视觉状态来概括。本文研究图像编辑模型是否可以作为稀疏视觉世界模型，用于机器人操作中预测任务级的未来状态，而无需进行密集的视频展开。我们首先在相同的机器人数据设置下，对视频生成模型 Wan2.2 与图像编辑模型 FLUX-Kontext 进行受控比较，发现图像编辑能够生成更可靠的任务级关键帧，具有更好的视觉保真度，并且推理成本显著更低。受这一观察启发，我们提出 SWEET，一种一次性的稀疏视觉规划框架，它在语言指令和可选的基于箭头的空间引导条件下，通过连续的图像编辑逐步生成一系列与任务相关的操作关键帧。随后，一个目标条件扩散动作预测器将相邻的想象关键帧转换为可执行的动作片段。为了减轻真实视觉子目标与编辑后视觉子目标之间的不匹配，我们进一步引入了带过滤编辑目标的混合训练策略。在 DROID 和 RoboMimic 上的实验表明，SWEET 能够提升已见和未见场景中的关键帧预测效果，并支持从顺序关键帧规划到可执行机器人动作的完整流程，这说明图像编辑是具身视觉预测中一种很有前景但尚未充分探索的方向。

</details>

---

### [[20_Research/Papers/大模型/MetaRA_Metamorphic_Robustness_Assessment_for_Multimodal_Large_Language_Model-based_Visual_Question_Answering_Systems|MetaRA: Metamorphic Robustness Assessment for Multimodal Large Language Model-based Visual Question Answering Systems]]

![[assets/2605.19307_figure.png|800]]

- **arXiv**: [2605.19307](https://arxiv.org/abs/2605.19307)
- **PDF**: https://arxiv.org/pdf/2605.19307
- **详细分析**: [[20_Research/Papers/大模型/MetaRA_Metamorphic_Robustness_Assessment_for_Multimodal_Large_Language_Model-based_Visual_Question_Answering_Systems|MetaRA: Metamorphic Robustness Assessment for Multimodal Large Language Model-based Visual Question Answering Systems]]
- **作者**: Quanxing Xu, Yuhao Tian, Ling Zhou, Xian Zhong, Xiaohua Huang, Rubing Huang, Chia-Wen Lin
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

视觉问答（VQA）是多模态大模型（MLLM）评估推理能力的代表性任务，常用于检验模型对图像内容、文本线索以及跨模态关系的理解。现有VQA评测大多依赖静态数据集和准确率指标，虽然能反映“答对多少”，却难以揭示模型在鲁棒性、一致性和泛化性上的真实表现。本文关注一个更现实的问题：当图像或问题发生轻微、可控变化时，MLLM-based VQA 系统是否仍能保持稳定输出，这对于可信多模态AI非常关键。

#### 方法概述和架构

论文提出 MetaRA（Metamorphic Robustness Assessment），一种基于变形测试（Metamorphic Testing, MT）的VQA鲁棒性评估框架。其核心思想是先从原始图文对输入出发，构造若干满足预期逻辑关系的变换样本，再检查模型在原始样本与变换样本上的输出是否保持一致。框架包含四个阶段：输入理解、测试用例生成、推理测试和失败检测，其中输入理解模块先评估图文对的难度，再据此决定后续变换强度与组合方式。测试用例生成同时覆盖图像和问题两个模态：图像侧包括水平翻转、风格迁移、局部特征修改、场景信息改变以及缩放、旋转、平移等几何变换；问题侧则采用同义改写和成分替换等句子变体。随后将原始输入与多组变换输入组成测试集批量送入模型，比较各输入下答案是否满足预设的 metamorphic relations，并结合输入顺序重复测试，以分析模型对顺序效应的敏感性。

#### 实验结果分析

作者在知识型VQA（KBVQA）和OCR-VQA等任务上，对多种主流 MLLM-based VQA 模型进行了系统测试，评估其在不同变换关系下的鲁棒性表现。结果表明，MetaRA 不仅能够发现传统准确率无法暴露的失效模式，还能更细致地区分模型对语言扰动、浅层视觉线索依赖以及跨模态推理不足等不同脆弱点。实验还显示，当前模型对全局扰动相对稳健，但对细粒度局部视觉变化和隐含文本知识变动仍较敏感。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

视觉问答（VQA）作为代表性的多模态任务，是评估多模态大语言模型（MLLM）推理能力的重要基准。然而，现有评测大多依赖静态数据集和基于准确率的指标，无法体现鲁棒性、一致性与泛化能力。受变形测试（Metamorphic Testing, MT）启发，我们提出 Metamorphic Robustness Assessment（MetaRA），这是一个利用变形关系（Metamorphic Relations, MRs）系统性探测 MLLM-based VQA 系统脆弱性的测试框架。MetaRA 基于特定的 MRs 生成受控的图像-问题输入变体，并在多种条件下评估模型。将 MetaRA 应用于多个不同任务上的 MLLM-based VQA 模型后，揭示出一系列细致的失效模式，包括对语言扰动的敏感性、对表面视觉线索的过度依赖，以及多模态推理层面的更深层次弱点。实验结果表明，MetaRA 相比传统准确率指标能够提供更丰富的诊断信息，暴露出在标准基准下难以发现的失效模式。总体而言，这项工作强调了对VQA进行系统化鲁棒性评估的必要性，并将变形评估定位为一种可扩展、与模型无关的可信多模态AI评估方法。

</details>

---

### [[20_Research/Papers/具身智能/EgoTraj_Real-World_Egocentric_Human_Trajectory_Dataset_for_Multimodal_Prediction|EgoTraj: Real-World Egocentric Human Trajectory Dataset for Multimodal Prediction]]

![[assets/2605.19004_figure.png|800]]

- **arXiv**: [2605.19004](https://arxiv.org/abs/2605.19004)
- **PDF**: https://arxiv.org/pdf/2605.19004
- **详细分析**: [[20_Research/Papers/具身智能/EgoTraj_Real-World_Egocentric_Human_Trajectory_Dataset_for_Multimodal_Prediction|EgoTraj: Real-World Egocentric Human Trajectory Dataset for Multimodal Prediction]]
- **作者**: Ahmad Yehia, Abduallah Mohamed, Tianyi Wang, Jiseop Byeon, Kun Qian, Junfeng Jiao, Christian Claudel
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.6，大模型 0.4，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

从第一人称视角预测人的行走轨迹，是人形机器人、可穿戴感知系统和辅助导航中的关键能力，尤其适用于 AR/VR、盲人导引和社交环境下的机器人导航。现有轨迹预测研究大多依赖俯视视角或固定摄像头数据，只能观察外显运动，难以建模人如何基于视觉注意、头部朝向和场景理解来形成下一步行动意图。相比之下，真实城市环境中的第一人称轨迹数据非常稀缺，且往往缺少同步的 gaze 和 6DoF 位姿，这限制了意图感知轨迹预测的发展。因此，这篇工作值得关注的核心原因在于：它补足了真实世界第一人称多模态轨迹数据的空白，并面向具身智能与辅助 AR 导航提供了可直接使用的数据与基准。

#### 方法概述和架构

论文提出 EgoTraj，一个基于 Meta Quest Pro 采集的第一人称多模态开放数据集。数据由 75 段真实城市导航序列组成，覆盖不同参与者在室外人行道、斑马线和繁忙街道中的自选路径；每段录制同步提供 RGB 视频、连续时间对齐的 6DoF 头部姿态、逐帧 3D 眼动 gaze 向量以及场景标注。作者通过自定义 Unity 采集应用接入 MQPro 的视觉-惯导 SLAM 系统，并以 30 Hz 记录多模态信号，形成可用于轨迹预测的统一输入；随后对数据进行多阶段处理、去隐私、场景标注和 gaze 校准。为了验证数据集价值，论文在 EgoTraj 上建立了第一人称轨迹预测基准，评测多种现有 SOTA 方法，并通过消融实验分析 gaze、场景上下文和运动线索对预测的贡献。

#### 实验结果分析

作者在 EgoTraj 上对多种现有轨迹预测基线进行了定量和定性评测，并做了消融研究；从节选文本可见，实验重点比较了 gaze、场景与运动信息的作用。结果表明，EgoTraj 能有效支持第一人称轨迹预测、AR 感知与辅助导航等下游任务。文本还强调该数据集具有更长时程的自发导航、多样化城市路线和较广的参与者差异，能够更好检验模型的泛化能力。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

从第一人称视角准确预测人的轨迹，在类人机器人、可穿戴感知系统和辅助导航等应用中具有核心作用。然而，由于真实世界中收集到的第一人称轨迹数据集十分稀缺，这一方向的进展仍然有限。为解决这一需求，我们提出 EgoTraj，这是一个使用 Meta Quest Pro（MQPro）录制的第一人称多模态开放数据集。EgoTraj 包含 75 段在真实城市环境中由多位 MQPro 佩戴者采集的人类导航序列。每段录制都提供了同步的 RGB 视频以及真实标注数据，包括连续时间同步的 6 自由度头部位姿、逐帧 3D 眼动 gaze 向量和场景标注。据我们所知，EgoTraj 区别于典型的第一人称轨迹数据集，它捕捉了跨越多样城市路线的长时程、自主导航，并具有广泛的参与者多样性。为展示该数据集的潜力，我们对多种当前最先进的第一人称轨迹预测方法进行了基准测试，并开展消融研究，以分析 gaze、场景和运动线索的贡献。实验结果表明，EgoTraj 对基于 AR 的感知、导航和辅助系统具有重要价值。EgoTraj 数据集、代码以及 EgoViz Dashboard 已公开发布于 https://github.com/yehiahmad/EgoTraj 。

</details>

---

### [[20_Research/Papers/大模型/Navigating_the_Emotion_Tree_Hierarchical_Hyperbolic_RAG_for_Multimodal_Emotion_Recognition|Navigating the Emotion Tree: Hierarchical Hyperbolic RAG for Multimodal Emotion Recognition]]

![[assets/2605.18884_figure.png|800]]

- **arXiv**: [2605.18884](https://arxiv.org/abs/2605.18884)
- **PDF**: https://arxiv.org/pdf/2605.18884
- **详细分析**: [[20_Research/Papers/大模型/Navigating_the_Emotion_Tree_Hierarchical_Hyperbolic_RAG_for_Multimodal_Emotion_Recognition|Navigating the Emotion Tree: Hierarchical Hyperbolic RAG for Multimodal Emotion Recognition]]
- **作者**: Zeheng Wang, Bo Zhao, Yijie Zhu, Zhishu Liu, Hui Ma, Ruixin Zhang, Shouhong Ding, Qianyu Xie, Zitong Yu
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

多模态情感识别需要联合文本、音频和视频来判断人的情绪状态，常用于教育、心理咨询和人机交互等场景。现有多模态大模型虽然具备较强的跨模态推理能力，但往往把情绪类别当作彼此独立的平面标签，忽略了人类心理学中天然存在的层级情绪体系。与此同时，缺少外部上下文知识时，模型容易过度解读噪声线索，导致细粒度情绪分类不稳定。因此，这篇工作值得关注之处在于：它把“层级情绪树”和“检索增强生成”结合起来，试图让大模型在更结构化的情绪知识上进行判断。

#### 方法概述和架构

论文提出 HyperEmo-RAG，一个面向多模态情感识别的检索增强生成框架。方法首先构建层级化的 Emotion Tree，并将情绪标签节点与多模态样本一起映射到 Poincaré ball 超曲空间中，用超曲几何来表达情绪类别的树状层级关系。对于输入样本，模型分别从音频、视觉和文本三路提取特征，再投影到同一超曲空间，融合成样本级查询向量。随后，模型在情绪树上执行从粗到细的分层 beam search 式检索，逐级筛选与当前样本路径一致的证据，构造 Deliberation Evidence Graph。最后，模型通过 Tree-Aware Attention 和 EmotionGraphFormer 将图结构证据压缩成图 token，与任务提示一起送入冻结的大语言模型完成分类；训练时还加入树距离感知的对比损失和路径一致性损失，以增强超曲空间中的层级对齐与检索路径约束。

#### 实验结果分析

论文在多个数据集上进行了实验，结果显示 HyperEmo-RAG 明显优于现有方法。对比实验表明，该方法相比传统 RAG 的单轮检索-生成范式更适合细粒度情绪识别，层级检索与结构化证据注入都带来了收益。消融实验和敏感性分析进一步验证了各模块的有效性，但节选文本未给出具体数值。

<details>
<summary>完整摘要</summary>

多模态情感识别旨在融合文本、音频和视频等来源，以理解人的情感状态。尽管多模态大语言模型在多模态推理方面表现出色，但它们通常把情绪类别视为彼此独立的标签，忽视了人类心理学中丰富的层级化分类体系。此外，缺乏外部上下文知识使其非常容易过度解读噪声线索，从而进一步增加细粒度情绪分类的难度。为了解决这些问题，我们提出 HyperEmo-RAG，一个利用结构化情感知识库的检索增强生成框架。该框架包含两项关键创新。1）层级超曲空间锚定。我们认识到情绪分类本身具有固有的树状层级结构，因此将层级情绪标签和多模态样本共同嵌入到连续的超曲空间（Poincaré ball）中，并设计了层级 beam-search 推理过程，按由粗到细的层级逐步检索样本。2）结构化证据注入。基于检索到的证据，我们构建证据图，并通过 Tree-Aware Attention 机制和 EmotionGraphFormer，将这种结构化知识作为显式认知上下文注入大语言模型，尽可能保持图结构信息的完整性。多组数据集上的实验表明，HyperEmo-RAG 显著优于现有方法。

</details>

---
