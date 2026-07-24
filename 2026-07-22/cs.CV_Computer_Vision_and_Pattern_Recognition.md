# cs.CV | Computer Vision and Pattern Recognition | 2026-07-22

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/强化学习/Masked_Visual_Actions_for_Unified_World_Modeling|Masked Visual Actions for Unified World Modeling]]

![[assets/2607.19343_figure.png|800]]

- **arXiv**: [2607.19343](https://arxiv.org/abs/2607.19343)
- **PDF**: https://arxiv.org/pdf/2607.19343
- **详细分析**: [[20_Research/Papers/强化学习/Masked_Visual_Actions_for_Unified_World_Modeling|Masked Visual Actions for Unified World Modeling]]
- **作者**: Hadi Alzayer, Wenlong Huang, Haonan Chen, Christopher Luey, Lvmin Zhang, Maneesh Agrawala, Gordon Wetzstein, Li Fei-Fei, Yilun Du, Jiajun Wu, Jia-Bin Huang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.2（加权：具身智能 0.3，世界模型 0.2，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Masked Visual Actions for Unified World Modeling》归入 机器人、具身智能、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video models absorb rich priors over how the visual world moves, interacts, and responds to contact, making them promising substrates for robotic world modeling. The central challenge is how to communicate action to such models in a form aligned with the visual space in which they learned these interaction priors, yet still grounded in physical manipulation. We introduce Masked Visual Actions, a pixel-space control interface that expresses action as a partially revealed trajectory of an arbitrary entity in a video. Revealing robot motion makes the model act as a forward dynamics model that predicts the scene's response to low-level robot actions, while revealing desired object motion makes the same model recover robot behavior consistent with that outcome. Finetuned with only 15 hours of masked examples from real videos and simulation, a single checkpoint achieves strong visual fidelity and controllability across diverse scenes and multiple embodiments. In downstream manipulation settings, the model produces imagined rollouts whose outcomes correlate with real-world execution for policy evaluation, improves decision making by ranking candidate futures in model-based planning, and supports inverse modeling by synthesizing robot motion from desired object motion.

</details>

---

### [[20_Research/Papers/具身智能/No_Training,_Better_Flights_Test-Time_Scaled_VLMs_for_UAV_Navigation|No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation]]

![[assets/2607.19288_first_page.png|800]]

- **arXiv**: [2607.19288](https://arxiv.org/abs/2607.19288)
- **PDF**: https://arxiv.org/pdf/2607.19288
- **详细分析**: [[20_Research/Papers/具身智能/No_Training,_Better_Flights_Test-Time_Scaled_VLMs_for_UAV_Navigation|No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation]]
- **作者**: Feinan Cheng, Dongliang Xu, Wenli Nong, Zhiheng Zhang, Ang Liu, Tianyu Wang, Yue Yao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-time scaling offers a promising method to improve the inference performance of Vision-Language Models (VLMs) without additional training. Existing approaches to vision-language navigation (VLN) for Unmanned Aerial Vehicle (UAV) typically relies on a single inference pass, which can falter in complex environments by producing suboptimal or unsafe trajectories. In this paper, we explore a simple and effective approach to apply test-time scaling to VLN for UAV. We enhance navigation reasoning through an iterative refinement process that requires no extra model training, guiding the model to re-evaluate its initial navigation plan for better accuracy and safety. Our method first prompts the model to generate multiple parallel candidates and then performs a self-correction step, achieving deeper and more robust planning without changing the underlying model. To further strengthen decision-making, we design a multi-criteria scoring function to evaluate the refined candidates based on safety, goal alignment, and forward-progress. This simple yet powerful combination enables a frozen UAV navigation VLMs to self-correct and generate more accurate and reliable flight plans, achieving SOTA performance in this task.

</details>

---

### [[20_Research/Papers/机器人/Gaze-DETR_Top-Down_Guidance_Through_Priority_Maps_for_Infrared_Weak-Small_UAV_Detection_with_DETR|Gaze-DETR: Top-Down Guidance Through Priority Maps for Infrared Weak-Small UAV Detection with DETR]]

![[assets/2607.19040_figure.png|800]]

- **arXiv**: [2607.19040](https://arxiv.org/abs/2607.19040)
- **PDF**: https://arxiv.org/pdf/2607.19040
- **详细分析**: [[20_Research/Papers/机器人/Gaze-DETR_Top-Down_Guidance_Through_Priority_Maps_for_Infrared_Weak-Small_UAV_Detection_with_DETR|Gaze-DETR: Top-Down Guidance Through Priority Maps for Infrared Weak-Small UAV Detection with DETR]]
- **作者**: Nian Liu, Yuxin Yang, Shubo Lin, Sikui Zhang, Liang Li, Boyu Cai, Yizheng Wang, Weiming Hu, Jin Gao
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.6（加权：机器人 0.6）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Gaze-DETR: Top-Down Guidance Through Priority Maps for Infrared Weak-Small UAV Detection with DETR》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALCNet, DNA-Net, ISNet, L2SKNet, MSHNet, SCTransNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Infrared small target detection (ISTD) remains challenging because tiny, low-contrast targets are easily overwhelmed by clutter, noise, or occlusion. Conventional single-frame and multi-frame detectors rely on bounding-box supervision, which specifies final target locations but offers little explicit guidance for prioritizing candidate regions or preserving weak-target evidence before localization. Task-driven visual search offers such guidance: top-down goals and visual evidence jointly form a spatial priority map that ranks candidate locations. Building on this principle, we propose Gaze-DETR, a bio-inspired detector that learns an internal priority map before localization. First, a priority head predicts a normalized priority map from image features. Second, Residual Priority-Guided Feature Modulation (RPFM) enhances high-priority responses while retaining multi-scale features. Finally, Priority-Guided Anchor Query Injection (PAQI) converts high-priority locations into decoder anchor queries. We train the priority head using three supervision schemes: box-derived Gaussian maps; real-gaze maps constructed from fixation-density maps; and transferred pseudo-gaze maps learned from gaze--box relations in paired annotations and applied to Anti-UAV410 training boxes. To support the latter two schemes, we construct TIR-UAV120-Gaze with paired detection and task-driven eye-tracking annotations. On TIR-UAV120-Gaze, Gaze-DETR achieves 85.76 mAP$_{50}$ and 88.77 F1 with box-derived supervision, and 86.18 mAP$_{50}$ and 89.00 F1 with real-gaze supervision. On Anti-UAV410, it achieves 87.06 mAP$_{50}$ and 90.90 F1 with box-derived supervision, and 87.08 mAP$_{50}$ and 90.43 F1 with transferred pseudo-gaze supervision. These results show that explicit spatial-priority learning provides pre-localization guidance complementary to bounding-box supervision across annotation settings and costs.

</details>

---

### [[20_Research/Papers/大模型/DobicVLM_Aligning_Chest_X-Ray_Report_Generation_with_Clinically-Grounded_Programmatic_Rewards_via_Group_Relative_Policy_Optimization|DobicVLM: Aligning Chest X-Ray Report Generation with Clinically-Grounded Programmatic Rewards via Group Relative Policy Optimization]]

![[assets/2607.18988_figure.png|800]]

- **arXiv**: [2607.18988](https://arxiv.org/abs/2607.18988)
- **PDF**: https://arxiv.org/pdf/2607.18988
- **详细分析**: [[20_Research/Papers/大模型/DobicVLM_Aligning_Chest_X-Ray_Report_Generation_with_Clinically-Grounded_Programmatic_Rewards_via_Group_Relative_Policy_Optimization|DobicVLM: Aligning Chest X-Ray Report Generation with Clinically-Grounded Programmatic Rewards via Group Relative Policy Optimization]]
- **作者**: Thanni Adewuyi, Angelica Obayi, Andem Aniekan, Samuel Okoko, Angel Ezendu, Ephraim Usani, Ademide Animasaun, Philip Chibundu, Christian Maurice, Mary Donald Essien, Oluwaseun Odunsi, Oluwasegun Oguntuase...
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.2，强化学习 1）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《DobicVLM: Aligning Chest X-Ray Report Generation with Clinically-Grounded Programmatic Rewards via Group Relative Policy Optimization》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Medical imaging is a cornerstone of diagnostics, yet automated chest X-ray report generation struggles with structural adherence, anatomical completeness, and semantic faithfulness. We introduce DobicVLM, a vision-language model combining supervised fine-tuning on MedGemma-4B with Group Relative Policy Optimization (GRPO) and clinically-grounded programmatic rewards. Our approach uses interpretable, rule-based reward components; structural verification, anatomical checklist, semantic similarity, and length constraints to enforce clinical standards without neural reward models. Trained on 1,000 de-identified image-report pairs from a private clinical dataset (with ethics approval and compliance to local regulations), DobicVLM is evaluated via blinded expert review on 69 held-out cases. DobicVLM outperforms Gemini 2.5 Flash across the majority of criteria, achieving the highest impression accuracy (27.2%) and medical terminology (86.5%) compared to both Gemini 2.5 Flash and MedGemma 4B baselines, with minor trade-offs in completeness and referrals. This demonstrates GRPO's value for transparent alignment in resource-limited settings. Keywords: Vision-Language Models, Radiology Report Generation, Reinforcement Learning, Medical AI, GRPO

</details>

---

### [[20_Research/Papers/大模型/TAP-RAG_Task-Aware_Policy_Control_for_Long-Document_Multimodal_Question_Answering|TAP-RAG: Task-Aware Policy Control for Long-Document Multimodal Question Answering]]

![[assets/2607.18917_figure.png|800]]

- **arXiv**: [2607.18917](https://arxiv.org/abs/2607.18917)
- **PDF**: https://arxiv.org/pdf/2607.18917
- **详细分析**: [[20_Research/Papers/大模型/TAP-RAG_Task-Aware_Policy_Control_for_Long-Document_Multimodal_Question_Answering|TAP-RAG: Task-Aware Policy Control for Long-Document Multimodal Question Answering]]
- **作者**: Zhong Ji, Keqi Jin, Yan Zhang, Jiasheng Li
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《TAP-RAG: Task-Aware Policy Control for Long-Document Multimodal Question Answering》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DocBench, MMLongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-document multimodal question answering requires more than retrieving relevant chunks from a large document. Different queries require different evidence behavior. Existing multimodal RAG systems improve evidence access through text chunks, page images, graph links, or heterogeneous document elements, but they often apply a largely query-agnostic evidence-use strategy. We present TAP-RAG, a task-aware policy-controlled RAG framework for long-document multimodal QA. TAP-RAG contains a main controller, the Task-Aware Policy Controller (TAPC), and two policy-guided evidence executors: Task-Aware Query-Guided Flow Diffusion (TA-QFD) and Task-Aware Visual Enhancement (TAVE). For each query, TAPC predicts the task prior, estimates visual/local/global evidence signals, and produces an executable policy. TA-QFD then expands textual and structural evidence over the multimodal document graph, while TAVE selectively inspects page images when visual or layout evidence is needed. A guarded synthesis stage fuses text, visual, and structural evidence and abstains when support is insufficient. On DocBench and MMLongBench-Doc, TAP-RAG achieves the best overall accuracy among the compared systems, improving over a matched multimodal-RAG baseline by +9.1 points (61.1 to 70.2) and +4.5 points (42.2 to 46.7), respectively.

</details>

---

### [[20_Research/Papers/机器人/CGMap_A_Geospatially_Aware_Deep_Learning_Framework_for_Crop_Gap_Mapping_Using_UAV|CGMap: A Geospatially Aware Deep Learning Framework for Crop Gap Mapping Using UAV]]

![[assets/2607.18779_figure.png|800]]

- **arXiv**: [2607.18779](https://arxiv.org/abs/2607.18779)
- **PDF**: https://arxiv.org/pdf/2607.18779
- **详细分析**: [[20_Research/Papers/机器人/CGMap_A_Geospatially_Aware_Deep_Learning_Framework_for_Crop_Gap_Mapping_Using_UAV|CGMap: A Geospatially Aware Deep Learning Framework for Crop Gap Mapping Using UAV]]
- **作者**: Karan Sharma, Rajiv Ranjan, Dinesh Kumar, Shashank Tamaskar
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《CGMap: A Geospatially Aware Deep Learning Framework for Crop Gap Mapping Using UAV》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In India, crop germination is primarily monitored by visual inspection and manual counting, which are prone to errors, despite their crucial role in determining eventual yield potential. This paper highlights a deep learning based pipeline which uses object detection methods and drone imagery to assess and provide a precise count of sugarcane germination in fields. The approch uses a pre-trained AI model to find germinated plant sampling and identify gaps, also known as ``bald spots'', which restricts field productivity. The techniques used here relies on the YOLOV8 architecture, which was trained on a carefully selected dataset of UAV photos taken in various agroclimatic zones of India. Here, we bring upon a novel orientation-normalization technique that uses minimum Spanning Trees (MST) to account for variations in planting geometry, allowing for dependable row and column extraction across a variety of field layouts. By converting detected seedlings into spatial point clouds, emergence gaps can be inferred from the anticipated spacing between plants. A geospatial germination map exported in Well-Known Text (WKT) format is the end result, and it can be easily incorporated into GIS platforms used by sugar mills and agronomists to direct transplant initiatives. Timely interventions based on the insights provided by the algorithm can significantly increase yield, resulting in higher profits. Hence, support proper allocation of resources, avoid wastage, and enhance long-term sustainability.

</details>

---

### [[20_Research/Papers/机器人/Cross-Modal_UAV_Object_Tracking_State-Aware_Representation_Learning_and_A_Unified_Benchmark|Cross-Modal UAV Object Tracking: State-Aware Representation Learning and A Unified Benchmark]]

![[assets/2607.18768_figure.png|800]]

- **arXiv**: [2607.18768](https://arxiv.org/abs/2607.18768)
- **PDF**: https://arxiv.org/pdf/2607.18768
- **详细分析**: [[20_Research/Papers/机器人/Cross-Modal_UAV_Object_Tracking_State-Aware_Representation_Learning_and_A_Unified_Benchmark|Cross-Modal UAV Object Tracking: State-Aware Representation Learning and A Unified Benchmark]]
- **作者**: Yun Xiao, Zhihong Hong, Jiandong Jin, Chenglong Li, Jin Tang, Amir Hussain
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Cross-Modal UAV Object Tracking: State-Aware Representation Learning and A Unified Benchmark》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MAFNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned Aerial Vehicle (UAV) object tracking has emerged as a popular research field with broad practical applications. Modern UAVs are increasingly equipped with both visible light and thermal infrared sensors. However, due to constraints in communication bandwidth, computational resources and power consumption, current systems often activate one modality and switch between modalities to maintain robust tracking in complex scenarios. Such modality switch inevitably leads to significant appearance change and sudden spatial shift, posing great challenges for existing tracking algorithms. To handle this problem, we propose a novel State-Aware Representation Learning Approach called SARLA, which perceives the inconsistent modality states of current frame with template and last frame in the target representations to adapt to the sudden changes in both appearance and position, for robust cross-modal object tracking. In particular, we propose the Modality State Aware Representation Module (MSARM) and Spatial State Aware Representation Module (SSARM). MSARM guides the model to learn appearance correlation, bridging the modality gap, while SSARM models cross-frame spatial correlation to mitigate sudden spatial shift impacts. In addition, we design a spatial shift prediction loss to further handle the effects of spatial variation caused by modality switch. To promote the development of this research field, we establish a large-scale video benchmark called CM-UOT, which consists of 1079 cross-modal sequences with an average video length greater than 621 frames and encompasses over 671K frames in total. Extensive experiments on CM-UOT dataset demonstrate the superior performance of the proposed SARLA against 20 excellent tracking methods. The source code, datasets, and evaluation protocols associated with this work are publicly available at: https://github.com/hongsmile365/sarla-.

</details>

---

### [[20_Research/Papers/机器人/SkyEV_RGB-Event_UAV_detection_and_tracking_dataset_and_baseline|SkyEV: RGB-Event UAV detection and tracking dataset and baseline]]

![[assets/2607.18747_figure.png|800]]

- **arXiv**: [2607.18747](https://arxiv.org/abs/2607.18747)
- **PDF**: https://arxiv.org/pdf/2607.18747
- **详细分析**: [[20_Research/Papers/机器人/SkyEV_RGB-Event_UAV_detection_and_tracking_dataset_and_baseline|SkyEV: RGB-Event UAV detection and tracking dataset and baseline]]
- **作者**: Jakub Mandula, Sebastian Heusinger, Julian Moosmann, Christian Vogt, Michele Magno
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《SkyEV: RGB-Event UAV detection and tracking dataset and baseline》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Detecting UAVs in air spaces has become increasingly important due to UAVs widespread availability and easy usage. However, due to their small size, they are typically difficult to detect at a sufficient range. For the training of optimized detection algorithms, datasets have been published, covering optical sensing methods ranging from infrared to regular RGB to event-sensor-based. However, these datasets often fail to reflect realistic counter-UAV scenarios, lacking critical factors such as camera ego-motion, extremely small target scales, and diverse lens configurations, and introduce compression artefacts on the frame images. To address this gap, we introduce SkyEV, an open-source dataset featuring highly synchronized uncompressed RGB and event-based data. SkyEV distinguishes itself by capturing complex real-world conditions, including significant camera motion and varied optical setups, which are essential for testing the fundamental trade-off between Field of View and detection range. Furthermore, we provide a unified data loader and establish an experimental baseline using a multi-modal architecture, demonstrating the dataset's efficacy in detecting challenging, small-scale targets.

</details>

---

### [[20_Research/Papers/强化学习/Confidence-Gated_Vision-Only_Heading_Alignment_for_UAV-UGV_Cooperative_Systems|Confidence-Gated Vision-Only Heading Alignment for UAV-UGV Cooperative Systems]]

![[assets/2607.18713_figure.png|800]]

- **arXiv**: [2607.18713](https://arxiv.org/abs/2607.18713)
- **PDF**: https://arxiv.org/pdf/2607.18713
- **详细分析**: [[20_Research/Papers/强化学习/Confidence-Gated_Vision-Only_Heading_Alignment_for_UAV-UGV_Cooperative_Systems|Confidence-Gated Vision-Only Heading Alignment for UAV-UGV Cooperative Systems]]
- **作者**: Reza Ahmari, Vahid Hemmati, Parham Kebria, Olusola Odeyomi, Kaushik Roy, Abdollah Homaifar
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: RL

#### 研究背景与动机

《Confidence-Gated Vision-Only Heading Alignment for UAV-UGV Cooperative Systems》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based heading prediction is useful for UAV--UGV cooperation, but accurate prediction alone does not guarantee that every predicted heading should be issued directly as a control command. This paper investigates the decision problem of when and how a fixed vision-based heading predictor should be trusted for command issuance. A lightweight confidence-gated framework is proposed in which execution decisions are made using two interpretable reliability proxies derived from the perception stream: bounding-box area as a visibility-related proxy and short-window variation in predicted heading as a stability-related proxy. During low-confidence intervals, the framework compares the baseline freeze-HOLD policy with a bounded-blend fallback that updates the issued command conservatively. The method is evaluated on a real UAV--UGV dataset under clean and perturbed conditions. The results show that confidence gating creates a clear trade-off among execution rate, executed-frame accuracy, issued-command accuracy, and smoothness. The results further show that sparse execution can cause severe stale-command error under the baseline freeze-HOLD policy, whereas the bounded-blend fallback substantially improves command-level behavior under the same gate decisions. These findings highlight that reliable perception-driven autonomy depends not only on prediction accuracy, but also on decision-aware command issuance during low-confidence

</details>

---

### [[20_Research/Papers/机器人/Recti-Q_Feature-Space_Rectification_for_Out-of-Distribution-Robust_Quantized_Perception_in_Edge_Robotics|Recti-Q: Feature-Space Rectification for Out-of-Distribution-Robust Quantized Perception in Edge Robotics]]

![[assets/2607.18540_figure.png|800]]

- **arXiv**: [2607.18540](https://arxiv.org/abs/2607.18540)
- **PDF**: https://arxiv.org/pdf/2607.18540
- **详细分析**: [[20_Research/Papers/机器人/Recti-Q_Feature-Space_Rectification_for_Out-of-Distribution-Robust_Quantized_Perception_in_Edge_Robotics|Recti-Q: Feature-Space Rectification for Out-of-Distribution-Robust Quantized Perception in Edge Robotics]]
- **作者**: Hamidreza Yaghoubi Araghi, Parastoo Pilevar, Ming C. Lin
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Recti-Q: Feature-Space Rectification for Out-of-Distribution-Robust Quantized Perception in Edge Robotics》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic perception pipelines increasingly rely on large vision backbones deployed on SWaP-constrained edge platforms, making post-training quantization (PTQ) attractive for real-time inference. However, while PTQ often preserves clean in-distribution accuracy, we show that it can substantially degrade reliability under deployment-relevant distribution shifts (e.g., sensor noise, severe weather, and novel operating environments), creating a Quantization-Induced Robustness Gap. Across foundational vision benchmarks (ImageNet-C and PACS), 4-bit PTQ models exhibit pronounced robustness degradation despite negligible ID accuracy loss. To address this, we propose Recti-Q, a lightweight feature-space rectification framework that freezes the quantized backbone and trains a small classifier-head LoRA adapter using only source data. Recti-Q is architecture-agnostic across CNNs and Transformers, supports efficient teacher-free training, and recovers a significant portion of the lost robustness, in some cases matching or exceeding FP32 performance. At less than 1% parameter overhead (as small as 6 KB), Recti-Q preserves over 99% of PTQ memory savings, adds negligible compute, and enables low-bandwidth Over-The-Air (OTA) resilience patching for deployed robotic fleets operating in unpredictable physical environments.

</details>

---
