# cs.CV | Computer Vision and Pattern Recognition | 2026-05-22

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/具身智能/GesVLA_Gesture-Aware_Vision-Language-Action_Model_Embedded_Representations|GesVLA: Gesture-Aware Vision-Language-Action Model Embedded Representations]]

![[assets/2605.22812_figure.png|800]]

- **arXiv**: [2605.22812](https://arxiv.org/abs/2605.22812)
- **PDF**: https://arxiv.org/pdf/2605.22812
- **详细分析**: [[20_Research/Papers/具身智能/GesVLA_Gesture-Aware_Vision-Language-Action_Model_Embedded_Representations|GesVLA: Gesture-Aware Vision-Language-Action Model Embedded Representations]]
- **作者**: Wenxuan Guo, Ziyuan Li, Meng Zhang, Yichen Liu, Yimeng Dong, Chuxi Xu, Yunfei Wei, Ze Chen, Erjin Zhou, Jianjiang Feng
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 2.4，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

Vision-Language-Action（VLA）模型正在成为通用机器人操作的重要方向，它试图把视觉感知、语言理解和动作生成统一到同一框架中，用于现实场景中的抓取、放置和选择等任务。然而，现有系统主要依赖文本指令，在杂乱环境中面对多个相似物体时，往往难以准确消解“这个”“那里”这类空间歧义。本文关注的价值在于：把人类自然使用的指向手势引入机器人指令接口，使机器人能够更直接地理解目标位置，从而提升具身交互的准确性与效率。

#### 方法概述和架构

论文提出 GesVLA（Gesture-Aware Vision-Language-Action Model Embedded Representations），把手势作为与语言并行的第一类指令模态，而不是事后辅助信号。方法核心是一个双 VLM 架构：VLM_int 负责基于手势和语言进行意图推理，输出目标描述及可视化提示；VLM_per 负责结合场景观测、语言和来自前者的推理结果进行在线感知，并将其映射到后续动作策略所需的潜在表示。作者没有把手势离散化为文本，而是把由手部关键点提取的手势特征直接编码进共享潜空间，使其能够同时参与高层推理和低层动作生成。动作部分采用基于 flow 的策略，通过迭代去噪生成连续动作序列；模块间采用单向、非对称的信息流，VLM_int 的缓存状态可复用，从而提高推理效率。数据层面，作者构建了可扩展的手势数据生成管线：将手模型渲染到真实场景图像上，生成带有精确指向标注的半合成数据，以缓解真实采集昂贵、标注困难以及 sim-to-real 视觉差距问题。训练上采用两阶段策略，先学习手势感知，再学习动作预测，以同时获得手势理解和操作能力。

#### 实验结果分析

作者在多个真实机器人任务上评估了 GesVLA，包括用于验证的受控积木操作任务，以及更贴近应用的商品选择和生鲜选择场景。实验表明，引入手势后，目标定位准确率和人机交互效率都得到稳定提升，尤其是在复杂、拥挤、相似物体较多的环境中效果更明显。文中还报告了消融实验与定性对比，用于验证手势嵌入表示、双 VLM 结构和两阶段训练的有效性；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

视觉-语言-动作（VLA）模型通过将感知与动作统一起来，在通用机器人操作中展现出很强的潜力。然而，现有 VLA 系统主要依赖文本指令，在包含多个相似物体的复杂场景中，难以消解空间歧义。为解决这一局限，我们引入手势作为并行指令模态，并提出一种手势感知的视觉-语言-动作模型 GesVLA。我们的方法将手势特征直接编码到潜在空间中，使其能够参与高层推理和低层动作生成，并采用双 VLM 架构，使手势表示与动作策略紧密耦合。在数据层面，我们构建了一个可扩展的手势数据生成管线：将手部模型渲染到真实场景图像上，从而减小 sim-to-real 视觉差距，同时生成具有多样运动模式和相应指向标注的丰富数据。此外，我们采用两阶段训练策略，使模型同时具备手势感知和动作预测能力。我们在多个真实机器人任务上评估了该方法，包括用于验证的受控积木操作任务，以及更实用的商品和生鲜选择场景。实验结果表明，加入手势能够持续提升目标定位准确率和人机交互效率，尤其是在复杂且杂乱的环境中效果更为明显。项目主页：https://gwxuan.github.io/GesVLA/。

</details>

---

### [[20_Research/Papers/具身智能/From_Abstraction_to_Instantiation_Learning_Behavioral_Representation_for_Vision-Language-Action_Model|From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model]]

![[assets/2605.22671_figure.png|800]]

- **arXiv**: [2605.22671](https://arxiv.org/abs/2605.22671)
- **PDF**: https://arxiv.org/pdf/2605.22671
- **详细分析**: [[20_Research/Papers/具身智能/From_Abstraction_to_Instantiation_Learning_Behavioral_Representation_for_Vision-Language-Action_Model|From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model]]
- **作者**: Bing Hu, Zaijing Li, Rui Shao, Junda Chen, April Hua Liu, Wei-Shi Zheng, Liqiang Nie
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.8（加权：具身智能 1.8）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

视觉-语言-动作模型（VLA）是具身智能中用于机器人操作的重要范式，但在从仿真到真实、或跨场景分布变化时，性能往往明显下降。现有方法通常依赖动作中心的隐变量来构造行为表示，却容易受到短时序切片和静态对齐假设的限制，导致复杂任务中的动作不连贯、执行漂移。本文关注如何从长时序演示中学习更稳定、可迁移的行为表示，因此对机器人操作与 sim-to-real 泛化具有较强研究价值。

#### 方法概述和架构

论文提出 BehaviorVLA，一个围绕“行为表示”设计的 VLA 框架，核心由 Visuomotor Behavior Encoder（VBE）和 Phase-conditioned Behavior Decoder（PBD）组成。VBE 采用因果的三流结构，分别建模视觉、动作与行为序列，并用基于 Mamba 的选择性状态空间模型在长时间跨度上聚合轨迹信息，从而把多步演示压缩为统一的行为表示。为减少环境噪声干扰，VBE 在时间建模后再通过交叉注意力融合视觉与动作信息，让行为流提取更偏向任务结构而非瞬时观测。PBD 则将该行为表示解码为具体动作，它引入阶段状态与进度感知机制，在执行过程中动态对齐任务先验和当前进度，避免静态 latent 造成的时间错位。训练上，模型分两阶段进行：先学习行为流形，再进行带先验引导的策略微调；推理时则结合从记忆库检索到的全局 prototype 和在线估计的 phase state 生成动作。

#### 实验结果分析

作者在 RoboTwin 2.0、LIBERO 和 CALVIN 上进行了实验，报告的结果分别达到 58%、98% 和 4.36（Avg.Len），显示出较强的任务成功率与长程执行能力。论文还在真实机器人与仿真到真实迁移场景中验证了方法，指出 BehaviorVLA 仅使用 50% 的示范数据即可达到与 OpenVLA-OFT 相当的表现，体现出更好的数据效率与泛化能力。根据正文节选，模型同时进行了消融研究与可视化分析，但节选中未给出更多具体数值。

<details>
<summary>完整摘要</summary>

视觉-语言-动作（VLA）模型在分布偏移下往往会出现性能下降，因为它们难以在不同环境中学习到可泛化的行为表示。现有方法虽然尝试通过以动作为中心的潜变量来构建行为表示，但通常受限于短时程的时间碎片化和静态执行对齐，因此在复杂场景中容易产生不一致的行为。为了解决这些问题，我们提出 BehaviorVLA，一个通过学习具有时间一致性的行为表示来实现稳健操控的框架。我们的方法包含两个对称的组成部分：（1）Visuomotor Behavior Encoder（VBE），它利用基于因果 Mamba 的架构，将长时程轨迹信息聚合为统一的行为表示；（2）Phase-conditioned Behavior Decoder（PBD），它通过将任务级先验与实时执行进度动态对齐，把该表示解码为精确动作。在 RoboTwin 2.0、LIBERO 和 CALVIN 上的实验表明，该方法取得了 58%、98% 和 4.36（Avg.Len）的最新最佳结果。值得注意的是，在真实世界的仿真到真实迁移中，BehaviorVLA 只使用 50% 的示范数据，就达到了与 OpenVLA-OFT 相当的性能，展示出更强的数据效率和泛化能力。

</details>

---

### [[20_Research/Papers/机器人/Decoupling_Ego-Motion_from_Target_Dynamics_via_Dual-Interval_Motion_Cues_for_UAV_Detection|Decoupling Ego-Motion from Target Dynamics via Dual-Interval Motion Cues for UAV Detection]]

![[assets/2605.22605_figure.png|800]]

- **arXiv**: [2605.22605](https://arxiv.org/abs/2605.22605)
- **PDF**: https://arxiv.org/pdf/2605.22605
- **详细分析**: [[20_Research/Papers/机器人/Decoupling_Ego-Motion_from_Target_Dynamics_via_Dual-Interval_Motion_Cues_for_UAV_Detection|Decoupling Ego-Motion from Target Dynamics via Dual-Interval Motion Cues for UAV Detection]]
- **作者**: Liuyang Wang, Feitian Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

无人机视角下的目标检测面临强烈自运动、相机抖动以及尺度剧烈变化等问题，尤其是在动态场景中，小目标很容易被漏检。虽然静态图像上的检测器已经较成熟，但直接用于 UAV 视频时，由于每帧独立处理、缺少时序信息，性能往往明显下降。现有基于运动的方案要么依赖计算开销较高的光流，要么只用单一时间间隔做差分，前者难以部署到资源受限平台，后者又对抖动敏感且难以兼顾快慢不同的运动模式。因此，这篇工作针对“如何在不引入重型光流的前提下，把目标运动从无人机自运动中分离出来”这一问题，具有较强的实用价值。

#### 方法概述和架构

论文提出一个仅依赖视觉信息的 motion-guided 检测框架，以 YOLO 为主体，在当前帧上做常规多尺度特征提取，同时并行处理历史帧来生成运动线索。首先使用基于单应性的 Global Motion Compensation（GMC）对齐相邻帧，训练阶段用高精度的 SIFT+RANSAC 估计单应矩阵，推理阶段则改用更轻量的 ORB 级联方案以满足实时性。随后设计 Dual-Interval Motion Extraction，在补偿后的帧空间中同时计算短间隔（t-1）与长间隔（t-5）的差分，分别通过平滑、阈值化、开运算等步骤得到互补的运动掩码，并进行交集与闭运算融合，得到更稳健的稀疏运动 mask。最后，Motion-Guided Attention（MGA）把该运动 mask 作为软空间注意力注入 FPN，在 P3/P4/P5 等多尺度特征上增强与运动一致的区域，从而帮助检测头恢复被抖动或背景干扰淹没的小目标。整体上，这一流程实现了“对齐背景—提取双时间尺度运动—注意力增强特征—输出检测框”的端到端检测思路。

#### 实验结果分析

作者在 VisDrone-VID 数据集上验证了方法，相比强基线 YOLOv8 在严重 ego-motion 条件下表现更稳定，并获得一致性提升。消融实验进一步表明，双时间间隔设计和 MGA 模块都对性能提升有明确贡献，同时也验证了该设计在保持较低额外开销的同时能够增强小目标和动态目标的检测效果。正文节选中提到还做了 padding 消融和运行时间分析，说明作者关注了部署效率与稳定性，但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

来自无人机（UAV）的目标检测会受到严重的自运动、相机抖动以及较大尺度变化的挑战。尽管现代检测器在静态图像上表现良好，但将其直接应用到 UAV 视频时往往会失败，尤其是在动态场景中的小目标检测。现有基于运动的方法要么依赖计算代价较高的光流，要么采用单一时间间隔的差分，这两类方法要么对抖动敏感，要么难以捕获多样化的运动模式。为此，我们提出一种仅依赖视觉信息的 motion-guided 检测框架，用于将目标运动与由相机引入的扰动解耦。首先，基于单应性的 Global Motion Compensation（GMC）对相邻帧进行对齐；随后引入 Dual-Interval Motion Extraction 策略，同时捕获短期与长期的运动线索。为了融合这些线索，我们在 Feature Pyramid Network 中设计了一个轻量级的 Motion-Guided Attention（MGA）模块，用于增强特征表示。基于 VisDrone-VID 数据集的实验表明，该方法在强 YOLOv8 基线之上，面对严重 ego-motion 时能够持续取得提升。消融研究也进一步证实了双时间间隔设计以及所提出 motion-guided attention 机制的有效性。

</details>

---

### [[20_Research/Papers/大模型/AgroTools_A_Benchmark_for_Tool-Augmented_Multimodal_Agents_in_Agriculture|AgroTools: A Benchmark for Tool-Augmented Multimodal Agents in Agriculture]]

![[assets/2605.22366_figure.png|800]]

- **arXiv**: [2605.22366](https://arxiv.org/abs/2605.22366)
- **PDF**: https://arxiv.org/pdf/2605.22366
- **详细分析**: [[20_Research/Papers/大模型/AgroTools_A_Benchmark_for_Tool-Augmented_Multimodal_Agents_in_Agriculture|AgroTools: A Benchmark for Tool-Augmented Multimodal Agents in Agriculture]]
- **作者**: Zi Ye, Yibin Wen, Xiaoya Fan, Xinyu Zhang, Jing Wu, Kun Zeng, Zurong Mai, Jiarui Zhang, Bohan Shi, Juepeng Zheng, Jianxi Huang, Yutong Lu...
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

农业决策越来越依赖能够同时理解图像、调用外部工具并输出可执行行动的多模态大模型，例如病虫害诊断、作物识别、数量测量、地块变化检测与农艺分析等场景。现有农业多模态基准大多只看最终答案对不对，难以评估模型是否真的会选工具、填参数、处理执行失败并把中间结果正确整合到最终结论中。对于精度敏感的农业工作流来说，过程正确性和结果正确性同样重要，因此需要一个面向“工具增强型多模态智能体”的专门评测基准。这篇论文值得关注之处在于，它把农业场景中的视觉理解、外部工具调用和可执行评测结合起来，补上了现有基准的关键空白。

#### 方法概述和架构

论文提出 AgroTools，一个面向农业工具增强型多模态智能体的基准。该基准包含 539 个问答样本和 1,097 张异构农业图像，覆盖 12 个公开农业数据集，并组织成五类任务：识别与检索、计数与测量、分割解释、变化检测、可视化与分析。作者同时构建了一个可执行的农业工具环境，内置 14 个面向农业工作流的工具；每个样本都配有结构化的参考工具使用轨迹，用于描述应该如何规划步骤、选择工具、生成参数并完成执行。整体采用类似 ReAct 的交互形式，模型需要根据图像和自然语言指令自行推断中间步骤，再逐步调用工具并整合输出，既能做终值评测，也能做过程级评测。论文还在无工具、逐步推理和端到端等设置下对多种多模态大模型进行统一测试，以观察工具规划、参数生成、执行恢复和最终答案合成等环节的能力差异。

#### 实验结果分析

作者在 AgroTools 上评测了 13 个代表性多模态大模型，包括 9 个开源模型和 4 个闭源模型；从节选内容看，实验覆盖了工具使用、轨迹评估和最终任务成功率等多个维度。结果表明，现有模型在农业工具使用场景中整体仍不可靠，尤其在工具规划、参数生成、执行失败后的恢复以及最终答案整合方面存在明显瓶颈。论文还指出，较强模型在加入工具后受益更明显，而较弱模型往往会被较长的工具说明、无效参数和不佳的执行恢复能力拖累。可见文本未给出具体数值，但结论清楚表明该基准能有效暴露当前农业多模态智能体的短板。

<details>
<summary>完整摘要</summary>

农业决策越来越需要多模态系统将视觉观察转化为可靠、可执行的行动。然而，现有农业多模态基准主要评估最终答案的正确性，对于模型能否使用外部工具完成精度敏感工作流的评估支持有限。本文提出 AgroTools，用于评估农业中的工具增强型多模态智能体。AgroTools 包含 539 个问答实例，配有 1,097 张异构农业图像，覆盖五类任务，并提供一个包含 14 个农业工具的可执行环境。每个查询都标注了结构化的工具使用轨迹，从而能够同时从过程层面评估执行质量和从结果层面评估任务成功。我们在 AgroTools 上评测了 9 个开源和 4 个闭源多模态大语言模型。结果表明，当前模型在农业工具使用设置下仍远未达到可靠水平，在工具规划、参数生成、执行恢复以及最终答案合成方面都存在明显瓶颈。我们希望 AgroTools 能支持未来面向高精度农业应用的多模态智能体研究。基准与评测已发布在 https://huggingface.co/datasets/AgroTools/AgroTools 。

</details>

---

### [[20_Research/Papers/大模型/Imagine2Real_Towards_Zero-shot_Humanoid-Object_Interaction_via_Video_Generative_Priors|Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors]]

![[assets/2605.22272_figure.png|800]]

- **arXiv**: [2605.22272](https://arxiv.org/abs/2605.22272)
- **PDF**: https://arxiv.org/pdf/2605.22272
- **详细分析**: [[20_Research/Papers/大模型/Imagine2Real_Towards_Zero-shot_Humanoid-Object_Interaction_via_Video_Generative_Priors|Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors]]
- **作者**: Jiahe Chen, ZiRui Wang, Feiyu Jia, Xiao Chen, Xiaojie Niu, Weishuai Zeng, Tianfan Xue, Xiaowei Zhou, Jiangmiao Pang, Jingbo Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.1，机器人 1.3）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

全身人形机器人与物体交互（HOI）是面向家庭、工厂等非结构化环境的重要能力，但高质量3D交互数据极其稀缺，导致现有方法很难学到稳定、通用的交互策略。已有基于视频生成先验的方法虽然为机器人学习提供了新路径，但在HOI场景中往往依赖显式CAD模型等几何先验，容易出现机器人与物体运动表征不对齐的问题；同时，密集运动重定向还会带来高复杂度和误差累积。该工作值得关注之处在于，它尝试把“从视频想象到现实执行”这条链路直接用于零样本HOI，并尽量摆脱几何建模与复杂重定向的限制。

#### 方法概述和架构

作者提出 Imagine2Real，一个面向零样本全身人形-物体交互的框架。方法先将机器人与物体的运动统一表示为4D点轨迹，用共享表征消除机器人和物体分别估计带来的空间/深度错位。推理时，系统先根据图像和文本指令合成交互视频，再从视频中提取稀疏的关键点轨迹，最后将这些轨迹送入 mocap 系统驱动实体机器人执行。核心控制器是 Keypoints Tracker，它只跟踪三个交互关键点——机器人底座和双手——从而绕过密集重定向流程。为了让这种稀疏信号下仍保持自然步态，作者把 Behavior Foundation Model（BFM）的潜在空间作为搜索域：先在大规模本体感知运动上预训练 BFM backbone，再在 loco-manipulation 数据上训练关键点跟踪器，最后用少量HOI数据微调 Interaction Adaptor，形成三阶段渐进式训练流程。

#### 实验结果分析

从节选内容看，实验覆盖了仿真到仿真（sim2sim）评估以及真实世界部署，重点验证从生成视频到4D轨迹再到实体机器人执行的完整闭环。对比对象包括现有的人形运动跟踪、HOI生成/跟踪及视频驱动机器人相关方法，评价重点应围绕跟踪质量、步态自然性与交互可执行性展开。作者还设计了分阶段训练与关键点稀疏跟踪的消融思路，用于说明 BFM 先验与 Interaction Adaptor 对稳定性和零样本迁移的贡献；但可见文本未给出具体数值。总体结论是，该框架在无需几何模型、无需复杂重定向的情况下，实现了零样本物理部署。

<details>
<summary>完整摘要</summary>

全身人形机器人与物体交互（HOI）受到高保真3D数据稀缺的严重制约。尽管视频生成先验提供了一条很有前景的替代路径，但现有方法由于依赖几何先验（例如显式CAD模型）而存在表征不对齐问题，并且由于大量重定向以及形态不匹配而面临重定向复杂度高的问题。为此，我们提出 Imagine2Real，一个面向灵活、免几何交互的零样本人形-物体交互框架。为解决表征不对齐，我们将机器人和物体的运动统一表述为4D点轨迹。为克服重定向复杂度，我们的 Keypoints Tracker 只跟踪稀疏的关键点（底座、双手和物体），完全绕开了会放大误差的重定向过程。为了在这些稀疏信号下仍保持自然步态，我们将 Behavior Foundation Model（BFM）的潜在空间用作跟踪器的搜索域。借助渐进式训练策略，Imagine2Real 通过简单的跟踪奖励学习到鲁棒行为，并能够在 mocap 系统中实现零样本的真实物理部署。

</details>

---

### [[20_Research/Papers/大模型/EvoIR-Agent_Self-Evolving_Image_Restoration_Agentic_System_via_Experience-Driven_Learning|EvoIR-Agent: Self-Evolving Image Restoration Agentic System via Experience-Driven Learning]]

![[assets/2605.22208_first_page.png|800]]

- **arXiv**: [2605.22208](https://arxiv.org/abs/2605.22208)
- **PDF**: https://arxiv.org/pdf/2605.22208
- **详细分析**: [[20_Research/Papers/大模型/EvoIR-Agent_Self-Evolving_Image_Restoration_Agentic_System_via_Experience-Driven_Learning|EvoIR-Agent: Self-Evolving Image Restoration Agentic System via Experience-Driven Learning]]
- **作者**: Kailin Zhuang, Jiawei Wu, Zhi Jin
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

在图像复原任务中，往往需要面对多种退化因素叠加的复杂场景，例如同时存在噪声、模糊、压缩伪影或其他退化时，模型不仅要判断使用哪些工具，还要决定不同退化的处理顺序。基于多模态大语言模型（MLLM）的图像复原智能体虽然具备灵活规划能力，但在零样本条件下常因缺少经验而频繁试错，带来较高的推理开销。现有方法分为两类：基于训练的方法效率高但难以适配新工具或新退化，免训练方法虽然更灵活，却往往依赖过于粗糙的显式经验，仍然需要大量试错。该论文围绕“经验如何组织、如何积累、如何自我进化”这一核心问题展开，因此对大模型驱动的图像复原智能体研究具有较强参考价值。

#### 方法概述和架构

作者提出 EvoIR-Agent，一种基于经验驱动学习的自进化图像复原智能体系统。首先，论文系统梳理了免训练图像复原智能体中的经验组成，将经验显式拆分并结构化表示。随后构建层次化经验池，把经验从粗到细组织起来，用于为不同工具选择与退化去除顺序提供指导。推理时，系统根据当前输入图像及其退化情况，从经验池中检索并利用相关经验，辅助 MLLM 进行工具选择和操作顺序规划，从而减少无效试错。与此同时，方法还引入自进化机制：系统会基于累计运行记录不断更新经验池，使经验从初始状态逐步扩展和优化，实现从“从头积累”到“持续迭代”的闭环。整体上，该方法强调经验的显式管理与动态更新，而不是将经验完全隐式地写入模型参数。

#### 实验结果分析

论文在实验中表明，EvoIR-Agent 在 full reference 指标上取得了明显领先，并且在性能与效率之间达到了更优的 Pareto 平衡。与现有最先进方法相比，它不仅提升了复原质量，也减少了因零样本规划不稳定而产生的试错成本。正文节选未提供具体实验设置、数据集名称和数值结果，因此可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

多模态大语言模型（MLLM）驱动的图像复原智能体在退化耦合场景中表现有效，因为它能够灵活选择工具并决定去除顺序。然而，这类方法的零样本规划通常在缺乏经验时会失败，为了获得满意结果，往往需要付出严重的试错开销。目前已有两种范式用于解决这一问题，但仍存在一个两难：基于训练的方法将内在经验嵌入参数中，推理效率高，但无法很好兼容新的工具或新的退化类型；而免训练方法通过显式存储经验来保证兼容性，但由于经验过于粗糙，仍然会带来试错开销。为解决这一困境，我们提出 EvoIR-Agent。该方法首先系统地形式化了免训练图像复原智能体中的经验组成；随后构建了一个层次化经验池，使其能够针对多样化工具和不同去除顺序提供由粗到细的引导；进一步地，我们引入自进化机制，利用累积的运行记录从头更新经验池，从而大幅提升性能与效率。大量实验表明，EvoIR-Agent 在 full reference 指标上取得了显著领先，并且相较于当前最先进方法，在性能与效率之间实现了出色的 Pareto 最优平衡。

</details>

---

### [[20_Research/Papers/大模型/SceneGraphGrounder_Zero-Shot_3D_Visual_Grounding_via_Structured_Scene_Graph_Matching|SceneGraphGrounder: Zero-Shot 3D Visual Grounding via Structured Scene Graph Matching]]

![[assets/2605.21788_first_page.png|800]]

- **arXiv**: [2605.21788](https://arxiv.org/abs/2605.21788)
- **PDF**: https://arxiv.org/pdf/2605.21788
- **详细分析**: [[20_Research/Papers/大模型/SceneGraphGrounder_Zero-Shot_3D_Visual_Grounding_via_Structured_Scene_Graph_Matching|SceneGraphGrounder: Zero-Shot 3D Visual Grounding via Structured Scene Graph Matching]]
- **作者**: Xuefei Sun, Xujia Zhang, Brendan Crowe, Doncey Albin, Christoffer Heckman
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

零样本 3D visual grounding 的目标，是在开放场景中根据自由形式语言描述，在三维环境里定位目标物体，这对机器人理解“桌子左边的杯子”“靠近门的椅子”这类组合式指代尤为关键。现有很多 VLM/LLM 方法虽然效果不错，但往往依赖视角相关的推理或隐式场景表示，容易带来跨视角不一致、可解释性不足、以及对多物体关系查询不稳的问题。本文值得关注之处在于，它尝试把 3D grounding 从“边看边想”的隐式推理，改写为“场景图与查询图的结构化匹配”，更贴近机器人长期运行中的可复用空间记忆需求。

#### 方法概述和架构

作者提出 SceneGraphGrounder，将 3D visual grounding 重构为“查询图—场景图”的图匹配问题。首先，系统输入 RGB-D 序列和里程计，对场景进行物体级重建：利用类无关检测器与分割模型获得物体掩码，再通过深度和相机位姿回投到 3D，形成可持续更新的物体实例。接着，采用 visual marker prompting，在每个 2D 物体掩码中心加上唯一标记，让 VLM 识别物体及其相互关系，并把这些 2D 关系提升到 3D，构建同时包含语义边和空间边的 persistent 3D scene graph。对于用户语言查询，系统用 LLM 解析出 query graph，把目标物体和参照物体及其关系显式建模出来；随后先做语义筛选缩小候选节点集合，再通过 DFS 枚举映射并用节点相似度、边相似度、目标节点匹配分数和覆盖率共同打分，选出最优 grounding 结果。文中还设计了 VLM gate，用于在存在视角歧义时借助额外的视觉-语言输入做 tie-break，增强多视角一致性。

#### 实验结果分析

作者在 ScanRefer 上进行了实验，并与多种 zero-shot 方法比较，结论是该方法在仅使用 RGB-D 输入的条件下，达到了具有竞争力的结果；节选文本未给出具体数值。正文还报告了 unique/multiple split、graph matching vs. VLM selection、架构设计影响等消融分析，用于验证图匹配和结构化表示的贡献。除此之外，作者还在真实移动机器人平台上进行了部署，展示了在长时程物理环境中的稳健空间推理能力；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

零样本 3D visual grounding 的任务，是在非结构化环境中依据自由形式自然语言，将目标物体定位出来。近年来基于 vision-language model（VLM）的方法取得了有前景的结果，但它们依赖视角相关的推理或隐式表示，因此在处理组合式查询时，空间一致性和可解释性受到限制。为此，我们提出 SceneGraphGrounder：将 3D grounding 重新表述为在重建得到的 3D 场景图上的结构化图匹配。为了实现这一表述，我们引入一种 visual marker prompting 策略，使 VLM 能够从 2D 视图中推断物体之间的关系，并进一步将这些关系提升为一个持久化的 3D scene graph，同时编码空间关系与语义关系。给定一个查询，我们构建查询图，并与场景图进行受约束的对齐，从而保证多视角一致性并提供可解释的推理。我们在 ScanRefer 基准上的实验表明，尽管只使用 RGB-D 输入，我们的方法在 zero-shot 方法中取得了具有竞争力的性能。我们还通过在移动机器人上的真实世界部署验证了该框架，展示了其在长时程物理环境中的稳健空间推理能力。论文接受后，我们将公开代码。

</details>

---

### [[20_Research/Papers/具身智能/PhysX-Omni_Unified_Simulation-Ready_Physical_3D_Generation_for_Rigid,_Deformable,_and_Articulated_Objects|PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects]]

![[assets/2605.21572_figure.png|800]]

- **arXiv**: [2605.21572](https://arxiv.org/abs/2605.21572)
- **PDF**: https://arxiv.org/pdf/2605.21572
- **详细分析**: [[20_Research/Papers/具身智能/PhysX-Omni_Unified_Simulation-Ready_Physical_3D_Generation_for_Rigid,_Deformable,_and_Articulated_Objects|PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects]]
- **作者**: Ziang Cao, Yinghao Liu, Haitian Li, Runmao Yao, Fangzhou Hong, Zhaoxi Chen, Liang Pan, Ziwei Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

面向机器人、具身智能和物理仿真，能够直接用于模拟器的“simulation-ready”三维资产越来越重要，因为这类资产不仅要外观逼真，还要具备尺度、材质、关节运动和可交互性等物理属性。现有三维生成方法大多偏重视觉外观，或者只覆盖刚体、可变形体、关节体中的单一类别，难以统一支持多种物理形态。与此同时，缺少大规模高质量带物理标注的数据集，以及缺少能够在真实场景中评估物理属性的通用基准，也限制了方法的实际应用。因此，这篇工作值得关注，因为它同时尝试补齐“统一生成”“数据集”“评测基准”三块短板。

#### 方法概述和架构

作者提出 PhysX-Omni，一个面向多类物体的统一 simulation-ready 物理三维生成框架，覆盖刚体、可变形体和关节体。方法采用基于 VLM 的自回归生成范式：先对输入的完整或部分遮挡图像进行全局理解，推断类别、语义身份、绝对尺度、部件层级以及潜在物理属性，再基于这些全局信息逐步生成局部的细粒度几何与物理属性。为解决高分辨率三维结构建模难题，论文设计了一种新的几何表示：将部件级体素网格沿 z 轴切片，并对每层二维掩码使用 RLE 编码，同时引入模板层以提升压缩效率和表达一致性。该表示可直接兼容已有的 voxel-based 3D decoder，从而在不依赖额外网格分割模块的情况下生成高质量网格。除此之外，作者构建了 PhysXVerse 数据集，收集了 8K+ 资产、覆盖 2K+ 室内外类别；并提出 PhysX-Bench，从几何、绝对尺度、材质、可供性、运动学和功能描述六个维度评估生成与理解能力。

#### 实验结果分析

论文在常规指标和 PhysX-Bench 上对 PhysX-Omni 进行了系统评估，并与近期先进方法比较，结果显示其在生成质量和泛化能力上都表现强劲。作者还通过消融实验验证了所提几何表示与整体框架的有效性，说明更直接的高分辨率结构建模有助于提升复杂拓扑和物理属性预测的准确性。进一步实验表明，PhysX-Omni 生成的资产可以直接用于仿真场景生成和机器人策略学习，展示了较好的可部署性。具体数值在节选文本中未给出。

<details>
<summary>完整摘要</summary>

simulation-ready 的物理三维资产由于在下游任务中的广泛应用而成为一个很有前景的方向。然而，现有大多数三维生成方法要么忽略物理属性，要么仅限于单一类别的资产，例如刚体、可变形体或关节体。为了解决这些限制，我们提出 PhysX-Omni，一个面向多种资产类型、统一的 simulation-ready 物理三维生成框架。具体而言，我们设计了一种新颖且高效的几何表示，专为视觉-语言模型（VLM）定制，能够无需压缩地直接编码高分辨率三维结构，从而显著提升生成性能。此外，我们构建了首个通用的 simulation-ready 三维数据集 PhysXVerse，覆盖丰富的室内与室外类别。进一步地，为了在真实场景中全面且灵活地评估生成与理解能力，我们提出 PhysX-Bench，其包含六个关键属性：几何、绝对尺度、材质、可供性、运动学以及功能描述。基于常规指标和 PhysX-Bench 的大量实验表明，PhysX-Omni 在生成与理解两方面都表现出色。此外，更多实验进一步验证了 PhysX-Omni 在 simulation-ready 场景生成和机器人策略学习中的应用潜力。我们相信，PhysX-Omni 将显著推动广泛的下游应用，尤其是具身智能和基于物理的仿真。

</details>

---
