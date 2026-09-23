# cs.HC | Human-Computer Interaction | 2026-09-21

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/机器人/MarineCraft_Enabling_Rapid_Prototyping_of_Underwater_Robots_via_Modular_Construction|MarineCraft: Enabling Rapid Prototyping of Underwater Robots via Modular Construction]]

![[assets/2609.21396_figure.png|800]]

- **arXiv**: [2609.21396](https://arxiv.org/abs/2609.21396)
- **PDF**: https://arxiv.org/pdf/2609.21396
- **详细分析**: [[20_Research/Papers/机器人/MarineCraft_Enabling_Rapid_Prototyping_of_Underwater_Robots_via_Modular_Construction|MarineCraft: Enabling Rapid Prototyping of Underwater Robots via Modular Construction]]
- **作者**: Yuta Sugiura
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《MarineCraft: Enabling Rapid Prototyping of Underwater Robots via Modular Construction》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Underwater robot development is often hindered by the complexities of waterproofing and wiring, which significantly delay the rapid prototyping process. This paper presents MarineCraft, a modular toolkit designed to accelerate the development cycle through structural reconfiguration. The system features self-contained, waterproof propulsion modules that integrate power, wireless communication, and actuation. By eliminating centralized wiring and the need for repeated sealing, MarineCraft allows diverse robot geometries to be assembled and tested in minutes rather than days. Experimental results demonstrate that this reconfigurable architecture enables fast, iterative design cycles while maintaining reliable operation and leak-free performance at depths of up to 2.5 meters. Our toolkit effectively lowers the barrier to underwater robotics by transforming modularity into a vehicle for rapid physical prototyping.

</details>

---

### [[20_Research/Papers/机器人/OpenRoIS_A_Community-Driven_Open-Source_Middleware_Implementing_the_Robotic_Interaction_Service_(RoIS)_Framework_for_Physical_Robots_and_Vir|OpenRoIS: A Community-Driven Open-Source Middleware Implementing the Robotic Interaction Service (RoIS) Framework for Physical Robots and Virtual Agents]]

![[assets/2609.21178_first_page.png|800]]

- **arXiv**: [2609.21178](https://arxiv.org/abs/2609.21178)
- **PDF**: https://arxiv.org/pdf/2609.21178
- **详细分析**: [[20_Research/Papers/机器人/OpenRoIS_A_Community-Driven_Open-Source_Middleware_Implementing_the_Robotic_Interaction_Service_(RoIS)_Framework_for_Physical_Robots_and_Vir|OpenRoIS: A Community-Driven Open-Source Middleware Implementing the Robotic Interaction Service (RoIS) Framework for Physical Robots and Virtual Agents]]
- **作者**: Sebastian Carrera Villalobos, Christopher Nolan Arellano, Arne Hitzmann, Edilson Morais Brito, Akira Utsumi, Yukiko Horikawa, Takahiro Miyashita, Lotfi El Hafi
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，大模型 0.4，机器人 1.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《OpenRoIS: A Community-Driven Open-Source Middleware Implementing the Robotic Interaction Service (RoIS) Framework for Physical Robots and Virtual Agents》归入 机器人、大模型、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Service applications for human-robot interaction are commonly written against the hardware-specific interfaces of one platform, so a change of hardware forces a rewrite of the application. The Robotic Interaction Service (RoIS) Framework 2.0, standardized by the Object Management Group (OMG), addresses this fragmentation by defining a platform-independent model in which Service Applications interact with Human-Robot Interaction (HRI) Engines through standardized interfaces and hardware-independent symbolic messages. A specification alone, however, does not provide the maintained implementation, Software Development Kits (SDKs), and adapters needed for practical adoption. This paper presents OpenRoIS, a community-driven open-source middleware providing a concrete implementation of the RoIS Framework 2.0. It takes the position that an openly developed, paradigm-neutral implementation is what carries the standard from specification to practice. OpenRoIS contributes a recursive engine architecture in which a single engine class realizes the main and sub HRI Engine roles, an internal five-method component contract distinct from the five external RoIS interfaces, a mapping of those interfaces onto JSON-RPC 2.0 over WebSocket, a single-source-of-truth type pipeline that generates three consistent language stacks, TypeScript and C# client SDKs that include web and Unity support, and a Python adapter SDK that includes ROS 2 support. Through the common RoIS interfaces, a Service Application can address physical robots and virtual agents over the internet. All source code, interface types, and documentation are released under the Apache-2.0 license and openly developed at this https URL .

</details>

---
