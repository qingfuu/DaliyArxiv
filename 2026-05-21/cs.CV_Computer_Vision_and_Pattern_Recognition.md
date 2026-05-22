# cs.CV | Computer Vision and Pattern Recognition | 2026-05-21

#arxiv #ComputerScience

**论文数**: 14

### [[20_Research/Papers/世界模型/Latent_Dynamics_for_Full_Body_Avatar_Animation|Latent Dynamics for Full Body Avatar Animation]]

![[assets/2605.21478_figure.png|800]]

- **arXiv**: [2605.21478](https://arxiv.org/abs/2605.21478)
- **PDF**: https://arxiv.org/pdf/2605.21478
- **详细分析**: [[20_Research/Papers/世界模型/Latent_Dynamics_for_Full_Body_Avatar_Animation|Latent Dynamics for Full Body Avatar Animation]]
- **作者**: Shichong Peng, Chengxiang Yin, Fei Jiang, Zhongshi Jiang, Lingchen Yang, Qingyang Tan, Amin Jourabloo, Jason Saragih, Ke Li, Christian Häne
- **cs 子类**: cs.CV, cs.GR
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

这篇论文聚焦于“姿态驱动的全身数字人动画”，目标是在给定人体姿态后，从新视角高质量渲染包含松散衣物的全身头像。现有方法虽然能较好地恢复静态或弱动态的人体外观，但面对衣物褶皱、摆动、惯性和接触等由历史状态决定的变化时，仅靠当前姿态往往无法唯一确定衣物形态，容易出现模糊、时序抖动和细节缺失。作者指出，显式物理仿真和分层服装建模虽然能处理这类动态，但通常依赖专门的服装模板或测试时仿真器，难以直接适配原始多视角捕获数据且推理开销较高。

#### 方法概述和架构

作者在一个基于姿态条件的 3D Gaussian Avatar 上，加入了一个 transformer 解码器和一个“残差潜变量”来表示超出驱动信号之外的时变几何与外观变化。训练时，残差潜变量从前视捕获图像中提取；推理时则由一个潜在动力学模型根据短期姿态历史和上一时刻潜变量，自回归地更新该潜变量。该动力学模型将每一步更新分解为驱动力、恢复力和耗散力三部分，从而显式刻画衣物在姿态驱动下的演化过程。整体上，用户在测试阶段只需输入身体和面部关键点等驱动信号，模型即可输出时序一致的全身头像动画。作者还强调，这种参数化方式可以通过不同初始条件生成多样但合理的运动轨迹，并能暴露出如“刚度”等可控因素。

#### 实验结果分析

论文在 9 段真实捕获序列上进行了评估，场景涵盖日常动作与多种松散服装。与近期数据驱动基线相比，该方法在定量指标和感知用户研究中都表现更好，说明其在动画质量与时序一致性上具有优势。作者还展示了力分解带来的可控性，以及不同初始条件下的多样化运动轨迹；节选中未给出具体数值。

<details>
<summary>完整摘要</summary>

基于姿态驱动的全身头像、并建立在神经渲染之上的方法，能够为被捕获的对象生成高质量的新视角图像。然而，松散衣物及其他动态元素的形变方式并不能仅由姿态解释：同一姿态可能对应多种不同状态，因为它们的运动取决于历史、惯性和接触。显式仿真和分层服装方法能够建模这类动态，但它们要么需要专门的服装模板，而原始多视角捕获数据并不天然提供这一点；要么需要在测试时运行物理仿真器，从而带来不小的运行成本。另一条研究路线学习数据驱动的服装头像，避免显式服装分层。这类方法会引入一个辅助潜变量来表示除姿态之外的变化；在推理时，它们通常将该潜变量固定、由姿态回归，或从训练数据中检索，而没有显式建模该潜变量如何在自身动力学作用下演化。此外，即使是在带有松散衣物的日常动作中，现有架构也常常难以捕捉细粒度细节，导致渲染结果模糊并产生时序伪影。为此，我们在一个姿态条件化的 3D Gaussian Avatar 上加入了基于 transformer 的解码器，以及一个用于捕捉驱动信号之外时间变化的动力学残差潜变量。该解码器有两个输入：用户提供的驱动信号，以及残差潜变量，后者捕捉超出驱动信号之外的时序外观与几何变化。在推理时，一个学习得到的潜在动力学模型会根据短时姿态历史和前一时刻的潜变量状态来演化该残差潜变量。该模型将每次更新分解为驱动力、恢复力和耗散力，从而生成时间一致、依赖历史的展开结果，且额外开销极小。不同的初始条件会产生多样但合理的运动轨迹，而力分解还提供了诸如刚度之类的控制能力。在九段包含多种松散服装的真实日常动作序列上，定量指标和感知用户研究都表明，该方法相较于近期数据驱动基线在动画质量上更优。

</details>

---

### [[20_Research/Papers/具身智能/PointACT_Vision-Language-Action_Models_with_Multi-Scale_Point-Action_Interaction|PointACT: Vision-Language-Action Models with Multi-Scale Point-Action Interaction]]

![[assets/2605.21414_figure.png|800]]

- **arXiv**: [2605.21414](https://arxiv.org/abs/2605.21414)
- **PDF**: https://arxiv.org/pdf/2605.21414
- **详细分析**: [[20_Research/Papers/具身智能/PointACT_Vision-Language-Action_Models_with_Multi-Scale_Point-Action_Interaction|PointACT: Vision-Language-Action Models with Multi-Scale Point-Action Interaction]]
- **作者**: Shizhe Chen, Paul Pacaud, Cordelia Schmid
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

视觉-语言-动作（VLA）模型正在成为通用机器人操作的重要路线，能够把自然语言指令映射为具体控制动作，用于抓取、摆放和长程操作等具身任务。然而，现有大多数 VLA 仍主要依赖 2D 图像表示，对精细几何关系和空间定位的建模不足，而这恰恰是三维环境中精准、稳定操控所必需的能力。本文关注的核心问题是：如何把显式 3D 几何信息更紧密地融入 VLA，从而避免仅靠 2D 语义特征带来的空间理解瓶颈，因此具有较强的机器人落地价值。

#### 方法概述和架构

作者提出 PointACT，一种双系统、3D 感知的 VLA 策略，把层级化的 3D 点云表示直接引入动作解码过程。方法整体由冻结的预训练视觉-语言骨干和一个负责动作预测的点云-动作专家组成：图像、语言和机器人本体状态先经各自编码，点云则通过基于 Point Transformer v3 的点云编码器获得多尺度几何特征。与仅把点云作为高层辅助特征的做法不同，PointACT 设计了 multi-scale point-action interaction 机制，让逐步演化的动作 token 在解码时通过高效的 bottleneck window self-attention，同步关注局部几何细节与全局场景结构。训练时，动作专家在点云与视觉-语言特征的条件下学习预测未来动作序列；推理时，冻结的 VLM 负责语义理解，点云-动作专家负责基于 3D 几何生成控制动作。

#### 实验结果分析

作者在 LIBERO 和 RLBench 基准上系统评估了 PointACT，并与单体式和双系统 VLA 基线进行比较，还纳入了加入点云输入的变体。实验表明，PointACT 在两个基准上都取得了稳定提升，其中在具有挑战性的 RLBench-10Tasks 上，相比当前最强的预训练 VLA 成功率提升了 10%。当视觉-语言骨干冻结、动作专家从头训练时，收益还会更大，说明细粒度的 3D 几何与预训练 2D 语义表示的紧密耦合对稳健控制尤为关键。消融结果进一步显示，把点云直接注入 VLM 主干并不如放入动作专家有效，而多尺度点-动作交互和预训练点云编码器都对性能有明显贡献。

<details>
<summary>完整摘要</summary>

视觉-语言-动作（VLA）模型通过利用大型预训练视觉-语言骨干，在通用机器人操作任务上展现出很强潜力。然而，现有大多数 VLA 主要依赖 2D 视觉表示，这限制了它们对精细几何和空间定位的推理能力，而这些能力对于 3D 环境中的精确且鲁棒的操作至关重要。本文提出 PointACT，这是一种双系统的 3D 感知 VLA 策略，它将层级化的 3D 点云表示直接融入动作解码过程。PointACT 采用多尺度点-动作交互机制，并结合高效的瓶颈窗口自注意力，使不断演化的动作 token 能够密集关注局部几何细节和全局场景结构。我们在 LIBERO 和 RLBench 基准上对 PointACT 进行了评估，并系统地将其与单体式和双系统 VLA 基线进行比较，包括加入点云输入的变体。PointACT 在两个基准上都取得了稳定提升，在具有挑战性的 RLBench-10Tasks 套件上，相比当前最先进的预训练 VLA，成功率提升了 10%；当视觉-语言骨干被冻结、动作专家从头训练时，提升幅度更大。大量消融实验表明，将层级化 3D 几何与预训练 2D 语义表示紧密耦合，对于实现稳健且具有空间定位能力的机器人控制至关重要。我们的结果也进一步表明，预训练的 3D 表示在 3D 感知 VLA 策略中具有很大潜力。

</details>

---

### [[20_Research/Papers/强化学习/Distill_to_Think,_Foresee_to_Act_Cognitive-Physical_Reinforcement_Learning_for_Autonomous_Driving|Distill to Think, Foresee to Act: Cognitive-Physical Reinforcement Learning for Autonomous Driving]]

![[assets/2605.21139_figure.png|800]]

- **arXiv**: [2605.21139](https://arxiv.org/abs/2605.21139)
- **PDF**: https://arxiv.org/pdf/2605.21139
- **详细分析**: [[20_Research/Papers/强化学习/Distill_to_Think,_Foresee_to_Act_Cognitive-Physical_Reinforcement_Learning_for_Autonomous_Driving|Distill to Think, Foresee to Act: Cognitive-Physical Reinforcement Learning for Autonomous Driving]]
- **作者**: Yang Wu, Qiang Meng, Zhaojiang Liu, Youquan Liu, Jian Yang, Jin Xie
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 0.96，世界模型 0.36）
- **关联关键词**: Multimodal, RL, WorldModel

#### 研究背景与动机

端到端自动驾驶模型通常受限于模仿学习的“行为克隆天花板”，只能学习专家轨迹，难以在开放场景中主动发现更优策略，也容易在分布外场景下变得脆弱。作者指出，强化学习虽然有望突破这一限制，但要真正用于自动驾驶，还缺少两类关键基础：一是能理解交通语义与驾驶意图的“认知”能力，二是能预判候选动作后果的“物理”前瞻能力。当前许多方法要么只做语义推理、忽略真实道路约束，要么只预测隐空间而缺少可解释的安全评估，因此这项工作值得关注，因为它尝试把语义理解、未来想象和强化学习统一到同一套自动驾驶框架中。

#### 方法概述和架构

论文提出 CoPhy（Cognitive-Physical reinforcement learning framework），核心由三部分组成：认知先验蒸馏、物理世界模型滚动预测、以及认知-物理联合策略优化。首先，模型将多模态传感器输入（RGB、LiDAR）编码为 BEV 状态，并通过离线训练的 VLM 生成交通标志、道路结构、驾驶意图等认知文本，再用文本编码结果去蒸馏 BEV 表征，使认知能力被“压缩”进车载主干网络，推理时不再需要在线运行 VLM。其次，作者构建了一个自回归 BEV world model，以当前 BEV、认知特征和候选轨迹为条件，逐步预测未来 BEV 状态，把它作为可解释的“物理沙盒”来评估碰撞、越线等安全风险。最后，在策略优化阶段采用 GRPO，并设计双奖励机制：物理奖励来自 BEV rollout，约束硬安全；认知奖励来自语言对齐评分器，约束意图一致性。推理时，认知通道还可以接收用户语言指令，从而实现可控驾驶。

#### 实验结果分析

实验在 NAVSIM v1 和 v2 上进行，并与现有端到端驾驶、VLM 结合驾驶、以及 world model/强化学习相关方法进行比较。文中报告 CoPhy 在 NAVSIM v1 和 v2 上分别达到 91.4 PDMS 和 86.1 EPDMS，同时在安全相关子指标上表现领先。消融实验表明，认知蒸馏、物理滚动预测和双奖励优化三者缺一不可；此外，模型还展示了通过用户语言指令进行意图控制驾驶的能力。

<details>
<summary>完整摘要</summary>

当前端到端自动驾驶模型本质上受限于模仿学习中的行为克隆天花板。虽然强化学习为更智能的自动驾驶提供了路径，但它需要两项缺失的基础设施：（1）能够理解交通语义和驾驶意图的认知基础，（2）能够预判候选动作后果的前瞻性物理环境。为此，我们提出 CoPhy，一个用于自动驾驶的认知-物理强化学习框架。为了“distill to think”，我们将 VLM 的知识蒸馏到 BEV 编码器中，然后完全舍弃 VLM，在零推理开销下保留认知能力，同时释放认知通道作为可插拔接口，以支持可选的人类语言指令。为了“foresee to act”，我们构建了一个自回归 BEV world model，在候选动作条件下显式预测未来语义地图，作为一个可解释的物理沙盒，并可直接从中推导安全指标。建立在这套双重基础设施之上，我们使用 GRPO 和一种新的双奖励机制来优化驾驶策略：由 BEV rollouts 产生的物理奖励用于施加硬安全约束，而来自语言对齐评分器的认知奖励则用于确保意图一致性。大量实验表明，CoPhy 不仅在 NAVSIM v1 和 v2 基准上取得了最先进结果，还通过具备认知引导的场景遵从能力和由用户定义语言指令实现的灵活意图控制，带来了更安全的驾驶表现。

</details>

---

### [[20_Research/Papers/机器人/LiteViLNet_Lightweight_Vision-LiDAR_Fusion_Network_for_Efficient_Road_Segmentation|LiteViLNet: Lightweight Vision-LiDAR Fusion Network for Efficient Road Segmentation]]

![[assets/2605.21007_figure.png|800]]

- **arXiv**: [2605.21007](https://arxiv.org/abs/2605.21007)
- **PDF**: https://arxiv.org/pdf/2605.21007
- **详细分析**: [[20_Research/Papers/机器人/LiteViLNet_Lightweight_Vision-LiDAR_Fusion_Network_for_Efficient_Road_Segmentation|LiteViLNet: Lightweight Vision-LiDAR Fusion Network for Efficient Road Segmentation]]
- **作者**: Daojie Peng, Bingtao Wang, Fulong Ma, Liang Zhang, Jun Ma
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

道路分割是自动驾驶和智能机器人中的基础感知任务，直接影响轨迹规划、避障和导航。现有多模态方法往往依赖较重的Transformer编码器来融合RGB与LiDAR信息，虽然精度高，但参数量和计算开销过大，难以在资源受限的边缘设备上实时部署。本文值得关注之处在于，它面向“高精度+高帧率”的实际落地需求，尝试在保持多模态优势的同时显著降低推理成本。

#### 方法概述和架构

论文提出LiteViLNet，一种轻量级视觉-LiDAR融合网络，用于高效道路分割。输入端使用RGB图像与由LiDAR点云生成的ADI（Altitude Difference Image）作为双模态输入，其中ADI将三维点云投影到二维平面，并编码局部高度差作为几何线索。网络主体采用双流轻量编码器：RGB分支使用预训练的MobileNetV3-Large，LiDAR分支使用基于深度可分离卷积的微型编码器，以多尺度方式提取两种模态特征。随后在每个尺度上引入MSFM（Multi-Scale Feature Fusion Module），先做通道压缩，再分别用ECA和Coordinate Attention增强两种模态特征，并通过双向跨模态注意力建模互补关系，最后进行自适应门控融合。为进一步捕获长程依赖，作者设计了large-kernel-bridge模块，用大核深度卷积在保持线性复杂度的前提下扩大感受野；解码阶段配合深度监督输出最终分割结果。

#### 实验结果分析

实验在KITTI Road数据集及真实场景部署中进行，比较了多种CNN和Transformer基线。结果显示，LiteViLNet仅有14.04M参数，却取得96.36%的MaxF，位居CNN方法最优，并且性能可与更大的Transformer模型相媲美。推理效率方面，模型在RTX 4060 Ti上可达到163.79 FPS，在Jetson Orin NX上为22.18 FPS，体现出较强的边缘部署潜力。正文还提到进行了消融与真实机器人实验，但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

道路分割是自动驾驶和智能机器人系统中的一项基础感知任务，既要求较高的精度，也要求实时推理，尤其是在资源受限的边缘设备上部署时更是如此。现有多模态道路分割方法通常依赖于较重的基于Transformer的编码器来达到最先进的性能，但其巨大的计算开销使其无法在嵌入式平台上实现实时运行。为了解决这一困境，我们提出LiteViLNet，这是一种轻量级多模态网络，融合RGB纹理信息与LiDAR几何信息，以实现高效道路分割。具体而言，我们设计了一个双流轻量编码器和深度可分离卷积，用于以极少的参数从两种模态中提取层次化特征。进一步地，我们提出Multi-Scale Feature Fusion Module（MSFM），以促进不同层级上的跨模态交互；同时设计了large-kernel-bridge模块，以线性复杂度捕获长程依赖关系。在KITTI Road数据集和真实世界应用上的大量实验表明，LiteViLNet在精度与效率之间取得了很好的平衡。尤其值得注意的是，我们的模型仅有14.04M参数，却达到了96.36%的MaxF，位列所有CNN方法中的最佳，并且与更大的Transformer模型相当；在RTX 4060 Ti上的仅模型推理速度达到163.79 FPS，在Jetson Orin NX上为22.18 FPS。该方法在推理速度上优于大量重型方法，同时保持了非常有竞争力的精度，充分验证了LiteViLNet在自动驾驶和智能机器人中进行实时嵌入式部署的潜力。

</details>

---

### [[20_Research/Papers/机器人/Towards_UAV_Detection_in_the_Real_World_A_New_Multispectral_Dataset_UAVNet-MS_and_a_New_Method|Towards UAV Detection in the Real World: A New Multispectral Dataset UAVNet-MS and a New Method]]

![[assets/2605.20963_figure.png|800]]

- **arXiv**: [2605.20963](https://arxiv.org/abs/2605.20963)
- **PDF**: https://arxiv.org/pdf/2605.20963
- **详细分析**: [[20_Research/Papers/机器人/Towards_UAV_Detection_in_the_Real_World_A_New_Multispectral_Dataset_UAVNet-MS_and_a_New_Method|Towards UAV Detection in the Real World: A New Multispectral Dataset UAVNet-MS and a New Method]]
- **作者**: Yihang Luo, Jun Chen, Chao Xiao, Yingqian Wang, Zhaoxu Li, Qiang Ling, Xu He, Nuo Chen, Gaowei Guo, Hongge Li, Miao Li, Longguang Wang...
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

无人机在低空经济、安防巡检和空域管理中的应用快速增长，使得对“小尺寸、细粒度、易混淆”的无人机检测需求变得非常迫切。现有基于RGB或RGB-IR的系统主要依赖空间纹理与轮廓信息，但在无人机目标很小、类别外观相近、鸟类等动态干扰复杂、以及目标与背景对比度很低时，判别能力会明显下降。论文值得关注之处在于：它把问题从“只靠空间信息的检测”推进到“利用物质相关光谱签名的多光谱检测”，试图为真实世界低空无人机监测建立新的数据与方法基准。

#### 方法概述和架构

作者首先构建了 UAVNet-MS，这是一个面向细粒度小无人机检测的多光谱数据集，包含 15,618 个时间同步的 RGB-MSI 数据立方体，采用 1440×1080 高分辨率采集，并标注了四类材质差异明显的无人机及其边界框。基于该数据集，论文提出 MFDNet 作为双分支基线：一条分支处理 RGB 的空间纹理信息，另一条分支处理 MSI 的跨波段光谱相关性，以保留两种模态的互补性。由于阵列式多光谱成像会带来波段间视差，MFDNet 引入共享的 ArrayCode 位置编码模块，将相机阵列几何信息注入两种模态以学习并补偿对齐误差。随后，模型采用细尺度、语义解耦的融合策略，在增强小目标对比度的同时，保留高层 RGB 语义通路以抑制误报。整个网络可端到端训练，并分别支持 RGB-only、MSI-only 和 RGB+MSI 三种评测协议。

#### 实验结果分析

论文在 UAVNet-MS 上与 20 种检测器进行了系统比较，涵盖 RGB-only、MSI-only 和 RGB+MSI 三种设置，验证了多光谱信息对细粒度小无人机识别的补充价值。结果显示，MFDNet 相比最强的 RGB-only 方法在 AP50 上提升了 6.2 个百分点，说明光谱线索能够提供超越空间线索的额外材质证据。作者还做了阵列对齐、光谱分支设计和融合阶段等消融实验，并分析了不同天气、场景和低对比条件下的鲁棒性；可见文本未给出所有消融的具体数值，但整体结论是该方法在复杂真实场景中更稳健。

<details>
<summary>完整摘要</summary>

无人机在低空经济中的快速普及，带来了对高精度、细粒度无人机监测系统的迫切需求。尽管近年来已经取得一定进展，但现有基于RGB成像或RGB与红外（IR）融合的无人机监测系统，主要依赖空间线索，而这些线索在小尺度场景下的判别能力会下降，尤其是在无人机类别间高度相似、目标与动态干扰（例如鸟类）容易混淆，以及目标与背景对比度较低时更为明显。为克服这一局限，本文引入具有物理属性补充信息的方案。多光谱成像（MSI）能够编码与材料相关的光谱签名，但由于缺乏专门的数据集、基线方法和评测基准，基于MSI的细粒度小无人机检测仍然研究不足。为填补这一空白，我们提出 UAVNet-MS，这是首个面向细粒度小无人机检测的多光谱数据集。UAVNet-MS 包含 15,618 个时间同步的 RGB-MSI 数据立方体，具有高空间分辨率（1440×1080），由基于阵列的多光谱成像系统采集，并带有边界框标注和四类材质差异明显的无人机类别。UAVNet-MS 还呈现出极具挑战性的小目标特征：93.7% 的目标面积不超过 32^2 像素，平均目标面积至多为 18^2 像素，仅占图像面积的约 0.02%，且普遍存在低对比度现象，更贴近真实低空无人机监测场景。基于 UAVNet-MS 数据集，我们提出多光谱融合检测器 MFDNet，这是一个双分支基线，旨在解决阵列式成像带来的波段间视差问题，并完成面向细粒度无人机检测的空间—光谱融合。具体而言，MFDNet 设计了共享的、感知阵列几何的位置信息编码模块 ArrayCode，将相机阵列结构信息注入两种模态，使网络能够学习并补偿阵列式采集固有的跨波段错位；同时采用模态专属的骨干网络，分别编码 RGB 的空间纹理与 MSI 的波段间光谱相关性。此外，MFDNet 还使用一种面向尺度的语义解耦融合策略，选择性注入细尺度的光谱线索以增强小目标对比度，同时保持稳定的高层 RGB 语义通路以提升误报抑制能力。通过将这些组件统一到一个端到端可训练框架中，MFDNet 为 UAVNet-MS 提供了强基线，使得基于阵列式多光谱感知的可靠细粒度无人机检测成为可能。为保证公平评测，本文定义了三种协议（RGB-only、MSI-only、RGB+MSI），并进行了大规模实验，包括与 20 种代表性检测器的对比，以验证该基线并量化多光谱线索对细粒度小无人机检测的增益。我们的贡献可概括为三点：（1）建立了一个面向细粒度小无人机多光谱检测的专用基准设置。为此，我们提出 UAVNet-MS，这是首个面向该任务的材料感知多光谱数据集，提供了时间同步、分辨率一致的 RGB-MSI 数据，覆盖四类材质差异明显的无人机，并处于真实的低对比度条件下，从而支持对小无人机光谱线索的分析。（2）提出 MFDNet，这是一种双流检测器，通过 ArrayCode 补偿阵列式采集带来的跨波段视差，并通过语义解耦融合有效整合材料线索，为 RGB-MSI 小目标检测建立了可靠基线。（3）基于 UAVNet-MS，在标准化协议下进行了大量实验与消融分析，量化了多光谱信息的经验收益，并提供了基线与洞见，以推动未来基于 MSI 的无人机监测研究。

</details>

---

### [[20_Research/Papers/大模型/FruitEnsemble_MLLM-Guided_Arbitration_for_Heterogeneous_ensemble_in_Fine-Grained_Fruit_Recognition|FruitEnsemble: MLLM-Guided Arbitration for Heterogeneous ensemble in Fine-Grained Fruit Recognition]]

![[assets/2605.20892_figure.png|800]]

- **arXiv**: [2605.20892](https://arxiv.org/abs/2605.20892)
- **PDF**: https://arxiv.org/pdf/2605.20892
- **详细分析**: [[20_Research/Papers/大模型/FruitEnsemble_MLLM-Guided_Arbitration_for_Heterogeneous_ensemble_in_Fine-Grained_Fruit_Recognition|FruitEnsemble: MLLM-Guided Arbitration for Heterogeneous ensemble in Fine-Grained Fruit Recognition]]
- **作者**: Enhui Yu, Junhui Li, Ruitong Lu, Jialu Li, Youshan Zhang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

细粒度水果分类是农业视觉中的关键任务，直接影响自动分拣、品质检测、价格评估和采后存储管理等应用。但这一任务面临两个核心瓶颈：一是高质量、大规模细粒度水果数据集稀缺，二是不同水果品类之间外观高度相似，类别边界非常模糊。论文关注的价值在于，它试图同时解决“识别精度”和“部署效率”之间的矛盾，面向真实农业产线场景给出可落地方案。

#### 方法概述和架构

作者首先构建了 Fruit-306 数据集，包含306个水果类别和116,233张图像，并为每个类别配套人工整理的形态学文本描述，用于支持多模态推理。方法 FruitEnsemble 采用两阶段动态推理：第一阶段将 DenseNet201、EfficientNetB7、Vision Transformer 和 ResNet50 组成异构加权集成，通过验证集校准后的权重融合输出预测结果及置信度，并形成 Top-3 候选集合。第二阶段设置置信度门控路由机制，当集成置信度低于0.6时，触发多模态大语言模型 Qwen-VL-Plus，对候选类别与水果描述进行结合推理与视觉核验。训练时还引入面向难样本的联合优化策略，只对路由识别出的难例施加特定的多样性损失，以增强不同骨干网络的互补性。整体上，该框架让简单样本走高效视觉分支，疑难样本才进入更昂贵但更强的语言推理分支。

#### 实验结果分析

实验在 Fruit-306 的固定划分上进行，并与现有单模型和静态集成基线比较，评价指标为分类准确率等。结果显示，FruitEnsemble 达到 70.49% 的分类准确率，优于现有最先进方法。作者还报告该方法可在 19.8 ms 的实时延迟下运行，并且仅约15%的样本会调用大模型，说明其兼顾了精度与效率。节选文本还提到消融实验支持动态路由、Top-K 约束和难样本优化的有效性，但可见文本未给出所有消融的具体数值。

<details>
<summary>完整摘要</summary>

细粒度水果分类是农业计算机视觉中的一项关键但极具挑战性的任务，其主要障碍在于高质量数据集严重匮乏，以及不同类别之间的视觉相似度极高。为应对这些问题，我们首先构建了一个综合性数据集，包含306个水果类别、116,233个样本。进一步地，我们提出 FruitEnsemble，这是一个实用的两阶段动态推理框架，旨在克服静态单模型架构在泛化能力上的局限。第一阶段中，FruitEnsemble 采用经过验证集校准的异构骨干网络加权集成，生成一个稳健的 Top-3 候选集合。为处理困难样本，我们引入专家仲裁机制：当集成置信度低于0.6时，系统会触发多模态大语言模型（MLLM），结合外部植物学描述并使用 Chain-of-Thought（CoT）推理进行严格的视觉核验。此外，我们还通过一种面向难样本感知的联合损失优化训练流程。大量实验表明，FruitEnsemble 实现了70.49%的分类准确率，并优于现有最先进模型。我们的框架为真实农业视觉分拣和质量检测任务提供了一种高效、面向部署的解决方案。

</details>

---

### [[20_Research/Papers/大模型/ProCrit_Self-Elicited_Multi-Perspective_Reasoning_with_Critic-Guided_Revision_for_Multimodal_Sarcasm_Detection|ProCrit: Self-Elicited Multi-Perspective Reasoning with Critic-Guided Revision for Multimodal Sarcasm Detection]]

![[assets/2605.20867_figure.png|800]]

- **arXiv**: [2605.20867](https://arxiv.org/abs/2605.20867)
- **PDF**: https://arxiv.org/pdf/2605.20867
- **详细分析**: [[20_Research/Papers/大模型/ProCrit_Self-Elicited_Multi-Perspective_Reasoning_with_Critic-Guided_Revision_for_Multimodal_Sarcasm_Detection|ProCrit: Self-Elicited Multi-Perspective Reasoning with Critic-Guided Revision for Multimodal Sarcasm Detection]]
- **作者**: Yingjia Xu, Jiulong Wu, Bowen Zhang, Baokui Guo, Siyuan Chai, Min Cao
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.9（加权：大模型 0.7，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

多模态讽刺检测要判断图文组合是否表达了与字面相反的讽刺意图，实际难点在于需要同时识别图像与文本之间的跨模态不一致之处。不同样本的讽刺机制差异很大，有的依赖夸张表达，有的依赖文化隐喻，有的则依赖场景常识冲突，因此推理时需要的分析视角并不固定。现有方法虽然开始显式建模推理过程，但往往预设一组固定视角，并用手工路由规则让各视角独立工作，难以适应样本级差异。这篇工作值得关注之处在于，它尝试让模型自主生成所需视角，并通过批判-修订机制提升推理可靠性。

#### 方法概述和架构

论文提出 ProCrit，一个面向多模态讽刺检测的 Proposal-Critic 双智能体框架。第一步是通过动态角色 rollout 合成“过程级”推理标注：一个强视觉语言模型在共享上下文中依次生成不同分析角色，每个角色输出分析视角、证据分析和是否足够继续推理的判断，最终把多轮轨迹压平成单序列，用来训练学生模型学习样本自适应的多视角推理。第二步采用 draft–critique–revise 流程：proposal agent 先根据图文输入生成初稿推理与讽刺预测，critic agent 再独立评估初稿，输出指出具体缺陷的自然语言反馈和质量分数，proposal agent 最后依据反馈从头修订推理并给出最终结果。第三步是 mutual-refinement 训练：在优化 proposal agent 时，把 critic 的评分与反馈作为强化学习信号；同时根据 proposal 的修订效果反过来更新 critic，使其反馈质量与实际可修正性对齐。整体上，该方法把“生成视角—外部批判—定向修订”串成闭环，并用双阶段强化学习联合优化推理生成与反馈能力。

#### 实验结果分析

作者在三个广泛使用的基准上验证了 ProCrit 的有效性，并与现有方法进行了比较。实验表明，该方法在多模态讽刺检测任务上取得了更好的表现，说明自发式多视角推理结合 critic 引导修订确实有助于提升识别能力。正文节选中未给出具体数值，但可见还进行了消融实验和额外分析，包括多轮修订、训练成本、推理成本与生成长度等维度，说明作者也关注了方法的效率与稳定性。

<details>
<summary>完整摘要</summary>

多模态讽刺检测需要对图像与文本之间的跨模态不一致进行推理，以判断字面表达与真实意图之间的差异，但由于讽刺机制多样，所需的具体分析视角会因样本而异。尽管近期方法已将这一分析过程显式化，它们仍然依赖固定、预定义的视角，并在手工设计的路由规则下彼此独立运行。我们认为，多模态讽刺检测更需要一种自发式多视角推理，即模型能够针对每个样本自主生成所需视角，并逐步将这些视角整合为连贯分析。为实现这一目标，我们提出 ProCrit，这是一个 Proposal-Critic 双智能体框架：proposal agent 负责多视角推理，critic agent 负责外部评估与定向修订指导。首先，为了克服现有讽刺数据集中缺乏过程级监督的问题，ProCrit 通过动态角色 agentic rollout 合成过程级推理标注：一个强视觉语言模型在共享上下文中按顺序生成分析角色，随后将多角色轨迹压平成序列，在保留跨视角依赖的同时支持高效自回归生成。其次，为了提升推理可靠性，ProCrit 采用 draft-critique-revise 范式：独立的 critic 识别推理中的缺陷并提供有针对性的自然语言反馈，用于定向修订。最后，我们设计了 mutual-refinement 训练框架，通过双阶段强化学习联合优化 proposal 的初稿生成与反馈引导修订，并根据 critic 的反馈实际修订效果反向优化 critic agent。三个广泛使用的基准实验表明，ProCrit 具有有效性。

</details>

---

### [[20_Research/Papers/机器人/VSCD_Video-based_Scene_Change_Detection_in_Unaligned_Scenes|VSCD: Video-based Scene Change Detection in Unaligned Scenes]]

![[assets/2605.20821_figure.png|800]]

- **arXiv**: [2605.20821](https://arxiv.org/abs/2605.20821)
- **PDF**: https://arxiv.org/pdf/2605.20821
- **详细分析**: [[20_Research/Papers/机器人/VSCD_Video-based_Scene_Change_Detection_in_Unaligned_Scenes|VSCD: Video-based Scene Change Detection in Unaligned Scenes]]
- **作者**: Jiae Yoon, Ue-Hwan Kim
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

长时序自主机器人在室内环境中运行时，必须持续判断“环境里发生了什么变化”，例如物体出现、消失或被移动。现有变化检测多假设视角基本固定、两段视频已对齐，或者只包含少量变化目标，因此难以应对真实场景中的自由相机运动、强视角错位和大量同时变化。本文关注的 VSCD 正是面向“未对齐场景中的视频级场景变化检测”，对具身智能中的长期巡检、环境理解和持续学习都很有现实意义。

#### 方法概述和架构

作者将任务定义为：给定同一室内空间在不同时刻拍摄的参考视频与查询视频，输出每个查询帧的像素级变化掩码。方法名为 VSCDNet，整体采用三阶段流程：首先做帧级对齐，从参考视频中筛选与当前查询帧最可能相关的候选参考片段；接着在候选帧上建立局部patch对应关系，通过可微 warping 将参考特征对齐到查询视角，并提取每个候选对应的低分辨率变化特征；最后利用帧级置信度与patch级置信度进行自适应融合，再由查询引导的解码器一次性输出高分辨率变化掩码。模型训练只依赖变化掩码监督，不需要显式位姿、时间同步或帧间配准标注，从而让时序匹配能力在监督中隐式学习出来。

#### 实验结果分析

作者构建了一个大规模 VSCD 基准，包含超过 110 万帧的像素级变化标注，并额外提供真实世界测试集以评估仿真到现实的泛化。实验中将方法与强大的图像级、视频级变化检测基线进行比较，结果表明该方法取得了当前最优表现；正文节选未给出具体数值。论文还包含消融实验与对齐质量分析，用于验证帧级对齐、patch对应和置信度融合各模块的贡献。进一步地，作者将方法部署到移动机器人上，在视觉监控和目标增量学习两个下游任务中验证了其实用性。

<details>
<summary>完整摘要</summary>

检测环境中发生了什么变化，是实现长期自主的重要能力，但大多数变化检测设定都假定视角固定、仅有轻微错位，或者只存在少量变化物体。我们提出视频场景变化检测 VSCD（Video-based Scene Change Detection），它以同一室内空间在不同时刻、在不受约束的相机运动下拍摄得到的一段参考 RGB 视频和一段查询 RGB 视频为输入，为每个查询帧预测像素级变化掩码。两段视频在时间上并不同步，并且可能有许多物体实例出现或消失。为了研究这一设定，我们构建了一个大规模基准，包含超过 110 万帧、带有像素级精确变化掩码的数据，同时还提供了一个真实世界测试集，用于评估超出仿真环境的迁移能力。我们提出了一种以查询为中心的多参考模型：它借助变化掩码监督隐式学习时序匹配，通过局部patch对应将候选参考特征对齐到查询视角，并在逐候选变化特征基础上结合帧级与patch级置信度进行融合，最后一次性解码出高分辨率掩码。我们的方法在与强图像级和视频级基线的比较中取得了最先进的性能，并且我们将其部署到移动机器人上，验证了其在两个下游应用——视觉监控和目标增量学习——中的现实价值。

</details>

---

### [[20_Research/Papers/大模型/OSGNet_with_MLLM_Reranking_@_Ego4D_Episodic_Memory_Challenge_2026|OSGNet with MLLM Reranking @ Ego4D Episodic Memory Challenge 2026]]

![[assets/2605.20818_figure.png|800]]

- **arXiv**: [2605.20818](https://arxiv.org/abs/2605.20818)
- **PDF**: https://arxiv.org/pdf/2605.20818
- **详细分析**: [[20_Research/Papers/大模型/OSGNet_with_MLLM_Reranking_@_Ego4D_Episodic_Memory_Challenge_2026|OSGNet with MLLM Reranking @ Ego4D Episodic Memory Challenge 2026]]
- **作者**: Yisen Feng, Leigang Qu, Haoyu Zhang, Qiaohui Chu, Meng Liu, Xuemeng Song, Weili Guan, Liqiang Nie
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

这篇工作聚焦 Ego4D Episodic Memory Challenge 中的两个视频时刻定位任务：Natural Language Queries 和 GoalStep，目标是在长时间、未裁剪的第一视角视频中精确找出与文本查询对应的时间片段。这类能力直接关系到智能眼镜助手、具身智能记忆检索等应用，但传统时刻定位方法在复杂查询、长视频和细粒度语义区分上往往泛化不足。另一方面，MLLM 虽然具备更强的视频-语言推理能力，但受上下文长度限制，难以直接高效处理整段长视频。因此，如何结合传统定位模型的候选召回能力与 MLLM 的语义判断能力，是这篇论文的核心关注点。

#### 方法概述和架构

论文提出的是一个基于重排序（reranking）的两阶段框架，名称可概括为“OSGNet with MLLM Reranking”。第一阶段先使用现有的时刻定位模型 OSGNet 为每个文本查询检索 top-5 候选时间段，以保证候选召回和效率。第二阶段再调用 GPT-5.4 对候选段进行重排序：在 NLQ 任务中，先将每个候选片段切分为 20 秒小段，并按 1 FPS 抽帧生成文本叙述，累积成该候选的“episodic memory”，再让 GPT-5.4 基于这些候选记忆和原始问题选择最匹配的片段。由于 GPT-5.4 的视觉输入存在图像数量限制，作者将重排序拆成“局部叙述生成 + 全局推理选择”两步，以便在较小输入成本下完成更细致的语义比较。对于 GoalStep 任务，作者复用同样的候选重排序流程，并额外利用步骤序列的先验约束，在后处理阶段鼓励相邻步骤的起始时间单调递增，通过最小化候选排名代价与时间违约惩罚的总和来联合选择整段流程中的候选。整体上，该方法把传统模型的高召回与 MLLM 的强推理能力串联起来，用 MLLM 专注区分 hard negative，而不是直接处理整段长视频。

#### 实验结果分析

实验在 Ego4D Episodic Memory Challenge 的 NLQ 和 GoalStep 测试集上进行，基线为 OSGNet，评价指标包括 R@1、R@5 以及不同 IoU 阈值下的表现。结果显示，在 NLQ 上，加入重排序后 R@1@0.3 从 21.63% 小幅提升到 21.78%，但整体增益有限；作者也指出这可能与 false negative 和评测协议有关。GoalStep 上，重排序带来更稳定的提升，R@1@0.3 从 55.31% 提升到 55.39%，R@1@0.5 从 47.82% 提升到 47.91%。进一步结合基于顺序先验的后处理后，作者最终在官方榜单上拿到两个赛道第一。

<details>
<summary>完整摘要</summary>

我们在此报告中介绍了我们在 CVPR 2026 的 Ego4D Episodic Memory Challenge 中，针对 Natural Language Queries 和 GoalStep 两个赛道的冠军方案。两个赛道都要求在长时间、未裁剪的第一视角视频中准确定位时间片段。为解决这些任务，我们提出了一种基于重排序的框架：它在保留传统定位流水线高效率与高候选召回的同时，充分利用了多模态大语言模型（MLLM）强大的视频-语言推理能力。具体而言，我们首先从现有定位模型 OSGNet 中获得一组候选片段，然后使用 MLLM 选择与给定查询最匹配的片段，从而细化最终预测。最终，我们的方法在 Natural Language Queries 和 GoalStep 两个赛道上均获得第一名。我们的代码可见于：https://github.com/iLearn-Lab/CVPR25-OSGNet 。

</details>

---

### [[20_Research/Papers/大模型/LER-YOLO_Reliability-Aware_Expert_Routing_for_Misaligned_RGB-Infrared_UAV_Detection|LER-YOLO: Reliability-Aware Expert Routing for Misaligned RGB-Infrared UAV Detection]]

![[assets/2605.20667_figure.png|800]]

- **arXiv**: [2605.20667](https://arxiv.org/abs/2605.20667)
- **PDF**: https://arxiv.org/pdf/2605.20667
- **详细分析**: [[20_Research/Papers/大模型/LER-YOLO_Reliability-Aware_Expert_Routing_for_Misaligned_RGB-Infrared_UAV_Detection|LER-YOLO: Reliability-Aware Expert Routing for Misaligned RGB-Infrared UAV Detection]]
- **作者**: Liming Hou, Yueping Peng, Hexiang Hao, Ji Wang, Xuekai Zhang, Wei Tang, Zecong Ye, Xin Ying, Yubo He
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

该文关注的是在RGB-红外成对遥感图像中检测小型无人机（UAV）的任务，这类问题常见于低空监视、交通监管、灾害救援和公共安全等场景。难点在于目标尺寸极小、背景杂乱，而且双传感器之间往往存在空间错位，导致可见光与红外特征难以一一对应。现有双模态检测方法通常只做对齐或融合，却很少评估局部对应关系是否可信，因此错位带来的伪匹配会继续传递到检测头中。因而，这篇工作值得关注的原因在于：它不是单纯增强融合能力，而是把“对齐是否可靠”显式纳入融合决策。

#### 方法概述和架构

论文提出 LER-YOLO（Local Reliability Expert Routing YOLO），核心思想是用局部对齐可靠性作为后续跨模态交互的路由先验。首先，Uncertainty-Aware Target Alignment（U-TA）模块以红外图像为参考，将可见光特征重采样到红外坐标系，同时预测一个空间可靠性图，用于标记哪些位置的对齐结果可信、哪些位置可能存在错位或遮挡。随后，Reliability-Guided Sparse MoE Fusion 模块接收对齐后的可见光特征、红外特征和可靠性图，在每个空间位置上从三个专家中稀疏选择 top-k 个进行计算：RGB主导专家、红外主导专家和交互融合专家。这样，可信区域会更多利用跨模态信息，不可信区域则倾向保留单模态证据，从而抑制错误融合。整体上，方法沿用 YOLOv5s 家族检测框架，主干与检测头保持轻量化，仅在对齐后引入可靠性驱动的专家路由机制。

#### 实验结果分析

作者在公开的 MBU 基准上评估了该方法，并采用 YOLOv5s 家族协议进行实验。结果显示，LER-YOLO 在三次独立随机种子下达到 89.7±0.2% 的 AP50，最好结果为 89.9%。文中还做了大量消融、参数量匹配对比、合成位移鲁棒性测试与复杂度分析，结论表明性能提升主要来自可靠性引导的专家路由，而不是简单增加模型容量。

<details>
<summary>完整摘要</summary>

在RGB-红外遥感图像对中检测小型无人机仍然具有挑战性，原因包括目标尺度极小、背景杂乱，以及异构传感器之间存在空间错位。现有的双模态检测器往往直接对特征进行对齐或融合，却没有评估局部跨传感器对应关系的可靠性，从而使错配伪影传播到检测头中。为了解决这一问题，我们提出 LER-YOLO，这是一种面向错位RGB-红外无人机检测的、具备可靠性感知的稀疏 Mixture of Experts 框架。LER-YOLO 首先引入 Uncertainty-Aware Target Alignment 模块，将可见光特征重采样到红外参考坐标系，并估计一个空间可靠性图。随后，这一可靠性先验被用于 Reliability-Guided Sparse MoE Fusion 模块中，模块会自适应地从 RGB主导、红外主导和交互融合三个专家中选择 k 个专家，从而在抑制不可靠融合的同时，实现可信的跨模态交互。在公开 MBU 基准上、采用 YOLOv5s 家族协议的实验表明，LER-YOLO 在三次独立随机种子下取得了 89.7±0.2% 的 AP50，最好结果达到 89.9%。大量消融实验、参数量匹配对比、合成位移评估以及复杂度分析表明，这些提升主要来自可靠性引导的专家路由，而不是模型容量的增加。

</details>

---

### [[20_Research/Papers/大模型/QwenSafe_Multimodal_Content_Rating_Description_Identification_via_Preference-Aligned_VLMs|QwenSafe: Multimodal Content Rating Description Identification via Preference-Aligned VLMs]]

![[assets/2605.20584_figure.png|800]]

- **arXiv**: [2605.20584](https://arxiv.org/abs/2605.20584)
- **PDF**: https://arxiv.org/pdf/2605.20584
- **详细分析**: [[20_Research/Papers/大模型/QwenSafe_Multimodal_Content_Rating_Description_Identification_via_Preference-Aligned_VLMs|QwenSafe: Multimodal Content Rating Description Identification via Preference-Aligned VLMs]]
- **作者**: Dishanika Denipitiyage, Aruna Seneviratne, Suranga Seneviratne
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

移动应用市场通常要求开发者提交标准化的内容分级描述（CRD），用于告知用户应用是否包含可能敏感或受限的内容。但应用内容天然具有多模态特征，既包含文本介绍，也包含界面截图，因此仅依赖单一模态很难保证分级信息准确、一致。论文指出，开发者自报分级存在被刻意低报或误报的风险，会削弱年龄分级与内容管控机制的有效性，尤其可能让未成年人暴露于不适宜内容中。因此，如何自动、稳健地从应用元数据中识别内容分级描述，具有明显的安全与平台治理价值。

#### 方法概述和架构

论文提出 QwenSafe，一个面向 Apple 内容分级描述识别的多模态视觉语言模型。其核心数据构造模块 metadata2CRD 会把应用描述、截图以及正式的分级定义结合起来，自动生成与具体描述项对齐的问答样本，从而形成可扩展的训练数据。模型以 Qwen3-VL-8B 为基础，先进行监督微调，再通过 DPO 进行偏好对齐，使模型输出不仅判断某个 CRD 是否存在，还能依据文本与视觉线索给出更贴近描述项的解释。整体流程上，输入是应用元数据和截图，输出是 12 个 Apple 定义的 CRD 上的二分类结果及对应证据解释。

#### 实验结果分析

作者在 12 个 Apple 定义的内容分级描述上评估了 QwenSafe，并与 Qwen3-VL、LLaVA-1.6 和 Gemini-2.5-Flash 等先进视觉语言模型对比。结果显示，QwenSafe 在二分类 CRD 识别上整体优于所有基线，尤其在正类召回率上分别相对提升了 111.8%、36.1% 和 2.1%。论文强调，描述项感知的多模态对齐能显著增强自动内容分类能力；可见文本未给出更细的消融或泛化数值。

<details>
<summary>完整摘要</summary>

移动应用市场要求开发者披露标准化的内容分级描述（CRD），以便向用户说明应用中可能存在的敏感或受限内容。由于应用内容具有多模态特征，既包括文本描述，也包括视觉界面，因此要确保这些披露信息准确且一致仍然具有挑战。本文提出 QwenSafe，这是一种视觉语言模型，旨在通过联合推理应用元数据和截图，自动识别 Apple 定义的 CRD 是否存在。为实现该任务的可扩展训练，我们提出 metadata2CRD，一种数据构造流程，通过结合应用描述、截图以及正式的描述定义，合成与描述项对齐的问答对。我们在 Qwen3-VL-8B 的基础上，先进行监督微调，再使用 Direct Preference Optimization（DPO）进行偏好优化，使模型预测与跨视觉和文本模态的、描述项特定的证据与解释对齐。我们在 12 个 Apple 定义的内容分级描述上评估 QwenSafe，并与当前最先进的视觉语言模型进行比较，包括 Qwen3-VL、LLaVA-1.6 和 Gemini-2.5-Flash。QwenSafe 在二分类 CRD 任务上稳定优于所有基线模型，在正类召回率方面分别实现了 111.8%、36.1% 和 2.1% 的提升。我们的结果表明，面向描述项的多模态对齐能够显著提升自动内容分类效果，并显示出视觉语言模型在支持移动应用市场可扩展且一致的内容分级方面的潜力。

</details>

---

### [[20_Research/Papers/具身智能/The_Yes-Man_Syndrome_Benchmarking_Abstention_in_Embodied_Robotic_Agents|The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents]]

![[assets/2605.20544_figure.png|800]]

- **arXiv**: [2605.20544](https://arxiv.org/abs/2605.20544)
- **PDF**: https://arxiv.org/pdf/2605.20544
- **详细分析**: [[20_Research/Papers/具身智能/The_Yes-Man_Syndrome_Benchmarking_Abstention_in_Embodied_Robotic_Agents|The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents]]
- **作者**: Doguhan Yeke, Elif Su Temirel, Ananth Shreekumar, Brandon Lee, Dongyan Xu, Z Berkay Celik
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.5，大模型 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

具身智能机器人越来越多地依赖视觉-语言模型（VLM）作为高层规划器，把自然语言指令和视觉观察转化为可执行动作，但现有研究更多关注“能不能回答”，较少关注“该不该执行”。在真实机器人环境中，系统不仅要识别指令，还要判断其是否存在歧义、物理上不可行、基于错误前提，或由于感知与上下文不足而无法可靠解析。若模型在这些场景下仍“照单全收”，就可能把错误决策带入多步任务执行，造成连锁失败。因此，这篇论文专门把“拒答/弃权”能力作为具身机器人规划中的独立能力来测量与评估，具有明显的现实意义。

#### 方法概述和架构

论文提出 RoboAbstention，一个用于生成具身机器人拒答样本的可扩展、可审计框架。首先，作者构建了一个包含八类拒答情形的分类体系，覆盖参考指向缺失或歧义、意图未充分说明、主观偏好、物理不可行、能力缺失、指令矛盾以及错误前提等情况。随后，RoboAbstention 采用三阶段流水线：先用 VLM 对图像中的场景进行结构化视觉锚定，抽取对象、属性和空间关系；再基于这些场景表示进行确定性的约束推导，判断哪些拒答条件成立；最后使用类别特定的模板生成受控指令，形成与图像严格对应、可验证的 (image, instruction) 对。该框架从五个机器人数据集中采样 1,250 张真实场景图像，并在其上生成 6,069 条评测指令，用于测试前沿 VLM 和具身规划模型的拒答行为。除直接基准测试外，作者还尝试了防御式提示和上下文学习等缓解策略，并将这些策略串联到推理阶段比较其对拒答率的影响。

#### 实验结果分析

实验在五个具身机器人数据集（DROID、Robo2VLM、RoboVQA、BridgeV2、EgoThink）上进行，并评测了多种前沿 VLM 以及具身规划模型。结果表明，当前模型在拒答能力上普遍薄弱：最佳模型 Gemini 2.5 Flash 也只在 6,069 条基准指令中拒答 39.0%，而具身规划器 Gemini Robotics ER 1.6 Preview 仅为 16.5%。进一步地，防御式提示和 in-context learning 能显著改善表现，使 Gemini Robotics ER 1.6 Preview 的拒答率提升到 93.6%，GPT 5.4 Mini 提升到 88.6%，但仍未彻底解决问题。论文还指出，模型存在明显的“默认执行”倾向，这说明拒答应被视为具身 AI 的独立评测维度。

<details>
<summary>完整摘要</summary>

视觉-语言模型（VLM）被用作具身智能体的高层规划器，将自然语言指令和视觉观察转化为动作计划。虽然已有工作研究了大语言模型（LLM）中的拒答能力，但现有基准大多是纯文本的，无法体现具身机器人环境中固有的感知锚定与物理约束。在这类场景中，拒答意味着模型需要识别指令何时是含糊的、在物理上不可行的、基于错误前提的，或由于可用感知模态与上下文限制而无法解决。为弥补这一空白，我们提出了一个用于刻画具身机器人中拒答的分类体系，并给出 RoboAbstention：一个可扩展且可审计的框架，用于基于来自五个机器人数据集的图像生成拒答指令。RoboAbstention 通过三阶段流水线实现该分类体系：（1）结构化视觉锚定，（2）确定性的约束推导，以及（3）通过类别特定模板进行受控指令生成。由此可以构建一个多样化且具有可验证拒答条件的数据集。我们评测了多种前沿 VLM，发现所有模型在拒答方面都存在显著弱点，即便是具备高级推理能力的模型也不例外。表现最好的模型 Gemini 2.5 Flash 只会对我们 6,069 条基准指令中的 39.0% 进行拒答，而具身规划器 Gemini Robotics ER 1.6 Preview 的拒答率仅为 16.5%。我们进一步探索了提升 VLM 规划器拒答能力的方法，如防御式提示和 in-context learning，发现这些干预能显著提升性能：Gemini Robotics ER 1.6 Preview 的拒答率达到 93.6%，GPT 5.4 Mini 达到 88.6%，但没有任何方法能够完全解决这一问题。我们已开源 RoboAbstention，地址为 https://purseclab.github.io/RoboAbstention/ 。

</details>

---

### [[20_Research/Papers/大模型/ParaVT_Taming_the_Tool_Prior_Paradox_for_Parallel_Tool_Use_in_Agentic_Video_Reinforcement_Learning|ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video Reinforcement Learning]]

![[assets/2605.20342_figure.png|800]]

- **arXiv**: [2605.20342](https://arxiv.org/abs/2605.20342)
- **PDF**: https://arxiv.org/pdf/2605.20342
- **详细分析**: [[20_Research/Papers/大模型/ParaVT_Taming_the_Tool_Prior_Paradox_for_Parallel_Tool_Use_in_Agentic_Video_Reinforcement_Learning|ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video Reinforcement Learning]]
- **作者**: Zuhao Yang, Kaichen Zhang, Sudong Wang, Keming Wu, Zhongyu Yang, Bo Li, Xiaojuan Qi, Shijian Lu, Xingxuan Li, Lidong Bing
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

长视频理解正在从“单次问答”转向“带工具的智能体推理”：模型需要在长视频中自主定位证据片段，并调用裁剪等视频处理工具完成精细分析。这类方法若采用顺序式多轮调用，容易出现单次裁剪失误被层层传递、上下文不断膨胀以及推理成本随轮数线性增长等问题。本文关注的核心瓶颈在于：当模型具备较强的预训练工具先验时，强化学习既能推动工具探索，又会破坏冷启动时学到的结构化输出格式，形成“工具先验悖论”，因此值得关注。

#### 方法概述和架构

论文提出 ParaVT，用于在长视频理解中进行并行视频工具调用：主智能体在单轮内同时发出多个时间窗口的 crop 请求，由多个共享参数的子智能体分别处理不同片段，并将各自返回的文本摘要汇总后生成最终答案。整体训练采用两阶段流程，先用包含并行工具轨迹的冷启动 SFT 建立可解析的工具调用格式，再用带可验证奖励的 agentic RL 进行强化学习。针对普通 GRPO 在格式稳定性和工具使用上的双重失效，作者进一步提出 PARA-GRPO（Parseability-Anchored and Ratio-gAted GRPO）。该方法包含两项关键机制：其一是在最容易坍塌的结构化 token 位置施加定向格式奖励，并通过受限生成固定起始推理标签，以稳定可解析性；其二是对每个提示随机化可用帧预算，构造“调用工具”相较于“跳过工具”具有可区分奖励信号的训练样本，从而抑制跳过工具的奖励捷径。

#### 实验结果分析

作者在 6 个长视频理解基准上评估了方法效果，与 Qwen3-VL 基线相比，ParaVT 平均提升 7.9%。实验还显示，PARA-GRPO 将训练时的格式遵循率从 0.13 提升到 0.64，说明其对结构化输出稳定性有显著修复作用。文中还通过与较弱工具先验的模型进行对照，验证了“强先验有助于工具探索但会加剧格式坍塌”的悖论；具体实验细节与部分数值在节选中未完整展开。

<details>
<summary>完整摘要</summary>

通过强化学习训练大型多模态模型（LMM）原生调用视频处理工具（例如裁剪）已成为长视频理解的一条有前景的路径。然而，现有的原生 RL 方法采用顺序式地分派工具调用（即每次只调用一个工具）：一次错误的裁剪会在没有同伴纠错的情况下传播错误，多轮工具调用会污染上下文，而且推理成本会随着轮数线性增长。为此，我们提出 ParaVT，这是首个面向并行视频工具调用（Parallel Video Tool calling）的多智能体端到端 RL 训练框架；它能够在单轮中分派多个时间窗口裁剪，从而获得更干净的上下文和更强的容错性。尽管如此，将标准 RL 应用于 ParaVT 时会暴露出一个我们称之为“工具先验悖论（Tool Prior Paradox）”的障碍：那些使工具探索成为可能的预训练工具先验，也会破坏冷启动的结构化格式，并在温度采样下暴露出跳过工具的奖励捷径。我们通过对一个工具先验更弱的 LMM 进行跨模型对照验证了这一点：其格式保持稳定，但 RL 却不会激发任何工具调用，这表明先验强度是格式坍塌与工具探索共同背后的驱动因素。为此，我们提出 PARA-GRPO（Parseability-Anchored and Ratio-gAted GRPO），它在标准 RL 基础上加入两项互补机制：（i）仅在最容易坍塌的结构化 token 位置施加定向格式奖励；（ii）对每个提示随机化帧预算，使得调用工具相较于跳过工具能产生可测量的奖励信号。在 6 个长视频理解基准上，ParaVT 相比 Qwen3-VL 基线平均提升 7.9%，而 PARA-GRPO 将训练时的格式遵循率从 0.13 提升到 0.64。随着现代 LMM 的工具能力越来越多地被内化，RL 必须与这些先验协同工作，而 ParaVT 为智能体式 RL 提供了一套通用方案。代码、数据和模型权重已公开。

</details>

---

### [[20_Research/Papers/大模型/WildRoadBench_A_Wild_Aerial_Road-Damage_Grounding_Benchmark_for_Vision-Language_Models_and_Autonomous_Agents|WildRoadBench: A Wild Aerial Road-Damage Grounding Benchmark for Vision-Language Models and Autonomous Agents]]

![[assets/2605.20306_figure.png|800]]

- **arXiv**: [2605.20306](https://arxiv.org/abs/2605.20306)
- **PDF**: https://arxiv.org/pdf/2605.20306
- **详细分析**: [[20_Research/Papers/大模型/WildRoadBench_A_Wild_Aerial_Road-Damage_Grounding_Benchmark_for_Vision-Language_Models_and_Autonomous_Agents|WildRoadBench: A Wild Aerial Road-Damage Grounding Benchmark for Vision-Language Models and Autonomous Agents]]
- **作者**: Bingnan Liu, Chenhang Cui, Rui Huang, Jiani Luo, Zhirong Shen, Tinghao Wang, Xiande Huang, Lingbei Meng, Fei Shen, An Zhang
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 1.0（加权：大模型 0.8，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

道路巡检中的损伤定位是一个很实际的视觉任务：无人机拍摄的航拍图像里，裂缝、坑洞、积水、路面碎屑等缺陷往往很小、很细微，还容易和阴影、水渍、接缝、车道线以及普通沥青纹理混淆。现有通用视觉语言模型虽然在开放词汇理解上进展很快，但在这种专业、嘈杂、细粒度的航拍场景中，是否还能稳定完成“看图找损伤”的定位任务仍缺乏系统检验。另一方面，LLM驱动的自主智能体已经能搜网页、写代码、搭建训练流程，但它们能否把一个感知任务真正做成可用检测器，也需要更贴近真实工程的评测。WildRoadBench 正是把这两个问题放到同一套专业标注的无人机数据上进行比较，因此很值得关注。

#### 方法概述和架构

论文提出 WildRoadBench，一个野外航拍道路损伤 grounding 基准，基于同一份 1,061 张图像的专业标注无人机语料，同时设计了两个评测轨道。VLM Track 评测固定视觉语言模型的直接定位能力：模型输入一张图和一个简短类别提示，零样本输出该场景下所有目标的边界框与置信度，使用统一的提示、解码和结果解析流程，并映射回统一坐标系后按 COCO 检测协议评分。Agent Track 评测 LLM 驱动的自主智能体：智能体只拿到任务说明、少量可见样例和固定交互预算，可以搜索公开网页、下载或适配预训练组件、编写训练与推理代码，并把预测结果提交给一个只返回标量反馈的评测器，在隐藏测试集上迭代改进。两个轨道使用相同的图像集和同一套 per-class AP_50 指标，额外报告 Macro mAP、Macro/Micro F1 与 TP/FP/FN，以便同时观察定位精度和漏检、误检模式。

#### 实验结果分析

作者在 25 个 VLM（16 个开源、9 个闭源前沿模型）和 15 个前沿 LLM 智能体上做了系统评测，数据集是同一套 1,061 张航拍道路损伤图像，指标以 Macro AP_50 为主。结果显示，两条路线在这一“野外”场景下都远未达到可靠水平：闭源前沿模型在 VLM 排行中领先，但仍有超过一半的指标空间没有被利用；开源模型明显落后，新一代或推理风格变体也没有稳定带来更好的定位效果。尤其是小目标对所有开源模型都非常困难；智能体虽然拥有更丰富的工具与工程自由度，但总体仍落后于最强 VLM，且有若干模型在预算内甚至无法完成一次有效提交。

<details>
<summary>完整摘要</summary>

我们提出 WildRoadBench，这是一个野外航拍道路损伤 grounding 基准，它把视觉语言模型的直接视觉定位能力与 LLM 驱动智能体的自主研究和工程能力，结合到同一套经过专业标注的无人机语料上。我们在同一图像集上、使用相同的 per-class AP_50 指标，设置了两种评测协议。VLM Track 通过统一的提示、解码和解析流程，考察一个固定的 VLM 能否仅凭一张图像和一个简短提示，在单次推理中定位特定领域的损伤。Agent Track 则考察一个自主智能体：在只得到书面任务说明、少量探索样本和固定交互预算的情况下，是否能够搜索公开网络、调整预训练组件、编写训练与推理代码，并通过一个标量反馈的评测器在隐藏测试集上提交预测结果。我们评测了大量闭源前沿模型和开源 VLM，也评测了若干前沿 LLM 智能体。结果表明，在这种野外场景下，两条路线都远未达到可靠性能：闭源前沿模型在 VLM 排行榜上领先，但仍然丢掉了超过一半的指标；开源 grounding 模型的表现明显更低，而更新一代模型或推理风格变体并不总能稳定提升定位效果；所有开源模型在小目标上都几乎失效；智能体虽然具备更丰富的能力，但仍落后于最强 VLM，而且有些智能体在预算内甚至无法完成有效提交。我们已在 https://anonymous.4open.science/r/wildroadbench-0607 开源代码和数据，以支持后续可复现研究。

</details>

---
