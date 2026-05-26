# cs.NI | Networking and Internet Architecture | 2026-05-25

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Sea_Trial_Validation_of_the_ROS-DESERT_Middleware_with_Autonomous_Underwater_Vehicles|Sea Trial Validation of the ROS-DESERT Middleware with Autonomous Underwater Vehicles]]

![[assets/2605.23553_figure.png|800]]

- **arXiv**: [2605.23553](https://arxiv.org/abs/2605.23553)
- **PDF**: https://arxiv.org/pdf/2605.23553
- **详细分析**: [[20_Research/Papers/机器人/Sea_Trial_Validation_of_the_ROS-DESERT_Middleware_with_Autonomous_Underwater_Vehicles|Sea Trial Validation of the ROS-DESERT Middleware with Autonomous Underwater Vehicles]]
- **作者**: Davide Cosimo, Davide Costa, Riccardo Costanzi, Filippo Campagnaro, Andrea Caiti, Michele Zorzi
- **cs 子类**: cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

水下自主航行器（AUV）在海洋观测、近海作业和国防任务中应用越来越广，但水声通信仍然是多艇协同的核心瓶颈。与陆地无线网络不同，水下声学链路带宽低、时延长且环境波动强，导致多AUV系统的控制、任务分配和数据回传都难以稳定实现。本文值得关注之处在于，它不是只讨论某个单点算法，而是试图把 ROS 2、DESERT Underwater 和传统 ROS 1 控制链路打通，形成可在真实海试中部署的通用通信与协同软件架构。

#### 方法概述和架构

论文提出一种名为 rmw_desert 的中间件架构，将 ROS 2 应用层与 DESERT Underwater 通信框架连接起来，并通过 ROS 1 bridge 兼容已有AUV前座控制器。该架构支持跨层、细粒度配置，可把应用层消息直接映射到水声通信栈，同时在艇上处理环境测量结果，为自适应通信行为提供依据。作为示例应用，作者实现了一种轻量级的深度优化策略：利用AUV机动能力和环境感知信息，动态调整节点深度，以改善声学链路质量。系统输出主要体现在两方面：一是支持多平台任务与通信协同的统一软件栈，二是基于环境反馈的通信策略执行结果。

#### 实验结果分析

作者在拉斯佩齐亚湾外海、平均水深约100 m的近岸海域进行了海试，部署了3艘承担不同角色的AUV，对完整软件栈进行了验证。实验结果表明，在约1 km的水平间距下，深度自适应重定位能够带来可测的包接收提升；而在更短距离上，由于接收信号能量仍高于解调门限，性能差异不明显。总体来看，海试验证了该架构在现有AUV平台上的可行性、模块化和实际部署能力；具体数值在节选中未给出。

<details>
<summary>完整摘要</summary>

本文提出了一种模块化软件架构，用于实现异构自主水下航行器（AUV）之间面向环境感知的协同，以提升水下声学连通性。该架构将 Robot Operating System 2（ROS 2）应用层与 DESERT Underwater 通信框架通过 rmw_desert 中间件进行结合，并集成了 Robot Operating System 1（ROS 1）桥接，以确保与传统车辆前座控制器的互操作性。该设计支持对通信栈进行细粒度、跨层配置，并支持对环境测量结果进行艇上处理，从而指导自适应通信行为。作为一个代表性用例，本文利用该架构实现了一种轻量级深度优化策略，借助环境感知与AUV机动性来提升声学链路性能。整套软件栈通过在拉斯佩齐亚湾外近岸水域进行的海试进行了验证，该区域平均水深约为100 m，试验部署包含3艘承担不同运行角色的AUV。实验结果表明，在约1 km的水平分离距离上，基于深度自适应的重定位能够带来可测的包接收提升；而在更短距离上，由于接收信号能量仍高于解调门限，性能差异可以忽略。除链路层性能外，海试还确认了所提架构在现有AUV平台上的可行性、模块化以及实际部署能力。

</details>

---
