# cs.LG | Machine Learning | 2026-05-20

#arxiv #ComputerScience

**论文数**: 14

### [[20_Research/Papers/机器人/Learning-Accelerated_Optimization-based_Trajectory_Planning_for_Cooperative_Aerial-Ground_Handover_Missions|Learning-Accelerated Optimization-based Trajectory Planning for Cooperative Aerial-Ground Handover Missions]]

![[assets/2605.19562_figure.png|800]]

- **arXiv**: [2605.19562](https://arxiv.org/abs/2605.19562)
- **PDF**: https://arxiv.org/pdf/2605.19562
- **详细分析**: [[20_Research/Papers/机器人/Learning-Accelerated_Optimization-based_Trajectory_Planning_for_Cooperative_Aerial-Ground_Handover_Missions|Learning-Accelerated Optimization-based Trajectory Planning for Cooperative Aerial-Ground Handover Missions]]
- **作者**: Jingshan Chen, Bochen Yu, Henrik Ebel, Peter Eberhard
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

本文面向协同空地接驳任务：无人机（UAV）与无人地面车（UGV）需要在运输过程中完成目标物交接，并兼顾到达时间、控制代价与动力学可行性。传统分层式规划虽然实现简单，但往往先给出几何路径再做时间参数化，难以从一开始就严格满足动力学和约束，因而在跟踪与安全性上存在隐患。作者此前的集中式轨迹优化能够同时考虑系统动力学和任务约束，但求解开销较大，难以支撑动态环境下的实时重规划，因此这项工作值得关注的核心原因，是尝试用学习方法为优化器“加速”而不是替代它。

#### 方法概述和架构

论文提出一种学习增强的优化式轨迹规划框架，核心是一个神经网络代理规划器，用来从任务规格直接预测 UAV 和 UGV 的协同接驳轨迹。该代理规划器采用解耦的 encoder-decoder LSTM，为每个机器人分别训练网络，而不是使用单一的整体策略，从而输出协调一致的轨迹预测。训练阶段，作者先使用已有的集中式轨迹优化器离线生成专家示范数据，再对代理网络进行监督学习，使其学会从初始状态、目标状态等任务输入映射到可用的轨迹初值。推理阶段，网络不直接作为最终控制器执行，而是将预测结果作为 downstream 集中式优化器的 warm start，由优化器进一步修正为满足动力学与约束的轨迹。整体流程形成“数据驱动粗预测 + 模型驱动精修”的两级结构，兼顾了速度与可行性。

#### 实验结果分析

实验基于协同空地接驳任务的数值 benchmark，对比了 cold start 优化与学习增强后的 warm start 优化。结果显示，该框架相较于直接从零初始化求解，优化速度提升超过 3 倍，同时优化成功率达到 100%。从文本可见，作者强调该方法在保持可行性与解质量的同时显著降低了计算成本；但节选内容未给出更细的实验数值、消融结果或泛化测试的具体指标。

<details>
<summary>完整摘要</summary>

本文提出一种用于协同无人机（UAV）与无人地面车（UGV）接驳任务的学习增强型轨迹规划框架。尽管集中式轨迹优化能够保证动力学可行性和任务最优性，但其较高的计算开销限制了实时应用。为此，我们提出一种神经网络代理规划器，采用解耦的 encoder-decoder 长短期记忆网络（LSTM），从任务规格中生成协调的接驳轨迹预测。这些预测随后作为下游集中式优化器的有信息 warm start，从而加速其收敛到动力学可行的解。基准评估表明，与 cold start 优化相比，学习增强的规划框架实现了超过三倍的速度提升以及 100% 的优化成功率。结果说明，将数据驱动推断与基于模型的精修相结合，能够为异构多机器人系统生成快速且可靠的轨迹。

</details>

---

### [[20_Research/Papers/具身智能/Domain-Adaptive_Communication-Rate_Optimization_for_Sim-to-Real_Humanoid-Robot_Wireless_XR_Teleoperation|Domain-Adaptive Communication-Rate Optimization for Sim-to-Real Humanoid-Robot Wireless XR Teleoperation]]

![[assets/2605.19293_figure.png|800]]

- **arXiv**: [2605.19293](https://arxiv.org/abs/2605.19293)
- **PDF**: https://arxiv.org/pdf/2605.19293
- **详细分析**: [[20_Research/Papers/具身智能/Domain-Adaptive_Communication-Rate_Optimization_for_Sim-to-Real_Humanoid-Robot_Wireless_XR_Teleoperation|Domain-Adaptive Communication-Rate Optimization for Sim-to-Real Humanoid-Robot Wireless XR Teleoperation]]
- **作者**: Caolu Xu, Zhiyong Chen, Meixia Tao, Li Song, Feng Yang, Wenjun Zhang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 5.42（加权：具身智能 3，强化学习 0.36，世界模型 0.16，机器人 1.9）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

无线 XR 遥操作可让人类通过沉浸式接口采集人形机器人的示教数据，是具身智能与大模型机器人数据获取的重要基础设施。但在实际应用中，机器人动作需要高频采样与传输，这会带来显著的通信开销和设备能耗，尤其对电池供电的 XR 终端不友好。与此同时，不同关节/动作维度对重建精度的贡献并不相同，统一满速传输往往低效；再加上真实机器人在线试错代价高，训练好的通信策略还会面临仿真到真实部署的分布偏移。因此，这篇工作值得关注之处在于：它把“通信率控制”与“sim-to-real 迁移”结合起来，直接面向可落地的人形机器人遥操作系统优化。

#### 方法概述和架构

论文提出了一个面向人形机器人无线 XR 遥操作的 sim-to-real 通信率优化框架，系统流程覆盖采样、传输、插值与重建。核心决策变量是各个动作维度的采样率，目标是在尽量降低通信能耗的同时，保持机器人运动轨迹的重建精度。为应对真实机器人反馈难以在线获取的问题，作者主要在仿真环境中交互训练，并利用离线真实域轨迹对策略进行校正。理论上，论文给出了带潜在密度比与编码器表示偏差的 PAC-Bayes 泛化分析，用来刻画仿真策略迁移到真实域时的误差来源。算法上，作者将密度比加权引入 PPO，并配合信任域正则化；训练流程包括先用 MMD 进行编码器 warm-up，再冻结编码器做潜空间密度比估计与加权 PPO，最后固定策略网络，对编码器进行带信任域约束的微调，以逐步对齐仿真与真实域表示。

#### 实验结果分析

论文在公开的人形遥操作数据集上进行了实验，并进一步考察了不同无线信道和动态运动轨迹下的表现。结果显示，所提方法在仿真到真实分布偏移下，能够更好地平衡重建误差与通信能耗，相比基线方法取得更优的折中。作者还分析了算法在多种无线环境中的有效性，以及对不同运动模式的适应能力。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

无线扩展现实（XR）遥操作为采集人形机器人示教数据提供了具身交互能力，但大规模应用受到高频动作传输开销的限制。本文构建了一个集采样、传输、插值和重建于一体的系统框架，并将问题形式化为通信率优化：通过按维度控制采样率，在保持机器人运动轨迹重建精度的同时最小化通信能耗。由于从物理机器人获取实时反馈受硬件成本限制，本文需要借助仿真交互并结合离线真实域数据校正来求解该问题。为指导仿真到真实（sim-to-real）适配，本文给出了一个 PAC-Bayes 泛化刻画，揭示了潜在密度比估计、有限样本偏差以及编码器偏差的影响。在此分析基础上，本文提出了一种结合密度比加权与信任域正则化的近端策略优化（PPO）方法。基于公开的人形遥操作数据集的实验表明，所提方法在 sim-to-real 分布偏移下，能够更好地平衡重建误差与通信能耗。本文还进一步分析了该算法在不同无线信道和动态运动轨迹下的有效性。

</details>

---

### [[20_Research/Papers/具身智能/Rethinking_Muon_Beyond_Pretraining_Spectral_Failures_and_High-Pass_Remedies_for_VLA_and_RLVR|Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR]]

![[assets/2605.19282_figure.png|800]]

- **arXiv**: [2605.19282](https://arxiv.org/abs/2605.19282)
- **PDF**: https://arxiv.org/pdf/2605.19282
- **详细分析**: [[20_Research/Papers/具身智能/Rethinking_Muon_Beyond_Pretraining_Spectral_Failures_and_High-Pass_Remedies_for_VLA_and_RLVR|Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR]]
- **作者**: Chongyu Fan, Gaowen Liu, Mingyi Hong, Ramana Rao Kompella, Sijia Liu
- **cs 子类**: cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型, 大模型
- **相关性评分**: 2.32（加权：具身智能 1.5，大模型 0.1，强化学习 0.36，世界模型 0.16，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

Muon 作为一种矩阵感知优化器，在大模型预训练中因能通过 Newton-Schulz 迭代把动量矩阵的奇异值统一拉到 1 而表现出较强的探索性，但作者指出，这种“全谱白化”并不一定适合预训练之外的任务。论文聚焦两个更贴近具身智能与强化学习的场景：视觉-语言-动作（VLA）训练，以及带可验证奖励的强化学习（RLVR）后训练。作者认为，在这两类任务中，梯度往往呈现低秩或低信噪比特征，Muon 反而会放大尾部噪声、破坏原有的头部专长结构，从而导致训练不稳定甚至性能崩溃。

#### 方法概述和架构

作者提出 Pion（sPectral hIgh-pass Optimizer on momeNtum），作为 Muon 的即插即用替代方案，保持同样的计算开销，但把原先“让所有奇异值都趋近 1”的统一白化，改造成两阶段的 Promotion+Suppression 机制。具体来说，Pion 仍沿用 Newton-Schulz 迭代更新动量矩阵，但通过重新设计迭代多项式，使其形成一种高通式谱滤波：把占主导的信息性奇异值锚定在 1，同时将噪声主导的尾部奇异值压向 0，并且可以调节滤波强度。为了更好保留预训练阶段形成的注意力头差异，Pion 还支持 per-head 模式，即把注意力投影按头维度重排后，分别在每个头上独立执行同样的高通迭代，额外开销为零。整体上，Pion 在训练时直接替换 Muon，不需要额外的 SVD 或 sketching。

#### 实验结果分析

在 VLA 任务上，作者在 LIBERO 和 LIBERO-Plus 上，用 VLA-Adapter 的 ℓ1 回归头以及 VLANeXt 的 flow-matching 结构进行实验，Pion 相比 Muon 和 AdamW 都更稳定、更强。比如在 LIBERO Object 上，使用 VLA-Adapter 训练 1,500 步后，Pion 达到 100% 成功率，Muon 为 97.0%，AdamW 仅为 32.2%。进一步地，Pion 的收益还扩展到真实 Franka Research 3 机器人和 pi_0.5 骨干、DROID 设置下的三个抓取-放置任务。作者还在 Qwen3-1.7B/4B 的 RLVR 后训练中，使用 GRPO 和 GMPO 在 MATH 与 GSM8K 上验证了 Pion 的优势，而 Muon 会直接崩溃到零。

<details>
<summary>完整摘要</summary>

Muon（Momentum Orthogonalized by Newton-Schulz）是一种矩阵感知优化器，它利用 Newton-Schulz（NS）迭代，通过把动量矩阵的所有奇异值都推向 1 来实现谱梯度正交化。虽然这种统一的谱白化在大语言模型预训练中能够增强探索并优于 AdamW，但我们发现它在预训练之外的两个重要场景中会带来根本性局限：（i）跨模态的视觉-语言-动作（VLA）训练中，动作模块梯度本身具有低秩特性，导致尾部噪声方向被放大；（ii）带可验证奖励的强化学习（RLVR）中，梯度信噪比低，且需要保留来自先前训练的按头专长结构，白化会使训练变得不稳定。为了解决这些问题，我们提出 Pion（sPectral hIgh-pass Optimizer on momeNtum），它是 Muon 的即插即用替代方案，在保留其计算效率的同时，用两阶段的 Promotion+Suppression 机制替换统一谱白化，我们将其称为高通 NS 迭代。该设计会产生明显的谱高通效应：把主导奇异值锚定在 1，同时将噪声尾部成分压向 0，并且滤波强度可控。为了保留预训练得到的按头异质性，Pion 还支持 per-head 模式，只需简单 reshape 就能在每个注意力头上独立应用更新，且不增加额外开销。大量实验表明，Pion 在 VLA 和 RLVR 两类场景中都能稳定优于 Muon 和 AdamW。在 LIBERO 与 LIBERO-Plus 上的 VLA 训练中，Pion 在 ℓ1 回归（VLA-Adapter）和 flow-matching（VLANeXt）两类架构上都持续优于基线，例如在使用 VLA-Adapter 训练 1,500 步后，Pion 在 LIBERO Object 上达到 100% 成功率，而 Muon 为 97.0%，AdamW 仅为 32.2%。Pion 的优势还扩展到真实的 Franka Research 3 机器人，在采用 pi_0.5 骨干、DROID 设置下的三个抓取与放置任务中同样表现突出。在使用 Qwen3-1.7B/4B、GRPO 和 GMPO 的 RLVR 后训练中，Pion 在 MATH 和 GSM8K 上也优于 AdamW，而 Muon 则退化到零。

</details>

---

### [[20_Research/Papers/强化学习/GAE_Falls_Short_in_Imperfect-Information_Self-Play_Reinforcement_Learning|GAE Falls Short in Imperfect-Information Self-Play Reinforcement Learning]]

![[assets/2605.19235_figure.png|800]]

- **arXiv**: [2605.19235](https://arxiv.org/abs/2605.19235)
- **PDF**: https://arxiv.org/pdf/2605.19235
- **详细分析**: [[20_Research/Papers/强化学习/GAE_Falls_Short_in_Imperfect-Information_Self-Play_Reinforcement_Learning|GAE Falls Short in Imperfect-Information Self-Play Reinforcement Learning]]
- **作者**: Zhiyuan Fan, Gabriele Farina
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.2，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

在不完美信息的对抗性多智能体强化学习中，智能体只能基于局部可见信息决策，同时还要面对会适应策略的对手，因此通常需要随机策略而不是确定性策略。现有自博弈方法中，PPO 配合 GAE 是很常见且有效的方案，但本文指出：GAE 在多步估计时会引入未来动作采样带来的额外方差，这种方差在均衡自博弈里会被进一步放大，且即使 critic 是精确的也不会消失。这个问题会直接恶化梯度估计稳定性，尤其在扑克牌、斗地主这类大规模不完美信息博弈中更为突出。因此，这篇工作值得关注，因为它针对的是自博弈强化学习里一个长期被忽视、但可能是训练不稳定根源的基础性瓶颈。

#### 方法概述和架构

作者提出了 Q-boosting，一种基于集中式动作价值 critic 的降方差优势估计器，用来替代标准 GAE。其核心做法是把 GAE 中沿采样轨迹的多步 bootstrap，改为多步 Expected SARSA(λ) trace：在每一步回传时都对策略分布做期望，从而平均掉未来动作采样噪声。基于这个估计器，作者进一步提出 Variance-Reduced Policy Optimization（VRPO），整体仍保留 PPO 的 clipped objective 和 on-policy actor 更新机制，因此兼容现有训练流程。训练时，集中式 Q critic 先输出动作价值，再通过策略期望递推得到更低方差的优势估计，actor 则用该优势进行策略梯度更新。方法的关键连接点是：用 Q critic 提供更细粒度的动作级信息，用期望回传替换采样回传，从而在不改变 PPO 主体结构的前提下提升稳定性。

#### 实验结果分析

实验覆盖了中等规模博弈、Dou Dizhu 以及 Heads-Up No-Limit Texas Hold’em 等环境，并与多种 PPO 类基线进行比较。论文报告称，VRPO 在可计算 exploitability 的中等规模基准上持续取得更低的 exploitability，说明其更接近纳什均衡；在更大规模任务上也表现出很强的实战性能。具体到 Dou Dizhu，VRPO 在相同训练预算下优于此前的 SOTA 代理 PerfectDou；在 HUNL 中，VRPO 在不依赖在线搜索、子博弈求解或 blueprint 式加注大小设定的情况下，对 Slumbot 取得了正性能。正文节选还提到做了针对通用超参数和 VRPO 特有超参数的消融分析，但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

竞争性的多智能体强化学习在不完美信息博弈中要求智能体在部分可观测条件下并面对对抗性对手进行决策，这使得随机策略成为必要。尽管采用 Proximal Policy Optimization（PPO）的自博弈强化学习已经取得了很强的经验表现，但其标准优势估计器——广义优势估计（GAE）——会因对随机未来动作进行采样而产生额外方差。这种方差在均衡自博弈中会被放大，因为均衡策略本身具有随机性；而且即使 critic 是精确的，这种方差仍然存在。为了解决这一瓶颈，我们提出了 Q-boosting：一种基于集中式动作价值 critic 的降方差优势估计器，并在此基础上提出 Variance-Reduced Policy Optimization（VRPO）。该算法用多步 Expected SARSA(λ) trace 替换了采样式的多步回传，在每一步都计算策略期望，以平均掉动作采样噪声，同时保留 PPO 的 clipped objective 和 on-policy actor 更新。实验表明，VRPO 在从中等规模到大规模的游戏中都能稳定取得很强的性能，包括 Dou Dizhu 和 Heads-Up No-Limit Texas Hold’em。

</details>

---

### [[20_Research/Papers/强化学习/Precision_Physical_Activity_Prescription_via_Reinforcement_Learning_for_Functional_Actions|Precision Physical Activity Prescription via Reinforcement Learning for Functional Actions]]

![[assets/2605.19208_figure.png|800]]

- **arXiv**: [2605.19208](https://arxiv.org/abs/2605.19208)
- **PDF**: https://arxiv.org/pdf/2605.19208
- **详细分析**: [[20_Research/Papers/强化学习/Precision_Physical_Activity_Prescription_via_Reinforcement_Learning_for_Functional_Actions|Precision Physical Activity Prescription via Reinforcement Learning for Functional Actions]]
- **作者**: Gefei Lin, Rui Miao, Jennifer Sacheck, Xiaoke Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

这篇论文关注的是“精准体力活动处方”问题：给定个体的健康指标和人口学特征，如何推荐一段时间内每天步数的最优分布，以更好地改善心代谢风险相关生物标志物。现有研究通常只把日步数压缩成均值或类别，容易丢失时间分布信息，也难以针对不同人群给出个性化建议。作者指出，基于可穿戴设备的连续步数数据已经足够丰富，但缺少一种能直接输出“步数分布型处方”的方法，因此这项工作具有明显的应用价值和方法学意义。

#### 方法概述和架构

论文把每日步数序列建模为“函数型动作”，即在一个时间区间内输出步数分布，而不是单一连续数值。方法上，作者构建了一个离线强化学习（offline RL）算法，在马尔可夫决策过程下学习策略：状态包含个体的健康生物标志物和人口学信息，动作则是未来一段时间的步数分布。算法核心是将经典的 fitted-Q iteration 扩展到函数型动作空间，并通过 Monte Carlo 采样近似对函数型动作的条件期望，解决函数动作没有显式条件密度的问题。为保证学到的最优策略平滑可解释，作者进一步用 penalized splines 对策略进行迭代更新，使输出的处方分布具有连续性和可读性。训练阶段完全依赖预先收集的观察数据，推理时则根据个体协变量直接生成未来 90 天的个性化步数分布建议。

#### 实验结果分析

实验使用 All of Us Research Program 的纵向数据，包含 Fitbit 日步数以及血糖、BMI、收缩压、舒张压、年龄和性别等重复测量信息。作者在模拟研究中将所提方法与现有连续动作离线强化学习方法比较，结果显示本文方法在函数型动作场景下更优；但从节选文本看，可见文本未给出具体数值。应用到真实数据后，学到的最优策略总体上建议人们增加每日步数，并保持更稳定、更加一致的活动模式；同时，不同血糖、BMI、血压、年龄和性别亚组的推荐分布存在差异，体现出分层个性化特征。

<details>
<summary>完整摘要</summary>

体力活动（PA）在维持和改善健康方面发挥着重要作用。每日步数是一个关键的 PA 指标，并且可以通过常见可穿戴设备便捷获取。然而，目前仍缺少一种方法，能够针对某段时间内的每日步数分布，推荐一个面向特定健康生物标志物的个性化最优方案。本文基于 All of Us Research Program 的数据填补了这一空白。该数据包含数月的步数记录，以及关键健康生物标志物的重复测量。我们开发了一种新的离线强化学习（RL）算法，用于学习与心代谢风险相关的、个性化且最优的 PA 分布，其中动作被表示为一个函数，刻画一段时间内的每日步数分布。模拟研究表明，与现有连续动作 RL 方法相比，所提出的方法具有优势。基于 All of Us 数据学到的最优策略总体上建议人们增加每日步数，并在较长时间内保持更一致的活动模式，同时还能针对血糖水平、BMI、血压、年龄和性别等亚组提供定制化建议。

</details>

---

### [[20_Research/Papers/大模型/Sequential_Consensus_for_Multi-Agent_LLM_Debates_A_Wald-SPRT_compute_governor_with_calibration-based_failure_detection|Sequential Consensus for Multi-Agent LLM Debates: A Wald-SPRT compute governor with calibration-based failure detection]]

![[assets/2605.19193_figure.png|800]]

- **arXiv**: [2605.19193](https://arxiv.org/abs/2605.19193)
- **PDF**: https://arxiv.org/pdf/2605.19193
- **详细分析**: [[20_Research/Papers/大模型/Sequential_Consensus_for_Multi-Agent_LLM_Debates_A_Wald-SPRT_compute_governor_with_calibration-based_failure_detection|Sequential Consensus for Multi-Agent LLM Debates: A Wald-SPRT compute governor with calibration-based failure detection]]
- **作者**: Andrea Morandi
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

多智能体LLM debate 已被证明能提升事实性和推理能力，但现有方法通常预先固定辩论轮数，这会在简单问题上浪费算力、在复杂问题上又可能停止过早。对于实际系统来说，更关键的问题不是“辩论能否提升答案”，而是“什么时候继续辩论已经不再值得付费”。这篇论文值得关注之处在于，它把经典序贯检验 SPRT 引入多智能体辩论流程，尝试把辩论系统从固定步数推进到按需停止的算力控制模式。

#### 方法概述和架构

论文提出 Sequential Consensus：在每一轮辩论后，由一个LLM judge 对当前各智能体立场输出一个位于[0,1]的共识分数，作为序贯观测输入到 Wald-SPRT 监控器中。监控器假设两类分布：一类对应“有用收敛/可停止”，另一类对应“尚未形成有用收敛/应继续”，并累积两者的对数似然比。若累计统计量越过上界，则判定已形成共识并停止；若跌破下界，则判定当前信号不足以支持继续收敛或给出“no-consensus”；若一直未越界，则在最大轮数 R_max 处截断，输出 best-effort 结果并标记为 capped。为适配实际任务，作者用小规模校准集拟合 Beta 似然族的参数，使 judge 分数在不同领域下分别对应合适的 f0、f1；论文还讨论了非 i.i.d. 假设、误校准和 judge 失效时的行为。

#### 实验结果分析

实验分为两部分：一是基于校准 Beta 模型的 Monte-Carlo 仿真，用来分析工作曲线、错误率、截断行为和对误校准的敏感性；二是在真实 LLM 上做 200 个 MMLU 和 200 个 GSM8K 样本的评测，使用三个异构智能体（gpt-5、claude-opus-4-6、gemini-2.5-pro）和 claude-opus-4-6 作为 judge，并为每个任务域使用不相交的 40 条样本做校准。结果显示，在 GSM8K 上，该方法平均只需 1.01 轮、4.06 次 LLM 调用即可达到 97.0% 准确率，而固定 5 轮辩论需要 15 次调用、准确率为 99.0%，相当于以约 3.7 倍的调用减少换取约 2 个百分点的准确率下降。

<details>
<summary>完整摘要</summary>

多智能体LLM辩论可以提升事实性与推理能力，但大多数方案仍然采用固定轮数，这会在简单样本上浪费算力，并且掩盖一个更棘手的系统问题：什么时候共识信号已经足够有信息量，可以停止继续辩论并不再付费？我们将 Wald 的序贯概率比检验（SPRT）改造为一个可插拔的算力调度器，应用于 LLM 辩论。每一轮之后，一个 LLM judge 会针对最新的智能体立场输出一个位于[0,1]的共识分数；Wald 监控器在“有用收敛”与“尚未形成有用收敛”这两个假设下，基于 Beta 似然族累积对数似然比，并在越过任一边界时停止，或者在达到 R_max 时返回一个封顶的 best-effort 结果。在 i.i.d. 假设下，该规则继承 SPRT 的第一类/第二类错误保证；而在实际部署中，更重要的是校准本身，也就是估计 judge 分数是否真的能在给定领域中区分“有用收敛”和“无效收敛”。我们从两条路径验证这一点：(i) 在校准的 Beta 模型下进行 Monte-Carlo 仿真，刻画工作曲线、错误率、封顶行为和敏感性；(ii) 在真实 LLM 上评测 200 个 MMLU 和 200 个 GSM8K 样本，使用三个异构智能体（gpt-5、claude-opus-4-6、gemini-2.5-pro）以及一个 claude-opus-4-6 judge，并为两个任务分别使用互不重叠的 40 条样本作为校准集。在 GSM8K 上，该规则平均在 1.01 轮后停止（4.06 次 LLM 调用），准确率为 97.0%，而固定 5 轮辩论的准确率为 99.0%、共需 15 次调用：这意味着调用数减少了 3.7 倍，但准确率下降了 2 个百分点。在 MMLU 上，校准后的 KL 约等于 0，规则在 99.5% 的样本上都会达到 R_max 封顶，成本增加约 2.1 倍。由此可见，这项工作的核心结论并不是 SPRT 能让辩论更准确，而是经典序贯检验可以作为多智能体 LLM 系统中一个低成本的算力控制与失效检测层。

</details>

---

### [[20_Research/Papers/具身智能/A_Heuristic_Approach_for_Performance_Tuning_in_RL-based_Quadrotor_Control_via_Reward_Design_and_Termination_Conditions|A Heuristic Approach for Performance Tuning in RL-based Quadrotor Control via Reward Design and Termination Conditions]]

![[assets/2605.19166_figure.png|800]]

- **arXiv**: [2605.19166](https://arxiv.org/abs/2605.19166)
- **PDF**: https://arxiv.org/pdf/2605.19166
- **详细分析**: [[20_Research/Papers/具身智能/A_Heuristic_Approach_for_Performance_Tuning_in_RL-based_Quadrotor_Control_via_Reward_Design_and_Termination_Conditions|A Heuristic Approach for Performance Tuning in RL-based Quadrotor Control via Reward Design and Termination Conditions]]
- **作者**: Fausto Mauricio Lagos Suarez, Akshit Saradagi, Vidya Sumathy, George Nikolakopoulos
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 1.52（加权：具身智能 0.3，强化学习 0.56，世界模型 0.16，机器人 0.5）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

四旋翼强化学习控制近年来在狭窄环境高速飞行、穿越和竞速等任务上表现突出，但这类工作通常更关注速度和机动性，而不是可调的控制品质。对于基础设施巡检等应用，控制器不仅要稳定跟踪，还需要具有可调的超调、收敛时间和稳态误差，以适配“更快的机动”或“更平稳的巡检”等不同需求。作者指出，传统 RL 训练流程中的奖励设计和终止条件往往难以像 PID 那样直观调参，因此提出一种面向性能整定的启发式方法，值得关注。

#### 方法概述和架构

本文针对 Crazyflie 四旋翼的端到端稳定控制，采用 PPO 训练一个从观测到原始电机转速的策略。观测空间包含位置误差、姿态误差四元数、线速度、角速度以及上一时刻动作，并在除历史动作外的状态量上加入高斯噪声以增强鲁棒性。动作空间为 4 维归一化电机 RPM，经过线性映射得到仿真中的实际转速。奖励函数由多项组成：生存奖励、水平与高度位置误差的指数型奖励、线速度奖励、基于四元数误差的测地角奖励，以及相邻动作差分的平滑惩罚，用以诱导类似导数项的阻尼行为。与此同时，作者还设计了成功/失败终止条件和时间截断条件，并提出一套启发式规则，通过调节奖励权重、指数系数以及终止条件来在“baseline、acrobatic、inspection”三种性能模式之间切换。

#### 实验结果分析

实验在 Crazyflie 四旋翼仿真平台上进行，训练采用 PPO，并在 100 次试验中评估 baseline、acrobatic 和 inspection 三种策略的稳定性能。作者报告称，所提出的奖励设计与截断条件组合能够在 600 万步训练内较样本高效地学到基线策略，且可实现近似临界阻尼响应与约 2% 的稳态误差。进一步通过调参得到的 acrobatic 与 inspection 策略分别对应更快和更慢的收敛行为，同时保持相近的稳态误差；但节选文本未给出具体数值结果。

<details>
<summary>完整摘要</summary>

基于强化学习（RL）的四旋翼控制策略在诸如拥挤环境中的快速导航和无人机竞速等任务上取得了令人印象深刻的性能，这些任务通常强调速度和机动性。然而，在基础设施巡检等应用中，关键需求是实现精确、受控且性能可调的机动控制。本文提出一种新的启发式方法，通过奖励设计和终止条件来实现 RL 四旋翼控制中的可调性能。我们提出一种新的奖励结构，其中包含双带宽指数项，可在定点跟踪中实现基线的临界阻尼响应，并具有较低的稳态误差。当与 Proximal Policy Optimization（PPO）算法结合训练，并配合 episode 截断条件时，可在 600 万个时间步内以较高的样本效率达到所需性能。为了围绕基线行为调节性能，我们提出直观的启发式规则，通过调整奖励权重和指数系数，获得更快的（类似特技飞行的）和更慢的（类似巡检的）收敛时间表现，同时保持基线的临界阻尼响应以及约 2% 的稳态误差。我们在 100 次试验中评估了三种 RL 策略（baseline、acrobatic 和 inspection），结果表明它们在随机初始条件下的位姿和偏航跟踪都具有准确且可调的性能，从而验证了所提启发式方法的有效性。

</details>

---

### [[20_Research/Papers/世界模型/The_impact_of_observation_density_on_Bayesian_inversion_of_latent_dynamics_in_shock-dominated_flows|The impact of observation density on Bayesian inversion of latent dynamics in shock-dominated flows]]

![[assets/2605.19076_figure.png|800]]

- **arXiv**: [2605.19076](https://arxiv.org/abs/2605.19076)
- **PDF**: https://arxiv.org/pdf/2605.19076
- **详细分析**: [[20_Research/Papers/世界模型/The_impact_of_observation_density_on_Bayesian_inversion_of_latent_dynamics_in_shock-dominated_flows|The impact of observation density on Bayesian inversion of latent dynamics in shock-dominated flows]]
- **作者**: Bipin Tiwari, Muhammad Abid, Omer San
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.92（加权：强化学习 0.16，世界模型 0.76）
- **关联关键词**: WorldModel

#### 研究背景与动机

这篇工作关注的是在强激波主导的可压缩流中，如何仅凭稀疏且带噪观测反推出未知初始状态，属于典型但非常困难的反问题。该问题在超高速飞行、再入器设计、风洞试验校准以及未来数字孪生中都很关键，但由于激波、接触间断和稀疏测量的共同作用，后验推断往往高度非线性且病态。传统高保真 CFD 做贝叶斯推断需要大量前向调用，成本过高，因此本文值得关注的地方在于把降阶建模与贝叶斯不确定性量化结合起来，尝试把原本不可承受的反演流程变成可计算的流程。

#### 方法概述和架构

作者提出一个非侵入式的 AE-ROM 框架用于贝叶斯初始状态反演。首先，使用基于卷积自编码器的降阶模型将高维流场压缩到低维非线性潜变量空间，再通过一个学习得到的潜空间前向算子，把编码后的初始条件映射到最终时刻的潜状态。随后，解码器把潜变量恢复回物理流场，从而实现快速前向评估，并可直接嵌入 No-U-Turn Sampler (NUTS) 中进行后验采样。数据方面，作者用 Latin hypercube sampling 生成 500 组高保真 Sod shock tube 模拟，并用五阶 WENO 格式求解；反演目标是利用最终时刻密度和压力的稀疏、带噪观测，恢复未知的左右初始密度与压力。该方法还系统考察了潜变量维度、训练数据量和观测密度对重建与反演性能的影响。

#### 实验结果分析

实验表明，AE-ROM 能较好重建 shock tube 的关键结构，包括稀疏波、接触间断和激波前沿。作者发现潜空间维度取 32 时在重建精度与压缩紧致性之间取得较好平衡，而 250 组训练模拟已足以获得高质量重建；这些结论来自对不同设置的对比分析。对于贝叶斯反演，增加观测密度会显著压缩后验不确定性，使密度和压力的平均后验标准差分别下降约 78% 和 76%，而后验均值误差下降相对更温和。可见文本未给出具体基线方法的完整数值对比，但整体结论是该框架在效率与不确定性刻画上都表现良好。

<details>
<summary>完整摘要</summary>

从稀疏且带噪测量中推断强激波主导可压缩流的未知初始状态，是一个困难的病态反问题，原因在于非线性波相互作用以及感知能力有限。本文提出一种非侵入式降阶建模框架，用于高效的贝叶斯初始状态反演，并带有不确定性量化。该框架结合了卷积自编码器和一个学习得到的潜空间前向算子：自编码器将高维流场压缩为紧凑的非线性潜在表示，而前向算子根据编码后的初始条件预测最终时刻的潜状态。这个 AE-ROM 代理模型能够快速执行前向评估，并可嵌入 No-U-Turn Sampler (NUTS) 中进行后验探索。文中使用 500 组由 Latin hypercube sampling 生成、并通过五阶 WENO 格式求解的高保真 Sod shock tube 模拟来验证该框架。反问题的目标是根据最终时刻密度和压力场的稀疏带噪观测，恢复未知的左右初始密度和压力状态。结果显示，AE-ROM 能够准确重建 shock tube 的关键结构，包括稀疏波、接触间断和激波前沿。潜空间维度为 32 时，在重建精度与降维紧致性之间取得了有效平衡；而 250 组训练模拟已足以实现准确重建。随着观测密度增加，后验不确定性显著收缩，密度和压力的平均后验标准差分别降低约 78% 和 76%。总体而言，所提出的框架为激波主导流动的逆向分析提供了一种计算高效且能够刻画不确定性的方案，并有望扩展到多维可压缩流和数字孪生应用中。

</details>

---

### [[20_Research/Papers/大模型/TabQL_In-Context_Q-Learning_with_Tabular_Foundation_Models|TabQL: In-Context Q-Learning with Tabular Foundation Models]]

![[assets/2605.18979_figure.png|800]]

- **arXiv**: [2605.18979](https://arxiv.org/abs/2605.18979)
- **PDF**: https://arxiv.org/pdf/2605.18979
- **详细分析**: [[20_Research/Papers/大模型/TabQL_In-Context_Q-Learning_with_Tabular_Foundation_Models|TabQL: In-Context Q-Learning with Tabular Foundation Models]]
- **作者**: Qisai Liu, Zhanhong Jiang, Timilehin Ayanlade, Ashutosh Kumar Nirala, Yang Li, Aditya Balu, Soumik Sarkar
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

强化学习中的 Q-learning/DQN 依赖大量在线交互和反复的梯度更新，在高维或分布外场景下往往样本效率不高、训练也不够稳定。另一方面，大模型与基础模型展现了 in-context learning 能力，使模型可以仅凭少量上下文示例完成快速适应，这为“把价值学习从参数更新转向上下文推理”提供了新思路。本文关注如何将这一能力引入强化学习中的 action-value 估计与 Bellman 迭代，从而降低在线采样成本并增强适应性，因此具有较强的方法学意义。

#### 方法概述和架构

论文提出 TabQL（Tabular Q-Learning），用具备 in-context learning 能力的 tabular foundation model（TFM）替换 DQN 中传统的参数化 Q-network。具体做法是把经验回放中的转移整理为 state-action-reward-next_state-Q 值五元组，并将最近的 K 条样本组成上下文窗口 C_t，作为 TFM 进行 Q 值推理的唯一在线适应机制。训练流程上，TabQL 先用标准 DQN 做一个 warm-up 阶段，在参数中学到较粗但较稳定的价值先验，并生成高质量的初始上下文；随后在线阶段由 TFM 根据上下文直接输出各动作的 Q 值，并按贪心策略选择动作。为了进一步提升上下文质量，作者还会把 TabQL 选出的动作与 DQN 预测的 Q 值结合，执行后把新转移写回 replay buffer，持续更新上下文。整体上，该方法在“表格化经验—上下文推理—动作选择—回填新样本”的闭环中运行，实现了从 vanilla Q-learning 到 DQN 再到 in-context Q-learning 的统一过渡。

#### 实验结果分析

论文从理论和实验两方面验证 TabQL 的有效性。理论上，作者分析了其收敛性和样本复杂度，说明在温和假设下 TabQL 通过 in-context learning 对 Bellman 更新进行摊销，相比 DQN 能以更少的在线交互达到更高效率。实验上，作者在多个基准上进行了数值验证，结论是 TabQL 展现出更好的样本效率和稳健的泛化能力；具体实验环境、数据集、基线和指标在节选中提及为多个 benchmark，但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

我们提出 Tabular Q-Learning（TabQL），这是一种强化学习框架，它用具有 in-context learning 能力的 tabular foundation model，替换了 Deep Q-Learning（DQN）中传统的参数化 Q 网络。其核心思想是：将 Q 值表示为一个序列到序列的基础模型在表格化的 state-action-Q-value 三元组序列上进行建模，从而能够基于最近的经验条件化，借助少量在线交互实现快速适应。TabQL 区别于经典 DQN 的关键在于：（i）通过 in-context 更新实现零样本或少样本的 Q 值推断；（ii）使用标准 DQN 的 warm-up 阶段来预先构建高质量上下文。尤其地，为了提升上下文质量，我们通过执行 TabQL 输出的动作，并结合 DQN 预测的 Q 值来生成新的转移样本。我们对 TabQL 进行了形式化定义，并在温和假设下分析了其收敛性与样本复杂度，表明 TabQL 在 vanilla Q-learning 与带有 in-context learning 的 DQN 之间形成了插值。我们的分析还表明，TabQL 通过在上下文中摊销 Bellman 更新，相比 DQN 能获得更高的效率。大量数值实验在多个基准上展示了所提 TabQL 的有效性与高效性。

</details>

---

### [[20_Research/Papers/具身智能/Emergence_of_a_Flow-Assisted_Casting_Strategy_for_Olfactory_Navigation_via_Memory-Augmented_Reinforcement_Learning|Emergence of a Flow-Assisted Casting Strategy for Olfactory Navigation via Memory-Augmented Reinforcement Learning]]

![[assets/2605.18881_figure.png|800]]

- **arXiv**: [2605.18881](https://arxiv.org/abs/2605.18881)
- **PDF**: https://arxiv.org/pdf/2605.18881
- **详细分析**: [[20_Research/Papers/具身智能/Emergence_of_a_Flow-Assisted_Casting_Strategy_for_Olfactory_Navigation_via_Memory-Augmented_Reinforcement_Learning|Emergence of a Flow-Assisted Casting Strategy for Olfactory Navigation via Memory-Augmented Reinforcement Learning]]
- **作者**: Changxu Zhao, Dongxiao Zhao, Xin Bian, Gaojin Li
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

嗅觉导航是动物在湍流、非稳态流场中依靠零散气味线索寻找目标的重要能力，也对应着污染监测、靶向治疗、海洋与深海探索等机器人导航场景。由于气味信号往往间歇、稀疏且受流场强烈扰动，智能体必须在有限历史信息中判断何时沿气味追踪、何时借助背景流进行搜索，这使问题天然具有部分可观测和强时序依赖特征。本文值得关注之处在于，它不预设人工规则或显式模型，而是直接考察带有限记忆的RL智能体能否在动态流场中自发形成与动物相似的高效搜索策略，并解释“最优记忆长度”为何存在。

#### 方法概述和架构

论文将嗅觉搜索建模为带记忆的RL任务，在二维非稳态尾涡流场中训练智能体寻找气味源。环境来自绕圆柱的von Kármán涡街数值模拟，智能体每一步观测局部浓度、浓度梯度和局部流速，并输出转向角作为动作，位置则由自推进速度与背景流共同决定。为显式控制历史信息，作者采用Bootstrapped Random Update（BRU）策略，把轨迹中的观测、动作和奖励切分为固定长度的记忆片段，结合RNN策略与RRSAC算法进行训练。训练过程中随机化气味源位置、初始位置与起始时刻，以避免智能体记忆绝对坐标。随后通过统计大量独立搜索轨迹，分析不同记忆长度下的轨迹几何、转向分布、与流速耦合关系以及成功率和有效速度，并用sector-search模型对结果进行几何解释。

#### 实验结果分析

实验在不同Re、Sc、检测频率和智能体速度设置下进行，评估指标包括成功率、有效速度以及轨迹统计特征；与常见规则或模型驱动方法相比，本文重点展示的是模型自由RL策略的涌现行为。结果表明，随着记忆长度增加，智能体会自发形成一种“flow-assisted casting”策略：在低浓度区域进行更大幅度的摆动搜索，在高浓度区域则更倾向于直线推进，同时还会利用横流分量提高位移效率。成功率对记忆长度呈非单调关系：过短记忆几乎无法有效搜寻，超过阈值后迅速提升，在某个最优记忆长度附近达到峰值，继续增大则性能回落；有效速度的分布也在该点附近最集中。作者进一步指出，转向角、浓度阈值和速度耦合强度都随记忆长度呈规律性变化，且可由sector-search模型解释；节选文本未给出完整对比基线与所有具体数值。

<details>
<summary>完整摘要</summary>

在动态流场中，尽管动物依赖的是随机、间歇性的气味检测，它们仍展现出惊人的气味搜索能力。有趣的是，将这些检测信息进行整合存在一个最优时间窗口，能够最大化搜索效率。为理解其背后的机理，我们考察了强化学习（RL）智能体在非稳态流场中的导航性能，并在不同记忆长度与流场条件下进行分析。在没有任何预设模型的情况下，智能体自发形成一种借助流场的casting策略，并能够自适应地调整搜索轨迹的几何形状以及启动casting的浓度阈值，从而最大化成功率。智能体朝向气味源的平均速度对记忆长度呈现非单调依赖，这一现象可由“sector-search”模型解释。

</details>

---

### [[20_Research/Papers/大模型/STRIDE_Learnable_Stepwise_Language_Feedback_for_LLM_Reasoning|STRIDE: Learnable Stepwise Language Feedback for LLM Reasoning]]

![[assets/2605.18851_figure.png|800]]

- **arXiv**: [2605.18851](https://arxiv.org/abs/2605.18851)
- **PDF**: https://arxiv.org/pdf/2605.18851
- **详细分析**: [[20_Research/Papers/大模型/STRIDE_Learnable_Stepwise_Language_Feedback_for_LLM_Reasoning|STRIDE: Learnable Stepwise Language Feedback for LLM Reasoning]]
- **作者**: Junjie Zhang, Guozheng Ma, Shunyu Liu, Zetian Hu, Yongcheng Jing, Ting-En Lin, Yongbin Li, Dacheng Tao
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

大模型推理能力的提升越来越依赖强化学习，但现有基于过程监督的方法要么需要昂贵的逐步标注，要么把复杂推理压缩成单个标量奖励，导致中间决策缺乏足够的语义反馈。相比之下，语言式批评能够提供更丰富的纠错信息，但通常依赖冻结或外部批评器，难以在训练过程中持续随模型一起改进。本文关注如何让LLM在多步推理中获得“可学习、逐步、带语义”的反馈，因此具有较强的研究价值。

#### 方法概述和架构

论文提出 STRIDE（Learnable Stepwise Language Feedback for LLM Reasoning），核心是用可学习的逐步语言反馈替代标量过程奖励。整体采用生成器-验证器（Generator-Verifier）联合训练：生成器负责输出推理轨迹，生成式验证器则对每一步生成自然语言批注，定位并解释错误。训练流程分为三阶段：Phase I 先用 outcome-based 的 RLVR 训练基础推理能力；Phase II 训练生成式验证器，使其仅基于最终结果学习如何分解成逐步语言反馈；Phase III 利用验证器定位“第一失败点（FPF）”，再从多个已验证前缀锚点进行多点轨迹重定向，重新展开后续推理。整个方法不依赖外部逐步标注，只使用终局正确性作为奖励信号，并通过轨迹重定向设计降低噪声验证器反馈带来的训练风险。

#### 实验结果分析

作者在多个推理基准上评估了 STRIDE，并与当前最强的奖励式基线进行比较，结果显示 STRIDE 整体上显著优于这些方法。正文还指出，在一些标量方法“零通过率”的问题上，STRIDE 仍能获得学习信号并取得突破，说明其对困难样本更有效。消融实验表明，Phase III 只占总训练流程约 1/13，却对从此前无法学习的问题中获得提升起到关键作用。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

近年来，强化学习（RL）的进展凸显了其激励大模型（LLMs）推理能力的潜力。然而，现有逐步级别的方法往往依赖昂贵的标注，限制了领域覆盖范围；同时，标量分数又进一步形成信息瓶颈，所提供的语义带宽不足以改进中间决策。另一类语言批评方法依赖冻结或外部批评器，虽然能提供更丰富的文本反馈，但缺乏支撑持续策略改进所需的可扩展性。为此，本文提出一种语言驱动的逐步轨迹重定向方法，称为 STRIDE，这是一种新的训练框架，将过程监督从标量奖励转向可学习的逐步语言反馈。具体而言，我们仅使用基于结果的奖励联合训练一个生成器和一个生成式验证器，从而消除外部标注的需求，同时通过联合对齐的验证器训练实现持续的策略改进。验证器的逐步语言批注能够明确定位并解释失败原因，使生成器可以在中间步骤将推理轨迹重定向到其他决策。轨迹重定向设计即使在验证器反馈存在噪声或次优时，也能保证无害的策略改进。不同推理基准上的实验表明，STRIDE 显著优于最先进基线；此外，在标量方法在消融研究中完全无法提供学习信号的零通过率问题上，STRIDE 也取得了突破，证明了可学习的逐步语言反馈在增强LLM推理方面的有效性。

</details>

---

### [[20_Research/Papers/大模型/TEMPO_Temporal_Enforcement_via_Mode-Separated_Policy_Optimization_for_Trustworthy_LLM_Backtesting|TEMPO: Temporal Enforcement via Mode-Separated Policy Optimization for Trustworthy LLM Backtesting]]

![[assets/2605.18843_figure.png|800]]

- **arXiv**: [2605.18843](https://arxiv.org/abs/2605.18843)
- **PDF**: https://arxiv.org/pdf/2605.18843
- **详细分析**: [[20_Research/Papers/大模型/TEMPO_Temporal_Enforcement_via_Mode-Separated_Policy_Optimization_for_Trustworthy_LLM_Backtesting|TEMPO: Temporal Enforcement via Mode-Separated Policy Optimization for Trustworthy LLM Backtesting]]
- **作者**: Zeyu Zhang, Bradly C. Stadie
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

大模型越来越常被用于金融、法律、体育等历史事件预测任务，而这类任务通常需要在某个截止日期之前完成“回测”，即只能使用当时可获得的信息来推断结果。现实中，模型很容易把训练阶段学到的截止日期之后的知识带入推理过程，造成“时间泄漏”，从而虚高预测准确率并破坏评测有效性。现有提示约束、知识遗忘或事后校验方法，要么压不住与答案强相关的泄漏信息，要么无法处理“同一事实在不同截止日期下合法性不同”的实例级约束，因此值得专门研究如何让模型学会按时间条件选择证据。

#### 方法概述和架构

论文提出 TEMPO（Temporal Enforcement via Mode-Separated Policy Optimization），用强化学习把“时间纪律”直接训练进模型行为中。它的核心是双模式奖励：先通过泄漏模式把含有截止日期之后信息的输出压到零，作为硬性前提；只有当一个训练组里的所有候选输出都不泄漏时，才切换到性能模式去优化任务准确率。训练时，模型以带截止日期的输入为条件，生成结构化输出，包含证据列表、推理过程和预测结果；随后由日期可行性验证器逐条检查证据是否越过截止日期，并据此决定当前组进入哪一种模式。优化上，作者采用基于 GRPO 的训练流程和 LoRA 微调，使模型在组内相对优势学习中逐步发现“既不泄漏又能完成预测”的推理策略；同时还给出了收敛与单调降低泄漏的理论分析。

#### 实验结果分析

论文在三个预测任务上验证了方法，包括股票排序、薪资预测和法律结果预测，并在两种模型规模上与多种基线方法比较；评价指标主要包括整体泄漏率 OLR、任务性能 Perf 和覆盖率。结果显示，TEMPO 能把泄漏率从 2%–13% 降到 0.6%–3.7%，说明其确实显著抑制了截止日期后的信息混入推理。与此同时，在前置信号较强的任务上，任务性能还能提升 6%–13%；而在仅靠合法信息本来就难以预测的任务上，性能则基本得以维持。正文节选还提到作者做了分任务分析、两阶段课程验证和案例研究，但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

在历史事件上回测大语言模型时，模型必须只基于指定截止日期之前可获得的信息进行推理。然而，模型经常把预训练中学到的截止日期之后的知识泄漏到推理中，从而抬高表面准确率，并削弱评测的有效性。基于提示词的约束在被抑制内容与预测结果存在因果关联时会失效，而知识遗忘也无法解决这一问题，因为时间合规是实例级的：同一个事实在某个截止日期下可能是合法证据，在另一个截止日期下却是违规信息。与其擦除知识，不如让模型学会“时间纪律”：根据每个实例的截止日期选择证据。我们提出 TEMPO（Temporal Enforcement via Mode-separated Policy Optimization），通过两项贡献来训练这种纪律：（1）一种双模式奖励，其中泄漏模式先将截止日期之后的陈述压到零，作为性能优化前的硬性前提；（2）一种基于 GRPO 的训练流程，使模型能够发现时间上合法的推理策略。我们证明，该训练过程会单调降低泄漏率，收敛到无泄漏最优解，并在实现合规后提升任务性能。在三个预测任务和两种模型上，TEMPO 将泄漏率从 2%–13% 降低到 0.6%–3.7%，在存在强预截止日期信号的条件下任务性能提升 6%–13%，而在仅凭合法信息本就难以完成预测的任务上则保持性能不变。

</details>

---

### [[20_Research/Papers/强化学习/Safe_Continual_Reinforcement_Learning_under_Nonstationarity_via_Adaptive_Safety_Constraints|Safe Continual Reinforcement Learning under Nonstationarity via Adaptive Safety Constraints]]

![[assets/2605.18842_figure.png|800]]

- **arXiv**: [2605.18842](https://arxiv.org/abs/2605.18842)
- **PDF**: https://arxiv.org/pdf/2605.18842
- **详细分析**: [[20_Research/Papers/强化学习/Safe_Continual_Reinforcement_Learning_under_Nonstationarity_via_Adaptive_Safety_Constraints|Safe Continual Reinforcement Learning under Nonstationarity via Adaptive Safety Constraints]]
- **作者**: Timofey Tomashevskiy
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

在非平稳环境中做安全强化学习，智能体不仅要“学会做任务”，还要在环境动态、代价函数或安全约束变化时持续保持安全，这在自动驾驶、机器人控制等场景里尤为重要。现有安全强化学习方法通常默认约束固定、环境稳定，因此在分布偏移下容易出现约束失效，或者在环境变化过快时来不及把新的安全要求落实到决策层。本文值得关注之处在于，它把安全问题从“固定约束”推进到“随上下文和变化速度自适应更新的约束构造”，更贴近真实连续部署场景。

#### 方法概述和架构

论文提出 LILAC+，这是一个面向非平稳持续强化学习的预测式安全层，核心由三类自适应约束组成。第一类是基于上下文的约束（CB），先通过上下文检测器从交互历史中估计当前上下文，再由预测器推断未来一段时间的安全相关上下文，用这些上下文去调整原有安全约束。第二类是适应速度约束（AS），把“环境变化所需的安全适应速度”与“智能体可达到的适应能力”进行比较，当变化快于可安全适应的能力时就收紧约束。第三类是软到硬的预算约束（SH），把累计安全预算转成可在单步决策时执行的局部状态级约束，从而支持运行时屏蔽危险动作。方法上，这三类约束共享同一条上下文预测管线，既可以生成策略层的安全正则或约束项，也可以生成动作层的硬安全集合；推理时输入当前观测历史、当前/未来上下文预测、安全预算与适应速度比值，输出用于策略学习与安全动作选择的约束。

#### 实验结果分析

作者在 highway-env 的 merge-v0 驾驶任务上进行了实验，覆盖 stationary、seen nonstationary 和 unseen nonstationary 三种条件，并与无约束基线和固定约束基线进行比较。结果表明，LILAC+ 在分布偏移下能显著减少安全违规，同时保持与基线相比有竞争力的任务回报。节选文本中没有给出具体数值，但明确指出该框架在违规次数与累计安全代价方面更优。论文也强调，结论依赖于上下文估计质量以及约束是否可被实际执行。

<details>
<summary>完整摘要</summary>

非平稳环境中的安全强化学习需要随着环境条件变化而自适应的安全机制。标准安全强化学习方法通常假设约束固定或环境条件稳定，而在分布偏移下这些假设会失效。为此，我们提出 LILAC+，一个面向非平稳持续强化学习的安全框架，它结合了三种自适应安全机制：基于上下文的安全约束、适应速度约束，以及预算到状态的安全执行。基于上下文的约束利用推断和预测到的环境上下文来调整安全要求；适应速度约束在环境变化速度超过智能体安全适应能力时收紧安全要求；预算到状态执行则将累计安全要求转换为可在决策时执行的局部状态级控制约束。三者结合后，为持续强化学习中的前瞻性与响应式安全自适应提供了统一方案。我们在模拟驾驶环境中，于 stationary、seen nonstationary 和 unseen nonstationary 条件下评估该框架。结果显示，与无约束和固定约束基线相比，自适应安全约束能够显著减少分布偏移下的安全违规，同时保持有竞争力的任务性能。这些结果表明，安全持续强化学习不仅需要响应当前状态信息，还需要响应预测到的环境上下文、适应需求以及剩余安全预算的自适应约束机制。

</details>

---

### [[20_Research/Papers/强化学习/From_Cumulative_Constraints_to_Adaptive_Runtime_Safety_Control_for_Nonstationary_Reinforcement_Learning|From Cumulative Constraints to Adaptive Runtime Safety Control for Nonstationary Reinforcement Learning]]

![[assets/2605.18841_figure.png|800]]

- **arXiv**: [2605.18841](https://arxiv.org/abs/2605.18841)
- **PDF**: https://arxiv.org/pdf/2605.18841
- **详细分析**: [[20_Research/Papers/强化学习/From_Cumulative_Constraints_to_Adaptive_Runtime_Safety_Control_for_Nonstationary_Reinforcement_Learning|From Cumulative Constraints to Adaptive Runtime Safety Control for Nonstationary Reinforcement Learning]]
- **作者**: Timofey Tomashevskiy
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

在强化学习的安全控制中，常见做法是用累积代价约束来限制长期风险，但这类轨迹级约束并不能直接阻止执行过程中的单步危险动作，尤其在环境非平稳、分布持续变化时更容易失效。对于自动驾驶合流、交叉口通行等场景，同一个动作在不同交通密度或不同阶段下的风险可能差异很大，固定的状态阈值往往要么过于保守，要么不够安全。本文关注的是如何把“累计安全预算”转化为“运行时可执行的局部安全控制”，因此具有较强的现实部署意义。

#### 方法概述和架构

论文提出 Constraint Projection Safety Shield（CPSS），是一种运行时安全屏蔽机制，用于把累计安全预算投影为随时间变化的状态级可接受风险阈值。具体来说，系统先跟踪已消耗的安全代价，计算剩余预算，再根据剩余步数将预算映射为基础阈值；随后结合上下文信号（如交通密度及其短期变化）对阈值进行自适应修正，使高风险或快速变化的场景下约束更严格。推理时，RL策略先给出候选动作，CPSS 评估该动作的预测安全代价；若超过当前阈值，则用备选安全动作替换，从而保证执行动作满足局部可接受条件。方法不需要改写底层 DQN 的训练过程，主要在执行阶段插入过滤器，因此可与现有强化学习算法直接组合。论文还给出理论分析，讨论了局部可接受性、累计代价上界、干预频率与性能损失之间的关系。

#### 实验结果分析

作者在 highway-env 的多个驾驶任务上验证了 CPSS，包括 merge-v0、highway-v0、intersection-v0 和 racetrack-v0，并在静态以及多种非平稳强度下进行评估。对比基线主要是不加屏蔽的 DQN，同时报告碰撞率、近距离风险和最小车距等指标。结果显示，CPSS 能显著降低碰撞与近距离危险事件，并在保证选择性干预的同时提升安全裕度；全文摘要给出的平均碰撞率从 0.0822 降至 0.0069，对应 91.6% 的相对下降。节选文本未给出更细的消融数值，但从描述看，方法在不同环境和非平稳设置下都表现出较好的泛化性。

<details>
<summary>完整摘要</summary>

强化学习中的安全性通常通过累积代价约束来规定，但这类轨迹级保证并不能直接阻止单个危险决策，尤其是在非平稳环境中更是如此。在持续学习和非平稳设置下，难度会进一步放大，因为同一个动作在不同上下文中的风险可能变化，而固定的状态级阈值要么过于保守，要么过于宽松。我们提出 Constraint Projection Safety Shield（CPSS），一种运行时机制，它将累积安全预算转换为执行过程中的自适应状态级控制约束。CPSS 跟踪剩余安全预算，将其投影为一个随时间变化的可接受风险阈值，并过滤掉那些预测安全代价超过当前阈值的策略动作。该阈值会利用上下文信号在线调整，使得在更苛刻或变化更快的场景中约束更严格，而在可用安全预算充足时则更宽松。我们分析了由此得到的加屏蔽策略，并表明该机制能够保证已执行动作满足逐状态阈值要求，诱导有限时域的累积代价上界，并给出一个以干预频率和单步奖励偏差为核心的性能损失界。我们在 highway-env 上的非平稳高速公路汇入场景中评估了 CPSS。跨多个随机种子，CPSS 显著降低了基于近距离的安全违规，并增加了分离裕度，同时只选择性地干预，而不是压制学习到的策略。结果支持将自适应的预算到阈值投影作为一种实用方法，用于把累积安全规范转化为持续强化学习系统中有效的局部安全控制。

</details>

---
