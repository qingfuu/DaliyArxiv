# cs.LG | Machine Learning | 2026-05-21

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/强化学习/roto_2.0_The_Robot_Tactile_Olympiad|roto 2.0: The Robot Tactile Olympiad]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2605.21429](https://arxiv.org/abs/2605.21429)
- **PDF**: https://arxiv.org/pdf/2605.21429
- **详细分析**: [[20_Research/Papers/强化学习/roto_2.0_The_Robot_Tactile_Olympiad|roto 2.0: The Robot Tactile Olympiad]]
- **作者**: Elle Miller, Jayaram Reddy, Ayush Deshmukh, Trevor McInroe, David Abel, Oisin Mac Aodha, Sethu Vijayakumar
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型, 大模型
- **相关性评分**: 2.22（加权：具身智能 0.3，大模型 0.1，强化学习 0.36，世界模型 0.16，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

触觉强化学习（tactile-based RL）旨在让机器人仅依靠本体感知与触觉完成精细操作，尤其适合对视觉受限、遮挡严重或需要高精度接触反馈的场景，如灵巧抓取、装配和旋转操作。然而，现有研究往往分散在不同任务与平台上，并且过度集中于“姿态/朝向”类任务，导致评测标准不统一、算法比较困难，也限制了该方向的进一步发展。roto 2.0 试图为触觉强化学习建立更标准化、更具挑战性的基准，因此具有较强的研究价值。

#### 方法概述和架构

本文提出 Robot Tactile Olympiad 第二版，即 roto 2.0，这是一个支持 GPU 并行的触觉强化学习基准。该基准覆盖四种不同的机器人形态，关节自由度范围从16-DOF到24-DOF，用于统一评估不同机械结构上的学习能力。与以往基准不同，roto 2.0 面向端到端的“盲操作”，输入仅包含本体感知和触觉信号，不使用状态信息，也不依赖蒸馏。作者围绕 Baoding ball 旋转等任务构建环境，并提供经过稳健调参的基线方法与开源环境，以便研究者直接比较算法，而不是把大量精力消耗在繁琐的RL参数调优上。

#### 实验结果分析

实验表明，基于该基准训练的盲代理在 Baoding ball 旋转任务上取得了显著提升，能够在10秒内完成13次旋转。作者将这一结果与当前最先进方法的速度对比，指出其达到约一个数量级的性能提升。由于正文节选未提供更详细的实验表格与消融结果，可见文本未给出具体数值，但整体结论是 roto 2.0 能有效推动触觉RL从零散任务评测走向更统一、更具挑战性的标准化比较。

<details>
<summary>完整摘要</summary>

基于触觉的强化学习（RL）目前受到研究分散以及过度集中于朝向类任务的限制。我们提出 Robot Tactile Olympiad（&lt;texttt{roto 2.0}&gt;）第二版，这是一个经过 GPU 并行化的基准，用于在四种不同的机器人形态（16-DOF 到 24-DOF）上标准化触觉强化学习。不同于以往基准，roto 2.0 聚焦于端到端的“盲”操作，仅使用本体感知和触觉感知，不使用状态信息，也不进行蒸馏。我们展示了显著的性能跃升：我们的盲代理在10秒内完成了13次 Baoding ball 旋转，速度比当前最先进方法快一个数量级。通过开源我们的环境和经过稳健调参的基线方法，我们降低了研究门槛，使研究者能够将重点放在基础算法挑战上，而不是耗费在繁琐的强化学习调参上。网站：https://elle-miller.github.io/roto/

</details>

---

### [[20_Research/Papers/大模型/What_Twelve_LLM_Agent_Benchmark_Papers_Disclose_About_Themselves_A_Pilot_Audit_and_an_Open_Scoring_Schema|What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2605.21404](https://arxiv.org/abs/2605.21404)
- **PDF**: https://arxiv.org/pdf/2605.21404
- **详细分析**: [[20_Research/Papers/大模型/What_Twelve_LLM_Agent_Benchmark_Papers_Disclose_About_Themselves_A_Pilot_Audit_and_an_Open_Scoring_Schema|What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema]]
- **作者**: Mahdi Naser Moghadasi, Faezeh Ghaderi
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

这篇论文聚焦于大模型 agent 基准评测的“可复现性披露”问题：同一个基准、同一个模型名，不同论文给出的结果却可能相差很大，而读者往往无法判断差异来自 scaffolding、采样设置、子集选择还是评测器版本。作者指出，现有论文和仓库通常不足以让下游读者还原一次 agent 评测的真实执行过程，尤其在工具调用、环境交互和闭源 API 场景下更为严重。由于 agent 评测已成为大模型研究和榜单比较的核心环节，这类信息缺口会直接影响结果可比性，因此值得专门审计。

#### 方法概述和架构

作者设计了一个小型审计 schema，用来逐篇检查论文对一次 agent 评测的披露程度。该 schema 包含五个字段：基准身份、评测 harness 规格、推理设置、成本报告、失败分类，并配套编写了评分 codebook 来处理边界情况。输入是论文正文和公开仓库，输出是每篇论文在各字段上的离散评分 {0, 0.5, 1} 及其平均值；整个过程不需要实际运行模型，而是由审计者直接阅读材料完成。作者将该 schema 应用于 12 篇经典基准论文，其中 8 篇是 agent 基准、4 篇是传统静态基准，并同时发布了 JSON Schema、Markdown 版 codebook 和 CSV 原始评分表。

#### 实验结果分析

审计结果显示，8 篇 agent 基准论文的平均披露得分为 0.38，低于 4 篇传统静态基准论文的 0.66，说明 agent 评测的可复现性披露显著更弱。最明显的短板出现在成本报告上：8 篇 agent 论文中没有一篇以任何形式披露推理成本；在 harness 规格上，也没有一篇完整披露带内容地址的容器镜像环境。论文还总结了若干常见失败模式，如 harness 漂移、静默子集化、解码设置不充分、代价缺失和失败分析不结构化；节选中未给出更细的实验数值或消融结果。

<details>
<summary>完整摘要</summary>

我们阅读了 12 篇知名的 LLM agent 基准论文，并按维度记录每篇论文实际说明了其评测是如何执行的。这样做的动机来自一个很常见的困扰：两篇论文在同一个基准上、用同一个模型名报告结果，却彼此不一致，而你无法判断原因究竟是 scaffold、采样设置、子集、还是评测器版本。很多情况下，已公开的材料并不能回答这个问题。本论文是对这次尝试的实施报告。我们设计了一个小型审计 schema（5 个字段：基准身份、harness 规格、推理设置、成本报告、失败分类），编写了一个 scoring codebook 来处理试点评分中遇到的边界情况，将其应用到 12 篇经典论文（8 篇 agent、4 篇传统静态基准），并记录了我们的发现。我们评分的是 agent 运行的披露程度，而不是其正确性；我们也不主张“披露得更多”就意味着结果可信。8 篇 agent 基准论文的平均审计得分为 0.38（满分 1.0），4 篇传统静态基准论文的平均得分为 0.66；最大的差距出现在成本披露上（8 篇 agent 论文中没有一篇以任何形式披露推理成本）以及 harness 规格上（8 篇 agent 论文中没有一篇完整披露带内容地址的容器镜像形式的评测环境）。我们将 schema 以 JSON Schema 文件形式发布，将 codebook 以 Markdown 文档形式发布，并将原始评分表以 CSV 形式发布。评分由单一审计者一次完成；多审计者审计是自然的下一步，我们也讨论了这会带来什么变化。

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning-based_Control_via_Y-wise_Affine_Neural_Networks_Comparative_Case_Studies_for_Chemical_Processes|Reinforcement Learning-based Control via Y-wise Affine Neural Networks: Comparative Case Studies for Chemical Processes]]

![[assets/2605.21211_figure.png|800]]

- **arXiv**: [2605.21211](https://arxiv.org/abs/2605.21211)
- **PDF**: https://arxiv.org/pdf/2605.21211
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning-based_Control_via_Y-wise_Affine_Neural_Networks_Comparative_Case_Studies_for_Chemical_Processes|Reinforcement Learning-based Control via Y-wise Affine Neural Networks: Comparative Case Studies for Chemical Processes]]
- **作者**: Austin Braniff, Yuhe Tian
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

本文聚焦于化工过程控制中的强化学习控制问题，目标是在连续搅拌釜反应器（CSTR）、四罐系统和多级萃取塔等典型流程系统中，用RL实现闭环控制。尽管RL在机器人和决策任务中表现突出，但在化工控制领域的落地一直较少，核心原因是训练过程中的安全性难以保证、策略可解释性不足，以及训练可靠控制器通常需要大量数据和较长时间。作者认为，这些痛点使得传统RL方法很难直接用于工业场景，因此需要一种既能提供可信初始策略、又能减少无效探索与训练成本的方法。

#### 方法概述和架构

论文提出基于Y-wise Affine Neural Network（YANN）的RL控制方法，并以YANN-DDPG作为核心实现。其思路是先对过程系统做线性化或系统辨识，再基于线性模型构建MPC问题并求解多参数MPC，从而得到显式的分段仿射控制律；这个控制律随后被用来初始化YANN-actor，使其一开始就等价于一个有理论依据的控制器。与此同时，作者还根据线性模型和MPC权重构造YANN-critic，使其初始时近似线性系统的显式Q函数，再通过后续训练扩展到非线性表达能力。训练流程上，YANN-DDPG沿用DDPG的actor-critic更新机制，但取消随机探索步骤，改为从这一套可解释、可信的初始化出发持续优化策略。最终输出的是针对给定过程状态的控制动作，可直接用于闭环控制。

#### 实验结果分析

作者在PC-Gym库公开的三个过程工程案例上进行比较实验，包括CSTR、四罐系统和多级萃取塔，并与PPO、SAC、DDPG、TD3以及NMPC进行对比，评价指标包括ISE、ITAE、稳态误差和累计代价。结果表明，YANN-RL能够显著减少训练时间和所需数据量，并且在化工过程系统中具备更高的部署可信度。与常见RL算法相比，其收敛更快、样本效率更高；同时性能可逼近NMPC，而不需要完整非线性模型。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

本文提出一种高效且具备实际可部署性的强化学习（RL）控制方法，用于化工过程系统中的控制任务。之所以需要这样的方案，是因为该领域尚未广泛采用RL控制，主要受制于对RL算法可信度的担忧，以及训练可靠智能体所需时间较长等问题。为应对这些挑战，我们利用一种称为Y-wise Affine Neural Network（YANN）的RL算法家族；该方法是我们在先前工作中开发的。通过对actor和critic网络进行策略性初始化，YANN-RL能够在控制方案中提供更有信心且更易解释的起始点。我们将这种基于RL的控制方法应用于PC-Gym库中公开提供的三类流程工程案例：(i) 连续搅拌釜反应器（CSTR），(ii) 四罐系统，以及 (iii) 多级萃取塔。并将该方法与多种流行的RL算法（PPO、SAC、DDPG和TD3）进行比较，同时以非线性模型预测控制（NMPC）作为基准。案例研究表明，YANN-RL可以大幅减少训练时间和所需数据，能够以更高信心部署到化工过程系统中，并且在不需要完整非线性模型知识的情况下，性能可接近NMPC。

</details>

---

### [[20_Research/Papers/强化学习/Domain-Adaptable_Reinforcement_Learning_for_Code_Generation_with_Dense_Rewards|Domain-Adaptable Reinforcement Learning for Code Generation with Dense Rewards]]

![[assets/2605.21180_figure.png|800]]

- **arXiv**: [2605.21180](https://arxiv.org/abs/2605.21180)
- **PDF**: https://arxiv.org/pdf/2605.21180
- **详细分析**: [[20_Research/Papers/强化学习/Domain-Adaptable_Reinforcement_Learning_for_Code_Generation_with_Dense_Rewards|Domain-Adaptable Reinforcement Learning for Code Generation with Dense Rewards]]
- **作者**: Erfan Aghadavoodi Jolfaei, Daniel Maninger, Abhinav Anand, Mert Tiftikci, Mira Mezini
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型
- **相关性评分**: 1.72（加权：强化学习 1.16，世界模型 0.16，机器人 0.4）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

大语言模型已经展现出较强的自动代码生成能力，但生成结果往往缺乏对正确性、质量、安全性以及领域约束的稳定保证。论文特别关注机器人场景：当代码被用于规划和执行动作时，模型不仅要“能写出来”，还必须理解环境状态和物理约束，否则很容易生成不可执行或不安全的程序。现有基于强化学习的代码优化方法多依赖稀疏的序列级奖励，难以把执行反馈准确归因到具体代码片段，导致学习效率和领域适配能力受限。因而，这项工作值得关注之处在于，它尝试把执行结果、静态检查和领域反馈统一纳入更细粒度的强化学习训练。

#### 方法概述和架构

论文提出了一个基于PPO的 Domain-Adaptable Reinforcement Learning 框架，用于对预训练代码大模型进行强化学习微调。整个流程分为三步：Rollout 阶段逐 token 生成代码并进行语法约束检查；Evaluation 阶段把多种奖励信号聚合成最终回报；Optimization 阶段利用回报和价值函数计算优势并更新策略模型与价值模型。奖励设计是核心，包含语法正确性、代码风格与漏洞检测、与参考模型的KL正则，以及可按任务定制的奖励项。论文在一般代码生成任务中加入单元测试结果和 DFG 匹配，在机器人任务中加入 RoboSim 的仿真反馈，使同一套框架能够适配不同领域。为了缓解稀疏奖励问题，作者还设计了 token-level reward attribution，把终端执行结果尽量映射回产生错误或成功的 token/token span，从而为每个生成位置提供更密集的学习信号。

#### 实验结果分析

实验在 MBPP、MBPP+ 和 RoboEval 上进行，基线是 Qwen2.5-Coder-1.5B-Instruct，指标包括 pass@1 以及机器人任务中的执行错误与完成情况。结果显示，该方法在 MBPP 上的 pass@1 从 0.460 提升到 0.653，在 MBPP+ 上从 0.413 提升到 0.556，说明密集奖励能显著改善函数正确性与鲁棒性。机器人任务中，仿真不可执行/执行失败显著减少，文中给出的总体结论是执行失败下降了 51%，并且模型从大量不可执行输出转向更多可在仿真器中运行的程序。正文还指出，相比只做 Robo-Instruct 的训练方式，这种结构化强化学习带来的相对增益更大，体现了方法对领域适配的优势。

<details>
<summary>完整摘要</summary>

大型语言模型在自动代码生成方面展现出很强的潜力，但它们并不能保证生成结果在正确性、质量、安全性以及领域特定约束方面都令人满意。以机器人为例，代码生成正越来越多地用于动作规划与执行，在这种场景下，对环境和物理约束的感知至关重要。为了让代码生成型LLM适应多样化需求，包括领域特定要求，我们提出了一个强化学习框架，使用近端策略优化（PPO）对预训练LLM进行微调。我们可定制的执行感知奖励公式能够同时捕捉并优化语法、功能正确性、代码风格、安全性以及仿真器可执行性。我们还设计了一个 token 级奖励映射机制，使执行结果能够更有效地归因到生成的 token 上。该框架在通用代码生成任务（MBPP/MBPP+）和机器人程序合成任务（RoboEval）上进行了评估。结果表明，该方法在功能正确性和仿真器可执行性方面都有显著提升，其中 MBPP 的 pass@1 绝对提升了 19%，RoboEval 上的执行失败减少了 51%。这些结果说明，结构化强化学习能够有效地使语言模型对齐到正确的程序生成以及领域特定要求上。

</details>

---

### [[20_Research/Papers/大模型/Learning_First_Integrals_via_Backward-Generated_Data_and_Guided_Reinforcement_Learning|Learning First Integrals via Backward-Generated Data and Guided Reinforcement Learning]]

![[assets/2605.21160_figure.png|800]]

- **arXiv**: [2605.21160](https://arxiv.org/abs/2605.21160)
- **PDF**: https://arxiv.org/pdf/2605.21160
- **详细分析**: [[20_Research/Papers/大模型/Learning_First_Integrals_via_Backward-Generated_Data_and_Guided_Reinforcement_Learning|Learning First Integrals via Backward-Generated Data and Guided Reinforcement Learning]]
- **作者**: Jingfeng Zhong, Zhengxiang Liu, Zhijie Wang, Shuai Li
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

这篇论文关注的是动力系统中“第一积分”的自动发现，即寻找沿系统轨迹保持不变的守恒量，这对理解守恒律、求解微分方程以及分析物理系统都很重要。现有符号计算工具和大模型在这类任务上表现受限，核心原因是高质量标注数据稀缺，而且成功求解往往依赖较强的数学直觉与经验搜索。论文因此值得关注之处在于，它尝试把第一积分发现转化为一个可规模化的数据驱动学习问题，并探索了大模型、合成数据与强化学习的组合路线。

#### 方法概述和架构

作者提出了一个名为 FISolver 的LLM求解器，整体流程包括数据生成、模型训练和推理验证三部分。数据生成上，论文既使用“正向生成”从可被专用求解器处理的方程中收集样本，也提出“Backward Generation”算法：先随机采样第一积分，再反推构造与之相容的微分方程，从而批量得到“微分方程—第一积分”配对数据。对于特定复杂系统，作者还设计了数据合成与数据混合策略：先用少量已知样本微调出一个生成模型 FIGenerator，再生成更多合成第一积分并反向构造数据，以增强对稀缺难题族的适应能力。模型训练上，先对一个紧凑的数学LLM进行监督微调，再用基于 Levenshtein Distance 的形状奖励进行强化学习，并结合结构与有效性惩罚项，强化模型输出在符号层面的精确性。推理阶段采用 beam search 生成多个候选第一积分，再逐个进行符号验证，直到找到正确答案。

#### 实验结果分析

实验在标准的第一积分发现基准上进行，重点比较了 FISolver、基础模型、参数更大的数学LLM以及 Mathematica 等商业求解器。论文声称 FISolver 以更低的计算成本，在困难基准上显著超过了更大规模模型和 Mathematica；在 Hard 集合上，beam size 为 70 时可达到 63.7%，而 Mathematica 为 23.3%。同时，强化学习带来的 Levenshtein Distance 奖励还能进一步提升性能，说明过程级引导对符号推理有实际增益。正文节选中未给出更完整的分数据集、分模型消融表格细节，部分具体数值在可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

发现第一积分对于理解动力系统中的守恒律具有基础性的科学意义。然而，由于高质量训练数据稀缺，而成功求解往往依赖数学直觉，现有符号计算工具和大语言模型（LLMs）在这一任务上仍然存在明显局限。为此，本文提出了 FISolver，一种基于LLM的求解器。首先，我们提出一种“Backward Generation（反向生成）”算法：通过从采样得到的积分出发反推出相应的微分方程，系统性地构建大规模的“微分方程—第一积分”配对数据集，从而缓解数据稀缺瓶颈。其次，我们对一个紧凑的数学模型进行监督微调，并进一步使用带有 Levenshtein Distance 形状奖励的强化学习来提升其性能。此外，我们还设计了数据合成与数据混合策略，使模型能够利用稀疏样本有效适应困难问题族。实验表明，FISolver 在计算成本显著更低的情况下，在具有挑战性的基准上明显优于更大的数学LLM以及 Mathematica 等商业求解器，这表明自动发现第一积分可以走出一条新的、数据驱动的路线。

</details>

---

### [[20_Research/Papers/强化学习/Advantage_Collapse_in_Group_Relative_Policy_Optimization_Diagnosis_and_Mitigation|Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation]]

![[assets/2605.21125_figure.png|800]]

- **arXiv**: [2605.21125](https://arxiv.org/abs/2605.21125)
- **PDF**: https://arxiv.org/pdf/2605.21125
- **详细分析**: [[20_Research/Papers/强化学习/Advantage_Collapse_in_Group_Relative_Policy_Optimization_Diagnosis_and_Mitigation|Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation]]
- **作者**: Xixiang He, Qiyao Sun, Ao Cheng, Xingming Li, Xuanyu Ji, Hailun Lu, Runke Huang, Qingyong Hu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

这篇论文关注的是 RLVR 框架下的 GRPO 在大语言模型数学推理训练中的一个关键失效模式：当同一组采样答案的奖励全都相同（全对或全错）时，组内方差消失，优势值接近 0，进而导致梯度几乎无法更新。由于这类“优势塌缩”在损失曲线和准确率上往往不明显，训练可能在不知不觉中浪费大量计算资源。作者指出，在 0.5B 到 14B 参数规模、多个数学推理基准上，这一现象都很普遍，因此值得作为训练诊断与修复问题单独研究。

#### 方法概述和架构

论文先定义了 Advantage Collapse Rate（ACR），用来统计一个训练 batch 中奖励方差低于阈值的样本组占比，从而量化“无效梯度”出现的频率。ACR 不需要额外前向推理，直接利用 GRPO 训练中已经计算出的组内奖励统计量，因此几乎没有额外开销。基于 ACR 的实时监控，作者提出 Adaptive Virtual Sample Policy Optimization（AVSPO）：当检测到某个组发生优势塌缩时，自动注入若干“虚拟奖励样本”，只参与优势归一化所需的均值和方差计算，不对应真实模型输出，也不参与策略梯度项。这样可以在不增加额外 rollout 的前提下，为原本塌缩的组重新构造非零优势，恢复可学习信号。论文还分析了虚拟样本的构造与自适应数量选择机制，使干预强度随 ACR 动态变化，从而在稳定训练和控制计算成本之间取得平衡。

#### 实验结果分析

作者在 0.5B 到 14B 不同规模模型、6 个数学推理基准上验证了方法，并以 GRPO 作为主要基线，同时考察了 MMLU-Pro 作为域外泛化任务。结果显示，早期 ACR 与最终性能呈强负相关，能够较好预测训练停滞与最终准确率；在所有模型规模上，AVSPO 相比 GRPO 将优势塌缩比例降低了 58%–63%，并带来 4–6 个百分点的一致准确率提升。实验还表明，该方法在域外任务上保持了泛化能力。节选文本中未给出更细的消融数值。

<details>
<summary>完整摘要</summary>

群相对策略优化（GRPO）是强化学习从可验证奖励（RLVR）框架中的一种代表性算法，在提升大语言模型（LLMs）的推理能力方面取得了很强的效果。然而，GRPO 容易出现优势塌缩（advantage collapse）这一失效模式：当同一组内的奖励是同质的（例如答案全对或全错）时，优势值会接近 0，梯度随之消失。为了解决这一问题，我们提出优势塌缩率（ACR），这是首个用于量化训练批次中无效梯度比例的诊断指标。在 0.5B 到 14B 参数规模的模型、数学推理基准上，我们发现 ACR 能强力预测训练停滞和最终性能。随后我们提出自适应虚拟样本策略优化（AVSPO），这是一种对 GRPO 的轻量扩展：它在实时 ACR 监控的指导下注入虚拟奖励样本，使模型能够从同质组中学习，而无需额外的模型 rollout。相较于 GRPO，AVSPO 将优势塌缩降低了 58%–63%，并在所有模型规模上带来一致的 4–6 个百分点准确率提升，同时在所评估的域外任务上保持了泛化能力。代码和数据集已公开，见 https://qingyonghu.github.io/AVSPO 。

</details>

---

### [[20_Research/Papers/强化学习/Beyond_the_Bellman_Recursion_A_Pontryagin-Guided_Framework_for_Non-Exponential_Discounting|Beyond the Bellman Recursion: A Pontryagin-Guided Framework for Non-Exponential Discounting]]

![[assets/2605.20996_figure.png|800]]

- **arXiv**: [2605.20996](https://arxiv.org/abs/2605.20996)
- **PDF**: https://arxiv.org/pdf/2605.20996
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_the_Bellman_Recursion_A_Pontryagin-Guided_Framework_for_Non-Exponential_Discounting|Beyond the Bellman Recursion: A Pontryagin-Guided Framework for Non-Exponential Discounting]]
- **作者**: Hojin Ko, Jeonggyu Huh
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

强化学习和连续时间控制通常依赖 Bellman 递推，但这一路线默认使用指数折扣；一旦折扣变成常见于人类偏好、寿命过程中的非指数形式，标准动态规划就会失效。作者指出，指数折扣之所以成立，依赖于“可乘性”和“时间齐次性”的脆弱交汇，破坏任一性质都会让递推结构崩塌。对于超几何折扣、survival discount 等非指数场景，现有基于值函数或 critic 的方法往往需要扩展 HJB、BSVIE 或其他非局部方程，计算上更脆弱，也更难扩展到高维问题，因此这篇工作值得关注。

#### 方法概述和架构

论文提出 Pontryagin-Guided Direct Policy Optimization（PG-DPO），核心思路是不再围绕 Bellman 递推做价值分解，而是转向 Pontryagin Maximum Principle（PMP）的变分视角。方法将“决策时刻锚定”的折扣核显式纳入目标函数，在每个锚点上构造对应的 Hamiltonian，并通过伴随方程刻画最优/均衡控制。训练上分为两阶段：Stage 1 用 Monte Carlo rollout 和 BPTT 对策略网络做 warm-start，直接优化路径回报；Stage 2 通过 Adjoint-MC projection 估计 costate（伴随变量），再在动作空间执行 Hamiltonian 最大化，从而把 PMP 的点态最优条件落实为可计算的投影步骤。论文还强调 BPTT 可视为随机伴随估计器，这使得该方法可以接入可微 world model 或物理仿真器，在不依赖 Bellman 递推的情况下完成策略优化。

#### 实验结果分析

作者在多维 hyperbolic discount 和 survival-discount 基准上进行了测试，涵盖了生存折扣目标控制、Merton 问题（超几何折扣）以及时间变化厌恶的资源分配等任务。实验对比了方程驱动求解器与 critic-based 基线，结果表明 PG-DPO 在精度和稳定性上更优，尤其是在传统 Bellman/critic 路线发散或失效的场景中表现更稳。正文节选中未给出具体数值，但结论显示该方法在非指数折扣下比现有深度求解器更具可扩展性，并能更好地降低 Hamiltonian residual。

<details>
<summary>完整摘要</summary>

大多数基于价值函数和 actor-critic 的强化学习方法都依赖 Bellman 式递推，但在非指数折扣下，这类递推会失效，而非指数折扣在人的偏好和生存过程里很常见。我们表明，这种失效是结构性的：指数折扣正处在“可乘性”和“时间齐次性”的脆弱交汇处，破坏任一性质都会使标准动态规划失效。为此，我们提出 Pontryagin-Guided Direct Policy Optimization（PG-DPO），这是一种变分框架，放弃递推结构，并将 Pontryagin Maximum Principle 与 Monte Carlo rollout 结合起来，通过 Adjoint-MC 投影强制逐点 Hamiltonian 最大化。在多维 hyperbolic 折扣和 survival-discount 基准上，PG-DPO 在方程驱动求解器和 critic 基线发散时，仍能带来更高的精度与稳定性。

</details>

---

### [[20_Research/Papers/大模型/PlexRL_Cluster-Level_Orchestration_of_Serviceized_LLM_Execution_for_RLVR|PlexRL: Cluster-Level Orchestration of Serviceized LLM Execution for RLVR]]

![[assets/2605.20863_figure.png|800]]

- **arXiv**: [2605.20863](https://arxiv.org/abs/2605.20863)
- **PDF**: https://arxiv.org/pdf/2605.20863
- **详细分析**: [[20_Research/Papers/大模型/PlexRL_Cluster-Level_Orchestration_of_Serviceized_LLM_Execution_for_RLVR|PlexRL: Cluster-Level Orchestration of Serviceized LLM Execution for RLVR]]
- **作者**: Yiqi Zhang, Fangzheng Jiao, Tian Tang, Boyu Tian, Hangyu Wang, Qiaoling Chen, Guoteng Wang, Zhen Jiang, Peng Sun, Ping Zhang, Xiaohe Hu, Ziming Liu...
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

RLVR（带可验证奖励的强化学习）近年来显著提升了大模型的推理能力，尤其适用于数学、逻辑与规划等需要明确反馈的任务，也正在推动工具使用型与智能体型LLM系统的发展。问题在于，这类训练流程往往包含长尾式 rollout、工具调用阻塞以及 rollout 与训练之间资源需求不对称，导致 GPU 大量空闲。论文指出，这种低效不是单个作业内部优化就能彻底解决的局部问题，而是训练结构本身带来的系统性瓶颈，因此很值得关注。

#### 方法概述和架构

论文提出 PlexRL，一个面向 RLVR 的集群级运行时，用于对“服务化”的 LLM 执行进行跨作业复用与调度。其核心思路是把算法控制与模型执行底座解耦：各 RL 作业不再直接管理私有模型实例，而是通过统一的服务接口发起 rollout、训练和相关函数调用请求。系统在集群层集中管理模型放置、状态迁移与函数级调度，并在严格的 affinity 约束下尽量避免昂贵的模型迁移。为此，PlexRL 设计了远程执行抽象、时空资源建模、作业放置策略、运行时调度器以及模型状态管理器，用于协调参数、梯度、优化器状态等的大模型状态驻留、物化、同步与迁移，并将这些状态管理与执行过程重叠起来。整体上，它通过在不同 RLVR 作业之间切分 LLM 执行时间片，把单个作业内不可避免的空闲期转化为集群层面的可利用资源。

#### 实验结果分析

作者在代表性的 RLVR 工作负载上评估了 PlexRL，比较了不同部署与调度方式下的端到端成本效率和集群容量利用情况。结果表明，PlexRL 能显著提升有效集群容量，并且在保持算法灵活性的同时，将用户 GPU-hour 成本最高降低 37.58%。从正文节选可见，论文还分析了 split、colocated 和 asynchronous rollout 等常见方案的结构性低效，并通过实验验证 PlexRL 对这些空闲间隙的回收能力；但节选中未给出更完整的具体数值细节。

<details>
<summary>完整摘要</summary>

近年来，带可验证奖励的强化学习（RLVR）已经为大语言模型（LLM）解锁了强大的推理能力，并引发了对新算法与新数据的快速探索。然而，RLVR 训练的效率一向很低：长尾式 rollout、由工具调用引起的停顿，以及 rollout 与训练之间不对称的资源需求，会带来大量无法通过作业内局部优化消除的空闲时间，例如同步流水线、异步 rollout 或共置执行等方法都难以彻底解决。我们认为，这种低效具有结构性。虽然单个 RLVR 作业内的空闲间隙不可避免，但这些空闲在不同作业之间往往呈现反相关，因此可以在集群层面加以利用。基于这一观察，我们提出 PlexRL：一种用于在 RLVR 作业之间复用统一 LLM 服务的集群级运行时。PlexRL 通过在严格的 affinity 约束下集中管理模型放置、状态迁移和函数级调度，使不同作业之间的 LLM 执行可以时间片轮转，从而填补原本空闲的时段，而无需昂贵的模型迁移。我们的实现与评估表明，PlexRL 在保持算法灵活性并带来极低单作业开销的同时，显著提升了有效集群容量，并最多将用户 GPU-hour 成本降低 37.58%。

</details>

---

### [[20_Research/Papers/强化学习/Distributed_Direct_Preference_Optimization|Distributed Direct Preference Optimization]]

![[assets/2605.20696_figure.png|800]]

- **arXiv**: [2605.20696](https://arxiv.org/abs/2605.20696)
- **PDF**: https://arxiv.org/pdf/2605.20696
- **详细分析**: [[20_Research/Papers/强化学习/Distributed_Direct_Preference_Optimization|Distributed Direct Preference Optimization]]
- **作者**: Zhanhong Jiang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

基于偏好的强化学习（Preference-based RL）是对齐模型行为与人类判断的重要路线，尤其适用于大模型对齐、机器人交互和交互式决策等场景。DPO 作为一种不显式训练奖励模型的简化方法，近年来被广泛用于偏好对齐，但其在联邦学习与去中心化学习这类分布式环境中的收敛性质一直缺乏严格理论分析。本文关注的核心问题是：当偏好数据分散在不同用户、不同设备且存在明显非独立同分布时，DPO 的优化过程会如何变化，以及通信受限和异质性会怎样影响训练稳定性与效率。

#### 方法概述和架构

论文围绕分布式 DPO 展开分析，首先将个性化离线强化学习建模为“每个客户端拥有独立偏好分布”的场景，并据此刻画全局优化目标的结构。作者分别研究了两种训练范式：FedDPO 和 DecDPO，其中 FedDPO 对应带中心服务器的联邦优化，DecDPO 对应无中心服务器、仅通过邻居通信的去中心化优化。方法上，论文从 DPO 的 log-linear softmax 参数化出发，显式推导了平滑常数与梯度方差，并将其写成与轨迹长度、特征范数、温度系数和轨迹混合率相关的可解释形式。随后在联邦场景下，分析本地多步更新、客户端漂移、采样频率和偏好异质性对收敛速度的共同影响；在去中心化场景下，则通过通信图的谱性质刻画共识误差与优化速度之间的关系。整体流程是：客户端基于本地偏好对（偏好轨迹与非偏好轨迹）计算 DPO 损失并进行局部更新，服务器或邻居节点再进行参数聚合/混合，从而逐步逼近平稳点。

#### 实验结果分析

论文给出了 DPO 在分布式环境中的首次收敛性与时间复杂度分析，并分别建立了联邦和去中心化两类设置下的理论保证。实验部分在标准对齐基准上验证了理论结论，可见文本显示作者考察了参与率、模型陈旧性（staleness）以及网络拓扑等因素对训练的影响，但节选中未给出具体数值。结果表明，所提方法不仅具有严格的收敛分析，而且在实践中表现出较强的鲁棒性与可扩展性。文中还指出，异质性、本地步数和采样方式对性能的依赖是不可消除的，这为分布式偏好对齐提供了重要的下界认识。

<details>
<summary>完整摘要</summary>

基于偏好的强化学习（RL）是使策略与人类判断对齐的重要范式，但当偏好数据分散在异质用户之间时，其在分布式设置下的理论行为仍然缺乏充分理解。直接偏好优化（DPO）避免了显式奖励建模，但在联邦和去中心化训练中缺乏收敛保证；而在这类场景下，通信约束与非独立同分布（non-IID）的偏好会从根本上改变优化动力学。本文给出了 DPO 在分布式环境中的首次收敛性与时间复杂度分析。我们将个性化离线 RL 建模为具有用户特定偏好分布的情形，并刻画了由此诱导的全局优化景观。对于联邦 DPO，我们推导了收敛速率，量化客户端漂移、通信频率和偏好异质性的影响；对于去中心化 DPO，我们在一般通信图上建立了收敛性，并表明谱连通性决定了优化速度与共识形成的快慢。实验上，我们在标准对齐基准上验证了理论洞见，表明所提出的方法不仅具有很强的理论保证，而且在实践中也能提供稳健且可扩展的性能。代码仓库已提供。

</details>

---

### [[20_Research/Papers/世界模型/Time-Dependent_PDE-Constrained_Optimization_via_Weak-Form_Latent_Dynamics|Time-Dependent PDE-Constrained Optimization via Weak-Form Latent Dynamics]]

![[assets/2605.20639_figure.png|800]]

- **arXiv**: [2605.20639](https://arxiv.org/abs/2605.20639)
- **PDF**: https://arxiv.org/pdf/2605.20639
- **详细分析**: [[20_Research/Papers/世界模型/Time-Dependent_PDE-Constrained_Optimization_via_Weak-Form_Latent_Dynamics|Time-Dependent PDE-Constrained Optimization via Weak-Form Latent Dynamics]]
- **作者**: April Tran, Terry Haut, David Bortz, Youngsoo Choi
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel, Systems

#### 研究背景与动机

时间相关、由高维偏微分方程（PDE）约束的优化问题，常见于控制、设计和数字孪生场景，但每一次参数更新都需要重新做前向求解和灵敏度分析，计算代价极高。在多次查询的设计优化中，这种高保真求解往往成为瓶颈，限制了方法在复杂系统中的实际应用。本文关注如何把这类 PDE 约束优化转化为更便宜、但仍可用于梯度优化的降阶代理问题，因此具有明显的世界模型和强化学习相关价值。

#### 方法概述和架构

论文提出 WLaSDI（Weak-form Latent Space Dynamics Identification）驱动的时变 PDE 约束优化框架。其核心思路是先用编码器/降阶映射把高维状态轨迹压缩到低维潜空间，再在潜空间中学习一个带参数的动力学模型，用该模型替代昂贵的全阶 PDE 求解。与强形式方法不同，WLaSDI 采用弱形式系统辨识，通过测试函数投影和分部积分来识别潜在动力学，从而避免对训练轨迹做显式数值微分，提升了对噪声数据的鲁棒性。

#### 实验结果分析

作者在三个时变基准问题上验证了方法：热辐射传输下的 hohlraum 设计、双流不稳定性的 Vlasov–Poisson 系统，以及无粘 Burgers 方程。实验对比了 WLaSDI 与全阶优化、强形式 LaSDI 以及插值型代理等基线，重点考察了优化设计质量、对噪声训练数据的鲁棒性以及计算开销。结果表明，WLaSDI 能够给出准确的最优设计，并在噪声训练数据下保持稳定；可见文本未给出具体数值，但作者报告相较全阶优化最高可获得达五个数量级的加速。

<details>
<summary>完整摘要</summary>

高维、随时间变化的偏微分方程（PDE）所约束的优化问题需要反复进行前向求解和灵敏度求解，这使得在多次查询的设计与控制场景中，高保真优化在计算上往往不可承受。我们提出一种基于弱形式潜空间降阶建模的框架，用于加速基于梯度的 PDE 约束优化。所提出的方法建立在 Weak-form Latent Space Dynamics Identification（WLaSDI）之上：该方法将高维解轨迹压缩为低维潜变量表示，并通过弱形式系统辨识来识别参数化的潜在动力学。通过避免对训练轨迹进行显式数值微分，弱形式方法提高了对噪声数据的鲁棒性，并为优化提供了更可靠的代理动力学。我们对由该学习得到的潜在动力学建立了相应的降阶 PDE 约束优化问题，并推导了直接灵敏度和基于伴随法的梯度表达式，从而能够针对设计参数进行可扩展的梯度计算。我们在三个时变基准问题上展示了该框架：用于最优 hohlraum 设计的热辐射传输、双流不稳定性的 Vlasov–Poisson 系统，以及无粘 Burgers 方程。在这些例子中，WLaSDI 产生了准确的最优设计，在有噪声的训练数据下依然保持鲁棒，并带来了显著的计算节省，相比全阶优化最高可实现五个数量级的加速。这些结果表明，弱形式潜在动力学为复杂时变 PDE 系统的基于梯度优化提供了一种高效且抗噪的代理基础。

</details>

---

### [[20_Research/Papers/强化学习/Compositional_Transduction_with_Latent_Analogies_for_Offline_Goal-Conditioned_Reinforcement_Learning|Compositional Transduction with Latent Analogies for Offline Goal-Conditioned Reinforcement Learning]]

![[assets/2605.20609_figure.png|800]]

- **arXiv**: [2605.20609](https://arxiv.org/abs/2605.20609)
- **PDF**: https://arxiv.org/pdf/2605.20609
- **详细分析**: [[20_Research/Papers/强化学习/Compositional_Transduction_with_Latent_Analogies_for_Offline_Goal-Conditioned_Reinforcement_Learning|Compositional Transduction with Latent Analogies for Offline Goal-Conditioned Reinforcement Learning]]
- **作者**: Junseok Kim, Dohyeong Kim, Mineui Hong, Songhwai Oh
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

离线目标条件强化学习（offline goal-conditioned reinforcement learning, GCRL）希望只利用固定数据集训练出一个通用的“到达任意目标”的智能体，适用于机器人操控等数据昂贵、难以在线试错的场景。现有方法多依赖轨迹拼接，只能把时间上相邻的片段连接起来，因此更擅长组合“先后顺序上的行为”，却难以把同一任务在不同上下文中的经验迁移到新上下文中。本文关注的是另一类更一般的组合泛化问题：如何把在不同环境上下文中学到的任务内在“类比”重新组合，从而在未见过的上下文组合下完成目标。

#### 方法概述和架构

论文将这一问题形式化为 analogy transduction，即把任务内生的类比与当前上下文进行组合，生成新的可执行计划。为此，作者提出一种新的类比表示：用最优 temporal distance 场的“差分”来刻画状态到目标之间真正需要改变的任务内在位移，尽量屏蔽窗口开关、背景状态等任务外生上下文变化。理论上，这种表示被证明既对上下文变化保持不变，又足以支持最优到达目标。进一步地，作者指出实际难点在于测试时会出现训练中没见过的“类比—上下文”组合，因此提出 CTA（Compositional Transduction with latent Analogies），通过转导式分解把初始状态视为 anchor、把类比视为 displacement，并在价值函数与策略参数化中采用类似双线性转导的方式，实现对未见组合的外推。整体流程是：先从无奖励离线数据中学习类比表征，再把类比与上下文组合成可泛化的决策表示，最后用于离线 GCRL 推理和目标到达。

#### 实验结果分析

作者在 OGBench manipulation 环境上验证了 CTA，实验对象包括离线目标条件操控任务及其组合泛化设置。结果表明，CTA 相比不使用 analogy transduction 的既有方法有明显优势，平均性能提升约 42%。论文还做了多组分析，包括 OOC（out-of-combination）泛化、双类比表示、层级结构与子目标步长等消融，结论显示其泛化能力主要来自对未见类比—上下文组合的外推能力；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

组合泛化对于在新的上下文变化下到达未见目标至关重要，尤其是在离线目标条件强化学习（GCRL）中，智能体必须仅从有限数据中学习到一个通用的目标到达策略。现有大多数方法主要通过在时间上连续的片段之间进行轨迹拼接来实现这一点，但这限制了在不同上下文之间组合行为的能力。为克服这一局限，本文将 analogy transduction（类比转导）形式化为：将任务内生的类比与给定上下文进行组合，从而合成新的计划，并提出一种专门适用于这一过程的新型类比表示。在理论分析的基础上，这种类比表示能够捕捉在最优任务执行过程中真正发生变化的部分，对上下文变化保持不变，并且足以支持最优目标到达。我们进一步指出，在类比转导中，将泛化能力扩展到未见过的类比—上下文配对是一项实际障碍，因此提出一种用于离线 GCRL 的新方法，使类比转导能够超越已见配对，推广到未见组合。实验结果表明，该方法在 OGBench 操控环境上表现有效，显著优于那些不执行类比转导的先前方法。

</details>

---

### [[20_Research/Papers/强化学习/ReversedQ_Opportunities_for_Faster_Q-Learning_in_Episodic_Online_Reinforcement_Learning|ReversedQ: Opportunities for Faster Q-Learning in Episodic Online Reinforcement Learning]]

![[assets/2605.20592_figure.png|800]]

- **arXiv**: [2605.20592](https://arxiv.org/abs/2605.20592)
- **PDF**: https://arxiv.org/pdf/2605.20592
- **详细分析**: [[20_Research/Papers/强化学习/ReversedQ_Opportunities_for_Faster_Q-Learning_in_Episodic_Online_Reinforcement_Learning|ReversedQ: Opportunities for Faster Q-Learning in Episodic Online Reinforcement Learning]]
- **作者**: Sofia R. Miskala-Dinc, Aviva Prins
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

这篇论文关注有限时域、按回合进行交互的在线强化学习问题，具体是在跨回合动力学保持稳定的 episodic MDP 中做模型无关的 Q-learning。此类方法在库存控制、机器人和规划决策等场景中很常见，但探索与利用的平衡一直是瓶颈：传统 UCB 类方法虽然有理论保证，却往往过于保守。作者指出，近期基于后验采样的模型无关方法在理论上取得进展，但为了证明收敛或遗憾界，通常依赖“延迟学习”机制，这会拖慢新信息的传播。因而，如何在保持理论框架启发的同时让信息更快进入价值更新，是这篇工作值得关注的核心问题。

#### 方法概述和架构

论文以 Wang et al. 的 RandomizedQ 为基线，提出 ReversedQ，核心是围绕“更快利用新观测”做三处修改。第一是把每个 episode 内的价值传播改为反向回传，即按时间步从后往前更新 Q 和 V，而不是按常规前向更新，以便当前轨迹中的最新回报能更快影响前面状态。第二是调整价值更新与重启的频率/时机，让某些探索性和利用性估计更及时地同步，减少旧估计在多步传播中的滞后。第三是在初始化阶段引入更有信息量的 value initialization，用更贴近回合长度的初值启动 Q/V 表。整体流程上，ReversedQ 在每个 episode 收集轨迹后，先沿轨迹反向更新两套 Q 估计与 V 表，再通过混合规则将探索估计与利用估计合并为实际执行的 Q 值，输出用于下一步动作选择的策略。

#### 实验结果分析

作者在 BDCL（Bidirectional Diabolical Combination Lock）和 chain MDP 两个环境上做了实验，并与 RandomizedQ 比较。结果显示，ReversedQ 将 scaled mean cumulative reward 在 BDCL 上从 9.53% 提升到 78.78%，在 chain MDP 上从 21.76% 提升到 61.81%。论文还报告了对三个改动因素的单独与累积影响分析，说明这些“更快学习”的设计不仅各自有效，而且组合后增益更明显。

<details>
<summary>完整摘要</summary>

我们研究有限时域、按回合进行的 Markov Decision Processes（MDPs）中的无模型 Q-learning，并假设跨回合的动力学是稳定的。我们指出，近期无模型后验采样方向的一类工作存在一个核心问题：为了证明理论保证，它们依赖于延迟学习。具体而言，我们识别出三种加速学习的机会：（i）价值函数更新顺序，（ii）更新频率，以及（iii）价值函数初始化。我们以 Wang et al. 的 RandomizedQ 为基础，展示这些改变以及它们各自和累积的影响，并在多组实证研究中进行分析。我们发现，将这些修改组合后得到的 ReversedQ，与 RandomizedQ 相比，在 Bidirectional Diabolical Combination Lock（BDCL）上的 scaled mean cumulative reward 从 9.53% 提升到 78.78%，在 chain MDP 上从 21.76% 提升到 61.81%。

</details>

---
