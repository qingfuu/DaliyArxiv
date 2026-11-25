# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-11-23

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/CTRL_Concurrent_Training_and_Rollout_for_LLM_Reinforcement_Learning_via_GPU_Co-Residency|CTRL: Concurrent Training and Rollout for LLM Reinforcement Learning via GPU Co-Residency]]

![[assets/2611.27119_figure.png|800]]

- **arXiv**: [2611.27119](https://arxiv.org/abs/2611.27119)
- **PDF**: https://arxiv.org/pdf/2611.27119
- **详细分析**: [[20_Research/Papers/大模型/CTRL_Concurrent_Training_and_Rollout_for_LLM_Reinforcement_Learning_via_GPU_Co-Residency|CTRL: Concurrent Training and Rollout for LLM Reinforcement Learning via GPU Co-Residency]]
- **作者**: Ruijia Yang, Ruikai Li, Zeyi Wen
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《CTRL: Concurrent Training and Rollout for LLM Reinforcement Learning via GPU Co-Residency》归入 强化学习、大模型、世界模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) post-training of large language models runs two GPU workloads with different hardware demands: rollout decoding, which is dominated by memory access and whose batch shrinks as responses finish, and a dense learner. Current systems either time-share every GPU between them, paying serial phases and switches, or split GPUs into pools whose sizes change only in whole devices. We present CTRL, which makes co-residency a third RL execution layout: every GPU runs a learner rank beside a persistent rollout engine, sharing the device under CUDA MPS. A host-owned learner makes the layout fit: optimizer state stays in host memory, and policy weights stream layer by layer through a bounded GPU window. A publication gate trains each ready batch first and waits only before releasing the next policy, keeping a dropless staleness bound. A step-time bound guides compute-share selection, and a GPU-time ledger explains overlap and sharing costs. On H100, A800, and RTX 4090 GPUs with Qwen3 models, CTRL achieves 1.11-2.24$\times$ the throughput of the stronger of verl's asynchronous baselines across 24 workload settings with the staleness limit set to two, and 1.23$\times$ verl's colocate_async on eight H100 GPUs. With the same learner, co-residency is 1.10-1.26$\times$ faster than time-sharing on all three platforms and 1.10-1.30$\times$ faster than the best measured whole-GPU split on H100 DAPO-Math workloads at 256-528 trajectories per step, on four and eight GPUs.

</details>

---

### [[20_Research/Papers/具身智能/Analysis_of_Multi-Client_Inference_Techniques_for_Vision-Language-Action_Models|Analysis of Multi-Client Inference Techniques for Vision-Language-Action Models]]

![[assets/2611.26944_figure.png|800]]

- **arXiv**: [2611.26944](https://arxiv.org/abs/2611.26944)
- **PDF**: https://arxiv.org/pdf/2611.26944
- **详细分析**: [[20_Research/Papers/具身智能/Analysis_of_Multi-Client_Inference_Techniques_for_Vision-Language-Action_Models|Analysis of Multi-Client Inference Techniques for Vision-Language-Action Models]]
- **作者**: Stefan de Lasa, Mohammadreza Mofayezi, Gennady Pekhimenko, Nandita Vijaykumar
- **cs 子类**: cs.DC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Analysis of Multi-Client Inference Techniques for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action models (VLAs) are a new class of machine learning model for generalizable robot control. While they enable robots to perform complex tasks in unseen environments, serving VLAs leaves hardware idle between inference passes and under-utilized during inference. Serving multiple clients at once can improve utilization, but fundamental multi-client techniques such as batching and co-execution have not been characterized for VLAs. We therefore characterize the trade-offs these known techniques impose across latency, throughput, power, and hardware utilization. Our findings inform trade-offs and challenges for future multi-VLA serving systems.

</details>

---

### [[20_Research/Papers/机器人/One_Behavior,_Out_of_Order_Deterministic_Execution_and_Parallel_Simulation_of_ROS_2_Applications|One Behavior, Out of Order: Deterministic Execution and Parallel Simulation of ROS 2 Applications]]

![[assets/2611.26676_figure.png|800]]

- **arXiv**: [2611.26676](https://arxiv.org/abs/2611.26676)
- **PDF**: https://arxiv.org/pdf/2611.26676
- **详细分析**: [[20_Research/Papers/机器人/One_Behavior,_Out_of_Order_Deterministic_Execution_and_Parallel_Simulation_of_ROS_2_Applications|One Behavior, Out of Order: Deterministic Execution and Parallel Simulation of ROS 2 Applications]]
- **作者**: Chengzi Huang, Behnam Khodabandeloo, Duc Anh Nguyen, Chuanchao Gao, Wang Yi
- **cs 子类**: cs.DC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《One Behavior, Out of Order: Deterministic Execution and Parallel Simulation of ROS 2 Applications》归入 机器人、具身智能 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

System-level simulation is widely used to validate robotic applications before hardware deployment. However, Robot Operating System 2 (ROS 2), a popular middleware for such applications, uses asynchronous publish-subscribe communication, which can make application behavior depend on scheduling and the platform. The behavior can then vary across runs and machines even with the same inputs. This nondeterminism makes faults hard to reproduce and tests unreliable. In this paper, we first give ROS 2 applications a lightweight coordination scheme in which every component, including event-driven ones, reads its inputs and writes its outputs at predefined time instants. By decoupling computation and communication, the scheme makes an application deterministic, that is, it always has one behavior for given inputs. Tests are thus repeatable, but for large applications they still take a long time. To speed up these tests, we then present an out-of-order parallel simulation algorithm. From the predefined read and write instants, it knows before the run which activations of components depend on which. It starts each activation as soon as those it depends on have finished. Finally, we implement the algorithm in a simulator that runs existing ROS 2 applications without any change to them or to ROS 2. We evaluate the simulator on industrial use cases and synthetic graphs. On the industrial use cases, it is up to 2.6 times faster than synchronous parallel simulation and needs an order of magnitude less memory for messages than asynchronous parallel simulation.

</details>

---
