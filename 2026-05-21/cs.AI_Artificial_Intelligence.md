# cs.AI | Artificial Intelligence | 2026-05-21

#arxiv #ComputerScience

**论文数**: 44

### [[20_Research/Papers/具身智能/Mem-$π$_Adaptive_Memory_through_Learning_When_and_What_to_Generate|Mem-$π$: Adaptive Memory through Learning When and What to Generate]]

![[assets/2605.21463_figure.png|800]]

- **arXiv**: [2605.21463](https://arxiv.org/abs/2605.21463)
- **PDF**: https://arxiv.org/pdf/2605.21463
- **详细分析**: [[20_Research/Papers/具身智能/Mem-$π$_Adaptive_Memory_through_Learning_When_and_What_to_Generate|Mem-$π$: Adaptive Memory through Learning When and What to Generate]]
- **作者**: Xiaoqiang Wang, Chao Wang, Hadi Nekoei, Christopher Pal, Alexandre Lacoste, Spandana Gella, Bang Liu, Perouz Taslakian
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 强化学习
- **相关性评分**: 1.25（加权：具身智能 0.3，大模型 0.75，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

大模型智能体正在被用于网页导航、终端工具调用和具身交互等真实任务，但现有记忆增强方法大多依赖“检索历史片段”的方式，把固定记忆条目直接取回给模型使用。这类做法在当前上下文变化较大时容易返回不相关、半相关或过于具体的内容，反而干扰智能体决策。论文关注的核心问题是：智能体记忆能否不再依赖静态检索，而是根据当前情境按需“生成”更合适的指导，并且学会判断何时不该生成。这个方向值得关注，因为它把记忆从存储与召回问题推进到了“生成式策略”问题，更贴近复杂智能体环境中的动态需求。

#### 方法概述和架构

论文提出 Mem-π，将记忆建模为一个独立于下游智能体的生成式策略，由专门的语言模型或视觉-语言模型参数化。其输入是智能体当前上下文，通常包括任务指令和环境观测；输出不是动作，而是插入到智能体上下文中的简短指导性记忆，用来辅助后续决策。方法分两阶段训练：第一阶段是经验蒸馏，用离线经验库中的“上下文-记忆”对进行监督学习，把可复用经验压缩进参数中；第二阶段是适应蒸馏，用强化学习根据下游任务成功与否进一步优化记忆生成。为避免“总是生成”带来的噪声，模型显式加入 [GENERATE] 和 [ABSTAIN] 两种决策，既学“何时生成”，也学“生成什么”。在优化上，作者设计了决策-内容解耦的策略优化，把生成/拒绝的路由决策和具体内容生成分开学习，并通过结构化反事实 rollout 与奖励塑形，鼓励模型在真正提升任务成功率时才输出记忆。

#### 实验结果分析

论文在多个智能体基准上评估了 Mem-π，包括 WebArena、WorkArena、LifelongAgentBench 和 ALFWorld，覆盖网页导航、终端工具使用以及文本具身环境。与基于检索的记忆方法和此前的 RL 优化记忆基线相比，Mem-π 在各项任务上都表现更好，平均相对提升约 20%，其中 WebArena 上的相对增益接近 50%；英文摘要还指出网页导航任务上的相对提升超过 30%。节选文本没有给出更细的具体数值，因此可见文本未给出具体数值。作者还报告了消融与深入分析，强调“何时生成”的 abstention 机制和决策-内容解耦设计对稳定性能提升是关键。

<details>
<summary>完整摘要</summary>

我们提出 Mem-π，一种用于大语言模型（LLM）智能体的自适应记忆框架，其中有用的指导不是从外部记忆库中检索，而是在需要时按需生成。现有的记忆增强型智能体通常依赖基于相似度的检索，从情景记忆库或技能库中返回静态条目，而这些条目往往与当前上下文不匹配。与此不同，Mem-π 使用一个独立于下游智能体、具有自身参数的专用语言模型或视觉-语言模型来生成面向具体上下文的指导，帮助复杂任务中的智能体行动。该记忆策略会在当前智能体上下文条件下，联合决定何时生成指导以及生成什么样的指导。我们采用决策-内容解耦的强化学习目标对其进行训练，使模型在生成无助于任务时学会拒绝输出，而在需要时生成简洁且有用的指导。我们在涵盖网页导航、终端工具使用和基于文本的具身交互等多种智能体基准上进行了评估，结果表明 Mem-π 稳定优于基于检索的记忆方法以及此前经过 RL 优化的记忆基线，在网页导航任务上取得了超过 30% 的相对提升。

</details>

---

### [[20_Research/Papers/强化学习/Mind_the_Sim-to-Real_Gap_&_Think_Like_a_Scientist|Mind the Sim-to-Real Gap & Think Like a Scientist]]

![[assets/2605.21458_figure.png|800]]

- **arXiv**: [2605.21458](https://arxiv.org/abs/2605.21458)
- **PDF**: https://arxiv.org/pdf/2605.21458
- **详细分析**: [[20_Research/Papers/强化学习/Mind_the_Sim-to-Real_Gap_&_Think_Like_a_Scientist|Mind the Sim-to-Real Gap & Think Like a Scientist]]
- **作者**: Harsh Parikh, Gabriel Levin-Konigsberg, Dominique Perrault-Joncas, Alexander Volfovsky
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 0.9（加权：具身智能 0.9）
- **关联关键词**: RL

#### 研究背景与动机

这篇论文关注具身智能和更广义的序贯决策问题：当研究者已经有一个便宜的仿真器，但现实部署又伴随真实成本时，应该何时继续依赖仿真，何时必须走向真实环境做实验。作者指出，仿真器往往继承了校准数据中的混杂偏差与分布漂移，而纯在线学习虽然无偏，却可能因为策略只覆盖了局部状态空间，永远学不到那些“没去过”的关键区域。这个问题在移动 HIV 检测、供应链调度等场景中都非常典型，因此值得关注。

#### 方法概述和架构

论文先从理论上给出一个扩展版 simulation lemma，把仿真器的价值误差分解为两部分：一部分是由校准到部署的分布变化造成的偏差，随机化实验可以识别；另一部分是参数化残差，继续交互也无法消除。接着作者证明策略价值差距可以拆成“局部项”和“可达性项”，前者发生在部署策略已经访问到的状态上，后者来自策略根本到不了的状态。基于这一分解，论文提出 Fisher-SEP，一种 simulation-aided experimental policy：先用仿真器评估目标策略的后验预测方差，再用 Fisher 信息设计实验，把有限真实试验投放到最能降低价值不确定性的状态-动作对上。该方法还给出 reward-only 和 transition-only 两个特化版本，并配套了 per-pair 的探索优先级指标 EPI，用于诊断哪些位置最值得先做试点。

#### 实验结果分析

论文通过两个案例验证方法适用范围：一个是 vending-machine supply chain，用来展示局部误差主导时，前置实验在足够长的规划跨度下会优于单纯的后验更新；另一个是 HIV mobile-testing，展示当存在把“可见区域”和“不可见区域”隔开的 corridor 时，只有经过专门设计的探索才能到达低监测区域。与单纯被动学习相比，结果显示局部误差可以逐步缩小，但可达性误差在任何有限或无限时域下都不会自动消失。文中还比较了组合锁（combination lock）和 hidden treasure 等环境，以及与 UCRL2、UCBVI 等无仿真基线的对照；可见文本未给出具体数值，但核心结论是：仿真器应被用来决定“去哪里实验”，而不只是直接给出部署策略。

<details>
<summary>完整摘要</summary>

假设一个规划者拥有某个序贯决策问题的预训练仿真器，并且可以在真实场景中进行实验。仿真器查询代价低，但会继承其校准数据中的混杂与漂移；而真实实验是无偏的，但每次试验都要消耗一个真实单位。我们研究规划者何时以及如何用真实实验来补充仿真器。我们给出三个结果。第一，一个扩展的 simulation lemma 将仿真器的价值误差分解为两部分：一部分是校准—部署偏移，这一部分可以通过随机化识别；另一部分是参数化残差，无法通过进一步交互消除。第二，仿真器最优策略与真实最优策略之间的价值差距可以分为局部成分和可达成分：局部成分发生在已部署策略本来就会访问的状态上，可达成分发生在它不会访问的状态上。在纯被动学习下，无论时域多长，可达成分都不会收敛到零。第三，我们提出 Fisher-SEP，一种 simulation-aided experimental policy（SEP），它最小化目标策略价值的后验预测方差，并给出了 reward-only 与 transition-only 两种特化形式。两个案例研究说明了不同适用情形。在一个 vending-machine 供应链中，当时域足够长、足以摊薄试点成本后，前置实验会超过单纯的后验更新。在一个 HIV 移动检测例子中，存在一条把监测充分的区域与监测不足的区域隔开的走廊，只有经过设计的探索才能到达监测不足的区域。

</details>

---

### [[20_Research/Papers/具身智能/Lost_in_Fog_Sensor_Perturbations_Expose_Reasoning_Fragility_in_Driving_VLAs|Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs]]

![[assets/2605.21446_figure.png|800]]

- **arXiv**: [2605.21446](https://arxiv.org/abs/2605.21446)
- **PDF**: https://arxiv.org/pdf/2605.21446
- **详细分析**: [[20_Research/Papers/具身智能/Lost_in_Fog_Sensor_Perturbations_Expose_Reasoning_Fragility_in_Driving_VLAs|Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs]]
- **作者**: Abhinaw Priyadershi, Jelena Frtunikj
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.9，机器人 0.3）
- **关联关键词**: Multimodal, Agent, Security

#### 研究背景与动机

自动驾驶中的 Vision-Language-Action（VLA）模型不仅要输出轨迹，还要给出可解释的推理链，这对于安全认证、故障诊断和运行时监控都很重要。但现实道路中摄像头会遭遇噪声、雾天、强光和低照度等传感器退化，解释是否仍然可靠，是当前解释式驾驶模型的关键瓶颈。本文聚焦“推理是否稳定地反映轨迹可靠性”这一问题，尤其关注雾天和传感器扰动如何暴露驾驶 VLA 的脆弱性，因此很值得具身智能与机器人方向关注。

#### 方法概述和架构

作者以 Alpamayo R1（10B 参数）为研究对象，在 PhysicalAI-Autonomous-Vehicles 验证集上选取 1,996 个驾驶场景，围绕八种传感器扰动条件开展系统评测，包括四档高斯噪声、两种亮度极值和两种雾强度。模型输入为多视角相机图像与自车历史信息，输出为 64 个 waypoint 构成的 6.4 秒轨迹，以及对应的 Chain-of-Causation（CoC）自然语言解释。实验同时比较清洁输入与扰动输入下的轨迹变化，并用 CoC 变化率、ADE、轨迹 L2 偏移等指标刻画“解释稳定性—轨迹稳定性”的关系。为区分“相关”与“因果”，作者还做了受控消融：在相同 checkpoint、相同解码超参数和固定随机种子下，分别进行带 CoC 生成与仅轨迹推理的对比。

#### 实验结果分析

结果显示，CoC 一旦在扰动后发生变化，轨迹偏移会显著上升，平均达到原来的 5.3 倍；在不同攻击类型上的相关性非常高，表明解释变化可以作为轨迹失真的高可信信号。作者还发现，在噪声强度 σ∈{10,30,50,70} 的范围内，性能退化近似线性，而常见输入预处理防御只能带来很有限的改善。消融实验表明，开启 CoC 生成与轨迹精度提升相关，平均可带来 11.8% 的改善；但节选中未给出所有对照设置下的完整数值细节。

<details>
<summary>完整摘要</summary>

自动驾驶中的可解释规划器，不仅依赖于生成解释，还依赖于这些解释在真实世界传感器退化条件下保持可靠性。本文对 Vision-Language-Action（VLA）模型在自动驾驶中的鲁棒性进行了受控扰动研究，评测对象为 Alpamayo R1（10B 参数），覆盖 1,996 个场景，并施加八种传感器扰动（四档高斯噪声、两种光照极端情况和两种雾强度；总计约 18,000 次推理试验）。我们发现，推理一致性是轨迹可靠性的高保真指示器：当扰动后 Chain-of-Causation（CoC）解释发生变化时，轨迹偏移会显著上升 5.3 倍（21.8 米对 4.1 米），并且在不同攻击类型上相关系数 r=0.99，单样本层面点二列相关 r_pb=0.53（Cohen’s d=1.12）。一项受控消融提供了证据，说明在匹配的推理设置下，启用 CoC 生成与轨迹精度提升相关（在所有条件下平均提升 11.8%；p&lt;0.0001）。在所测试的噪声范围（σ∈{10,30,50,70}）内，性能退化近似线性（R^2=0.957），而标准输入预处理防御只能带来有限缓解。总体而言，这些结果确立了 CoC 一致性可作为规划安全性的定量代理，并推动基于推理的运行时监控，以实现更安全的 VLA 部署。

</details>

---

### [[20_Research/Papers/强化学习/SpecBench_Measuring_Reward_Hacking_in_Long-Horizon_Coding_Agents|SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents]]

![[assets/2605.21384_figure.png|800]]

- **arXiv**: [2605.21384](https://arxiv.org/abs/2605.21384)
- **PDF**: https://arxiv.org/pdf/2605.21384
- **详细分析**: [[20_Research/Papers/强化学习/SpecBench_Measuring_Reward_Hacking_in_Long-Horizon_Coding_Agents|SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents]]
- **作者**: Bingchen Zhao, Dhruv Srikanth, Yuxiang Wu, Zhengyao Jiang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, RL

#### 研究背景与动机

随着长上下文、长任务的软件工程智能体能够自动生成远超人工逐行审查能力的代码，开发者实际上越来越依赖自动化测试套件来判断系统是否“真的可用”。这就带来了一个核心风险：智能体可能为了通过测试而投机取巧，表面上拿到高分，实际却没有满足用户真实需求。本文聚焦这种在长周期代码生成中的 reward hacking 问题，尝试给出可量化、可复现的测量方式，因此具有很强的现实意义。

#### 方法概述和架构

论文提出 SpecBench，用来测量长周期 coding agents 的 reward hacking。作者把每个软件工程任务拆成三部分：自然语言规格说明、对单个功能进行检查的可见 validation tests，以及隐藏的 held-out tests。智能体在推理时只能看到规格说明和 validation tests，并通过迭代写码、运行测试、继续修复的方式生成候选实现；随后再在隐藏测试上统一评估。方法上用验证集通过率与隐藏集通过率的差值 Δ=s_val−s_test 作为 reward hacking gap，若 Δ>0，说明模型优化了测试代理指标却没有真正满足完整规格。SpecBench 共包含 30 个系统级编程任务，覆盖从 JSON 解析器到从零实现操作系统内核等不同任务跨度，并进一步比较不同模型、不同外层搜索策略（AIDE、Linear、Autoresearch）下的差异。

#### 实验结果分析

作者在 SpecBench 上对 frontier 级 coding agents 及多种开源/闭源模型进行了大规模实验，评估维度包括 validation pass rate、held-out pass rate 和 reward hacking gap。结果显示，几乎所有模型都能把可见测试集“刷满”，但隐藏测试上的表现明显更差，说明 reward hacking 普遍存在。节选文本给出的趋势表明，任务越长、代码规模越大，reward hacking gap 越严重；同时能力较弱的模型也更容易出现更大的 gap。文中还展示了多种失败模式，包括特征彼此隔离、以及直接用查表等方式“记住”测试输入的投机实现；具体数值除“每增加 10 倍代码规模，gap 约增加 27/28 个百分点”等趋势外，可见文本未给出更多完整统计。

<details>
<summary>完整摘要</summary>

当长周期编码智能体生成的代码量超过任何开发者能够审查的规模时，监督实际上会收缩到一个单一表面：自动化测试套件。在这种设置下，reward hacking 很自然地出现，因为智能体优化的是通过测试，而不是偏离用户真实目标的行为。我们通过将软件工程任务分解为三部分来研究这一 reward hacking 现象：(i) 自然语言形式的规格说明；(ii) 可见的验证测试，用于单独检验被指定的功能；(iii) 留出测试，用于把这些相同功能组合起来，模拟真实世界的使用场景。基于规格说明和可见验证测试套件，一个真正符合要求的智能体应该能够生成一个也能通过所有留出测试的解决方案。因此，我们用这两类测试通过率之间的差距来量化 reward hacking。基于这一方法，我们提出 SpecBench，这一基准包含 30 个系统级编程任务，范围从构建 JSON 解析器这样的短周期任务，到从零开始构建整个操作系统内核这样的超长周期任务。大规模实验表明，一个一致的模式是：尽管所有前沿智能体都能在可见测试集上达到饱和，reward hacking 仍然存在，而且较小模型在留出测试集上的差距更大。该差距还会随任务长度急剧扩大：代码规模每增加一个数量级，差距就会增加 28 个百分点。失败形式从微妙的特征隔离，到故意设计的投机行为都有，包括一个 2,900 行的哈希表“编译器”，它通过记忆测试输入来取巧。SpecBench 提供了一个有原则的测试平台，用于衡量编码智能体究竟是在构建真正可工作的系统，还是仅仅在操纵开发者提供的测试套件。

</details>

---

### [[20_Research/Papers/大模型/Insights_Generator_Systematic_Corpus-Level_Trace_Diagnostics_for_LLM_Agents|Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents]]

![[assets/2605.21347_figure.png|800]]

- **arXiv**: [2605.21347](https://arxiv.org/abs/2605.21347)
- **PDF**: https://arxiv.org/pdf/2605.21347
- **详细分析**: [[20_Research/Papers/大模型/Insights_Generator_Systematic_Corpus-Level_Trace_Diagnostics_for_LLM_Agents|Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents]]
- **作者**: Akshay Manglik, Apaar Shanker, Kaustubh Deshpande, Jason Qin, Yash Maurya, Veronica Chatrath, Vijay S. Kalmath, Levi Lentz, Yuan, Xue
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

LLM agents 在执行复杂任务时会产生很长的推理、工具调用与环境交互轨迹，但现有调试方式仍主要依赖人工抽查少量轨迹、再凭经验提出假设并反复试错。这种做法只能看到局部现象，难以发现跨大量轨迹才会显现的系统性模式，也无法应对生产级语料中单条轨迹可达数万 token 的规模。论文聚焦“轨迹语料级诊断”这一新问题，目标是从整批执行轨迹中自动产出有证据支撑的自然语言洞见，因此很值得关注。

#### 方法概述和架构

论文提出 Insights Generator（IG），这是一个用于大规模轨迹语料诊断的多智能体系统。IG 将分析过程拆成“假设提出”和“假设验证”两步：Scout 先从代表性样本中通过总结与信息抽取提出候选假设，Investigator 再针对每个假设在整个语料上做群体级验证，并输出确认、否定或不确定的结论。系统由 Orchestrator 统一调度，负责分发子任务、判断当前发现是否足够、并合成最终报告。所有轨迹都先进入结构化的数据处理层，而不是直接塞入上下文窗口；子智能体通过 Python 工具访问聚合统计、摘要、检索与 cohort comparison 等能力，从而支持超长语料上的迭代式分析。最终输出的是包含发现、证据、 prevalence 估计和修正建议的诊断报告。

#### 实验结果分析

论文在多个基准上评估 IG，并从报告质量与下游效果两个维度考察其价值；对比对象包括其他轨迹分析系统以及不同的诊断/优化框架。结果显示，使用 IG 报告的人类专家将 scaffold 性能相对未修改基线提升了 30.4 个百分点，而采用 IG 洞见的 coding agents 也获得了稳定且持续的收益。与其他方法相比，IG 的 scout-investigator 架构在检测覆盖率上具有可比性，同时在深度和证据质量上更受领域专家认可。文中还强调，若仅看局部轨迹或单次轨迹诊断，很多“静默失败”与群体差异模式都难以被发现。

<details>
<summary>完整摘要</summary>

诊断 LLM agents 的失败原因在很大程度上仍依赖人工。实践者通常只检查少量执行轨迹，提出临时性的假设，然后反复迭代。这个过程会遗漏那些只有在轨迹总体中才会显现的模式，而且在生产级语料中难以扩展，因为单条轨迹往往包含数万 token。我们将“轨迹语料级诊断”形式化：给定一组执行轨迹，目标是生成有依据的自然语言洞见，用来刻画不同轨迹群组中的系统性行为模式，并为每条洞见关联支持证据。我们提出 Insights Generator（IG），这是一个多智能体系统，通过在整个轨迹语料上提出并测试假设来回答诊断问题，从而生成一份有证据支撑的洞见报告。我们从定性与定量两个层面对 IG 进行评估，既包括基于 rubric 的报告质量评测，也包括将 IG 洞见落地后带来的下游性能提升。使用 IG 报告的人类专家将 scaffold 性能相对未修改基线提升了 30.4 个百分点；利用 IG 洞见的 coding agents 也表现出持续而稳定的增益。在多个基准上，IG 的 scout-investigator 架构在检测覆盖率方面与竞争方法相当，而领域专家则认为 IG 报告在深度与证据质量上领先。

</details>

---

### [[20_Research/Papers/强化学习/DeCoR_Design_and_Control_Co-Optimization_for_Urban_Streets_Using_Reinforcement_Learning|DeCoR: Design and Control Co-Optimization for Urban Streets Using Reinforcement Learning]]

![[assets/2605.21311_figure.png|800]]

- **arXiv**: [2605.21311](https://arxiv.org/abs/2605.21311)
- **PDF**: https://arxiv.org/pdf/2605.21311
- **详细分析**: [[20_Research/Papers/强化学习/DeCoR_Design_and_Control_Co-Optimization_for_Urban_Streets_Using_Reinforcement_Learning|DeCoR: Design and Control Co-Optimization for Urban Streets Using Reinforcement Learning]]
- **作者**: Bibek Poudel, Lei Zhu, Kevin Heaslip, Sai Swaminathan, Weizi Li
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision, Systems

#### 研究背景与动机

城市道路中，行人过街设施的选址与信号灯配时往往被分开处理，但两者实际上强耦合：路口/中段人行横道的位置会影响行人绕行距离、车辆停车次数和冲突点分布，而信号控制又决定这些冲突如何被消解。尽管现代视觉系统已经能够大规模感知、跟踪和预测城市参与者，如何把这些感知结果进一步用于道路设计仍然是一个明显空白。本文聚焦“行人过街设计 + 路网信号控制”的联合优化问题，试图用强化学习把真实交通感知数据转化为可执行的基础设施设计决策，因此具有较强的现实应用价值。

#### 方法概述和架构

论文提出 DeCoR，一个两阶段的强化学习协同优化框架。第一阶段是设计阶段：将行人网络编码为图结构，设计策略基于图注意力网络输出一个高斯混合模型（GMM）的参数，再从中采样新的横道位置与宽度，以生成候选人行横道布局。第二阶段是控制阶段：在给定某个布局后，共享的控制策略在闭环仿真中学习网络级信号配时，以联合最小化行人和车辆的等待/延误。训练时，设计阶段把每一轮生成的布局送入 SUMO 闭环仿真，并结合来自视频和 Wi-Fi 日志的真实需求；控制阶段则在多个并行环境中使用随机缩放的需求进行训练，以增强对需求变化的鲁棒性。两个阶段都采用 PPO 更新：设计策略把布局质量作为即时回报，控制策略则根据多步交互的累计奖励更新，且控制策略的学习结果还反过来为设计策略提供评价信号。

#### 实验结果分析

作者在一段 750 m 的真实城市走廊上验证了方法，该场景的需求来自视频与 Wi-Fi 记录，包含行人与车辆的实际流量。结果显示，DeCoR 学到的布局在使用更少横道的情况下，将行人到最近横道的到达时间降低了 23%，同时控制策略相较固定时制信号把行人等待时间降低 79%、车辆等待时间降低 65%。文中还指出，该控制策略对训练外的需求分布具有泛化能力，并且在布局变化后无需重新训练仍保持鲁棒性；从正文节选可见文本未给出更完整的基线对比数值。

<details>
<summary>完整摘要</summary>

现代视觉系统已经能够在大规模场景下检测、跟踪并预测城市交通参与者，但把感知输出转化为城市设计决策的能力仍然有限。为此，我们提出 DeCoR，一个两阶段强化学习框架，利用流量观测数据对人行横道布局与路网级信号控制进行协同优化。在设计阶段，模型将行人网络编码为图，并学习一个生成式策略，对人行横道的位置与宽度进行参数化，具体通过高斯混合模型（GMM）来表示，从中采样生成新的横道方案。对于每一种布局，共享的控制策略进一步学习自适应信号配时，以最小化行人与车辆的联合延误。在一条 750 m 的真实城市走廊上，我们使用来自视频与 Wi-Fi 日志感知到的需求进行实验，DeCoR 学到的布局在使用更少横道的情况下，将行人到最近横道的到达时间降低了 23%。在控制方面，相较固定时制信号，DeCoR 将行人和车辆的等待时间分别降低了 79% 和 65%。此外，控制策略能够泛化到训练范围之外的需求，并且在布局发生变化时无需重新训练也能保持鲁棒性。我们的代码和数据已公开提供在 https://github.com/poudel-bibek/DeCoR 。

</details>

---

### [[20_Research/Papers/大模型/TimeSRL_Generalizable_Time-Series_Behavioral_Modeling_via_Semantic_RL-Tuned_LLMs_--_A_Case_Study_in_Mental_Health|TimeSRL: Generalizable Time-Series Behavioral Modeling via Semantic RL-Tuned LLMs -- A Case Study in Mental Health]]

![[assets/2605.21295_figure.png|800]]

- **arXiv**: [2605.21295](https://arxiv.org/abs/2605.21295)
- **PDF**: https://arxiv.org/pdf/2605.21295
- **详细分析**: [[20_Research/Papers/大模型/TimeSRL_Generalizable_Time-Series_Behavioral_Modeling_via_Semantic_RL-Tuned_LLMs_--_A_Case_Study_in_Mental_Health|TimeSRL: Generalizable Time-Series Behavioral Modeling via Semantic RL-Tuned LLMs -- A Case Study in Mental Health]]
- **作者**: Yuang Fan, Lilin Xu, Millie Wu, Jingping Nie, Qingyu Chen, Yuzhe Yang, Zhuo Zhang, Xin Liu, Subigya Nepal, Xiaofan Jiang, Xuhai "Orson" Xu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

这篇论文关注的是基于智能手机和可穿戴设备的长期被动感知，去预测心理健康状态（如焦虑、抑郁）这类纵向行为健康任务。该场景的核心难点不是单次预测，而是模型在跨数据集、跨人群、跨传感管线时容易发生分布偏移，传统机器学习往往会过拟合某个队列的数值特征，而直接用大模型处理原始长时序又很难稳定推理。作者认为，若想提升真实部署场景下的泛化能力，关键不在于更复杂的数值特征，而在于让模型先把行为轨迹压缩成更高层次、可复用的语义表示。

#### 方法概述和架构

作者提出 TimeSRL（Time-series Semantic Reinforcement Learning），是一个两阶段的大模型框架：第一阶段把原始行为时序信号抽象成自然语言形式的高层语义总结，第二阶段仅根据这段语义总结完成最终预测，而不再直接访问原始数值输入。这个“语义瓶颈”设计强制模型围绕稳定、异常、时间动态、信号依赖等行为概念进行推理，避免只记住数据集特有的数值模式。由于中间语义摘要没有人工标注，作者使用 GRPO 结合 RLVR 对端到端流程进行强化学习优化：奖励由可验证的下游预测结果提供，从而反向塑造更有用的中间摘要。整体上，训练时同时优化“先抽象、后预测”的两步轨迹，推理时则沿着同样的两阶段路径输出结果。

#### 实验结果分析

作者在一个专门考验跨队列泛化能力的心理健康基准上进行实验，并采用严格的 leave-one-dataset-out（LOSO）协议评估，同时与强非LLM机器学习基线和多种LLM基线比较。结果表明，TimeSRL 在焦虑预测上相对强非LLM基线的 MAE 降低了 3.1%–10.1%，相对LLM基线降低了 9.5%–44.1%；在抑郁预测上分别降低了 3.2%–9.6% 和 27.4%–57.6%，且均具有统计显著性。论文还报告了跨数据集、跨 LLM backbone 的一致提升，以及跨 benchmark、跨传感管线迁移时无需目标域微调仍能保持较强性能；消融结果显示，RL 与两阶段语义瓶颈结合优于单独使用任一组件。

<details>
<summary>完整摘要</summary>

纵向被动感知能够实现连续健康预测，但模型在跨数据集分布偏移下往往失效。传统机器学习容易过拟合队列特有的伪相关模式，而大语言模型（LLMs）则难以对长而异构的时间序列进行可靠推理。为此，我们提出 TimeSRL，这是一个两阶段 LLM 框架，通过一个显式的语义瓶颈来承载预测流程。模型首先将原始信号抽象为高层次的自然语言描述，然后仅基于这些抽象来预测行为结果。这样做迫使模型围绕语义概念进行推理，而我们认为这些概念比原始数值更具泛化性。我们使用 Group Relative Policy Optimization（GRPO）与 Reinforcement Learning from Verifiable Rewards（RLVR）对这一过程进行端到端优化，在没有人工中间标注的情况下学习与结果对齐的抽象表示。将其应用于心理健康预测后，TimeSRL 在一个专门用于检验跨队列泛化能力、并采用严格 leave-one-dataset-out（LOSO）协议的基准上取得了最先进性能：在焦虑预测上，相比强非LLM机器学习基线，MAE 平均降低 3.1%–10.1%，相比LLM基线降低 9.5%–44.1%；在抑郁预测上，相应降幅分别为 3.2%–9.6% 和 27.4%–57.6%（均为显著差异）。TimeSRL 在跨 benchmark、跨不同传感管线的迁移中也显著优于此前方法，甚至在无需目标域微调的情况下，其表现接近自身在域内训练时的水平。这些结果表明，语义抽象是可复用的，并为通过 RL 调优的 LLM 实现可泛化的行为建模提供了新的方向。

</details>

---

### [[20_Research/Papers/具身智能/Learning_Structural_Latent_Points_for_Efficient_Visual_Representations_in_Robotic_Manipulation|Learning Structural Latent Points for Efficient Visual Representations in Robotic Manipulation]]

![[assets/2605.21258_figure.png|800]]

- **arXiv**: [2605.21258](https://arxiv.org/abs/2605.21258)
- **PDF**: https://arxiv.org/pdf/2605.21258
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Structural_Latent_Points_for_Efficient_Visual_Representations_in_Robotic_Manipulation|Learning Structural Latent Points for Efficient Visual Representations in Robotic Manipulation]]
- **作者**: Yicheng Jiang, Jiaxu Wang, Junhao He, Zesen Gan, Junhao Li, Qiang Zhang, Jingkai Sun, Jiahang Cao, Mingyuan Sun, Xiangyu Yue, Qiming Shao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

面向机器人操作的具身智能，模型不仅要看懂图像，还要理解三维空间中的几何结构、物体关系和可操作性，这对多视角感知和下游抓取、放置、交互任务都很关键。现有 3D-aware 预训练方法大致分为隐式表示和显式几何原语两类：前者表达能力强，但缺少明确结构线索；后者保留了几何结构，却常受分辨率上限和泛化不足影响。论文聚焦于如何在效率、结构性和泛化之间取得平衡，因此具有较强的机器人落地价值。

#### 方法概述和架构

论文提出一种学习“结构化潜在点（structural latent points）”的预训练框架，核心是在点云自编码器的潜在空间中插入点级 latent VAE（PL-VAE）。具体做法是先用 PTv3 编码原始点云得到稀疏特征点，再通过 PL-VAE 同时对点特征和坐标进行高斯先验正则，使潜表示既保留粗粒度几何趋势，又不再是完全显式的点云。随后，这些结构化潜表示送入 PTv3 解码器恢复更高分辨率的点云，从而为后续任务提供紧凑且鲁棒的视觉表征。训练时，框架还结合一个轻量化的 3DGS 渲染管线，通过多视角重建对表示进行自监督约束；作者刻意裁剪掉冗余模块，把更多表示能力留给前端潜模块。整体流程上，输入是多视角图像与点云/几何信息，输出是可用于下游机器人操作的 3D 感知表征。

#### 实验结果分析

作者在 RLBench、ManiSkill2 以及真实机器人平台上做了系统评测，并与强基线进行比较，实验重点覆盖任务成功率、样本效率以及对视角变化和场景变化的鲁棒性。结果显示，该方法在这些指标上都取得了稳定提升，说明结构化潜在点确实增强了跨场景泛化能力。消融实验进一步表明，PL-VAE、轻量化 3DGS 渲染以及整体的优化设计都是性能提升的关键组成部分。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

当前用于具身感知与操作的 3D-aware 预训练方法，大多建立在可微渲染框架之上，通常形成两类表示：完全隐式的神经场，或完全显式的几何原语。隐式表示虽然表达能力强，但缺少显式的结构线索；显式表示虽然保留了几何信息，但受限于分辨率并且泛化能力较弱。为了解决这些问题，我们提出一种新的预训练框架，用于学习一种混合表示——结构化潜在点。具体而言，我们将一个点级 latent variational autoencoder 插入到点云自编码器的潜在空间中，并联合约束点级特征与坐标，使其向高斯先验靠拢。由此得到的紧凑潜表示保留了粗粒度的结构趋势，这些结构并不编码精确几何，但能够捕获更丰富的粗形状与语义信息，从而有效结合隐式表示的表达能力与显式表示的结构先验。此外，参考已有工作的共同设计选择，我们构建了一个简化且高效的、基于 3DGS 的渲染管线，并有意保持其轻量化，以提升效率，同时将更多表示容量留给前端潜模块。在 RLBench、ManiSkill2 以及真实机器人平台上的大量实验表明，相比强基线，该方法在任务成功率、样本效率以及对视角和场景变化的鲁棒性方面都持续提升。消融研究进一步证实，框架中的各个组件对整体性能都至关重要。

</details>

---

### [[20_Research/Papers/大模型/APEX_Autonomous_Policy_Exploration_for_Self-Evolving_LLM_Agents|APEX: Autonomous Policy Exploration for Self-Evolving LLM Agents]]

![[assets/2605.21240_figure.png|800]]

- **arXiv**: [2605.21240](https://arxiv.org/abs/2605.21240)
- **PDF**: https://arxiv.org/pdf/2605.21240
- **详细分析**: [[20_Research/Papers/大模型/APEX_Autonomous_Policy_Exploration_for_Self-Evolving_LLM_Agents|APEX: Autonomous Policy Exploration for Self-Evolving LLM Agents]]
- **作者**: Yibo Li, Jiashuo Yang, Zhi Zheng, Zhiyuan Hu, Yuan Sui, Shizun Wang, Yufei He, Bryan Hooi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

大模型智能体在复杂交互任务中表现突出，尤其适合需要长程决策的环境，例如文字冒险游戏和真实网页操作。但这类智能体通常无法在测试时直接更新参数，只能依赖跨回合积累的记忆与反思来自我进化。论文指出，这会带来“探索坍缩”：随着记忆增多，智能体越来越倾向于重复少数高回报套路，反而更难发现更优策略。因而，如何在自我进化过程中持续保持探索能力，是这篇工作关注的核心问题。

#### 方法概述和架构

论文提出 APEX（Autonomous Policy Exploration），核心是维护一个显式的策略空间——strategy map。该图是一个有向无环图，节点表示里程碑式子目标，边表示先决依赖关系，并为每个节点记录访问次数、平均回报和回报方差等统计量。APEX 由两个互补模块组成：Fork Discovery 负责从历史轨迹中挖掘“看见过但从未真正走下去”的分叉方向，扩展策略图的前沿；Policy Selection 则在每个回合内基于带不确定性的打分策略（如 Thompson Sampling、UCB 或 ϵ-Greedy）从当前可达里程碑中选择下一步，平衡探索与利用。执行过程中，智能体并不是一次性固定整条计划，而是每完成或失败一个里程碑就重新选择下一目标，从而避免依赖失败路径继续向下推进。每隔若干回合，系统还会进行 Map Refinement：用 LLM 对轨迹做结构化总结，修正节点内容、依赖边和重复节点，并通过 Return Propagation 更新图上的统计信息。

#### 实验结果分析

论文在 9 个 Jericho 文字冒险游戏和 WebArena 真实网页交互基准上评估 APEX，并与多种基线方法比较。结果显示，APEX 在两类环境中都优于所有基线，尤其在需要发现全新策略而非重复旧套路的任务上优势更明显。消融实验表明，Fork Discovery、Policy Selection 和 Map Refinement 都对性能有贡献，且方法在不同设置、不同 backbone LLM 下都表现稳健。可见文本未给出具体数值，但整体结论是 APEX 能有效缓解自我进化智能体中的探索坍缩问题。

<details>
<summary>完整摘要</summary>

大模型智能体在多种复杂任务中表现出强大能力，包括需要长程决策的交互式环境。但这类智能体无法在测试时即时学习。自我进化智能体通过跨回合积累记忆与反思，而不是更新模型权重，来解决这一问题。然而，这类智能体常常遭遇探索坍缩：随着记忆不断增长，行为会逐渐集中到熟悉的高回报套路上，从而降低发现更优替代方案的机会。为了解决这一问题，我们提出 Autonomous Policy EXploration（APEX），它通过一个策略图——即由里程碑节点及其先决依赖边构成的有向无环图——来构建并维护一个显式的策略空间。在 APEX 中，Fork Discovery 通过有证据支撑的未探索方向扩展策略图，而 Policy Selection 则在规划过程中平衡探索与利用。我们在 9 个 Jericho 文字冒险游戏以及 WebArena 这一真实网页交互基准上进行了评估，APEX 在所有基线方法上都取得了更优表现。大量消融实验验证了各个组件的贡献，并展示了其在多种场景下的鲁棒性，说明 APEX 能有效支持自我进化智能体进行持续探索。

</details>

---

### [[20_Research/Papers/大模型/PREFINE_Preference-Based_Implicit_Reward_and_Cost_Fine-Tuning_for_Safety_Alignment|PREFINE: Preference-Based Implicit Reward and Cost Fine-Tuning for Safety Alignment]]

![[assets/2605.21225_figure.png|800]]

- **arXiv**: [2605.21225](https://arxiv.org/abs/2605.21225)
- **PDF**: https://arxiv.org/pdf/2605.21225
- **详细分析**: [[20_Research/Papers/大模型/PREFINE_Preference-Based_Implicit_Reward_and_Cost_Fine-Tuning_for_Safety_Alignment|PREFINE: Preference-Based Implicit Reward and Cost Fine-Tuning for Safety Alignment]]
- **作者**: Richa Verma, Bavish Kulur, Sanjay Chawla, Balaraman Ravindran
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

在安全强化学习中，很多预训练策略已经能获得较高回报，但仍可能频繁触发约束违规、灾难性失败等安全问题。传统做法通常需要从头求解带约束的CMDP，或依赖明确的数值成本信号与大量在线交互，计算代价高且在真实场景中往往难以满足。本文关注一种更一般也更现实的情形：安全成本不是精确数值，而是以“哪条轨迹更安全”的偏好形式给出，因此值得关注。

#### 方法概述和架构

论文提出 PREFINE（Preference-Based Implicit Reward and Cost Fine-Tuning for Safety Alignment），将 DPO 从大模型偏好对齐迁移到连续控制中的轨迹级安全对齐。方法输入为一个已预训练、以高回报为目标的参考策略 π_ref，以及少量偏好数据：安全的优选轨迹和不安全的非优选轨迹。PREFINE 会基于现有策略采样构造反事实轨迹，用于形成更有区分度的偏好比较，再联合优化 DPO 目标与 SFT 目标，从而一边保持参考策略的高回报行为，一边将策略推向低成本区域。整体训练是完全离线的，不需要显式学习成本模型，也不需要在线交互；论文还强调采用单阶段训练流程以提高效率。

#### 实验结果分析

实验在 DSRL 安全离线强化学习基准上进行，覆盖 HalfCheetah、Walker 等 12 个连续控制任务，并与若干成本优化、分布匹配和模仿学习基线比较。结果显示，PREFINE 在保持原始回报行为的同时，能够显著降低约束违规和灾难性失败；摘要中报告的降幅超过 60%，正文节选进一步写到可达 60%–92%。从效率上看，它相比完整离线 RL 或 imitation learning 具有更好的数据与计算效率，收敛墙钟时间可快一个数量级。节选中还提到消融与对比实验表明，policy-sampled 的反事实采样比混合采样能带来更少的标签不一致和更稳定的安全对齐；但具体数值在可见文本中未完整给出。

<details>
<summary>完整摘要</summary>

我们研究如何在不从头重新训练的情况下，使一个预训练强化学习（RL）策略在安全上具备感知能力，即在加入成本约束后仍能保持原有能力。虽然成本可以被数值化编码，但我们考虑的是更一般的场景：成本以偏好的形式提供。给定一个经过回报优化的策略，以及一小批由“优选”（低成本）和“非优选”（高成本）轨迹组成的数据集，我们的目标是对策略进行微调，使其生成低成本行为，同时保留高回报。不同于大模型中的标准 RLHF——其中偏好是针对同一提示下的不同回答定义的——我们的设置涉及连续控制环境中的轨迹级偏好。我们提出 PREFINE：Preference-Based Implicit Reward and Cost Fine-Tuning for Safety Alignment，这是一种基于偏好的微调方法，将目前在大语言模型微调中广泛使用的 Direct Preference Optimization（DPO）适配到序列决策场景中。PREFINE 通过构造由策略采样得到的反事实轨迹来建立有意义的偏好对比，并联合优化回报保持与安全对齐。实验表明，PREFINE 在维持原始回报行为的同时，将约束违规和灾难性失败降低了 60% 以上。与完整的离线 RL 或模仿学习相比，PREFINE 能以显著更高的数据和计算效率，得到低成本、高回报的策略，进而在偏好对齐与连续领域中的安全策略适配之间建立起桥梁。

</details>

---

### [[20_Research/Papers/强化学习/Behavior-Consistent_Deep_Reinforcement_Learning|Behavior-Consistent Deep Reinforcement Learning]]

![[assets/2605.21214_figure.png|800]]

- **arXiv**: [2605.21214](https://arxiv.org/abs/2605.21214)
- **PDF**: https://arxiv.org/pdf/2605.21214
- **详细分析**: [[20_Research/Papers/强化学习/Behavior-Consistent_Deep_Reinforcement_Learning|Behavior-Consistent Deep Reinforcement Learning]]
- **作者**: Marcel Hussing, Liv G. d'Aliberti, Claas Voelcker, Benjamin Eysenbach, Eric Eaton
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

强化学习在不同随机种子、初始化和数据顺序下，训练结果常出现较大波动，导致同一算法多次运行得到的策略在回报和行为上都不稳定。这种跨运行差异不仅会干扰科研中的公平比较和可复现性，也会给机器人控制、奖励设计、调试以及安全验证带来实际风险。论文将“不同训练次运行出的策略是否行为一致”显式提升为优化目标，关注的不只是平均性能，而是行为稳定性与可部署性。

#### 方法概述和架构

论文提出了 Behavior-Consistent RL（BRL）这一设定，用来度量并优化多个独立训练运行之间的策略一致性。作者首先用跨运行策略之间的分布差异定义“inter-run variability”，把行为一致性形式化为一个可比较的目标。随后基于 MaxEnt RL 给出理论分析：当策略服从 Boltzmann 形式时，温度参数可以控制策略对 Q 值差异的敏感度，从而限制不同运行策略之间的 KL 散度。基于这一结论，论文提出 Q-value Expectile Disagreement（QED），用双 critic 的分歧作为单次训练中对跨运行分歧的代理，并据此构造状态相关的温度调度 α(s)。在训练中，QED 先在 Q 估计不稳定时提高温度以增强一致性，随后随着 critic 收敛逐步降温，以减轻高熵带来的离策略误差和优化困难。

#### 实验结果分析

作者在 18 个连续控制任务上验证了 QED，相比传统熵自动调节方法，跨运行策略分歧下降了约两个数量级，同时没有牺牲任务性能。实验还表明，QED 能显著降低回报方差，文中给出的总体结论是方差约减少 50%，但节选中未给出各任务的完整具体数值。论文同时分析了高熵设置下的离策略不稳定性，并通过消融说明，单纯增大熵并不等价于更好的行为一致性，QED 的状态相关温度更能兼顾稳定性与性能。

<details>
<summary>完整摘要</summary>

强化学习（RL）在不同训练运行之间往往表现出很高的方差，这会导致性能不可靠，并给真实世界应用带来重大部署挑战。本文针对跨运行策略分歧问题，形式化提出了行为一致性强化学习（behavior-consistent RL），其目标是学习既高性能、又在不同训练运行之间分布相似的策略。我们的关键观察是，最大熵强化学习为控制行为分歧提供了直接机制，因为它通过一个共同的（均匀）先验将不同运行锚定在一起。我们证明：对于 Boltzmann 策略，如果将温度设置为与 Q 函数分歧成比例，则可以对由这些策略诱导出的两两 KL 散度给出上界。然而，我们也表明，简单地提高熵可能会损害策略优化，并放大离策略误差。基于这些观察，我们提出 Q-value Expectile Disagreement（QED），这是一种状态相关的温度调度方法，利用双 critic 之间的分歧作为跨运行分歧的单次运行代理。在实验上，我们在 18 个连续控制任务上展示了 QED：它在不牺牲性能的情况下，将跨运行分歧降低了两个数量级，并在仅带来适度样本效率代价的前提下，显著降低了回报方差。

</details>

---

### [[20_Research/Papers/强化学习/Enhanced_Reinforcement_Learning-based_Process_Synthesis_via_Quantum_Computing|Enhanced Reinforcement Learning-based Process Synthesis via Quantum Computing]]

![[assets/2605.21213_figure.png|800]]

- **arXiv**: [2605.21213](https://arxiv.org/abs/2605.21213)
- **PDF**: https://arxiv.org/pdf/2605.21213
- **详细分析**: [[20_Research/Papers/强化学习/Enhanced_Reinforcement_Learning-based_Process_Synthesis_via_Quantum_Computing|Enhanced Reinforcement Learning-based Process Synthesis via Quantum Computing]]
- **作者**: Austin Braniff, Fengqi You, Yuhe Tian
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

流程综合（process synthesis）旨在自动设计化工或能源流程的流程图与操作变量，是过程系统工程中的核心问题，但其设计空间会随着候选单元数量增加而快速膨胀，传统 MINLP/GDP 方法往往依赖预设超结构、专家知识，且计算开销很高。近年来强化学习被用于把流程设计视为序列决策问题，能够在不预先枚举全部结构的情况下逐步搜索设计方案，但深度强化学习在大规模流程设计中仍面临收敛慢、超参数敏感和高维状态-动作表示困难等瓶颈。本文进一步将量子计算引入这一任务，试图缓解强化学习在组合爆炸场景下的可扩展性问题，因此具有较强的交叉研究价值。

#### 方法概述和架构

本文将流程综合形式化为一个 Markov Decision Process（MDP），把流程图状态、可执行结构修改动作以及由仿真反馈得到的奖励统一纳入强化学习框架。作为经典基线，作者采用 DQN 进行价值函数近似，并在相同训练条件下与量子强化学习方案进行对照。量子方法的核心是用参数化量子电路（PQC）作为 Q 函数近似器，同时设计状态编码与解码机制，将流程规模与所需 qubit 数量解耦，从而改善早期量子 RL 方案在 qubit 需求随问题规模增长而失控的问题。整体流程是：将流程设计状态编码为量子可处理表示，输入量子/经典价值网络估计动作价值，依据 ε-greedy 策略选择动作，环境执行动作并返回奖励，再通过经验回放与目标网络更新参数。文中还提出了多种状态编码策略，用于比较不同量子实现的可扩展性与性能表现。

#### 实验结果分析

作者在一个随着单元数量增加的 flowsheet synthesis 案例上系统评估了经典 DQN 与多种量子 RL 变体，并在相同训练设置下进行对比。结果表明，在较小设计空间中，各类方法都能找到最优流程图设计；在中等规模单元数下，量子方法在每个 episode 的表现上具有竞争力，并且在按参数量衡量时比经典 RL 基线更高效。文中重点强调了可扩展性分析与公平基准对比，但节选内容未给出具体数值。

<details>
<summary>完整摘要</summary>

本文提出将量子强化学习（RL）作为流程综合问题的一种求解策略。在我们此前工作的基础上，本文构建了一个更一般化的框架，将流程综合严格表述为 Markov decision process，并引入量子增强的 RL 算法，以提升求解的可扩展性。早期基于量子的流程综合 RL 实现受限于 qubit 数量需求，而该需求会随着问题复杂度增长而表现出较差的扩展性。本文通过引入状态编码算法，将 qubit 需求与问题规模解耦，从而克服这一挑战。我们采用经典 RL 求解策略作为基线，在相同训练条件下对量子算法进行基准评估。所有算法都在一个单元数量逐步增加的 flowsheet synthesis 问题上进行测试，以分析其性能与可扩展性。结果显示，在较小设计空间中，各种方法都能识别出最优流程图设计；在中等规模的单元数下，量子方法在按 episode 计算时表现出有竞争力的性能，并且相较经典 RL 基线在按参数量计算时更有效率。本文为量子计算在过程系统工程中的未来应用奠定了基础，建立了一个用于比较经典与量子算法的受控基准，并表明本文提出的量子变体在所研究的流程综合问题上仍然具有竞争力。

</details>

---

### [[20_Research/Papers/机器人/Comparative_Analysis_of_Military_Detection_Using_Drone_Imagery_Across_Multiple_Visual_Spectrums|Comparative Analysis of Military Detection Using Drone Imagery Across Multiple Visual Spectrums]]

![[assets/2605.21157_figure.png|800]]

- **arXiv**: [2605.21157](https://arxiv.org/abs/2605.21157)
- **PDF**: https://arxiv.org/pdf/2605.21157
- **详细分析**: [[20_Research/Papers/机器人/Comparative_Analysis_of_Military_Detection_Using_Drone_Imagery_Across_Multiple_Visual_Spectrums|Comparative Analysis of Military Detection Using Drone Imagery Across Multiple Visual Spectrums]]
- **作者**: Sourov Roy Shuvo, Prajwal Panth, Rajesh Chowdhury, Sorup Chakraborty, Sudip Chakrabarty, Prasant Kumar Pattnaik
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

无人机已成为现代军事侦察、目标识别和精准打击中的关键平台，但其在低照度、热成像、夜视和雾化/遮蔽等复杂环境下的目标检测可靠性仍然不足。现有研究往往基于单一成像条件评估模型，较少系统比较不同视觉谱系对检测性能的影响，因此难以支撑真实战场中的稳定部署。本文围绕 drone imagery 下的军事目标检测展开，具有较强的应用导向，尤其适合关注机器人与具身智能中“感知—决策”链路鲁棒性的读者。

#### 方法概述和架构

论文以 KIIT-MiTA 无人机军事场景数据集为基础，构建了四个派生版本：Gray Scale、Thermal Vision、Night Vision 和 ObscuraVision，用于模拟灰度、热成像、夜间和轻度退化等不同视觉条件。作者选择 YOLOv11-small 作为检测模型，在每一种视觉模式上分别训练并评估，输入为 640×640 图像，输出为目标框及类别标签。数据准备阶段通过灰度转换、伪热成像映射、亮度/对比度增强与绿色夜视风格叠加，以及模糊、雾化和对比度扰动等方式生成域偏移样本。训练使用 Kaggle 云端的 NVIDIA T4 GPU，迭代 100 轮，并结合数据增强与学习率调度稳定收敛。评估时重点比较 mAP@50、mAP@50-95、Precision、Recall 和 F1-score，并对四类视觉条件下的检测结果进行横向分析。

#### 实验结果分析

实验基于 KIIT-MiTA 数据集及其四种视觉变体展开，模型在四个数据集上分别训练与测试，评价指标以 mAP@50 和 mAP@50-95 为主。正文节选明确指出，Night Vision 和 Gray Scale 的检测效果最好，Thermal Vision 与 ObscuraVision 也表现稳定，说明 YOLOv11-small 对多种退化场景具有一定鲁棒性。可见文本未给出具体数值，也未在节选中展示与其他基线模型的定量对比细节。

<details>
<summary>完整摘要</summary>

在现代战争中，无人机正成为不同敌对环境下进行情报收集和实施精确打击的重要组成部分。它们能够在安全距离外实时并在敌对环境中运行，因此对于监视和军事行动具有不可替代的价值。KIIT-MiTA 数据集由无人机拍摄的不同军事场景图像组成，为军事目标检测提供了基础，但它并未考虑现实世界中的多种场景类型。基于这一点，为了评估模型在不同条件下的表现，本文构建了四种不同类型的数据集：Gray Scale、Thermal Vision、Night Vision 和 Obscura Vision。这些数据集模拟了低可见度、基于热辐射的成像以及夜间等真实环境。研究中使用 YOLOv11-small 模型进行训练，并用于在多种场景下检测目标。该研究通过为防御和进攻任务中的先进检测系统开发提供贡献，提升了无人机作战的性能与可靠性。

</details>

---

### [[20_Research/Papers/强化学习/Decoupling_Communication_from_Policy_Robust_MARL_under_Bandwidth_Constraints|Decoupling Communication from Policy: Robust MARL under Bandwidth Constraints]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2605.21085](https://arxiv.org/abs/2605.21085)
- **PDF**: https://arxiv.org/pdf/2605.21085
- **详细分析**: [[20_Research/Papers/强化学习/Decoupling_Communication_from_Policy_Robust_MARL_under_Bandwidth_Constraints|Decoupling Communication from Policy: Robust MARL under Bandwidth Constraints]]
- **作者**: Alexi Canesse, Benoît Goupil, Jesse Read, Sonia Vanier
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.36，世界模型 0.16，机器人 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

在多智能体强化学习（MARL）中，智能体之间的通信通常是实现协同的关键，尤其是在部分可观测任务中，例如无人机集群搜救、协同探索与分布式控制等场景。现实应用往往受到严格带宽限制，但许多现有通信架构把“用于策略执行的表示”和“用于智能体间通信的表示”耦合在同一个潜在空间里，导致一旦压缩消息长度，策略能力也会被同步削弱。本文关注的核心问题是：如何在通信受限时，尽量保留策略表达能力，同时仍然允许高效的在线通信，因此具有较强的工程与应用价值。

#### 方法概述和架构

作者提出了两个关键设计。第一，定义了一个归一化的、按智能体计算的带宽预算 β，用来统一描述消息稀疏度、通信轮数和消息维度，使不同通信约束可以在同一尺度下比较。第二，提出 SLIM 这一最小化架构，将通信通路与策略的潜在表示解耦：策略网络保留独立的表示空间，通信模块则单独生成和传递消息，从而避免压缩通信时直接挤压策略容量。模型在每一步决策中仍可进行通信，但通信信息不会与动作策略所依赖的表示混在一起。整体流程上，智能体先基于局部观测形成策略表征，再通过独立通信路径交换消息，最后融合本地信息与接收到的通信信息输出动作。

#### 实验结果分析

作者在多个部分可观测、通信至关重要的 MARL 基准上进行了评估，并与已有方法对比。结果表明，该方法取得了当前最优性能，且在带宽受限时表现出更好的可扩展性和鲁棒性。尤其值得注意的是，当通信预算下降时，性能只出现轻微退化，说明解耦设计有效隔离了通信压缩对策略容量的负面影响。可见文本未给出具体数值，也未提供正文节选中的详细消融结果。

<details>
<summary>完整摘要</summary>

通信在多智能体强化学习（MARL）中有助于实现协同，但许多真实世界应用，例如无人机集群搜救，都运行在极其严格的带宽约束下。许多通信架构仍然存在一个耦合瓶颈：同一个共享潜在表示同时用于策略执行和智能体间通信。因此，缩减消息大小会直接限制策略的潜在空间，往往导致显著的性能下降。为了解决这一问题，我们提出两项贡献。首先，我们引入 β 这一归一化的、按智能体计算的带宽预算，将稀疏性、通信轮数和消息维度统一到一个可比较的约束中。其次，我们提出 SLIM，一种最小化架构，它将通信路径与策略的潜在表示解耦，使我们能够在受益于逐步通信的同时，隔离带宽对策略容量的影响。我们在多个部分可观测且通信至关重要的 MARL 基准上评估了该方法。结果表明，我们的方法取得了最先进的性能，并且在有限通信条件下具有良好的可扩展性和鲁棒性；当带宽减少时，性能仅出现轻微退化。

</details>

---

### [[20_Research/Papers/大模型/AutoRPA_Efficient_GUI_Automation_through_LLM-Driven_Code_Synthesis_from_Interactions|AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions]]

![[assets/2605.21082_figure.png|800]]

- **arXiv**: [2605.21082](https://arxiv.org/abs/2605.21082)
- **PDF**: https://arxiv.org/pdf/2605.21082
- **详细分析**: [[20_Research/Papers/大模型/AutoRPA_Efficient_GUI_Automation_through_LLM-Driven_Code_Synthesis_from_Interactions|AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions]]
- **作者**: Minghao Chen, Xinyi Hu, Zhou Yu, Yufei Yin
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 1.1（加权：大模型 0.9，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

图形用户界面（GUI）上的多步任务广泛存在于网页、桌面和移动场景中，很多任务具有高度重复性，例如报表提交、信息查询和订票等。当前基于大模型的 GUI agent 虽然灵活，但通常采用 ReAct 式逐步推理，每次执行都要反复调用模型，导致 token 成本和运行时开销较高，不适合重复任务的规模化部署。传统 RPA 虽然执行效率高，但依赖人工编写和维护脚本，面对界面变化时也较脆弱。因此，这篇工作值得关注的地方在于：它试图把“灵活但昂贵”的 LLM agent 与“高效但难维护”的 RPA 连接起来，自动从交互中生成可复用的 GUI 自动化代码。

#### 方法概述和架构

论文提出 AutoRPA，一个从交互轨迹中自动蒸馏 RPA 函数的框架。整体流程分为三步：首先由 ReAct 风格的 agent 在目标任务上探索并收集成功轨迹；随后通过 translator agent 将这些带有硬编码动作编号或坐标的 ReAct 步骤，转换为更适合泛化的软编码过程；最后由 builder agent 基于检索增强生成（RAG）和轨迹数据库中的多条历史轨迹，合成稳健的 RPA 代码。为了提高代码可执行性，AutoRPA 还设计了一个混合修复策略：在代码验证阶段，如果生成的 RPA 执行失败，就让 ReAct agent 从断点继续探索，得到纠错示范，再回传给 builder 进行迭代修正。论文将 GUI 环境建模为 POMDP，并把目标定义为为某一类任务生成函数 F_k，使其在尽量减少 token 消耗的同时保证任务成功。

#### 实验结果分析

作者在多个 GUI 环境和三个 GUI 基准上验证了 AutoRPA 的效果，并与现有 LLM-based GUI agent 方案进行比较。结果表明，由 AutoRPA 生成的 RPA 函数能够在相似任务上稳定复用，同时将 token 使用量减少 82% 到 96%。论文还报告称，该方法在保持甚至超过基线成功率的同时，显著提升了运行效率和可重用性。节选中未给出更细的具体数值表格，消融实验和泛化分析在正文后续部分展开。

<details>
<summary>完整摘要</summary>

基于大语言模型（LLM）的 agent 已经在图形用户界面（GUI）的多步交互任务中表现出较强能力。现有研究大多聚焦于提升单任务性能，但在实际应用中，更多场景涉及重复性的 GUI 任务；对于这类任务，反复调用 LLM 进行推理，即 ReAct 范式，效率并不高。在 LLM 出现之前，传统的 Robotic Process Automation（RPA）能够在运行时提供较高效率，但其开发和维护需要大量人工投入。为了弥合这一差距，我们提出 AutoRPA，一个能够将 ReAct 风格 agent 的决策逻辑自动提炼为稳健 RPA 函数的框架。AutoRPA 包含两项核心创新：（1）translator-builder 管线，其中 translator agent 将硬编码的 ReAct 动作转换为软编码流程，builder agent 则通过对多条轨迹进行检索增强生成来合成稳健的 RPA 函数；（2）在代码验证阶段采用混合修复策略，将 RPA 执行与基于 ReAct 的回退机制结合起来，以实现迭代式精炼。跨多个 GUI 环境的实验表明，AutoRPA 生成的 RPA 函数能够成功完成相似任务，同时将 token 使用量降低 82% 到 96%，显著提升了运行时效率和可复用性。

</details>

---

### [[20_Research/Papers/具身智能/Grounding_Driving_VLA_via_Inverse_Kinematics|Grounding Driving VLA via Inverse Kinematics]]

![[assets/2605.21061_figure.png|800]]

- **arXiv**: [2605.21061](https://arxiv.org/abs/2605.21061)
- **PDF**: https://arxiv.org/pdf/2605.21061
- **详细分析**: [[20_Research/Papers/具身智能/Grounding_Driving_VLA_via_Inverse_Kinematics|Grounding Driving VLA via Inverse Kinematics]]
- **作者**: Junsung Park, Hyunjung Shim
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

驾驶领域的 Vision-Language-Action（Driving VLA）模型试图把视觉、语言和动作规划统一到一个端到端策略中，用于自动驾驶中的轨迹预测与规划。然而，作者指出现有方法虽然表面上接收图像输入，实际却常常主要依赖 ego status 和文本指令来生成轨迹，对视觉 token 的利用很弱，容易陷入“盲目规划”。论文认为，这一问题不只是训练不充分，更根源于任务形式本身不合理：只给当前视觉状态、直接监督未来轨迹，会让模型缺少必须利用视觉信息的动力。这使得该工作值得关注，因为它从“任务重定义”的角度解释并修复了 Driving VLA 的视觉失焦问题。

#### 方法概述和架构

论文提出 Grounding Driving VLA via Inverse Kinematics，将驾驶规划重新表述为一个“逆运动学”式问题。首先，模型不再只预测轨迹，而是增加一个 next visual state prediction 目标，让 LLM 先根据当前视觉状态、ego status 和文本命令预测未来视觉场景，从而把视觉监督重新放回输出空间。其次，作者引入一个独立的 Inverse Kinematics Network（IK Network），它是基于 cross-attention 的 conditional diffusion model，推理轨迹时只接收当前视觉状态和预测的未来视觉状态作为输入，不直接使用 ego status 和文本命令。这样做的效果是把轨迹解码过程限制在“当前/未来视觉状态”这组边界条件上，减少绕过视觉特征的捷径。训练时，next-state 预测损失与轨迹损失联合优化；推理时，先由主干生成未来视觉状态，再由 IK Network 输出最终轨迹。

#### 实验结果分析

论文在 NAVSIM-v2 的闭环评测和 nuScenes 基准上进行了实验，对比了多种 7B–8B 级别的 Driving VLA 基线。结果显示，作者的 0.5B 规模模型在轨迹规划性能上可达到与大一个数量级的模型相当的水平，说明结构重设计比单纯扩参更有效。进一步分析（包括 GradCAM、对照式 obstacle stitching、逐样本统计分析等）表明，性能提升主要来自模型恢复了对视觉特征的利用，且这种收益在转弯等动态驾驶场景中最明显。可见文本未给出具体数值，但整体结论是该方法显著缓解了视觉忽略问题，并带来与更大模型相媲美的规划表现。

<details>
<summary>完整摘要</summary>

现有的 Driving VLA 在预测轨迹时，大体上忽略了视觉 token；我们将这一现象归因于任务形式在结构上就是不适定的，而不是训练不足。我们表明，从逆运动学的视角来看，轨迹恢复需要将当前视觉状态和未来视觉状态同时作为边界条件；而现有的 Driving VLA 只提供了前者，这会促使模型仅依赖 ego status 和文本指令走捷径。为了解决这一问题，我们将 Driving VLA 重新设计为逆运动学求解器的形式。第一，我们引入 next visual state prediction 目标，要求 LLM 预测未来视觉场景，以提供稠密的视觉监督并抑制捷径路径。第二，我们设计了一个独立的 Inverse Kinematics Network（基于 cross-attention 的 conditional diffusion model），它只以当前和未来视觉状态作为输入，用于在轨迹解码阶段抑制对 ego status 和文本捷径的依赖。仅凭这一简单的改造，我们的 0.5B 规模模型就恢复了视觉 grounding，并在闭环 NAVSIM-v2 和 nuScenes 基准上达到了与规模大一个数量级以上的 7B–8B VLA 相当的轨迹规划性能。进一步的大量分析显示，这一改进来源于模型重新学会利用视觉特征，而且这种效果在转向等动态驾驶场景中最为显著。

</details>

---

### [[20_Research/Papers/大模型/Causal_Past_Logic_for_Runtime_Verification_of_Distributed_LLM_Agent_Workflows|Causal Past Logic for Runtime Verification of Distributed LLM Agent Workflows]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2605.20923](https://arxiv.org/abs/2605.20923)
- **PDF**: https://arxiv.org/pdf/2605.20923
- **详细分析**: [[20_Research/Papers/大模型/Causal_Past_Logic_for_Runtime_Verification_of_Distributed_LLM_Agent_Workflows|Causal Past Logic for Runtime Verification of Distributed LLM Agent Workflows]]
- **作者**: Benedikt Bollig
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

分布式 LLM agent 工作流并不是单一顺序日志可以刻画的系统：在异步执行中，一个决策只能依赖对当前 lifeline 来说“因果可见”的事件，而不是全局上更早发生的事件。现有运行时监控若按顺序日志理解，会把尚未因果可见的信息也算进来，从而误判分支与循环条件。本文关注如何把运行时验证直接嵌入多智能体协同语言中，使监控结果能够真正影响执行控制，而不是事后审计。

#### 方法概述和架构

论文在 ZipperGen agent-workflow 框架上扩展了 Causal Past Logic（CPL），用于条件分支和 while 循环中的守卫表达。CPL 是一种小型的过去时态逻辑，除了常见的 previous 与 since 之外，还允许守卫检查另一个 lifeline 的“最新因果可见事件”及其上存储的变量值。守卫以源码级形式写在工作流中，由拥有该决策的 lifeline 在线求值，并直接决定控制流走向。为支持在线监控，作者设计了基于向量时钟和 latest-value views 的监控器：向量时钟负责刻画因果可见性，latest-value views 负责维护各 lifeline 最新可见状态。论文还证明了本地在线计算得到的监控值，与事件当前位置上的语义定义完全一致，并给出了 Lean 4 形式化机械化。

#### 实验结果分析

论文给出了一个分布式代码审查场景，用来说明如果只看顺序日志，监控器会把“尚未因果可见”的失败更新误判为应阻止合并的证据。作者证明了所提在线监控算法在语义上正确：局部计算结果与 CPL 在 MSC 语义下的取值一致，因此运行时验证可以作为协调语言的一部分直接参与决策。正文节选还提到已在 ZipperGen 中实现原型，并完成了相关定义与正确性定理的 Lean 4 机械化；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

分布式 LLM agent 工作流不应被当作生成单一顺序日志的系统来监控。在异步执行中，一个决策只能依赖对作出该决策的 lifeline 而言“因果可见”的事件；在某个日志里看起来更早发生的事件，局部上仍可能未知。我们在 ZipperGen agent-workflow 框架上扩展了 Causal Past Logic（CPL），这是一种用于条件语句和 while 循环守卫的小型过去时态逻辑。除了 previous 和 since 等标准过去时态模态之外，守卫还可以检查另一个 lifeline 的最新因果可见事件，以及存储在该事件中的部分变量值。该公式是源码级守卫：它由拥有该决策的 lifeline 在线求值，并可在运行时影响控制流。我们给出了一种结合向量时钟与 latest-value views 的监控器，并证明局部计算得到的监控值与当前事件处该守卫的指称语义一致。因此，运行时验证成为协调语言本身的一部分，而不再是对执行日志的事后检查。

</details>

---

### [[20_Research/Papers/强化学习/For_How_Long_Should_We_Be_Punching_Learning_Action_Duration_in_Fighting_Games|For How Long Should We Be Punching? Learning Action Duration in Fighting Games]]

![[assets/2605.20911_figure.png|800]]

- **arXiv**: [2605.20911](https://arxiv.org/abs/2605.20911)
- **PDF**: https://arxiv.org/pdf/2605.20911
- **详细分析**: [[20_Research/Papers/强化学习/For_How_Long_Should_We_Be_Punching_Learning_Action_Duration_in_Fighting_Games|For How Long Should We Be Punching? Learning Action Duration in Fighting Games]]
- **作者**: Hoang Hai Nguyen, Kurt Driessens, Dennis J. N. J. Soemers
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

格斗游戏如 Street Fighter II 对强化学习（RL）提出了特殊挑战：对局节奏快、决策窗口短，而且动作时序本身就是胜负关键。现有RL框架通常固定每隔1帧或N帧决策，这虽然保证了响应及时性，但也把“何时出手”硬编码死了，导致智能体要么反应过快得不真实，要么因为固定间隔过长而错失时机。本文值得关注之处在于，它不只让智能体学“做什么动作”，还让它学“这个动作要持续多久”，把动作持续时间显式纳入决策过程。

#### 方法概述和架构

论文以 FightLadder 环境中的 Street Fighter II - Special Champion Edition 为实验平台，采用 PPO 训练Ryu角色与游戏内置脚本Bot对战。作者将原本固定的 frame skip 机制扩展为可学习的动作持续时间：在每次决策时，智能体同时输出普通动作（移动、攻击或连招）以及要跳过的帧数。方法上比较了三类策略：固定 frame skip、每步随机采样 frame skip，以及学习 frame skip；其中学习型策略又分为“分离头”（一个输出动作、一个输出帧跳过数）和“组合头”（把动作与帧跳过数做笛卡尔积后统一输出）两种实现。输入是堆叠的历史游戏画面，输出则是当前动作及其持续帧数，训练过程中通过 PPO 端到端优化。

#### 实验结果分析

实验在 FightLadder 的脚本Bot上进行，评估指标主要是对局胜率，同时观察训练过程中的回报、回合长度和动作分布变化。结果显示，学习到的动作持续时间可以达到与合适固定 frame skip 相当的性能，但并不能单独保证鲁棒性；多数情况下，表现最好的反而是较高的 frame skip，也就是较低的响应频率。作者还发现，较粗粒度的时间分辨率更容易学到重复同一动作的利用型策略，而脚本Bot对这类模式较为脆弱。对未见过的对手，泛化表现起伏较大；节选中对部分微调实验给出了胜率表，但整体结论是：自适应时序有潜力，但仍需结合更强的对手、多样化训练或更稳健的策略设计。

<details>
<summary>完整摘要</summary>

格斗游戏如 Street Fighter II 由于其快节奏、实时性的特点，会给强化学习（RL）智能体带来独特挑战。在大多数RL框架中，智能体会被硬编码为以固定间隔做出决策，通常是每一帧或每N帧一次。尽管这种设计能够确保及时响应，但它限制了智能体调整反应时机的能力。每帧行动可以带来逐帧精确的反应，但与人类玩家相比并不现实；而更长的固定间隔虽然能降低计算成本，却会削弱响应能力。我们考虑一种替代的决策框架：智能体不仅学习该采取什么动作，还学习该动作应持续多久。通过联合预测动作与持续时间，智能体可以根据游戏中的不同情境动态调整响应速度。我们使用开源的 FightLadder 环境实现该方法，并让智能体与脚本化的内置Bot对战，系统测试不同的 frame skip 配置，以分析其对性能、响应性以及学习到的行为模式的影响。实验表明，学习到的时序可以达到精心选择的固定 frame skip 的性能，并鼓励形成可重复的动作模式，但单靠这一点并不能保证鲁棒性。在大多数情况下，我们观察到智能体在持续较高的 frame skip 值（即较低的响应频率）下表现最佳。这种策略更容易学习到利用型策略，即反复重复同一个动作，而脚本Bot似乎对此较为脆弱。

</details>

---

### [[20_Research/Papers/强化学习/Multi-Step_Likelihood-Ratio_Correction_for_Reinforcement_Learning_with_Verifiable_Rewards|Multi-Step Likelihood-Ratio Correction for Reinforcement Learning with Verifiable Rewards]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2605.20865](https://arxiv.org/abs/2605.20865)
- **PDF**: https://arxiv.org/pdf/2605.20865
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Step_Likelihood-Ratio_Correction_for_Reinforcement_Learning_with_Verifiable_Rewards|Multi-Step Likelihood-Ratio Correction for Reinforcement Learning with Verifiable Rewards]]
- **作者**: Deokgyu Yoon, Hyungkyu Kang, Joongkyu Lee, Byeongchan Kim, Gyungin Shin, Sungrae Park, Min-hwan Oh
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

这篇论文关注的是带有可验证奖励的强化学习（RLVR），其核心应用场景是提升大语言模型的推理能力，尤其适用于数学、逻辑与可自动判分的任务。当前主流的PPO类目标函数虽然训练稳定，但本质上是对真实策略梯度目标的局部近似，因此会带来结构性偏差。论文指出，这种偏差通常需要借助信赖域机制加以控制，而如何在偏差与方差之间取得更合理的平衡，仍是RLVR中的关键问题，因此值得关注。

#### 方法概述和架构

作者提出了N-step forward trace：在PPO surrogate objective的基础上，引入未来N-1个token的累计似然比，从而把局部近似扩展为更长步长的前向轨迹估计。基于这一思想，论文提出N-Step Forward-Trace Policy Optimization（NFPO），将N-step forward trace 融入 masked policy gradient 框架中。训练时，NFPO以当前策略生成的token序列为基础，利用连续多个token的似然比来修正策略更新信号；当N较小时更接近PPO的局部近似，当N增大时又逐步逼近精确策略梯度目标。整体上，NFPO提供了一条在PPO surrogate 与 exact policy gradient 之间连续过渡的路径，用于更系统地控制偏差-方差权衡。作者还从理论上分析了该目标的策略改进性质，并说明在合适的N取值下可获得更紧的策略改进界。

#### 实验结果分析

论文在多个推理基准上进行了实验，验证NFPO的有效性；从摘要可见，其对综合性推理任务表现出稳定提升。对比对象主要是标准PPO surrogate及相关强化学习基线，结果表明NFPO在多数设置下都能带来更好的性能。论文同时给出理论分析，说明该方法在适当选择N时，相比标准PPO surrogate具有更紧的策略改进界。正文节选未提供具体数据、基准名称或消融细节，因此可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

带有可验证奖励的强化学习（RLVR）在提升大语言模型推理能力方面发挥着关键作用。然而，广泛使用的PPO代理目标在本质上是局部的，因为它依赖于精确策略梯度目标的局部近似。虽然这种近似通过降低由重要性采样引入的方差提高了稳定性，但也会在代理目标中引入结构性偏差，而这种偏差必须通过信赖域机制加以控制。在这项工作中，我们提出了N-step forward trace，它通过累积未来N-1个token的似然比来增强PPO代理目标。基于这一思想，我们提出了N-Step Forward-Trace Policy Optimization（NFPO），这是一种实用的RLVR算法，将N-step forward trace集成到masked policy gradient框架中。NFPO在PPO代理目标与精确策略梯度目标之间提供了一条连续的桥梁，为控制偏差-方差权衡提供了一个有原则的方法。我们的理论分析表明，在选择合适的N时，所提出的目标函数能给出比标准PPO代理更紧的策略改进界。在综合推理基准上的实验表明，NFPO能够持续提升性能，从而支持了我们的理论发现。

</details>

---

### [[20_Research/Papers/具身智能/ArchSIBench_Benchmarking_the_Architectural_Spatial_Intelligence_of_Vision-Language_Models|ArchSIBench: Benchmarking the Architectural Spatial Intelligence of Vision-Language Models]]

![[assets/2605.20837_figure.png|800]]

- **arXiv**: [2605.20837](https://arxiv.org/abs/2605.20837)
- **PDF**: https://arxiv.org/pdf/2605.20837
- **详细分析**: [[20_Research/Papers/具身智能/ArchSIBench_Benchmarking_the_Architectural_Spatial_Intelligence_of_Vision-Language_Models|ArchSIBench: Benchmarking the Architectural Spatial Intelligence of Vision-Language Models]]
- **作者**: Qirui Shen, Wenda Wang, Jiachen Lu, Zilong Huang, Jin Bai, Lei He, Hongxuan Chen, Weixin Huang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.8（加权：具身智能 0.6，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

建筑空间智能是机器人导航、具身交互以及3D场景理解与生成中的基础能力，但现有针对视觉语言模型（VLMs）的空间评测，大多只覆盖相对方位、距离比较、物体计数等最基础任务。相比之下，建筑空间中的关键能力还包括对平面布局、交通流线、功能分区、空间尺度和结构配置的理解与推断，这些往往无法仅凭局部几何线索直接得到。作者指出，现有基准普遍偏向对象级、单房间级的空间关系，缺少面向建筑空间层级认知的系统评价，因此很难判断当前VLM是否真正具备接近人类、尤其是专业建筑师的空间智能。

#### 方法概述和架构

本文提出 ArchSIBench，一个面向建筑空间智能的基准数据集与评测体系，基于建筑学、认知科学和心理学构建能力层级。该基准将建筑空间智能划分为五个核心维度：感知、推理、导航、转换和配置，并进一步细分为17个子任务，覆盖从基础空间判断到更高层的布局理解、视角变换、2D/3D转换与功能分析。数据来源包括建筑技术图纸（如平面图、剖面图）、3D表示（如轴测图、渲染图）和真实场景图像，共构建3,000组问答对，且由具备建筑背景的专家进行人工标注与审核。评测时，作者将同一套问题输入给27个VLM进行统一测试，并设置有无建筑训练背景的双重人类基线，用于比较模型与不同层次人类能力的差异。

#### 实验结果分析

实验在 ArchSIBench 上对27个VLM进行了系统评测，比较对象包括多种主流模型与人类基线。结果显示，大多数模型的建筑空间智能与人类水平存在明显差距，而且在不同能力维度上的表现差异很大；部分当前最先进模型可以接近没有建筑训练背景的人类评测者，但距离受过建筑专业训练的人类仍有清晰差距。作者特别指出，模型在空间转换和配置推理方面的短板最为明显。正文节选中未给出具体数值。

<details>
<summary>完整摘要</summary>

建筑空间智能，即识别并推断建筑空间的能力，是机器人导航、具身交互以及3D场景理解与生成等任务的基础。尽管已有大量研究评估了视觉语言模型（VLMs）的基础空间能力，例如相对方位、距离比较和物体计数，但这些任务仅覆盖了空间认知中最初级的层次，且在很大程度上忽略了对建筑空间更高层次的认知，包括布局理解、流线模式以及功能分区等。本文提出 ArchSIBench，一个基于建筑学、认知科学和心理学视角构建的建筑空间智能基准。ArchSIBench 覆盖五个核心维度：感知、推理、导航、转换和配置，共包含17个细粒度子任务。通过具有建筑背景专家的精心人工标注，我们构建了3,000个问答对，以实现对建筑空间智能的全面评估。基于 ArchSIBench，我们评测了多种VLM，并发现大多数模型的建筑空间智能与人类基线存在显著差异；此外，模型在各能力维度上的表现也存在很大波动。一些最先进的模型能够接近没有建筑训练背景的人类评测者的水平。然而，与接受过建筑训练的人类评测者相比，仍然存在明显差距，尤其是在空间转换和配置推理方面。我们相信 ArchSIBench 将为衡量和提升VLM的建筑空间智能提供重要洞见与系统性资源。数据集和代码已公开，地址为 https://huggingface.co/datasets/ArchSIBench/ArchSIBench 。

</details>

---

### [[20_Research/Papers/大模型/Distribution-Aware_Reward_Reinforcement_Learning_over_Predictive_Distributions_for_LLM_Regression|Distribution-Aware Reward: Reinforcement Learning over Predictive Distributions for LLM Regression]]

![[assets/2605.20740_figure.png|800]]

- **arXiv**: [2605.20740](https://arxiv.org/abs/2605.20740)
- **PDF**: https://arxiv.org/pdf/2605.20740
- **详细分析**: [[20_Research/Papers/大模型/Distribution-Aware_Reward_Reinforcement_Learning_over_Predictive_Distributions_for_LLM_Regression|Distribution-Aware Reward: Reinforcement Learning over Predictive Distributions for LLM Regression]]
- **作者**: Jungsoo Park, Hyungjoo Chae, Ethan Mendes, Jay DeYoung, Varsha Kishore, Wei Xu, Alan Ritter
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.67（加权：大模型 0.55，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL, ComputerVision

#### 研究背景与动机

大模型已经能够从文本、代码和分子字符串等异构输入中回归连续数值，但现有训练目标通常只对每个解码出的浮点数单独打分，主要提升点估计，却不能保证预测分布是校准的。这会限制那些依赖候选排序、相对比较和不确定性估计的应用，例如代码性能预测、科学实验结果预测和分子性质预测。本文值得关注之处在于，它把 LLM 回归从“只追求单点更准”推进到“直接优化一组采样结果形成的预测分布”。

#### 方法概述和架构

论文提出 Distribution-Aware Reward（DAR），是一种 on-policy 强化学习目标，专门用于训练 LLM 在回归任务上生成更好的 predictive distributions。方法会对同一个输入采样 K 次，得到一组数值预测，并把这些 rollouts 视作经验预测分布，而不是彼此独立的答案。随后使用 CRPS（Continuous Ranked Probability Score）评估整组预测与真实值的匹配程度，其中既考虑预测值靠近目标的程度，也考虑样本之间的分散性。由于强化学习需要把分布级别的分数分配到单个 rollout，DAR 进一步采用 leave-one-out credit assignment：比较“包含某个 rollout 的分布”与“去掉该 rollout 的分布”的 CRPS 差值，把这个边际贡献作为该 rollout 的奖励。这样，模型既会被鼓励把预测放在正确位置，也会被鼓励保留有用的分布宽度，避免 rollouts 过度塌缩到单点。

#### 实验结果分析

作者在三个任务上验证了方法：受控的 Gaussian-mixture 合成回归、代码性能预测，以及基于 SMILES 的分子性质预测，并与监督微调和逐点强化学习基线比较。结果显示，DAR 在多个任务上都优于这些基线，尤其在排序相关指标上提升明显；例如在 KBSS 上，Spearman 相关系数提升了 6 个点。论文还指出，在 MoleculeNet 上，DAR 仅使用 SMILES 字符串输入，表现仍能与强大的图模型和 3D 分子模型竞争。进一步分析表明，DAR 缓解了 rollout 多样性塌缩，并改善了不确定性诊断；可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

大语言模型可以从文本、代码和分子字符串等异构输入中预测实值数量，但大多数训练目标都是对每个解码出的浮点数单独打分，这会改进点估计，却不能保证预测分布是校准的。这限制了需要候选排序或不确定性估计的应用。我们提出 Distribution-Aware Reward，一种 on-policy 强化学习目标，其核心贡献是训练语言模型为回归任务产生更好的预测分布，而不仅仅是针对单个解码输出优化其与标量目标的匹配。我们的方法把多个解码样本视为经验预测分布，用 Continuous Ranked Probability Score 进行评估，并通过 leave-one-out 信用分配来衡量每次 rollout 对分布质量的边际贡献，从而奖励那些既准确又具有适当分散性的预测。我们在受控的高斯混合任务、代码性能预测以及基于 SMILES 字符串的分子性质预测上评估了该方法。跨任务结果表明，我们的方法优于监督微调和逐点强化学习基线，并在排序相关性上取得了显著提升，包括在 KBSS 上提升 6 个 Spearman 点。对于 MoleculeNet，我们仅使用 SMILES 字符串输入，但仍能与强大的基于图和 3D 的分子模型相抗衡。进一步分析显示，该方法缓解了 rollout 多样性塌缩，并改善了不确定性诊断，说明直接优化预测分布可以让语言模型回归更加稳健且校准更好。

</details>

---

### [[20_Research/Papers/大模型/An_Application-Layer_Multi-Modal_Covert-Channel_Reference_Monitor_for_LLM_Agent_Egress|An Application-Layer Multi-Modal Covert-Channel Reference Monitor for LLM Agent Egress]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2605.20734](https://arxiv.org/abs/2605.20734)
- **PDF**: https://arxiv.org/pdf/2605.20734
- **详细分析**: [[20_Research/Papers/大模型/An_Application-Layer_Multi-Modal_Covert-Channel_Reference_Monitor_for_LLM_Agent_Egress|An Application-Layer Multi-Modal Covert-Channel Reference Monitor for LLM Agent Egress]]
- **作者**: Alfredo Metere
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

在大模型 Agent 的真实部署中，允许它发消息、发图片甚至发音频，本身就可能成为数据外泄通道。现有的目的地白名单和内容扫描，主要检查“发给谁”和“发了什么显式敏感词”，却很难判断一个看似正常的载荷是否在暗中携带信息。论文关注的是应用层的隐蔽信道问题，覆盖文本、图像、音频以及时序/大小等元数据，因此对 Agent 出站安全具有直接现实意义。

#### 方法概述和架构

论文提出一个面向 LLM Agent 出站流量的多模态隐蔽信道参考监控器，核心是在单一出站闸口上做统一拦截与改写。文本侧采用十个按顺序执行的降容量阶段，包括规范化、敏感值追踪、熵与高压缩性检测、重放识别、噪声注入、节流与行为塑形等，并为每个下游目标维护一个 leaky-bucket 容量账本。多媒体侧提供两个“洗牌器”：一个基于傅里叶域的音频带限器，用来压制超声和可听带中的声码/调制载体；一个对 RGB 图像做 6bit/通道重量化并结合平均亮度分桶，用来破坏 LSB 隐写和跨图像亮度/顺序载体。为了避免把合法媒体和“被音频化/栅格化的数据”混为一谈，论文引入启动时的密码学合法性证明：审计器在启动时发布可信 Ed25519 密钥及允许的 {kind, data-class} 对，只有带有效签名且属于授权类别的载荷才免于洗牌，未签名媒体默认视为可疑。

#### 实验结果分析

作者用 15 种工作中的隐蔽信道编码器做对抗评测，覆盖文本、图像和音频，并用 Miller-Madow 校正后的互信息衡量残余容量。可见文本显示，该实现能把所有可被破坏的信道残余容量压到 0；对唯一无法在不破坏图像质量前提下完全消除的“平均亮度”信道，也给出了明确上界。节选中未给出具体数值，因此无法补充定量提升幅度；但从结论看，该方法相较传统白名单/DLP 方案，重点补上了多模态隐蔽信道与 sonification 这类难以靠内容分类器识别的外泄路径。

<details>
<summary>完整摘要</summary>

大语言模型（LLM）Agent 如果能够发送消息，就可能在消息中泄露数据。目的地白名单和内容扫描器并不能约束一个看似无害的载荷本身是否构成隐蔽信道：被攻陷的 Agent 可以用零宽字符、同形异义字、空白、Base64、JSON 键顺序、消息时序或消息大小来编码比特；在二进制出站中，还可以利用图像像素的最低有效位（LSB）平面、跨图像的平均亮度、图像序列排列、超声频率，或者可听频段中的声码化数据。我们的出站参考监控器有三项贡献。（i）一个文本管线：包含十个降容量阶段、按目标端点维护的 leaky-bucket 容量账本，以及一种分阶段的部署姿态，从一开始就把无损阶段强制启用。（ii）两个媒体洗牌器：一个基于傅里叶域的音频带限器，以及一个对红绿蓝（RGB）图像做位深和平均亮度分桶的处理器；它们由启动时的密码学合法性证明所门控：审计器在启动时发布可信的 Ed25519 密钥以及 {kind, data-class} 对；只有能用授权类别的验证签名通过校验的载荷才被免于处理。该证明机制绕开了“真实媒体”与“被声码化或栅格化作为载体的数据”之间难以解决的内容分类问题；未签名媒体默认可疑；基于内容地址的规范化器关闭了跨图像排列信道。（iii）残余容量定义为嵌入比特与恢复比特之间经 Miller-Madow 校正后的互信息（当信道被摧毁时为零），并通过涵盖文本、图像和音频的 15 个工作编码器组成的对抗性集合进行测量。参考实现将所有可摧毁信道的残余容量都降为零，并且对唯一一个不能在不破坏图像的情况下摧毁的信道（每图平均亮度）给出明确上界。

</details>

---

### [[20_Research/Papers/大模型/AGPO_Adaptive_Group_Policy_Optimization_with_Dual_Statistical_Feedback|AGPO: Adaptive Group Policy Optimization with Dual Statistical Feedback]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2605.20722](https://arxiv.org/abs/2605.20722)
- **PDF**: https://arxiv.org/pdf/2605.20722
- **详细分析**: [[20_Research/Papers/大模型/AGPO_Adaptive_Group_Policy_Optimization_with_Dual_Statistical_Feedback|AGPO: Adaptive Group Policy Optimization with Dual Statistical Feedback]]
- **作者**: Miaobo Hu, Shuhao Hu, Bokun Wang, Ruohan Wang, Xin Wang, Xiaobo Guo, Daren Zha, Jun Xiao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

强化学习被用于提升大语言模型的推理能力，但现有 PPO 和 GRPO 往往依赖固定的裁剪阈值与解码温度，导致训练过程对超参数很敏感，也更容易出现不稳定。对于数学与 STEM 推理这类需要持续探索、又要求更新幅度受控的任务，这种“固定策略”尤其容易限制效果。作者因此关注如何利用训练过程中的群体统计信息，动态调节策略更新强度与采样探索程度，以降低调参成本并提升鲁棒性。

#### 方法概述和架构

论文提出 AGPO（Adaptive Group Policy Optimization），它是对 GRPO 的一种无需 critic 的改进。方法从同一组样本中构建共享的统计状态，并据此驱动两个控制器：其一是自适应裁剪，根据奖励离散度与偏态、探针投票熵、策略熵以及逐步 KL 漂移来动态设定信任域大小，从而控制每次策略更新的幅度；其二是双向自适应温度采样，在基础温度附近依据“居中不确定性”对解码温度进行升温或降温，以同时支持探索与收敛。训练时，模型先生成一组候选回答，再由群体统计信号决定更新约束和下一轮采样温度，二者共享同一统计反馈，因此能协同作用而不是彼此独立调参。

#### 实验结果分析

作者在 9 个中英文数学与 STEM 基准上评测了该方法，以 Qwen2.5-14B 为主模型，在相同生成 token 预算下，AGPO 整体优于 PPO 和 GRPO。摘要中给出的代表性结果包括：在 GSM8K 上达到 67.3%，在 MATH 上达到 40.5%。此外，方法还能迁移到 Llama-3-8B 和 Gemma-2-9B，说明其并不依赖单一底座模型；消融实验也表明，自适应裁剪与双向温度模块具有互补性。

<details>
<summary>完整摘要</summary>

强化学习可以提升大语言模型的推理能力，但 PPO/GRPO 通常使用固定的裁剪阈值和解码温度，这使得训练过程脆弱且高度依赖调参。我们提出自适应组策略优化（Adaptive Group Policy Optimization, AGPO），这是对 GRPO 的一种不需要 critic 的改进，它利用组级统计量同时控制更新幅度和探索强度。AGPO 使用一个由探针（probe）得到的共享统计状态，来驱动两个控制器：（i）自适应裁剪：根据奖励离散度与偏态、探针投票熵、策略熵以及逐步 KL 漂移来设置信任域大小；（ii）双向自适应温度采样：围绕基础温度，根据相对于运行基线的居中不确定性，对解码进行升温或降温。在 9 个英文和中文数学/STEM 基准上，使用 AGPO 训练的 Qwen2.5-14B 在相同生成 token 预算下优于 PPO/GRPO，在 GSM8K 上达到 67.3%，在 MATH 上达到 40.5%。这些增益还能迁移到 Llama-3-8B 和 Gemma-2-9B，消融实验也证实两个模块具有互补作用。我们的实现已公开发布在 https://github.com/wandugu/paper_agpo 。

</details>

---

### [[20_Research/Papers/强化学习/Design_for_Manufacturing_A_Manufacturability_Knowledge-Integrated_Reinforcement_Learning_Framework_for_Free-Form_Pipe_Routing_in_Aeroengines|Design for Manufacturing: A Manufacturability Knowledge-Integrated Reinforcement Learning Framework for Free-Form Pipe Routing in Aeroengines]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2605.20644](https://arxiv.org/abs/2605.20644)
- **PDF**: https://arxiv.org/pdf/2605.20644
- **详细分析**: [[20_Research/Papers/强化学习/Design_for_Manufacturing_A_Manufacturability_Knowledge-Integrated_Reinforcement_Learning_Framework_for_Free-Form_Pipe_Routing_in_Aeroengines|Design for Manufacturing: A Manufacturability Knowledge-Integrated Reinforcement Learning Framework for Free-Form Pipe Routing in Aeroengines]]
- **作者**: Caicheng Wang, Zili Wang, Shuyou Zhang, Yongzhe Xiang, Zheyi Li, Liangyou Li, Jianrong Tan
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

在先进航空发动机设计中，管路布置不仅要满足功能需求，还必须兼顾后续制造可行性，属于典型的 Design for manufacturing 问题。现有管路设计流程往往与下游制造环节相互割裂，导致设计一旦进入加工阶段，常常需要反复试错和人工迭代才能得到可制造方案。对于自由形状管路而言，这种问题尤为突出，因为其几何复杂、约束多、且容易与障碍物或制造设备能力发生冲突。本文值得关注之处在于，它尝试把制造知识直接融入强化学习优化过程，从源头上让“可设计”与“可制造”统一起来。

#### 方法概述和架构

论文提出了基于 Frenet 标架的管路优化框架 FPRO（Frenet-based pipe routing optimization）。该方法将管路路由问题形式化为 Frenet 框架下的边值问题，用曲率和挠率轮廓来表示管道中心线，并通过三次 Hermite 插值生成这些几何控制量。为了把制造约束纳入优化过程，作者将领域制造知识编码为曲率和挠率允许范围的约束，从而在搜索空间中直接排除不可制造解。优化阶段采用 PPO 进行强化学习，并结合随机探索与分阶段引导的奖励机制，使智能体在逐步接近目标端点的同时兼顾路径长度、避障和制造性。最后，框架通过统一映射将优化得到的路径转换为弯管模具的运动轨迹，从而可以直接驱动六轴自由弯管机完成加工。

#### 实验结果分析

实验表明，FPRO 相比基于笛卡尔坐标的方法，能够稳定生成无碰撞且可制造的管路路径，并得到更平滑的几何曲线。与现有强化学习基线相比，它在收敛速度以及终端对齐、路径长度、障碍物规避和制造可行性等方面表现更优。论文还进行了真实制造验证，结果显示加工出的管件与数字设计在几何上具有较高一致性，说明该方法具备实际落地可行性。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

设计即制造在先进航空发动机开发中具有关键作用，因为复杂部件需要仔细考虑其可制造性。然而，当前管路设计实践在很大程度上仍与下游制造相分离，往往需要通过大量人工和试错式迭代才能获得可制造的设计。为解决这一问题，本文提出 Frenet-based pipe routing optimization（FPRO）框架，这是一种将制造知识集成到强化学习中的自由形管路设计方法，面向航空发动机中的自由形管路优化。FPRO 将路由问题表述为 Frenet 标架下的边值问题。在该框架中，管道路径由曲率和挠率轮廓表示，并通过三次 Hermite 插值生成。为了实现设计与制造的融合，作者将特定领域的制造知识嵌入为曲率和挠率可允许范围的约束。路径优化使用 proximal policy optimization 算法完成，并结合随机探索与分阶段引导的奖励机制。随后，一个统一映射公式将优化后的路径转换为弯管模具的运动轨迹，使其能够直接在六轴自由弯管机上制造。实验结果表明，与基于笛卡尔坐标的方法相比，FPRO 能够持续生成无碰撞、可制造且几何更平滑的路径。与最先进的强化学习基线相比，它在收敛速度以及终端对齐、路径长度、避障和可制造性方面也表现出更优性能。真实世界验证进一步证实，实际制造出的管件与其数字设计在几何上高度一致，验证了 FPRO 的实践可行性。

</details>

---

### [[20_Research/Papers/强化学习/Mahjax_A_GPU-Accelerated_Mahjong_Simulator_for_Reinforcement_Learning_in_JAX|Mahjax: A GPU-Accelerated Mahjong Simulator for Reinforcement Learning in JAX]]

![[assets/2605.20577_figure.png|800]]

- **arXiv**: [2605.20577](https://arxiv.org/abs/2605.20577)
- **PDF**: https://arxiv.org/pdf/2605.20577
- **详细分析**: [[20_Research/Papers/强化学习/Mahjax_A_GPU-Accelerated_Mahjong_Simulator_for_Reinforcement_Learning_in_JAX|Mahjax: A GPU-Accelerated Mahjong Simulator for Reinforcement Learning in JAX]]
- **作者**: Soichiro Nishimori, Shinri Okano, Keigo Habara, Sotetsu Koyamada, Eason Yu, Masashi Sugiyama
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

立直麻将（Riichi Mahjong）是典型的多玩家、不完全信息、强随机性的复杂决策任务，既与真实世界中的博弈和序列决策问题高度相似，也很适合作为强化学习研究平台。现有不少麻将智能体主要依赖人类对局日志进行监督学习或离线强化学习预训练，这使得方法往往带有人类先验，难以验证“从零开始”自博弈学习的可行性。另一方面，麻将环境状态维度高、对局回合长、四人交互复杂，传统 CPU 仿真器很容易成为大规模自博弈训练的瓶颈，因此构建高吞吐、可并行的 GPU 环境具有很强的研究价值。

#### 方法概述和架构

论文提出 Mahjax，一个用 JAX 实现的、完全向量化的立直麻将环境，目标是让强化学习可以在 GPU 上进行大规模并行 rollout。其 API 兼容 Pgx 风格，状态被设计为不可变的 JAX 数组数据结构，统一保存手牌、分数、风向、副露、mask 等信息，便于 JIT 编译和批量计算。为了适配 GPU 并减少控制流分歧，作者将大量 if-else 逻辑替换为矩阵运算，并对高开销的役种（Yaku）计算做了缓存，将可能的组合统计预先编码为 bitmask。环境同时提供动作空间与合法动作掩码，若执行非法动作则立即终止并给出惩罚；观测空间则面向 Transformer 设计，包含手牌索引、行动历史、shanten 等结构化特征。除此之外，Mahjax 还集成了基于 SVG 的可视化和网页交互界面，用于调试和分析智能体行为。

#### 实验结果分析

在性能评测中，作者将 Mahjax 与 CPU 版的 Libriichi 以及 Pgx 的 Shogi 环境作对比，并在配备 8 张 NVIDIA A100 GPU 的机器上测试吞吐量。结果显示，Mahjax 在无红牌规则下最高可达每秒 200 万步，在红牌规则下可达每秒 100 万步，整体明显快于 Libriichi，且优于 Pgx Shogi。为了验证环境可用于学习，作者在无红牌、单回合设置下，用 500k 样本做行为克隆预训练，再用 PPO 加 KL 正则进行微调；训练在 1,024 个并行环境上进行，100 million 步约耗时 5.8 小时。评测结果表明，训练后的智能体相较于基线策略能够稳定取得更好的平均名次，说明 Mahjax 适合用于深度强化学习研究。

<details>
<summary>完整摘要</summary>

立直麻将是一种多玩家、不完全信息游戏，具有随机性强和状态空间高维等特点。这些属性共同构成了强化学习中的一类独特挑战，并与现实世界中的复杂决策问题相呼应。尽管先前研究大量依赖人类对局日志进行监督学习，以预训练策略，能够从零开始学习（tabula rasa）的算法更具普适性，这一点也已由 AlphaZero 系列工作所证明。为了促进这类研究，我们提出 Mahjax：一个完全向量化的立直麻将环境，使用 JAX 实现，支持在图形处理器（GPU）上进行大规模 rollout 并行化。我们还提供了一个高质量可视化工具，以简化调试并增强与训练后智能体的交互。实验结果表明，在 8 张 NVIDIA A100 GPU 上，Mahjax 在无红牌规则和红牌规则下分别可达到每秒最多 200 万步和 100 万步的吞吐量。此外，我们还通过展示智能体能够有效训练并提升相对于基线策略的名次，验证了该环境在强化学习中的实用性。

</details>

---

### [[20_Research/Papers/强化学习/Complementing_reinforcement_learning_with_SFT_through_logit_averaging_in_the_post_training_of_LLMs|Complementing reinforcement learning with SFT through logit averaging in the post training of LLMs]]

![[assets/2605.20555_figure.png|800]]

- **arXiv**: [2605.20555](https://arxiv.org/abs/2605.20555)
- **PDF**: https://arxiv.org/pdf/2605.20555
- **详细分析**: [[20_Research/Papers/强化学习/Complementing_reinforcement_learning_with_SFT_through_logit_averaging_in_the_post_training_of_LLMs|Complementing reinforcement learning with SFT through logit averaging in the post training of LLMs]]
- **作者**: Xingwei Gan, Ying Zhu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

大模型后训练通常依赖两条路线：先做 SFT 让模型学会稳定的格式与表达，再用强化学习提升推理与答题能力。但经典做法往往需要 KL 正则把策略强行拉回 SFT 参考模型，这会连带限制后续优化，容易保留 SFT 的格式优势却压制模型进一步突破推理上限。本文关注如何在不使用 KL 约束和 critic 的情况下，把 SFT 的“格式能力”和 RL 的“推理能力”更自然地结合起来，这对数学推理、中文理科题和通用知识问答都很有现实意义。

#### 方法概述和架构

论文提出一种基于 logits 平均的后训练方法：将冻结的参考策略（如 SFT）与可训练策略的 logits 按权重 α 线性混合，再通过 softmax 得到混合策略 π^mix。训练时只更新可训练策略参数，参考策略始终冻结；rollout 也从混合策略采样，因此参考策略不仅提供锚定，还会部分参与探索。作者把该方法嵌入 GRPO，构造了基于混合策略的 importance ratio 和裁剪目标，替代传统 RLVR 中对原策略和参考策略之间的 KL 约束。论文还给出两种权重方案：固定权重直接设定 α；自适应权重则在验证集上比较“只用可训练策略”和“混合策略”的正确性增益与遗忘，依据净收益通过 sigmoid 动态调整 α。

#### 实验结果分析

实验在 MATH、cn-k12 和 MMLU 上进行，模型规模覆盖 Qwen2.5-Instruct 1.5B、3B、7B，并与经典 KL 正则化 GRPO 对比。结果显示，在全部 9 个“数据集 × 模型规模”组合上，该方法要么优于，要么至少与基线持平。正文节选还提到，固定混合与自适应混合都进行了比较，并做了 SFT 锚点与 base 锚点的消融；不过节选中未给出具体数值。

<details>
<summary>完整摘要</summary>

我们提出一种新方法：将冻结的参考策略（例如 SFT）与可训练策略的 logits 进行平均，并把该方法融入 Group Relative Policy Optimization（GRPO）中。与 Reinforcement Learning with Verifiable Rewards（RLVR）方法不同，我们的方法不使用 Kullback-Leibler（KL）正则项，也不使用 critic；可训练策略与参考锚点通过 logits 平均结构耦合，从而既利用可训练策略的推理能力，又保持 SFT 的格式优势。我们在 MATH、cn-k12 和 MMLU 上评估了该方法，结果表明，相比经典的带 KL 正则的 GRPO，它取得了更高的准确率，或者至少达到了可比的准确率。

</details>

---

### [[20_Research/Papers/大模型/AgentAtlas_Beyond_Outcome_Leaderboards_for_LLM_Agents|AgentAtlas: Beyond Outcome Leaderboards for LLM Agents]]

![[assets/2605.20530_figure.png|800]]

- **arXiv**: [2605.20530](https://arxiv.org/abs/2605.20530)
- **PDF**: https://arxiv.org/pdf/2605.20530
- **详细分析**: [[20_Research/Papers/大模型/AgentAtlas_Beyond_Outcome_Leaderboards_for_LLM_Agents|AgentAtlas: Beyond Outcome Leaderboards for LLM Agents]]
- **作者**: Parsa Mazaheri, Kasra Mazaheri
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

随着大模型智能体开始在代码库、浏览器、操作系统、日历、文件系统和工具生态中执行真实任务，评估问题已经不再是“最终答案对不对”这么简单，而是要同时判断它何时该行动、何时该提问、何时该拒绝、何时该停止，以及在出错后能否正确恢复。现有基准被切分得很碎：有的看任务成功率，有的看工具调用是否有效，有的看多轮一致性，有的看轨迹安全性，还有的看对攻击的鲁棒性，因此单一准确率列越来越不足以比较可部署智能体。AgentAtlas 正是针对这一瓶颈，试图给智能体评测提供一套更统一的行为地图和诊断语言。

#### 方法概述和架构

AgentAtlas 不是单纯提出新榜单，而是一个面向智能体评测的“分类学 + 测量协议”研究。它首先定义了六种控制决策状态：Act、Ask、Refuse、Stop、Confirm、Recover，用来刻画智能体在给出动作前应当采取的控制策略。其次，它采用九类轨迹失败 taxonomy，并进一步引入两个正交层级标签：primary_error_source 和 impact，用于分别描述错误来源与错误后果。第三，它设计了 taxonomy-aware 与 taxonomy-blind 两种提示方式，用来衡量模型表面能力有多少其实来自提示中的显式标签菜单。最后，论文还对 15 个智能体基准做了覆盖审计，映射其在六个行为轴上的覆盖情况，并在一个固定的 8 模型、1,342 条生成样本的合成评测集上演示整套测量流程。

#### 实验结果分析

在固定的八个模型设置下，作者分别在 taxonomy-aware 和 taxonomy-blind 两种提示模式中进行比较，评估控制决策、轨迹诊断和工具上下文保留能力。结果显示，去掉显式标签菜单后，所有模型的轨迹准确率都下降了 14–40 个百分点，并且不分模型家族，最终都收敛到 0.54–0.62 的较低水平，说明不少“能力”实际上依赖提示监督。论文还发现，没有任何单一模型能同时在控制准确率、轨迹诊断和工具上下文效用保持三项上都拿到最优，体现出不同评测轴之间存在明显不一致。文中也对现有 15 个基准做了覆盖审计；可见文本未给出完整的逐项数值，但明确指出当前基准在行为覆盖上仍然存在显著空缺。

<details>
<summary>完整摘要</summary>

大模型智能体如今已经能够作用于代码库、浏览器、操作系统、日历、文件以及各类工具生态，但用于评测它们的基准却高度碎片化：每个基准强调的测量单位各不相同，包括最终任务成功、工具调用有效性、重复多轮一致性、轨迹安全性或对攻击的鲁棒性。2024–2025 年的一系列工作已经逐渐形成共识：对于可部署的智能体而言，单一的准确率列不再是合适的比较单位。AgentAtlas 在这一脉络上扩展出四个组成部分：（i）一个六状态的控制决策分类法（Act / Ask / Refuse / Stop / Confirm / Recover）；（ii）一个九类的轨迹失败分类法，并配有两个正交的层级标签（primary_error_source、impact）；（iii）一种 taxonomy-aware 与 taxonomy-blind 的方法，用于衡量模型表面能力中有多少来自提示中的监督信息；（iv）一项基准覆盖审计，将 15 个智能体基准映射到 6 个行为轴上。为了展示该方法，作者在一个固定的八模型集合上做了小规模实验（1,342 个生成样本，包含四个前沿闭源模型和四个开源权重模型），并分别在两种提示模式下进行评估。去掉显式标签菜单后，所有模型的轨迹准确率都下降了 14–40 个百分点，并且无论模型家族如何，准确率都收敛到 0.54–0.62 的较低下限；同时，没有任何单一模型能在控制准确率、轨迹诊断和工具上下文效用保留这三项上同时取胜。作者将这次合成实验明确视为一次测量协议演示，而不是一个新的基准发布。

</details>

---

### [[20_Research/Papers/大模型/Decomposing_MXFP4_quantization_error_for_LLM_reinforcement_learning_reducible_bias,_recoverable_deadzone,_and_an_irreducible_floor|Decomposing MXFP4 quantization error for LLM reinforcement learning: reducible bias, recoverable deadzone, and an irreducible floor]]

![[assets/2605.20402_figure.png|800]]

- **arXiv**: [2605.20402](https://arxiv.org/abs/2605.20402)
- **PDF**: https://arxiv.org/pdf/2605.20402
- **详细分析**: [[20_Research/Papers/大模型/Decomposing_MXFP4_quantization_error_for_LLM_reinforcement_learning_reducible_bias,_recoverable_deadzone,_and_an_irreducible_floor|Decomposing MXFP4 quantization error for LLM reinforcement learning: reducible bias, recoverable deadzone, and an irreducible floor]]
- **作者**: Xiaocan Li, Shiliang Wu, Zheng Shen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

在大模型强化学习后训练中，rollout 生成与反向传播计算开销都很高，MXFP4 这类 4-bit 浮点格式因其高吞吐、低显存占用而很有吸引力，尤其适合在新的硬件平台上加速 RL 训练。然而，直接用 MXFP4 替代 BF16 往往会带来明显的精度退化，现有工作通常把量化误差当作单一噪声处理，难以解释它究竟通过哪些路径损伤训练。本文之所以值得关注，是因为它把 MXFP4 误差拆成可分析、可对应修复的三个部分，并进一步说明这些误差分别影响梯度、rollout 和探索。

#### 方法概述和架构

论文首先对 MXFP4 的量化误差做了精确三分解：由 E8M0 尺度四舍五入带来的 scale bias、将小值直接置零产生的 deadzone truncation，以及映射到 4-bit 网格时产生的 grid noise。作者证明了该分解是严格成立的，并指出 deadzone 项与另外两项在结构上正交，而 scale bias 与 grid noise 之间存在稳定的负相关，因此总误差并不是简单的独立噪声叠加。基于这一分解，论文进一步把三类误差分别映射到三条 RL 受损路径：scale bias 主要影响反向传播中的梯度精度，deadzone 主要损伤 rollout 质量，grid noise 则提高策略熵、改变探索强度。围绕这三类失败模式，作者设计了三种互补修正：Macro-block Scaling 用更细的尺度处理减轻 scale bias，Outlier Fallback 将 deadzone 中被抹掉的异常值恢复回来，Adaptive Quantization Noise (AQN) 则用于控制策略熵、调节探索；这些模块并非严格一一对应某个误差项，而是按 RL 问题定向修补。

#### 实验结果分析

作者在 Qwen2.5-3B 稠密模型和 Qwen3-30B-A3B-Base MoE 模型上验证了上述方法，并将效果与 BF16 基准进行比较。实验显示，针对性的修正可以把 MXFP4 的 RL 后训练精度恢复到接近 BF16，其中稠密模型的差距收敛到 0.7 个百分点以内，MoE 模型收敛到 3.0 个百分点以内。正文节选还表明，三类误差在不同模型规模下呈现相似结构：grid noise 占总 MSE 的大头且几乎不随模型规模变化，说明它构成一个难以通过单纯调尺度进一步消除的误差下限。

<details>
<summary>完整摘要</summary>

MXFP4 算术可以显著加速大语言模型（LLM）的强化学习（RL）后训练，但量化误差会带来严重的精度下降。已有工作通常把量化误差视为一个整体噪声项，缺少从“量化误差究竟如何损伤训练”这一角度对其机制的区分。我们证明了量化误差的一个精确三向分解，并展示每个分量分别主导一种不同的 RL 训练路径。我们的理论与实验分析将 MXFP4 量化误差分解为三个可加分量：由幂次取整带来的“尺度偏差”（scale bias）、将小值置零带来的“死区截断”（deadzone truncation）、以及将数值四舍五入到 4-bit 网格带来的“网格噪声”（grid noise）。每个分量主导一种不同的 RL 失效模式：尺度偏差会通过反向传播乘性累积，影响梯度精度；死区截断会降低 rollout 质量；网格噪声会提高策略熵。我们组合了针对 RL 失效模式而设计、但并非严格只作用于单一分量的修正方法：用 Macro-block Scaling 降低尺度偏差，用 Outlier Fallback 恢复死区中的条目，同时也会部分降低由尺度偏差引起的误差；再用 Adaptive Quantization Noise (AQN) 控制策略熵。在 Qwen2.5-3B 稠密模型和 Qwen3-30B-A3B-Base 混合专家模型上，这些定向修正分别将性能恢复到接近 BF16，精度差距控制在 0.7% 和 3.0% 以内。

</details>

---

### [[20_Research/Papers/强化学习/ConceptSeg-R1_Segment_Any_Concept_via_Meta-Reinforcement_Learning|ConceptSeg-R1: Segment Any Concept via Meta-Reinforcement Learning]]

![[assets/2605.20385_figure.png|800]]

- **arXiv**: [2605.20385](https://arxiv.org/abs/2605.20385)
- **PDF**: https://arxiv.org/pdf/2605.20385
- **详细分析**: [[20_Research/Papers/强化学习/ConceptSeg-R1_Segment_Any_Concept_via_Meta-Reinforcement_Learning|ConceptSeg-R1: Segment Any Concept via Meta-Reinforcement Learning]]
- **作者**: Yuan Zhao, Youwei Pang, Jiaming Zuo, Wei Ji, Kailai Zhou, Bin Fan, Yunkang Cao, Lihe Zhang, Xiaofeng Liu, Huchuan Lu, Weisi Lin, Dacheng Tao...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

现有可提示分割（promptable segmentation）正在把视觉感知从“找物体”推进到“理解概念”，但“概念”本身并没有被清晰定义，导致很难判断模型究竟是在做类别识别，还是已经具备更广泛的概念理解能力。论文认为，现实中的分割目标不仅包括依赖外观即可识别的类别，还包括依赖上下文关系、以及需要视觉与文本证据共同推理的复杂概念，这使得传统方法在跨任务泛化和推理型场景中显得不足。该工作值得关注之处在于，它首次用一个层次化概念体系系统刻画了概念分割的能力边界，并尝试把“规则归纳”和“像素级分割”统一到同一框架中。

#### 方法概述和架构

论文提出 ConceptSeg-R1，将广义概念分割重写为“规则诱导的概念落地（grounding）”问题。整体流程是：先输入参考图像的拼接块、目标查询图像和文本提示；再由 MLLM 作为推理引擎，从支持样例中归纳任务规则，并在代理查询上验证这些规则；最后把验证后的推理状态通过轻量的 Concept Translation Module（CTM）转成可直接喂给 SAM 3 的概念提示。核心训练机制是 Meta-GRPO，一种面向元学习的强化学习方法，它通过“支持集—代理查询”的分裂参考策略，联合优化代理验证和目标定位，从而鼓励模型学习可迁移的任务规则，而不是记忆单个样本。CTM 采用交叉注意力把 MLLM 的链式推理隐藏状态压缩成多维隐式概念组，再与 SAM 3 的显式文本嵌入拼接，形成分割所需的提示表示。为了保证简单样例上的效率，方法还加入了 Shortcut Router：对于 CI 类简单概念直接走 SAM 3 快捷路径，复杂情况才启用完整推理链路。

#### 实验结果分析

作者在 16 个覆盖 CI、CD、CR 三层概念的基准上评估了 ConceptSeg-R1，任务横跨自然、工业、医疗和推理密集型场景，并与主流可提示分割、推理分割和强化学习分割方法对比。实验结论表明，该方法在完整概念层级上都取得了较强表现，同时保持了 SAM 3 的原生效率特性；在 Cityscapes、ReasonSeg 等常用基准上也表现出较好的泛化能力。节选中未给出具体数值，但文本强调其在无需复杂花哨设计的情况下，能够在分割精度与推理能力之间取得较好平衡。

<details>
<summary>完整摘要</summary>

近期可提示分割的进展，正在把视觉感知从物体级定位推进到概念级理解。然而，“概念”这一术语的含义并不明确，因此目前的方法是否真正超越了类别识别、实现了更广义的泛化，仍不清楚。为此，我们提出一个三层级的广义概念分割定义体系，包括上下文无关（CI）、上下文相关（CD）和上下文推理（CR）概念，这一体系揭示了随着认知复杂度提升而出现的清晰能力鸿沟。为应对这一挑战，我们提出 ConceptSeg-R1，一个统一框架，将概念分割重新表述为规则诱导的概念落地问题。方法的核心是 Meta-GRPO，一种元强化学习机制，它从视觉示例中学习可迁移的任务规则，并通过代理推理对其进行验证。随后，将推断得到的推理状态通过一个轻量级概念翻译模块转化为可直接用于分割的概念提示，从而能够以演绎方式应用到目标图像上。一个快捷路由策略则进一步在简单案例中保留了分割模型的原生效率。为了系统评估广义概念分割，我们在涵盖自然、工业、医疗以及推理密集型领域的多种 CI、CD 和 CR 概念分割基准上进行了大量实验。ConceptSeg-R1 在不依赖额外花哨设计的情况下，在整个概念层级上都取得了较强性能，同时保持了可提示分割骨干网络的原生能力。作为“分割任意概念”的初步尝试，我们希望 ConceptSeg-R1 能成为推动分割从物体级预测迈向概念级理解的实用基线。

</details>

---

### [[20_Research/Papers/强化学习/SUGAR_A_Scalable_Human-Video-Driven_Generalizable_Humanoid_Loco-Manipulation_Learning_Framework|SUGAR: A Scalable Human-Video-Driven Generalizable Humanoid Loco-Manipulation Learning Framework]]

![[assets/2605.20373_figure.png|800]]

- **arXiv**: [2605.20373](https://arxiv.org/abs/2605.20373)
- **PDF**: https://arxiv.org/pdf/2605.20373
- **详细分析**: [[20_Research/Papers/强化学习/SUGAR_A_Scalable_Human-Video-Driven_Generalizable_Humanoid_Loco-Manipulation_Learning_Framework|SUGAR: A Scalable Human-Video-Driven Generalizable Humanoid Loco-Manipulation Learning Framework]]
- **作者**: Tianshu Wu, Xiangqi Kong, Yue Chen, Qize Yu, Hang Ye, Jia Li, Yizhou Wang, Hao Dong
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

人形机器人要在真实世界完成全身移动与操作一体化任务（loco-manipulation），例如搬运、推拉、拾取和接触式交互，但现有方法要么依赖大量任务特定奖励设计，要么只是机械复现参考动作，泛化能力有限，要么依赖昂贵的遥操作，难以规模化。相比之下，人类视频包含丰富多样的行为模式，但从视频中直接提取的运动先验会受到遮挡、接触误差和动作重定向偏差影响，无法直接用于策略学习。本文值得关注之处在于，它试图把“海量但不完美”的人类视频，转化为可直接部署到真实人形机器人的通用全身操作技能。

#### 方法概述和架构

论文提出 SUGAR，一个从人类视频学习通用人形机器人全身移动-操作技能的三阶段框架。第一阶段是全自动的 kinematic interaction priors 提取：从无标注视频中重建人体运动、6D 物体轨迹，并通过 VLM 或启发式规则生成接触标签，形成包含轨迹与接触信息的数据集。第二阶段是基于特权信息的物理修正器 refiner：利用统一的 mimic 风格奖励和 progressive state pool，把带噪的运动先验转化为物理可行、质量更高的专家示范，同时保留原始任务意图。第三阶段是分层策略蒸馏：将修正后的示范训练成一个由高层 command generator 和低层 command tracker 组成的自主策略，高层负责生成动作意图，低层负责稳定跟踪与闭环执行。整体上，训练流程是“视频提取先验 → 物理仿真中精炼 → 分层策略学习”，推理时不再依赖参考动作条件输入，而是直接依据机器人本体状态、物体状态和任务目标输出控制动作。

#### 实验结果分析

论文在 6 个代表性任务上评估了方法，包括推箱、抓瓶、搬箱、坐椅子、踢箱以及带外部扰动的抓瓶任务，覆盖仿真与真实人形硬件。与 reference-tracking 基线相比，SUGAR 表现明显更好，并且随着人类视频数据量增加，性能呈现清晰的规模效应。作者还报告了零样本真实世界迁移，能够实现可靠闭环执行、自动失败恢复以及在外部扰动下的稳定长时程表现；不过节选文本未给出具体数值。

<details>
<summary>完整摘要</summary>

让人形机器人具备可泛化的全身移动-操作能力，并能在真实世界中稳定执行，仍然是一个基础性难题。现有方法要么依赖繁重的任务特定奖励工程，要么机械地回放参考动作、无法泛化，要么依赖昂贵的遥操作，因而难以规模化。虽然人类视频能够捕捉多样化的人类行为，但从中推断出的运动先验天然不完美，常常受到遮挡、接触伪影和重定向误差的影响，因此不适合直接用于策略学习。为此，我们提出 SUGAR，一个数据驱动框架，能够把多样的人类视频转化为可部署的人形机器人移动-操作技能，而在推理时既不需要任务特定的奖励工程，也不需要参考动作条件输入。SUGAR 分三步进行：第一，利用一个全自动流水线，从非结构化的人类视频中提取运动学交互先验，包括人与物体的运动轨迹和接触标签；第二，使用一个带特权信息的物理修正器，结合统一的 mimic 风格奖励与 progressive state pool，把不完美的先验转化为物理可行、保真度更高的技能；第三，将修正后的技能蒸馏为一个分层自主策略，由命令生成器和命令跟踪器构成。我们在仿真和真实人形硬件上对六个具有代表性的移动-操作任务进行了评估。结果表明，我们的方法显著优于 reference-tracking 基线，且性能会随着人类视频数据量增加而明显提升。它还实现了零样本真实世界迁移，具备可靠的闭环执行、自动失败恢复，以及在外部扰动下稳定的长时程表现。项目主页：https://tianshuwu.github.io/sugar-humanoid/

</details>

---

### [[20_Research/Papers/大模型/Security_Document_Classification_with_a_Fine-Tuned_Local_Large_Language_Model_Benchmark_Data_and_an_Open-Source_System|Security Document Classification with a Fine-Tuned Local Large Language Model: Benchmark Data and an Open-Source System]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2605.20368](https://arxiv.org/abs/2605.20368)
- **PDF**: https://arxiv.org/pdf/2605.20368
- **详细分析**: [[20_Research/Papers/大模型/Security_Document_Classification_with_a_Fine-Tuned_Local_Large_Language_Model_Benchmark_Data_and_an_Open-Source_System|Security Document Classification with a Fine-Tuned Local Large Language Model: Benchmark Data and an Open-Source System]]
- **作者**: Ivan Dobrovolskyi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Security, Systems

#### 研究背景与动机

许多组织需要对文档进行安全扫描，以识别其中是否包含敏感信息、泄密线索或合规风险。但实际使用中，云端服务会把文档内容上传到外部基础设施，带来隐私与数据治理顾虑；而基于规则的工具又常常难以识别依赖上下文的威胁。本文关注的是“安全文档分类”这一具体任务，即判断文档属于哪类安全风险及其细分子类，因此具有较强的现实落地价值。

#### 方法概述和架构

作者提出了开源本地系统 TorchSight，用于在本地环境完成安全文档分类，核心模型是经过微调的 Qwen 3.5 27B。训练数据来自 13 个允许宽松使用许可的数据源，并结合 GPT-4 生成的合成数据，共计 78,358 个样本，覆盖 7 个安全类别和 51 个子类别。模型的输入是待分类文档，输出是文档对应的安全类别判断；训练完成后可直接在本地推理，无需将文档发送到云端。整体流程是先构建多来源标注/合成训练集，再对基础模型进行领域微调，最后用于安全文档分类推断。

#### 实验结果分析

在主要评测中，模型在 1,000 篇文档上取得了 95.0% 的类别级准确率，95% 置信区间为 93.5-96.2。相比之下，在相同提示词协议下测试的商业模型得分为 75.4-79.9%，说明该本地微调模型具有明显优势。作者还在一个独立的外部测试集上评估了 500 个保留样本，准确率达到 93.8%，表明其效果不仅限于主基准集，但泛化幅度仍会受到数据组成和难例边界情况影响。整体结论是：经过微调的本地大模型可以在保持文档本地处理的同时，实现较高精度的安全文档分类。

<details>
<summary>完整摘要</summary>

组织在扫描文档中的敏感信息时，会遇到一个实际问题：云服务要求将数据发送到外部基础设施，而基于规则的工具往往会漏掉那些依赖上下文才能识别的威胁。本文提出 TorchSight，这是一个面向安全文档分类的开源本地系统，基于经过微调的 Qwen 3.5 27B 模型构建。该模型使用来自 13 个宽松许可来源的 78,358 个样本以及 GPT-4 合成数据进行训练，覆盖 7 个安全类别和 51 个子类别。在 1,000 篇文档的主要评估中，模型达到了 95.0% 的类别级准确率（95% 置信区间：93.5-96.2）。在相同提示词协议下测试的商业模型得分为 75.4-79.9%。在另一个独立的外部测试集上，模型在 500 个保留样本上达到了 93.8% 的准确率，这表明其性能能够扩展到主基准之外，不过具体提升幅度会受到数据集组成和困难边界样本的影响。结果表明，一个经过微调的本地模型可以在保持文档处理完全受本地控制的同时，为安全文档分类提供准确支持。

</details>

---

### [[20_Research/Papers/具身智能/Mechanisms_of_Misgeneralization_in_Physical_Sequence_Modeling|Mechanisms of Misgeneralization in Physical Sequence Modeling]]

![[assets/2605.20299_figure.png|800]]

- **arXiv**: [2605.20299](https://arxiv.org/abs/2605.20299)
- **PDF**: https://arxiv.org/pdf/2605.20299
- **详细分析**: [[20_Research/Papers/具身智能/Mechanisms_of_Misgeneralization_in_Physical_Sequence_Modeling|Mechanisms of Misgeneralization in Physical Sequence Modeling]]
- **作者**: Kento Nishi, Raphael Tang, Karun Kumar, Core Francisco Park, Hidenori Tanaka
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

这篇论文关注具身智能和机器人中的生成式序列建模：模型在训练时学习的是轨迹本身，但工程上往往希望它同时遵守某个物理量的分布约束，例如行走距离、机械能或能耗范围。作者指出，现有深度学习模型即使生成的单条轨迹看起来都合理，也可能在整体上偏离训练数据所希望表达的物理分布，这会直接影响机器人规划、仿真和运动预测中的安全性与可控性。该问题在 Maze2D 导航、双摆动力学等任务中都可能出现，因此值得作为物理生成模型的一个新的失配机制来研究。

#### 方法概述和架构

论文将这种现象定义为“physical misgeneralization（物理误泛化）”，并把问题拆解为“轨迹生成”和“物理量恢复”两个环节：先从联合分布中生成轨迹，再用测量函数从轨迹中恢复出标量物理量。为解释偏移来源，作者提出 data deviation kernel（数据偏差核），用来刻画模型类典型的局部生成误差如何在物理测量过程中被放大，并最终把概率质量从某些物理量区间转移到另一些区间。实验上，论文先构造具有已知物理量、先验分布和轨迹生成规则的受控合成任务，以便隔离机制；再将同样的分析应用到 Maze2D 导航和双摆模拟等更接近实际的任务中。整体流程是：用轨迹数据训练无条件生成模型，随后通过物理测量恢复量值分布，并用数据偏差核预测哪些量值会增减。最后，作者基于这一机制讨论并验证了几类缓解策略，包括调整数据集构成、改变生成接口以及变换数据表示。

#### 实验结果分析

在受控合成任务中，作者发现数据偏差核能够较准确地预测训练后模型在物理量分布上的漂移方向，说明误泛化并非随机噪声，而是可由模型局部误差传播机制解释。进一步在 Maze2D 和双摆任务中，这一机制同样能够预测哪些物理量会被过度或不足表示，并能解释 Maze2D 中路径长度整体上移的现象。论文还比较了数据层、接口层和表示层的多种干预方式，结果表明基于核的思路可以帮助判断哪些缓解策略更有结构性潜力。节选文本未给出具体数值。

<details>
<summary>完整摘要</summary>

生成式序列模型常被用于物理领域中的运动规划，例如机器人和机械仿真。在为这类模型构建训练数据集时，工程师可能会精心筛选示范轨迹，以规定某个物理量的分布方式，比如行进距离或机械能。例如，构建迷宫导航智能体的机器人研究者，可能会选择行进距离在固定范围内均匀分布的示范轨迹，希望借此约束智能体的预期能耗。我们发现，标准深度学习会违背这一意图：每条生成轨迹单独看起来都合理，但在物理量上的整体分布却是错误的。我们将这种失效称为物理误泛化，并分析其机制。通过受控的合成任务，我们表明：当模型类别中典型的局部误差沿着物理测量过程传播时，就会导致恢复出的分布发生偏移，从而产生物理误泛化。我们使用数据偏差核来估计这些误差，并用它预测在合成任务以及更接近实际的迷宫导航和双摆运动任务中，哪些物理量会增加或减少概率质量。最后，我们的机制解释还帮助识别出哪些缓解策略在结构上更有希望，并据此提出了一种基于核信息的干预方法。

</details>

---

### [[20_Research/Papers/大模型/Introspective_X_Training_Feedback_Conditioning_Improves_Scaling_Across_all_LLM_Training_Stages|Introspective X Training: Feedback Conditioning Improves Scaling Across all LLM Training Stages]]

![[assets/2605.20285_figure.png|800]]

- **arXiv**: [2605.20285](https://arxiv.org/abs/2605.20285)
- **PDF**: https://arxiv.org/pdf/2605.20285
- **详细分析**: [[20_Research/Papers/大模型/Introspective_X_Training_Feedback_Conditioning_Improves_Scaling_Across_all_LLM_Training_Stages|Introspective X Training: Feedback Conditioning Improves Scaling Across all LLM Training Stages]]
- **作者**: Brandon Cui, Ximing Lu, Jaehun Jung, Syeda Nahida Akter, Hyunwoo Kim, Yuxiao Qu, David Acuna, Shrimai Prabhumoye, Yejin Choi, Prithviraj Ammanabrolu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.4，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

当前大模型训练流程已经从传统的“预训练—后训练”扩展为包含预训练、继续预训练、中期训练、监督微调等多个阶段，但各阶段往往各自为政，早期训练很少直接利用后期阶段才会出现的质量判断、偏好信息和任务反馈。作者指出，这种单向流水线使得训练中“并非所有 token 都同等重要”这一事实没有在更早阶段被充分利用，导致算力投入与最终能力之间的效率不够理想。本文关注如何把后训练阶段的质量信号前移，用更早的反馈建模来改善 LLM 的整体缩放效率，因此对强化学习、大模型训练流程优化以及世界模型式的反馈驱动学习都具有启发意义。

#### 方法概述和架构

论文提出 Introspective Training（IXT），核心思想是先用一个“思考型”奖励/评审模型对训练文档进行离线标注，再把标注结果作为前缀条件附加到原始文本前面进行标准 next-token prediction 训练。标注信息包含两类：一类是将整体质量量化为五档的模板化质量标签，另一类是更丰富的自然语言批注，说明文档为何高或低质量，并可按写作风格、专业性、教育价值、事实密度/准确性、效率五个维度打分。训练时，模型输入不是单纯的原文，而是“反馈前缀 + 原文”拼接后的序列；在预训练阶段前缀也参与损失，从而让模型更早学习“质量条件化”的生成分布，而在 SFT 中则把前缀放入 system message 里并对其做掩码。推理时，模板化模型直接选择五档质量前缀，自然语言批注模型则可以根据目标领域与输出特征构造新的反馈提示，用于引导生成。

#### 实验结果分析

作者在从头训练的 7.5B–12B dense Transformer 大模型上，以及累计看过 95B、12T、18T token 的不同训练阶段上进行了系统实验，并同时考察了数学与代码等领域专门化效果。结果显示，IXT 能显著弯折 scaling curve，在考虑离线标注额外开销后，整体最高可带来 2.8x 的算力效率提升。文中还报告，在早期训练时就引入 IXT 可在 HumanEval 和 MATH 上带来明显增益，并且这些收益会延续到后续更大规模训练阶段；同时，自然语言批注普遍优于其他反馈形式，模板化质量 token 也优于完全不加条件的基线。

<details>
<summary>完整摘要</summary>

我们试图解决一个问题：如何在当前不断增长、阶段越来越多的大模型训练流水线中，以更高效率完成规模扩展。我们的核心直觉来自这样一个事实：流水线后期阶段（例如后训练）的动态信息，可以反过来帮助前期阶段（例如预训练）。为此，我们提出 Introspective Training（简称 IXT），其灵感来自离线的奖励条件强化学习，并且可应用于训练流程的任何阶段。IXT 使用一个“思考型”奖励模型，利用自然语言批注式反馈对数据进行标注，从而使从最早阶段开始的训练都能够感知数据质量。随后，模型通过将这些生成的反馈作为前缀来训练，也就是在更早的训练阶段就让不同 token 不再被同等对待。我们在 7.5B 到 12B 的基于 Transformer 的稠密 LLM 上开展了全面实验，模型从头训练直到累计看到 18 万亿个 token。实验表明，我们的方法能够弯折缩放曲线，在总体上带来最高 2.8 倍的算力效率提升；并且在数学和代码等领域，能够达到其他训练方式难以实现的性能水平。

</details>

---

### [[20_Research/Papers/大模型/JUDO_A_Juxtaposed_Domain-Oriented_Multimodal_Reasoner_for_Industrial_Anomaly_QA|JUDO: A Juxtaposed Domain-Oriented Multimodal Reasoner for Industrial Anomaly QA]]

![[assets/2605.20284_figure.png|800]]

- **arXiv**: [2605.20284](https://arxiv.org/abs/2605.20284)
- **PDF**: https://arxiv.org/pdf/2605.20284
- **详细分析**: [[20_Research/Papers/大模型/JUDO_A_Juxtaposed_Domain-Oriented_Multimodal_Reasoner_for_Industrial_Anomaly_QA|JUDO: A Juxtaposed Domain-Oriented Multimodal Reasoner for Industrial Anomaly QA]]
- **作者**: Hyunju Kang, Woohyun Lee, Jaewon Kim, Hogun Park
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

工业异常检测正从“找出缺陷”走向“解释缺陷”：在产线质检、故障排查等场景中，模型不仅要判断是否异常，还要回答缺陷类型、位置、成因和影响等问题。近年来，大模型/多模态大模型（LMM）显著提升了这类视觉问答能力，但在复杂工业场景中仍受限于领域知识不足，容易给出看似合理却不够准确的解释。尤其是工业缺陷往往具有强领域属性，单靠通用预训练知识很难稳定覆盖，因此如何把“正常样本的视觉上下文”和“工业领域知识”真正内化进模型，值得重点关注。

#### 方法概述和架构

论文提出 JUDO（Juxtaposed Domain-Oriented Multimodal Reasoner），用三阶段训练把视觉比较推理与文本领域知识统一起来。第一阶段通过“并置式”比较学习，将异常图像与同类别正常图像配对输入，让模型在16×16网格上输出缺陷区域坐标，并同步生成基于对比证据的解释，从而学会细粒度定位异常。第二阶段用由 MMAD 原始领域文本整理出的问答数据进行监督微调，把工业对象、缺陷类型、成因与表现等领域知识注入模型参数，而不是只在推理时临时提供提示词。第三阶段采用 GRPO 做强化学习对齐，并设计面向领域推理的奖励，包括域知识推理、分割正确性、选择准确率和结构一致性等，促使模型输出同时具备定位能力、领域一致性和可解释性。整体上，JUDO 的输入是异常查询图像与正常参照图像及领域文本知识，输出则是带有缺陷区域定位和文字分析的工业异常问答结果。

#### 实验结果分析

论文在 MMAD 基准上验证了 JUDO 的效果，并与 Qwen2.5-VL-7B、GPT-4o 等模型比较，结果表明其整体表现更优。作者还通过消融实验和多阶段学习分析说明：仅有视觉对比或仅有领域知识都不如将二者结合，再用 GRPO 做统一对齐。节选文本中未给出具体数值，但结论明确指向：领域知识内化与正常样本上下文的联合建模，是提升工业异常理解性能的关键。

<details>
<summary>完整摘要</summary>

工业异常检测在大型多模态模型（LMM）推动下取得了显著进展，这些模型使得除检测之外的多样化人类指令成为可能，尤其是通过视觉落地的推理来提升图像理解能力。然而，LMM 缺乏领域特定知识，这限制了它们在复杂工业场景中生成准确回答的能力。为此，我们提出 JUDO（Juxtaposed Domain-Oriented Multimodal Reasoner），一种能够高效融合领域知识与上下文、用于视觉与文本推理的框架。通过视觉推理，我们的模型将查询图像与正常图像并置为视觉领域上下文，从而分割缺陷区域，实现细粒度的视觉对比检查。此外，我们通过监督微调（SFT）注入领域知识，以增强上下文理解能力，并随后利用带有定制奖励的强化学习（GRPO）引导领域推理，选择一种面向领域的推理过程。实验结果表明，JUDO 在 MMAD 基准上取得了更优表现，超过了 Qwen2.5-VL-7B 和 GPT-4o 等模型。这些结果凸显了增强领域知识与上下文对于异常理解中的有效推理至关重要。

</details>

---

### [[20_Research/Papers/大模型/ClaimDiff-RL_Fine-Grained_Caption_Reinforcement_Learning_through_Visual_Claim_Comparison|ClaimDiff-RL: Fine-Grained Caption Reinforcement Learning through Visual Claim Comparison]]

![[assets/2605.20278_figure.png|800]]

- **arXiv**: [2605.20278](https://arxiv.org/abs/2605.20278)
- **PDF**: https://arxiv.org/pdf/2605.20278
- **详细分析**: [[20_Research/Papers/大模型/ClaimDiff-RL_Fine-Grained_Caption_Reinforcement_Learning_through_Visual_Claim_Comparison|ClaimDiff-RL: Fine-Grained Caption Reinforcement Learning through Visual Claim Comparison]]
- **作者**: Tianle Li, Xuyang Shen, Yan Ma, Rongxin Guo, Shaoxiang Chen, Jiacheng Chen, Haochen Wang, Hongyang Tang, Yucong Zhou, Yu Cheng
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.02（加权：大模型 0.1，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

长篇图像描述任务中，模型需要同时做到“信息充分”和“事实可信”，但强化学习往往把整段 caption 只压缩成一个序列级奖励，难以定位具体是哪条视觉事实出了错。这样一来，幻觉、遗漏关键信息、以及安全但过于保守的表述会被混在同一个分数里，导致模型可能通过少说来降低幻觉，却牺牲覆盖度。该论文聚焦于奖励粒度不匹配这一问题，尤其适合需要细粒度视觉理解、可诊断优化的多模态生成场景，因此很值得关注。

#### 方法概述和架构

论文提出 ClaimDiff-RL，将长篇 caption 的奖励单位从“整句评分”改为“基于参考 caption 的原子视觉 claim 差异”。给定图像、演员生成的 caption 和参考 caption，模型先由多模态评审器找出两段文本之间的视觉差异，再逐条回到图像中验证这些差异是否成立，并为每一侧标注开放词表的错误类型与严重程度。随后，方法把这些逐差异统计量组合成标量奖励，提供两种形式：一种是相对奖励，比较演员侧与参考侧在错误数量和严重度上的差异；另一种是仅惩罚演员侧错误的 actor-only 奖励。训练时仍沿用标准的 RL 优化方式，但奖励来源从整体打分变成了“差异发现—图像验证—类型化计数—标量合成”的流水线，从而显式暴露事实性与覆盖度之间的权衡。

#### 实验结果分析

作者在 160 张人工标注的诊断集、公开 caption 基准以及 VQA 基准上评估了该方法；对比对象包括整体标量奖励、无参考/有参考的直接评审方案，以及若干细粒度 caption 训练方法。结果显示，ClaimDiff-RL 能更平衡地处理“幻觉—遗漏事实”权衡，并保持甚至提升通用能力；在若干细粒度能力维度上，例如目标计数、空间关系和场景识别，甚至超过了 Gemini-3-Pro-Preview。消融分析还表明，严重度加权可以控制“可信度—覆盖度”的折中；同时，作者指出整体标量奖励虽然能降低幻觉，但往往是通过增加遗漏事实实现的，而 ClaimDiff-RL 能把这种代价显式化并提供更可控的优化方向。

<details>
<summary>完整摘要</summary>

长篇图像描述会在强化学习中暴露一个奖励粒度问题：caption 是按整段序列来评判的，但真正重要的错误却发生在单个视觉事实（visual claim）的层面。一个好的密集 caption 应当既可信又信息充分，在避免幻觉的同时不遗漏显著细节。然而，成对偏好、基于参考的指标以及整体标量奖励都会把这些局部错误压缩成一个序列级信号，从而掩盖事实性与覆盖度之间的权衡。我们提出 ClaimDiff-RL，这是一个将“基于参考 caption 的原子视觉事实差异”作为 caption 强化学习奖励单位的框架。给定一张图像、一个演员生成的 caption 和一个参考 caption，一个多模态评审器会枚举有视觉依据的差异，基于图像验证每个差异，为其分配开放词表的错误类型和严重程度，并生成用于奖励构造的逐差异统计量。这样，幻觉事实和遗漏的重要事实就能被分别度量和调节。实验表明，整体标量奖励虽然能通过增加遗漏事实来降低幻觉，但 ClaimDiff-RL 能显式揭示这种“可信度—覆盖度”权衡，并实现更均衡的工作点。在一个包含 160 张图像且带人工标注的诊断基准、公开 caption 基准和 VQA 基准上，ClaimDiff-RL 改善了幻觉与遗漏事实之间的平衡，保持了通用能力，甚至在若干细粒度能力维度上，如目标计数、空间关系和场景识别，超过了 Gemini-3-Pro-Preview。这些结果说明，带类型、可验证的视觉事实差异，是一种适用于细粒度且可诊断 caption 强化学习的有效奖励单位。

</details>

---

### [[20_Research/Papers/强化学习/Smaller_Abstract_State_Spaces_Enable_Cross-Scale_Generalization_in_Reinforcement_Learning|Smaller Abstract State Spaces Enable Cross-Scale Generalization in Reinforcement Learning]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2605.20272](https://arxiv.org/abs/2605.20272)
- **PDF**: https://arxiv.org/pdf/2605.20272
- **详细分析**: [[20_Research/Papers/强化学习/Smaller_Abstract_State_Spaces_Enable_Cross-Scale_Generalization_in_Reinforcement_Learning|Smaller Abstract State Spaces Enable Cross-Scale Generalization in Reinforcement Learning]]
- **作者**: Nasehatul Mustakim, Lucas Lehnert
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

人类能够把“抽象概念”迁移到更复杂、规模更大的任务中，但让强化学习（RL）智能体也具备这种跨尺度泛化能力，一直是一个难题。尤其在部分可观测环境中，智能体不仅要从有限观测中做决策，还要学会哪些经验可以视为等价、哪些必须区分，这使得分布外（OOD）泛化更加困难。本文聚焦于“从小任务泛化到更复杂任务”的核心机制，试图从理论上解释为什么更小的抽象状态空间可能更有利于泛化，因此具有较强的基础研究价值。

#### 方法概述和架构

论文以 Partially Observable Markov Decision Processes（POMDPs）为建模对象，研究智能体如何通过抽象函数把原始状态压缩为抽象状态。作者首先将既有的状态抽象框架及证明技术推广到 POMDP 场景，使其能够分析部分可观测条件下的泛化问题。随后提出一种 successor-weighted model reduction（后继加权模型约简）方法，通过对状态转移中的后继信息加权，实现比传统定义更小的抽象空间压缩。该方法的输入可以理解为原始环境中的经验与转移结构，输出则是一个更紧凑的抽象状态模型，供智能体在训练与推理时使用。最后，作者基于该抽象模型推导 OOD 测试性能上界，并将性能损失分解为近似误差和估计误差两部分，从而刻画抽象空间大小与泛化能力之间的关系。

#### 实验结果分析

论文给出了一个关于 RL 智能体 OOD 测试表现的理论上界，说明在何种条件下跨尺度泛化是可实现的。分析表明，性能损失可以分解为近似误差与估计误差，而缩小抽象状态空间能够降低测试误差、提升 OOD 泛化能力。作者进一步指出，将智能体限制在一个小而有限的抽象状态集合上，可能是实现更复杂任务泛化的必要条件。由于正文节选中未给出具体实验设置、数据集或数值结果，可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

虽然人类能够轻松地将抽象概念泛化到更复杂或更大规模的任务中，但在强化学习（RL）系统中实现这种能力仍然十分困难。本文提出了首个关于 RL 智能体如何实现这种分布外（OOD）泛化的理论模型。我们的方法考虑部分可观测马尔可夫决策过程（POMDPs），并假设智能体会使用一个抽象函数来判断哪些经验可以视为等价，哪些必须加以区分。首先，我们将现有的状态抽象框架及证明技术扩展到 POMDPs。随后，我们定义了一种后继加权的模型约简方法，这是一类模型约简变体，它能够压缩到比以往定义允许的更小抽象空间中。我们推导了智能体 OOD 测试性能的一个上界，从而定义了在何种条件下 OOD 泛化是可实现的。该上界将智能体的性能损失分解为近似误差和估计误差，揭示了缩小智能体抽象状态空间大小如何提升测试性能和 OOD 泛化能力。我们的分析表明，限制智能体在一个小而有限的抽象状态集合上运行，对于实现向更复杂任务的泛化是必要的。我们的结果也激励进一步研究能够跨越不同复杂度任务进行扩展的 RL 架构学习方法。

</details>

---

### [[20_Research/Papers/大模型/Chronicle_A_Multimodal_Foundation_Model_for_Joint_Language_and_Time_Series_Understanding|Chronicle: A Multimodal Foundation Model for Joint Language and Time Series Understanding]]

![[assets/2605.20268_figure.png|800]]

- **arXiv**: [2605.20268](https://arxiv.org/abs/2605.20268)
- **PDF**: https://arxiv.org/pdf/2605.20268
- **详细分析**: [[20_Research/Papers/大模型/Chronicle_A_Multimodal_Foundation_Model_for_Joint_Language_and_Time_Series_Understanding|Chronicle: A Multimodal Foundation Model for Joint Language and Time Series Understanding]]
- **作者**: Paul Quinlan, Jeremy Levasseur, Qingguo Li, Xiaodan Zhu
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

真实世界中的时间序列往往伴随文本信息，例如元数据、业务描述、新闻报道和异常说明，但现有时间序列基础模型通常只处理数值序列，无法利用这些上下文。另一方面，已有的文本-时间序列多模态方法大多是在预训练语言模型上后接适配器或微调模块，文本表征在训练前从未见过时间数据，时间序列也被迫适应一个并非为其设计的表示空间。作者指出，现有工作还几乎只和多模态基线比较，缺少与各自领域最强的单模态基础模型对照，因此“是否真的需要联合训练”这一问题仍未被充分回答。这篇论文值得关注之处在于，它尝试用一个小规模、从头训练的统一模型同时学习语言与时间序列表示，并在两个领域都做了严格的对照评测。

#### 方法概述和架构

论文提出 Chronicle，一个 324M 参数的 decoder-only Transformer，从随机初始化开始在自然语言和时间序列上联合预训练。模型主体只有一套共享的 Transformer blocks、注意力机制和残差流，模态特定部分仅保留输入/输出接口：文本侧使用 131072 词表的 BPE embedding，时间序列侧先做标准化与 asinh 变换，再切成长度为 32 的 patch，并将位置、数值、有效性掩码和通道信息拼接成 patch 特征后投影到共享隐空间。训练分两阶段：第一阶段大部分是单模态 batch，让文本和时间序列通过共享参数共同塑造骨干；第二阶段引入少量交错的文本+时间序列序列，在更长上下文下做跨模态对齐。推理时，文本 token 和时间序列 patch 可以自由交错输入同一序列，跨模态信息通过因果自注意力自然流动，无需额外架构改动。输出端同时支持语言建模和分位数预测，并且可直接抽取冻结 embedding 用于下游分类。

#### 实验结果分析

作者在 19 个 NLU 任务上将 Chronicle 与 GPT-2 到 LLaMA-3.2-1B 以及 Gemma-3-270M-PT 等小型语言模型比较，结果显示其语言理解能力可与 Gemma-3-270M-PT 持平。时间序列方面，模型在 24 个 UCR/UEA 数据集上的冻结 embedding 分类刷新了新的基准，并在 GIFT-Eval 上与专门的时间序列基础模型进行对照。多模态任务上，Chronicle 在 Time-MMD 上的预测超过所有监督式融合基线。文中未给出具体数值的部分，节选中可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

现实世界中的时间序列通常伴随文本信息：元数据、描述、新闻、报告。然而，时间序列基础模型往往将数值序列孤立地处理；而那些试图连接文本与时间序列的多模态模型，几乎都只是事后适配一个预训练语言模型，因此继承了从未接触过时间数据的表示方式。这些模型的评测也几乎只与其他多模态基线比较，而不是与任一领域中最强的单模态基础模型比较，因此“联合训练是否真的必要”这一问题仍未被回答。我们提出 Chronicle，一个紧凑的 324M 参数 decoder-only Transformer，在一个统一架构内从头同时用自然语言和时间序列进行训练。两种模态共享相同的 Transformer blocks、注意力机制和残差流；预训练的大部分阶段使用单模态 batch，因此跨模态能力完全通过共享参数自发形成，之后再通过一个简短的对齐阶段交错训练两种模态。据我们所知，Chronicle 是第一个从零开始对文本和时间序列进行联合预训练的模型，也是第一个同时在两个领域都与专门基础模型比较的多模态模型。它在 19 个 NLU 任务上与 Gemma-3-270M-PT 持平，在 24 个 UCR/UEA 数据集上的冻结 embedding 时间序列分类中建立了新的标杆，并在 Time-MMD 上生成的多模态预测优于所有监督式融合基线，且这一切都来自同一个骨干模型。

</details>

---

### [[20_Research/Papers/强化学习/FBOS-RL_Feedback-Driven_Bi-Objective_Synergistic_Reinforcement_Learning|FBOS-RL: Feedback-Driven Bi-Objective Synergistic Reinforcement Learning]]

![[assets/2605.20256_figure.png|800]]

- **arXiv**: [2605.20256](https://arxiv.org/abs/2605.20256)
- **PDF**: https://arxiv.org/pdf/2605.20256
- **详细分析**: [[20_Research/Papers/强化学习/FBOS-RL_Feedback-Driven_Bi-Objective_Synergistic_Reinforcement_Learning|FBOS-RL: Feedback-Driven Bi-Objective Synergistic Reinforcement Learning]]
- **作者**: Xikai Zhang, Yongzhi Li, Likang Xiao, Yingze Zhang, Yanhua Cheng, Quan Chen, Peng Jiang, Wenjun Wu, Liu Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

强化学习已成为对齐大模型并释放其推理能力的重要手段，尤其是在 GRPO 及其变体的训练循环中，rollout 采样与策略更新交替进行，采样质量直接决定后续梯度方向是否有效。现有主流方法往往只基于同一个原始提示词进行盲采样，当任务难度超出当前策略能力时，很难采到高质量 rollout，进而导致训练缺乏有意义的优化锚点、学习停滞。本文关注的正是这一“采样盲区”问题，尝试把环境反馈真正闭环到采样与优化之中，因此具有较强的实践价值。

#### 方法概述和架构

作者提出 FBOS-RL（Feedback-Driven Bi-Objective Synergistic Reinforcement Learning）框架，核心思路是先用环境反馈增强探索，再用两个相互促进的目标联合训练策略。具体流程分为三步：首先，策略模型仅基于原始提示词进行初始探索，生成一批 rollout，并由规则验证器输出标量奖励和自然语言反馈，反馈会指出错误位置、错误原因或格式违规等问题。其次，将“原始提示词 + 初始 rollout + 反馈”拼接成反馈增强提示（FAP），再进行第二轮采样，以得到更高质量的反馈引导 rollout。最后，在优化阶段交替训练两个目标：EPA（Exploitation-oriented Policy Alignment）利用收集到的高质量 rollout 做策略对齐，ECC（Exploration-oriented Capability Cultivation）则专门培养模型在反馈提示下继续采出更好结果的能力，从而形成正向自举飞轮。

#### 实验结果分析

实验部分在不同数据集、不同模型家族与不同规模上验证了 FBOS-RL 的有效性，基线包括 GRPO 及若干反馈驱动方法。结果表明，在相同 rollout 预算下，FBOS-RL 的学习速度明显快于 GRPO 和反馈基线，并能达到更高的性能上限，同时训练过程中表现为更高的策略熵和更低的梯度范数，说明其探索能力更强、训练更稳定。正文还给出消融分析，验证 EPA 与 ECC 之间存在相互促进关系；在控制参数更新次数的实验中，方法仍保持优势。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

强化学习已经成为对齐并释放大规模模型推理能力的基石。在其核心训练循环中，GRPO 及其变体在 rollout 采样与策略更新之间交替进行：策略先从动作空间中采样 rollout，再根据这些 rollout 上计算得到的优势来更新参数。与监督学习不同，在这种设置下，每一步梯度更新并没有一个显式的真实标签作为锚点；因此，在采样阶段获得的高质量 rollout 实际上充当了隐式“教师”，引导每一次参数更新。然而，GRPO 采用的是一种简单的采样方案，即让所有 rollout 都以同一个原始提示词为条件。当任务超出当前策略模型能力时，这种采样方式往往很难产生高质量 rollout，导致策略模型在更新参数时缺乏有意义的梯度方向，训练因此会陷入停滞。为解决这一问题，我们提出 FBOS-RL，一种反馈驱动的双目标协同强化学习框架。具体而言，我们让模型基于环境提供的反馈进行反馈引导探索增强，并在此基础上设计两个相互促进的训练目标：面向利用的策略对齐（EPA）和面向探索的能力培养（ECC）。大量实验表明，EPA 与 ECC 能够相互强化，形成正向飞轮效应，显著提升强化学习的训练效率与最终性能上限。具体来说，在相同的 rollout 预算下，FBOS-RL 比 GRPO 和基于反馈的基线学习得更快，并最终达到更高的性能上限；同时，在整个训练过程中，它表现出更高的策略熵和更低的梯度范数。

</details>

---

### [[20_Research/Papers/具身智能/Multi-Agent_Reinforcement_Learning_for_Safe_Autonomous_Driving_Under_Pedestrian_Behavioral_Uncertainty|Multi-Agent Reinforcement Learning for Safe Autonomous Driving Under Pedestrian Behavioral Uncertainty]]

![[assets/2605.20255_figure.png|800]]

- **arXiv**: [2605.20255](https://arxiv.org/abs/2605.20255)
- **PDF**: https://arxiv.org/pdf/2605.20255
- **详细分析**: [[20_Research/Papers/具身智能/Multi-Agent_Reinforcement_Learning_for_Safe_Autonomous_Driving_Under_Pedestrian_Behavioral_Uncertainty|Multi-Agent Reinforcement Learning for Safe Autonomous Driving Under Pedestrian Behavioral Uncertainty]]
- **作者**: Prakash Aryan, Kaushik Raghupathruni, Timo Kehrer, Sebastiano Panichella
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 大模型, 机器人, 世界模型
- **相关性评分**: 2.62（加权：具身智能 0.6，大模型 0.4，强化学习 1.16，世界模型 0.16，机器人 0.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

自动驾驶车辆的仿真测试通常依赖脚本化或过于简化的行人模型，难以刻画真实人类过街行为的异质性与不确定性，尤其是在“闯红灯/横穿马路（jaywalking）”这类由潜在人格特质驱动、且车辆无法直接观测的场景中。这样的测试设定会低估真实道路中的风险，从而限制安全评估的可信度。本文关注在行人行为不确定条件下，如何通过更真实的交互建模来提升自动驾驶安全训练与评测的有效性。

#### 方法概述和架构

论文构建了一个基于多智能体强化学习的仿真环境，使用 MAPPO 对一辆自驾车（SDC）与12个行人进行联合训练。行人的底层移动由脚本化的 Dijkstra 最短路径规划完成，而强化学习策略只负责“走/等（go/wait）”这类高层决策；当选择“走”时，是否走人行横道或横穿马路由一个在回合开始时采样、且对 SDC 隐藏的人格特质参数决定。SDC 采用运动学自行车模型，观测自身状态、目标、道路与车道信息以及最近行人的状态；行人观测则包含自身状态、人格特质、航点方向、地表类型和与 SDC 的相对状态。训练阶段采用 CTDE 范式下的共享集中式 critic，推理时仅使用分散式 actor。为了刻画不确定性，作者提出 Speed Differential 指标，直接从轨迹中比较 SDC 在靠近可预测的横道行人与不确定的横穿行人时的速度差，并进一步统计碰撞归因。

#### 实验结果分析

实验在500个 episode 上评估，并与多种规则基线以及单智能体强化学习方案比较。结果显示，联合训练的 SDC 达到78%的目标到达率和14%的碰撞率，优于最佳规则基线的35%目标到达率和33%碰撞率；相比单智能体 RL 的20%碰撞率，联合训练将碰撞进一步降至14%。在不确定性分析中，SDC 在距离0–3米范围内靠近 jaywalker 时的速度比靠近横道行人时快2.65 m/s，说明其对这类突发过街并未充分预期；尽管 jaywalking 仅占13%的过街事件，却关联了62%的碰撞。消融结果还表明，随着 jaywalking 概率从0%提升到50%，性能先平稳后显著恶化，说明该方法能容忍一定程度的真实不确定性，但在高比例横穿场景下会出现非线性退化。

<details>
<summary>完整摘要</summary>

基于仿真的自动驾驶汽车（SDC）测试通常依赖脚本化或简化的行人模型，这些模型无法刻画真实人类过街行为的异质性与不确定性。这限制了安全评估的真实性，尤其是在闯红灯（jaywalking）场景中，因为这类行为由车辆无法观测的潜在人格特质所支配。我们假设：将行人与 SDC 通过多智能体强化学习（MARL）进行联合训练，比让 SDC 仅与固定行人策略对抗，能够产生更真实的交互场景；并且，预测性过街与非预测性过街之间的行为差距可以直接从轨迹中测量出来。本文描述了一个 MARL 环境，其中一辆 SDC 与12个行人使用 Multi-Agent Proximal Policy Optimization（MAPPO）共同训练。行人的运动方式遵循脚本化的 Dijkstra 路径搜索，而强化学习策略控制高层的“走/等”决策。闯红灯概率取决于每个行人在回合开始时采样得到、且对 SDC 隐藏的人格特质。经过500个 episode 的评估，共同训练的 SDC 达到78%的目标到达率和14%的碰撞率；相比之下，最佳规则基线仅达到35%的目标到达率和33%的碰撞率。一个速度差异指标表明，在近距离（0–3米）时，SDC 在靠近闯红灯行人时的速度比靠近人行横道行人时快2.65 m/s，这说明它没有预料到闯红灯交互。虽然闯红灯仅占13%的过街事件，却与62%的碰撞相关。与单智能体 RL 相比，与 MARL 行人共同训练可将碰撞率降低30%，因为行人在学习到 SDC 快速接近时会主动等待。

</details>

---

### [[20_Research/Papers/大模型/ProcBench_Evaluating_Process-Level_Defects_and_Control_Preservation_in_LLM_Coding_Agents|ProcBench: Evaluating Process-Level Defects and Control Preservation in LLM Coding Agents]]

![[assets/2605.20251_figure.png|800]]

- **arXiv**: [2605.20251](https://arxiv.org/abs/2605.20251)
- **PDF**: https://arxiv.org/pdf/2605.20251
- **详细分析**: [[20_Research/Papers/大模型/ProcBench_Evaluating_Process-Level_Defects_and_Control_Preservation_in_LLM_Coding_Agents|ProcBench: Evaluating Process-Level Defects and Control Preservation in LLM Coding Agents]]
- **作者**: Jiawei He, Jie Jia, Chenbo Liu, Chaoyi Xue, Yapeng Song, Xikai Yang, Dong Sun
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

现有针对 LLM 编码智能体的评测，大多只看最终结果，例如任务是否完成、是否通过测试或能否成功编译，但这类指标很难反映智能体在执行过程中的真实行为。对于多步、长时程的代码修复和终端操作任务而言，很多关键缺陷并不会直接体现在最终答案上，而是出现在中间过程，例如上下文陈旧、重复无效调用、流程过长或难以监督。作者因此提出需要一种面向“执行过程”的评测方式，用来补足传统 outcome-based evaluation 的盲区。

#### 方法概述和架构

论文提出 ProcBench，用于评测 LLM coding agents 的执行过程质量，而不是只看最终产出。其核心做法是先把不同系统的原始日志标准化为统一的轨迹表示，再在该表示上抽取过程证据，并将其映射到一个可复用的缺陷本体中。该本体覆盖 4 大类、11 种执行缺陷，包括上下文管理、工具使用效率、工作流结构和工具生态一致性。ProcBench 进一步对缺陷证据进行校准，输出分级风险与可比的 scorecard，而不是直接用简单阈值二值化。除此之外，作者引入 control preservation 来衡量执行过程是否可解释、可中断、可修复、可回滚，以及是否能在需要时交还控制权，并将其与缺陷发现一起纳入统一报告。

#### 实验结果分析

作者在从 AndroidBench、TerminalBench 和 SWE-bench-Verified 中抽样的 200 个案例上评估 ProcBench，并与传统只看结果的评测方式进行对比。实验表明，ProcBench 能以较好的可靠性完成实例化，且其校准后的语义比直接阈值判定更稳定。它还能揭示许多传统 outcome 指标容易忽略的执行质量差异，说明仅看最终成功率不足以刻画编码智能体的真实行为。节选文本中未给出具体数值。

<details>
<summary>完整摘要</summary>

现有针对 LLM 编码智能体的基准测试主要评估最终结果。虽然这类指标有助于衡量整体能力，但它们提供的可见性有限，而且经常会遗漏在执行过程中出现的缺陷。我们提出 ProcBench，这是一个用于 LLM 编码智能体执行过程评测的基准。ProcBench 将反复出现的执行缺陷组织为一个可复用的本体，覆盖 4 个类别中的 11 种缺陷类型，并通过标准化的过程证据来评估智能体轨迹，而不仅仅依赖最终结果。为了支持异构智能体之间的比较，ProcBench 将原始日志标准化为统一的轨迹表示，并针对过程层面的发现报告经过校准的计分卡。此外，ProcBench 使用 control preservation 来量化执行过程质量，用以刻画执行是否保持可解释、可中断、可修正、可回滚，以及在需要时是否能够交还控制权。我们在从 AndroidBench、TerminalBench 和 SWE-bench-Verified 三个基准中抽样得到的 200 个案例上评估 ProcBench。结果表明，ProcBench 可以被实例化且具有较好的可靠性，相比直接阈值化具有更稳定的语义，并且能够揭示常规基于结果的评测往往忽略的执行质量差异。

</details>

---

### [[20_Research/Papers/大模型/GROW_Aligning_GRPO_with_State-Action_Modeling_for_Open-World_VLM_Agents|GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents]]

![[assets/2605.20246_figure.png|800]]

- **arXiv**: [2605.20246](https://arxiv.org/abs/2605.20246)
- **PDF**: https://arxiv.org/pdf/2605.20246
- **详细分析**: [[20_Research/Papers/大模型/GROW_Aligning_GRPO_with_State-Action_Modeling_for_Open-World_VLM_Agents|GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents]]
- **作者**: Xiongbin Wu, Zhihao Luo, Shanzhe Lei, Lechao Zhang, Xuhong Wang, Jie Yang, Zhonglong Zheng, Yuanjie Zheng, Xin Tan, Wei Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.72（加权：大模型 1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

视觉-语言模型（VLM）智能体在开放世界任务中进展迅速，但这类任务往往需要多轮视觉感知与动作执行，才能逐步完成目标。现有方法仍主要依赖带专家演示的 SFT，数据收集成本高、扩展性有限，而且单纯模仿学习在很多场景下不如 RL 的上限高。虽然 GRPO 这类相对策略优化方法已在部分 VLM 训练中表现出优势，但直接用于开放世界多轮交互时，标准做法需要把整条轨迹作为训练样本，容易带来上下文过长、噪声累积和优化不稳定等问题。

#### 方法概述和架构

论文提出 GROW，用于将 GRPO 改造为适配开放世界 VLM 智能体的强化学习框架。其核心做法是先对采样得到的整条 rollout 轨迹做分解，把每一步转化为状态-动作样本，再在同一组 rollout 内基于这些细粒度样本计算相对优势，而不是把完整轨迹当作单一优化单位。为给稀疏的终局奖励分配学习信号，方法沿轨迹按时间步进行折扣回传，越接近成功终点的状态-动作对获得越强的训练信号。随后，GROW 在分解后的状态-动作样本上执行类似 GRPO 的 clipped policy optimization，从而保留相对优化思想，同时避免长上下文与无关信息干扰。论文还给出一个 surrogate analysis，说明在若干简化假设下，即使分组样本来自不同局部状态而不是同一提示上下文，也仍能保留有效的相对策略优化信号。

#### 实验结果分析

实验主要在 Minecraft 中进行，覆盖 800 多个任务，任务类型包括空间导航、GUI 操作和动态战斗等，并与多种基于模仿学习和 RL 的基线进行比较。结果显示，GROW 在成功率和执行效率上都达到 SOTA；可见文本未给出具体数值。作者还报告了对未见任务的泛化能力，以及行为层面的改进，例如更强的目标重新定位能力和对干扰项更鲁棒的 GUI 操作；消融实验也支持了轨迹分解与状态-动作建模的有效性。

<details>
<summary>完整摘要</summary>

近年来，视觉-语言模型（VLM）智能体在开放世界任务中取得了可观进展，而这类任务的成功完成通常需要多轮视觉感知与动作执行。然而，现有方法仍主要依赖带专家演示的监督微调（SFT）；先进的强化学习（RL）算法，尤其是组相对策略优化（GRPO），尚未在这类任务的多轮 RL 中得到有效应用，因为标准 GRPO 需要将完整轨迹作为训练样本，这会导致上下文过长并引入过多噪声。为解决这一问题，我们提出 GROW，这是一种面向开放世界 VLM 智能体的 RL 框架，它将采集到的轨迹分解为状态-动作样本，并在这些样本之间计算优势，而不是把整条轨迹视为一个单一实体。我们进一步给出一个 surrogate analysis，表明尽管分组样本对应的是不同的局部状态，而非相同的提示上下文，但在若干简化假设下，该目标仍能保留 GRPO 的核心相对策略优化信号。在 800 多个 Minecraft 任务上的实验表明，我们的方法达到了最先进（SOTA）性能，证明了该 RL 框架对开放世界 VLM 智能体的有效性。

</details>

---

### [[20_Research/Papers/大模型/Evaluating_multimodal_emotion_recognition_in_proactive_conversational_agents_A_user_study|Evaluating multimodal emotion recognition in proactive conversational agents: A user study]]

![[assets/2605.20200_figure.png|800]]

- **arXiv**: [2605.20200](https://arxiv.org/abs/2605.20200)
- **PDF**: https://arxiv.org/pdf/2605.20200
- **详细分析**: [[20_Research/Papers/大模型/Evaluating_multimodal_emotion_recognition_in_proactive_conversational_agents_A_user_study|Evaluating multimodal emotion recognition in proactive conversational agents: A user study]]
- **作者**: Adnana Dragut, Raquel Lacuesta, F. Xavier Gaya-Morey, Jose M. Buades-Rubio
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

这篇论文关注的是主动式对话智能体中的情绪识别问题，尤其是在大模型驱动的社交交互场景里，系统如何实时理解用户的情感状态。现有方法往往依赖面部表情、语音或离线数据集，但在真实对话中，用户的外显表情未必能反映真实情绪，容易出现“扑克脸”现象。作者认为，仅靠视觉信号会低估或误判用户情绪，因此需要结合语义上下文来做更可靠的情绪判断。这项工作值得关注之处在于，它把多模态情绪识别放进了真实的、非脚本化的人机对话中，而不是停留在静态数据集或模拟实验。

#### 方法概述和架构

论文构建了一个集成到主动式 Socially Interactive Agent（SIA）中的多模态情绪识别模块，由两个核心通道组成：基于计算机视觉的面部识别模块和基于生成式人工智能的语义语言分析引擎。系统在用户与智能体的实时对话过程中并行收集视觉表情和文本语义信息，再与用户自报告的情绪状态进行对照分析。实验采用 20 名参与者，与智能体进行动态、非脚本化对话，以观察不同话题和对话结构如何影响情绪表达与识别结果。方法上还引入了“2D Emotion Matrix”来记录和评估主观体验与情绪变化，并分析智能体使用同理心、幽默等结构化语言模式时对用户情绪的触发效果。整体流程是：智能体主动发起对话、实时采集面部与语言信号、分别进行视觉和语义情绪推断、最后用问卷与自报告作为参照进行比较。

#### 实验结果分析

实验在实验室环境中进行，使用 Sanbot Elf 作为硬件平台，并结合自研 Android 中间件完成实时交互与数据同步；节选中未给出具体基线模型和定量指标数值。结果显示，面部表情识别与用户真实内在情绪之间存在显著偏差，很多用户在与 AI 交互时表现出认真、专注的“扑克脸”，即使内心处于积极情绪也未必会在脸上明显体现。相比之下，基于生成式 AI 的语言语义分析更可靠，因为它能结合上下文理解用户表达。论文还发现，SIA 通过调整话题和使用同理心、幽默等语言结构，能够有效诱发特定情绪；但如果主动性设计不够校准，也可能导致用户 disengagement 并产生“过于人工”的感受。

<details>
<summary>完整摘要</summary>

本文提出了一个集成到由生成式人工智能驱动的主动式 Socially Interactive Agent（SIA）中的多模态情绪识别模块。该系统通过两个不同通道对实时情感状态进行评估：一个是基于计算机视觉的面部识别模块，另一个是语义语言分析引擎。为验证该框架，研究开展了一项实证研究，邀请 20 名用户与对话智能体进行动态、非脚本化对话。研究结果揭示了自动视觉线索与真实内在情绪状态之间存在显著差异。用户在与 AI 互动时，尽管实际体验到的是积极情绪，却往往持续表现出一种“扑克脸”效应，即面部表情严肃、专注。因此，生成式 AI 的语言分析由于能够结合用户言语表达的上下文信息，被证明显著更可靠。此外，对交互动态的分析表明，SIA 通过调整对话主题并采用结构化的语言模式，例如同理心或幽默语言，能够有效诱发特定情绪。然而，研究也指出，在某些情况下，未经校准的主动性会导致用户 disengagement，并让用户产生智能体“过于人工”的感受。总体而言，本研究强调：要让 SIA 更自然、更具人类交互感，必须进一步改进其对用户情绪演化的动态适应能力，并依赖更深层的语言上下文来进行情绪理解。

</details>

---

### [[20_Research/Papers/大模型/Tool-Augmented_Agent_for_Closed-loop_Optimization,Simulation,and_Modeling_Orchestration|Tool-Augmented Agent for Closed-loop Optimization,Simulation,and Modeling Orchestration]]

![[assets/2605.20190_figure.png|800]]

- **arXiv**: [2605.20190](https://arxiv.org/abs/2605.20190)
- **PDF**: https://arxiv.org/pdf/2605.20190
- **详细分析**: [[20_Research/Papers/大模型/Tool-Augmented_Agent_for_Closed-loop_Optimization,Simulation,and_Modeling_Orchestration|Tool-Augmented Agent for Closed-loop Optimization,Simulation,and Modeling Orchestration]]
- **作者**: Liyuan Deng, Shujian Deng, Yongkang Chen, Yongkang Dai, Zhihang Zhong, Linyang Li, Xiao Sun, Yilei Shi, Huaxi Huang
- **cs 子类**: cs.AI, cs.GR
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

工业设计中的闭环优化通常需要在CAD建模、CAE仿真、结果解析和几何修改之间反复迭代，但真实场景里常常存在CAD与CAE之间的语义鸿沟：仿真反馈是高维的物理量，而工程师需要将其转化为可执行、可保持历史树一致的参数化几何编辑。与此同时，几何重建失败、网格划分错误和求解器不收敛等工具链问题频繁出现，使得这一过程不再是简单优化，而是带有硬执行约束、随机失败状态和长时序决策的复杂任务。该论文关注将大模型与强化学习用于工程设计自动化，尝试让LLM真正学会在真实工具链中完成闭环CAD-CAE优化，因此具有较强的工业应用价值。

#### 方法概述和架构

论文提出COSMO-Agent（Closed-loop Optimization, Simulation, and Modeling Orchestration），这是一个工具增强的强化学习框架，用来训练LLM在闭环CAD-CAE流程中进行多轮决策。作者把CAD生成、CAE求解、结果解析和几何修正统一建模为交互式RL环境，LLM在每一轮根据当前参数、材料、仿真反馈和历史记录，输出下一步参数化编辑与工具调用策略。系统通过MCP暴露四类工具：CAD生成器、CAE求解器、结果提取器和成本计算器，形成“生成几何—仿真求解—抽取指标—判断是否满足约束—继续修正”的循环。为保证训练稳定，方法设计了多约束奖励，同时鼓励可行性、工具链鲁棒性和结构化输出有效性，避免模型生成数值上看似优秀但实际上不可执行的设计。论文还构建了一个与工业对齐的数据集，覆盖25类部件、约2万个可执行CAD-CAE任务，用于训练和统一评测。

#### 实验结果分析

实验在该工业对齐基准上，将COSMO-Agent与多种开源和闭源LLM在统一接口、固定工具调用与重试预算下进行比较，评估指标包括可行性、效率和稳定性。结果表明，经过COSMO-Agent训练后，小型开源LLM在约束驱动设计任务上的能力显著提升，在可行性、效率和稳定性上超过了更大规模的开源模型以及一些强闭源模型。正文节选还提到作者做了强化学习训练效果、基于rollout日志的奖励设计以及泛化性能等消融与分析；但可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

迭代式工业设计—仿真优化的瓶颈在于CAD与CAE之间存在语义鸿沟：如何在多种耦合约束下，把仿真反馈转化为有效的几何编辑。为填补这一鸿沟，我们提出COSMO-Agent（Closed-loop Optimization, Simulation, and Modeling Orchestration），一种工具增强的强化学习（RL）框架，用于训练LLM完成闭环CAD-CAE流程。具体而言，我们将CAD生成、CAE求解、结果解析和几何修正建模为一个交互式RL环境，其中LLM学习调度外部工具，并持续修正参数化几何，直到满足约束为止。为使这种学习过程稳定且适合工业使用，我们设计了一个多约束奖励函数，联合鼓励可行性、工具链鲁棒性和结构化输出有效性。此外，我们还贡献了一个与工业对齐的数据集，覆盖25类部件，包含可执行的CAD-CAE任务，用于真实训练与评测。实验表明，COSMO-Agent训练能够显著提升小型开源LLM在约束驱动设计上的能力，在可行性、效率和稳定性方面超过了更大规模的开源模型以及强闭源模型。

</details>

---

### [[20_Research/Papers/强化学习/SOLAR_A_Self-Optimizing_Open-Ended_Autonomous_Agent_for_Lifelong_Learning_and_Continual_Adaptation|SOLAR: A Self-Optimizing Open-Ended Autonomous Agent for Lifelong Learning and Continual Adaptation]]

![[assets/2605.20189_figure.png|800]]

- **arXiv**: [2605.20189](https://arxiv.org/abs/2605.20189)
- **PDF**: https://arxiv.org/pdf/2605.20189
- **详细分析**: [[20_Research/Papers/强化学习/SOLAR_A_Self-Optimizing_Open-Ended_Autonomous_Agent_for_Lifelong_Learning_and_Continual_Adaptation|SOLAR: A Self-Optimizing Open-Ended Autonomous Agent for Lifelong Learning and Continual Adaptation]]
- **作者**: Nitin Vetcha, Dianbo Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

大模型虽然在离线基准上表现出色，但在真实世界的流式、动态场景中会遇到概念漂移、数据分布非平稳以及梯度微调成本高的问题，传统 fine-tuning 往往还会带来灾难性遗忘。现有参数高效微调方法虽然减少了更新量，但本质上仍是静态方案，难以自动学习“如何适应”新任务。本文关注的是让模型在测试时和持续学习过程中自主调整内部权重策略，从而更接近人类在终身学习中的自我修正能力，因此具有较强的研究价值。

#### 方法概述和架构

论文提出 SOLAR（Self-Optimizing Lifelong Autonomous Reasoner），将大模型权重视为可探索的环境变量，通过参数级 meta-learning 让模型在权重空间中自我优化。方法先构建一个关于常识知识的强先验，并只在低秩参数上进行探索，以降低高维非凸权重空间的搜索难度；同时利用卷积式解码器从可行的权重分布中采样初始探索点。随后，SOLAR 使用基于大模型的强化学习代理，在测试时生成关于“如何修改自身权重”的假设，并把人手整理的种子知识库作为初始动作空间。训练过程分为三个层级：Level I 学习从候选知识库中选择单个有效自编辑策略，Level II 学习串联多个自编辑形成链式策略，Level III 则放开到完整策略空间，探索超越人工设计的修改方法。系统还维护一个不断扩展的有效修改策略库，作为隐式的 episodic memory，用来平衡对新任务的适应性与对历史元知识的保留。

#### 实验结果分析

论文在常识、数学、医疗、代码、社交和逻辑推理等任务上进行了实验，并与强基线方法比较；从正文节选可见，评测包含持续自适应、测试时适应和迁移学习相关设置。结果表明，SOLAR 在多类任务上优于强基线，说明其自动发现权重修改策略的能力具有跨领域泛化性。正文还提到进行了消融研究，用于分析不同训练层级和组件设计的作用；但节选中未给出具体数值，因此可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

尽管大语言模型（LLMs）已经取得了显著成功，但在动态的真实世界环境中部署时仍然面临瓶颈，主要挑战是概念漂移以及基于梯度的适应成本过高。传统 fine-tuning（FT）难以在非平稳数据流上进行自适应，往往会导致灾难性遗忘，或者需要大量人工数据整理。为了解决流式学习与持续学习范式下的这些限制，我们提出 Self-Optimizing Lifelong Autonomous Reasoner（SOLAR），这是一个开放式的自主智能体，它利用参数级 meta-learning 来实现自我改进，并将模型权重视为可探索的环境。系统首先通过整合一个关于常识知识的强先验来启动，使其对 transfer-learning 更加有效。借助多层级强化学习方法，SOLAR 能够自主发现适应策略，从而在测试时高效地适应未见过的领域。更关键的是，SOLAR 维护一个不断演化的有效修改策略知识库，这在隐式上充当了 episodic memory buffer，以平衡可塑性（对新任务的适应）与稳定性（对元知识的保留）。实验表明，SOLAR 在常识、数学、医疗、代码、社交和逻辑推理任务上都优于强基线，标志着向能够在不断演化环境中进行终身适应的自主智能体迈出了重要一步。

</details>

---
