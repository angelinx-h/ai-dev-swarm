# AI Dev Swarm 中文用户手册

## 目录

1. [什么是 AI Dev Swarm?](#什么是-ai-dev-swarm)
2. [核心理念](#核心理念)
3. [快速开始](#快速开始)
4. [开发流程详解](#开发流程详解)
5. [技能系统说明](#技能系统说明)
6. [项目结构](#项目结构)
7. [最佳实践](#最佳实践)
8. [常见问题](#常见问题)
9. [获取帮助](#获取帮助)

---

## 什么是 AI Dev Swarm?

AI Dev Swarm 是一个由 AI 驱动的开发框架,旨在将一个简单的想法自动转化为功能完整、可投入商用的全栈产品。

### 核心特点

- **无需编程知识** - 不需要懂代码
- **无需技术背景** - 不需要技术专业知识
- **只需一个想法** - 从想法出发,AI 处理一切

AI Dev Swarm 将逐步引导您完成整个产品生命周期:

- AI 处理所有技术细节
- 您专注于愿景和决策
- 实现真正的"一人公司"梦想

---

## 核心理念

我们的目标简单而宏大:

**让一个人也能成立一家公司 — 由 AI 提供支持。**

---

## 快速开始

### 第一步:准备工作

1. **Fork 和克隆项目**
   ```bash
   git clone https://github.com/your-username/ai-dev-swarm.git
   cd ai-dev-swarm
   ```

2. **选择您的 AI 助手**

   **推荐选项 - Claude Code (默认)**
   - Claude Code 原生支持 Agent Skills
   - 直接使用,无需额外配置

   **其他选项 - Gemini CLI 或其他 AI Agent**
   - 需要配置 MCP 服务器
   - 在您的配置文件中添加:

   ```json
   {
     "mcpServers": {
       "skillz": {
         "command": "uvx",
         "args": [
           "skillz@latest",
           "/项目根目录绝对路径/dev-swarms/skills",
           "--verbose"
         ]
       }
     }
   }
   ```

### 第二步:从想法开始

1. 打开 `ideas.md` 文件
2. 用简单的语言写下您的项目想法
3. 描述您想解决的问题
4. 说明目标用户是谁
5. 列出任何要求或限制条件

示例:
```markdown
# 我的想法

我想创建一个帮助小企业管理客户的应用。

## 问题
小企业主没有时间和预算使用复杂的 CRM 系统。

## 目标用户
拥有 1-10 名员工的小企业主。

## 核心功能需求
- 简单的客户信息管理
- 跟踪客户互动历史
- 设置提醒和跟进任务
```

### 第三步:开始开发旅程

编写好 `ideas.md` 后,通过 AI 助手运行:

```
/init-ideas
```

或者告诉 AI:
```
请帮我初始化项目并启动 Stage 0
```

---

## 开发流程详解

AI Dev Swarm 采用结构化的 11 个阶段(Stage 0-10),将想法转化为产品。

### 规划与策略阶段 (Stages 0-4)

#### Stage 0: 初始化想法 (Init Ideas)
**目标**: 将非正式的想法转化为专业的项目文档

**输入**: `ideas.md` 中的想法
**输出**: `00-init-ideas/` 文件夹中的结构化文档
- `README.md` - 项目概述和指南
- `problem-statement.md` - 清晰的问题定义
- `target-users.md` - 目标用户群体
- `value-proposition.md` - 价值主张
- `cost-budget.md` - 预算评估
- `owner-requirement.md` - 项目要求

**如何使用**:
```
/init-ideas
```

---

#### Stage 1: 市场调研 (Market Research)
**目标**: 验证问题并了解市场环境

**输出**: `01-market-research/` 文件夹
- `market-overview.md` - 市场规模、趋势、增长动力
- `competitor-analysis.md` - 竞争对手分析
- `gap-analysis.md` - 市场空白分析
- `pricing-research.md` - 定价策略研究
- `validation-findings.md` - 问题验证证据

**如何使用**:
```
/market-research
```

**提示**: AI 会通过网络搜索收集市场数据和竞争对手信息

---

#### Stage 2: 用户画像 (Personas)
**目标**: 定义详细的用户画像和用户故事

**输出**: `02-personas/` 文件夹
- `persona-primary.md` - 主要用户画像
- `persona-secondary.md` - 次要用户画像(可选)
- `user-stories.md` - 优先级排序的用户故事 (P0/P1/P2)

**如何使用**:
```
/personas
```

**关键点**: 用户故事使用业务语言,不涉及技术实现

---

#### Stage 3: MVP 定义 (MVP)
**目标**: 定义最小可行产品的范围和成功指标

**输出**: `03-mvp/` 文件夹
- `mvp-scope.md` - MVP 定义:最小可测试产品
- `out-of-scope.md` - 明确排除的功能(防止范围蔓延)
- `success-metrics.md` - 成功指标(使用率/留存率/转化率等)

**如何使用**:
```
/mvp
```

**重要**: 明确说明什么 **不做** 和做什么同样重要

---

#### Stage 4: 产品需求文档 (PRD)
**目标**: 创建全面的产品需求文档

**输出**: `04-prd/` 文件夹
- `prd.md` - 产品概述/目标/用户旅程
- `functional-requirements.md` - 功能需求(产品必须做什么)
- `non-functional-requirements.md` - 非功能需求(性能/安全/合规)
- `out-of-scope.md` - PRD 级别的排除项

**如何使用**:
```
/prd
```

**注意**: 此阶段仍然不涉及技术栈选择

---

### 设计与架构阶段 (Stages 5-7)

#### Stage 5: 用户体验设计 (UX Design)
**目标**: 设计用户流程、交互和界面原型

**输出**: `05-ux/` 文件夹
- `user-flows.md` - 用户流程图(可包含 Mermaid 图表)
- `interaction-specs.md` - 状态、转换、交互规则
- `edge-cases.md` - 边缘情况和预期结果
- `accessibility.md` - 无障碍需求
- `mockup/` - 静态 HTML/CSS/JS 原型(可选)

**如何使用**:
```
/ux
```

**提示**: AI 可以生成 Mermaid 流程图和简单的 HTML 原型

---

#### Stage 6: 系统架构 (Architecture)
**目标**: 定义系统组件、数据流和部署边界

**输出**: `06-architecture/` 文件夹
- `system-overview.md` - 主要组件和职责
- `architecture-diagram.md` - 系统架构图(Mermaid 或图片)
- `data-flow.md` - 前端/后端/数据库/外部服务的数据流
- `deployment-boundaries.md` - 本地 vs 云端边界、信任区域

**如何使用**:
```
/architecture
```

---

#### Stage 7: 技术规范 (Tech Specs)
**目标**: 确定技术栈和开发标准

**输出**: `07-tech-specs/` 文件夹
- `tech-solution-research.md` - 技术方案研究
- `tech-stack.md` - 语言/框架/数据库/云服务提供商选择
- `theme-standards.md` - UI 主题规范(字体/尺寸/颜色)
- `coding-standards.md` - 代码风格规范
- `testing-standards.md` - 测试标准
- `security-standards.md` - 安全编码规范

**如何使用**:
```
/tech-specs
```

**关键决策**: 此阶段锁定所有技术选型

---

### 开发与部署阶段 (Stages 8-10)

#### Stage 8: DevOps 设置 (DevOps)
**目标**: 建立开发环境基础

**输出**: `08-devops/` 文件夹
- `github-setup.md` - GitHub 仓库设置、分支保护
- `mcp-setup.md` - MCP 工具设置
- `vscode-devcontainer.md` - VS Code Dev Container 配置

**如何使用**:
```
/devops
```

**包含**:
- GitHub 仓库配置
- MCP 服务器设置(Playwright/GitHub/AWS 等)
- Docker 开发容器配置

---

#### Stage 9: 敏捷开发 (Sprints)
**目标**: 使用 AI 加速的功能驱动开发

**输出**: `09-sprints/` 文件夹
- 每个 Sprint 一个子文件夹
- 四种 Backlog 类型:
  - `FEATURE-*.md` - 新功能需求
  - `CHANGE-*.md` - 功能变更需求
  - `BUG-*.md` - Bug 修复
  - `IMPROVE-*.md` - 改进/重构

**如何使用**:
```
/project-management
```

**工作流程**:
1. 创建 Sprint 和 Backlog
2. 使用 `/code-development` 实现功能
3. 使用 `/code-review` 审查代码
4. 使用 `/code-test` 测试实现
5. 迭代直到完成

**示例结构**:
```
09-sprints/
├── README.md
├── user-auth/
│   ├── README.md
│   ├── FEATURE-auth-login.md
│   ├── CHANGE-login-error.md
│   └── BUG-session-timeout.md
└── profile-basics/
    └── ...
```

---

#### Stage 10: 部署 (Deployment)
**目标**: 部署到测试/生产环境,配置 CI/CD

**输出**: `10-deployment/` 文件夹
- `deployment-index.md` - 部署路径和检查清单
- `_templates/` - 部署模板
- `infra/` - 云基础设施文档
- `releases/` - 版本发布记录
- `evidence/` - 部署证据(截图、URL 等)

**如何使用**:
```
/deployment
```

**包含**:
- 云基础设施配置(AWS/Azure/GCP)
- CI/CD 流水线设置
- 测试/生产环境部署
- 发布验证和回滚计划

---

## 技能系统说明

AI Dev Swarm 提供一系列专业技能来加速开发:

### 核心阶段技能

| 技能 | 命令 | 用途 |
|------|------|------|
| 初始化想法 | `/init-ideas` | 将想法转化为项目文档 (Stage 0) |
| 市场调研 | `/market-research` | 市场验证和竞争分析 (Stage 1) |
| 用户画像 | `/personas` | 创建用户画像和故事 (Stage 2) |
| MVP 定义 | `/mvp` | 定义 MVP 范围 (Stage 3) |
| 产品需求 | `/prd` | 编写产品需求文档 (Stage 4) |
| UX 设计 | `/ux` | 用户体验设计 (Stage 5) |
| 系统架构 | `/architecture` | 系统架构设计 (Stage 6) |
| 技术规范 | `/tech-specs` | 定义技术栈和标准 (Stage 7) |
| DevOps 设置 | `/devops` | 开发环境配置 (Stage 8) |
| 项目管理 | `/project-management` | Sprint 和 Backlog 管理 (Stage 9) |
| 部署 | `/deployment` | 应用部署 (Stage 10) |

### 开发辅助技能

| 技能 | 命令 | 用途 |
|------|------|------|
| 代码开发 | `/code-development` | 实现功能/修复/改进 |
| 代码审查 | `/code-review` | 代码质量审查 |
| 代码测试 | `/code-test` | 全面测试(单元/集成/UI/API) |
| 提交信息 | `/draft-commit-message` | 生成规范的提交信息 |

### 工具技能

| 技能 | 命令 | 用途 |
|------|------|------|
| MCP 服务器 | `/mcp-server` | 添加/管理 MCP 服务器 |
| Mermaid 图表 | `/mermaid` | 创建和转换 Mermaid 图表 |
| Node.js | `/nodejs` | 配置 Node.js 环境 |
| Python | `/python` | 配置 Python 环境 |
| 屏幕快照 | `/screen-snapshot` | 捕获和检查屏幕区域 |
| 后台进程 | `/background-process` | 运行后台进程 |
| 使用计算机 | `/use-computer` | GUI 应用交互 |
| 项目归档 | `/project-archive` | 归档当前项目 |
| 创建/更新技能 | `/create-update-agent-skill` | 创建或更新 Agent 技能 |

---

## 项目结构

```
ai-dev-swarm/
├── README.md                 # 项目说明
├── ideas.md                  # 起点:您的想法
├── 00-init-ideas/            # Stage 0: 问题定义
├── 01-market-research/       # Stage 1: 市场调研
├── 02-personas/              # Stage 2: 用户画像
├── 03-mvp/                   # Stage 3: MVP 定义
├── 04-prd/                   # Stage 4: 产品需求
├── 05-ux/                    # Stage 5: UX 设计
├── 06-architecture/          # Stage 6: 系统架构
├── 07-tech-specs/            # Stage 7: 技术规范
├── 08-devops/                # Stage 8: DevOps
├── 09-sprints/               # Stage 9: 敏捷开发
├── 10-deployment/            # Stage 10: 部署
├── 99-archive/               # 已完成项目归档
├── features/                 # 功能知识库
├── src/                      # 源代码
└── dev-swarms/               # 框架核心
    ├── skills/               # Agent 技能定义
    ├── docs/                 # 框架文档
    └── py_scripts/           # Python 工具脚本
```

### 关键文件夹说明

- **00-10**: 按顺序的 11 个开发阶段
- **features/**: AI 压缩的产品知识库,按需加载
  - `flows/` - 跨功能流程
  - `contracts/` - API/接口契约
  - `impl/` - 实现说明
- **src/**: 实际代码
- **99-archive/**: 已完成或归档的项目

---

## 最佳实践

### 1. 循序渐进
- 按照 Stage 0-10 的顺序执行
- 不要跳过阶段(除非是非常小的项目)
- 每个阶段完成后再进入下一个

### 2. 详细的想法描述
在 `ideas.md` 中越详细越好:
- 清晰描述问题
- 说明目标用户
- 列出核心功能
- 提及任何技术偏好或限制

### 3. 与 AI 互动
- 主动提问和澄清
- 审查 AI 生成的文档
- 提供反馈和调整方向
- 您做决策,AI 做执行

### 4. 文档驱动开发
- 所有决策都记录在文档中
- 文档是后续阶段的输入
- 保持文档更新

### 5. 迭代和改进
- 使用四种 Backlog 类型管理变更:
  - FEATURE - 新功能
  - CHANGE - 变更现有功能
  - BUG - 修复问题
  - IMPROVE - 改进和重构

### 6. 小项目可以简化
根据项目规模调整:
- **极小项目 (L0-L1)**: 只需 `00-init-ideas/README.md` + 源代码
- **小项目 (L2-L3)**: 可跳过部分阶段
- **大项目 (L4+)**: 完整使用所有 11 个阶段

参考: `dev-swarms/docs/software-dev-classification.md`

---

## 常见问题

### Q1: 我需要懂编程吗?
**答**: 不需要。AI Dev Swarm 设计为非技术人员也能使用。您只需:
- 有清晰的想法
- 能够做出业务决策
- 与 AI 沟通您的需求

### Q2: 使用哪个 AI 助手最好?
**答**:
- **推荐**: Claude Code - 原生支持,开箱即用
- **备选**: Gemini CLI、其他支持 MCP 的 AI Agent

### Q3: 需要多长时间完成一个项目?
**答**: 取决于项目规模:
- 简单工具/脚本: 几小时到 1 天
- 小型应用: 1-2 周
- 中型产品: 2-4 周
- 大型产品: 1-3 个月

### Q4: 可以跳过某些阶段吗?
**答**: 对于小项目可以。但建议至少包括:
- Stage 0 (Init Ideas) - 明确问题
- Stage 3 (MVP) - 定义范围
- Stage 7 (Tech Specs) - 技术决策
- Stage 9 (Sprints) - 开发实现

### Q5: 生成的代码质量如何?
**答**: AI Dev Swarm 包含质量保证机制:
- 代码审查技能 (`/code-review`)
- 全面测试技能 (`/code-test`)
- 编码标准定义 (Stage 7)
- 迭代改进流程 (IMPROVE Backlog)

### Q6: 支持哪些技术栈?
**答**: AI 可以使用任何主流技术栈,包括:
- **前端**: React、Vue、Angular、Next.js、HTML/CSS/JS
- **后端**: Node.js、Python、Go、Java、.NET
- **数据库**: PostgreSQL、MySQL、MongoDB、Redis
- **云服务**: AWS、Azure、GCP、Vercel、Netlify

技术栈在 Stage 7 (Tech Specs) 确定。

### Q7: 如何管理成本?
**答**:
- Stage 0 会生成 `cost-budget.md` 估算每阶段的 LLM Token 成本
- 小项目通常花费 $5-$20
- 中型项目 $50-$200
- 使用更便宜的模型(如 Claude Haiku)可降低成本

### Q8: 可以用于现有项目吗?
**答**: 可以。您可以:
- 使用特定技能(如 `/code-development`, `/code-review`)
- 为现有项目补充文档(从 Stage 4 PRD 开始)
- 用于重构或添加新功能(Stage 9 Sprints)

### Q9: 多人团队可以使用吗?
**答**: 可以,但 AI Dev Swarm 主要针对个人或小团队(1-3人)优化。大团队可能需要额外的协作工具。

### Q10: 如何保持项目整洁?
**答**:
- 完成的工作移到 `99-archive/`
- 使用 `/project-archive` 技能归档整个项目
- 保持 `features/` 知识库更新
- 定期清理不需要的文档

---

## 获取帮助

### 文档资源
- **仓库结构**: `dev-swarms/docs/repository-structure.md`
- **AI 敏捷开发**: `dev-swarms/docs/ai-agile-development.md`
- **功能驱动开发**: `dev-swarms/docs/ai-feature-driven-development.md`
- **Agent 技能规范**: `dev-swarms/docs/agent-skill-specification.md`
- **项目分类**: `dev-swarms/docs/software-dev-classification.md`

### 社区支持
- **Discord 服务器**: https://juniorit.ai/virtual-office
- **GitHub Issues**: https://github.com/your-repo/ai-dev-swarm/issues

### 贡献
欢迎贡献!
- 不需要编程经验
- 不需要技术背景
- 只需要好奇心和学习意愿

有兴趣贡献?加入我们的 Discord,项目维护者会亲自指导您。

---

## 开始您的 AI 开发之旅

1. 打开 `ideas.md`
2. 写下您的想法
3. 运行 `/init-ideas`
4. 跟随 AI 的引导
5. 将想法变成现实

**一个想法。一个人。一个 AI 群体。**

让我们在 AI 时代重新定义产品构建方式。

---

## 许可证

本项目采用 GNU Affero General Public License v3.0 许可 - 详见 [LICENSE](LICENSE) 文件。

本项目可能包含其他开源许可证的代码,这些代码将保留其原始许可证。

---

**Star ⭐ | Fork 🍴 | 分享 💬 | 贡献 🤝**

加入我们的 Discord: https://juniorit.ai/virtual-office
