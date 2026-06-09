# AXIS — AI 漫剧 / 短剧工业级生产流水线

> AXIS (AI-Powered Short Drama / Comic Production Pipeline)
> 从「原著小说 / 一个脑洞」到「可直接投喂 Seedance 的分镜提示词」的全链路自动化系统：
> 多阶段工作流 + 成对的「生成 / 审核」Skill 体系 + 数据驱动的阶段门禁 + 31 个自动化校验器。

---

## 一、核心理念

- **逐阶段推进**：每个阶段都有明确的「输入 → Agent + Skill → 产物 → 门禁校验 → 下一步」闭环。
- **生成与审核分离**：核心生产 Skill 配对独立 `*-review-skill` 审核 Skill；部分辅助 Skill（如 aesthetic-vision / scene-concept-design / prop-concept-design）由共享审核器（art-direction-review 等）覆盖；另有全局合规审核。
- **门禁不可跳过**：阶段产物必须通过对应校验器（exit≠0 即产物作废、重新生成）。
- **原文忠实**：剧情逐事件覆盖、台词逐字比对原著，不允许压缩 / 改写 / 意译。

---

## 二、三条工作流路径

唯一权威定义见 `lib/workflow_paths.py`。三条路径**全部收敛于 `分镜编写`**：

| 路径 | 入口 | 阶段序列 |
|------|------|----------|
| **路径一** | 有原著小说 | 小说分析 → 道具与金手指提取 → 集纲生成 → 剧本生成 → 导演分析 → 视觉风格选择 → 服化道设计 → 分镜编写 |
| **路径二** | 只有脑洞 | 脑洞生成 → 道具与金手指提取 → 集纲生成 → 剧本生成 → 导演分析 → 视觉风格选择 → 服化道设计 → 分镜编写 |
| **路径三** | 已有剧本 | 导演分析 → 视觉风格选择 → 服化道设计 → 分镜编写 |

> 阶段完成后自动进入「集间交接」（生成进度报告、上下文快照、下一步提示、增量基线、项目仪表盘）。
> 每阶段的「Skill 强制加载清单」唯一权威来源：`AXIS-workflow-stages.md` ＞「铁律级 Skill 强制调用 Must-Call Checklist」。

---

## 三、目录地图

```
AXIS-漫剧内测教学/
├── CLAUDE.md                  # 系统主提示词 / 强执行规则（子规则 1-9）
├── AXIS-workflow-stages.md    # 全阶段执行规范 + Must-Call Checklist（单一权威）
├── AXIS-全流程指令合集.md      # 指令速查
├── CHANGELOG.md               # 版本更新日志
├── engine_cli.py              # 引擎 CLI（状态 / 快照 / 下一步 / 门禁）
│
├── lib/                       # 共享库（workflow_paths 路径权威 / io_utils / file_parser …）
├── agents/                    # 7 个 Agent 定义（导演 / 服化道 / 分镜师 / 集纲 / 剧本 / 脑洞 / 视觉风格）
├── skills/                    # 42 个 Skill（生产 Skill + 配对的 *-review-skill 审核 Skill）
│
├── tools/
│   ├── validators/            # 31 个校验器（剧情 / 台词 / 节拍 / 时序 / 一致性 / 合规 …）
│   │   ├── run_validators.py        # 统一校验入口（fail-closed）
│   │   ├── plot-fidelity-checker.py # 剧情逐事件覆盖率
│   │   ├── novel-dialogue-fidelity-checker.py  # 台词逐字忠实度（支持 --target script / --all-chapters）
│   │   ├── seedance-template-validator.py / beat-density-checker.py / …
│   │   └── cross-file-consistency-checker.py / cross-episode-consistency-checker.py
│   ├── generators/            # 生成器（上下文快照 / 跨平台转换 / 时长预测 / 预告片 …）
│   ├── management/            # 流程管理（门禁运行 / 进度 / 仪表盘 / 重置 / 增量基线）
│   └── references/            # 运镜 / 风格 / 敏感词等参考资料
│
├── assets/                    # 资产：novel-analysis/ outline/ prompts/(character|scene|props) + character-bible + visual-style-guide
├── outputs/                   # 各集产物（01-director-analysis / 02-seedance-prompts / 03-text-storyboard …）
├── novel/                     # 原著小说（按章节拆分）
├── resources/                 # 视听语言 / AI 绘画 / 电影摄影等白皮书
├── tests/                     # 单元测试（tests/run_all.py，190 测试全绿）
│
├── .agent-state.json          # 活跃项目 / 集数 / 阶段状态
└── .stage-gate.json           # 阶段门禁配置（stages[].steps[].script + episodeProgress）
```

---

## 四、常用命令

> 环境：Python 3（macOS 用 `python3`）。所有命令在项目根目录执行。

### 进度与状态

```bash
python3 engine_cli.py --mode status        --ep ep01            # 查看某集阶段状态
python3 engine_cli.py --mode check-snapshot --ep ep01           # 校验上下文快照
python3 engine_cli.py --mode next-step      --ep ep01 --stage 分镜编写   # 下一步指令
python3 engine_cli.py --mode gate           --ep ep01 --stage 剧本生成   # 执行该阶段门禁（exit≠0 即未通过）
```

### 校验（质量门禁）

```bash
python3 tools/validators/run_validators.py ep01            # 单集全套校验
python3 tools/validators/run_validators.py all --json      # 全部集数，JSON 输出
python3 tools/management/run-stage-checks.py ep01 剧本生成   # 执行某阶段 .stage-gate.json 中的脚本门禁
python3 tools/management/run-stage-checks.py ep01 --all --dry-run   # 预览全部阶段门禁命令
```

### 测试

```bash
python3 tests/run_all.py                                   # 运行全部单元测试（190 tests）
```

### 切换 / 重置项目

```bash
python3 tools/management/reset_project.py --name "新书名" --novel novel/新书名.txt --path 路径一 --dry-run
```

---

## 五、阶段门禁机制

1. `.stage-gate.json` 的 `stages.{阶段}.steps[]` 中带 `script` 字段的步骤即为机器门禁，支持 `{ep}` / `{ch}` 占位符。
2. `tools/management/run-stage-checks.py` 读取这些步骤，用 `shlex` 分词 + `shell=False` 安全执行，按退出码更新步骤状态，任一失败即整体 `exit 1`。
3. `engine_cli.py --mode gate` 委托上面的运行器执行某阶段门禁。
4. `tools/validators/run_validators.py` 为 **fail-closed**：子进程崩溃 / 非零退出 / 脚本缺失一律计入失败，绝不默认放行。

**剧本生成阶段**门禁示例（均为硬门禁 `required: true`）：

- `plot-fidelity-checker.py {ep}` — 剧情逐事件覆盖率（加权，要求 100%）
- `novel-dialogue-fidelity-checker.py {ep} --target script --chapter {ch} --all-chapters` — 台词逐字忠实度（跨章节比对，杜绝单章定位误报）

---

## 六、状态文件

| 文件 | 作用 |
|------|------|
| `.agent-state.json` | 活跃项目名 / 活跃集数 / 工作流路径 / 各集阶段历史 |
| `.stage-gate.json`  | 阶段门禁配置 + `episodeProgress`（按集追踪每阶段 completed/skipped） |

> `lib/io_utils.check_project_consistency()` 会校验两份状态文件的 `projectName` 是否一致，防止多项目脏数据混淆。

---

## 七、脚本化辅助工具（v8.9–v8.13）

> 主线：把每阶段「确定性的铺架/统计/切分/审计」交给脚本，AI 只保留创作与审美判断。
> 边界铁律：脚本只产出确定性外壳与 `〔待填写〕` 空壳，绝不预填剧情/台词/审美结论。

### 阶段骨架生成器（创作前铺空壳，AI 只填空）

```bash
python3 tools/generators/stage-scaffold-generator.py outline    --chapter ch01 --episodes 10
python3 tools/generators/stage-scaffold-generator.py director   --ep ep01 --pblocks 8
python3 tools/generators/stage-scaffold-generator.py storyboard --ep ep01 --pblocks 8 --source assets/novel/ch01-script.md
# 安全：目标非空默认拒覆盖（--force 覆盖）；--stdout 预览
```
集纲/导演/分镜阶段的下一步指令（`next-step-prompter` / `stage-pipeline`）会自动以「🧱 第1步·骨架预生成」提示对应命令。

### 小说分析抽取生成器（统计/切分归脚本，定性留 AI）

```bash
python3 tools/generators/novel-analysis-scaffold-generator.py groups     --book <书名> --per-group 3
python3 tools/generators/novel-analysis-scaffold-generator.py events     --book <书名>
python3 tools/generators/novel-analysis-scaffold-generator.py characters --book <书名> --characters "角色1,角色2"
# 给定角色名单→精确出场频次+同章共现矩阵；不给→高频候选词（标注"候选·需人工筛选"）
```

### 章节-集数-P块映射表（消除跨阶段对应漂移）

```bash
python3 tools/generators/chapter-episode-map-generator.py            # 生成 assets/chapter-episode-map.json + 表格
python3 tools/generators/chapter-episode-map-generator.py --ep ep02  # 单集查询
```
解析集纲「对应原著」标注得到 集↔小说章节↔P块。`lib/episode_map.py` 提供读取助手；`plot-fidelity-checker` 在未传 `--chapter` 时自动从此 map 回退。集纲阶段完成后自动刷新。

### 存量分镜瘦身（方向B 配套）

```bash
python3 tools/management/slim-seedance-audit-tables.py <seedance文件>          # 预览
python3 tools/management/slim-seedance-audit-tables.py --dir <目录> --apply    # 改写（默认写 .bak）
```
剥离存量文件里的 **📐翻译审计 + ⏱密度校验** 两张冗余自评表（权威校验已脚本化）。
🔴 **不剥离 🎭台词审计**——它是非配音台词的唯一逐字留存处，关乎源剧本忠实度。
