# 🚀 Antigravity 全局技能库 (Skill Library)

**总计已加载技能数**: 894

---

## 目录
- [🔧 开发工具与代码工作流 (Development & Code Workflow)](#dev_code) (34)
- [☁️ 部署与云服务 (Deployment & Cloud)](#cloud_deploy) (16)
- [💬 通讯与协作 (Communication & Collaboration)](#comm_collab) (43)
- [📈 效率与项目管理 (Productivity & Project Management)](#prod_pm) (731)
- [📊 市场营销与 CRM (Marketing & CRM)](#marketing_crm) (16)
- [🎨 设计与 UI/UX (Design & UI/UX)](#design_ui) (15)
- [🤖 AI 生成与多媒体 (AI & Media)](#ai_media) (16)
- [📄 文档、表格与知识库 (Documents, Spreadsheets & Knowledge)](#docs_data) (5)
- [🔌 其他自动化扩展 (Other Integrations)](#other) (18)

---

## <a id='dev_code'></a>🔧 开发工具与代码工作流 (Development & Code Workflow)

### 🔹 "develop-web-game"
- **功能说明**: "Use when Codex is building or iterating on a web game (HTML/JS) and needs a reliable development + testing loop: implement small changes, run a Playwright-based test script with short input bursts and intentional pauses, inspect screenshots/text, and review console errors with render_game_to_text."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "develop-web-game" 执行操作'`

### 🔹 "figma-implement-design"
- **功能说明**: 读取 Figma 设计图并将其 1:1 完美还原转换为生产环境前端代码。
- **使用方法**: `输入指令：'将这个 Figma 链接转换为 React 组件代码'`

### 🔹 "gh-fix-ci"
- **功能说明**: "Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "gh-fix-ci" 执行操作'`

### 🔹 "openai-docs"
- **功能说明**: "Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations (for example: Codex, Responses API, Chat Completions, Apps SDK, Agents SDK, Realtime, model capabilities or limits); prioritize OpenAI docs MCP tools and restrict any fallback browsing to official OpenAI domains."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "openai-docs" 执行操作'`

### 🔹 "playwright"
- **功能说明**: 控制真实浏览器执行网页导航、截图、表单填写和数据抓取等自动化任务。
- **使用方法**: `输入指令：'打开浏览器访问 google.com 帮我搜索一下并截图'`

### 🔹 "security-best-practices"
- **功能说明**: "Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "security-best-practices" 执行操作'`

### 🔹 "security-ownership-map"
- **功能说明**: "Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "security-ownership-map" 执行操作'`

### 🔹 "security-threat-model"
- **功能说明**: "Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "security-threat-model" 执行操作'`

### 🔹 "sentry"
- **功能说明**: "Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry API; perform read-only queries with the bundled script and require `SENTRY_AUTH_TOKEN`."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "sentry" 执行操作'`

### 🔹 "yeet"
- **功能说明**: 一键聚合执行 Git 的 stage、commit、push 操作并自动发起 Pull Request。
- **使用方法**: `输入指令：'代码写完了，yeet 一下'`

### 🔹 appveyor-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Appveyor 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Appveyor 中创建一个...', '查询 Appveyor 的数据'`

### 🔹 buildkite-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Buildkite 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Buildkite 中创建一个...', '查询 Buildkite 的数据'`

### 🔹 codeinterpreter-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Codeinterpreter 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Codeinterpreter 中创建一个...', '查询 Codeinterpreter 的数据'`

### 🔹 codereadr-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Codereadr 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Codereadr 中创建一个...', '查询 Codereadr 的数据'`

### 🔹 connect
- **功能说明**: Connect Claude to any app. Send emails, create issues, post messages, update databases - take real actions across Gmail, Slack, GitHub, Notion, and 1000+ services.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 connect 执行操作'`

### 🔹 connect-apps
- **功能说明**: Connect Claude to external apps like Gmail, Slack, GitHub. Use this skill when the user wants to send emails, create issues, post messages, or take actions in external services.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 connect-apps 执行操作'`

### 🔹 developer-growth-analysis
- **功能说明**: Analyzes your recent Claude Code chat history to identify coding patterns, development gaps, and areas for improvement, curates relevant learning resources from HackerNews, and automatically sends a personalized growth report to your Slack DMs.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 developer-growth-analysis 执行操作'`

### 🔹 domain-name-brainstormer
- **功能说明**: Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.). Saves hours of brainstorming and manual checking.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 domain-name-brainstormer 执行操作'`

### 🔹 figma
- **功能说明**: Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Trigger when a task involves Figma URLs, node IDs, design-to-code implementation, or Figma MCP setup and troubleshooting.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 figma 执行操作'`

### 🔹 gh-address-comments
- **功能说明**: Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 gh-address-comments 执行操作'`

### 🔹 google-maps-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Maps 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Maps 中创建一个...', '查询 Google Maps 的数据'`

### 🔹 LaunchDarkly Automation
- **功能说明**: "Automate LaunchDarkly feature flag management -- list projects and environments, create and delete trigger workflows, and track code references via the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 LaunchDarkly Automation 执行操作'`

### 🔹 lead-research-assistant
- **功能说明**: Identifies high-quality leads for your product or service by analyzing your business, searching for target companies, and providing actionable contact strategies. Perfect for sales, business development, and marketing professionals.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 lead-research-assistant 执行操作'`

### 🔹 linear
- **功能说明**: Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 linear 执行操作'`

### 🔹 logo-dev-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Logo Dev 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Logo Dev 中创建一个...', '查询 Logo Dev 的数据'`

### 🔹 Microsoft Clarity Automation
- **功能说明**: "Automate user behavior analytics with Microsoft Clarity -- export heatmap data, session metrics, and engagement analytics segmented by browser, device, country, source, and more through the Composio Microsoft Clarity integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Microsoft Clarity Automation 执行操作'`

### 🔹 notebooklm
- **功能说明**: Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers from Gemini. Browser automation, library management, persistent auth. Drastically reduced hallucinations through document-only responses.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 notebooklm 执行操作'`

### 🔹 notion-meeting-intelligence
- **功能说明**: Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 notion-meeting-intelligence 执行操作'`

### 🔹 npm-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 NPM 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 NPM 中创建一个...', '查询 NPM 的数据'`

### 🔹 render-deploy
- **功能说明**: Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 render-deploy 执行操作'`

### 🔹 skill-installer
- **功能说明**: Install skills into the global or workspace-specific skills directory from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 skill-installer 执行操作'`

### 🔹 sourcegraph-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sourcegraph 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sourcegraph 中创建一个...', '查询 Sourcegraph 的数据'`

### 🔹 wakatime-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Wakatime 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Wakatime 中创建一个...', '查询 Wakatime 的数据'`

### 🔹 webapp-testing
- **功能说明**: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 webapp-testing 执行操作'`

## <a id='cloud_deploy'></a>☁️ 部署与云服务 (Deployment & Cloud)

### 🔹 "doc"
- **功能说明**: "Use when the task involves reading, creating, or editing `.docx` documents, especially when formatting or layout fidelity matters; prefer `python-docx` plus the bundled `scripts/render_docx.py` for visual checks."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "doc" 执行操作'`

### 🔹 "pdf"
- **功能说明**: "Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "pdf" 执行操作'`

### 🔹 cloudflare-api-key-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cloudflare API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cloudflare API 中创建一个...', '查询 Cloudflare API 的数据'`

### 🔹 cloudflare-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cloudflare 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cloudflare 中创建一个...', '查询 Cloudflare 的数据'`

### 🔹 cloudflare-browser-rendering-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cloudflare Browser Rendering 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cloudflare Browser Rendering 中创建一个...', '查询 Cloudflare Browser Rendering 的数据'`

### 🔹 cloudflare-deploy
- **功能说明**: 将应用程序或基础设施部署到 Cloudflare 服务（如 Workers, Pages）。
- **使用方法**: `输入指令：'帮我把当前目录的项目部署到 Cloudflare'`

### 🔹 digital-ocean-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 DigitalOcean 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 DigitalOcean 中创建一个...', '查询 DigitalOcean 的数据'`

### 🔹 Docker Hub Automation
- **功能说明**: "Automate Docker Hub operations -- manage organizations, repositories, teams, members, and webhooks via the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Docker Hub Automation 执行操作'`

### 🔹 docker_hub-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Docker Hub 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Docker Hub 中创建一个...', '查询 Docker Hub 的数据'`

### 🔹 jigsawstack-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Jigsawstack 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Jigsawstack 中创建一个...', '查询 Jigsawstack 的数据'`

### 🔹 Neon Automation
- **功能说明**: "Automate Neon serverless Postgres operations -- manage projects, branches, databases, roles, and connection URIs via the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Neon Automation 执行操作'`

### 🔹 netlify-deploy
- **功能说明**: Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 netlify-deploy 执行操作'`

### 🔹 prerender-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Prerender 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Prerender 中创建一个...', '查询 Prerender 的数据'`

### 🔹 renderform-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Renderform 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Renderform 中创建一个...', '查询 Renderform 的数据'`

### 🔹 turso-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Turso 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Turso 中创建一个...', '查询 Turso 的数据'`

### 🔹 vercel-deploy
- **功能说明**: Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 vercel-deploy 执行操作'`

## <a id='comm_collab'></a>💬 通讯与协作 (Communication & Collaboration)

### 🔹 -2chat-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 2chat 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 2chat 中创建一个...', '查询 2chat 的数据'`

### 🔹 agencyzoom-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Agencyzoom 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Agencyzoom 中创建一个...', '查询 Agencyzoom 的数据'`

### 🔹 agent-mail-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Agent Mail 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Agent Mail 中创建一个...', '查询 Agent Mail 的数据'`

### 🔹 benchmark-email-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Benchmark Email 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Benchmark Email 中创建一个...', '查询 Benchmark Email 的数据'`

### 🔹 bigmailer-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bigmailer 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bigmailer 中创建一个...', '查询 Bigmailer 的数据'`

### 🔹 chatbotkit-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Chatbotkit 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Chatbotkit 中创建一个...', '查询 Chatbotkit 的数据'`

### 🔹 chatfai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Chatfai 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Chatfai 中创建一个...', '查询 Chatfai 的数据'`

### 🔹 chatwork-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Chatwork 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Chatwork 中创建一个...', '查询 Chatwork 的数据'`

### 🔹 Customer.io Automation
- **功能说明**: "Automate customer engagement workflows including broadcast triggers, message analytics, segment management, and newsletter tracking through Customer.io via Composio"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Customer.io Automation 执行操作'`

### 🔹 discordbot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Discordbot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Discordbot 中创建一个...', '查询 Discordbot 的数据'`

### 🔹 emailable-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Emailable 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Emailable 中创建一个...', '查询 Emailable 的数据'`

### 🔹 emaillistverify-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Emaillistverify 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Emaillistverify 中创建一个...', '查询 Emaillistverify 的数据'`

### 🔹 emailoctopus-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Emailoctopus 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Emailoctopus 中创建一个...', '查询 Emailoctopus 的数据'`

### 🔹 enginemailer-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Enginemailer 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Enginemailer 中创建一个...', '查询 Enginemailer 的数据'`

### 🔹 findymail-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Findymail 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Findymail 中创建一个...', '查询 Findymail 的数据'`

### 🔹 Gorgias Automation
- **功能说明**: "Automate e-commerce customer support workflows in Gorgias -- manage tickets, customers, tags, and teams through natural language commands."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Gorgias Automation 执行操作'`

### 🔹 GroqCloud Automation
- **功能说明**: "Automate AI inference, chat completions, audio translation, and TTS voice management through GroqCloud's high-performance API via Composio"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 GroqCloud Automation 执行操作'`

### 🔹 Hunter Automation
- **功能说明**: "Automate Hunter.io email intelligence -- search domains for email addresses, find specific contacts, verify email deliverability, manage leads, and monitor account usage -- using natural language through the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Hunter Automation 执行操作'`

### 🔹 Instantly Automation
- **功能说明**: "Automate Instantly cold email outreach -- manage campaigns, sending accounts, lead lists, bulk lead imports, and campaign analytics -- using natural language through the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Instantly Automation 执行操作'`

### 🔹 mailbluster-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mailbluster 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mailbluster 中创建一个...', '查询 Mailbluster 的数据'`

### 🔹 mailboxlayer-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mailboxlayer 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mailboxlayer 中创建一个...', '查询 Mailboxlayer 的数据'`

### 🔹 mailcheck-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mailcheck 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mailcheck 中创建一个...', '查询 Mailcheck 的数据'`

### 🔹 mailcoach-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mailcoach 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mailcoach 中创建一个...', '查询 Mailcoach 的数据'`

### 🔹 MailerLite Automation
- **功能说明**: "Automate email marketing workflows including subscriber management, campaign analytics, group segmentation, and account monitoring through MailerLite via Composio"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 MailerLite Automation 执行操作'`

### 🔹 mailersend-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mailersend 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mailersend 中创建一个...', '查询 Mailersend 的数据'`

### 🔹 mails-so-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mails So 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mails So 中创建一个...', '查询 Mails So 的数据'`

### 🔹 mailsoftly-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mailsoftly 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mailsoftly 中创建一个...', '查询 Mailsoftly 的数据'`

### 🔹 many-chat-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 ManyChat 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 ManyChat 中创建一个...', '查询 ManyChat 的数据'`

### 🔹 many_chat-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 ManyChat 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 ManyChat 中创建一个...', '查询 ManyChat 的数据'`

### 🔹 notion-knowledge-capture
- **功能说明**: Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 notion-knowledge-capture 执行操作'`

### 🔹 proxiedmail-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Proxiedmail 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Proxiedmail 中创建一个...', '查询 Proxiedmail 的数据'`

### 🔹 ring_central-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 RingCentral 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 RingCentral 中创建一个...', '查询 RingCentral 的数据'`

### 🔹 sendbird-ai-chabot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sendbird AI Chabot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sendbird AI Chabot 中创建一个...', '查询 Sendbird AI Chabot 的数据'`

### 🔹 sendbird-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sendbird 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sendbird 中创建一个...', '查询 Sendbird 的数据'`

### 🔹 skill-share
- **功能说明**: A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 skill-share 执行操作'`

### 🔹 slack-gif-creator
- **功能说明**: Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. This skill applies when users request animated GIFs or emoji animations for Slack from descriptions like "make me a GIF for Slack of X doing Y".
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 slack-gif-creator 执行操作'`

### 🔹 slackbot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Slackbot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Slackbot 中创建一个...', '查询 Slackbot 的数据'`

### 🔹 superchat-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Superchat 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Superchat 中创建一个...', '查询 Superchat 的数据'`

### 🔹 verifiedemail-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Verifiedemail 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Verifiedemail 中创建一个...', '查询 Verifiedemail 的数据'`

### 🔹 Webex Automation
- **功能说明**: "Automate Cisco Webex messaging, rooms, teams, webhooks, and people management through natural language commands"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Webex Automation 执行操作'`

### 🔹 zoho-mail-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoho Mail 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoho Mail 中创建一个...', '查询 Zoho Mail 的数据'`

### 🔹 zoho_mail-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoho Mail 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoho Mail 中创建一个...', '查询 Zoho Mail 的数据'`

### 🔹 zoominfo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoominfo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoominfo 中创建一个...', '查询 Zoominfo 的数据'`

## <a id='prod_pm'></a>📈 效率与项目管理 (Productivity & Project Management)

### 🔹 "spreadsheet"
- **功能说明**: "Use when tasks involve creating, editing, analyzing, or formatting spreadsheets (`.xlsx`, `.csv`, `.tsv`) using Python (`openpyxl`, `pandas`), especially when formulas, references, and formatting need to be preserved and verified."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "spreadsheet" 执行操作'`

### 🔹 -21risk-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 21risk 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 21risk 中创建一个...', '查询 21risk 的数据'`

### 🔹 ably-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ably 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ably 中创建一个...', '查询 Ably 的数据'`

### 🔹 abstract-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Abstract 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Abstract 中创建一个...', '查询 Abstract 的数据'`

### 🔹 abuselpdb-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Abuselpdb 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Abuselpdb 中创建一个...', '查询 Abuselpdb 的数据'`

### 🔹 abyssale-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Abyssale 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Abyssale 中创建一个...', '查询 Abyssale 的数据'`

### 🔹 accelo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Accelo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Accelo 中创建一个...', '查询 Accelo 的数据'`

### 🔹 accredible-certificates-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Accredible Certificates 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Accredible Certificates 中创建一个...', '查询 Accredible Certificates 的数据'`

### 🔹 acculynx-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Acculynx 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Acculynx 中创建一个...', '查询 Acculynx 的数据'`

### 🔹 active-campaign-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 ActiveCampaign 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 ActiveCampaign 中创建一个...', '查询 ActiveCampaign 的数据'`

### 🔹 addresszen-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Addresszen 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Addresszen 中创建一个...', '查询 Addresszen 的数据'`

### 🔹 adobe-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Adobe 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Adobe 中创建一个...', '查询 Adobe 的数据'`

### 🔹 adrapid-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Adrapid 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Adrapid 中创建一个...', '查询 Adrapid 的数据'`

### 🔹 adyntel-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Adyntel 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Adyntel 中创建一个...', '查询 Adyntel 的数据'`

### 🔹 aero-workflow-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Aero Workflow 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Aero Workflow 中创建一个...', '查询 Aero Workflow 的数据'`

### 🔹 aeroleads-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Aeroleads 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Aeroleads 中创建一个...', '查询 Aeroleads 的数据'`

### 🔹 affinda-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Affinda 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Affinda 中创建一个...', '查询 Affinda 的数据'`

### 🔹 affinity-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Affinity 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Affinity 中创建一个...', '查询 Affinity 的数据'`

### 🔹 agentql-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Agentql 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Agentql 中创建一个...', '查询 Agentql 的数据'`

### 🔹 agenty-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Agenty 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Agenty 中创建一个...', '查询 Agenty 的数据'`

### 🔹 agiled-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Agiled 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Agiled 中创建一个...', '查询 Agiled 的数据'`

### 🔹 agility-cms-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Agility CMS 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Agility CMS 中创建一个...', '查询 Agility CMS 的数据'`

### 🔹 ai-ml-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 AI ML API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 AI ML API 中创建一个...', '查询 AI ML API 的数据'`

### 🔹 aivoov-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Aivoov 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Aivoov 中创建一个...', '查询 Aivoov 的数据'`

### 🔹 alchemy-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Alchemy 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Alchemy 中创建一个...', '查询 Alchemy 的数据'`

### 🔹 algodocs-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Algodocs 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Algodocs 中创建一个...', '查询 Algodocs 的数据'`

### 🔹 algolia-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Algolia 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Algolia 中创建一个...', '查询 Algolia 的数据'`

### 🔹 all-images-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 All Images AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 All Images AI 中创建一个...', '查询 All Images AI 的数据'`

### 🔹 alpha-vantage-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Alpha Vantage 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Alpha Vantage 中创建一个...', '查询 Alpha Vantage 的数据'`

### 🔹 altoviz-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Altoviz 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Altoviz 中创建一个...', '查询 Altoviz 的数据'`

### 🔹 alttext-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Alttext AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Alttext AI 中创建一个...', '查询 Alttext AI 的数据'`

### 🔹 amara-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Amara 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Amara 中创建一个...', '查询 Amara 的数据'`

### 🔹 amazon-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Amazon 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Amazon 中创建一个...', '查询 Amazon 的数据'`

### 🔹 ambee-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ambee 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ambee 中创建一个...', '查询 Ambee 的数据'`

### 🔹 ambient-weather-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ambient Weather 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ambient Weather 中创建一个...', '查询 Ambient Weather 的数据'`

### 🔹 amcards-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Amcards 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Amcards 中创建一个...', '查询 Amcards 的数据'`

### 🔹 anchor-browser-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Anchor Browser 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Anchor Browser 中创建一个...', '查询 Anchor Browser 的数据'`

### 🔹 anonyflow-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Anonyflow 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Anonyflow 中创建一个...', '查询 Anonyflow 的数据'`

### 🔹 anthropic-administrator-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Anthropic Admin 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Anthropic Admin 中创建一个...', '查询 Anthropic Admin 的数据'`

### 🔹 anthropic_administrator-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Anthropic Admin 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Anthropic Admin 中创建一个...', '查询 Anthropic Admin 的数据'`

### 🔹 apaleo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Apaleo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Apaleo 中创建一个...', '查询 Apaleo 的数据'`

### 🔹 apex27-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Apex27 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Apex27 中创建一个...', '查询 Apex27 的数据'`

### 🔹 api-bible-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 API Bible 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 API Bible 中创建一个...', '查询 API Bible 的数据'`

### 🔹 api-labz-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 API Labz 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 API Labz 中创建一个...', '查询 API Labz 的数据'`

### 🔹 api-ninjas-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 API Ninjas 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 API Ninjas 中创建一个...', '查询 API Ninjas 的数据'`

### 🔹 api-sports-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 API Sports 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 API Sports 中创建一个...', '查询 API Sports 的数据'`

### 🔹 api2pdf-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Api2pdf 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Api2pdf 中创建一个...', '查询 Api2pdf 的数据'`

### 🔹 apiflash-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Apiflash 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Apiflash 中创建一个...', '查询 Apiflash 的数据'`

### 🔹 Apify Automation
- **功能说明**: "Automate web scraping and data extraction with Apify -- run Actors, manage datasets, create reusable tasks, and retrieve crawl results through the Composio Apify integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Apify Automation 执行操作'`

### 🔹 apilio-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Apilio 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Apilio 中创建一个...', '查询 Apilio 的数据'`

### 🔹 apipie-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Apipie AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Apipie AI 中创建一个...', '查询 Apipie AI 的数据'`

### 🔹 apitemplate-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Apitemplate IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Apitemplate IO 中创建一个...', '查询 Apitemplate IO 的数据'`

### 🔹 apiverve-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Apiverve 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Apiverve 中创建一个...', '查询 Apiverve 的数据'`

### 🔹 appcircle-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Appcircle 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Appcircle 中创建一个...', '查询 Appcircle 的数据'`

### 🔹 appdrag-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Appdrag 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Appdrag 中创建一个...', '查询 Appdrag 的数据'`

### 🔹 appointo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Appointo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Appointo 中创建一个...', '查询 Appointo 的数据'`

### 🔹 appsflyer-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Appsflyer 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Appsflyer 中创建一个...', '查询 Appsflyer 的数据'`

### 🔹 aryn-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Aryn 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Aryn 中创建一个...', '查询 Aryn 的数据'`

### 🔹 ascora-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ascora 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ascora 中创建一个...', '查询 Ascora 的数据'`

### 🔹 asin-data-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Asin Data API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Asin Data API 中创建一个...', '查询 Asin Data API 的数据'`

### 🔹 astica-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Astica AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Astica AI 中创建一个...', '查询 Astica AI 的数据'`

### 🔹 async-interview-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Async Interview 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Async Interview 中创建一个...', '查询 Async Interview 的数据'`

### 🔹 atlassian-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Atlassian 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Atlassian 中创建一个...', '查询 Atlassian 的数据'`

### 🔹 auth0-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Auth0 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Auth0 中创建一个...', '查询 Auth0 的数据'`

### 🔹 autobound-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Autobound 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Autobound 中创建一个...', '查询 Autobound 的数据'`

### 🔹 autom-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Autom 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Autom 中创建一个...', '查询 Autom 的数据'`

### 🔹 axonaut-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Axonaut 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Axonaut 中创建一个...', '查询 Axonaut 的数据'`

### 🔹 ayrshare-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ayrshare 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ayrshare 中创建一个...', '查询 Ayrshare 的数据'`

### 🔹 backendless-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Backendless 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Backendless 中创建一个...', '查询 Backendless 的数据'`

### 🔹 bannerbear-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bannerbear 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bannerbear 中创建一个...', '查询 Bannerbear 的数据'`

### 🔹 bart-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bart 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bart 中创建一个...', '查询 Bart 的数据'`

### 🔹 baselinker-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Baselinker 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Baselinker 中创建一个...', '查询 Baselinker 的数据'`

### 🔹 baserow-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Baserow 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Baserow 中创建一个...', '查询 Baserow 的数据'`

### 🔹 basin-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Basin 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Basin 中创建一个...', '查询 Basin 的数据'`

### 🔹 battlenet-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Battlenet 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Battlenet 中创建一个...', '查询 Battlenet 的数据'`

### 🔹 beaconchain-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Beaconchain 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Beaconchain 中创建一个...', '查询 Beaconchain 的数据'`

### 🔹 beaconstac-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Beaconstac 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Beaconstac 中创建一个...', '查询 Beaconstac 的数据'`

### 🔹 beamer-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Beamer 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Beamer 中创建一个...', '查询 Beamer 的数据'`

### 🔹 beeminder-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Beeminder 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Beeminder 中创建一个...', '查询 Beeminder 的数据'`

### 🔹 bench-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bench 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bench 中创建一个...', '查询 Bench 的数据'`

### 🔹 benzinga-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Benzinga 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Benzinga 中创建一个...', '查询 Benzinga 的数据'`

### 🔹 bestbuy-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bestbuy 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bestbuy 中创建一个...', '查询 Bestbuy 的数据'`

### 🔹 better-proposals-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Better Proposals 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Better Proposals 中创建一个...', '查询 Better Proposals 的数据'`

### 🔹 better-stack-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Better Stack 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Better Stack 中创建一个...', '查询 Better Stack 的数据'`

### 🔹 bidsketch-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bidsketch 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bidsketch 中创建一个...', '查询 Bidsketch 的数据'`

### 🔹 big-data-cloud-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Big Data Cloud 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Big Data Cloud 中创建一个...', '查询 Big Data Cloud 的数据'`

### 🔹 bigml-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bigml 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bigml 中创建一个...', '查询 Bigml 的数据'`

### 🔹 bigpicture-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bigpicture IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bigpicture IO 中创建一个...', '查询 Bigpicture IO 的数据'`

### 🔹 bitquery-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bitquery 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bitquery 中创建一个...', '查询 Bitquery 的数据'`

### 🔹 bitwarden-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bitwarden 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bitwarden 中创建一个...', '查询 Bitwarden 的数据'`

### 🔹 blackbaud-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Blackbaud 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Blackbaud 中创建一个...', '查询 Blackbaud 的数据'`

### 🔹 blackboard-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Blackboard 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Blackboard 中创建一个...', '查询 Blackboard 的数据'`

### 🔹 blocknative-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Blocknative 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Blocknative 中创建一个...', '查询 Blocknative 的数据'`

### 🔹 boldsign-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Boldsign 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Boldsign 中创建一个...', '查询 Boldsign 的数据'`

### 🔹 bolna-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bolna 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bolna 中创建一个...', '查询 Bolna 的数据'`

### 🔹 boloforms-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Boloforms 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Boloforms 中创建一个...', '查询 Boloforms 的数据'`

### 🔹 bolt-iot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bolt Iot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bolt Iot 中创建一个...', '查询 Bolt Iot 的数据'`

### 🔹 bonsai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bonsai 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bonsai 中创建一个...', '查询 Bonsai 的数据'`

### 🔹 bookingmood-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bookingmood 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bookingmood 中创建一个...', '查询 Bookingmood 的数据'`

### 🔹 booqable-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Booqable 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Booqable 中创建一个...', '查询 Booqable 的数据'`

### 🔹 borneo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Borneo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Borneo 中创建一个...', '查询 Borneo 的数据'`

### 🔹 botbaba-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Botbaba 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Botbaba 中创建一个...', '查询 Botbaba 的数据'`

### 🔹 botpress-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Botpress 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Botpress 中创建一个...', '查询 Botpress 的数据'`

### 🔹 botsonic-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Botsonic 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Botsonic 中创建一个...', '查询 Botsonic 的数据'`

### 🔹 botstar-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Botstar 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Botstar 中创建一个...', '查询 Botstar 的数据'`

### 🔹 bouncer-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bouncer 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bouncer 中创建一个...', '查询 Bouncer 的数据'`

### 🔹 boxhero-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Boxhero 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Boxhero 中创建一个...', '查询 Boxhero 的数据'`

### 🔹 brandfetch-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Brandfetch 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Brandfetch 中创建一个...', '查询 Brandfetch 的数据'`

### 🔹 breeze-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Breeze 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Breeze 中创建一个...', '查询 Breeze 的数据'`

### 🔹 breezy-hr-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Breezy HR 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Breezy HR 中创建一个...', '查询 Breezy HR 的数据'`

### 🔹 brex-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Brex 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Brex 中创建一个...', '查询 Brex 的数据'`

### 🔹 brex-staging-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Brex Staging 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Brex Staging 中创建一个...', '查询 Brex Staging 的数据'`

### 🔹 brightdata-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Brightdata 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Brightdata 中创建一个...', '查询 Brightdata 的数据'`

### 🔹 brightpearl-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Brightpearl 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Brightpearl 中创建一个...', '查询 Brightpearl 的数据'`

### 🔹 brilliant-directories-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Brilliant Directories 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Brilliant Directories 中创建一个...', '查询 Brilliant Directories 的数据'`

### 🔹 browseai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Browseai 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Browseai 中创建一个...', '查询 Browseai 的数据'`

### 🔹 browser-tool-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Browser Tool 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Browser Tool 中创建一个...', '查询 Browser Tool 的数据'`

### 🔹 browserbase-tool-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Browserbase Tool 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Browserbase Tool 中创建一个...', '查询 Browserbase Tool 的数据'`

### 🔹 browserhub-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Browserhub 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Browserhub 中创建一个...', '查询 Browserhub 的数据'`

### 🔹 browserless-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Browserless 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Browserless 中创建一个...', '查询 Browserless 的数据'`

### 🔹 btcpay-server-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Btcpay Server 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Btcpay Server 中创建一个...', '查询 Btcpay Server 的数据'`

### 🔹 bubble-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bubble 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bubble 中创建一个...', '查询 Bubble 的数据'`

### 🔹 bugbug-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bugbug 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bugbug 中创建一个...', '查询 Bugbug 的数据'`

### 🔹 bugherd-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bugherd 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bugherd 中创建一个...', '查询 Bugherd 的数据'`

### 🔹 bugsnag-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bugsnag 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bugsnag 中创建一个...', '查询 Bugsnag 的数据'`

### 🔹 builtwith-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Builtwith 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Builtwith 中创建一个...', '查询 Builtwith 的数据'`

### 🔹 bunnycdn-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Bunnycdn 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Bunnycdn 中创建一个...', '查询 Bunnycdn 的数据'`

### 🔹 byteforms-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Byteforms 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Byteforms 中创建一个...', '查询 Byteforms 的数据'`

### 🔹 cabinpanda-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cabinpanda 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cabinpanda 中创建一个...', '查询 Cabinpanda 的数据'`

### 🔹 cal-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cal 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cal 中创建一个...', '查询 Cal 的数据'`

### 🔹 calendarhero-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Calendarhero 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Calendarhero 中创建一个...', '查询 Calendarhero 的数据'`

### 🔹 callerapi-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Callerapi 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Callerapi 中创建一个...', '查询 Callerapi 的数据'`

### 🔹 callingly-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Callingly 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Callingly 中创建一个...', '查询 Callingly 的数据'`

### 🔹 callpage-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Callpage 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Callpage 中创建一个...', '查询 Callpage 的数据'`

### 🔹 campaign-cleaner-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Campaign Cleaner 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Campaign Cleaner 中创建一个...', '查询 Campaign Cleaner 的数据'`

### 🔹 campayn-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Campayn 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Campayn 中创建一个...', '查询 Campayn 的数据'`

### 🔹 canny-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Canny 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Canny 中创建一个...', '查询 Canny 的数据'`

### 🔹 canvas-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Canvas 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Canvas 中创建一个...', '查询 Canvas 的数据'`

### 🔹 Capsule CRM Automation
- **功能说明**: "Automate Capsule CRM operations -- manage contacts (parties), run structured filter queries, track tasks and projects, log entries, and handle organizations -- using natural language through the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Capsule CRM Automation 执行操作'`

### 🔹 capsule_crm-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Capsule CRM 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Capsule CRM 中创建一个...', '查询 Capsule CRM 的数据'`

### 🔹 carbone-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Carbone 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Carbone 中创建一个...', '查询 Carbone 的数据'`

### 🔹 cardly-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cardly 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cardly 中创建一个...', '查询 Cardly 的数据'`

### 🔹 castingwords-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Castingwords 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Castingwords 中创建一个...', '查询 Castingwords 的数据'`

### 🔹 cats-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cats 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cats 中创建一个...', '查询 Cats 的数据'`

### 🔹 cdr-platform-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cdr Platform 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cdr Platform 中创建一个...', '查询 Cdr Platform 的数据'`

### 🔹 census-bureau-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Census Bureau 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Census Bureau 中创建一个...', '查询 Census Bureau 的数据'`

### 🔹 centralstationcrm-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Centralstationcrm 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Centralstationcrm 中创建一个...', '查询 Centralstationcrm 的数据'`

### 🔹 certifier-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Certifier 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Certifier 中创建一个...', '查询 Certifier 的数据'`

### 🔹 chaser-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Chaser 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Chaser 中创建一个...', '查询 Chaser 的数据'`

### 🔹 chmeetings-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Chmeetings 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Chmeetings 中创建一个...', '查询 Chmeetings 的数据'`

### 🔹 cincopa-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cincopa 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cincopa 中创建一个...', '查询 Cincopa 的数据'`

### 🔹 claid-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Claid AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Claid AI 中创建一个...', '查询 Claid AI 的数据'`

### 🔹 classmarker-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Classmarker 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Classmarker 中创建一个...', '查询 Classmarker 的数据'`

### 🔹 clearout-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Clearout 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Clearout 中创建一个...', '查询 Clearout 的数据'`

### 🔹 clickmeeting-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Clickmeeting 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Clickmeeting 中创建一个...', '查询 Clickmeeting 的数据'`

### 🔹 Clockify Automation
- **功能说明**: "Automate time tracking workflows in Clockify -- create and manage time entries, workspaces, and users through natural language commands."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Clockify Automation 执行操作'`

### 🔹 cloudcart-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cloudcart 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cloudcart 中创建一个...', '查询 Cloudcart 的数据'`

### 🔹 cloudconvert-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cloudconvert 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cloudconvert 中创建一个...', '查询 Cloudconvert 的数据'`

### 🔹 cloudlayer-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cloudlayer 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cloudlayer 中创建一个...', '查询 Cloudlayer 的数据'`

### 🔹 cloudpress-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cloudpress 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cloudpress 中创建一个...', '查询 Cloudpress 的数据'`

### 🔹 coassemble-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Coassemble 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Coassemble 中创建一个...', '查询 Coassemble 的数据'`

### 🔹 codacy-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Codacy 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Codacy 中创建一个...', '查询 Codacy 的数据'`

### 🔹 coinmarketcal-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Coinmarketcal 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Coinmarketcal 中创建一个...', '查询 Coinmarketcal 的数据'`

### 🔹 coinmarketcap-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Coinmarketcap 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Coinmarketcap 中创建一个...', '查询 Coinmarketcap 的数据'`

### 🔹 coinranking-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Coinranking 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Coinranking 中创建一个...', '查询 Coinranking 的数据'`

### 🔹 college-football-data-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 College Football Data 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 College Football Data 中创建一个...', '查询 College Football Data 的数据'`

### 🔹 composio-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Composio 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Composio 中创建一个...', '查询 Composio 的数据'`

### 🔹 composio-search-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Composio Search 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Composio Search 中创建一个...', '查询 Composio Search 的数据'`

### 🔹 connecteam-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Connecteam 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Connecteam 中创建一个...', '查询 Connecteam 的数据'`

### 🔹 content-research-writer
- **功能说明**: Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section. Transforms your writing process from solo effort to collaborative partnership.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 content-research-writer 执行操作'`

### 🔹 contentful-graphql-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Contentful Graphql 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Contentful Graphql 中创建一个...', '查询 Contentful Graphql 的数据'`

### 🔹 control-d-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Control D 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Control D 中创建一个...', '查询 Control D 的数据'`

### 🔹 conversion-tools-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Conversion Tools 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Conversion Tools 中创建一个...', '查询 Conversion Tools 的数据'`

### 🔹 convertapi-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Convertapi 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Convertapi 中创建一个...', '查询 Convertapi 的数据'`

### 🔹 conveyor-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Conveyor 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Conveyor 中创建一个...', '查询 Conveyor 的数据'`

### 🔹 convolo-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Convolo AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Convolo AI 中创建一个...', '查询 Convolo AI 的数据'`

### 🔹 corrently-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Corrently 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Corrently 中创建一个...', '查询 Corrently 的数据'`

### 🔹 countdown-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Countdown API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Countdown API 中创建一个...', '查询 Countdown API 的数据'`

### 🔹 coupa-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Coupa 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Coupa 中创建一个...', '查询 Coupa 的数据'`

### 🔹 craftmypdf-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Craftmypdf 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Craftmypdf 中创建一个...', '查询 Craftmypdf 的数据'`

### 🔹 crowdin-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Crowdin 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Crowdin 中创建一个...', '查询 Crowdin 的数据'`

### 🔹 crustdata-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Crustdata 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Crustdata 中创建一个...', '查询 Crustdata 的数据'`

### 🔹 cults-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cults 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cults 中创建一个...', '查询 Cults 的数据'`

### 🔹 curated-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Curated 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Curated 中创建一个...', '查询 Curated 的数据'`

### 🔹 currents-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Currents API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Currents API 中创建一个...', '查询 Currents API 的数据'`

### 🔹 customgpt-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Customgpt 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Customgpt 中创建一个...', '查询 Customgpt 的数据'`

### 🔹 customjs-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Customjs 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Customjs 中创建一个...', '查询 Customjs 的数据'`

### 🔹 cutt-ly-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Cutt Ly 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Cutt Ly 中创建一个...', '查询 Cutt Ly 的数据'`

### 🔹 d2lbrightspace-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 D2lbrightspace 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 D2lbrightspace 中创建一个...', '查询 D2lbrightspace 的数据'`

### 🔹 dadata-ru-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dadata Ru 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dadata Ru 中创建一个...', '查询 Dadata Ru 的数据'`

### 🔹 daffy-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Daffy 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Daffy 中创建一个...', '查询 Daffy 的数据'`

### 🔹 dailybot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dailybot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dailybot 中创建一个...', '查询 Dailybot 的数据'`

### 🔹 datagma-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Datagma 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Datagma 中创建一个...', '查询 Datagma 的数据'`

### 🔹 datarobot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Datarobot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Datarobot 中创建一个...', '查询 Datarobot 的数据'`

### 🔹 deadline-funnel-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Deadline Funnel 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Deadline Funnel 中创建一个...', '查询 Deadline Funnel 的数据'`

### 🔹 deel-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Deel 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Deel 中创建一个...', '查询 Deel 的数据'`

### 🔹 deepgram-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Deepgram 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Deepgram 中创建一个...', '查询 Deepgram 的数据'`

### 🔹 demio-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Demio 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Demio 中创建一个...', '查询 Demio 的数据'`

### 🔹 desktime-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Desktime 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Desktime 中创建一个...', '查询 Desktime 的数据'`

### 🔹 detrack-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Detrack 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Detrack 中创建一个...', '查询 Detrack 的数据'`

### 🔹 dialmycalls-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dialmycalls 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dialmycalls 中创建一个...', '查询 Dialmycalls 的数据'`

### 🔹 dialpad-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dialpad 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dialpad 中创建一个...', '查询 Dialpad 的数据'`

### 🔹 dictionary-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dictionary API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dictionary API 中创建一个...', '查询 Dictionary API 的数据'`

### 🔹 diffbot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Diffbot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Diffbot 中创建一个...', '查询 Diffbot 的数据'`

### 🔹 digicert-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Digicert 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Digicert 中创建一个...', '查询 Digicert 的数据'`

### 🔹 dnsfilter-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dnsfilter 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dnsfilter 中创建一个...', '查询 Dnsfilter 的数据'`

### 🔹 dock-certs-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dock Certs 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dock Certs 中创建一个...', '查询 Dock Certs 的数据'`

### 🔹 docmosis-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Docmosis 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Docmosis 中创建一个...', '查询 Docmosis 的数据'`

### 🔹 docnify-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Docnify 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Docnify 中创建一个...', '查询 Docnify 的数据'`

### 🔹 docsbot-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Docsbot AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Docsbot AI 中创建一个...', '查询 Docsbot AI 的数据'`

### 🔹 docsumo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Docsumo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Docsumo 中创建一个...', '查询 Docsumo 的数据'`

### 🔹 docugenerate-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Docugenerate 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Docugenerate 中创建一个...', '查询 Docugenerate 的数据'`

### 🔹 documenso-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Documenso 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Documenso 中创建一个...', '查询 Documenso 的数据'`

### 🔹 documint-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Documint 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Documint 中创建一个...', '查询 Documint 的数据'`

### 🔹 docupilot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Docupilot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Docupilot 中创建一个...', '查询 Docupilot 的数据'`

### 🔹 docupost-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Docupost 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Docupost 中创建一个...', '查询 Docupost 的数据'`

### 🔹 docuseal-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Docuseal 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Docuseal 中创建一个...', '查询 Docuseal 的数据'`

### 🔹 doppler-marketing-automation-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Doppler Marketing Automation 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Doppler Marketing Automation 中创建一个...', '查询 Doppler Marketing Automation 的数据'`

### 🔹 doppler-secretops-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Doppler Secretops 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Doppler Secretops 中创建一个...', '查询 Doppler Secretops 的数据'`

### 🔹 dotsimple-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dotsimple 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dotsimple 中创建一个...', '查询 Dotsimple 的数据'`

### 🔹 dovetail-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dovetail 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dovetail 中创建一个...', '查询 Dovetail 的数据'`

### 🔹 dpd2-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dpd2 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dpd2 中创建一个...', '查询 Dpd2 的数据'`

### 🔹 draftable-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Draftable 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Draftable 中创建一个...', '查询 Draftable 的数据'`

### 🔹 dreamstudio-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dreamstudio 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dreamstudio 中创建一个...', '查询 Dreamstudio 的数据'`

### 🔹 drip-jobs-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Drip Jobs 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Drip Jobs 中创建一个...', '查询 Drip Jobs 的数据'`

### 🔹 dripcel-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dripcel 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dripcel 中创建一个...', '查询 Dripcel 的数据'`

### 🔹 dromo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dromo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dromo 中创建一个...', '查询 Dromo 的数据'`

### 🔹 dropbox-sign-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dropbox Sign 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dropbox Sign 中创建一个...', '查询 Dropbox Sign 的数据'`

### 🔹 dropcontact-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dropcontact 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dropcontact 中创建一个...', '查询 Dropcontact 的数据'`

### 🔹 dungeon-fighter-online-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Dungeon Fighter Online 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Dungeon Fighter Online 中创建一个...', '查询 Dungeon Fighter Online 的数据'`

### 🔹 echtpost-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Echtpost 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Echtpost 中创建一个...', '查询 Echtpost 的数据'`

### 🔹 elorus-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Elorus 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Elorus 中创建一个...', '查询 Elorus 的数据'`

### 🔹 emelia-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Emelia 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Emelia 中创建一个...', '查询 Emelia 的数据'`

### 🔹 encodian-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Encodian 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Encodian 中创建一个...', '查询 Encodian 的数据'`

### 🔹 endorsal-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Endorsal 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Endorsal 中创建一个...', '查询 Endorsal 的数据'`

### 🔹 enigma-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Enigma 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Enigma 中创建一个...', '查询 Enigma 的数据'`

### 🔹 entelligence-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Entelligence 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Entelligence 中创建一个...', '查询 Entelligence 的数据'`

### 🔹 eodhd-apis-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Eodhd Apis 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Eodhd Apis 中创建一个...', '查询 Eodhd Apis 的数据'`

### 🔹 epic-games-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Epic Games 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Epic Games 中创建一个...', '查询 Epic Games 的数据'`

### 🔹 esignatures-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Esignatures IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Esignatures IO 中创建一个...', '查询 Esignatures IO 的数据'`

### 🔹 espocrm-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Espocrm 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Espocrm 中创建一个...', '查询 Espocrm 的数据'`

### 🔹 esputnik-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Esputnik 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Esputnik 中创建一个...', '查询 Esputnik 的数据'`

### 🔹 etermin-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Etermin 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Etermin 中创建一个...', '查询 Etermin 的数据'`

### 🔹 evenium-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Evenium 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Evenium 中创建一个...', '查询 Evenium 的数据'`

### 🔹 eventee-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Eventee 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Eventee 中创建一个...', '查询 Eventee 的数据'`

### 🔹 eventzilla-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Eventzilla 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Eventzilla 中创建一个...', '查询 Eventzilla 的数据'`

### 🔹 everhour-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Everhour 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Everhour 中创建一个...', '查询 Everhour 的数据'`

### 🔹 eversign-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Eversign 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Eversign 中创建一个...', '查询 Eversign 的数据'`

### 🔹 exa-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Exa 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Exa 中创建一个...', '查询 Exa 的数据'`

### 🔹 exist-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Exist 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Exist 中创建一个...', '查询 Exist 的数据'`

### 🔹 expofp-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Expofp 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Expofp 中创建一个...', '查询 Expofp 的数据'`

### 🔹 extracta-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Extracta AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Extracta AI 中创建一个...', '查询 Extracta AI 的数据'`

### 🔹 faceup-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Faceup 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Faceup 中创建一个...', '查询 Faceup 的数据'`

### 🔹 factorial-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Factorial 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Factorial 中创建一个...', '查询 Factorial 的数据'`

### 🔹 feathery-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Feathery 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Feathery 中创建一个...', '查询 Feathery 的数据'`

### 🔹 felt-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Felt 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Felt 中创建一个...', '查询 Felt 的数据'`

### 🔹 fibery-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fibery 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fibery 中创建一个...', '查询 Fibery 的数据'`

### 🔹 fidel-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fidel API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fidel API 中创建一个...', '查询 Fidel API 的数据'`

### 🔹 file-organizer
- **功能说明**: 智能分析并整理你的电脑文件与文件夹，寻找重复项，重建目录结构。
- **使用方法**: `输入指令：'帮我把 Downloads 文件夹里的东西按日期和类型整理清楚'`

### 🔹 files-com-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Files Com 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Files Com 中创建一个...', '查询 Files Com 的数据'`

### 🔹 fillout-forms-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fillout 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fillout 中创建一个...', '查询 Fillout 的数据'`

### 🔹 fillout_forms-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fillout 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fillout 中创建一个...', '查询 Fillout 的数据'`

### 🔹 finage-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Finage 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Finage 中创建一个...', '查询 Finage 的数据'`

### 🔹 finerworks-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Finerworks 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Finerworks 中创建一个...', '查询 Finerworks 的数据'`

### 🔹 fingertip-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fingertip 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fingertip 中创建一个...', '查询 Fingertip 的数据'`

### 🔹 finmei-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Finmei 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Finmei 中创建一个...', '查询 Finmei 的数据'`

### 🔹 fireberry-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fireberry 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fireberry 中创建一个...', '查询 Fireberry 的数据'`

### 🔹 fireflies-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fireflies 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fireflies 中创建一个...', '查询 Fireflies 的数据'`

### 🔹 firmao-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Firmao 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Firmao 中创建一个...', '查询 Firmao 的数据'`

### 🔹 fitbit-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fitbit 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fitbit 中创建一个...', '查询 Fitbit 的数据'`

### 🔹 fixer-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fixer 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fixer 中创建一个...', '查询 Fixer 的数据'`

### 🔹 fixer-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fixer IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fixer IO 中创建一个...', '查询 Fixer IO 的数据'`

### 🔹 flexisign-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Flexisign 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Flexisign 中创建一个...', '查询 Flexisign 的数据'`

### 🔹 flowiseai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Flowiseai 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Flowiseai 中创建一个...', '查询 Flowiseai 的数据'`

### 🔹 flutterwave-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Flutterwave 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Flutterwave 中创建一个...', '查询 Flutterwave 的数据'`

### 🔹 fluxguard-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fluxguard 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fluxguard 中创建一个...', '查询 Fluxguard 的数据'`

### 🔹 folk-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Folk 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Folk 中创建一个...', '查询 Folk 的数据'`

### 🔹 fomo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fomo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fomo 中创建一个...', '查询 Fomo 的数据'`

### 🔹 forcemanager-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Forcemanager 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Forcemanager 中创建一个...', '查询 Forcemanager 的数据'`

### 🔹 formbricks-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Formbricks 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Formbricks 中创建一个...', '查询 Formbricks 的数据'`

### 🔹 formcarry-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Formcarry 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Formcarry 中创建一个...', '查询 Formcarry 的数据'`

### 🔹 formdesk-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Formdesk 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Formdesk 中创建一个...', '查询 Formdesk 的数据'`

### 🔹 formsite-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Formsite 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Formsite 中创建一个...', '查询 Formsite 的数据'`

### 🔹 foursquare-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Foursquare 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Foursquare 中创建一个...', '查询 Foursquare 的数据'`

### 🔹 fraudlabs-pro-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fraudlabs Pro 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fraudlabs Pro 中创建一个...', '查询 Fraudlabs Pro 的数据'`

### 🔹 FreshBooks Automation
- **功能说明**: "FreshBooks Automation: manage businesses, projects, time tracking, and billing in FreshBooks cloud accounting"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 FreshBooks Automation 执行操作'`

### 🔹 front-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Front 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Front 中创建一个...', '查询 Front 的数据'`

### 🔹 fullenrich-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Fullenrich 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Fullenrich 中创建一个...', '查询 Fullenrich 的数据'`

### 🔹 gagelist-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gagelist 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gagelist 中创建一个...', '查询 Gagelist 的数据'`

### 🔹 gamma-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gamma 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gamma 中创建一个...', '查询 Gamma 的数据'`

### 🔹 gan-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gan AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gan AI 中创建一个...', '查询 Gan AI 的数据'`

### 🔹 gatherup-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gatherup 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gatherup 中创建一个...', '查询 Gatherup 的数据'`

### 🔹 gemini-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gemini 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gemini 中创建一个...', '查询 Gemini 的数据'`

### 🔹 gender-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gender API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gender API 中创建一个...', '查询 Gender API 的数据'`

### 🔹 genderapi-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Genderapi IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Genderapi IO 中创建一个...', '查询 Genderapi IO 的数据'`

### 🔹 genderize-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Genderize 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Genderize 中创建一个...', '查询 Genderize 的数据'`

### 🔹 geoapify-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Geoapify 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Geoapify 中创建一个...', '查询 Geoapify 的数据'`

### 🔹 geocodio-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Geocodio 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Geocodio 中创建一个...', '查询 Geocodio 的数据'`

### 🔹 geokeo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Geokeo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Geokeo 中创建一个...', '查询 Geokeo 的数据'`

### 🔹 getform-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Getform 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Getform 中创建一个...', '查询 Getform 的数据'`

### 🔹 gift-up-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gift Up 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gift Up 中创建一个...', '查询 Gift Up 的数据'`

### 🔹 gigasheet-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gigasheet 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gigasheet 中创建一个...', '查询 Gigasheet 的数据'`

### 🔹 giphy-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Giphy 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Giphy 中创建一个...', '查询 Giphy 的数据'`

### 🔹 gist-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gist 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gist 中创建一个...', '查询 Gist 的数据'`

### 🔹 givebutter-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Givebutter 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Givebutter 中创建一个...', '查询 Givebutter 的数据'`

### 🔹 gladia-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gladia 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gladia 中创建一个...', '查询 Gladia 的数据'`

### 🔹 gleap-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gleap 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gleap 中创建一个...', '查询 Gleap 的数据'`

### 🔹 globalping-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Globalping 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Globalping 中创建一个...', '查询 Globalping 的数据'`

### 🔹 go-to-webinar-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 GoToWebinar 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 GoToWebinar 中创建一个...', '查询 GoToWebinar 的数据'`

### 🔹 godial-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Godial 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Godial 中创建一个...', '查询 Godial 的数据'`

### 🔹 goodbits-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Goodbits 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Goodbits 中创建一个...', '查询 Goodbits 的数据'`

### 🔹 goody-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Goody 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Goody 中创建一个...', '查询 Goody 的数据'`

### 🔹 google-address-validation-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Address Validation 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Address Validation 中创建一个...', '查询 Google Address Validation 的数据'`

### 🔹 google-admin-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Workspace Admin 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Workspace Admin 中创建一个...', '查询 Google Workspace Admin 的数据'`

### 🔹 google-classroom-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Classroom 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Classroom 中创建一个...', '查询 Google Classroom 的数据'`

### 🔹 google-cloud-vision-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Cloud Vision 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Cloud Vision 中创建一个...', '查询 Google Cloud Vision 的数据'`

### 🔹 google-search-console-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Search Console 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Search Console 中创建一个...', '查询 Google Search Console 的数据'`

### 🔹 google_admin-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Admin 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Admin 中创建一个...', '查询 Google Admin 的数据'`

### 🔹 google_classroom-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Classroom 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Classroom 中创建一个...', '查询 Google Classroom 的数据'`

### 🔹 google_maps-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Maps 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Maps 中创建一个...', '查询 Google Maps 的数据'`

### 🔹 google_search_console-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Search Console 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Search Console 中创建一个...', '查询 Google Search Console 的数据'`

### 🔹 googleads-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Ads analytics 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Ads analytics 中创建一个...', '查询 Google Ads analytics 的数据'`

### 🔹 googlebigquery-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google BigQuery 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google BigQuery 中创建一个...', '查询 Google BigQuery 的数据'`

### 🔹 googlecalendar-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Calendar 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Calendar 中创建一个...', '查询 Google Calendar 的数据'`

### 🔹 googledocs-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Docs 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Docs 中创建一个...', '查询 Google Docs 的数据'`

### 🔹 googledrive-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Drive 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Drive 中创建一个...', '查询 Google Drive 的数据'`

### 🔹 googlemeet-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Meet 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Meet 中创建一个...', '查询 Google Meet 的数据'`

### 🔹 googlephotos-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Photos 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Photos 中创建一个...', '查询 Google Photos 的数据'`

### 🔹 googleslides-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Slides 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Slides 中创建一个...', '查询 Google Slides 的数据'`

### 🔹 googlesuper-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Google Super 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Google Super 中创建一个...', '查询 Google Super 的数据'`

### 🔹 googletasks-automation
- **功能说明**: "Automate Google Tasks via Rube MCP (Composio): create, list, update, delete, move, and bulk-insert tasks and task lists. Always search tools first for current schemas."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 googletasks 执行操作'`

### 🔹 gosquared-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Gosquared 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Gosquared 中创建一个...', '查询 Gosquared 的数据'`

### 🔹 grafbase-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Grafbase 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Grafbase 中创建一个...', '查询 Grafbase 的数据'`

### 🔹 graphhopper-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Graphhopper 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Graphhopper 中创建一个...', '查询 Graphhopper 的数据'`

### 🔹 griptape-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Griptape 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Griptape 中创建一个...', '查询 Griptape 的数据'`

### 🔹 grist-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Grist 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Grist 中创建一个...', '查询 Grist 的数据'`

### 🔹 habitica-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Habitica 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Habitica 中创建一个...', '查询 Habitica 的数据'`

### 🔹 hackernews-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Hackernews 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Hackernews 中创建一个...', '查询 Hackernews 的数据'`

### 🔹 happy-scribe-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Happy Scribe 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Happy Scribe 中创建一个...', '查询 Happy Scribe 的数据'`

### 🔹 Harvest Automation
- **功能说明**: "Automate time tracking, project management, and invoicing workflows in Harvest -- log hours, manage projects, clients, and tasks through natural language commands."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Harvest Automation 执行操作'`

### 🔹 hashnode-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Hashnode 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Hashnode 中创建一个...', '查询 Hashnode 的数据'`

### 🔹 helcim-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Helcim 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Helcim 中创建一个...', '查询 Helcim 的数据'`

### 🔹 helloleads-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Helloleads 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Helloleads 中创建一个...', '查询 Helloleads 的数据'`

### 🔹 helpwise-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Helpwise 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Helpwise 中创建一个...', '查询 Helpwise 的数据'`

### 🔹 here-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Here 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Here 中创建一个...', '查询 Here 的数据'`

### 🔹 heyreach-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Heyreach 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Heyreach 中创建一个...', '查询 Heyreach 的数据'`

### 🔹 heyzine-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Heyzine 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Heyzine 中创建一个...', '查询 Heyzine 的数据'`

### 🔹 highergov-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Highergov 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Highergov 中创建一个...', '查询 Highergov 的数据'`

### 🔹 highlevel-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Highlevel 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Highlevel 中创建一个...', '查询 Highlevel 的数据'`

### 🔹 honeybadger-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Honeybadger 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Honeybadger 中创建一个...', '查询 Honeybadger 的数据'`

### 🔹 honeyhive-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Honeyhive 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Honeyhive 中创建一个...', '查询 Honeyhive 的数据'`

### 🔹 hookdeck-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Hookdeck 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Hookdeck 中创建一个...', '查询 Hookdeck 的数据'`

### 🔹 hotspotsystem-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Hotspotsystem 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Hotspotsystem 中创建一个...', '查询 Hotspotsystem 的数据'`

### 🔹 html-to-image-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Html To Image 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Html To Image 中创建一个...', '查询 Html To Image 的数据'`

### 🔹 humanitix-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Humanitix 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Humanitix 中创建一个...', '查询 Humanitix 的数据'`

### 🔹 humanloop-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Humanloop 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Humanloop 中创建一个...', '查询 Humanloop 的数据'`

### 🔹 hypeauditor-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Hypeauditor 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Hypeauditor 中创建一个...', '查询 Hypeauditor 的数据'`

### 🔹 hyperbrowser-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Hyperbrowser 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Hyperbrowser 中创建一个...', '查询 Hyperbrowser 的数据'`

### 🔹 hyperise-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Hyperise 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Hyperise 中创建一个...', '查询 Hyperise 的数据'`

### 🔹 hystruct-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Hystruct 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Hystruct 中创建一个...', '查询 Hystruct 的数据'`

### 🔹 icims-talent-cloud-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Icims Talent Cloud 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Icims Talent Cloud 中创建一个...', '查询 Icims Talent Cloud 的数据'`

### 🔹 icypeas-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Icypeas 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Icypeas 中创建一个...', '查询 Icypeas 的数据'`

### 🔹 idea-scale-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Idea Scale 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Idea Scale 中创建一个...', '查询 Idea Scale 的数据'`

### 🔹 identitycheck-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Identitycheck 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Identitycheck 中创建一个...', '查询 Identitycheck 的数据'`

### 🔹 ignisign-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ignisign 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ignisign 中创建一个...', '查询 Ignisign 的数据'`

### 🔹 imagekit-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Imagekit IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Imagekit IO 中创建一个...', '查询 Imagekit IO 的数据'`

### 🔹 imgbb-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Imgbb 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Imgbb 中创建一个...', '查询 Imgbb 的数据'`

### 🔹 imgix-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Imgix 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Imgix 中创建一个...', '查询 Imgix 的数据'`

### 🔹 influxdb-cloud-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Influxdb Cloud 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Influxdb Cloud 中创建一个...', '查询 Influxdb Cloud 的数据'`

### 🔹 insighto-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Insighto AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Insighto AI 中创建一个...', '查询 Insighto AI 的数据'`

### 🔹 instacart-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Instacart 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Instacart 中创建一个...', '查询 Instacart 的数据'`

### 🔹 intelliprint-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Intelliprint 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Intelliprint 中创建一个...', '查询 Intelliprint 的数据'`

### 🔹 interzoid-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Interzoid 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Interzoid 中创建一个...', '查询 Interzoid 的数据'`

### 🔹 ip2location-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ip2location 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ip2location 中创建一个...', '查询 Ip2location 的数据'`

### 🔹 ip2location-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ip2location IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ip2location IO 中创建一个...', '查询 Ip2location IO 的数据'`

### 🔹 ip2proxy-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ip2proxy 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ip2proxy 中创建一个...', '查询 Ip2proxy 的数据'`

### 🔹 ip2whois-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ip2whois 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ip2whois 中创建一个...', '查询 Ip2whois 的数据'`

### 🔹 ipdata-co-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ipdata co 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ipdata co 中创建一个...', '查询 Ipdata co 的数据'`

### 🔹 ipinfo-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ipinfo IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ipinfo IO 中创建一个...', '查询 Ipinfo IO 的数据'`

### 🔹 iqair-airvisual-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Iqair Airvisual 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Iqair Airvisual 中创建一个...', '查询 Iqair Airvisual 的数据'`

### 🔹 jobnimbus-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Jobnimbus 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Jobnimbus 中创建一个...', '查询 Jobnimbus 的数据'`

### 🔹 jumpcloud-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Jumpcloud 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Jumpcloud 中创建一个...', '查询 Jumpcloud 的数据'`

### 🔹 junglescout-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Junglescout 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Junglescout 中创建一个...', '查询 Junglescout 的数据'`

### 🔹 kadoa-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Kadoa 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Kadoa 中创建一个...', '查询 Kadoa 的数据'`

### 🔹 kaggle-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Kaggle 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Kaggle 中创建一个...', '查询 Kaggle 的数据'`

### 🔹 kaleido-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Kaleido 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Kaleido 中创建一个...', '查询 Kaleido 的数据'`

### 🔹 keap-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Keap 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Keap 中创建一个...', '查询 Keap 的数据'`

### 🔹 keen-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Keen IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Keen IO 中创建一个...', '查询 Keen IO 的数据'`

### 🔹 kickbox-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Kickbox 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Kickbox 中创建一个...', '查询 Kickbox 的数据'`

### 🔹 kit-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Kit 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Kit 中创建一个...', '查询 Kit 的数据'`

### 🔹 klipfolio-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Klipfolio 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Klipfolio 中创建一个...', '查询 Klipfolio 的数据'`

### 🔹 ko-fi-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ko Fi 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ko Fi 中创建一个...', '查询 Ko Fi 的数据'`

### 🔹 Kommo Automation
- **功能说明**: "Automate Kommo CRM operations -- manage leads, pipelines, pipeline stages, tasks, and custom fields -- using natural language through the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Kommo Automation 执行操作'`

### 🔹 kontent-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Kontent AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Kontent AI 中创建一个...', '查询 Kontent AI 的数据'`

### 🔹 kraken-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Kraken IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Kraken IO 中创建一个...', '查询 Kraken IO 的数据'`

### 🔹 l2s-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 L2s 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 L2s 中创建一个...', '查询 L2s 的数据'`

### 🔹 labs64-netlicensing-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Labs64 Netlicensing 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Labs64 Netlicensing 中创建一个...', '查询 Labs64 Netlicensing 的数据'`

### 🔹 landbot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Landbot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Landbot 中创建一个...', '查询 Landbot 的数据'`

### 🔹 langbase-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Langbase 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Langbase 中创建一个...', '查询 Langbase 的数据'`

### 🔹 lastpass-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Lastpass 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Lastpass 中创建一个...', '查询 Lastpass 的数据'`

### 🔹 launch_darkly-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 LaunchDarkly 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 LaunchDarkly 中创建一个...', '查询 LaunchDarkly 的数据'`

### 🔹 leadfeeder-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Leadfeeder 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Leadfeeder 中创建一个...', '查询 Leadfeeder 的数据'`

### 🔹 leadoku-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Leadoku 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Leadoku 中创建一个...', '查询 Leadoku 的数据'`

### 🔹 leiga-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Leiga 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Leiga 中创建一个...', '查询 Leiga 的数据'`

### 🔹 lemon_squeezy-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Lemon Squeezy 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Lemon Squeezy 中创建一个...', '查询 Lemon Squeezy 的数据'`

### 🔹 lessonspace-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Lessonspace 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Lessonspace 中创建一个...', '查询 Lessonspace 的数据'`

### 🔹 lever-sandbox-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Lever Sandbox 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Lever Sandbox 中创建一个...', '查询 Lever Sandbox 的数据'`

### 🔹 leverly-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Leverly 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Leverly 中创建一个...', '查询 Leverly 的数据'`

### 🔹 lexoffice-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Lexoffice 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Lexoffice 中创建一个...', '查询 Lexoffice 的数据'`

### 🔹 linguapop-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Linguapop 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Linguapop 中创建一个...', '查询 Linguapop 的数据'`

### 🔹 linkhut-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Linkhut 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Linkhut 中创建一个...', '查询 Linkhut 的数据'`

### 🔹 linkup-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Linkup 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Linkup 中创建一个...', '查询 Linkup 的数据'`

### 🔹 listclean-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Listclean 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Listclean 中创建一个...', '查询 Listclean 的数据'`

### 🔹 listennotes-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Listennotes 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Listennotes 中创建一个...', '查询 Listennotes 的数据'`

### 🔹 livesession-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Livesession 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Livesession 中创建一个...', '查询 Livesession 的数据'`

### 🔹 lmnt-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Lmnt 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Lmnt 中创建一个...', '查询 Lmnt 的数据'`

### 🔹 lodgify-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Lodgify 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Lodgify 中创建一个...', '查询 Lodgify 的数据'`

### 🔹 loomio-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Loomio 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Loomio 中创建一个...', '查询 Loomio 的数据'`

### 🔹 loyverse-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Loyverse 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Loyverse 中创建一个...', '查询 Loyverse 的数据'`

### 🔹 magnetic-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Magnetic 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Magnetic 中创建一个...', '查询 Magnetic 的数据'`

### 🔹 maintainx-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Maintainx 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Maintainx 中创建一个...', '查询 Maintainx 的数据'`

### 🔹 mapbox-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mapbox 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mapbox 中创建一个...', '查询 Mapbox 的数据'`

### 🔹 mapulus-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mapulus 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mapulus 中创建一个...', '查询 Mapulus 的数据'`

### 🔹 mboum-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mboum 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mboum 中创建一个...', '查询 Mboum 的数据'`

### 🔹 melo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Melo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Melo 中创建一个...', '查询 Melo 的数据'`

### 🔹 mem-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mem 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mem 中创建一个...', '查询 Mem 的数据'`

### 🔹 mem0-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mem0 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mem0 中创建一个...', '查询 Mem0 的数据'`

### 🔹 memberspot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Memberspot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Memberspot 中创建一个...', '查询 Memberspot 的数据'`

### 🔹 memberstack-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Memberstack 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Memberstack 中创建一个...', '查询 Memberstack 的数据'`

### 🔹 membervault-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Membervault 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Membervault 中创建一个...', '查询 Membervault 的数据'`

### 🔹 metaads-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Metaads 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Metaads 中创建一个...', '查询 Metaads 的数据'`

### 🔹 metaphor-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Metaphor 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Metaphor 中创建一个...', '查询 Metaphor 的数据'`

### 🔹 mezmo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mezmo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mezmo 中创建一个...', '查询 Mezmo 的数据'`

### 🔹 microsoft-tenant-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Microsoft Tenant 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Microsoft Tenant 中创建一个...', '查询 Microsoft Tenant 的数据'`

### 🔹 microsoft_clarity-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Microsoft Clarity 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Microsoft Clarity 中创建一个...', '查询 Microsoft Clarity 的数据'`

### 🔹 minerstat-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Minerstat 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Minerstat 中创建一个...', '查询 Minerstat 的数据'`

### 🔹 missive-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Missive 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Missive 中创建一个...', '查询 Missive 的数据'`

### 🔹 mistral_ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mistral AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mistral AI 中创建一个...', '查询 Mistral AI 的数据'`

### 🔹 mocean-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mocean 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mocean 中创建一个...', '查询 Mocean 的数据'`

### 🔹 moco-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Moco 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Moco 中创建一个...', '查询 Moco 的数据'`

### 🔹 modelry-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Modelry 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Modelry 中创建一个...', '查询 Modelry 的数据'`

### 🔹 moneybird-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Moneybird 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Moneybird 中创建一个...', '查询 Moneybird 的数据'`

### 🔹 moonclerk-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Moonclerk 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Moonclerk 中创建一个...', '查询 Moonclerk 的数据'`

### 🔹 moosend-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Moosend 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Moosend 中创建一个...', '查询 Moosend 的数据'`

### 🔹 mopinion-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mopinion 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mopinion 中创建一个...', '查询 Mopinion 的数据'`

### 🔹 more-trees-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 More Trees 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 More Trees 中创建一个...', '查询 More Trees 的数据'`

### 🔹 moxie-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Moxie 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Moxie 中创建一个...', '查询 Moxie 的数据'`

### 🔹 moz-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Moz 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Moz 中创建一个...', '查询 Moz 的数据'`

### 🔹 msg91-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Msg91 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Msg91 中创建一个...', '查询 Msg91 的数据'`

### 🔹 mural-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mural 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mural 中创建一个...', '查询 Mural 的数据'`

### 🔹 mx-technologies-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 MX Technologies 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 MX Technologies 中创建一个...', '查询 MX Technologies 的数据'`

### 🔹 mx-toolbox-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Mx Toolbox 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Mx Toolbox 中创建一个...', '查询 Mx Toolbox 的数据'`

### 🔹 nango-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Nango 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Nango 中创建一个...', '查询 Nango 的数据'`

### 🔹 nano-nets-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Nano Nets 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Nano Nets 中创建一个...', '查询 Nano Nets 的数据'`

### 🔹 nasa-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Nasa 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Nasa 中创建一个...', '查询 Nasa 的数据'`

### 🔹 nasdaq-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Nasdaq 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Nasdaq 中创建一个...', '查询 Nasdaq 的数据'`

### 🔹 ncscale-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ncscale 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ncscale 中创建一个...', '查询 Ncscale 的数据'`

### 🔹 needle-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Needle 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Needle 中创建一个...', '查询 Needle 的数据'`

### 🔹 neuronwriter-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Neuronwriter 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Neuronwriter 中创建一个...', '查询 Neuronwriter 的数据'`

### 🔹 neutrino-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Neutrino 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Neutrino 中创建一个...', '查询 Neutrino 的数据'`

### 🔹 neverbounce-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Neverbounce 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Neverbounce 中创建一个...', '查询 Neverbounce 的数据'`

### 🔹 new_relic-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 New Relic 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 New Relic 中创建一个...', '查询 New Relic 的数据'`

### 🔹 news-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 News API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 News API 中创建一个...', '查询 News API 的数据'`

### 🔹 nextdns-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Nextdns 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Nextdns 中创建一个...', '查询 Nextdns 的数据'`

### 🔹 ngrok-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ngrok 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ngrok 中创建一个...', '查询 Ngrok 的数据'`

### 🔹 ninox-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ninox 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ninox 中创建一个...', '查询 Ninox 的数据'`

### 🔹 nocrm-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Nocrm IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Nocrm IO 中创建一个...', '查询 Nocrm IO 的数据'`

### 🔹 notion-research-documentation
- **功能说明**: Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 notion-research-documentation 执行操作'`

### 🔹 notion-spec-to-implementation
- **功能说明**: Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 notion-spec-to-implementation 执行操作'`

### 🔹 ocr-web-service-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 OCR Web Service 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 OCR Web Service 中创建一个...', '查询 OCR Web Service 的数据'`

### 🔹 ocrspace-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ocrspace 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ocrspace 中创建一个...', '查询 Ocrspace 的数据'`

### 🔹 oncehub-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Oncehub 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Oncehub 中创建一个...', '查询 Oncehub 的数据'`

### 🔹 onedesk-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Onedesk 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Onedesk 中创建一个...', '查询 Onedesk 的数据'`

### 🔹 onepage-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Onepage 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Onepage 中创建一个...', '查询 Onepage 的数据'`

### 🔹 onesignal-rest-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 OneSignal 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 OneSignal 中创建一个...', '查询 OneSignal 的数据'`

### 🔹 onesignal-user-auth-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Onesignal User Auth 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Onesignal User Auth 中创建一个...', '查询 Onesignal User Auth 的数据'`

### 🔹 onesignal_rest_api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 OneSignal 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 OneSignal 中创建一个...', '查询 OneSignal 的数据'`

### 🔹 open-sea-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Open Sea 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Open Sea 中创建一个...', '查询 Open Sea 的数据'`

### 🔹 opencage-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Opencage 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Opencage 中创建一个...', '查询 Opencage 的数据'`

### 🔹 opengraph-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Opengraph IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Opengraph IO 中创建一个...', '查询 Opengraph IO 的数据'`

### 🔹 openperplex-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Openperplex 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Openperplex 中创建一个...', '查询 Openperplex 的数据'`

### 🔹 openrouter-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Openrouter 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Openrouter 中创建一个...', '查询 Openrouter 的数据'`

### 🔹 openweather-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Openweather API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Openweather API 中创建一个...', '查询 Openweather API 的数据'`

### 🔹 optimoroute-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Optimoroute 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Optimoroute 中创建一个...', '查询 Optimoroute 的数据'`

### 🔹 owl-protocol-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Owl Protocol 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Owl Protocol 中创建一个...', '查询 Owl Protocol 的数据'`

### 🔹 page-x-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Page X 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Page X 中创建一个...', '查询 Page X 的数据'`

### 🔹 paradym-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Paradym 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Paradym 中创建一个...', '查询 Paradym 的数据'`

### 🔹 parallel-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Parallel 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Parallel 中创建一个...', '查询 Parallel 的数据'`

### 🔹 parma-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Parma 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Parma 中创建一个...', '查询 Parma 的数据'`

### 🔹 parsehub-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Parsehub 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Parsehub 中创建一个...', '查询 Parsehub 的数据'`

### 🔹 parsera-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Parsera 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Parsera 中创建一个...', '查询 Parsera 的数据'`

### 🔹 parseur-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Parseur 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Parseur 中创建一个...', '查询 Parseur 的数据'`

### 🔹 passcreator-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Passcreator 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Passcreator 中创建一个...', '查询 Passcreator 的数据'`

### 🔹 passslot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Passslot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Passslot 中创建一个...', '查询 Passslot 的数据'`

### 🔹 payhip-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Payhip 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Payhip 中创建一个...', '查询 Payhip 的数据'`

### 🔹 pdf-api-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 PDF API IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 PDF API IO 中创建一个...', '查询 PDF API IO 的数据'`

### 🔹 pdf-co-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 PDF co 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 PDF co 中创建一个...', '查询 PDF co 的数据'`

### 🔹 pdf4me-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Pdf4me 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Pdf4me 中创建一个...', '查询 Pdf4me 的数据'`

### 🔹 pdfless-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Pdfless 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Pdfless 中创建一个...', '查询 Pdfless 的数据'`

### 🔹 pdfmonkey-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Pdfmonkey 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Pdfmonkey 中创建一个...', '查询 Pdfmonkey 的数据'`

### 🔹 peopledatalabs-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Peopledatalabs 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Peopledatalabs 中创建一个...', '查询 Peopledatalabs 的数据'`

### 🔹 perigon-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Perigon 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Perigon 中创建一个...', '查询 Perigon 的数据'`

### 🔹 perplexityai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Perplexityai 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Perplexityai 中创建一个...', '查询 Perplexityai 的数据'`

### 🔹 persistiq-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Persistiq 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Persistiq 中创建一个...', '查询 Persistiq 的数据'`

### 🔹 pexels-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Pexels 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Pexels 中创建一个...', '查询 Pexels 的数据'`

### 🔹 piggy-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Piggy 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Piggy 中创建一个...', '查询 Piggy 的数据'`

### 🔹 piloterr-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Piloterr 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Piloterr 中创建一个...', '查询 Piloterr 的数据'`

### 🔹 pilvio-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Pilvio 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Pilvio 中创建一个...', '查询 Pilvio 的数据'`

### 🔹 pingdom-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Pingdom 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Pingdom 中创建一个...', '查询 Pingdom 的数据'`

### 🔹 pipeline-crm-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Pipeline CRM 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Pipeline CRM 中创建一个...', '查询 Pipeline CRM 的数据'`

### 🔹 placekey-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Placekey 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Placekey 中创建一个...', '查询 Placekey 的数据'`

### 🔹 placid-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Placid 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Placid 中创建一个...', '查询 Placid 的数据'`

### 🔹 plain-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Plain 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Plain 中创建一个...', '查询 Plain 的数据'`

### 🔹 plasmic-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Plasmic 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Plasmic 中创建一个...', '查询 Plasmic 的数据'`

### 🔹 platerecognizer-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Platerecognizer 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Platerecognizer 中创建一个...', '查询 Platerecognizer 的数据'`

### 🔹 plisio-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Plisio 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Plisio 中创建一个...', '查询 Plisio 的数据'`

### 🔹 polygon-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Polygon 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Polygon 中创建一个...', '查询 Polygon 的数据'`

### 🔹 polygon-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Polygon IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Polygon IO 中创建一个...', '查询 Polygon IO 的数据'`

### 🔹 poptin-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Poptin 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Poptin 中创建一个...', '查询 Poptin 的数据'`

### 🔹 postgrid-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Postgrid 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Postgrid 中创建一个...', '查询 Postgrid 的数据'`

### 🔹 postgrid-verify-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Postgrid Verify 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Postgrid Verify 中创建一个...', '查询 Postgrid Verify 的数据'`

### 🔹 precoro-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Precoro 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Precoro 中创建一个...', '查询 Precoro 的数据'`

### 🔹 printautopilot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Printautopilot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Printautopilot 中创建一个...', '查询 Printautopilot 的数据'`

### 🔹 prisma-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Prisma 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Prisma 中创建一个...', '查询 Prisma 的数据'`

### 🔹 process-street-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Process Street 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Process Street 中创建一个...', '查询 Process Street 的数据'`

### 🔹 procfu-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Procfu 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Procfu 中创建一个...', '查询 Procfu 的数据'`

### 🔹 productlane-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Productlane 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Productlane 中创建一个...', '查询 Productlane 的数据'`

### 🔹 project-bubble-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Project Bubble 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Project Bubble 中创建一个...', '查询 Project Bubble 的数据'`

### 🔹 proofly-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Proofly 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Proofly 中创建一个...', '查询 Proofly 的数据'`

### 🔹 pushbullet-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Pushbullet 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Pushbullet 中创建一个...', '查询 Pushbullet 的数据'`

### 🔹 pushover-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Pushover 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Pushover 中创建一个...', '查询 Pushover 的数据'`

### 🔹 quaderno-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Quaderno 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Quaderno 中创建一个...', '查询 Quaderno 的数据'`

### 🔹 qualaroo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Qualaroo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Qualaroo 中创建一个...', '查询 Qualaroo 的数据'`

### 🔹 radar-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Radar 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Radar 中创建一个...', '查询 Radar 的数据'`

### 🔹 rafflys-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Rafflys 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Rafflys 中创建一个...', '查询 Rafflys 的数据'`

### 🔹 ragic-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ragic 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ragic 中创建一个...', '查询 Ragic 的数据'`

### 🔹 raisely-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Raisely 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Raisely 中创建一个...', '查询 Raisely 的数据'`

### 🔹 ravenseotools-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ravenseotools 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ravenseotools 中创建一个...', '查询 Ravenseotools 的数据'`

### 🔹 re-amaze-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Re Amaze 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Re Amaze 中创建一个...', '查询 Re Amaze 的数据'`

### 🔹 realphonevalidation-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Realphonevalidation 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Realphonevalidation 中创建一个...', '查询 Realphonevalidation 的数据'`

### 🔹 recallai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Recallai 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Recallai 中创建一个...', '查询 Recallai 的数据'`

### 🔹 recruitee-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Recruitee 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Recruitee 中创建一个...', '查询 Recruitee 的数据'`

### 🔹 refiner-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Refiner 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Refiner 中创建一个...', '查询 Refiner 的数据'`

### 🔹 remarkety-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Remarkety 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Remarkety 中创建一个...', '查询 Remarkety 的数据'`

### 🔹 remote-retrieval-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Remote Retrieval 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Remote Retrieval 中创建一个...', '查询 Remote Retrieval 的数据'`

### 🔹 remove-bg-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Remove Bg 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Remove Bg 中创建一个...', '查询 Remove Bg 的数据'`

### 🔹 repairshopr-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Repairshopr 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Repairshopr 中创建一个...', '查询 Repairshopr 的数据'`

### 🔹 reply-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Reply 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Reply 中创建一个...', '查询 Reply 的数据'`

### 🔹 reply-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Reply IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Reply IO 中创建一个...', '查询 Reply IO 的数据'`

### 🔹 resend-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Resend 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Resend 中创建一个...', '查询 Resend 的数据'`

### 🔹 respond-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Respond IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Respond IO 中创建一个...', '查询 Respond IO 的数据'`

### 🔹 retailed-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Retailed 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Retailed 中创建一个...', '查询 Retailed 的数据'`

### 🔹 retellai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Retellai 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Retellai 中创建一个...', '查询 Retellai 的数据'`

### 🔹 retently-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Retently 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Retently 中创建一个...', '查询 Retently 的数据'`

### 🔹 rev-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Rev AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Rev AI 中创建一个...', '查询 Rev AI 的数据'`

### 🔹 revolt-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Revolt 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Revolt 中创建一个...', '查询 Revolt 的数据'`

### 🔹 rippling-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Rippling 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Rippling 中创建一个...', '查询 Rippling 的数据'`

### 🔹 ritekit-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ritekit 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ritekit 中创建一个...', '查询 Ritekit 的数据'`

### 🔹 rkvst-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Rkvst 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Rkvst 中创建一个...', '查询 Rkvst 的数据'`

### 🔹 rocketlane-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Rocketlane 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Rocketlane 中创建一个...', '查询 Rocketlane 的数据'`

### 🔹 rootly-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Rootly 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Rootly 中创建一个...', '查询 Rootly 的数据'`

### 🔹 rosette-text-analytics-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Rosette Text Analytics 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Rosette Text Analytics 中创建一个...', '查询 Rosette Text Analytics 的数据'`

### 🔹 route4me-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Route4me 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Route4me 中创建一个...', '查询 Route4me 的数据'`

### 🔹 safetyculture-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Safetyculture 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Safetyculture 中创建一个...', '查询 Safetyculture 的数据'`

### 🔹 sage-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sage 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sage 中创建一个...', '查询 Sage 的数据'`

### 🔹 salesforce-marketing-cloud-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Salesforce Marketing Cloud 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Salesforce Marketing Cloud 中创建一个...', '查询 Salesforce Marketing Cloud 的数据'`

### 🔹 salesforce-service-cloud-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Salesforce Service Cloud 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Salesforce Service Cloud 中创建一个...', '查询 Salesforce Service Cloud 的数据'`

### 🔹 salesmate-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Salesmate 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Salesmate 中创建一个...', '查询 Salesmate 的数据'`

### 🔹 sap-successfactors-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 SAP SuccessFactors 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 SAP SuccessFactors 中创建一个...', '查询 SAP SuccessFactors 的数据'`

### 🔹 satismeter-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Satismeter 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Satismeter 中创建一个...', '查询 Satismeter 的数据'`

### 🔹 scrape-do-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Scrape Do 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Scrape Do 中创建一个...', '查询 Scrape Do 的数据'`

### 🔹 scrapegraph-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Scrapegraph AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Scrapegraph AI 中创建一个...', '查询 Scrapegraph AI 的数据'`

### 🔹 scrapfly-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Scrapfly 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Scrapfly 中创建一个...', '查询 Scrapfly 的数据'`

### 🔹 scrapingant-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Scrapingant 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Scrapingant 中创建一个...', '查询 Scrapingant 的数据'`

### 🔹 scrapingbee-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Scrapingbee 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Scrapingbee 中创建一个...', '查询 Scrapingbee 的数据'`

### 🔹 screenshot-fyi-automation
- **功能说明**: 捕获全屏、某个应用程序窗口或特定屏幕区域的截图。
- **使用方法**: `输入指令：'帮我截个全屏图'`

### 🔹 screenshotone-automation
- **功能说明**: 捕获全屏、某个应用程序窗口或特定屏幕区域的截图。
- **使用方法**: `输入指令：'帮我截个全屏图'`

### 🔹 seat-geek-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Seat Geek 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Seat Geek 中创建一个...', '查询 Seat Geek 的数据'`

### 🔹 securitytrails-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Securitytrails 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Securitytrails 中创建一个...', '查询 Securitytrails 的数据'`

### 🔹 segmetrics-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Segmetrics 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Segmetrics 中创建一个...', '查询 Segmetrics 的数据'`

### 🔹 seismic-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Seismic 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Seismic 中创建一个...', '查询 Seismic 的数据'`

### 🔹 semanticscholar-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Semanticscholar 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Semanticscholar 中创建一个...', '查询 Semanticscholar 的数据'`

### 🔹 sendfox-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sendfox 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sendfox 中创建一个...', '查询 Sendfox 的数据'`

### 🔹 sendlane-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sendlane 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sendlane 中创建一个...', '查询 Sendlane 的数据'`

### 🔹 sendloop-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sendloop 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sendloop 中创建一个...', '查询 Sendloop 的数据'`

### 🔹 sendspark-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sendspark 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sendspark 中创建一个...', '查询 Sendspark 的数据'`

### 🔹 sensibo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sensibo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sensibo 中创建一个...', '查询 Sensibo 的数据'`

### 🔹 seqera-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Seqera 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Seqera 中创建一个...', '查询 Seqera 的数据'`

### 🔹 serpapi-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Serpapi 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Serpapi 中创建一个...', '查询 Serpapi 的数据'`

### 🔹 serpdog-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Serpdog 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Serpdog 中创建一个...', '查询 Serpdog 的数据'`

### 🔹 serply-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Serply 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Serply 中创建一个...', '查询 Serply 的数据'`

### 🔹 servicem8-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Servicem8 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Servicem8 中创建一个...', '查询 Servicem8 的数据'`

### 🔹 sevdesk-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sevdesk 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sevdesk 中创建一个...', '查询 Sevdesk 的数据'`

### 🔹 share_point-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 SharePoint 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 SharePoint 中创建一个...', '查询 SharePoint 的数据'`

### 🔹 shipengine-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Shipengine 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Shipengine 中创建一个...', '查询 Shipengine 的数据'`

### 🔹 short-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Short IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Short IO 中创建一个...', '查询 Short IO 的数据'`

### 🔹 short-menu-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Short Menu 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Short Menu 中创建一个...', '查询 Short Menu 的数据'`

### 🔹 Shortcut Automation
- **功能说明**: "Automate project management workflows in Shortcut -- create stories, manage tasks, track epics, and organize workflows through natural language commands."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Shortcut Automation 执行操作'`

### 🔹 shorten-rest-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Shorten Rest 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Shorten Rest 中创建一个...', '查询 Shorten Rest 的数据'`

### 🔹 shortpixel-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Shortpixel 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Shortpixel 中创建一个...', '查询 Shortpixel 的数据'`

### 🔹 shotstack-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Shotstack 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Shotstack 中创建一个...', '查询 Shotstack 的数据'`

### 🔹 sidetracker-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sidetracker 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sidetracker 中创建一个...', '查询 Sidetracker 的数据'`

### 🔹 signaturely-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Signaturely 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Signaturely 中创建一个...', '查询 Signaturely 的数据'`

### 🔹 signpath-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Signpath 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Signpath 中创建一个...', '查询 Signpath 的数据'`

### 🔹 signwell-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Signwell 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Signwell 中创建一个...', '查询 Signwell 的数据'`

### 🔹 similarweb-digitalrank-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 SimilarWeb 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 SimilarWeb 中创建一个...', '查询 SimilarWeb 的数据'`

### 🔹 similarweb_digitalrank_api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 SimilarWeb 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 SimilarWeb 中创建一个...', '查询 SimilarWeb 的数据'`

### 🔹 simla-com-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Simla Com 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Simla Com 中创建一个...', '查询 Simla Com 的数据'`

### 🔹 simple-analytics-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Simple Analytics 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Simple Analytics 中创建一个...', '查询 Simple Analytics 的数据'`

### 🔹 simplesat-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Simplesat 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Simplesat 中创建一个...', '查询 Simplesat 的数据'`

### 🔹 sitespeakai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sitespeakai 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sitespeakai 中创建一个...', '查询 Sitespeakai 的数据'`

### 🔹 skyfire-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Skyfire 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Skyfire 中创建一个...', '查询 Skyfire 的数据'`

### 🔹 smartproxy-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Smartproxy 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Smartproxy 中创建一个...', '查询 Smartproxy 的数据'`

### 🔹 smartrecruiters-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Smartrecruiters 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Smartrecruiters 中创建一个...', '查询 Smartrecruiters 的数据'`

### 🔹 sms-alert-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 SMS Alert 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 SMS Alert 中创建一个...', '查询 SMS Alert 的数据'`

### 🔹 smtp2go-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Smtp2go 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Smtp2go 中创建一个...', '查询 Smtp2go 的数据'`

### 🔹 smugmug-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Smugmug 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Smugmug 中创建一个...', '查询 Smugmug 的数据'`

### 🔹 splitwise-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Splitwise 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Splitwise 中创建一个...', '查询 Splitwise 的数据'`

### 🔹 spoki-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Spoki 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Spoki 中创建一个...', '查询 Spoki 的数据'`

### 🔹 spondyr-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Spondyr 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Spondyr 中创建一个...', '查询 Spondyr 的数据'`

### 🔹 spotlightr-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Spotlightr 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Spotlightr 中创建一个...', '查询 Spotlightr 的数据'`

### 🔹 sslmate-cert-spotter-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sslmate Cert Spotter API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sslmate Cert Spotter API 中创建一个...', '查询 Sslmate Cert Spotter API 的数据'`

### 🔹 stack-exchange-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Stack Exchange 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Stack Exchange 中创建一个...', '查询 Stack Exchange 的数据'`

### 🔹 stannp-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Stannp 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Stannp 中创建一个...', '查询 Stannp 的数据'`

### 🔹 starton-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Starton 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Starton 中创建一个...', '查询 Starton 的数据'`

### 🔹 statuscake-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Statuscake 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Statuscake 中创建一个...', '查询 Statuscake 的数据'`

### 🔹 storeganise-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Storeganise 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Storeganise 中创建一个...', '查询 Storeganise 的数据'`

### 🔹 storerocket-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Storerocket 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Storerocket 中创建一个...', '查询 Storerocket 的数据'`

### 🔹 stormglass-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Stormglass IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Stormglass IO 中创建一个...', '查询 Stormglass IO 的数据'`

### 🔹 strava-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Strava 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Strava 中创建一个...', '查询 Strava 的数据'`

### 🔹 streamtime-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Streamtime 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Streamtime 中创建一个...', '查询 Streamtime 的数据'`

### 🔹 supadata-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Supadata 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Supadata 中创建一个...', '查询 Supadata 的数据'`

### 🔹 supportbee-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Supportbee 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Supportbee 中创建一个...', '查询 Supportbee 的数据'`

### 🔹 supportivekoala-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Supportivekoala 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Supportivekoala 中创建一个...', '查询 Supportivekoala 的数据'`

### 🔹 survey_monkey-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 SurveyMonkey 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 SurveyMonkey 中创建一个...', '查询 SurveyMonkey 的数据'`

### 🔹 svix-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Svix 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Svix 中创建一个...', '查询 Svix 的数据'`

### 🔹 sympla-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Sympla 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Sympla 中创建一个...', '查询 Sympla 的数据'`

### 🔹 synthflow-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Synthflow AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Synthflow AI 中创建一个...', '查询 Synthflow AI 的数据'`

### 🔹 taggun-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Taggun 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Taggun 中创建一个...', '查询 Taggun 的数据'`

### 🔹 talenthr-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Talenthr 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Talenthr 中创建一个...', '查询 Talenthr 的数据'`

### 🔹 tally-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Tally 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Tally 中创建一个...', '查询 Tally 的数据'`

### 🔹 tapfiliate-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Tapfiliate 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Tapfiliate 中创建一个...', '查询 Tapfiliate 的数据'`

### 🔹 tapform-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Tapform 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Tapform 中创建一个...', '查询 Tapform 的数据'`

### 🔹 tavily-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Tavily 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Tavily 中创建一个...', '查询 Tavily 的数据'`

### 🔹 taxjar-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Taxjar 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Taxjar 中创建一个...', '查询 Taxjar 的数据'`

### 🔹 teamcamp-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Teamcamp 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Teamcamp 中创建一个...', '查询 Teamcamp 的数据'`

### 🔹 telnyx-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Telnyx 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Telnyx 中创建一个...', '查询 Telnyx 的数据'`

### 🔹 teltel-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Teltel 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Teltel 中创建一个...', '查询 Teltel 的数据'`

### 🔹 templated-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Templated 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Templated 中创建一个...', '查询 Templated 的数据'`

### 🔹 test-app-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Test App 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Test App 中创建一个...', '查询 Test App 的数据'`

### 🔹 text-to-pdf-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Text To PDF 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Text To PDF 中创建一个...', '查询 Text To PDF 的数据'`

### 🔹 textcortex-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Textcortex 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Textcortex 中创建一个...', '查询 Textcortex 的数据'`

### 🔹 textit-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Textit 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Textit 中创建一个...', '查询 Textit 的数据'`

### 🔹 textrazor-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Textrazor 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Textrazor 中创建一个...', '查询 Textrazor 的数据'`

### 🔹 thanks-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Thanks IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Thanks IO 中创建一个...', '查询 Thanks IO 的数据'`

### 🔹 the-odds-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 The Odds API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 The Odds API 中创建一个...', '查询 The Odds API 的数据'`

### 🔹 ticketmaster-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ticketmaster 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ticketmaster 中创建一个...', '查询 Ticketmaster 的数据'`

### 🔹 ticktick-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ticktick 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ticktick 中创建一个...', '查询 Ticktick 的数据'`

### 🔹 timecamp-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Timecamp 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Timecamp 中创建一个...', '查询 Timecamp 的数据'`

### 🔹 timekit-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Timekit 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Timekit 中创建一个...', '查询 Timekit 的数据'`

### 🔹 timelinesai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Timelinesai 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Timelinesai 中创建一个...', '查询 Timelinesai 的数据'`

### 🔹 timelink-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Timelink 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Timelink 中创建一个...', '查询 Timelink 的数据'`

### 🔹 timely-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Timely 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Timely 中创建一个...', '查询 Timely 的数据'`

### 🔹 tinyurl-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Tinyurl 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Tinyurl 中创建一个...', '查询 Tinyurl 的数据'`

### 🔹 tisane-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Tisane 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Tisane 中创建一个...', '查询 Tisane 的数据'`

### 🔹 Toggl Automation
- **功能说明**: "Automate time tracking workflows in Toggl Track -- create time entries, manage projects, clients, tags, and workspaces through natural language commands."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Toggl Automation 执行操作'`

### 🔹 token-metrics-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Token Metrics 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Token Metrics 中创建一个...', '查询 Token Metrics 的数据'`

### 🔹 tomba-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Tomba 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Tomba 中创建一个...', '查询 Tomba 的数据'`

### 🔹 tomtom-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Tomtom 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Tomtom 中创建一个...', '查询 Tomtom 的数据'`

### 🔹 toneden-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Toneden 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Toneden 中创建一个...', '查询 Toneden 的数据'`

### 🔹 tpscheck-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Tpscheck 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Tpscheck 中创建一个...', '查询 Tpscheck 的数据'`

### 🔹 triggercmd-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Triggercmd 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Triggercmd 中创建一个...', '查询 Triggercmd 的数据'`

### 🔹 tripadvisor-content-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 TripAdvisor 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 TripAdvisor 中创建一个...', '查询 TripAdvisor 的数据'`

### 🔹 turbot-pipes-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Turbot Pipes 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Turbot Pipes 中创建一个...', '查询 Turbot Pipes 的数据'`

### 🔹 twelve-data-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Twelve Data 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Twelve Data 中创建一个...', '查询 Twelve Data 的数据'`

### 🔹 twitch-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Twitch 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Twitch 中创建一个...', '查询 Twitch 的数据'`

### 🔹 twocaptcha-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Twocaptcha 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Twocaptcha 中创建一个...', '查询 Twocaptcha 的数据'`

### 🔹 typefully-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Typefully 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Typefully 中创建一个...', '查询 Typefully 的数据'`

### 🔹 typless-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Typless 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Typless 中创建一个...', '查询 Typless 的数据'`

### 🔹 u301-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 U301 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 U301 中创建一个...', '查询 U301 的数据'`

### 🔹 unione-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Unione 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Unione 中创建一个...', '查询 Unione 的数据'`

### 🔹 updown-io-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Updown IO 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Updown IO 中创建一个...', '查询 Updown IO 的数据'`

### 🔹 uptimerobot-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Uptimerobot 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Uptimerobot 中创建一个...', '查询 Uptimerobot 的数据'`

### 🔹 userlist-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Userlist 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Userlist 中创建一个...', '查询 Userlist 的数据'`

### 🔹 v0-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 V0 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 V0 中创建一个...', '查询 V0 的数据'`

### 🔹 venly-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Venly 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Venly 中创建一个...', '查询 Venly 的数据'`

### 🔹 veo-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Veo 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Veo 中创建一个...', '查询 Veo 的数据'`

### 🔹 veriphone-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Veriphone 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Veriphone 中创建一个...', '查询 Veriphone 的数据'`

### 🔹 vero-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Vero 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Vero 中创建一个...', '查询 Vero 的数据'`

### 🔹 vestaboard-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Vestaboard 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Vestaboard 中创建一个...', '查询 Vestaboard 的数据'`

### 🔹 virustotal-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Virustotal 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Virustotal 中创建一个...', '查询 Virustotal 的数据'`

### 🔹 visme-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Visme 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Visme 中创建一个...', '查询 Visme 的数据'`

### 🔹 waboxapp-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Waboxapp 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Waboxapp 中创建一个...', '查询 Waboxapp 的数据'`

### 🔹 wachete-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Wachete 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Wachete 中创建一个...', '查询 Wachete 的数据'`

### 🔹 waiverfile-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Waiverfile 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Waiverfile 中创建一个...', '查询 Waiverfile 的数据'`

### 🔹 wati-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Wati 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Wati 中创建一个...', '查询 Wati 的数据'`

### 🔹 wave_accounting-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Wave Accounting 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Wave Accounting 中创建一个...', '查询 Wave Accounting 的数据'`

### 🔹 weathermap-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Weathermap 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Weathermap 中创建一个...', '查询 Weathermap 的数据'`

### 🔹 webscraping-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Webscraping AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Webscraping AI 中创建一个...', '查询 Webscraping AI 的数据'`

### 🔹 webvizio-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Webvizio 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Webvizio 中创建一个...', '查询 Webvizio 的数据'`

### 🔹 whautomate-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Whautomate 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Whautomate 中创建一个...', '查询 Whautomate 的数据'`

### 🔹 winston-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Winston AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Winston AI 中创建一个...', '查询 Winston AI 的数据'`

### 🔹 wit-ai-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Wit AI 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Wit AI 中创建一个...', '查询 Wit AI 的数据'`

### 🔹 wiz-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Wiz 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Wiz 中创建一个...', '查询 Wiz 的数据'`

### 🔹 wolfram-alpha-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Wolfram Alpha API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Wolfram Alpha API 中创建一个...', '查询 Wolfram Alpha API 的数据'`

### 🔹 woodpecker-co-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Woodpecker co 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Woodpecker co 中创建一个...', '查询 Woodpecker co 的数据'`

### 🔹 workable-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Workable 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Workable 中创建一个...', '查询 Workable 的数据'`

### 🔹 Workday Automation
- **功能说明**: "Automate HR operations in Workday -- manage workers, time off requests, absence balances, and employee data through natural language commands."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Workday Automation 执行操作'`

### 🔹 workiom-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Workiom 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Workiom 中创建一个...', '查询 Workiom 的数据'`

### 🔹 worksnaps-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Worksnaps 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Worksnaps 中创建一个...', '查询 Worksnaps 的数据'`

### 🔹 writer-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Writer 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Writer 中创建一个...', '查询 Writer 的数据'`

### 🔹 y-gy-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Y Gy 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Y Gy 中创建一个...', '查询 Y Gy 的数据'`

### 🔹 yandex-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Yandex 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Yandex 中创建一个...', '查询 Yandex 的数据'`

### 🔹 yelp-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Yelp 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Yelp 中创建一个...', '查询 Yelp 的数据'`

### 🔹 ynab-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Ynab 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Ynab 中创建一个...', '查询 Ynab 的数据'`

### 🔹 yousearch-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Yousearch 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Yousearch 中创建一个...', '查询 Yousearch 的数据'`

### 🔹 zenrows-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zenrows 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zenrows 中创建一个...', '查询 Zenrows 的数据'`

### 🔹 zenserp-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zenserp 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zenserp 中创建一个...', '查询 Zenserp 的数据'`

### 🔹 zeplin-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zeplin 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zeplin 中创建一个...', '查询 Zeplin 的数据'`

### 🔹 zerobounce-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zerobounce 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zerobounce 中创建一个...', '查询 Zerobounce 的数据'`

### 🔹 zoho-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoho 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoho 中创建一个...', '查询 Zoho 的数据'`

### 🔹 zoho-bigin-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoho Bigin 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoho Bigin 中创建一个...', '查询 Zoho Bigin 的数据'`

### 🔹 zoho-inventory-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoho Inventory 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoho Inventory 中创建一个...', '查询 Zoho Inventory 的数据'`

### 🔹 zoho-invoice-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoho Invoice 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoho Invoice 中创建一个...', '查询 Zoho Invoice 的数据'`

### 🔹 zoho_bigin-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoho Bigin 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoho Bigin 中创建一个...', '查询 Zoho Bigin 的数据'`

### 🔹 zoho_books-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoho Books 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoho Books 中创建一个...', '查询 Zoho Books 的数据'`

### 🔹 zoho_desk-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoho Desk 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoho Desk 中创建一个...', '查询 Zoho Desk 的数据'`

### 🔹 zoho_inventory-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoho Inventory 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoho Inventory 中创建一个...', '查询 Zoho Inventory 的数据'`

### 🔹 zoho_invoice-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zoho Invoice 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zoho Invoice 中创建一个...', '查询 Zoho Invoice 的数据'`

### 🔹 zylvie-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zylvie 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zylvie 中创建一个...', '查询 Zylvie 的数据'`

### 🔹 zyte-api-automation
- **功能说明**: 借助 Composio MCP 集成，通过自然语言自动执行 Zyte API 的各类任务和操作。
- **使用方法**: `自然语言输入指令，例如：'帮我在 Zyte API 中创建一个...', '查询 Zyte API 的数据'`

## <a id='marketing_crm'></a>📊 市场营销与 CRM (Marketing & CRM)

### 🔹 Apollo Automation
- **功能说明**: "Automate Apollo.io lead generation -- search organizations, discover contacts, enrich prospect data, manage contact stages, and build targeted outreach lists -- using natural language through the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Apollo Automation 执行操作'`

### 🔹 Attio Automation
- **功能说明**: "Automate Attio CRM operations -- search records, query contacts and companies with advanced filters, manage notes, list attributes, and navigate your relationship data -- using natural language through the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Attio Automation 执行操作'`

### 🔹 Braintree Automation
- **功能说明**: "Braintree Automation: manage payment processing via Stripe-compatible tools for customers, subscriptions, payment methods, and transactions"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Braintree Automation 执行操作'`

### 🔹 changelog-generator
- **功能说明**: Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes. Turns hours of manual changelog writing into minutes of automated generation.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 changelog-generator 执行操作'`

### 🔹 Dynamics 365 Automation
- **功能说明**: "Dynamics 365 Automation: manage CRM contacts, accounts, leads, opportunities, sales orders, invoices, and cases via the Dynamics CRM Web API"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Dynamics 365 Automation 执行操作'`

### 🔹 Gumroad Automation
- **功能说明**: "Automate Gumroad product management, sales tracking, license verification, and webhook subscriptions using natural language through the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Gumroad Automation 执行操作'`

### 🔹 internal-comms
- **功能说明**: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 internal-comms 执行操作'`

### 🔹 Lemlist Automation
- **功能说明**: "Automate Lemlist multichannel outreach -- manage campaigns, enroll leads, add personalization variables, export campaign data, and handle unsubscribes via the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Lemlist Automation 执行操作'`

### 🔹 Lemon Squeezy Automation
- **功能说明**: "Automate Lemon Squeezy store management -- products, orders, subscriptions, customers, discounts, and checkout tracking -- using natural language through the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Lemon Squeezy Automation 执行操作'`

### 🔹 meeting-insights-analyzer
- **功能说明**: Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. Identifies when you avoid conflict, use filler words, dominate conversations, or miss opportunities to listen. Perfect for professionals seeking to improve their communication and leadership skills.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 meeting-insights-analyzer 执行操作'`

### 🔹 NetSuite Automation
- **功能说明**: "NetSuite Automation: manage customers, sales orders, invoices, inventory, and records via Oracle NetSuite ERP with SuiteQL queries"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 NetSuite Automation 执行操作'`

### 🔹 Omnisend Automation
- **功能说明**: "Automate ecommerce marketing workflows including contact management, bulk operations, and subscriber segmentation through Omnisend via Composio"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Omnisend Automation 执行操作'`

### 🔹 PhantomBuster Automation
- **功能说明**: "Automate lead generation, web scraping, and social media data extraction workflows through PhantomBuster's cloud platform via Composio"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 PhantomBuster Automation 执行操作'`

### 🔹 QuickBooks Automation
- **功能说明**: "QuickBooks Automation: manage invoices, customers, accounts, and payments in QuickBooks Online for streamlined bookkeeping"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 QuickBooks Automation 执行操作'`

### 🔹 Zoho Books Automation
- **功能说明**: "Automate Zoho Books accounting workflows including invoice creation, bill management, contact lookup, payment tracking, and multi-organization support through natural language commands"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Zoho Books Automation 执行操作'`

### 🔹 Zoho Desk Automation
- **功能说明**: "Zoho Desk automation via Rube MCP -- toolkit not currently available in Composio; no ZOHO_DESK_ tools found"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Zoho Desk Automation 执行操作'`

## <a id='design_ui'></a>🎨 设计与 UI/UX (Design & UI/UX)

### 🔹 "imagegen"
- **功能说明**: 调用 OpenAI DALL-E 接口生成高质量图像、进行图片编辑、抠图等。
- **使用方法**: `输入指令：'帮我生成一张在太空里的猫咪图片'`

### 🔹 "sora"
- **功能说明**: 调用 OpenAI Sora 接口生成、修改或下载高质量 AI 视频。
- **使用方法**: `输入指令：'生成一段关于赛博朋克城市的视频'`

### 🔹 "speech"
- **功能说明**: "Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "speech" 执行操作'`

### 🔹 artifacts-builder
- **功能说明**: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 artifacts-builder 执行操作'`

### 🔹 Ashby Automation
- **功能说明**: "Automate recruiting and hiring workflows in Ashby -- manage candidates, jobs, applications, interviews, and notes through natural language commands."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Ashby Automation 执行操作'`

### 🔹 brand-guidelines
- **功能说明**: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 brand-guidelines 执行操作'`

### 🔹 canvas-design
- **功能说明**: Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 canvas-design 执行操作'`

### 🔹 image-enhancer
- **功能说明**: Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. Perfect for preparing images for presentations, documentation, or social media posts.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 image-enhancer 执行操作'`

### 🔹 langsmith-fetch
- **功能说明**: Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. Use when debugging agent behavior, investigating errors, analyzing tool calls, checking memory operations, or examining agent performance. Automatically fetches recent traces and analyzes execution patterns. Requires langsmith-fetch CLI installed.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 langsmith-fetch 执行操作'`

### 🔹 Lever Automation
- **功能说明**: "Automate recruiting workflows in Lever ATS -- manage opportunities, job postings, requisitions, pipeline stages, and candidate tags through the Composio Lever integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Lever Automation 执行操作'`

### 🔹 mcp-builder
- **功能说明**: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 mcp-builder 执行操作'`

### 🔹 Mistral AI Automation
- **功能说明**: "Automate Mistral AI operations -- manage files and libraries, upload documents for fine-tuning, batch processing, and OCR, track fine-tuning jobs, and build RAG pipelines via the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Mistral AI Automation 执行操作'`

### 🔹 OpenAI Automation
- **功能说明**: "Automate OpenAI API operations -- generate responses with multimodal and structured output support, create embeddings, generate images, and list models via the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 OpenAI Automation 执行操作'`

### 🔹 Schematic Analyzer
- **功能说明**: Analyzes Cadence OrCAD schematics by searching datasheets, checking component usage, and verifying connectivity/power designs.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Schematic Analyzer 执行操作'`

### 🔹 skill-creator
- **功能说明**: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 skill-creator 执行操作'`

## <a id='ai_media'></a>🤖 AI 生成与多媒体 (AI & Media)

### 🔹 "screenshot"
- **功能说明**: 捕获全屏、某个应用程序窗口或特定屏幕区域的截图。
- **使用方法**: `输入指令：'帮我截个全屏图'`

### 🔹 "transcribe"
- **功能说明**: "Transcribe audio files to text with optional diarization and known-speaker hints. Use when a user asks to transcribe speech from audio/video, extract text from recordings, or label speakers in interviews or meetings."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 "transcribe" 执行操作'`

### 🔹 Ahrefs Automation
- **功能说明**: "Automate SEO research with Ahrefs -- analyze backlink profiles, research keywords, track domain metrics history, audit organic rankings, and perform batch URL analysis through the Composio Ahrefs integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Ahrefs Automation 执行操作'`

### 🔹 competitive-ads-extractor
- **功能说明**: Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative approaches are working. Helps inspire and improve your own ad campaigns.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 competitive-ads-extractor 执行操作'`

### 🔹 ElevenLabs Automation
- **功能说明**: "Automate ElevenLabs text-to-speech workflows -- generate speech from text, browse and inspect voices, check subscription limits, list models, stream audio, and retrieve history via the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 ElevenLabs Automation 执行操作'`

### 🔹 Facebook Automation
- **功能说明**: "Automate Facebook Page management including post creation, scheduling, video uploads, Messenger conversations, and audience engagement via Composio"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Facebook Automation 执行操作'`

### 🔹 Gong Automation
- **功能说明**: "Automate Gong conversation intelligence -- retrieve call recordings, transcripts, detailed analytics, speaker stats, and workspace data -- using natural language through the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Gong Automation 执行操作'`

### 🔹 HeyGen Automation
- **功能说明**: "Automate AI video generation, avatar browsing, template-based video creation, and video status tracking through HeyGen's platform via Composio"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 HeyGen Automation 执行操作'`

### 🔹 raffle-winner-picker
- **功能说明**: Picks random winners from lists, spreadsheets, or Google Sheets for giveaways, raffles, and contests. Ensures fair, unbiased selection with transparency.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 raffle-winner-picker 执行操作'`

### 🔹 Replicate Automation
- **功能说明**: "Automate Replicate AI model operations -- run predictions, upload files, inspect model schemas, list versions, and manage prediction history via the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Replicate Automation 执行操作'`

### 🔹 RingCentral Automation
- **功能说明**: "RingCentral automation via Rube MCP -- toolkit not currently available in Composio; no RING_CENTRAL_ tools found"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 RingCentral Automation 执行操作'`

### 🔹 SEMrush Automation
- **功能说明**: "Automate SEO analysis with SEMrush -- research keywords, analyze domain organic rankings, audit backlinks, assess keyword difficulty, and discover related terms through the Composio SEMrush integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 SEMrush Automation 执行操作'`

### 🔹 Spotify Automation
- **功能说明**: "Automate Spotify workflows including playlist management, music search, playback control, and user profile access via Composio"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Spotify Automation 执行操作'`

### 🔹 tailored-resume-generator
- **功能说明**: Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills, and achievements to maximize interview chances
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 tailored-resume-generator 执行操作'`

### 🔹 Wave Accounting Automation
- **功能说明**: "Wave Accounting toolkit is not currently available as a native integration. No Wave-specific tools were found in the Composio platform. This skill is a placeholder pending future integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Wave Accounting Automation 执行操作'`

### 🔹 youtube-downloader
- **功能说明**: Download YouTube videos with customizable quality and format options. Use this skill when the user asks to download, save, or grab YouTube videos. Supports various quality settings (best, 1080p, 720p, 480p, 360p), multiple formats (mp4, webm, mkv), and audio-only downloads as MP3.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 youtube-downloader 执行操作'`

## <a id='docs_data'></a>📄 文档、表格与知识库 (Documents, Spreadsheets & Knowledge)

### 🔹 Excel Automation
- **功能说明**: "Excel Automation: create workbooks, manage worksheets, read/write cell data, and format spreadsheets via Microsoft Excel and Google Sheets integration"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Excel Automation 执行操作'`

### 🔹 PandaDoc Automation
- **功能说明**: "Automate document workflows with PandaDoc -- create documents from files, manage contacts, organize folders, set up webhooks, create templates, and track document status through the Composio PandaDoc integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 PandaDoc Automation 执行操作'`

### 🔹 Prismic Automation
- **功能说明**: "Automate headless CMS operations in Prismic -- query documents, search content, retrieve custom types, and manage repository refs through the Composio Prismic integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Prismic Automation 执行操作'`

### 🔹 SharePoint Automation
- **功能说明**: "SharePoint Automation: manage sites, lists, documents, folders, pages, and search content across SharePoint and OneDrive"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 SharePoint Automation 执行操作'`

### 🔹 theme-factory
- **功能说明**: Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 theme-factory 执行操作'`

## <a id='other'></a>🔌 其他自动化扩展 (Other Integrations)

### 🔹 "jupyter-notebook"
- **功能说明**: 在本地创建、编辑或运行 Jupyter Notebook 进行数据探索。
- **使用方法**: `输入指令：'创建一个新的 notebook 并写一段数据分析代码'`

### 🔹 BOM Comparison Skill
- **功能说明**: Comprehensively compares two Bill of Materials (BOM) files to identify differences in Reference, Value, and PCB Footprint.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 BOM Comparison Skill 执行操作'`

### 🔹 Cloudinary Automation
- **功能说明**: "Automate Cloudinary media management including folder organization, upload presets, asset lookup, transformations, and usage monitoring through natural language commands"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Cloudinary Automation 执行操作'`

### 🔹 Coinbase Automation
- **功能说明**: "Coinbase Automation: list and manage cryptocurrency wallets, accounts, and portfolio data via Coinbase CDP SDK"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Coinbase Automation 执行操作'`

### 🔹 Contentful Automation
- **功能说明**: "Automate headless CMS operations in Contentful -- list spaces, retrieve space metadata, and update space configurations through the Composio Contentful integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Contentful Automation 执行操作'`

### 🔹 Eventbrite Automation
- **功能说明**: "Automate Eventbrite event management, attendee tracking, organization discovery, and category browsing through natural language commands"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Eventbrite Automation 执行操作'`

### 🔹 Firecrawl Automation
- **功能说明**: "Automate web crawling and data extraction with Firecrawl -- scrape pages, crawl sites, extract structured data, batch scrape URLs, and map website structures through the Composio Firecrawl integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Firecrawl Automation 执行操作'`

### 🔹 invoice-organizer
- **功能说明**: Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting key information, renaming them consistently, and sorting them into logical folders. Turns hours of manual bookkeeping into minutes of automated organization.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 invoice-organizer 执行操作'`

### 🔹 Jotform Automation
- **功能说明**: "Automate Jotform form listing, user management, activity history, folder organization, and plan inspection through natural language commands"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Jotform Automation 执行操作'`

### 🔹 New Relic Automation
- **功能说明**: "Automate New Relic observability workflows -- manage alert policies, notification channels, alert conditions, and monitor applications and browser apps via the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 New Relic Automation 执行操作'`

### 🔹 Productboard Automation
- **功能说明**: "Automate product management workflows in Productboard -- manage features, notes, objectives, components, and releases through natural language commands."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Productboard Automation 执行操作'`

### 🔹 Ramp Automation
- **功能说明**: "Ramp Automation: manage corporate card transactions, reimbursements, users, and expense tracking via the Ramp platform"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Ramp Automation 执行操作'`

### 🔹 Snowflake Automation
- **功能说明**: "Automate Snowflake data warehouse operations -- list databases, schemas, and tables, execute SQL statements, and manage data workflows via the Composio MCP integration."
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Snowflake Automation 执行操作'`

### 🔹 SurveyMonkey Automation
- **功能说明**: "Automate SurveyMonkey survey creation, response collection, collector management, and survey discovery through natural language commands"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 SurveyMonkey Automation 执行操作'`

### 🔹 template-skill
- **功能说明**: Replace with description of the skill and when Claude should use it.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 template-skill 执行操作'`

### 🔹 twitter-algorithm-optimizer
- **功能说明**: Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. Rewrite and edit user tweets to improve engagement and visibility based on how the recommendation system ranks content.
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 twitter-algorithm-optimizer 执行操作'`

### 🔹 Uploadcare Automation
- **功能说明**: "Automate Uploadcare file management including listing, storing, inspecting, downloading, and organizing file groups through natural language commands"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Uploadcare Automation 执行操作'`

### 🔹 Xero Automation
- **功能说明**: "Xero Automation: manage invoices, contacts, payments, bank transactions, and accounts in Xero for cloud-based bookkeeping"
- **使用方法**: `直接在聊天中说出你的需求，例如：'帮我使用 Xero Automation 执行操作'`

