# Daily Arxiv

面向 Obsidian 的中文 arXiv 每日论文简报仓库，重点跟踪具身智能、大模型、强化学习、世界模型和机器人方向的每日新增论文。

本仓库每天自动同步 `10_Daily` 目录内容。每个日期对应一个独立文件夹，包含当日汇总入口、按 arXiv CS 子类拆分的论文列表、重点领域汇总、论文图片资源和结构化元数据。

## 内容范围

- **具身智能**：Embodied AI、VLA、导航、操作、抓取、仿真到真实等。
- **大模型**：LLM、VLM、多模态基础模型、RAG、智能体相关模型等。
- **强化学习**：RL、offline RL、policy optimization、reward model、MDP/POMDP 等。
- **世界模型**：world model、latent dynamics、transition model、model-based RL 等。
- **机器人**：robotics、humanoid、quadruped、UAV、SLAM、motion planning 等。

论文会根据标题、摘要、关键词和 arXiv 分类进行相关性打分。每篇论文只归入加权分最高的一个主领域，避免在多个领域重复出现；其它命中方向会保留在条目的“相关领域”字段中。

## 目录结构

~~~text
.
├── README.md
└── YYYY-MM-DD/
    ├── Daily_arxiv_report_YYYY-MM-DD.md     # 当日入口文件
    ├── 重点关键词论文汇总.md                  # 按主领域归类的重点论文汇总
    ├── cs.RO_Robotics.md                    # 按 arXiv CS 子类拆分的列表
    ├── cs.LG_Machine_Learning.md
    ├── papers_YYYY-MM-DD.json               # 当日论文结构化元数据
    └── assets/                              # 论文主图/兜底首页图片
~~~

## 在 Obsidian 中使用

推荐将本仓库作为一个 Obsidian Vault 打开。

1. 克隆仓库：

~~~bash
git clone git@github.com:qingfuu/DaliyArxiv.git
~~~

2. 用 Obsidian 打开克隆后的 `DaliyArxiv` 文件夹。

3. 从日期文件夹进入当天日报，例如：

~~~text
2026-05-20/Daily_arxiv_report_2026-05-20.md
~~~

4. 推荐阅读顺序：

- 先打开 `Daily_arxiv_report_YYYY-MM-DD.md` 查看当日入口。
- 再进入 `重点关键词论文汇总.md`，按主领域快速浏览。
- 对感兴趣的论文，继续查看对应 arXiv 链接、PDF 链接和主图。
- 如果需要结构化处理，可读取 `papers_YYYY-MM-DD.json`。

## 报告内容

每篇论文通常包含：

- 论文标题和本地 Obsidian 链接
- 本地主图或 PDF 首页兜底图
- arXiv 链接和 PDF 链接
- 作者、CS 子类、归属领域、相关领域
- 相关性加权评分
- 中文分析：
  - 研究背景与动机
  - 方法概述和架构
  - 实验结果分析
- 折叠的完整摘要中文翻译

## 自动更新

日报由本地自动任务生成：

- 每天 08:00（Asia/Shanghai）运行
- 收集前一天 arXiv 新增论文
- 筛选最多 100 篇高相关论文
- 下载论文主图或生成 PDF 首页兜底图
- 生成中文分析和 Obsidian Markdown 文件
- 自动提交并推送本仓库

如果当天没有符合条件的论文，会生成情况说明；如果远程推送失败，本地文件仍会保留。

## GitHub 显示说明

本仓库主要面向 Obsidian 使用。部分 Obsidian WikiLink 语法（例如 `[[...]]` 或 `![[...]]`）在 GitHub Markdown 中不完全兼容。若需要优先兼容 GitHub 图片显示，可将图片输出改为标准 Markdown 语法：

~~~markdown
![论文主图](assets/example.png)
~~~

## 备注

本项目是个人科研阅读与资料整理工作流的一部分，报告内容用于快速筛选和初读论文。重要论文仍建议结合原文 PDF、实验表格和代码仓库进一步核查。

