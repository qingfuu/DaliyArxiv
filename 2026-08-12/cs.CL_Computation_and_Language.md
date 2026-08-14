# cs.CL | Computation and Language | 2026-08-12

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/大模型/MultiModal_Code-Switching_Interleaving_Visual_Objects_into_Language_for_Explicit_Object-Level_Alignment|MultiModal Code-Switching: Interleaving Visual Objects into Language for Explicit Object-Level Alignment]]

![[assets/2608.11167_figure.png|800]]

- **arXiv**: [2608.11167](https://arxiv.org/abs/2608.11167)
- **PDF**: https://arxiv.org/pdf/2608.11167
- **详细分析**: [[20_Research/Papers/大模型/MultiModal_Code-Switching_Interleaving_Visual_Objects_into_Language_for_Explicit_Object-Level_Alignment|MultiModal Code-Switching: Interleaving Visual Objects into Language for Explicit Object-Level Alignment]]
- **作者**: Changhao Xiang, Shangyu Xing, Zhen Wu, Jianbing Zhang, Xinyu Dai
- **cs 子类**: cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《MultiModal Code-Switching: Interleaving Visual Objects into Language for Explicit Object-Level Alignment》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing Multimodal Large Language Models (MLLMs) predominantly rely on image-text pairs for modality alignment pretraining, mapping global image representations to long textual descriptions. However, this image-level alignment suffers from referential ambiguity: models struggle to infer the correspondences between multiple visual objects and textual entities from the global representation, leading to data inefficiency and suboptimal semantic grounding. To address this, we propose MultiModal Code-Switching (MMCS), a novel pretraining paradigm that provides explicit object-level supervision. Inspired by the linguistic phenomenon of code-switching, MMCS interleaves vision and language by replacing textual entities with their corresponding visual objects, enforcing local vision-language grounding. We further develop a scalable data synthesis pipeline to generate a pretraining dataset of 773K samples with accurate object-entity correspondences. Experiments show that MMCS is highly data-efficient: with only 50K samples, it matches or surpasses models trained on 600K image-text pairs. Furthermore, MMCS consistently improves visual grounding and perception capabilities across varying model scales.

</details>

---

### [[20_Research/Papers/强化学习/Actions_Speak_Louder_than_Words_Measuring_Cross-Lingual_Policy_Retention_in_Tool-Using_Agents|Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention in Tool-Using Agents]]

![[assets/2608.11110_first_page.png|800]]

- **arXiv**: [2608.11110](https://arxiv.org/abs/2608.11110)
- **PDF**: https://arxiv.org/pdf/2608.11110
- **详细分析**: [[20_Research/Papers/强化学习/Actions_Speak_Louder_than_Words_Measuring_Cross-Lingual_Policy_Retention_in_Tool-Using_Agents|Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention in Tool-Using Agents]]
- **作者**: Sourabrata Mukherjee, Kalika Bali, Sunayana Sitaram
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention in Tool-Using Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When a tool-using agent is given the same task in a different language, does it still take the same steps? Multilingual evaluation rarely asks: it compares final answers and discards the actions. Yet those actions are the product: they fix cost and latency, decide how the system fails, and are the only auditable part of its behaviour. We make the action policy the measured object across 8 models, 6 parallel benchmarks and 41 languages (2.38M rollouts). The naive measurement fails: five confounds sit between raw trace similarity and any defensible claim, each able to flip a conclusion. Short traces score higher, empty traces score perfectly, unrelated traces agree by chance over half the time, the gap is capped by each model's reproducibility, and a model asked the same question twice in one language answers differently, leaving no baseline. We remove all five, and every correction makes the effect larger. Divergence proves structural, not sampling noise: it survives greedy decoding in every cell and stays flat as temperature rises, even as models grow less self-consistent. Normalised by their own reproducibility, four very different frontier models converge under greedy decoding, each keeping 71-73% of its action policy across languages, with model identity explaining only 5.7% of the variance. Below roughly 10B parameters it breaks down, and the ordering among smaller models is largely an artifact of a chance floor we measure by permutation rather than assume. Agents route non-English tasks through English; this pivot is causally load-bearing, confirmed by a pre-registered prediction across four models, and models will not abandon it when told to. Finally, a single trace-extraction regex, not the model, manufactured a multilingual failure: two worked examples raise one model's measured accuracy twenty-sixfold while its accuracy on readable outputs barely moves.

</details>

---

### [[20_Research/Papers/大模型/ReRound_Reconstructive_Rounding_to_Resolve_Midpoint_Ambiguity_in_Calibration-Free_LLM_Quantization|ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Free LLM Quantization]]

![[assets/2608.11045_figure.png|800]]

- **arXiv**: [2608.11045](https://arxiv.org/abs/2608.11045)
- **PDF**: https://arxiv.org/pdf/2608.11045
- **详细分析**: [[20_Research/Papers/大模型/ReRound_Reconstructive_Rounding_to_Resolve_Midpoint_Ambiguity_in_Calibration-Free_LLM_Quantization|ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Free LLM Quantization]]
- **作者**: He-Yen Hsieh, H. T. Kung
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Free LLM Quantization》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

ReRound (Reconstructive Rounding) is a post-training quantization method that addresses the midpoint ambiguity inherent in standard round-to-nearest (RTN) schemes when quantizing weights near the centers of quantization intervals. Starting from a pretrained LLM, ReRound trains a conditional diffusion model to produce continuous reconstructions of low-bit weights for the LLM. These reconstructed weights act as a guidance signal to disambiguate the rounding direction of weights located close to interval midpoints. To integrate this reconstruction-guided rounding with conventional RTN, ReRound introduces a tolerance metric measuring how far the quantized weight (not the final quantized integer) is away from the midpoint: quantized weights within a tolerance region around midpoints are quantized using diffusion-based reconstructions, whereas weights closer to quantization boundaries are quantized with RTN. By sweeping the tolerance parameter, ReRound generates multiple candidate quantized integer weight matrices and selects the de-quantized weight matrix candidate whose leading singular values most closely match those of the original full-precision weights. This selected candidate determines the tolerance parameter ReRound uses. ReRound is particularly effective for smaller LLMs. Across a range of such models, it consistently outperforms standard RTN for 3-bit and 4-bit weight quantization. ReRound achieves superior accuracy compared to an extensive set of calibration-free methods, remains competitive with calibration-dependent approaches, and operates entirely offline, introducing no additional overhead during low-bit inference. The ReRound strategy represents a new approach for low-bit quantization. The method applies to AI models beyond LLMs. This paper focuses on its applications to small LLMs.

</details>

---

### [[20_Research/Papers/强化学习/ConRub-Med_Reinforcement_Learning_with_Consensus_Rubrics_for_Open-Ended_Medical_Question_Answering|ConRub-Med: Reinforcement Learning with Consensus Rubrics for Open-Ended Medical Question Answering]]

![[assets/2608.10996_first_page.png|800]]

- **arXiv**: [2608.10996](https://arxiv.org/abs/2608.10996)
- **PDF**: https://arxiv.org/pdf/2608.10996
- **详细分析**: [[20_Research/Papers/强化学习/ConRub-Med_Reinforcement_Learning_with_Consensus_Rubrics_for_Open-Ended_Medical_Question_Answering|ConRub-Med: Reinforcement Learning with Consensus Rubrics for Open-Ended Medical Question Answering]]
- **作者**: Taojie Zhu, Yuan Xia, Tao Sun, Yizhi Wang, Yan Chen, Qunshan He, Tian Guan, Jian Wang, Jinjie Gu, Junwei Liu, Yonghong He
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《ConRub-Med: Reinforcement Learning with Consensus Rubrics for Open-Ended Medical Question Answering》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HealthBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards has been especially effective in mathematics and coding, where answers can be checked automatically. Many open-ended medical questions lack comparably cheap outcome verifiers: responses may be partly correct, incomplete, or contain clinically consequential errors. Rubrics written or validated by physicians offer strong clinical grounding, but involving experts in every instance is costly. Model-generated rubrics make this supervision scalable. We introduce ConRub-Med to preserve useful distinctions as rubric feedback moves from construction to policy optimization. For each prompt, three heterogeneous language models propose atomic criteria independently; a separate model reviews them, retaining only criteria with semantic support from all three generators. Three-State scoring distinguishes correct coverage, missing information, and incorrect claims. Errors receive negative rather than zero credit. When every response in a complete Group Relative Policy Optimization (GRPO) group receives the same final reward, a pairwise judge provides sequence advantages only if both candidate orders agree, without changing the scalar rewards. Groups without ties use vanilla GRPO. In a blinded study matched by question, two medical experts rate panels from the full pipeline as more clinically relevant than panels produced by one generator. Across the evaluated open models, ConRub-Med ranks first on six of nine benchmarks and achieves the highest medical and generalization averages. Using the resulting rubric dataset of 5,166 prompts, it scores $38.98 \pm 1.04$ (mean $\pm$ SD) on HealthBench-Hard, compared with InfiMed-ORBIT's 33.60 with 8,000 samples and 37.30 with 28,000.

</details>

---

### [[20_Research/Papers/强化学习/Mitigating_Context_Interference_for_Reliable_and_Efficient_Search_Agents|Mitigating Context Interference for Reliable and Efficient Search Agents]]

![[assets/2608.10743_figure.png|800]]

- **arXiv**: [2608.10743](https://arxiv.org/abs/2608.10743)
- **PDF**: https://arxiv.org/pdf/2608.10743
- **详细分析**: [[20_Research/Papers/强化学习/Mitigating_Context_Interference_for_Reliable_and_Efficient_Search_Agents|Mitigating Context Interference for Reliable and Efficient Search Agents]]
- **作者**: Boyang Xue, Bin Wu, Shuofei Qiao, Sheng Wang, Rui Wang, Yiming Du, Hongru Wang, Jeff Z. Pan, Emine Yilmaz, Kam-Fai Wong, Aldo Lipani
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Mitigating Context Interference for Reliable and Efficient Search Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CRRL, HotpotQA, PopQA, TriviaQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent research empowers Large Language Models (LLMs) as multi-turn search agents to iteratively retrieve and generate outputs until complex tasks are solved. However, the contexts of multi-turn search agents are lengthy and complex. For example, the retrieved set of documents in each turn would inevitably introduce irrelevant information that distracts LLMs, referring to \textit{context interference}, potentially hindering the reliability and efficiency of search agents. Therefore, we conduct a systematic study on context interference in multi-turn search agents, focusing on investigating i) which parts of the context of search agents will contribute to the context interference, ii) how to refine the contexts of search agents to mitigate the interference, and iii) can incorporating context refinement into search agent training yield further improvements. We reveal that interference primarily arises from the latest retrieved documents. Based on the explored findings, we then introduce a distill-based context refiner to dynamically mitigate context interference for multi-turn search agents. Finally, we validate that incorporating context refinement into RL training pipelines of search agents can significantly enhance both reliability and efficiency. This study highlights the importance of mitigating context interference of search agents, inspiring a novel paradigm of ``refine context and then generate'' for AI agents.

</details>

---

### [[20_Research/Papers/大模型/The_Signal_Rail_A_Deterministic_Motion_Grammar_for_Communicating_Conversational_Agent_State_in_Terminal_Interfaces|The Signal Rail: A Deterministic Motion Grammar for Communicating Conversational Agent State in Terminal Interfaces]]

![[assets/2608.10689_first_page.png|800]]

- **arXiv**: [2608.10689](https://arxiv.org/abs/2608.10689)
- **PDF**: https://arxiv.org/pdf/2608.10689
- **详细分析**: [[20_Research/Papers/大模型/The_Signal_Rail_A_Deterministic_Motion_Grammar_for_Communicating_Conversational_Agent_State_in_Terminal_Interfaces|The Signal Rail: A Deterministic Motion Grammar for Communicating Conversational Agent State in Terminal Interfaces]]
- **作者**: Matteo Grella
- **cs 子类**: cs.CL, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《The Signal Rail: A Deterministic Motion Grammar for Communicating Conversational Agent State in Terminal Interfaces》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Terminal interfaces to conversational agents report rich internal state (listening, thinking, executing tools, awaiting input, failing) almost entirely through text, while the motion channel beside it, the one peripheral vision monitors without reading, carries a single bit: alive. We present the Signal Rail, a one-row terminal status instrument that gives that channel a grammar. Four ideas govern it: spatial semantics (input, processing, and output zones, with direction as meaning), a motion grammar (one kinetic rule per state, never color alone), determinism (frames as a pure function of explicit inputs, golden-frame testable), and honesty (no invented progress or activity). We contribute a 45-section normative specification and a reference implementation inside a working full-duplex local voice agent driven by real signals.

</details>

---

### [[20_Research/Papers/大模型/Every_Token_Counts_Exact_Likert-Scale_Distributions_for_Measuring_LLM_Attitudes_and_Biases|Every Token Counts: Exact Likert-Scale Distributions for Measuring LLM Attitudes and Biases]]

![[assets/2608.10503_figure.png|800]]

- **arXiv**: [2608.10503](https://arxiv.org/abs/2608.10503)
- **PDF**: https://arxiv.org/pdf/2608.10503
- **详细分析**: [[20_Research/Papers/大模型/Every_Token_Counts_Exact_Likert-Scale_Distributions_for_Measuring_LLM_Attitudes_and_Biases|Every Token Counts: Exact Likert-Scale Distributions for Measuring LLM Attitudes and Biases]]
- **作者**: Davood Wadi, Mohsen Ghodrat, Matthew Philp
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Every Token Counts: Exact Likert-Scale Distributions for Measuring LLM Attitudes and Biases》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As Large Language Models (LLMs) are increasingly deployed as autonomous agents, accurately evaluating their latent values and biases is critical. The NLP community typically evaluates models using large, unstructured benchmarks. While effective for general capabilities, these datasets fundamentally conflate causal mechanisms: even when an aggregate bias is detected, unstructured evaluations cannot disentangle whether it stems from baseline traits, contextual confounders, or complex interactions. To address this, we introduce an analytically exact framework for the controlled behavioral evaluation of LLMs. We bridge human psychometrics with LLM mechanics by resolving gaps in design, measurement, and analysis. First, we replace unstructured prompting with fully crossed factorial experiments to systematically isolate causal main and interaction effects. Second, we eliminate Monte Carlo text sampling noise by operating directly on exact, token-level Probability Mass Functions (PMFs). Third, we derive a multivariate ordinal consensus metric and a distributional ANOVA to process these PMFs analytically. We validate our framework with a case study on consumer ethnocentrism across five LLMs, demonstrating how our approach isolates systemic country-of-origin biases that aggregate benchmarks otherwise obscure.

</details>

---

### [[20_Research/Papers/大模型/Calibrating_Post-Training_Feature_Shifts_for_LLM_Data_Contamination_Detection|Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection]]

![[assets/2608.10462_figure.png|800]]

- **arXiv**: [2608.10462](https://arxiv.org/abs/2608.10462)
- **PDF**: https://arxiv.org/pdf/2608.10462
- **详细分析**: [[20_Research/Papers/大模型/Calibrating_Post-Training_Feature_Shifts_for_LLM_Data_Contamination_Detection|Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection]]
- **作者**: Zhen Yang, Mengqi Wang, Gengda Zhao, Mo Zhou, Jianwei Wang, Wenjie Zhang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, ComputerVision, Security

#### 研究背景与动机

《Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are trained on massive and largely undisclosed corpora that may contain copyrighted or privacy-sensitive content. Data contamination detection (DCD) therefore aims to determine whether a given text is a member of the pre-training corpus of a target LLM. Recent state-of-the-art DCD methods follow a feature-based paradigm that derives membership features from the input text and the corresponding model output. However, most modern LLMs undergo post-training, such as instruction tuning, preference optimization, and reasoning-oriented training, which can alter model outputs and shift the corresponding membership features, thereby reducing the separability between members and non-members. To address this problem, we propose CalibDCD, a broadly applicable calibration framework for feature-based DCD methods, comprising (1) Multi-View Shift Detection, which identifies recurring feature shifts associated with post-training, and (2) Bounded Feature Correction, which selectively mitigates their influence on membership prediction. Specifically, Multi-View Shift Detection evaluates controlled prompt variants on known non-member texts and consolidates the most informative views to identify recurring feature shifts. Bounded Feature Correction selectively adjusts feature components aligned with the detected shifts and controls the correction extent to preserve useful detection information. Experiments show that CalibDCD consistently improves existing feature-based detectors, with gains of up to 7.0% in AUC and 15.0% in TPR@5%FPR.

</details>

---

### [[20_Research/Papers/大模型/Detecting_an_Effect_Is_Not_Learning_to_Act_on_It_A_Reward-SNR_Floor_for_LLM_Acquisition_Agents|Detecting an Effect Is Not Learning to Act on It: A Reward-SNR Floor for LLM Acquisition Agents]]

![[assets/2608.10441_figure.png|800]]

- **arXiv**: [2608.10441](https://arxiv.org/abs/2608.10441)
- **PDF**: https://arxiv.org/pdf/2608.10441
- **详细分析**: [[20_Research/Papers/大模型/Detecting_an_Effect_Is_Not_Learning_to_Act_on_It_A_Reward-SNR_Floor_for_LLM_Acquisition_Agents|Detecting an Effect Is Not Learning to Act on It: A Reward-SNR Floor for LLM Acquisition Agents]]
- **作者**: Ying Yuan
- **cs 子类**: cs.CL, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Detecting an Effect Is Not Learning to Act on It: A Reward-SNR Floor for LLM Acquisition Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many pipelines can pay a per-example cost to acquire an auxiliary, model-derived observation -- an LLM's structured reasoning, a slow oracle, an expensive measurement -- and then must decide when the acquired signal is worth using. Our thesis is a distinction that is easy to miss: detecting that such a signal helps on average is not the same as learning to act on it per instance, and a reward-SNR floor governs when the second is even possible. Even when the signal is faithful and an in-sample oracle picking the top-b examples by realized reward shows a sizable apparent gain, no deployable policy can learn when to acquire it: across per-impression, cluster, regime, and uplift-tree granularities, learned routing never beats random, and a matched-moment noise placebo reproduces &gt;=100% of the oracle's apparent gain -- the apparent "learnable structure" is order statistics of noise. We explain this with one distinction, detecting a mean effect vs. learning a per-instance acquisition policy, and a reward-SNR detectability floor: routing is estimable offline only if the reward SNR rho clears rho*(N) ~= 2.8/sqrt(N), with a positive control confirming a true low-SNR limit rather than a broken pipeline. As a concrete instantiation we introduce Structured Hypothesis Embeddings (SHE): a frozen LLM turns a user history into ranked, confidence-scored, evidence-grounded intent hypotheses, fused into a recommender. On three public datasets (MIND, REES46, Amazon-Beauty), SHE is faithful and calibratable, yet its value is backbone- and regime-conditional (significant over an ordered GRU, +0.0114, 95% CI [+0.0030, +0.0209], but a global redundancy gap indistinguishable from zero), and learned acquisition collapses at every granularity because all three datasets sit below the floor. The realizable unit is a design-time regime gate, not a per-instance policy. We release code and a one-command reproduction.

</details>

---

### [[20_Research/Papers/大模型/OpenPM_Auditable_Point-in-Time_Evaluation_for_LLM_Portfolio-Management_Agents|OpenPM: Auditable Point-in-Time Evaluation for LLM Portfolio-Management Agents]]

![[assets/2608.09988_first_page.png|800]]

- **arXiv**: [2608.09988](https://arxiv.org/abs/2608.09988)
- **PDF**: https://arxiv.org/pdf/2608.09988
- **详细分析**: [[20_Research/Papers/大模型/OpenPM_Auditable_Point-in-Time_Evaluation_for_LLM_Portfolio-Management_Agents|OpenPM: Auditable Point-in-Time Evaluation for LLM Portfolio-Management Agents]]
- **作者**: Xinying Cai, Minghao Guo, Jiahe Liu, Jiaojiao Han, Bangwei Guo, Yitao Long, Yuxuan Chen, Bohan Wu, Dimitris N. Metaxas, Raymond Li
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《OpenPM: Auditable Point-in-Time Evaluation for LLM Portfolio-Management Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：InvestorBench, LiveTradeBench, OpenPM-Bench, PortBench, StockBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models are increasingly used to read markets, assess risk, and allocate capital. However, reported results for LLM trading agents can be inflated by look-ahead leakage, optimistic execution, and risk mandates that are described but not enforced. We present OpenPM, an auditable point-in-time evaluation framework for LLM portfolio-management agents. In OpenPM, an agent manages a \$1M long-only book over the S\&amp;P 500 universe using market data at five-minute intervals. Every record visible to the agent must be available at the decision time. Natural-language risk mandates are converted into typed constraints and enforced on the executed portfolio. Each run produces audit artifacts, including a contamination certificate, a cost-sensitivity curve, and a constraint-adherence report. We also build a reference agent named the tiered allocator, where typed analysts score candidates, a constructor LLM proposes weights, and a deterministic critic guarantees feasibility. We isolate constructor behavior by capturing analyst evidence once and replaying it across constructor models. In our short-window case study, stronger constructors show modest and model-dependent gains over equal weighting on the same pool, but analyst quality matters more than constructor choice, and turnover is the main cost driver. All returns are upper bounds on a single frozen window without market impact, not validated alpha.

</details>

---
