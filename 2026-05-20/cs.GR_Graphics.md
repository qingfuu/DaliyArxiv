# cs.GR | Graphics | 2026-05-20

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/其他/BrepForge_Factorized_B-rep_Synthesis_via_Wireframe_Composition_and_Boundary-Conditioned_Surface_Instantiation|BrepForge: Factorized B-rep Synthesis via Wireframe Composition and Boundary-Conditioned Surface Instantiation]]

- **arXiv**: [2605.19411](https://arxiv.org/abs/2605.19411)
- **PDF**: https://arxiv.org/pdf/2605.19411
- **详细分析**: [[20_Research/Papers/其他/BrepForge_Factorized_B-rep_Synthesis_via_Wireframe_Composition_and_Boundary-Conditioned_Surface_Instantiation|BrepForge: Factorized B-rep Synthesis via Wireframe Composition and Boundary-Conditioned Surface Instantiation]]
- **作者**: Jing Li, Yihang Fu, Falai Chen
- **cs 子类**: cs.GR
- **关联关键词**: cs.GR
- **背景与动机**: 《BrepForge: Factorized B-rep Synthesis via Wireframe Composition and Boundary-Conditioned Surface Instantiation》关注 cs.GR 相关问题，主要动机是：该工作聚焦 Graphics 方向中的具体问题。
- **研究方法**: 方法上，论文主要：提出新的模型、框架或算法；设计端到端框架。
- **主要结果**: 结果上，论文表明：具体结论需结合论文实验与原文进一步确认。

<details>
<summary>英文摘要</summary>

Boundary representation (B-rep) is the de facto standard for modern CAD, yet learning-based B-rep synthesis remains challenging due to the tight coupling between discrete topology and continuous geometry. We observe a fundamental asymmetry in B-reps: while wireframe composition involves high-entropy structural decisions, the interior surface geometry is largely constrained by its boundary loops. Motivated by this observation, we propose BrepForge, a generative framework that factorizes B-rep synthesis into two stages: wireframe composition and boundary-conditioned surface instantiation. In the first stage, a face-aware autoregressive model serializes the wireframe into structured sequences that explicitly encode hierarchical Vertex-Edge-Face (V-E-F) connectivity, yielding a topologically complete scaffold. In the second stage, precise surface geometries are instantiated by incorporating...

</details>

---

### [[20_Research/Papers/大模型/CompoSE_Compositional_Synthesis_and_Editing_of_3D_Shapes_via_Part-Aware_Control|CompoSE: Compositional Synthesis and Editing of 3D Shapes via Part-Aware Control]]

- **arXiv**: [2605.19350](https://arxiv.org/abs/2605.19350)
- **PDF**: https://arxiv.org/pdf/2605.19350
- **详细分析**: [[20_Research/Papers/大模型/CompoSE_Compositional_Synthesis_and_Editing_of_3D_Shapes_via_Part-Aware_Control|CompoSE: Compositional Synthesis and Editing of 3D Shapes via Part-Aware Control]]
- **作者**: Habib Slim, Shariq Farooq Bhat, Mohamed Elhoseiny, Yifan Wang, Mike Roberts
- **cs 子类**: cs.GR, cs.LG
- **关联关键词**: LLM, ComputerVision
- **背景与动机**: 《CompoSE: Compositional Synthesis and Editing of 3D Shapes via Part-Aware Control》关注 LLM、ComputerVision 相关问题，主要动机是：现有方法仍面临挑战。
- **研究方法**: 方法上，论文主要：使用 Transformer/基础模型结构。
- **主要结果**: 结果上，论文表明：具体结论需结合论文实验与原文进一步确认。

<details>
<summary>英文摘要</summary>

Creating and editing high-quality 3D content remains a central challenge in computer graphics. We address this challenge by introducing CompoSE, a novel method for Compositional Synthesis and Editing of 3D shapes via part-aware control. Our method takes as input a set of coarse geometric primitives (e.g., bounding boxes) that represent distinct object parts arranged in a particular spatial configuration, and synthesizes as output part-separated 3D objects that support localized granular (i.e., compositional) editing of individual parts. The key insight that enables our method is our use of a diffusion transformer architecture that alternates between processing each part locally and aggregating contextual information across parts globally, and features a novel conditioning technique that ensures strong adherence to the user's input. Importantly, our method learns to infer part semantics...

</details>

---

### [[20_Research/Papers/其他/Spatially_Accelerated_Winding_Numbers_for_Curved_Geometry|Spatially Accelerated Winding Numbers for Curved Geometry]]

- **arXiv**: [2605.19200](https://arxiv.org/abs/2605.19200)
- **PDF**: https://arxiv.org/pdf/2605.19200
- **详细分析**: [[20_Research/Papers/其他/Spatially_Accelerated_Winding_Numbers_for_Curved_Geometry|Spatially Accelerated Winding Numbers for Curved Geometry]]
- **作者**: Jacob Spainhour, Brad Whitlock, Kenneth Weiss
- **cs 子类**: cs.GR
- **关联关键词**: ComputerVision
- **背景与动机**: 《Spatially Accelerated Winding Numbers for Curved Geometry》关注 ComputerVision 相关问题，主要动机是：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。
- **研究方法**: 方法上，论文主要：围绕论文提出的建模、算法或系统设计进行实验验证。
- **主要结果**: 结果上，论文表明：关注鲁棒性或泛化表现。

<details>
<summary>英文摘要</summary>

The generalized winding number (GWN) is a scalar field that supports robust containment queries on curved geometry, including non-watertight, overlapping, and nested boundary representations. While queries can be easily parallelized over samples, direct evaluation on parametric curves and surfaces remains costly for large and complex models. Fast, state-of-the-art GWN approaches leverage a spatial index to approximate the GWN, typically coupled with a Taylor expansion which approximates the GWN contribution for far clusters of geometric primitives. However, such methods operate only on discrete inputs such as triangle meshes and point clouds, and would introduce containment errors near boundaries if applied to curved input. We extend support for fast GWN evaluation over arbitrary collections of NURBS curves in 2D and trimmed NURBS patches in 3D via a Bounding Volume Hierarchy that...

</details>

---

### [[20_Research/Papers/其他/Generative_and_isoparametric_geometric_modeling_of_large-scale_and_multiscale_microstructures|Generative and isoparametric geometric modeling of large-scale and multiscale microstructures]]

- **arXiv**: [2605.18894](https://arxiv.org/abs/2605.18894)
- **PDF**: https://arxiv.org/pdf/2605.18894
- **详细分析**: [[20_Research/Papers/其他/Generative_and_isoparametric_geometric_modeling_of_large-scale_and_multiscale_microstructures|Generative and isoparametric geometric modeling of large-scale and multiscale microstructures]]
- **作者**: Guoyue Luo, Yuntao Ma, Qiang Zou
- **cs 子类**: cs.GR
- **关联关键词**: cs.GR
- **背景与动机**: 《Generative and isoparametric geometric modeling of large-scale and multiscale microstructures》关注 cs.GR 相关问题，主要动机是：现有方法仍面临挑战；系统成本或推理开销是关键约束。
- **研究方法**: 方法上，论文主要：围绕论文提出的建模、算法或系统设计进行实验验证。
- **主要结果**: 结果上，论文表明：具体结论需结合论文实验与原文进一步确认。

<details>
<summary>英文摘要</summary>

As additive manufacturing advances toward higher printing resolution and larger build volumes, microstructures can be designed with finer geometric features over larger physical domains. This trend poses a fundamental challenge for geometric modeling: massive geometric details must be represented compactly, while their associations across scales must be maintained consistently.Existing methods cannot scale well to this requirement. Explicit representations suffer from prohibitive memory cost, and implicit representations remain compact only when microstructures admit analytic, periodic, or otherwise concise procedural descriptions. This paper proposes a new geometric modeling method that treats microstructure modeling as an on-demand generative process, rather than requiring the full instantiation of all geometric details. We first develop ExVCC, an extended volumetric Catmull-Clark...

</details>

---
