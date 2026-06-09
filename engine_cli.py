#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AXIS Engine CLI
===============
用法：
  python engine_cli.py --mode check-snapshot --ep <集数>
  python engine_cli.py --mode next-step --ep <集数> --stage <阶段> [--chapter <章节>]
  python engine_cli.py --mode status --ep <集数>
  python engine_cli.py --mode gate --ep <集数> --stage <阶段>   # 执行该阶段门禁校验，exit≠0 即未通过
"""
import sys
import json
import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_json(path):
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def cmd_check_snapshot(ep):
    snapshot_path = ROOT / "outputs" / ep / "context-snapshot.json"
    if not snapshot_path.exists():
        print(f"❌ 上下文快照不存在：outputs/{ep}/context-snapshot.json")
        print(f"   请先运行：python3 tools/generators/context-snapshot-generator.py {ep}")
        return 1
    snapshot = load_json(snapshot_path)
    meta = snapshot.get("_meta", {})
    snap_ep = meta.get("episode", "")
    if snap_ep != ep:
        print(f"❌ 快照集数不匹配：快照记录 {snap_ep}，请求 {ep}")
        return 1
    print(f"✅ 上下文快照有效  集数：{ep}  阶段：{meta.get('stage','未知')}  生成时间：{meta.get('generated_at','未知')}")
    return 0


def cmd_next_step(ep, stage, chapter):
    agent_data = load_json(ROOT / ".agent-state.json")
    project = agent_data.get("projectName", "未知项目")
    workflow_path = agent_data.get("workflowPath", "路径一")
    sys.path.insert(0, str(ROOT))
    try:
        from lib.workflow_paths import get_next_stage
    except Exception as e:
        print(f"❌ 无法加载 lib.workflow_paths（{e}）；无法判断下一阶段")
        return 1
    next_s = get_next_stage(workflow_path, stage)
    print(f"📋 [{project}] {ep} 下一步  当前阶段：{stage}  路径：{workflow_path}")
    if next_s:
        print(f"▶  下一阶段：{next_s}")
        print(f"   python engine_cli.py --mode check-snapshot --ep {ep}")
        if chapter:
            print(f"   章节：{chapter}")
    else:
        print(f"🏁 {ep} 所有阶段已完成")
        print(f"   python3 tools/management/episode-progress-reporter.py {ep}")
    return 0


def cmd_status(ep):
    gate_data = load_json(ROOT / ".stage-gate.json")
    agent_data = load_json(ROOT / ".agent-state.json")
    ep_progress = gate_data.get("episodeProgress", {}).get(ep, {})
    ep_agent = agent_data.get("episodes", {}).get(ep, {})
    project = agent_data.get("projectName", "未知项目")
    print(f"📊 [{project}] {ep} 阶段状态")
    print("─" * 50)
    if ep_agent:
        print(f"  currentStage : {ep_agent.get('currentStage','N/A')}")
        history = ep_agent.get("stageHistory", [])
        print(f"  stageHistory : {', '.join(history) if history else '（空）'}")
        print("─" * 50)
    if ep_progress:
        for s, status in ep_progress.items():
            if s.startswith("_"):
                continue
            icon = "✅" if status == "completed" else ("🔄" if status == "in-progress" else "⬜")
            print(f"  {icon} {s:<12} {status}")
    else:
        print("  （此集数暂无进度记录）")
    return 0


def cmd_gate(ep, stage):
    """执行指定阶段的门禁校验脚本（委托 tools/management/run-stage-checks.py）。

    返回该执行器的退出码：0=全部脚本步骤通过，非0=存在失败。
    这是把 engine_cli 从“只读状态查看器”升级为“可执行门禁”的入口。
    """
    runner = ROOT / "tools" / "management" / "run-stage-checks.py"
    if not runner.exists():
        print(f"❌ 门禁执行器不存在：{runner}")
        return 1
    if not stage:
        print("❌ --mode gate 需要 --stage <阶段名>，例如：--stage 分镜编写")
        return 2
    cmd = [sys.executable, str(runner), ep, stage]
    print(f"🚦 执行门禁：{ep} / {stage}")
    try:
        proc = subprocess.run(cmd, cwd=str(ROOT))
    except Exception as e:
        print(f"❌ 门禁执行异常：{e}")
        return 1
    if proc.returncode == 0:
        print(f"✅ 门禁通过：{ep} / {stage}")
    else:
        print(f"⛔ 门禁未通过（exit={proc.returncode}）：{ep} / {stage} —— 禁止进入下一阶段")
    return proc.returncode


def main():
    parser = argparse.ArgumentParser(description="AXIS Engine CLI")
    parser.add_argument("--mode", required=True,
                        choices=["check-snapshot", "next-step", "status", "gate"])
    parser.add_argument("--ep", required=True)
    parser.add_argument("--stage", default="")
    parser.add_argument("--chapter", default="")
    args = parser.parse_args()
    sys.path.insert(0, str(ROOT))
    try:
        from lib.io_utils import check_project_consistency
        _ok, _msg = check_project_consistency(ROOT)
        if not _ok:
            print(_msg)
    except Exception:
        pass
    if args.mode == "check-snapshot":
        return cmd_check_snapshot(args.ep)
    elif args.mode == "next-step":
        return cmd_next_step(args.ep, args.stage, args.chapter)
    elif args.mode == "status":
        return cmd_status(args.ep)
    elif args.mode == "gate":
        return cmd_gate(args.ep, args.stage)
    return 0


if __name__ == "__main__":
    sys.exit(main())
