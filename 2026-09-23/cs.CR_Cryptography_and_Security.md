# cs.CR | Cryptography and Security | 2026-09-23

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Design_and_Evaluation_of_a_Controlled_Post-Alert_Incident_Orchestration_and_Response_Subsystem_Using_a_Rule_Engine_and_a_Local_Large_Languag|Design and Evaluation of a Controlled Post-Alert Incident Orchestration and Response Subsystem Using a Rule Engine and a Local Large Language Model]]

![[assets/2609.26316_figure.png|800]]

- **arXiv**: [2609.26316](https://arxiv.org/abs/2609.26316)
- **PDF**: https://arxiv.org/pdf/2609.26316
- **详细分析**: [[20_Research/Papers/大模型/Design_and_Evaluation_of_a_Controlled_Post-Alert_Incident_Orchestration_and_Response_Subsystem_Using_a_Rule_Engine_and_a_Local_Large_Languag|Design and Evaluation of a Controlled Post-Alert Incident Orchestration and Response Subsystem Using a Rule Engine and a Local Large Language Model]]
- **作者**: Hoang-Lam Huynh, Quoc-Cuong Tang, Van-Tri Phan, Khuong Nguyen-An
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM

#### 研究背景与动机

《Design and Evaluation of a Controlled Post-Alert Incident Orchestration and Response Subsystem Using a Rule Engine and a Local Large Language Model》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a controlled post-alert incident orchestration and response subsystem for educational information systems. The architecture separates deterministic classification, contextual analysis, human approval, and technical execution. A Rule Engine determines severity and selects the playbook, while Static RAG and a local large language model provide advisory content under Validator, Guardrail, Output Sanitizer, and Safe Fallback controls. Experiments begin after simulated alerts are stored in Elasticsearch. The Rule Engine matched the predefined routing matrix in all 30 boundary cases. The Durable Queue completed 100 events without duplicate tasks, new failed tasks, or unintended firewall rules. An eight-alert contention experiment preserved the configured limit of one active model request, and 30 sequential measurements showed an overall mean post-alert processing time of approximately 33 seconds. The results demonstrate functional correctness, traceability, controlled recovery, and bounded model integration within the evaluated laboratory scope.

</details>

---

### [[20_Research/Papers/强化学习/A_Cross-Dataset_based_Zero-Day_Intrusion_Detection_System_by_Integrating_Siamese_Network_and_Reinforcement_Learning|A Cross-Dataset based Zero-Day Intrusion Detection System by Integrating Siamese Network and Reinforcement Learning]]

![[assets/2609.26115_first_page.png|800]]

- **arXiv**: [2609.26115](https://arxiv.org/abs/2609.26115)
- **PDF**: https://arxiv.org/pdf/2609.26115
- **详细分析**: [[20_Research/Papers/强化学习/A_Cross-Dataset_based_Zero-Day_Intrusion_Detection_System_by_Integrating_Siamese_Network_and_Reinforcement_Learning|A Cross-Dataset based Zero-Day Intrusion Detection System by Integrating Siamese Network and Reinforcement Learning]]
- **作者**: Md. Meheraj Hossain, Saumik Das Turja, Sibgatullah Tasnim, Md. Fahmid-Ul-Alam Juboraj, Muhammad Iqbal Hossain
- **cs 子类**: cs.CR
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，强化学习 1）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《A Cross-Dataset based Zero-Day Intrusion Detection System by Integrating Siamese Network and Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Cryptography and Security 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Zero-day threats are nascent for the Internet of Things (IoT) network security, which demands cognitive detec-tion mechanisms that can identify emerging malicious behavior. Conventional intrusion detection mechanisms fail to generalize dynamic zero-day exploits within sophisticated IoT environments. This paper proposes a hybrid zero-day intrusion detection system using Siamese network-based anomaly correlation and reinforcement learning-based adaptive defense. Furthermore, the paper uses unsupervised machine learning classifiers over benchmark IoT datasets with the intention of detection of known attack types compared to unknown anomalies using distance-based similarity analysis to detect possible zero-day attacks. To facilitate adaptability, a Proximal Policy Optimization (PPO) reinforcement learning-based agent dynamically adjusts the defense policy with continuous feedback and optimization. Experimental evaluations demonstrate 99.28% training accuracy, 99.07% accuracy in unknown attack detection, and 93.94% zero-day detection ratio, confirming the convergence and stability of the model on this http URL system offers a self-learning and extensible defense mechanism of IoT deployments by finding the right balance between precision, latency and false positives. This deep anomaly correlation with adaptive reinforcement learning is a firm base on which the next generation and autonomic cyber security solutions can take the reins as the zero-day threats keep changing their course.

</details>

---
