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

《GesVLA: Gesture-Aware Vision-Language-Action Model Embedded Representations》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GesVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown strong potential for general-purpose robot manipulation by unifying perception and action. However, existing VLA systems primarily rely on textual instructions and struggle to resolve spatial ambiguity in complex scenes with multiple similar objects. To address this limitation, we introduce gesture as a parallel instruction modality and propose a Gesture-aware Vision-Language-Action model (GesVLA). Our approach encodes gesture features directly into the latent space, enabling them to participate in both high-level reasoning and low-level action generation, and adopts a dual-VLM architecture to achieve tight coupling between gesture representations and action policies. At the data level, we construct a scalable gesture data generation pipeline by rendering hand models onto real-world scene images. This reduces the sim-to-real visual gap while producing rich data with diverse motion patterns and corresponding pointing annotations. In addition, we employ a two-stage training strategy to equip the model with both gesture perception and action prediction capabilities. We evaluate our approach on multiple real-world robotic tasks, including a controlled block manipulation task for validation and more practical scenarios such as product and produce selection. Experimental results show that incorporating gesture consistently improves target grounding accuracy and human-robot interaction efficiency, especially in complex and cluttered environments. Project page: https://gwxuan.github.io/GesVLA/.

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

《From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BehaviorVLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models often suffer from performance degradation under distribution shifts, as they struggle to learn generalized behavior representations across varying environments. While existing approaches attempt to construct behavior representations through action-centric latent variables, they are often limited by short-horizon temporal fragmentation and static execution-alignment, leading to inconsistent behaviors in complex scenarios. To address these limitations, we propose \textbf{BehaviorVLA}, a framework that facilitates robust manipulation through the learning of a temporally coherent behavioral representations. Our approach features two symmetric components: (1) the \textbf{Visuomotor Behavior Encoder (VBE)}, which utilizes a causal Mamba-based architecture to aggregate long-horizon trajectory information into a unified behavior representation; and (2) the \textbf{Phase-conditioned Behavior Decoder (PBD)}, which decodes this representation into precise actions by dynamically aligning task-level priors with real-time execution progress. Experiments on RoboTwin 2.0, LIBERO, and CALVIN demonstrate state-of-the-art success rates of 58\%, 98\%, and 4.36 (Avg.Len), respectively. Notably, in real-world sim-to-real transfer, BehaviorVLA matches the performance of OpenVLA-OFT using only 50\% of the demonstration data, showcasing its superior data efficiency and generalization.

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

《Decoupling Ego-Motion from Target Dynamics via Dual-Interval Motion Cues for UAV Detection》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RetinaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object detection from Unmanned Aerial Vehicles (UAVs) is challenged by severe ego-motion, camera jitter, and large scale variations. While modern detectors perform well on static images, their direct application to UAV video often fails, particularly for small objects in dynamic scenes. Existing motion-based methods either rely on computationally expensive optical flow or use single-interval differencing, which is sensitive to jitter and limited in capturing diverse motion patterns. We propose a vision-only motion-guided detection framework that decouples target motion from camera-induced disturbances. A homography-based Global Motion Compensation (GMC) first aligns adjacent frames. We then introduce a Dual-Interval Motion Extraction strategy that captures both short-term and long-term motion cues. To integrate these cues, a lightweight Motion-Guided Attention (MGA) module enhances feature representations within a Feature Pyramid Network. Experiments on the VisDrone-VID dataset demonstrate consistent improvements over a strong YOLOv8 baseline under severe ego-motion. Ablation studies further confirm the effectiveness of the dual-interval design and the proposed motion-guided attention mechanism.

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

《AgroTools: A Benchmark for Tool-Augmented Multimodal Agents in Agriculture》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgroBench, MCP-AgentBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agricultural decision-making increasingly requires multimodal systems that can transform visual observations into reliable, executable actions. However, existing agricultural multimodal benchmarks mainly evaluate final-answer correctness and provide limited support for assessing whether models can use external tools to complete precision-sensitive workflows. In this paper, we introduce AgroTools, a benchmark for evaluating tool-augmented multimodal agents in agriculture. AgroTools contains 539 question-answer instances paired with 1,097 heterogeneous agricultural images, spanning five task families and an executable environment of 14 agricultural tools. Each query is annotated with structured tool-use traces, enabling a dual-view evaluation of both process-level execution quality and outcome-level task success. We benchmark 9 open-source and 4 closed-source multimodal large language models on AgroTools. Results show that current models remain far from reliable in agricultural tool-use settings, with clear bottlenecks in tool planning, argument generation, execution recovery, and final-answer synthesis. We hope AgroTools will support future research on multimodal agents for high-precision agricultural applications. The benchmark and evaluation are available at https://huggingface.co/datasets/AgroTools/AgroTools.

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

《Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Whole-body Humanoid-Object Interaction (HOI) is bottlenecked by the scarcity of high-fidelity 3D data. While video generative priors offer a promising alternative, existing methods suffer from \textit{Representation Misalignment} due to their reliance on geometric priors (e.g., explicit CAD models), and \textit{Retargeting Complexity} arising from intensive morphing and morphological mismatch. We propose Imagine2Real, a zero-shot HOI framework for flexible, geometry-free interaction. To resolve misalignment, we formulate robot and object motions as unified 4D point trajectories. To overcome retargeting complexity, our Keypoints Tracker tracks only sparse critical points (base, hands, and object), entirely bypassing the error-amplifying retargeting process. To maintain natural gaits despite these sparse signals, we utilize the latent space of a Behavior Foundation Model (BFM) as the tracker's search domain. Using a progressive training strategy, Imagine2Real learns robust behaviors with simple tracking rewards, enabling zero-shot physical deployment within a motion capture(mocap) system.

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

《EvoIR-Agent: Self-Evolving Image Restoration Agentic System via Experience-Driven Learning》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal Large Language Model (MLLM)-driven image restoration agent demonstrates effectiveness in degradation coupling scenarios by flexibly selecting tools and determining removal orders. However, their zero-shot planning often fails without experience, necessitating severe trial-and-error overhead to achieve satisfactory outcomes. Currently, two paradigms are employed to address this issue, yet a dilemma persists: Training-based methods embed intrinsic experience into parameters, achieving high inference efficiency but lacking compatibility with new tools or degradation. In contrast, training-free methods utilize explicit experience storage for compatibility but still incur trial-and-error overhead due to naive experience. To resolve the dilemma, we propose EvoIR-Agent, which first systematically formulates the experience components of a training-free image restoration agent. Subsequently, a hierarchical experience pool is constructed, which enables coarse-to-fine guidance for diverse tools and removal orders. Furthermore, a self-evolving mechanism is introduced to update the pool from scratch using accumulated records, thereby greatly improving performance and efficiency. Extensive experiments reveal that EvoIR-Agent achieves a significant lead in the full reference metrics and yields a remarkable Pareto-optimal balance between performance and efficiency compared to the state-of-the-art methods.

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

《SceneGraphGrounder: Zero-Shot 3D Visual Grounding via Structured Scene Graph Matching》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Zero-shot 3D visual grounding requires localizing objects in unstructured environments from free-form natural language. Recent vision-language model (VLM) approaches achieve promising results but rely on view-dependent reasoning or implicit representations, limiting spatial consistency and interpretability for compositional queries. We propose SceneGraphGrounder, a framework that reformulates 3D grounding as structured graph matching over a reconstructed 3D scene graph. To enable this formulation, we introduce a visual marker prompting strategy that enables a VLM to infer object-object relationships from 2D views, which are subsequently lifted into a persistent 3D scene graph encoding both spatial and semantic relations. Given a query, we construct a query graph and perform constrained alignment with the scene graph, ensuring multi-view consistency and interpretable reasoning. Experiments on the ScanRefer benchmark demonstrate that our method achieves competitive performance among zero-shot approaches, using only RGB-D inputs. We further validate our framework through real-world deployment on a mobile robot, demonstrating robust spatial reasoning in long-horizon physical environments. We will make our code publicly available upon acceptance.

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

《PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PhysX-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation-ready physical 3D assets have emerged as a promising direction owing to their broad applicability in downstream tasks. However, most existing 3D generation methods either neglect physical properties or are limited to a single asset category, e.g., rigid, deformable, or articulated objects. To address these limitations, we introduce PhysX-Omni, a unified framework for simulation-ready physical 3D generation across diverse asset types. Specifically, we develop a novel and efficient geometry representation tailored for Vision-Language Models, which directly encodes high-resolution 3D structures without compression, significantly improving generation performance. In addition, we construct the first general simulation-ready 3D dataset, PhysXVerse, covering diverse indoor and outdoor categories. Furthermore, to comprehensively and flexibly evaluate both generative and understanding capabilities in the wild, we propose PhysX-Bench, which encompasses six key attributes: geometry, absolute scale, material, affordance, kinematics, and function description. Extensive experiments with conventional metrics and PhysX-Bench show that PhysX-Omni performs strongly in both generation and understanding. Moreover, additional studies further validate the potential of PhysX-Omni for applications in simulation-ready scene generation and robotic policy learning. We believe PhysX-Omni can significantly advance a wide range of downstream applications, particularly in embodied AI and physics-based simulation.

</details>

---
