# cs.CV | Computer Vision and Pattern Recognition | 2026-09-16

#arxiv #ComputerScience

**论文数**: 16

### [[20_Research/Papers/世界模型/SlotDiT_Object-Centric_Representations_for_Diffusion_Transformers|SlotDiT: Object-Centric Representations for Diffusion Transformers]]

![[assets/2609.17414_first_page.png|800]]

- **arXiv**: [2609.17414](https://arxiv.org/abs/2609.17414)
- **PDF**: https://arxiv.org/pdf/2609.17414
- **详细分析**: [[20_Research/Papers/世界模型/SlotDiT_Object-Centric_Representations_for_Diffusion_Transformers|SlotDiT: Object-Centric Representations for Diffusion Transformers]]
- **作者**: Gjergj Plepi, Sven Behnke
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《SlotDiT: Object-Centric Representations for Diffusion Transformers》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Text-conditioned latent diffusion models perform strongly in video generation and are promising backbones for robotic applications. However, existing approaches rely on pixel-level or VAE-based latent representations that lack explicit semantic structure, leaving the impact of the representation space largely unexplored. Slot-based object-centric representations offer a structured alternative by decomposing scenes into object-level latents, or slots. While they have shown success in dynamics modeling and planning, they have not yet been explored for diffusion-based generative modeling. We introduce SlotDiT, a text-guided Diffusion Transformer (DiT) that operates in a slot-based latent space. Given a reference image and a language instruction, SlotDiT decomposes the scene into object-centric slots representing individual entities. Conditioned on the instruction and observed scene context, the model autoregressively denoises future slot trajectories to predict scene dynamics. To systematically investigate latent-space design for diffusion transformers, we compare slot-based representations against VAE-based and semantics-aligned alternatives within a unified DiT framework. Our experiments show that using slots as DiT latents yields competitive video generation quality while consistently improving task-completion rates across four robotic datasets. Furthermore, their compact representation provides a computationally efficient alternative to VAE-based and semantics-aligned latent spaces. Overall, our results demonstrate that object-centric structure is a powerful inductive bias for diffusion-based generative modeling in robotic environments. The project page is available at this https URL .

</details>

---

### [[20_Research/Papers/机器人/PanoGS-SLAM_Panoramic_3D_Gaussian_Splatting_SLAM|PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM]]

![[assets/2609.17387_figure.png|800]]

- **arXiv**: [2609.17387](https://arxiv.org/abs/2609.17387)
- **PDF**: https://arxiv.org/pdf/2609.17387
- **详细分析**: [[20_Research/Papers/机器人/PanoGS-SLAM_Panoramic_3D_Gaussian_Splatting_SLAM|PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM]]
- **作者**: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-time dense SLAM is a core capability for robotics applications that require robust localization and high- quality mapping in dynamic or fast-changing environments. Recent 3D Gaussian Splatting (3DGS)-based SLAM methods have shown promising performance, but most are designed for narrow-FoV pinhole cameras, where limited angular coverage weakens pose observability and often leads to unstable photo- metric optimization under rapid motion and large viewpoint changes. We present PanoGS-SLAM, the first panoramic dense SLAM system built on 3D Gaussian Splatting. Our method per- forms differentiable rendering and pose optimization directly in the spherical domain, enabling omnidirectional photometric constraints for more stable tracking. To improve geometric consistency and robustness, we introduce (1) a sphere-consistent photometric loss that compensates for the area distortion of equirectangular projection, and (2) a depth-guided Gaussian initialization strategy that stabilizes incremental mapping in newly observed regions. Extensive experiments on both real and synthetic panoramic benchmarks (PALVIO and SynPano) show that PanoGS-SLAM consistently outperforms geometric and GS-based baselines in tracking accuracy and rendering quality, while achieving fast front-end convergence and real-time perfor- mance. In addition, controlled field-of-view experiments reveal a clear monotonic improvement in optimization conditioning and convergence stability as angular coverage increases, high- lighting the fundamental role of sensing geometry in shaping the optimization landscape of differentiable Gaussian-based SLAM. The source code will be made publicly available.

</details>

---

### [[20_Research/Papers/机器人/HuMemSLAM_Efficient_Human-Inspired_Semantic_Place_Recognition_for_Robust_Visual_SLAM|HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM]]

![[assets/2609.17168_figure.png|800]]

- **arXiv**: [2609.17168](https://arxiv.org/abs/2609.17168)
- **PDF**: https://arxiv.org/pdf/2609.17168
- **详细分析**: [[20_Research/Papers/机器人/HuMemSLAM_Efficient_Human-Inspired_Semantic_Place_Recognition_for_Robust_Visual_SLAM|HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM]]
- **作者**: Mayowa Adebambo, Sebastian Donnelly, Armand Amaritei, Andrew Bradley, Alexander Rast
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OSRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous systems require reliable place recognition for efficient and effective simultaneous localisation and mapping (SLAM). Traditional geometric visual SLAM approaches rely on low-level features and geometric consistency, but remain vulnerable to perceptual aliasing, where different places appear similar, and perceptual variation, where the same place appears different. Although semantic SLAM and modern learned visual place recognition (VPR) methods improve robustness under challenging perceptual conditions, real-time deployment requires both high retrieval accuracy and low latency. Inspired by human memory and perception, we propose HuMem-VPR, which exploits the bidirectional relationship between bottom-up perceptual evidence and top-down contextual reasoning to achieve high-level place understanding. We further introduce HuMemSLAM, the integration of HuMem-VPR with ORB-SLAM3. HuMem VPR achieved the highest aggregate retrieval accuracy on the real-image benchmark, competitive accuracy on the CARLA benchmark, and approximately two to three times lower latency than the evaluated state-of-the-art VPR methods. Across the evaluated dataset families and online experiments, HuMemSLAM substantially improved integrated Recall @1 over ORB-SLAM3's native retrieval while reducing the proposals submitted to its geometric backend.

</details>

---

### [[20_Research/Papers/具身智能/GeoLAM_Learning_Geometry-Grounded_Latent_Actions_from_Unlabeled_Human_Videos|GeoLAM: Learning Geometry-Grounded Latent Actions from Unlabeled Human Videos]]

![[assets/2609.17099_figure.png|800]]

- **arXiv**: [2609.17099](https://arxiv.org/abs/2609.17099)
- **PDF**: https://arxiv.org/pdf/2609.17099
- **详细分析**: [[20_Research/Papers/具身智能/GeoLAM_Learning_Geometry-Grounded_Latent_Actions_from_Unlabeled_Human_Videos|GeoLAM: Learning Geometry-Grounded Latent Actions from Unlabeled Human Videos]]
- **作者**: Yifan Xie, Hekun Tian, Jinkun Liu, YuAn Wang, Qiao Sun, Wenbo Ding
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《GeoLAM: Learning Geometry-Grounded Latent Actions from Unlabeled Human Videos》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LARYBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human videos provide rich manipulation experience, but extracting action representations that preserve useful motion remains challenging. Visual reconstruction alone can entangle manipulation-related motion with appearance changes and camera movement. We present GeoLAM, a framework for learning geometry-grounded latent actions from action-free human videos. GeoLAM combines future-frame reconstruction through a frozen geometric feature hierarchy with motion supervision from a training-only 4D geometry teacher. The geometric representation provides a structural prior, while the teacher's predictions yield spatially pooled targets capturing 3D displacement, residual image-plane motion, and surface-orientation changes. Visibility and confidence weighting reduces the contribution of unreliable estimates, encouraging continuous latent actions to retain geometric motion without explicit hand-pose or hand-trajectory annotations. After video pretraining without action labels, the learned representation provides transition targets for a world-action model trained on action-labeled robot demonstrations. The model jointly denoises latent actions and executable action chunks, with future-video prediction used only as an auxiliary training task. Deployment therefore requires neither the geometry teacher nor future-video generation. Evaluations on a latent-action benchmark and robotic manipulation tasks demonstrate the strong performance of GeoLAM.

</details>

---

### [[20_Research/Papers/具身智能/sensVLA_Spatially-Grounded_Vision-Language-Action_Model_for_Autonomous_Wheel_Loader|sensVLA: Spatially-Grounded Vision-Language-Action Model for Autonomous Wheel Loader]]

![[assets/2609.17021_figure.png|800]]

- **arXiv**: [2609.17021](https://arxiv.org/abs/2609.17021)
- **PDF**: https://arxiv.org/pdf/2609.17021
- **详细分析**: [[20_Research/Papers/具身智能/sensVLA_Spatially-Grounded_Vision-Language-Action_Model_for_Autonomous_Wheel_Loader|sensVLA: Spatially-Grounded Vision-Language-Action Model for Autonomous Wheel Loader]]
- **作者**: Gopi Krishna Erabati, Bjarne Johannsen, Angus Stewart, Vardeep Singh Sandhu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.3，机器人 0.3）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《sensVLA: Spatially-Grounded Vision-Language-Action Model for Autonomous Wheel Loader》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous wheel-loader control requires joint reasoning over task semantics, egocentric vision, proprioception, and 3D scene geometry. We present sensVLA, a Vision-Language-Action (VLA) architecture that combines a Qwen3-2B Vision-Language Model (VLM) with a fully trainable transformer action expert trained by flow-matching velocity regression. sensVLA routes Bird's-Eye-View (BEV) features, extracted from fused front and rear lidar, directly to the action expert through a dedicated cross-attention pathway, while the VLM consumes front and rear RGB views to provide task-conditioned semantic context. This design decouples spatial grounding from linguistic reasoning while preserving interaction between both streams at decision time. The expert predicts six action dimensions: longitudinal velocity, steering, body-frame displacement, arm rate, and bucket rate. On a real-world dataset from a wheel loader, sensVLA reaches aggregate per-step parity with a strong camera-only baseline and reduces longitudinal velocity RMSE by 28% and displacement error by 9% on loading centric scenarios. It also degrades 29% less when the camera stream is corrupted or removed, evidencing that explicit spatial grounding improves accuracy and fault-tolerance for heavy equipment autonomy.

</details>

---

### [[20_Research/Papers/具身智能/NeuroSymbEAD_A_Large_Scale_Neuro-Symbolic_Caption_Dataset_for_Omni-Directional_Embodied_Autonomous_Driving|NeuroSymbEAD: A Large Scale Neuro-Symbolic Caption Dataset for Omni-Directional Embodied Autonomous Driving]]

![[assets/2609.16919_figure.png|800]]

- **arXiv**: [2609.16919](https://arxiv.org/abs/2609.16919)
- **PDF**: https://arxiv.org/pdf/2609.16919
- **详细分析**: [[20_Research/Papers/具身智能/NeuroSymbEAD_A_Large_Scale_Neuro-Symbolic_Caption_Dataset_for_Omni-Directional_Embodied_Autonomous_Driving|NeuroSymbEAD: A Large Scale Neuro-Symbolic Caption Dataset for Omni-Directional Embodied Autonomous Driving]]
- **作者**: Muhammad Ahmed Ullah Khan, Mohammed Elamine, Sheikh Talha Uddin, Didier Stricker, Sk Aziz Ali, Muhammad Zeshan Afzal
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 0.9（加权：具身智能 0.9）
- **关联关键词**: Multimodal, EmbodiedAI, ComputerVision

#### 研究背景与动机

《NeuroSymbEAD: A Large Scale Neuro-Symbolic Caption Dataset for Omni-Directional Embodied Autonomous Driving》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ActivityNet, ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper introduces NeuroSymbEAD, a large-scale neuro-symbolic caption dataset featuring an ego-centric knowledge graph (KG) of static and dynamic objects annotated with classes, categories, heading directions, orientations, and distances from the ego-vehicle. These annotations are used on the KITTI-360 dataset to generate multilevel textual captions representing a lightweight version of an ego-centric scene map. Outdoor scene-map reconstruction, visual recognition, and object grounding establish baselines for driving common sense and traffic/scene understanding. For these purposes, natural language-based grounded captioning of objects and their complex relationships is a widely adopted contextual representation for indoor scene tasks. Neuro-symbolic representations have proven effective in handling structured information for various computer vision and language applications. Our data annotation pipeline allows the generation of varied map segments, populating simulated or real objects within the bounding boxes predicted by any 3D object detection network, and building hierarchical text captions. We benchmark our neuro-symbolic and ontological caption generation using pre-trained grounding and learned auto-regressive captioning networks. By converting 3D driving scenes into structured ego-centric language, NeuroSymbEAD provides a benchmark for vision-language and foundation models for traffic-scene explanation, 3D reasoning, and interpretable autonomous-driving perception.

</details>

---

### [[20_Research/Papers/具身智能/TEMPO_Learning_Temporal_Context_for_Dynamic_Robot_Manipulation|TEMPO: Learning Temporal Context for Dynamic Robot Manipulation]]

![[assets/2609.16864_figure.png|800]]

- **arXiv**: [2609.16864](https://arxiv.org/abs/2609.16864)
- **PDF**: https://arxiv.org/pdf/2609.16864
- **详细分析**: [[20_Research/Papers/具身智能/TEMPO_Learning_Temporal_Context_for_Dynamic_Robot_Manipulation|TEMPO: Learning Temporal Context for Dynamic Robot Manipulation]]
- **作者**: Zhenyang Feng, Jimin Heo, Erik B. Sudderth, Unnat Jain
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.8，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《TEMPO: Learning Temporal Context for Dynamic Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DynamicVLA, MVBench, SmolVLA, TEMPO-Bench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have achieved impressive performance in quasi-static manipulation, but struggle in dynamic manipulation tasks because they operate on a single observation at inference time. We identify two representational failures that underlie this limitation. The first is motion ambiguity, where a single observation does not include scene dynamics and therefore cannot anticipate the future state of moving objects. The second is state aliasing, where visually similar observations from different points in a task require different actions. We argue that these failures persist regardless of model scale and inference latency, showing that the bottleneck is missing temporal context rather than model capacity. Based on this insight, we propose TEMPO, which augments a pretrained VLA with two temporal inputs: a motion summary extracted from a frozen video foundation model to resolve motion ambiguity and a compact proprioceptive history to resolve state aliasing. TEMPO requires no modification to the backbone and adds minimal compute overhead at training or deployment. Across four dynamic manipulation tasks, it improves Bottle Handover success from 44% to 74% and is the only method that solves state aliasing. Probing and ablation studies confirm that each temporal signal independently addresses its corresponding failure. We further release TEMPO-Bench, a benchmark of over 50k annotated frames for evaluating motion-aware robot perception in both regression and multiple-choice formats. Project Website: this https URL

</details>

---

### [[20_Research/Papers/机器人/Differentiable_Mesh_State_Estimation_via_Factor_Graph_Inference_for_Deformable_Object_Reconstruction|Differentiable Mesh State Estimation via Factor Graph Inference for Deformable Object Reconstruction]]

![[assets/2609.16686_figure.png|800]]

- **arXiv**: [2609.16686](https://arxiv.org/abs/2609.16686)
- **PDF**: https://arxiv.org/pdf/2609.16686
- **详细分析**: [[20_Research/Papers/机器人/Differentiable_Mesh_State_Estimation_via_Factor_Graph_Inference_for_Deformable_Object_Reconstruction|Differentiable Mesh State Estimation via Factor Graph Inference for Deformable Object Reconstruction]]
- **作者**: Lidia Al-Zogbi, Fangjie Li, Samuel Tobin, James Ferguson, Nithesh Kumar, Alejandro Chara, Kuan-I Chung, Mingxing Rao, Ayberk Acar, Susheela Sharma Stern, Robert Webster, Daniel Moyer...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Differentiable Mesh State Estimation via Factor Graph Inference for Deformable Object Reconstruction》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Estimating deformable object states remains a fundamental challenge in robotics and simulation. We propose a novel factor graph-based framework for probabilistic mesh state estimation of deformable objects. The method directly updates a tetrahedral mesh, a rich and physically-grounded representation of an environment, by combining physics priors, noisy sensor measurements, and temporal smoothness constraints within a unified probabilistic formulation. The estimation problem is posed as a nonlinear least-squares optimization and solved using Levenberg-Marquardt. Ex vivo central-airway obstruction experiments and simulations on deforming cube models demonstrate reliable and accurate reconstruction under both rigid motion and deformation, highlighting the potential of this probabilistic approach for principled, measurement-driven mesh state estimation in deformable object reconstruction.

</details>

---

### [[20_Research/Papers/机器人/Can_Knowledge_Transfer_Parameters_Be_Learned_LePoKet_for_Efficient_Robotic_Vision|Can Knowledge Transfer Parameters Be Learned? LePoKet for Efficient Robotic Vision]]

![[assets/2609.16637_first_page.png|800]]

- **arXiv**: [2609.16637](https://arxiv.org/abs/2609.16637)
- **PDF**: https://arxiv.org/pdf/2609.16637
- **详细分析**: [[20_Research/Papers/机器人/Can_Knowledge_Transfer_Parameters_Be_Learned_LePoKet_for_Efficient_Robotic_Vision|Can Knowledge Transfer Parameters Be Learned? LePoKet for Efficient Robotic Vision]]
- **作者**: Yanick C. Tchenko, Felix Mohr, Hicham Hadj-Abdelkader, Hedi Tabia
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Can Knowledge Transfer Parameters Be Learned? LePoKet for Efficient Robotic Vision》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Efficient perception is central to robotic systems operating under constrained computation, memory, and latency budgets. Knowledge transfer from larger pretrained models offers a practical route to stronger compact perception networks, but existing approaches commonly rely on fixed distillation objectives or manually designed interaction mechanisms. Building on Hereditary Knowledge Transfer (HKT), we propose LePoKet (Learnable Parameter Optimization for Knowledge Transfer), a structural transfer framework that embeds knowledge inheritance directly into the forward computation. LePoKet introduces a block-wise Extract-Transform-Mix interface whose interaction parameters are optimized jointly with the child network through a Learnable Genetic Attention (LGA) operator, without auxiliary distillation losses or temperature scaling. We first characterize the mechanism on CIFAR-10 and CIFAR-100 using ResNet parent-child pairs, obtaining relative error reductions of 24.57% and 25.1%, respectively, over standard child training. We then evaluate LePoKet for dense motion estimation by integrating it into a compact RAFT-based optical-flow model trained only on FlyingChairs and FlyingThings3D. LePoKet improves the compact RAFT baseline from 2.21 to 1.92 EPE on Sintel Clean, from 3.35 to 3.01 on Sintel Final, and from 7.51 to 6.39 on KITTI. A direct comparison with HKT further shows that LePoKet improves CIFAR-10 accuracy from 92.40% to 93.40% while achieving the best Sintel Final and KITTI errors among the evaluated compact transfer variants, with comparable performance on Sintel Clean. These results demonstrate that learnable structural transfer generalizes across recognition and motion perception tasks and provides a promising approach for efficient robotic vision.

</details>

---

### [[20_Research/Papers/大模型/SAVOR_Self-Aware_Visual_Grounding_via_Confidence-Calibrated_Reinforcement_Learning_for_Multimodal_Hallucination_Mitigation|SAVOR: Self-Aware Visual Grounding via Confidence-Calibrated Reinforcement Learning for Multimodal Hallucination Mitigation]]

![[assets/2609.16601_figure.png|800]]

- **arXiv**: [2609.16601](https://arxiv.org/abs/2609.16601)
- **PDF**: https://arxiv.org/pdf/2609.16601
- **详细分析**: [[20_Research/Papers/大模型/SAVOR_Self-Aware_Visual_Grounding_via_Confidence-Calibrated_Reinforcement_Learning_for_Multimodal_Hallucination_Mitigation|SAVOR: Self-Aware Visual Grounding via Confidence-Calibrated Reinforcement Learning for Multimodal Hallucination Mitigation]]
- **作者**: Zixiu Ding, Zilin Zhao, Yingjie He, Xinlang Kang, Guansu Wang, Wei Zhang
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.4，强化学习 0.6）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《SAVOR: Self-Aware Visual Grounding via Confidence-Calibrated Reinforcement Learning for Multimodal Hallucination Mitigation》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HallusionBench, MMBench, MMHal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) have made strong progress on visual question answering and image captioning, yet they still produce fluent claims about objects, attributes, or relations that are not grounded in the image. Many remedies either modify decoding at test time, which adds latency, or fine tune with preferences such as DPO variants, which teach which answer is preferred but not when the model's own answer is unreliable. We argue that calibrated self assessment is the missing signal. We introduce Savor, a training framework that (i) augments the output schema with token and answer confidence, (ii) optimises the policy with a Group Relative Policy Optimisation (GRPO) objective that penalises calibration error and poor abstention decisions, and (iii) uses the learned confidence at inference time to revisit visual evidence only when the model is uncertain. Experiments on POPE, HallusionBench, AMBER and MMHal-Bench across two recent backbones (InternVL3-8B and Qwen3-VL-8B) show that Savor reduces hallucination while preserving general capability on MME and MMBench, with lower Expected Calibration Error than DPO and decoding baselines.

</details>

---

### [[20_Research/Papers/大模型/A_multimodal_large_language_model_for_evidence-based_autism_spectrum_disorder_screening|A multimodal large language model for evidence-based autism spectrum disorder screening]]

![[assets/2609.16464_figure.png|800]]

- **arXiv**: [2609.16464](https://arxiv.org/abs/2609.16464)
- **PDF**: https://arxiv.org/pdf/2609.16464
- **详细分析**: [[20_Research/Papers/大模型/A_multimodal_large_language_model_for_evidence-based_autism_spectrum_disorder_screening|A multimodal large language model for evidence-based autism spectrum disorder screening]]
- **作者**: Jun Chen, Qi Zhao, Yunliang Jiang, Shuqin Cao, Yunqiang Lin, Chenglong Jia, Qiang Guo, Guang Dai, Xiongtao Zhang, Mengmeng Wang, Xiaoyue Ma
- **cs 子类**: cs.CV, cs.HC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《A multimodal large language model for evidence-based autism spectrum disorder screening》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The clinical management of autism spectrum disorder (ASD) faces a bottleneck in early screening, mainly because trained specialists are scarce and conventional assessment tools are subjective. Here, we introduce ASDchat, a multimodal large language model designed for evidence-based ASD screening, which takes video, audio, and dialogue as input. ASDchat adopts a dual-branch architecture, where the decision branch generates screening probabilities and the evidence branch generates traceable, timestamped behavioral evidence aligned with standardized clinical criteria (ADOS-2). The model was trained and evaluated on a dataset of 1,035 participants from 27 sites in China, which covered typically developing (TD) children, children with ASD, and children with other disorders. For ASD versus TD, ASDchat reached an area under the receiver operating characteristic curve (AUC) of 0.953 $\pm$ 0.021. On 9 held-out sites that were not used for training, the mean AUC was 0.932. Furthermore, unsupervised clustering of the behavioral dimensions split the ASD cases into six subtypes with different phenotypic profiles, and ASDchat suggests an intervention for each subtype. ASDchat provides a feasible path for large-scale, evidence-based early ASD screening in clinical practice.

</details>

---

### [[20_Research/Papers/具身智能/The_Neverwhere_Visual_Parkour_Benchmark_Suite|The Neverwhere Visual Parkour Benchmark Suite]]

![[assets/2609.16443_figure.png|800]]

- **arXiv**: [2609.16443](https://arxiv.org/abs/2609.16443)
- **PDF**: https://arxiv.org/pdf/2609.16443
- **详细分析**: [[20_Research/Papers/具身智能/The_Neverwhere_Visual_Parkour_Benchmark_Suite|The Neverwhere Visual Parkour Benchmark Suite]]
- **作者**: Ziyu Chen, Henghui Bao, Haoran Chang, Alan Yu, Ran Choi, Kai McClennen, Gio Huh, Kevin Yang, Ri-Zhao Qiu, Yajvan Ravan, John J. Leonard, Xiaolong Wang...
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《The Neverwhere Visual Parkour Benchmark Suite》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BiGym, GaussGym, IssacSim, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

State-of-the-art visual locomotion controllers are increasingly capable at handling complex visual environments, making evaluating their real-world performance before deployment increasingly difficult. This work intends to narrow this train/evaluation gap by developing a collection of hyper-photo-realistic, closed-loop evaluation environments - The Neverwhere Benchmark Suite - comprised of over sixty 3D Gaussian Splatting reconstructions of urban indoor and outdoor scenes. Our goal is to encourage large-scale and reproducible robot evaluation by making it easier to create and integrate Gaussian splats-based reconstructions into simulated continuous testing setups. We also underscore the potential pitfalls of relying exclusively on 3D Gaussian-generated data for training, by providing policy checkpoints trained over multiple Neverwhere scenes and their performance when evaluated in novel scenes. Our analysis illustrates the necessity of sourcing diverse data to ensure performance. Code and data are available on the project page: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/ConGraspXL_Controllable_Constraint-Conditioned_Dexterous_Grasping_Motion_Synthesis|ConGraspXL: Controllable Constraint-Conditioned Dexterous Grasping Motion Synthesis]]

![[assets/2609.16319_figure.png|800]]

- **arXiv**: [2609.16319](https://arxiv.org/abs/2609.16319)
- **PDF**: https://arxiv.org/pdf/2609.16319
- **详细分析**: [[20_Research/Papers/具身智能/ConGraspXL_Controllable_Constraint-Conditioned_Dexterous_Grasping_Motion_Synthesis|ConGraspXL: Controllable Constraint-Conditioned Dexterous Grasping Motion Synthesis]]
- **作者**: Hui Zhang, Mirko Meboldt, Jie Song
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.0（加权：具身智能 2.7，机器人 0.3）
- **关联关键词**: EmbodiedAI

#### 研究背景与动机

《ConGraspXL: Controllable Constraint-Conditioned Dexterous Grasping Motion Synthesis》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous grasping is usually conducted for specific tasks, leading to heterogeneous constraints such as specific approach directions, desired contact regions, specified wrist trajectories, and functional hand poses. Our previous work, GraspXL, achieves scalable grasping motion synthesis for diverse objects and hand morphologies, while lacking controllability for synthesis under such various task-driven constraints. In this paper, we propose ConGraspXL, which extends GraspXL with controllable constraint-conditioned grasp motion synthesis that accommodates diverse task-driven constraints and their combinations. We introduce a hierarchical constraint formulation, enable flexible constraint composition with a masked residual interface, and improve control precision with dynamic hand centers and feed-forward wrist guidance. Without losing the strong generalization capabilities of GraspXL, ConGraspXL enables precise and flexible controllability for various individual constraints and their combinations, providing a plug-and-play low-level grasp controller for downstream applications such as whole-body grasp completion, functional grasping, and human-motion imitation.

</details>

---

### [[20_Research/Papers/机器人/Occupancy_Network-Guided_Autonomous_Robotic_Partial_Nephrectomy|Occupancy Network-Guided Autonomous Robotic Partial Nephrectomy]]

![[assets/2609.16186_first_page.png|800]]

- **arXiv**: [2609.16186](https://arxiv.org/abs/2609.16186)
- **PDF**: https://arxiv.org/pdf/2609.16186
- **详细分析**: [[20_Research/Papers/机器人/Occupancy_Network-Guided_Autonomous_Robotic_Partial_Nephrectomy|Occupancy Network-Guided Autonomous Robotic Partial Nephrectomy]]
- **作者**: Ethan Kilmer, Pit Henrich, Jiawei Ge, Paul M. Scheikl, Laura Connolly, Soum D. Lokeshwar, Joseph Chen, Justin D. Opfermann, Kaitlyn Kumar, Lauren Shepard, Ahmed Ghazi, Nirmish Singla...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Occupancy Network-Guided Autonomous Robotic Partial Nephrectomy》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous soft-tissue cancer surgery has been limited to interventions on organ surfaces, because current systems cannot perceive and adapt to anatomy once it deforms or is cut. We introduce the first vision-guided autonomous system capable of performing complete tumor resections for partial nephrectomy. Our system integrates conditional occupancy networks, trained entirely in a physics-based simulation, that infer full 3-D anatomy (tumor, margin tissue, and kidney) from single-view partial point clouds. These occupancy networks maintain intraoperative tracking even as tissue is cut and deformed, enabling adaptive planning and execution. The surgical platform combines a depth camera for capturing surface point clouds, dual robotic arms for electrosurgical cutting and vacuum-based tissue manipulation, and an autonomous control strategy for tumor resection. In patient-derived hydrogel phantoms under an open partial nephrectomy setting, the robot performed eight consecutive autonomous tumor resections comprising 77 electrosurgical cuts, with all cuts achieving negative surgical margins and 1.61 $\pm$ 0.48 mm mean absolute margin error. This work demonstrates, for the first time, a foundation for supervised autonomous closed-loop, imaging-driven, margin-negative tumor removal in phantoms.

</details>

---

### [[20_Research/Papers/具身智能/World-Action_Models_for_Robot_Learning_and_Control_A_Survey|World-Action Models for Robot Learning and Control: A Survey]]

![[assets/2609.16074_figure.png|800]]

- **arXiv**: [2609.16074](https://arxiv.org/abs/2609.16074)
- **PDF**: https://arxiv.org/pdf/2609.16074
- **详细分析**: [[20_Research/Papers/具身智能/World-Action_Models_for_Robot_Learning_and_Control_A_Survey|World-Action Models for Robot Learning and Control: A Survey]]
- **作者**: Zuxing Lu, Hongjia Zhai, Guanzhi Wang, Huajian Zeng, Jiaqi Yang, Jingyu Liu, Lei Cheng, Yuantai Zhang, Yuheng Qiu, Zezhou Cheng, Ivan Laptev, Danfei Xu...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型, 强化学习
- **相关性评分**: 3.1（加权：具身智能 1.2，强化学习 0.2，世界模型 0.4，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《World-Action Models for Robot Learning and Control: A Survey》归入 机器人、具身智能、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Awesome-World, OpenVLA, URL, WM-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots operating in open environments act under partial observability, physical constraints, and dynamic task contexts. Beyond mapping observations and language instructions to actions, they must anticipate how candidate actions may affect future states and task-relevant outcomes. Recent advances in world models, video generation, and Vision-Language-Action (VLA) policies have motivated the development of World-Action Models (WAMs), which couple future world prediction with executable action generation. This survey provides a robotics-oriented review of WAMs. We clarify their scope relative to conventional world models, model-based reinforcement learning, action-conditioned video generation, and reactive VLA policies, and organize existing methods through a unified taxonomy covering representations, transition modeling, action interfaces, architectures, training pipelines, data modalities, and scaling strategies. We further review applications of WAMs in manipulation, navigation, and autonomous driving, and we summarize the datasets, benchmarks, metrics, and protocols used to evaluate WAM systems. Finally, we discuss key challenges in action alignment, world-action factorization, spatial and multi-view consistency, long-horizon memory, neural simulation for closed-loop policy learning, and efficient inference. Taken together, this survey aims to provide a concise technical foundation for integrating predictive world modeling with action generation, toward more reliable embodied robot intelligence. Project page: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/EMODY_Flow_Emotion-Aware_Audio-Driven_Full-Body_Motion_Generation|EMODY Flow: Emotion-Aware Audio-Driven Full-Body Motion Generation]]

![[assets/2609.16011_figure.png|800]]

- **arXiv**: [2609.16011](https://arxiv.org/abs/2609.16011)
- **PDF**: https://arxiv.org/pdf/2609.16011
- **详细分析**: [[20_Research/Papers/具身智能/EMODY_Flow_Emotion-Aware_Audio-Driven_Full-Body_Motion_Generation|EMODY Flow: Emotion-Aware Audio-Driven Full-Body Motion Generation]]
- **作者**: Harsh Kumar Agarwal, Xavier Alameda-Pineda, Olivier Perrotin
- **cs 子类**: cs.CV, cs.GR, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.6，大模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《EMODY Flow: Emotion-Aware Audio-Driven Full-Body Motion Generation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied conversational agents require synchronized full-body motion (body gestures and facial expressions) that aligns with speech and emotional state. Omni-modal large language models excel at multimodal understanding but produce only linguistic outputs, leaving a critical gap in embodied response generation. We identify and address a failure of emotion conditioning: like other conditional generators that under-use weak conditioning signals, a flow-matching model given both a rich audio embedding and a discrete emotion label suppresses the emotion, generating near-identical motion regardless of the specified emotion. We present EMODY Flow, a lightweight (around 35M parameters) flow-matching framework that attaches to a frozen Qwen-3 Omni model and reuses its internal Mimi audio-codecs to condition two parallel DiT generators - one for SMPL-X body pose, one for FLAME facial expressions. A training-time auxiliary emotion classifier restores emotion sensitivity by forcing generated motion to be emotion-identifiable. EMODY Flow sets a new state of the art on BEAT2 gesture quality, with FGD 0.302, Beat Correlation 0.853, and Diversity 24.62 - improving over the best prior results by 26%, 5%, and 62% respectively - and transfers to zero-shot facial animation on TFHP without domain-specific fine-tuning. Beyond these quantitative gains, the classifier yields clearly emotion-separated motion, which we demonstrate qualitatively through a multidimensional-scaling analysis of the generated gestures.

</details>

---
