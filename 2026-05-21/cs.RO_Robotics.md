# cs.RO | Robotics | 2026-05-21

#arxiv #ComputerScience

**论文数**: 26

### [[20_Research/Papers/大模型/MC-Risk_Multi-Component_Risk_Fields_for_Risk_Identification_and_Motion_Planning|MC-Risk: Multi-Component Risk Fields for Risk Identification and Motion Planning]]

![[assets/2605.21406_figure.png|800]]

- **arXiv**: [2605.21406](https://arxiv.org/abs/2605.21406)
- **PDF**: https://arxiv.org/pdf/2605.21406
- **详细分析**: [[20_Research/Papers/大模型/MC-Risk_Multi-Component_Risk_Fields_for_Risk_Identification_and_Motion_Planning|MC-Risk: Multi-Component Risk Fields for Risk Identification and Motion Planning]]
- **作者**: Maximilian Link, Yingjie Xu, Yingbai Hu, Yinlong Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.2，机器人 0.9）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

自动驾驶和机器人运动规划需要在复杂交通场景中尽早、稳定且可解释地识别风险，并将风险直接转化为规划代价。现有方法要么依赖黑盒预测，虽然覆盖全面但缺乏可解释性；要么采用经典势场，但往往对车辆类别、速度、转向曲率和道路拓扑的刻画过于粗糙。对于行人等弱势交通参与者，很多方法仍使用近似对称的“团块”风险表示，难以体现其朝向和运动意图。因此，这篇工作值得关注之处在于，它试图把“早期风险定位”和“可直接用于规划”这两个目标统一起来。

#### 方法概述和架构

论文提出 MC-Risk，一种面向规划器对齐的多组件风险场，定义在鸟瞰图（BEV）网格上，并将场景风险表示为多个可解释模块的线性叠加。第一部分是 motorized-agent field（MAF），它把黑盒多模态轨迹预测器的候选未来轨迹与解析的 Gaussian-torus 风险构造结合起来，使风险带宽随速度和曲率变化，并让风险高度随前瞻距离衰减。第二部分是 VRU risk field（VRF），针对行人等弱势道路使用者，使用与朝向和速度对齐的各向异性核，并引入前向偏置，以替代传统各向同性的风险团块。第三部分是 road penalty field（RPF），基于 HD-map 的完整拓扑对道路区域、同向车道和对向车道施加不同风险/惩罚，显式编码越界与车道语义。最终，三类场被叠加成场景级风险图，可用于 RiskBench 的风险识别评估，也可直接作为 MPC 的代价密度输入，从而在无需额外训练的情况下实现风险感知轨迹生成。

#### 实验结果分析

作者在 RiskBench 的 collision 子集上进行了标准化定量评测，这是论文所述的首个对风险场形式进行统一量化的公开基准评估。实验覆盖了 rule-based、forecast+check、collision anticipation 和 behavior prediction 等多类基线，评价指标包括 OT-F1、OT-F1-T（1/2/3 s）、wMOTA 和 PIC；可见文本未给出具体数值，但结果表明 MC-Risk 在整体风险定位和最早危险提示方面最好。论文还做了规划集成实验，将风险场作为 MPC 的成本密度，展示了无需再训练即可生成风险感知轨迹。正文还提到进行了消融研究，并引入 visibility adapter 与统一指标套件来保证评估一致性。

<details>
<summary>完整摘要</summary>

我们提出 MC-Risk，这是一种面向规划器对齐的多组件风险场，定义在鸟瞰图（BEV）网格上，能够实现更早、经过校准且具有类别感知的风险定位。MC-Risk 由三个可解释模块线性组合而成：（i）motorized-agent field，它将黑盒多模态轨迹预测器与解析的 Gaussian-torus 构造相融合，其中横向宽度会随速度和曲率增大，而高度会随前瞻距离衰减；（ii）VRU risk field，它用一个与朝向和速度对齐、且具有前向偏置的各向异性核，替代了各向同性的行人风险团块；（iii）road penalty field，它利用完整的 HD-map 拓扑，对越界区域施加惩罚，并针对同向与对向车道建模车道相关的风险暴露。我们据我们所知，在 RiskBench 的碰撞子集上进行了首次标准化的风险场定量评估。MC-Risk 在整体风险定位和最早危险提示方面都取得了最佳表现。最后，我们还展示了一个可直接插拔的规划接口：将该风险场作为 MPC 的代价密度使用，从而无需额外训练即可实现风险感知轨迹生成。

</details>

---

### [[20_Research/Papers/具身智能/From_swept_contact_to_pose_Probe-aware_registration_via_complementary-shape_docking|From swept contact to pose: Probe-aware registration via complementary-shape docking]]

![[assets/2605.21398_figure.png|800]]

- **arXiv**: [2605.21398](https://arxiv.org/abs/2605.21398)
- **PDF**: https://arxiv.org/pdf/2605.21398
- **详细分析**: [[20_Research/Papers/具身智能/From_swept_contact_to_pose_Probe-aware_registration_via_complementary-shape_docking|From swept contact to pose: Probe-aware registration via complementary-shape docking]]
- **作者**: Chen Chen, Yunwen Li, Yifan Xu, Xiangjie Yan, Chang Shu, Jianxia Hou, Shiji Song, Xiang Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

在机器人高精度操作中，必须先将先验模型与真实场景准确配准，才能把规划的动作稳定地落到目标上，尤其是在牙科制备、骨科手术和精密装配这类需要亚毫米精度的任务中。现有光学配准往往依赖手眼标定、标记物和视线条件，链路长且容易累积制造误差与外参误差，在狭窄或遮挡环境里也不够实用。接触式配准虽然摆脱了外部传感器，但很多方法把探针简化为点或球头，忽略了真实探针几何，并且对稀疏、间歇接触很脆弱。因此，这篇工作值得关注，因为它尝试把“接触配准”重新表述为一种显式考虑探针形状的几何对接问题，从而在无外部传感器条件下获得更高精度。

#### 方法概述和架构

论文提出的是一种面向探针感知的配准方法，核心思想是将接触注册重写为“互补形状对接（complementary-shape docking）”：把物体与探针的扫掠体积看成两种互补几何，再通过对接来估计位姿。方法首先把物体表示为体素网格，同时结合 watertight mesh 的 SDF 和可触达表面掩码，构造一个既能奖励贴近表面、又能惩罚深穿透、还会限制到可接触区域的评分网格。探针一侧则根据整段运动轨迹和探针自身 SDF，生成扫掠占据网格，用来表达轨迹经过的空间范围。推理阶段采用两步全局到局部搜索：先在 SO(3) 上用低差异采样做方向搜索，并通过 3D FFT 相关在平移空间快速找出粗位姿；再在局部邻域继续细化方向。最后进入连续优化阶段，在 SE(3) 上使用李代数更新与解析接触敏感度进行精修，从而在不依赖脆弱点对应关系的情况下获得高精度收敛。

#### 实验结果分析

作者在自由形状网格的仿真中验证了该方法，达到小于 0.04 mm 的平移误差和小于 0.4° 的旋转误差，并且对位姿噪声和接触丢失表现出较强鲁棒性。真实实验是在牙科制备机器人上完成的，使用圆柱形 bur 作为探针，在不依赖外部传感器的条件下取得了 0.42 mm 和 3.75° 的结果。与光学跟踪器配准流程相比，该方法取得了更好的表现；节选文本未给出更完整的基线列表与消融细节。

<details>
<summary>完整摘要</summary>

在机器人高精度操作中，先验模型与真实场景之间的准确配准至关重要，但光学方法通常存在标定链路过长、视线受限以及制造误差等问题。我们提出一种无需标定的替代方案，将接触式配准重构为物体与探针扫掠体积之间的互补形状对接，并显式考虑探针几何，同时融合接触与非接触两类证据。我们的求解器采用全局到局部的搜索流程：先在低差异采样的 SO(3) 上进行 3D FFT 相关搜索，再通过李代数更新与解析接触敏感度进行连续 SE(3) 精修。该流程能够高效探索位姿空间，并实现接近计量级的收敛，同时避免脆弱的点对应关系。在自由形状网格的仿真中，该方法达到了小于 0.04 mm 和小于 0.4° 的精度，并且对位姿噪声与接触丢失具有鲁棒性。在一台牙齿制备机器人上，我们的方法取得了 0.42 mm 和 3.75° 的结果，优于光学跟踪器配准方法，同时无需任何外部传感器。这些结果表明，该方法为外科与工业机器人提供了一种实用且精确的配准策略。

</details>

---

### [[20_Research/Papers/强化学习/Learning_Robust_Dexterous_In-Hand_Manipulation_from_Joint_Sensors_with_Proprioceptive_Transformer|Learning Robust Dexterous In-Hand Manipulation from Joint Sensors with Proprioceptive Transformer]]

![[assets/2605.21330_figure.png|800]]

- **arXiv**: [2605.21330](https://arxiv.org/abs/2605.21330)
- **PDF**: https://arxiv.org/pdf/2605.21330
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Robust_Dexterous_In-Hand_Manipulation_from_Joint_Sensors_with_Proprioceptive_Transformer|Learning Robust Dexterous In-Hand Manipulation from Joint Sensors with Proprioceptive Transformer]]
- **作者**: Senlan Yao, Chenyu Yang, Jaehoon Kim, Aristotelis Sympetheros, Robert K. Katzschmann
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.2（加权：具身智能 1.5，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

灵巧手的手内操作（in-hand manipulation）是机器人实现类人精细操作的关键能力，但由于接触动力学复杂、动作空间高维且状态感知困难，一直难以稳定落地。现有方法多依赖视觉或触觉来跟踪物体状态，而机器人手上最基础、最容易获取的关节传感信息却长期被低估，尤其是在腱驱动灵巧手上更是如此。本文聚焦“仅靠关节传感，机器人究竟还能做到多少”这一问题，进一步关注：直接关节传感是否优于电机编码器反馈、如何从关节测量中提取环境/物体信息，以及在没有外部感知时能否实现有竞争力的真实世界控制。

#### 方法概述和架构

作者提出 Proprioceptive Transformer（PT），用于腱驱动灵巧手上的连续立方体旋转任务，整个控制过程只使用关节位置和速度历史，不依赖视觉或触觉。训练流程采用教师-学生蒸馏：教师策略在仿真中通过 PPO 学习，并使用特权信息（包括真实物体位姿）进行强化学习；随后将教师策略蒸馏给学生策略，学生仅接收带噪声的关节传感序列、上一时刻动作与控制指令。PT 的核心是 Transformer 编码器，通过自注意力建模时间序列，挖掘关节测量中的隐式物体状态信息；同时结合辅助重建目标，让学生不仅模仿教师动作，还重建物体状态和干净的关节状态。推理阶段，PT 直接在真实 ORCA 手上零样本部署，实现仅基于本体感觉反馈的控制。

#### 实验结果分析

实验在真实 ORCA 灵巧手上进行，并与 PPO 基线及 MLP、LSTM 等结构比较，任务是连续旋转 55mm 立方体。结果显示，PT 的旋转速度达到基线的 3.1 倍，且在立方体位姿估计上，相比 MLP 基线的 RMSE 低 23.4%，说明 Transformer 更擅长从关节历史中提取隐式外部状态。正文节选还指出，直接关节传感比电机编码器反馈更适合作为腱传动灵巧手的本体感觉输入，能够缓解由传动非线性带来的仿真到现实差异。可见文本还给出，方法在真实硬件上实现了 100% 成功率和零掉落，并且辅助重建损失对鲁棒操控至关重要。

<details>
<summary>完整摘要</summary>

手内物体操控是灵巧机器人一项基础但极具挑战性的能力。尽管灵巧操作已经取得了显著进展，现有方法仍严重依赖视觉或触觉来跟踪物体状态，而关节传感——机器人手上最容易获得的模态——却长期被忽视，尤其是在腱驱动手上更是如此。本文研究仅靠关节传感究竟能做到什么程度，具体提出以下问题：(i) 电机编码器还是直接关节传感能提供更好的本体感觉反馈；(ii) 如何从关节测量中提取环境信息；(iii) 在没有外部感知的情况下，仅靠关节控制能否实现有竞争力的真实世界性能。为此，我们提出 Proprioceptive Transformer（PT），这是一种无需外部感知的连续立方体旋转方法，面向腱驱动灵巧手，仅使用关节传感反馈。首先在带有特权物体信息的强化学习中训练教师策略，然后将其蒸馏为 PT，PT 仅依赖关节位置与速度的历史序列运行。Transformer 结构能够有效从关节传感读数的时间模式中提取隐式物体状态信息。在真实 ORCA 手上的实验表明，我们的方法相比基线实现了 3.1 倍更高的旋转速度。我们还证明，PT 在立方体位置估计上的 RMSE 比 MLP 基线低 23.4%，表明其能够从本体感觉来源中更优地提取外部感知信息。

</details>

---

### [[20_Research/Papers/具身智能/Reinforcement_Learning_for_Risk_Adaptation_via_Differentiable_CVaR_Barrier_Functions|Reinforcement Learning for Risk Adaptation via Differentiable CVaR Barrier Functions]]

![[assets/2605.21257_figure.png|800]]

- **arXiv**: [2605.21257](https://arxiv.org/abs/2605.21257)
- **PDF**: https://arxiv.org/pdf/2605.21257
- **详细分析**: [[20_Research/Papers/具身智能/Reinforcement_Learning_for_Risk_Adaptation_via_Differentiable_CVaR_Barrier_Functions|Reinforcement Learning for Risk Adaptation via Differentiable CVaR Barrier Functions]]
- **作者**: Xinyi Wang, Taekyung Kim, Bardh Hoxha, Georgios Fainekos, Dimitra Panagou
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.8，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

在拥挤、动态且障碍物运动存在不确定性的环境中进行机器人导航，既要避免碰撞，又要尽量保持通行效率，这对具身智能与移动机器人都是典型难题。现有风险中性方法容易忽视尾部危险事件，而鲁棒优化虽然更安全，却常常过于保守，导致机器人动作迟缓甚至不可行。本文关注的是如何让机器人根据场景自适应地调节风险偏好，在保证显式概率安全约束的同时避免“总是很谨慎”的低效率行为，因此具有较强的机器人落地价值。

#### 方法概述和架构

论文提出一种端到端的风险自适应导航框架，核心是将强化学习与基于 CVaR barrier functions 的可微分二次规划安全层结合起来。首先，障碍物未来运动被建模为 Gaussian mixture model，从而刻画多种可能的行为模式与不确定性。其次，RL 策略并不直接输出最终控制量，而是联合学习名义控制输入、风险水平 β 以及安全裕度 ΔR，这些量再送入可微分 CVaR-BF-QP 层。该安全层根据概率安全约束对控制进行修正，在训练时可反向传播梯度，使策略与安全模块端到端协同优化。推理时，策略会依据场景上下文调整保守程度：在风险较低或空间充足时更高效，在拥挤或不确定性更强时自动变得更谨慎。

#### 实验结果分析

作者在动态、随机和拥挤环境中对方法进行了大规模评估，并考察了不同障碍物密度与多种机器人模型下的表现。对比对象覆盖了基于优化的方法、纯强化学习方法以及强化学习与优化结合的方法；评价重点包括安全性、效率、泛化能力和计算效率。实验还设置了 3 类分布外（out-of-distribution）场景，用于检验方法在未见过环境下的鲁棒性。根据摘要和正文节选，本文方法在总体上取得了最强表现；但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

在拥挤环境中、且障碍物运动存在不确定性的情况下进行规划仍然很困难，因为随机交互往往会导致机器人行为过于保守，或者效率下降。为了解决这一问题，我们提出了一个面向拥挤导航的端到端风险自适应框架，其中障碍物运动的不确定性由 Gaussian mixture model 建模。该框架将强化学习（RL）与基于 Conditional Value-at-Risk（CVaR） barrier functions 的可微分二次规划安全层结合起来，联合学习名义控制输入、风险水平和安全裕度，并显式施加概率安全约束。这样的设计使系统能够依据场景进行上下文感知的自适应，在需要时才提高谨慎程度，从而兼顾效率与安全。我们在动态、不确定且拥挤的环境中，针对不同障碍物密度和机器人模型进行了广泛评估，并进一步在 3 种分布外场景下测试其泛化能力。我们还比较了基于优化、基于强化学习以及强化学习与优化集成的多种方法，结果表明，所提出的方法在不确定条件下的安全性、效率和泛化能力方面整体表现最强。

</details>

---

### [[20_Research/Papers/大模型/To_Select_or_not_to_Select,_that_is_the_Question_Distilling_Robot_Skill_Prediction_into_a_Small_Ensemble|To Select or not to Select, that is the Question: Distilling Robot Skill Prediction into a Small Ensemble]]

![[assets/2605.21242_figure.png|800]]

- **arXiv**: [2605.21242](https://arxiv.org/abs/2605.21242)
- **PDF**: https://arxiv.org/pdf/2605.21242
- **详细分析**: [[20_Research/Papers/大模型/To_Select_or_not_to_Select,_that_is_the_Question_Distilling_Robot_Skill_Prediction_into_a_Small_Ensemble|To Select or not to Select, that is the Question: Distilling Robot Skill Prediction into a Small Ensemble]]
- **作者**: Haechan Mark Bong, Simon Roy, Euhid Aman, Giovanni Beltrame
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

随着机器人群体越来越异构，包含人形机器人、履带车、四足机器人和无人机，如何为一个自然语言任务选择合适的机器人，正在成为多机器人系统中的关键问题。论文聚焦“机器人技能预测”：把任务描述映射为执行任务所需的物理能力，例如飞行、轮式移动、足式移动、水面行动、水下行动和手部操作。作者指出，现有瓶颈在于缺少“自然语言任务—机器人技能”对应的标注数据，而直接依赖大模型零样本推理虽然省事，但在固定技能 taxonomy 下未必最优。因此，这篇工作值得关注的地方在于，它把“机器人该不该接这个任务”的问题从开放式推理，转化为一个可训练、可部署的轻量级技能预测问题。

#### 方法概述和架构

论文构建了一个合成任务到技能数据集：先用 Claude Opus 4.5、GPT-5 和 DeepSeek-R1 逐步生成 1000 条多样化任务描述，再结合人工抽查和边界样本定向生成，最终得到 1261 条任务及其六维技能标签。技能集合被定义为六类差异化能力：fly、legs、wheels、hands、under water、surface water；每个任务输出一个 6 维二值向量，采用多标签分类而不是单标签分类。模型部分使用两个句向量编码器 all-mpnet-base-v2 和 all-MiniLM-L6-v2，各自接一个四层 MLP 分类头，输出六个 sigmoid 概率；训练时仅解冻编码器最后两层，以降低小数据场景下的过拟合风险。最终推理时对两个模型的 sigmoid 概率做平均，再以 0.5 阈值产生技能集合预测，形成一个小型集成模型。论文还根据错误分析对训练数据做了“边界任务”补充，例如专门增加 legs 与 wheels 的区分样本，以强化模型对容易混淆技能边界的识别。

#### 实验结果分析

实验在 200 条分层测试任务上评估，指标包括 EM、Hamming Score 和 Macro F1。结果显示，133M 参数的集成模型达到 83.5% EM、96.3% Hamming Score 和 0.941 Macro F1，超过 Kimi K2 的 72.0% EM、GPT-OSS-120B 的 71.5% EM 和 Llama-4-Scout-17B 的 69.0% EM。单独微调的 all-mpnet-base-v2 也达到 81.5% EM，已经优于所有零样本大模型基线，说明小型专用模型在该固定技能分类任务上更占优势。作者还指出，性能提升主要来自对 wheels 等易错边界的定向数据增强，而在 underwater 和 surface water 等关键词明显的技能上，各模型都表现较稳。

<details>
<summary>完整摘要</summary>

随着机器人群体越来越异构，包含人形机器人、地面车、四足机器人和无人机，为任务选择合适的机器人已经成为一个核心系统问题。我们研究机器人技能预测：即将自然语言任务描述映射到执行该任务所需的物理能力，例如飞行、轮式移动、足式移动、水面行动、水下行动和手部操作。由于不存在将自然语言任务描述映射到机器人物理能力的标注数据，我们利用大语言模型辅助生成并结合定向标签审查，构建了一个合成的任务到技能数据集。基于这些数据训练后，一个约 133M 参数的两模型集成体（mpnet + MiniLM）在一个分层抽样的 200 条任务测试集上达到了 83.5% 的任务到技能匹配准确率，优于在相同零样本提示下的 Kimi K2（1T MoE，72.0%）、GPT-OSS-120B（71.5%）和 Llama-4-Scout-17B（69.0%）。这些结果表明，对于固定的机器人技能分类体系，使用合成数据训练的小型专用模型，可以在车队级任务路由中优于更大规模的通用大模型。

</details>

---

### [[20_Research/Papers/机器人/Humanoid_Whole-Body_Manipulation_via_Active_Spatial_Brain_and_Generalizable_Action_Cerebellum|Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum]]

![[assets/2605.21133_figure.png|800]]

- **arXiv**: [2605.21133](https://arxiv.org/abs/2605.21133)
- **PDF**: https://arxiv.org/pdf/2605.21133
- **详细分析**: [[20_Research/Papers/机器人/Humanoid_Whole-Body_Manipulation_via_Active_Spatial_Brain_and_Generalizable_Action_Cerebellum|Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum]]
- **作者**: Zhizhao Liang, Yi-Lin Wei, Xuhang Chen, Mu Lin, Yi-Xiang He, Zhexi Luo, Jun-Hui Liu, Kun-Yu Lin, Wei-Shi Zheng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

这篇论文关注的是人形机器人在复杂三维环境中的全身操控任务，尤其是需要边移动边操作的空间感知型抓取、搬运与协同操作。与桌面场景相比，这类任务面临两类核心瓶颈：一是环境空间关系复杂、遮挡多，机器人很难仅靠固定视角完成稳定理解；二是全身动作生成需要大量真实机器人数据，而这类数据昂贵且稀缺，导致数据驱动方法泛化能力受限。论文之所以值得关注，是因为它试图把多智能体大模型的空间理解能力和动作生成能力拆开建模，直接面向真实机器人、且不依赖任务特定实机数据。

#### 方法概述和架构

作者提出一个名为“Active Spatial Brain + Generalizable Action Cerebellum”的分层多智能体人形全身操控框架。上层 Active Spatial Brain 负责主动空间感知、任务理解与规划：它根据语言指令和视觉观察主动调整带有2-DoF云台与人体底盘联动的相机视角，以解决遮挡和视角不足问题，并结合 Memory Bank 记录当前观察、相机位姿以及执行历史。基于这些信息，Brain 会进行自适应任务分解与动态重规划，把长时程目标拆成可执行子任务，并在需要时决定继续探索视角或调用下层动作代理。下层 Generalizable Action Cerebellum 负责把高层子任务转成可执行的机器人动作，作者将其拆为下肢移动与上肢灵巧操作两部分：下肢代理负责避障导航、接近目标并调整身体位置，上肢代理负责生成可行抓取位姿和后续机械臂轨迹。整个系统在推理时形成感知-规划-控制闭环，Brain 根据执行反馈不断重新评估并触发相应动作代理完成任务。

#### 实验结果分析

论文设计了一组面向空间操控的基准任务，同时评估视觉语言模型在复杂空间理解上的能力，以及系统在真实机器人上的任务表现。实验涵盖多种真实世界任务与环境，并与数据驱动基线方法进行对比；作者还分析了各模块的作用以及不同 VLM 的空间智能水平。结果表明，该框架在空间感知、任务决策和真实机器人执行上都表现出较强能力，并且在多样化任务与环境中优于现有数据驱动方法；但节选文本未给出具体数值。作者还指出，该方法在不使用任务特定真实机器人训练数据或微调的情况下，仍能取得更好的泛化表现。

<details>
<summary>完整摘要</summary>

本文研究空间感知型人形机器人全身操控任务。与桌面场景相比，这一任务带来两个关键挑战：1）在复杂的三维环境中进行空间理解更困难，因为存在丰富而多样的空间关系；2）动作生成更难泛化，因为有限且昂贵的真实机器人数据限制了数据驱动模型的泛化能力。为了解决这些问题，我们提出了一种可泛化的人形移动操作框架，利用多智能体大模型的空间感知与动作生成能力。具体而言，我们的框架包含两个部分：用于主动空间感知和决策的 Active Spatial Brain，以及用于生成可执行机器人动作的 Generalizable Action Cerebellum。前者主动感知空间场景，并对任务规划和子任务分解作出决策；后者根据前一个模块的决策生成可执行的机器人动作，而无需任务特定的真实机器人数据。为了对该框架进行基准测试，我们从两个角度设计了一组空间操控任务：评估空间感知与理解能力，以及评估真实机器人任务性能。实验结果表明，该方法在多样化任务和环境中，在这两个方面都表现出很强的能力。

</details>

---

### [[20_Research/Papers/机器人/Perception_of_Social_Robots_as_Communication_Partners_in_Healthcare_for_Older_Adults|Perception of Social Robots as Communication Partners in Healthcare for Older Adults]]

![[assets/2605.21053_figure.png|800]]

- **arXiv**: [2605.21053](https://arxiv.org/abs/2605.21053)
- **PDF**: https://arxiv.org/pdf/2605.21053
- **详细分析**: [[20_Research/Papers/机器人/Perception_of_Social_Robots_as_Communication_Partners_in_Healthcare_for_Older_Adults|Perception of Social Robots as Communication Partners in Healthcare for Older Adults]]
- **作者**: Hana Yamamoto, Carlotta Julia Mayer, Charlotte Raithel, Theresa Buchner, Christian Werner, Yasuhisa Hirata, Monika Eckstein, Katja Mombaur
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

随着全球护理人力持续短缺，社会辅助机器人被寄予缓解养老与医疗照护压力的希望，但它们能否在老年人群中被视为“可信的交流对象”，以及这类互动是否会带来额外心理负担，仍缺乏系统证据。本文聚焦医疗照护场景中的老年人机交互，试图回答社会机器人是否能像人类一样成为有效沟通伙伴，以及通过“积极提示”是否还能进一步改善互动体验。由于老年人对机器人常同时存在好奇与顾虑，理解其主观接受度、情绪反应和生理压力反应，对于机器人在养老护理中的落地尤其关键。

#### 方法概述和架构

作者采用一个2×2混合实验设计：组间因素为是否加入“积极提示”，组内因素为互动对象是机器人还是人类，并对交互顺序进行平衡，以降低顺序效应。实验共招募35名70岁及以上、具备正常认知功能的德国老年参与者，每人分别与人类和社会机器人各进行一次结构化互动。所用平台是类人机器人Navel，具备头部、肩部、躯干俯仰和移动等自由度，并通过TTS、视觉追踪等能力维持对话与注视互动；实验中采用受限感知的WoZ（Wizard-of-Oz）方式，由远程实验者控制机器人。数据采集采用多模态方式，结合面部表情分析、心率/心率变异性以及问卷主观评价，从情绪、生理与接受度三个维度评估不同条件下的互动效果。

#### 实验结果分析

实验在受控的养老相关交互场景中比较了“机器人 vs. 人类”以及“有无积极提示”的影响，评估指标包括面部表情、心率相关生理数据和问卷反馈。结果显示，机器人互动与人类互动在总体压力水平上没有显著差异；面部表情分析表明，参与者将机器人接受为有效的交流伙伴。生理数据上，机器人互动期间心率略低，提示其可能比人类主导会话更让参与者放松。文中未给出具体数值，但作者指出机器人可承担健康感知问卷等结构化任务，并建议后续重点改进机器人外观与交互内容之间的“不匹配”问题。

<details>
<summary>完整摘要</summary>

为应对全球护理人力短缺，社会辅助机器人需要被用于支持老年人照护，而这要求我们深入理解它们在人机交互过程中对老年人的心理与生理影响。本研究关注两个问题：与人类相比，社会机器人是否可以成为有效的交互伙伴；以及“积极提示”是否也能以类似方式改善这类互动。我们对35名70岁及以上参与者开展了比较研究。通过整合面部表情数据、心率变异性和主观问卷的多模态分析，我们发现，在人类互动与机器人互动之间，总体压力水平没有显著差异。面部表情分析进一步确认，机器人被接受为有效的交互伙伴；而生理数据则显示，机器人互动期间心率略低，表明参与者相较于人类主导的会话处于更放松的状态。这些结果说明，社会机器人能够在不引发心理压力的情况下与老年人互动，并且能够通过执行结构化任务（例如健康感知问卷）来减轻护理人员负担。未来工作应针对机器人设计中发现的“外观—内容不匹配”问题进行改进，以促进更加自然且有效的交互。

</details>

---

### [[20_Research/Papers/机器人/Modeling_and_Control_of_a_Pneumatic_Morphing_Soft_Quadrotor_based_on_the_SOFA_Framework_for_Dynamic_Soft_Robotic_Simulation|Modeling and Control of a Pneumatic Morphing Soft Quadrotor based on the SOFA Framework for Dynamic Soft Robotic Simulation]]

![[assets/2605.21031_figure.png|800]]

- **arXiv**: [2605.21031](https://arxiv.org/abs/2605.21031)
- **PDF**: https://arxiv.org/pdf/2605.21031
- **详细分析**: [[20_Research/Papers/机器人/Modeling_and_Control_of_a_Pneumatic_Morphing_Soft_Quadrotor_based_on_the_SOFA_Framework_for_Dynamic_Soft_Robotic_Simulation|Modeling and Control of a Pneumatic Morphing Soft Quadrotor based on the SOFA Framework for Dynamic Soft Robotic Simulation]]
- **作者**: F. Labra Caso, V. Sumathy, P. Ferrentino, V. Vanderborght, J. Haluska, G. Nikolakopoulos
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics

#### 研究背景与动机

软体无人机兼具高顺应性和较强的抗碰撞能力，适合搜救、狭窄空间穿行、贴附飞行和安全人机交互等场景，但其形变明显、动力学强非线性，给建模与控制带来很大困难。对于气动驱动的软四旋翼而言，气压变化会同时影响结构变形与飞行姿态，传统刚体四旋翼模型难以准确描述这种耦合行为。本文值得关注之处在于，它将 SOFA 这一软体仿真框架与有限元建模、动态仿真和闭环控制结合起来，尝试在保持四旋翼动力学可解释性的同时刻画软臂的时变形变。

#### 方法概述和架构

论文提出一种基于 SOFA 的有限元建模与动态控制方法，用于气动形变软四旋翼（PMSQ）的仿真。作者将软气动臂离散为四面体网格，并采用弹性/超弹性材料本构来计算内部力，从而在仿真中逼近真实的软体动态响应。结构上，软臂由半刚性的内脊柱和硅胶气动执行器组成，两者通过双边约束耦合；气腔则以表面压力约束方式施加压力载荷。SOFA 场景同时包含机械状态、质量矩阵、内部力、外力、约束、碰撞与可视化映射，并通过隐式 Euler 求解器在每个时间步推进系统状态。控制方面，论文先设计周期性差压输入，用左右气腔的反相正弦压力实现臂的横向摆动；随后进一步提出比例-积分（PI）控制器，根据末端位置误差调节单腔压力，以跟踪目标位置并验证闭环形变能力。

#### 实验结果分析

实验在 SOFA 动态仿真环境中完成，验证对象为带有四个软气动臂的 PMSQ，重点展示单臂在周期性激励与误差反馈控制下的形变响应。结果表明，所建模型能够稳定复现气压驱动下的弯曲与位移变化，且闭环 PI 控制可将气动输入调节到目标位置附近，说明该框架具备有效的动态控制分析能力。周期性差压实验中，臂的横向位移表现明显，最大弯曲位移可见文本给出约 ΔY=5 cm、ΔX=1.8 cm；但与真实硬件的系统性对比、消融实验和更完整的性能指标，可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

本文提出一种基于 SOFA 的新型有限元方法，用于气动形变软四旋翼的软体建模，以及相应的动态仿真与控制。该建模方法在保留传统四旋翼动力学物理可解释性与控制结构的同时，能够刻画气动驱动软臂复杂且随时间变化的行为。在 SOFA 中，气动软臂被离散为四面体网格，并依据弹性材料定律计算内部力，以产生与真实动态行为相符的效果。研究在软体内部腔体中施加由周期信号和误差信号共同驱动的气动激励，用于分析其形变能力。最后，作者提出比例-积分控制器，用于研究气动臂的受控动态行为与形变能力，其中通过控制作用于软臂的气动输入来达到期望目标位置。仿真结果表明，所提出的新型建模框架及其控制器设计是有效的。

</details>

---

### [[20_Research/Papers/机器人/Component_Influence-Driven_Fastener_Reduction_for_Robotic_Disassemblability-Aware_Design_Simplification|Component Influence-Driven Fastener Reduction for Robotic Disassemblability-Aware Design Simplification]]

![[assets/2605.21026_figure.png|800]]

- **arXiv**: [2605.21026](https://arxiv.org/abs/2605.21026)
- **PDF**: https://arxiv.org/pdf/2605.21026
- **详细分析**: [[20_Research/Papers/机器人/Component_Influence-Driven_Fastener_Reduction_for_Robotic_Disassemblability-Aware_Design_Simplification|Component Influence-Driven Fastener Reduction for Robotic Disassemblability-Aware Design Simplification]]
- **作者**: Takuya Kiyokawa, Tomoki Ishikura, Shingo Hamada, Genichiro Matsuda, Kensuke Harada
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

为了加速自动再制造，产品设计阶段就需要考虑机器人拆解，但设计人员通常缺少能够量化指出“哪些结构元素在阻碍机器人操作”的反馈。现有可拆卸性设计方法更多关注人工拆解或泛化的结构复杂度指标，难以直接转化为具体、可执行的改版建议。本文聚焦于紧固件减量这一高频、易修改的设计参数，因为紧固件几乎存在于所有制造产品中，且数量多、对拆解时间和路径影响显著。因此，这篇工作值得关注之处在于，它把机器人拆解规划结果反向映射到产品结构上，给出面向设计简化的定量指导。

#### 方法概述和架构

论文提出一个面向机器人可拆卸性设计简化的分析框架 Component Influence-Driven Fastener Reduction。其输入是CAD模型及自动生成的 Contact-Connection-Constraint（CCC）图，以及一条可行的机器人拆解基准序列；首先通过在序列中对部件位置进行交换，统计结构约束违反和评价目标退化的频率，为每个部件计算影响分数。随后，系统在CCC图中识别紧固件节点，并按其所连接的宿主零件进行分组，在每组内优先选择影响分数最高的紧固件作为候选。接着，框架对候选删除进行解析式模拟，重新计算约束边数变化、工具切换次数和机器人移动距离，并用几何稳定性指标筛除会导致结构失稳或孤立的危险修改。最终，系统输出按影响分数排序的紧固件减量候选列表，并将影响分数投影到CAD几何上形成3D热力图，便于设计人员直观定位结构瓶颈。

#### 实验结果分析

作者在7种家用电器上进行了验证，包括冷凝器单元、电视、空调室外机、微波炉、紧凑型微波炉、美容光学设备和电动工具。结果表明，该框架能够准确定位冗余紧固件；移除推荐紧固件后，依据产品结构不同，可在图结构上消除8到132条结构约束，并在结构允许的情况下消除不必要的工具切换，同时将机器人行走距离缩短165到1675毫米。正文节选中未给出与现有基线方法的完整对比表，因此可见文本未给出具体数值的基线提升细节。

<details>
<summary>完整摘要</summary>

为了加速自动再制造，机器人拆解必须在产品设计阶段就被纳入考虑。然而，当前设计人员缺乏能够量化识别哪些结构元素会妨碍机器人操作的反馈。为解决这一问题，本文提出了一个分析框架，重点围绕紧固件减量提供可执行的再设计指导，因为紧固件是几乎所有制造产品中都普遍存在且数量众多的部件。该框架使用计算机辅助设计（CAD）模型及其自动生成的 Contact-Connection-Constraint（CCC）图，将机器人拆解序列规划的结果转化为部件影响分数。这些分数反映了某个部件在机器人拆解序列中引发结构约束违反或评价目标变差的频率。为了直观突出结构上的阻碍因素，框架将这些分数投影到CAD几何上，形成三维热力图。随后，系统对影响力最高的紧固件进行解析式删除模拟，并在评估几何稳定性指标以防止不安全修改的同时，报告结构约束、工具切换和机器人行走距离的预期减少量。对7种家用电器的实验表明，该框架能够成功定位冗余紧固件。移除推荐的紧固件后，依据每个产品的结构配置不同，图上的结构依赖关系减少了8到132条结构约束；此外，在结构允许的情况下，还消除了不必要的工具切换操作，并将机器人移动距离缩短了165到1675毫米。

</details>

---

### [[20_Research/Papers/具身智能/WiXus_A_Wheeled-Legged_Robot_with_Wire-Driven_Environmental_Utilizing_to_Integrate_Mobility_and_Manipulation|WiXus: A Wheeled-Legged Robot with Wire-Driven Environmental Utilizing to Integrate Mobility and Manipulation]]

![[assets/2605.20932_figure.png|800]]

- **arXiv**: [2605.20932](https://arxiv.org/abs/2605.20932)
- **PDF**: https://arxiv.org/pdf/2605.20932
- **详细分析**: [[20_Research/Papers/具身智能/WiXus_A_Wheeled-Legged_Robot_with_Wire-Driven_Environmental_Utilizing_to_Integrate_Mobility_and_Manipulation|WiXus: A Wheeled-Legged Robot with Wire-Driven Environmental Utilizing to Integrate Mobility and Manipulation]]
- **作者**: Shintaro Inoue, Kento Kawaharazuka, Temma Suzuki, Sota Yuzaki, Kei Okada
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

轮式足式机器人因兼具轮式高速移动和足式越障能力，已成为地面移动平台的重要方向，但现有系统大多仍把腿部仅作为“行走机构”，难以在不接触地面的高处、悬崖或垂直墙面执行任务，更无法把腿直接转用于抓取、操作工具等操作类任务。本文关注的正是如何通过外部支撑把腿从纯粹的移动角色中“解放”出来，从而同时扩展机器人的可达空间与任务类型。这一问题对灾害救援、户外作业和农业等场景尤其重要，因此具有较强的现实意义。

#### 方法概述和架构

论文提出并实现了 WiXus，一种将轮式足式机构与利用环境的绳驱动机构融合的新机器人。WiXus 机身为立方体结构，前侧布置四根用于环境锚定的绳索，后侧中心还可接出一根用于工具连接的绳索；两侧各装有一条 3-DOF 的轮式足腿，既能用于常规行走，也能在机身被绳索悬挂后转化为“手臂”执行操作。系统控制上，WiXus 采用并行运行的两套控制器：绳驱控制器负责绳长/速度或质心速度控制，轮式足式控制器负责平面移动；二者通过状态机协调模式切换，并结合 SLAM 与遥操作输入完成任务。论文还设计了可选的 Flying Anchor 模块，使机器人能够借助小型无人机将绳索自动锚定到周围环境中，从而实现更自主的环境利用。

#### 实验结果分析

实验部分展示了 WiXus 在多种任务中的能力，包括平面移动与地图构建、协调绳驱与轮式足式驱动的三维移动/悬崖攀爬，以及在悬挂状态下的物体操作和工具使用。具体包括“救援一只狗（毛绒玩具）”以及使用 loppers 收获苹果（模型）等演示，说明腿部在脱离承重/行走职责后可以被重新当作操作机构使用。节选文本未给出具体数值指标，但可见文本未给出具体数值；整体结论是，借助绳驱对环境的利用，轮式足式机器人的作业边界可以从地面移动显著扩展到高处与复杂三维空间。

<details>
<summary>完整摘要</summary>

轮式足式机器人在脚部装有轮子，通过协调轮驱和腿驱实现高机动性，已经得到开发。不过，这类机器人一直被设计为专门用于移动的作业平台，因此它们没有把腿部重新用于除移动之外的功能，例如物体操作或工具使用的方法。本文针对的问题是：如何通过外部机体支撑，把腿部从移动角色中解放出来，从而挖掘其潜在的任务执行能力。为此，我们提出并开发了一种新机器人 WiXus，它将轮式足式机构与利用外部环境的绳驱机构融合在一起。所开发的 WiXus 不仅能够通过轮式足式驱动实现平面运动，还能通过协调绳驱与轮式足式执行实现三维机动，例如悬崖攀爬。此外，当机身由绳驱悬挂起来时，WiXus 还能成功地把腿部重新用作机械臂，执行物体操作（例如救援一只狗的毛绒玩具）以及工具使用（例如借助 loppers 收获一个苹果模型）。本研究表明，利用绳驱对环境进行利用，是一种能够扩展轮式足式机器人作业范围的新设计原则。

</details>

---

### [[20_Research/Papers/机器人/SubTGraph_Large-Scale_Subterranean_Environment_Synthesis_with_Controllable_Topological_Variability_for_Robotic_Autonomy_Validation|SubTGraph: Large-Scale Subterranean Environment Synthesis with Controllable Topological Variability for Robotic Autonomy Validation]]

![[assets/2605.20917_figure.png|800]]

- **arXiv**: [2605.20917](https://arxiv.org/abs/2605.20917)
- **PDF**: https://arxiv.org/pdf/2605.20917
- **详细分析**: [[20_Research/Papers/机器人/SubTGraph_Large-Scale_Subterranean_Environment_Synthesis_with_Controllable_Topological_Variability_for_Robotic_Autonomy_Validation|SubTGraph: Large-Scale Subterranean Environment Synthesis with Controllable Topological Variability for Robotic Autonomy Validation]]
- **作者**: F. Labra Caso, A. Saradagi, S. Fredriksson, S. Nordström, A. Koval, G. Nikolakopoulos
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.1（加权：具身智能 0.3，大模型 0.1，机器人 1.7）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

地下环境（如矿井、天然洞穴和火山熔岩管）是自主机器人验证的高难度场景，广泛涉及探索、定位、建图、路径规划与多机协同等任务，也与矿山自动化和行星探测密切相关。由于真实地下环境难以进入、采集成本高且安全风险大，研究通常只能在少量环境中做验证，缺乏可用于严格统计评估的大规模仿真基准。该论文关注的核心问题，是如何快速生成具有可控拓扑差异、可重复、且足够逼真的地下仿真世界，以支撑机器人自治系统的硬化与失效分析。

#### 方法概述和架构

论文提出 SubTGraph，一个用于大规模地下环境合成的生成框架，允许用户显式指定环境的拓扑、维度、纹理和障碍物等属性。其核心思想是先将地下空间离散为图结构，在网格中布置约束节点与目标节点，再依据用户给定的结构约束（如交叉口、分支、环路数量）构造成本矩阵，并用 Dijkstra 算法求出连接路径。路径会经过线性构造与扰动处理，以增加随机性与拓扑多样性；随后将二维拓扑扩展为多层结构，通过竖向连通节点形成多层地下世界。最后，系统把图中的顶点类型映射到对应的 topometric tiles，并为各层关联 3D 网格与纹理，生成可直接用于仿真器的地下场景。该方法的输出是一个包含拓扑结构、网格和视觉外观的可仿真地下世界，同时开源了生成代码与 150 个高变异地下世界数据库。

#### 实验结果分析

论文用三个案例验证了 SubTGraph 的实用性：结构语义分割、多机器人路径规划以及 LIO SLAM。实验分别检验了结构语义分割与 topometric 真值的一致性、路径规划在大量不同地下拓扑上的行为模式，以及 LIO SLAM 在复杂地下区域中的失效情形；可见文本未给出具体数值。作者还从拓扑多样性、外观分布、网格生成时间、存储开销和仿真内存占用等方面做了统计分析，用于说明该生成器可支持规模化基准测试。整体结论是，SubTGraph 能提供更可控、更大规模的地下仿真验证平台，弥补现有地下机器人研究中缺少统计化评测基础设施的短板。

<details>
<summary>完整摘要</summary>

地下环境一直是自主机器人研究的前沿方向，主要受到矿山自动化和行星探测（如火星熔岩管）需求的推动。由于真实地下环境难以进入，在逼真的仿真环境中对自治系统进行严格加固与验证至关重要。本文填补了一个众所周知的空白：缺乏大规模、基于仿真的基准测试基础设施，难以对机器人自治能力进行严格的统计评估；因此，地下机器人研究论文通常最多只在少数环境中展示验证结果。本文提出 SubTGraph，一种新颖的框架，可快速合成具有高度多样性的多层地下环境，并支持用户对拓扑、维度、纹理等进行指定，从而生成作业矿井、天然洞穴和熔岩管等不同场景。SubTGraph 通过根据用户指定的结构约束构建成本矩阵，借助经典 Dijkstra 算法和来自 DARPA World Generator 的 topometric tiles，程序化生成地下世界。论文通过三个机器人案例研究展示 SubTGraph 对机器人自治栈不同层级进行严格验证的能力：结构语义分割在 topometric 真值上进行验证，多机器人路径规划被广泛测试以识别算法行为中的模式与趋势，而 LIO SLAM 则在具有挑战性的地下区域中进行压力测试，以识别失效案例。SubTGraph 的世界生成代码已开源（https://github.com/LTU-RAI/SubTGraph.git），同时发布了一个包含 150 个高度多样化地下世界的数据库。

</details>

---

### [[20_Research/Papers/具身智能/Mobile_UMI_Cross-View_Diffusion_Policy_with_Decoupled_Kinematics_for_Mobile_Manipulation|Mobile UMI: Cross-View Diffusion Policy with Decoupled Kinematics for Mobile Manipulation]]

![[assets/2605.20894_figure.png|800]]

- **arXiv**: [2605.20894](https://arxiv.org/abs/2605.20894)
- **PDF**: https://arxiv.org/pdf/2605.20894
- **详细分析**: [[20_Research/Papers/具身智能/Mobile_UMI_Cross-View_Diffusion_Policy_with_Decoupled_Kinematics_for_Mobile_Manipulation|Mobile UMI: Cross-View Diffusion Policy with Decoupled Kinematics for Mobile Manipulation]]
- **作者**: Haoran Huang, Haonan Dong, Huixu Dong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

移动操作机器人要同时完成底盘导航和机械臂操作，在家庭等非结构化环境中尤其依赖高质量示范数据。然而，现有便携式示范接口要么只看见手部、缺少全局导航信息，要么加入躯干视角后又把“走路位移”和“手部动作”混在一起，导致动作标签难以学习。另一方面，扩散策略等生成式方法在移动底盘上推理存在明显延迟，机器人会在生成结果返回前继续前进，执行时就容易出现回退修正和抖动。Mobile UMI 正是针对“示范采集的运动耦合”和“推理延迟的执行错位”这两个瓶颈提出的，因此很值得关注。

#### 方法概述和架构

论文提出 Mobile UMI，一个无需真实机器人参与的移动操作示范与学习框架。示范阶段使用双相机采集：胸部相机记录全局导航上下文，腕部相机记录局部交互细节，从而同时覆盖底盘运动和手部操作。随后，系统通过一次性的 ChArUco 空间锚定，把胸部与手部的视觉惯性坐标系统一到同一参考下，再将手部位姿改写为相对胸部的表示，分解出彼此解耦的 SE(2) 底盘轨迹与 SE(3) 机械臂轨迹。训练阶段在这些解耦标签上学习一个跨视角条件扩散策略；推理阶段则引入异步的滚动时域执行器，通过在线状态匹配把每次生成的动作片段与当前真实位姿重新对齐，丢弃已经过时的航点后再执行。整体上，方法把“动作表示解耦”和“执行时延对齐”连接成一条闭环流程，不需要改动底层策略网络结构。

#### 实验结果分析

作者在 4 个长时程家庭任务上进行了真实世界实验，每个任务做了 100 次试验，平均成功率达到 83.8%。与 ACT 和 Diffusion Policy 的对比表明，仅将标签改为胸部相对表示就能弥补大部分性能差距，而在线状态匹配机制则进一步补上剩余差距。实验结论支持：在本文测试条件下，显式的运动学因子分解结合状态级延迟对齐，是一种无需改造策略架构也能有效提升移动操作性能的方案。

<details>
<summary>完整摘要</summary>

移动端模仿学习在便携式示范接口上面临两个相互耦合的瓶颈：一是动作标签受到行走运动的污染，二是连续移动底盘上的推理延迟会影响执行。近期腕部安装的接口降低了台面级数据采集成本，但单一腕部视角无法捕捉底盘导航所需的全局上下文；如果再加入躯干相机，又会把人类行走和手部动作纠缠在一起。与此同时，生成式策略会带来数百毫秒的推理延迟，在这段时间内底盘已经超过了预测的航点，导致每次动作拼接处都需要向后修正。本文提出 Mobile UMI，一个无需真实机器人参与的示范框架，通过三个组成部分解决上述问题。首先，双相机采集系统同时记录以胸部为中心的全局上下文和以腕部为中心的局部交互，而不需要机器人本体参与。其次，基于 ChArUco 的一次性空间锚定统一胸部与手部的视觉惯性坐标系，然后把手部位姿改写为相对于胸部的表示，提取出解耦的 SE(3) 机械操作轨迹和 SE(2) 底盘轨迹。第三，异步滚动时域执行器执行在线状态匹配：每个新生成的动作片段都会与当前物理位姿重新对齐，从而在执行前丢弃过期航点。完整系统在 4 个长时程家庭任务上进行评估，每个任务进行了 100 次试验，平均成功率达到 83.8%。与 ACT 和 Diffusion Policy 的受控对比表明，仅采用胸部相对标签就能弥补很大一部分差距，而在线状态匹配机制则补上了剩余差距。这些结果说明，在本文测试条件下，显式运动学分解结合状态级延迟对齐，是一种有效的移动模仿学习方案，而且无需对底层策略类别做架构改动。

</details>

---

### [[20_Research/Papers/世界模型/Demo-JEPA_Joint-Embedding_Predictive_Architecture_for_One-shot_Cross-Embodiment_Imitation|Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation]]

![[assets/2605.20811_figure.png|800]]

- **arXiv**: [2605.20811](https://arxiv.org/abs/2605.20811)
- **PDF**: https://arxiv.org/pdf/2605.20811
- **详细分析**: [[20_Research/Papers/世界模型/Demo-JEPA_Joint-Embedding_Predictive_Architecture_for_One-shot_Cross-Embodiment_Imitation|Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation]]
- **作者**: Jingyang He, Guangrun Li, Jieyu Zhang, Chengkai Hou, Zhengping Che, Shanghang Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，世界模型 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

机器人模仿学习通常被理解为“复现示范动作”，但动作本身高度依赖具体机体，换一种人形机器人、机械臂或人类示范者，关节结构、运动学和动作空间都可能完全不同。现有方法往往依赖共享动作空间、手工重定向规则，或大规模多具身联合训练，成本高且在异构机体间泛化困难。这篇工作值得关注之处在于，它把示范重新解释为“未来目标的隐式规格说明”：机器人不必复刻对方怎么动，而是要推断对方试图实现什么状态。

#### 方法概述和架构

论文提出 Demo-JEPA，将跨具身模仿表述为共享预测表征空间中的“潜在目标条件规划”。方法包含一个基于 JEPA 的世界模型和一个 Dreamer Predictor：前者用目标机器人的交互经验学习动作条件动态，编码当前观测并在潜空间预测未来状态；后者接收目标机器人当前观测以及来源示范中的一对视觉帧，推断出与目标机体兼容的未来潜在轨迹/子目标。推理时，Dreamer Predictor 先把源示范翻译成潜在子目标，再由目标端世界模型通过 CEM 搜索动作序列，使预测的潜在轨迹逼近该子目标。整个流程不依赖动作级对应关系，也不需要源目标共享动作空间，只使用源端视觉示范和目标端自身交互数据。训练上，文中采用分阶段方案：先训练动作条件世界模型，再训练潜在目标预测器，随后进行动作协同训练以增强规划能力。

#### 实验结果分析

作者在 RLBench 仿真任务以及真实机器人操作任务上进行了验证，覆盖了已见任务的行为对齐、未见动作的跨具身桥接，以及未见配置的零样本泛化等更强分布偏移场景。结果表明，Demo-JEPA 在性能上可匹配专门设计的域内规划器，并且在任务或机体配置变化更大的情况下，相比先前方法展现出更强的鲁棒性与泛化能力。节选文本中未给出具体数值，但明确指出其优势会随着分布偏移增大而更加明显。

<details>
<summary>完整摘要</summary>

机器人模仿学习通常被视为对示范动作的复现，但动作本身具有明显的具身特异性。当示范来自不同形态、运动学结构或动作空间的人类或机器人时，这种以动作为中心的观点往往需要共享动作空间、启发式重定向，或大规模多具身联合训练。我们则将示范视为未来目标的隐式规格说明：目标智能体应当推断示范者想要实现什么状态，而不是示范者如何执行动作。为此，我们提出 Demo-JEPA，这是一个跨具身模仿框架，用于将示范意图与具身相关的执行过程解耦。Demo-JEPA 基于 JEPA 世界模型，将来源视觉示范转换为目标机器人可用的、共享预测表示空间中的未来潜在轨迹。随后，目标机器人把这些潜在轨迹作为子目标，并在自身学习到的前向动力学下通过规划来实现它们。由于 Demo-JEPA 避免了动作级对应关系，并且只需要视觉示范以及目标机器人自身的交互经验，因此它能够在异构具身之间实现灵活的模仿。我们在 RLBench 和真实世界操作任务上的实验表明，Demo-JEPA 的表现可与专门的域内规划器相当，并且能够推广到未见任务和未见具身配置，而先前方法在这些场景下会失效。

</details>

---

### [[20_Research/Papers/具身智能/Q-SpiRL_Quantum_Spiking_Reinforcement_Learning_for_Adaptive_Robot_Navigation|Q-SpiRL: Quantum Spiking Reinforcement Learning for Adaptive Robot Navigation]]

![[assets/2605.20801_figure.png|800]]

- **arXiv**: [2605.20801](https://arxiv.org/abs/2605.20801)
- **PDF**: https://arxiv.org/pdf/2605.20801
- **详细分析**: [[20_Research/Papers/具身智能/Q-SpiRL_Quantum_Spiking_Reinforcement_Learning_for_Adaptive_Robot_Navigation|Q-SpiRL: Quantum Spiking Reinforcement Learning for Adaptive Robot Navigation]]
- **作者**: Mohamed Khair Altrabulsi, Nouhaila Innan, Alberto Marchisio, Muhammad Kashif, Muhammad Shafique
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 3.7（加权：具身智能 1.5，大模型 0.1，强化学习 1，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

面向动态环境中的机器人导航，智能体不仅要准确到达目标点，还要在存在静态与动态障碍物时保持轨迹高效、平稳且稳定，这对具身智能和移动机器人部署都非常关键。传统表格型Q-learning在状态空间变大时难以扩展，而常规深度强化学习又往往依赖较高的训练开销与算力，不利于资源受限的机器人平台。与此同时，脉冲神经网络（SNN）具备事件驱动、时序处理和潜在低功耗优势，量子机器学习则提供了新的特征变换与表示能力，因此这篇工作值得关注的地方在于：它尝试把“脉冲时序表示”和“变分量子特征变换”结合到导航强化学习中，探索是否能在效率、稳定性与成功率之间取得更好的折中。

#### 方法概述和架构

论文提出 Q-SpiRL（Quantum Spiking Reinforcement Learning）框架，用于障碍感知的机器人导航，并在统一训练与评测流程下比较五类智能体：tabular Q-learning、经典MLP、经典SNN、量子增强MLP（QMLP）和量子增强SNN（QSNN）。其中 QSNN 是核心模型，它先将离散导航状态转为脉冲驱动的时序/发放率表示，再通过参数化量子电路完成特征变换，最后进行动作价值估计。整个任务被建模为二维网格世界中的强化学习问题，智能体从固定起点出发，在五个离散动作下控制转向并前进，目标是在避开障碍物的同时抵达终点。训练完成后，论文将各个策略转换为显式Q表，并在测试阶段采用确定性的贪婪动作选择，以减少随机性并保证公平比较。评测指标包括 success rate、success-weighted path length、path length 和 turn rate，用于同时衡量任务成功率、路径效率与运动平滑性。

#### 实验结果分析

实验在三种规模递增的网格世界环境中进行，分别是 20×20、30×30 和 40×40，并同时包含静态与动态障碍物；对比基线覆盖了表格法、经典神经网络、脉冲网络以及量子增强网络。结果显示，QSNN 在整体上取得了最佳权衡，在任务完成、轨迹效率和运动平滑性之间表现最优，在最困难设置下 success rate 最高可达 99%。论文还在 IBM 量子硬件上验证了该混合策略的可执行性，说明其不仅适用于模拟环境，也具备真实量子设备部署的可行性。可见文本未给出更细的消融数值，但从描述看，量子特征变换与脉冲时序表示的结合是性能优势的关键来源。

<details>
<summary>完整摘要</summary>

动态环境中的自适应机器人导航需要能够可靠到达目标、同时生成高效且稳定轨迹的策略。本文提出 Q-SpiRL，一种用于障碍感知机器人导航的量子脉冲强化学习框架。该框架设计并评估了五类智能体：表格型Q-learning、经典MLP、经典SNN、量子增强MLP（QMLP）以及量子增强脉冲神经网络（QSNN）。尽管所有模型都在统一的训练与评测流程下实现，QSNN 是本文关注的核心架构，因为它将基于脉冲的时序处理与变分量子特征变换结合起来。实验在三个规模逐步增大的网格世界环境中进行，分别为 20×20、30×30 和 40×40，并同时设置静态与动态障碍物。性能通过确定性推理下的成功率、成功加权路径长度、路径长度和转向率来评估。结果表明，QSNN 在任务完成率、轨迹效率和运动平滑性之间取得了最佳整体折中，在最具挑战性的设置中成功率最高可达 99%，同时仍保持较高的路径效率。在 IBM 量子硬件上的执行进一步证明了所提出的混合策略在真实设备条件下部署的可行性。

</details>

---

### [[20_Research/Papers/机器人/CMC-Opt_Constraint_Manifold_with_Corners_for_Inequality-Constrained_Optimization|CMC-Opt: Constraint Manifold with Corners for Inequality-Constrained Optimization]]

![[assets/2605.20796_figure.png|800]]

- **arXiv**: [2605.20796](https://arxiv.org/abs/2605.20796)
- **PDF**: https://arxiv.org/pdf/2605.20796
- **详细分析**: [[20_Research/Papers/机器人/CMC-Opt_Constraint_Manifold_with_Corners_for_Inequality-Constrained_Optimization|CMC-Opt: Constraint Manifold with Corners for Inequality-Constrained Optimization]]
- **作者**: Yetong Zhang, Frank Dellaert
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

机器人优化与轨迹规划中经常同时存在等式约束和不等式约束，例如动力学可行性、接触条件、关节限位、碰撞避免和执行器约束等。现有罚函数、增广拉格朗日、SQP 和内点法等方法，要么依赖较难调的惩罚权重，要么在强非线性场景下数值稳定性和全局收敛性较差。本文关注的价值在于：它尝试把“约束”直接纳入搜索空间的几何结构中，从而在具身智能与机器人规划中更自然地处理严格可行性问题。

#### 方法概述和架构

论文提出 CMC-Opt（Constraint Manifold with Corners）框架，将同时满足非线性等式约束和不等式约束的可行域建模为“带角点的约束流形”。核心做法是先用 factor graph 表示原始优化问题，把与同一约束连通分量相关的变量与约束隔离出来，再把这些分量转换为 CMC 上的无约束优化问题。随后，作者为 CMC 定义了局部参数化、切空间、函数在 CMC 上的微分以及 retraction；其中在角点处，切空间不再是普通线性空间，而是由活跃不等式约束形成的凸锥。优化阶段则在每次迭代中先计算目标函数在 CMC 上的梯度近似，再通过 retraction 把更新后的点投影回可行域，从而扩展 Riemannian gradient descent 以适配带边界和角点的结构。

#### 实验结果分析

论文在一个大规模 kinodynamic planning 任务上验证了方法的鲁棒性，实验重点是生成动力学可行轨迹。作者报告称，CMC-Opt 能够成功得到标准方法失败时无法获得的可行解，并在四足机器人跳跃轨迹示例中生成更平滑、更自然的运动。对比图显示，罚函数方法会出现明显的 collocation leakage，导致轨迹在物理上不可行；而 CMC-Opt 能更好地维持约束满足。可见文本未给出具体数值，但结论明确指向其在可行性与稳定性上的优势。

<details>
<summary>完整摘要</summary>

我们提出一种基于流形的框架，用于处理机器人中常见的带等式约束和不等式约束的优化问题。该方法将原始问题直接转换为定义在受约束状态空间上的无约束优化问题。为此，我们引入“带角点的约束流形”来表示满足混合非线性等式与不等式约束的状态空间，并进一步扩展流形优化算法，使其能够作用于这种新的拓扑结构。我们在一个大规模 kinodynamic 规划问题中展示了该框架的强大能力与鲁棒性，成功生成了动力学可行的轨迹，而标准方法在该任务上失败了。

</details>

---

### [[20_Research/Papers/具身智能/VLA-REPLICA_A_Low-Cost,_Reproducible_Benchmark_for_Real-World_Evaluation_of_Vision-Language-Action_Models|VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models]]

![[assets/2605.20774_figure.png|800]]

- **arXiv**: [2605.20774](https://arxiv.org/abs/2605.20774)
- **PDF**: https://arxiv.org/pdf/2605.20774
- **详细分析**: [[20_Research/Papers/具身智能/VLA-REPLICA_A_Low-Cost,_Reproducible_Benchmark_for_Real-World_Evaluation_of_Vision-Language-Action_Models|VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models]]
- **作者**: Alex S. Huang, Jiahui Zhang, Shiqing Tang, Yu Xiang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.5（加权：具身智能 3，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

视觉-语言-动作（VLA）模型被认为是通用机器人操作的重要方向，但其真实世界评测长期受制于缺少便捷、可复现且标准统一的基准。现有仿真基准难以反映真实环境中的物理复杂性，而真实世界基准又常常依赖昂贵硬件、集中式评测流程，或任务种类过于单一。作者指出，目前仍缺少一个既真实落地、又能在不同实验室之间稳定复现的操作评测平台，因此这项工作值得关注。

#### 方法概述和架构

论文提出 VLA-REPLICA，这是一个面向真实世界 VLA 评测的低成本、可复现基准。该基准基于现成组件搭建，包括低成本 SO-101 机械臂、RGB-D 相机、RGB 摄像头以及受控光箱环境，力求让不同实验室都能快速搭建出近似一致的测试场景。方法上同时设计了硬件标准化流程和环境重建流程：一方面通过相机视角叠加、AprilTag 标定与统一的工作空间布置来固定观测与场景；另一方面把 SO-101 的原始舵机编码动作归一化为统一动作空间，以便不同设备之间共享示教数据与策略输出。基准包含十个真实操作任务，覆盖抓取放置、拉拽、擦拭、倒液和记忆类操作，并提供面向域内微调的小规模示范数据集。评测流程同时支持分布内（ID）和分布外（OOD）设置，前者考察少量真实数据适配能力，后者考察对物体属性、数量和任务要求变化的泛化能力。

#### 实验结果分析

作者在统一训练与评测协议下，对模仿学习方法以及多种 SOTA VLA 模型进行了实验。结果显示，这些方法在 VLA-REPLICA 上表现出不同的优势与局限，尤其能看出当前 VLA 系统在新环境适配与分布外泛化方面仍有明显挑战。论文还报告了两个独立搭建的系统上得到一致的评测结果，说明该基准具备较好的可复现性。具体成功率或其他数值指标在节选文本中未给出具体数值。

<details>
<summary>完整摘要</summary>

视觉-语言-动作（VLA）模型在通用机器人操作中展现出很强的潜力，但由于缺少可访问、可复现且一致的基准，其真实世界评测仍然受到限制。仿真基准无法捕捉真实世界的复杂性，而现有真实世界基准往往需要昂贵硬件、集中式评测，或者任务多样性有限。为此，我们提出 VLA-REPLICA，这是一个用于评测 VLA 模型的低成本、易复现的真实世界基准。该系统基于现成组件构建，可以快速组装并在不同实验室间复制，从而在世界任何地方都能提供一致的策略评测环境。VLA-REPLICA 包含一套多样化的操作任务，以及一个用于目标域适配的小规模示范数据集，并为分布内和分布外场景提供真实世界评测协议。我们在模仿学习方法和当前最先进的 VLA 模型上进行实验，揭示了模型的优势与局限；同时，两个独立构建的系统上得到一致的结果，证明了该基准的可复现性。

</details>

---

### [[20_Research/Papers/具身智能/GaussianDream_A_Feed-Forward_3D_Gaussian_World_Model_for_Robotic_Manipulation|GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation]]

![[assets/2605.20752_figure.png|800]]

- **arXiv**: [2605.20752](https://arxiv.org/abs/2605.20752)
- **PDF**: https://arxiv.org/pdf/2605.20752
- **详细分析**: [[20_Research/Papers/具身智能/GaussianDream_A_Feed-Forward_3D_Gaussian_World_Model_for_Robotic_Manipulation|GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation]]
- **作者**: Zijian Zhang, Yuqing Jiang, Qian Cheng, Si Liu, Ding Zhao, Ping Luo, Weitao Zhou, Haibao Yu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 4.0（加权：具身智能 2.1，世界模型 0.6，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

在语言条件下的机器人操作中，VLA策略虽然能借助预训练视觉语言模型获得较强的语义理解与泛化能力，但训练通常主要依赖行为克隆，对3D几何、稠密视觉结构以及短时环境变化缺乏显式监督。这会导致抓取点偏移、接触位置不准等物理执行误差，尤其在需要精细空间定位的任务中更明显。作者因此关注如何把机器人轨迹中的密集空间-时间信息转化为可学习的世界模型监督，同时又不增加测试时闭环控制的推理开销。

#### 方法概述和架构

论文提出 GaussianDream，一个用于机器人操作的前馈式3D Gaussian世界模型插件。方法在训练阶段引入一个时序3D感知编码器，从当前观测、短时间历史帧、语言指令和机器人状态中提取 GaussianDream prefix；该 prefix 再分别送入两个辅助解码头：当前 Gaussian 重建头用于恢复可渲染的当前场景，未来 Gaussian 预测头用于根据时间跨度预测后续几何变化。训练时，模型通过当前与未来的 RGB 渲染、深度以及伪3D scene flow 进行密集监督，把普通机器人轨迹转化为结构化的空间-时间学习信号。推理时则删除全部辅助解码头，只保留学到的 prefix 作为策略条件，直接驱动动作生成，从而避免测试时的 Gaussian 解码、渲染、视频 rollout 或额外规划。

#### 实验结果分析

作者在 LIBERO、RoboCasa Human-50 和真实机器人任务上进行了评测，并与现有 VLA、3D增强策略和世界模型方法对比。结果显示，GaussianDream 在多个空间要求较高的任务上表现强劲且具有竞争力：LIBERO 平均成功率达到 98.4%，RoboCasa Human-50 达到 52.6%，真实世界评测达到 50.0%。正文节选还指出，消融实验验证了各组件与监督信号的作用，并显示预测式未来几何与可执行控制之间具有较好的时空对齐。

<details>
<summary>完整摘要</summary>

视觉-语言-动作（VLA）策略通过将预训练视觉语言模型中的语义先验迁移到动作生成中，推动了语言条件下的机器人操作。然而，标准的动作模仿训练通常对3D几何、稠密视觉结构以及短时环境演化提供的显式监督有限，而这些对于物理上精确的操作至关重要。为此，我们提出 GaussianDream：一种前馈式3D Gaussian世界模型插件，它将机器人轨迹转化为结构化的空间-时间监督。其核心思想是在训练过程中将当前 Gaussian 重建与带时间跨度条件的未来 Gaussian 预测耦合起来，迫使一个紧凑的时空前缀能够被解码为可渲染的3D Gaussian状态。这样就能在不需要测试时 Gaussian 解码的情况下，获得稠密 RGB 渲染、深度以及伪3D scene flow 监督。在推理阶段，GaussianDream 会丢弃所有辅助解码头，仅保留学到的前缀来条件化动作生成，从而在闭环控制中避免渲染、视频 rollout 或额外规划。LIBERO、RoboCasa Human-50 以及真实机器人任务上的实验表明，该方法性能强且极具竞争力，在 LIBERO 上取得 98.4% 的平均成功率，在 RoboCasa Human-50 上取得 52.6%，在真实世界评测中取得 50.0%。

</details>

---

### [[20_Research/Papers/机器人/Conflict-Aware_Active_Perception_and_Control_in_3D_Gaussian_Splatting_Fields_via_Control_Barrier_Functions|Conflict-Aware Active Perception and Control in 3D Gaussian Splatting Fields via Control Barrier Functions]]

![[assets/2605.20566_figure.png|800]]

- **arXiv**: [2605.20566](https://arxiv.org/abs/2605.20566)
- **PDF**: https://arxiv.org/pdf/2605.20566
- **详细分析**: [[20_Research/Papers/机器人/Conflict-Aware_Active_Perception_and_Control_in_3D_Gaussian_Splatting_Fields_via_Control_Barrier_Functions|Conflict-Aware Active Perception and Control in 3D Gaussian Splatting Fields via Control Barrier Functions]]
- **作者**: Amirhossein Mollaei Khass, Athanasios Cosse, Vivek Pandey, Nader Motee
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

在未知或不确定环境中，机器人既要安全避障，又要主动选择“最有信息量”的视角来更新3D地图，这两类目标往往天然冲突：越有信息的观测位姿，通常越靠近未探索或高不确定区域，也意味着更高碰撞风险。本文聚焦基于3D Gaussian Splatting（3DGS）的机器人主动感知与控制问题，试图解决“为了看得更清楚而更危险、为了更安全而更看不清”的矛盾。相比已有3DGS安全导航工作主要关注避障，本文进一步把感知目标显式纳入安全控制，因此更贴近具身智能中的真实闭环决策需求。

#### 方法概述和架构

作者提出一个面向3DGS场景的“冲突感知”主动感知与控制框架，核心是将安全与感知分别写成可优化的约束并统一进一个CBF-QP。安全部分用基于AV@R碰撞风险度量构造的Control Barrier Function（CBF），把几何不确定性转化为对控制输入的硬约束，从而保证安全集的前向不变性。感知部分先用3DGS的渲染/重建模型计算Next Best View的Expected Information Gain（EIG），再引入风险感知的掩膜机制，只对与规划轨迹相关且风险更高的区域进行信息增益评估。除此之外，论文还设计了“perception barrier functions”，分别从空间运动和角度朝向两个层面，引导相机朝局部信息上升方向对齐。最终通过一个统一的安全关键、感知感知的二次规划（quadratic program）求解控制量：安全约束保持为硬约束，而感知约束通过松弛变量放宽，以避免安全与感知目标彼此不可行。

#### 实验结果分析

论文在仿真中验证了该方法，相比现有基于3DGS的方案，同时提升了安全性和信息获取能力。正文节选中提到的实验包括双积分器安全屏障、unicycle动力学以及带角度感知约束的unicycle动力学等案例，用于展示该方法在不同控制模型下对安全约束和感知约束的协调能力。可见文本未给出具体数值，但作者明确指出该方法在碰撞风险控制与主动观测质量上均优于对比方法。

<details>
<summary>完整摘要</summary>

主动感知在不确定环境中要求机器人在安全导航的同时获取有信息量的观测，以降低地图不确定性。这两个目标天然冲突，因为信息量高的观测位姿往往位于不确定区域附近，而这些区域也伴随更高的碰撞风险。为应对这一挑战，我们为在由3D Gaussian Splatting（3DGS）表示的环境中运行的机器人系统开发了一种冲突感知的主动感知与控制框架。安全性通过由Average Value-at-Risk（AV@R）碰撞风险度量导出的Control Barrier Function（CBF）来保证，该度量考虑了几何不确定性，并保证安全集的前向不变性。为了提升感知效果，我们提出一种风险感知的Expected Information Gain（EIG）形式来选择下一最佳视角，并引入感知屏障函数，使相机朝向与局部信息上升方向对齐。为了得到一个可处理的统一形式来协调这些相互冲突的安全与感知目标，我们提出一个统一的、具有安全关键性且感知感知的二次规划：将安全作为硬约束执行，而通过松弛变量放宽感知约束。仿真结果表明，与现有基于3DGS的方法相比，所提方法在安全性和信息获取两方面均有所提升。

</details>

---

### [[20_Research/Papers/机器人/Fault-Tolerant,_Rigidity-Preserving_Control_of_Inflatable_Truss_Robots|Fault-Tolerant, Rigidity-Preserving Control of Inflatable Truss Robots]]

![[assets/2605.20561_figure.png|800]]

- **arXiv**: [2605.20561](https://arxiv.org/abs/2605.20561)
- **PDF**: https://arxiv.org/pdf/2605.20561
- **详细分析**: [[20_Research/Papers/机器人/Fault-Tolerant,_Rigidity-Preserving_Control_of_Inflatable_Truss_Robots|Fault-Tolerant, Rigidity-Preserving Control of Inflatable Truss Robots]]
- **作者**: James Wade, Isaac Weaver, Mihai Stanciu, Nathan Usevitch
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

可充气桁架机器人具有高强重比、可大幅变形和可重构等特点，适合用于远程基础设施部署、野外机器人和航天场景。但这类结构的执行器紧耦合，一旦电机或滚轮失效，机器人可达工作空间、可操控性和轨迹跟踪性能都会明显下降。论文聚焦于二维 isoperimetric truss 机器人在执行器退化条件下的可靠控制问题，核心目标是在故障发生后仍尽量保持结构刚性与任务能力，因此具有较强的工程价值。

#### 方法概述和架构

作者提出了一套面向故障容错与刚性保持的控制框架 Fault-Tolerant, Rigidity-Preserving Control of Inflatable Truss Robots。方法首先在原有基于运动学的二次规划（QP）上加入故障约束：当某些滚轮电机失效时，通过线性等式约束显式强制这些失效执行器的速度为零，从而支持任意组合的电机故障。其次，引入离散时间控制屏障函数（DTCBF）约束，把结构刚性作为安全条件嵌入优化问题中，在离散采样控制下保证系统不进入奇异、失稳区域。最后，系统还结合板载编码器反馈与基于正向运动学的状态估计器，实现闭环位置控制；控制流程是先根据故障状态与当前构型更新运动学模型，再求解带故障约束和刚性约束的优化问题，输出修正后的电机命令。

#### 实验结果分析

作者在二维 6 执行器的 isoperimetric truss 测试平台上进行了仿真和硬件实验。结果显示，在单电机失效情况下，方法可保持超过 69% 的工作空间，并且闭环控制相比开环/基线方案将轨迹跟踪精度提升超过 25%。节选文本表明论文还评估了滚轮故障和节点故障导致的运动学退化、DTCBF 对刚性维持的作用，以及闭环控制对位置精度的影响；更细的对比数值在给出的文本中未完全展开。

<details>
<summary>完整摘要</summary>

可充气的等周桁架机器人之所以能够适应不同任务和环境，是因为它们具有较高的强重比、能够显著改变自身形状，并且可以重构为多种不同构型。然而，在实际运行环境中，电机失效会严重限制其工作能力，如果不加以处理，系统性能会大幅下降。本文提出了一种面向可充气桁架机器人的容错控制框架，即使在电机失效的情况下也能维持功能，并通过三项关键贡献加以实现。首先，我们扩展了运动学优化，使其能够处理任意组合的电机失效，通过施加等式约束确保失效执行器不被使用。其次，我们引入离散时间控制屏障函数（DTCBF）约束，在数学上保证结构刚性，同时最大化工作空间利用率，这对于离散时间控制下可靠运行的桁架机器人而言至关重要。第三，我们利用板载编码器反馈和基于正向运动学的状态估计器实现闭环位置控制，从而在存在扰动时提高位置精度。我们通过二维等周桁架测试平台上的仿真和硬件实验验证了该方法。对于具有 6 个执行器的二维构型，我们证明了在单电机失效下可保持超过 69% 的工作空间，并且闭环控制可使跟踪精度提升超过 25%。这些结果为在执行能力退化条件下运行的更稳健、更具韧性的等周桁架机器人奠定了基础。

</details>

---

### [[20_Research/Papers/具身智能/Enhancing_Graph-Based_SLAM_in_GNSS-Denied_environments_by_leveraging_leg_odometry|Enhancing Graph-Based SLAM in GNSS-Denied environments by leveraging leg odometry]]

![[assets/2605.20484_figure.png|800]]

- **arXiv**: [2605.20484](https://arxiv.org/abs/2605.20484)
- **PDF**: https://arxiv.org/pdf/2605.20484
- **详细分析**: [[20_Research/Papers/具身智能/Enhancing_Graph-Based_SLAM_in_GNSS-Denied_environments_by_leveraging_leg_odometry|Enhancing Graph-Based SLAM in GNSS-Denied environments by leveraging leg odometry]]
- **作者**: Léon Perruchot-Triboulet, Luc Jaulin, Kai Xiao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: EmbodiedAI

#### 研究背景与动机

在GNSS受限或完全不可用的环境中，四足机器人要实现稳定自主导航仍然很困难，尤其是依赖LiDAR的SLAM系统在地形起伏小、垂直结构稀疏或场景重复时，容易出现高度方向漂移。论文指出，LIO-SAM这类图优化式LiDAR-IMU SLAM在没有GNSS锚点时，最典型的失效模式就是累计的z轴误差不断放大，最终导致地图“包层”或直接发散。由于四足机器人本身就会在步态控制中计算腿部里程计，作者认为这类本体感知信息可以作为一种轻量、无需新增传感器的垂直约束，因此值得在SLAM中重新利用。

#### 方法概述和架构

作者在LIO-SAM的因子图框架上加入了一条并行的运动学分支，称为leg odometry lane，并让它与原有的LiDAR-IMU分支同时优化。该分支直接复用机器人已有的腿部正运动学/里程计输出，将其按LiDAR关键帧时间对齐后，构建连续位姿因子与高度先验因子，用于描述机器人相对地面的垂向运动。两条分支通过一个身份相对位姿约束耦合起来，但该约束采用选择性噪声模型：在z方向上赋予较强信任，而在平面位置和姿态上保留较大不确定性，从而让腿里程计主要充当“垂直锚点”，不干扰LiDAR分支在水平定位上的主导作用。最终输出仍来自LiDAR-IMU分支的位姿节点，因而该方法更像对原SLAM的非侵入式正则化，而不是对各传感器的对称融合。

#### 实验结果分析

作者在Linxai D50 四足平台上进行了两组室外闭环实验，数据集分别是 Factory 和 CocoPark，总里程超过1公里。实验对比的基线是未加入GNSS的LIO-SAM，评价主要使用闭环误差和轨迹是否收敛；结果显示，在 Factory 上，基线的高度漂移超过30米，而加入腿里程计后降到约20厘米，水平闭环误差约为2米。CocoPark 场景中，基线在完成闭环前就发散崩溃，而改进方法可以稳定收敛，全程完成并将高度误差控制在约30厘米；文中还指出，该方法没有明显牺牲水平精度，并且能缓解ICP前端因高度漂移带来的不稳定。

<details>
<summary>完整摘要</summary>

GNSS受限环境下的自主导航仍然是腿足机器人面临的核心挑战，尤其是在几何结构稀疏或重复的场景中，LiDAR等外部感知传感器容易出现高度漂移。我们提出一种因子图架构，在LIO-SAM框架上增加一条由本体感知腿里程计驱动的并行运动学分支，并通过带选择性噪声模型的身份相对位姿约束，将其与主LiDAR-惯性分支耦合。该方法应用于Linxai D50 四足平台，在两条总长度超过一公里的室外闭环轨迹上进行验证，结果将高度漂移从30米以上降低到30厘米以内，并且在一个基线管线完全失效的场景中实现了收敛。这些结果表明，机器人本体上已经为步态控制计算好的本体感知数据，可以作为GNSS缺失条件下SLAM系统一个轻量而有效的垂直锚点。

</details>

---

### [[20_Research/Papers/强化学习/Spacetime_Optimal-Transport_Attention_for_Visuo-Haptic_Imitation_Learning_of_Contact-Rich_Manipulation|Spacetime Optimal-Transport Attention for Visuo-Haptic Imitation Learning of Contact-Rich Manipulation]]

![[assets/2605.20433_figure.png|800]]

- **arXiv**: [2605.20433](https://arxiv.org/abs/2605.20433)
- **PDF**: https://arxiv.org/pdf/2605.20433
- **详细分析**: [[20_Research/Papers/强化学习/Spacetime_Optimal-Transport_Attention_for_Visuo-Haptic_Imitation_Learning_of_Contact-Rich_Manipulation|Spacetime Optimal-Transport Attention for Visuo-Haptic Imitation Learning of Contact-Rich Manipulation]]
- **作者**: Yue Feng, Weicheng Huang, I-Ming Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

紧配插入、连接器对接、表面擦拭和抛光等接触丰富型操作，是机器人在工业装配与服务场景中的核心能力，但这类任务同时受到接触动力学突变、部分可观测以及安全约束的影响，数据驱动控制很容易失稳。单一模态通常不够：视觉更适合在接触前提供全局场景信息，力/力矩反馈在接触后用于调节交互，而位姿信息则提供稳定的运动学骨架。现有模仿学习方法多采用单模态或双模态融合，三模态方法也往往直接套用通用注意力模块，缺少对任务相关区域应如何分配注意力的结构性先验，因此在杂乱、遮挡和光照变化下容易受干扰。

#### 方法概述和架构

论文提出 Spacetime Optimal-Transport Attention（SO-TA），作为面向视觉-触觉/力觉-位姿三模态模仿学习的融合骨干。其核心思想是用带熵正则的最优传输（OT）对齐，替代传统 softmax 注意力：将由力-位姿信息生成的子查询与视觉patch做匹配，并通过显式的边缘约束控制注意力质量的分布。整体流程中，力和位姿先经过 MLP 编码并投影为条件 token，再与图像序列特征一起进入 SO-TA；SO-TA 输出时序对齐的融合表示后，送入帧内模态融合模块和时间 Transformer，形成可供后续策略使用的 fused 表征。动作生成部分采用 diffusion-based sequence policy，以观察窗口为条件，预测未来一段 pose-action chunk；在线推理时使用较少步数的反向去噪实现低延迟滚动控制。论文还给出了 OT 生成的 patch heatmap 以及 leave-one-out 模态影响比例，用于解释不同阶段各模态的贡献。

#### 实验结果分析

作者在三项真实机器人任务上评估了该方法：紧配插入（tight peg-in-hole）、BCM wiring-connector 插入以及曲面标记擦除，并与拼接基线和 force–pose-conditioned cross-attention 基线比较。根据摘要中的结果，在约 200 次 rollout/条件下，SO-TA 在 tight peg-in-hole 上达到 100% 成功率，高于同容量的 cross-attention 基线 93%；在光照变化、干扰物和部分遮挡扰动下仍保持 82.5% 成功率，而拼接基线降至 43.5%。正文节选还指出，OT 导出的注意力热图具有阶段一致性，说明该方法不仅提升性能，也增强了可解释性；若需要更细的消融结论，节选中可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

紧配插入、连接器对接、抛光以及贴合表面的擦拭等接触丰富型操作之所以对数据驱动控制器仍然困难，是因为这类任务同时耦合了不连续的接触动力学、部分可观测性以及严格的安全约束。没有任何单一传感模态足以胜任：视觉在接触前提供全局上下文，力/力矩（F/T）反馈在接触后主导交互，而本体感觉位姿则提供一致的运动学骨架。现有大多数面向接触丰富任务的模仿学习策略只使用单模态或双模态信号，而少数三模态融合方法通常采用现成的注意力模块，并没有关于注意力质量应如何分配到任务相关区域的显式先验。我们提出 Spacetime Optimal-Transport Attention（SO-TA），一种三模态融合骨干，用带熵正则的最优传输（OT）对齐，替代 softmax 归一化的patch注意力，将力-位姿导出的子查询与视觉patch进行匹配。显式的边缘约束作为接触丰富任务中的结构化归纳偏置，促进与条件状态相一致的空间选择，并且在光照变化、干扰物以及部分遮挡下保持稳定。SO-TA 与一个基于扩散的序列策略相结合，将观察窗口映射为位姿-动作块。我们在三个真实机器人任务上评估 SO-TA：紧配插入装配、BCM wiring-connector 插入以及曲面标记擦除。在每种条件下约 200 次 rollout 的设置中，SO-TA 在紧配插入任务上达到 100% 成功率，相比同等容量的 cross-attention 基线为 93%；在光照、干扰物和部分遮挡扰动下仍保持 82.5% 的成功率，而拼接基线降至 43.5%。基于 OT 的patch热图以及逐一去除模态后的影响比例，为不同阶段提供了可解释的诊断信息。

</details>

---

### [[20_Research/Papers/机器人/Multi-Week,_In-Class_Deployments_of_Telepresence_Robots_With_Four_Homebound_K-12_Students_Benefits,_Challenges,_and_Recommendations|Multi-Week, In-Class Deployments of Telepresence Robots With Four Homebound K-12 Students: Benefits, Challenges, and Recommendations]]

![[assets/2605.20431_figure.jpg|800]]

- **arXiv**: [2605.20431](https://arxiv.org/abs/2605.20431)
- **PDF**: https://arxiv.org/pdf/2605.20431
- **详细分析**: [[20_Research/Papers/机器人/Multi-Week,_In-Class_Deployments_of_Telepresence_Robots_With_Four_Homebound_K-12_Students_Benefits,_Challenges,_and_Recommendations|Multi-Week, In-Class Deployments of Telepresence Robots With Four Homebound K-12 Students: Benefits, Challenges, and Recommendations]]
- **作者**: Matthew Rueben, Rhianna Lee, Thomas R. Groechel, Hengzhi Chen, Haemi Lee, Gisele Ragusa, Maja J. Matarić
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

K-12 学生因长期缺课会面临认知和社交发展风险，而传统的家庭辅导、线上学习虽然能维持部分教学连续性，却难以提供课堂中的同伴互动、师生交流与参与感。移动远程 присутств/临场系统（telepresence robots）有望让居家或住院学生在课堂中获得“具身”参与能力，不仅能看见听见课堂，还能在教室中移动、调整视角并主动互动。本文聚焦这一真实教育场景下的长期部署问题，关注机器人在噪声、拥挤、课堂管理和同伴关系中的实际可用性，因此具有较强的应用价值与落地意义。

#### 方法概述和架构

论文围绕 4 名因健康或心理原因无法长期到校的 K-12 学生，开展了为期多周的课堂内 telepresence robot 部署研究。研究采用案例研究与跨案例对比相结合的方法，共收集 15 次访谈，并结合音视频记录分析学生在系统使用、课堂临场感以及与同学和老师互动中的体验。作者将分析重点分为三部分：一是系统可用性与需求，二是远程“在场”带来的参与感、自我意识与课堂融入，三是社交关系、注意力获取与回避、以及课堂活动参与。整体流程包括部署前的初始设置与训练、课堂中的持续运行与支持、部署后的访谈收集，以及对不同个案的质性编码和归纳。

#### 实验结果分析

结果显示，所有参与者都从移动远程到课中获得了某些共同收益，例如更强的自主性、社交连接、焦虑缓解、疲劳管理、安全感和自我倡导能力，但不同学生的收益组合存在明显差异。研究还识别出若干关键挑战，包括听不清/说不清、看不见/被看见、机器人在教室中移动困难，以及课堂管理和同伴不友好互动等问题；这些问题分别指向系统设计改进和部署流程优化。实验环境为四所不同学校、四个多周真实课堂部署；基线、量化指标及对照实验在节选中未详细给出，可见文本未给出具体数值。作者据此提出了面向真实校园部署的建议，强调要确保远程学生能被纳入课堂活动、对教师负责，并受到同学尊重。

<details>
<summary>完整摘要</summary>

K-12 教育阶段学生因长期缺课而缺席大量学校课程，已知会使其认知和社交发展面临风险。家庭教学和在线学习等替代方案较为常见，但它们无法在课堂中提供与同伴和教师足够的互动。移动远程临场系统，或称 telepresence robots（远程 присутств机器人），对于居家无法到校的学生而言具有潜力，因为它们除了提供视频会议式的实时参与外，还能提供具身性和移动能力。然而，要让 telepresence robots 满足居家学生在 K-12 课堂情境中的复杂需求，仍需要更多研究。我们报告了四次为期多周的部署结果，这些部署中，居家 K-12 学生通过 telepresence robots 参与课堂。我们共进行了 15 次访谈，对居家学生的体验进行了记录，并以质性方式作为案例研究进行分析。参与学生及其部署情境在多个维度上彼此不同；尽管所有参与者都享受到了一些移动远程到课带来的共同收益，但每位参与者也都体验到了独特的好处。与听觉、视觉以及在教室中移动机器人相关的一些挑战表明，telepresence 系统的设计仍需改进。另一些挑战则提示了课堂部署管理的优先事项，例如需要确保远程学生被纳入课堂活动、对教师负责，并受到同学的尊重。基于该研究的洞见，我们提出了适用于类似场景下真实世界部署流程的建议。

</details>

---

### [[20_Research/Papers/机器人/Scalable_Multi-robot_Motion_Planning_via_Hierarchical_Subproblem_Expansion_and_Workspace_Decomposition_Refinement|Scalable Multi-robot Motion Planning via Hierarchical Subproblem Expansion and Workspace Decomposition Refinement]]

![[assets/2605.20395_figure.png|800]]

- **arXiv**: [2605.20395](https://arxiv.org/abs/2605.20395)
- **PDF**: https://arxiv.org/pdf/2605.20395
- **详细分析**: [[20_Research/Papers/机器人/Scalable_Multi-robot_Motion_Planning_via_Hierarchical_Subproblem_Expansion_and_Workspace_Decomposition_Refinement|Scalable Multi-robot Motion Planning via Hierarchical Subproblem Expansion and Workspace Decomposition Refinement]]
- **作者**: Isaac Ngui, Courtney McBeth, James D. Motes, Marco Morales, Nancy M. Amato
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

多机器人运动规划要在保证机器人彼此不碰撞、且不与环境障碍冲突的前提下，为多个移动机器人同时生成可执行轨迹，广泛应用于仓储调度、搜索救援等场景。现有方法面临一个核心矛盾：联合搜索所有机器人构成的配置空间虽然协调性强，但计算开销极大；而完全解耦的规划虽然快，却容易留下难以消解的冲突。本文值得关注之处在于，它尝试用工作空间的层次化表示来提供“足够的协调”，从而尽量避免昂贵的联合配置空间搜索。

#### 方法概述和架构

论文提出 CIPHER（Coordinated Incremental Planning with Hierarchical Expansion and Refinement），是一种面向多移动机器人、同时兼顾几何规划与动力学约束的混合式规划方法。方法首先将共享工作空间做区域分解，并在高层用 MAPF（如 CBS）为每个机器人计算无冲突的区域序列，输出的是机器人应依次经过的区域路径，而不是直接在联合状态空间里搜索。随后，每个机器人在低层基于自己的区域路径进行引导式连续空间规划，生成满足动力学约束的具体轨迹，同时将已规划机器人的轨迹视为动态障碍。与以固定分辨率分解不同，CIPHER 在检测到多个机器人需要经过同一区域时，会进行层次化冲突消解：要么进一步细化该区域的工作空间分解，要么进行空间扩张，将原本耦合的子问题拆成更小、彼此解耦的配置空间问题。整个流程体现为“高层区域协调 + 低层引导规划 + 冲突触发的自适应细化/扩张”，以尽量减少进入高维联合空间的次数。

#### 实验结果分析

实验在多种工作空间环境中验证了方法，包括空旷环境、房间环境以及随机障碍环境，并同时评估了几何规划和 kinodynamic 规划设置。对比基线包含若干代表性的多机器人几何/动力学规划方法，如 K-CBS、db-CBS、K-ARC、WG-DaSH 等；评价重点是规划时间与求解效果。作者报告 CIPHER 的规划时间相较现有方法最高可提升一个数量级，尤其在开放空间和需要自适应协调的场景中优势更明显。节选中未给出具体数值细节，但文本明确指出其在保持协调性的同时显著降低了进入联合配置空间规划的开销。

<details>
<summary>完整摘要</summary>

多机器人运动规划的一个根本挑战，是如何在避免机器人之间发生冲突的同时，避免为机器人群搜索联合配置空间所带来的巨大计算开销。本文提出了一种面向多个移动机器人的运动规划方法，利用在工作空间分解上进行离散搜索这一思想，在规划过程中为机器人提供协调，从而使规划时间最多提升一个数量级。不同于以往工作主要利用工作空间拓扑来判断何时需要机器人协同，并随后将机器人组合到其联合配置空间中，我们进一步通过迭代细化工作空间表示，使规划器能够在更小、彼此解耦的配置空间中搜索。

多机器人系统具有广泛应用，从自动化仓储管理到搜索与救援均可见其身影。这些应用都要求进行精细的多机器人运动规划（MRMP），以避免与环境和其他机器人发生碰撞。规划时协调程度与速度之间存在权衡，尤其是在机器人数量较多且具有动力学约束时更为明显。搜索机器人团队的联合配置空间（即复合空间）虽然能够保证避碰，但由于空间规模巨大，计算成本非常高。另一方面，将问题分解处理则需要额外推理，以防止未解决的机器人间冲突。现有方法已经探索使用引导信息，通常由工作空间表示提供，以加速 MRMP。先前工作利用采样引导来偏向于配置空间中的高质量区域；一些规划器则利用协调引导，在规划中判断何时需要把机器人组合到同一个配置空间。通常，这一判断由工作空间的拓扑骨架来指示；骨架是嵌入式图结构，边表示工作空间中的自由区域。骨架在狭窄通道环境中对运动规划器很有帮助，但在开放环境中表现较弱，因此本文考虑采用区域分解，以使方法在开放空间中也具有鲁棒性。这类引导虽然降低了提供协调时的计算负担，但在整个规划过程中，或者在无法避免机器人冲突时，仍然需要在多个机器人组成的复合空间中进行规划。

本文进一步迈出一步，通过引入“分辨率引导”来避免这一计算瓶颈；分辨率引导通过在不同分辨率下推理工作空间表示，为机器人协调提供支持。我们提出的 MRMP 方法 CIPHER（Coordinated Incremental Planning with Hierarchical Expansion and Refinement）能够自适应地细化工作空间表示的分辨率。通过在工作空间表示上引导机器人运动，我们在高层提供协调，并减少进入复合空间规划的需求。我们还认识到，可以在规划过程中对区域分解进行细化，从而利用分辨率引导。CIPHER 采用层次化搜索：先为每个机器人在工作空间表示上规划高层路径，再将这些路径转换为配置空间中的具体轨迹。当多个机器人需要经过同一区域时，我们会尝试进一步分解该区域，使机器人在工作空间表示上走向不同路径。借此，我们在高层提供机器人间协调，并减少将机器人组合到更大、计算更昂贵的配置空间中的需要。实验表明，与其他先进的几何和 kinodynamic MRMP 方法相比，我们的方法在规划时间上最多可提升一个数量级。我们的贡献包括：1）CIPHER，一种混合式多机器人运动规划算法，它在区域分解上进行搜索，以高层方式协调机器人，从而减少在复合空间中规划的需求；2）分辨率引导，一种在规划过程中迭代细化工作空间表示、以更细粒度指导机器人运动的机制；3）广泛的实验验证，用于评估该方法相较于其他方法的优势与局限。

</details>

---

### [[20_Research/Papers/具身智能/VBT-MPC_Vision-Based_Tactile_MPC_for_Contour_Following|VBT-MPC: Vision-Based Tactile MPC for Contour Following]]

![[assets/2605.20392_figure.png|800]]

- **arXiv**: [2605.20392](https://arxiv.org/abs/2605.20392)
- **PDF**: https://arxiv.org/pdf/2605.20392
- **详细分析**: [[20_Research/Papers/具身智能/VBT-MPC_Vision-Based_Tactile_MPC_for_Contour_Following|VBT-MPC: Vision-Based Tactile MPC for Contour Following]]
- **作者**: Edison Velasco-Sanchez, Luis F. Recalde, Guanrui Li, Pablo Gil
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

触觉感知在机器人操作中尤其重要，特别是在表面检测、沿边界扫描这类必须持续保持接触的任务中，仅靠视觉往往难以稳定完成。现有触觉伺服方法要么依赖接触位姿估计与监督学习，要么需要额外的力控制器来维持接触，系统复杂度较高。本文聚焦“沿轮廓跟踪”这一具身智能/机器人中的基础能力，尝试让机器人直接基于触觉轮廓特征完成稳定控制，因此具有较强的实用价值。

#### 方法概述和架构

论文提出 VBT-MPC（Vision-Based Tactile Model Predictive Control）框架，面向装有 Vision-Based Tactile Sensor（VBTS）的眼在手端执行器进行轮廓跟随。方法直接在轮廓特征空间中进行控制：首先从标记式/无标记触觉图像中提取触觉特征，再构造包含轮廓位置、方向、切向姿态与局部形变等信息的轮廓特征向量。随后通过 MPC 在有限预测时域内联合优化未来状态与末端速度输入，同时显式加入接触保持、触觉特征位于视野内以及输入幅值等约束。论文还设计了一个轮廓特征提取流程，将分割网络、线段拟合与 EKF 结合，用于估计并过采样轮廓特征；并将该方法与适配到触觉特征上的视觉伺服、解耦视觉-触觉伺服等基线进行比较。

#### 实验结果分析

实验在仿真与真实世界中同时验证，场景覆盖了不同几何形状和不同材质的对象，包括 3D 打印轮廓和真实物体。作者还对触觉轮廓提取方法进行了定量评估，并与三种轮廓提取基线进行了比较；同时在仿真与真实机器人上对比了 couple 和 decoupled 视觉伺服策略。总体结论是，VBT-MPC 在轮廓跟踪性能上优于对照方法，并且能在不依赖独立位姿估计模块或复杂力控制架构的情况下实现更稳健的接触跟踪；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

触觉感知在机器人操作中起着关键作用，尤其是在表面检测等任务中。成功执行这些任务需要在保持接触的同时准确跟踪物体轮廓。在这项工作中，我们提出了一种用于机器人轮廓跟随的 Vision-Based Tactile Model Predictive Control（VBT-MPC）框架，该框架使用安装在眼在手端配置中的 Vision-Based Tactile Sensor（VBTS）。所提出的控制器直接在轮廓特征空间中工作，从而避免了单独的位姿估计模块或复杂的力控制架构。我们进一步将 VBT-MPC 与适配到触觉特征上的视觉伺服策略进行比较，并在仿真和真实世界实验中，对不同几何形状和材料的物体上的轮廓跟踪效果进行了评估。

</details>

---

### [[20_Research/Papers/具身智能/Terrestrial_Soft_Mobile_Robots_A_Review|Terrestrial Soft Mobile Robots: A Review]]

![[assets/2605.20304_figure.jpg|800]]

- **arXiv**: [2605.20304](https://arxiv.org/abs/2605.20304)
- **PDF**: https://arxiv.org/pdf/2605.20304
- **详细分析**: [[20_Research/Papers/具身智能/Terrestrial_Soft_Mobile_Robots_A_Review|Terrestrial Soft Mobile Robots: A Review]]
- **作者**: Dimuthu D. K. Arachchige
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

软体移动机器人因具有柔顺、可变形和更高的环境适应性，被认为适合搜索救援、服务巡检、监视、勘探和制造等任务，尤其是在狭窄、崎岖、危险或对接触敏感的场景中。相比传统轮式或刚性机器人，软体系统更容易通过不规则地形、缝隙和障碍，但其设计、驱动、建模与控制仍面临材料、制造与可靠性等方面的瓶颈。本文聚焦“无轮式”的陆地软体移动机器人，对该方向的研究脉络做系统梳理，因此对机器人与具身智能领域的研究者具有较强参考价值。

#### 方法概述和架构

这篇论文不是提出单一新模型，而是一篇面向陆地无轮式软体移动机器人的综述。作者按照系统功能链条组织内容：先按形态将机器人分为软肢体与软无肢体两类，再进一步总结多足、蠕动、波动、侧向波动、蛇形、侧滑、钟形运动、滚动、翻转、缠绕与跳跃等主要运动模式。随后综述不同驱动方式，包括气动、电机驱动、形状记忆合金、介电弹性体、电静力、磁驱动、燃烧驱动以及混合驱动。论文还系统比较了建模方法、轨迹生成方法和控制方法，并把这些模块与具体运动策略对应起来，形成从结构—驱动—建模—规划—控制的完整分类框架。

#### 实验结果分析

从正文节选可见，作者梳理了1996年至2024年间相关研究的分布，并归纳出该领域在不同拓扑结构和运动方式上的代表性原型与发展趋势。论文对比了多种软体机器人形态在稳定性、地形适应性、载荷能力和多模态运动上的特点，指出目前研究已覆盖从三足到多足、从软肢体到软无肢体的多类平台。作者进一步总结了该方向的关键挑战，包括设计、制造、建模和控制四个层面的难点；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

软体移动机器人已经成为一个很有前景的研究方向，并有望应用于搜索救援、服务、监视、勘探和制造等多个领域。本文对当前软体移动机器人研究的现状进行了全面综述，重点关注无轮式的陆地行走系统。我们总结了过去和现在在运动策略、驱动方法、建模方法以及控制系统方面的发展进展。此外，我们还识别出若干关键研究挑战，这些挑战必须被解决，软体移动机器人才能在各种应用中得到广泛采用。总体而言，本文为对软体移动机器人和软体机器人领域感兴趣的研究人员与实践者提供了有价值的参考资源。

</details>

---

### [[20_Research/Papers/具身智能/Adaptive_Human-Robot_Collaboration_for_Masonry_Construction_Under_Material_and_Assembly_Uncertainty|Adaptive Human-Robot Collaboration for Masonry Construction Under Material and Assembly Uncertainty]]

![[assets/2605.20264_figure.png|800]]

- **arXiv**: [2605.20264](https://arxiv.org/abs/2605.20264)
- **PDF**: https://arxiv.org/pdf/2605.20264
- **详细分析**: [[20_Research/Papers/具身智能/Adaptive_Human-Robot_Collaboration_for_Masonry_Construction_Under_Material_and_Assembly_Uncertainty|Adaptive Human-Robot Collaboration for Masonry Construction Under Material and Assembly Uncertainty]]
- **作者**: Jutang Gao, Arash Adel
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

建筑机器人在砌体施工中具有提升效率、安全性和一致性的潜力，但真实工地同时存在材料尺寸波动、装配误差累积以及人机之间通信不直观等问题，导致传统开环执行容易偏离预期。对于胶粘式砖砌任务而言，薄胶层带来的容差空间更小，一旦前序砖块或胶层位置出现微小偏差，就可能在后续砌筑中逐步放大，甚至引发碰撞或层高不平。本文聚焦“机器人放砖、人工涂胶”的协作砌筑场景，试图解决机器人如何把空间意图清晰传达给人，以及如何基于现场感知及时修正装配偏差这两个核心瓶颈，因此具有较强的工程现实意义。

#### 方法概述和架构

论文提出一种面向砌体施工的自适应人机协作工作流，包含两个互补模块：末端执行器搭载投影仪用于向人提供空间注册、即时的涂胶指引，激光扫描用于对砖块抓取与放置位姿进行反馈修正。系统在共享工作空间中执行循环流程：机器人先用一维激光扫描砖块顶面，估计单砖姿态与尺寸并自适应抓取；随后移动到投影位姿，将规划好的砖块轮廓以注册四边形投到施工表面，指导人工在指定边界内涂胶。完成后机器人放置砖块，并在每一层施工前扫描已建表面，估计当前层高与累计偏差，再对后续放置位姿进行修正，以维持水平层和对齐的墙边。投影模块通过末端执行器与投影仪之间的标定建立固定变换关系，并将三维任务点映射到投影平面，实现“所见即所做”的可视化引导；自适应模块则通过点云拟合和几何约束，将感知到的砖块姿态、尺寸和已建结构高度转化为抓取与放置修正量。

#### 实验结果分析

作者在全尺寸砌体实验中验证了方法，覆盖了传统 running-bond 以及非标准构型；实验对象为真实砖块和胶粘式砖砌流程，而非仿真场景。结果表明，投影引导能够提升人工涂胶的一致性，并缩短涂胶时间；激光反馈修正则能保持砌筑层的水平度，并避免开环执行中常见的碰撞失败。文中未给出具体数值，因此可见文本未给出具体数值；从结果描述看，该方法在容差累积和施工鲁棒性方面优于不带反馈修正的开环流程。

<details>
<summary>完整摘要</summary>

人机协作在建筑施工中常常受到机器人与人之间通信手段有限的制约，同时还需要应对材料与装配不确定性带来的容差累积问题。我们提出了一种用于砌体施工的自适应人机协作工作流，用来缓解通信受限与容差累积两类挑战，并通过一个砖砌案例进行验证：机器人负责放置砖块，人类负责涂布胶黏剂。该工作流由两个互补机制支撑：1）安装在末端执行器上的投影仪，为人工涂胶提供空间注册、即时的投影引导；2）激光扫描，用于基于反馈的抓取与放置位姿修正。二者结合后，系统能够根据材料变化和累积装配误差同步调整人的操作与机器人的动作。基于全尺寸实验的结果表明，在传统 running-bond 以及非标准构型下，投影引导提高了胶黏剂涂布的一致性并缩短了涂布时间；基于激光的修正则能够保持砌筑层水平，并避免开环执行中容易出现的碰撞失败。上述结果说明，将空间投影与反馈驱动的自适应机制结合起来，并借助材料感知与已建结构感知，可以缓解容差累积问题，提升人机协作建筑施工的精度与鲁棒性。

</details>

---
