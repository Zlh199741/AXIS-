---
name: incremental-update-system
description: 增量更新系统。避免全量覆盖，仅更新变更部分，支持差异检测、版本回滚和变更追踪。
---

# 增量更新系统

## 概述

增量更新系统用于避免全量覆盖，仅更新文件或素材的变更部分。该系统提供：

- 变更检测：自动识别文件变化
- 差异更新：仅更新变化的章节/段落
- 版本管理：保留历史版本，支持回滚
- 变更追踪：记录所有变更历史

---

## 核心概念

### 变更类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `新增` | 新增素材或内容 | 新增角色、场景 |
| `修改` | 修改现有内容 | 修改提示词 |
| `删除` | 删除已有内容 | 删除废弃素材 |
| `复用` | 复用其他集数素材 | 跨集复用 |

### 变更粒度

| 粒度 | 说明 |
|------|------|
| 文件级 | 整个文件的增删改 |
| 章节级 | 文件内某个章节的变化 |
| 段落级 | 某个段落的修改 |
| 字段级 | 某个字段的更新 |

---

## 工具实现

### incremental_update_tool.py

```python
#!/usr/bin/env python3
"""
增量更新工具
用于检测变更并执行增量更新
"""

import json
import hashlib
import difflib
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
from collections import defaultdict
import re


@dataclass
class ChangeRecord:
    """变更记录"""
    id: str
    file_path: str
    change_type: str  # added, modified, deleted, reused
    scope: str  # file, section, paragraph, field
    old_content: Optional[str]
    new_content: Optional[str]
    timestamp: str
    episode: str
    reason: Optional[str] = None
    
    def to_dict(self):
        return asdict(self)


@dataclass
class VersionSnapshot:
    """版本快照"""
    version_id: str
    file_path: str
    content_hash: str
    content: str
    timestamp: str
    episode: str
    description: str


class IncrementalUpdateSystem:
    """增量更新系统"""
    
    def __init__(self, project_dir: str):
        self.project_dir = Path(project_dir)
        self.change_history_file = self.project_dir / ".cache" / "changes.json"
        self.versions_dir = self.project_dir / ".cache" / "versions"
        self.change_records: List[ChangeRecord] = []
        self.load_change_history()
    
    def load_change_history(self):
        """加载变更历史"""
        if self.change_history_file.exists():
            with open(self.change_history_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.change_records = [ChangeRecord(**r) for r in data]
    
    def save_change_history(self):
        """保存变更历史"""
        self.change_history_file.parent.mkdir(parents=True, exist_ok=True)
        data = [r.to_dict() for r in self.change_records]
        with open(self.change_history_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    # ========== 变更检测 ==========
    
    def compute_hash(self, content: str) -> str:
        """计算内容哈希"""
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    def detect_file_changes(self, old_content: str, new_content: str,
                           file_path: str, episode: str) -> List[ChangeRecord]:
        """检测文件级变更"""
        changes = []
        
        old_hash = self.compute_hash(old_content)
        new_hash = self.compute_hash(new_content)
        
        if old_hash == new_hash:
            return changes  # 无变化
        
        # 判断变更类型
        if not old_content or old_content.strip() == "":
            change_type = "added"
        elif not new_content or new_content.strip() == "":
            change_type = "deleted"
        else:
            change_type = "modified"
        
        change_id = f"{episode}_{Path(file_path).stem}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        record = ChangeRecord(
            id=change_id,
            file_path=file_path,
            change_type=change_type,
            scope="file",
            old_content=old_content if change_type != "added" else None,
            new_content=new_content if change_type != "deleted" else None,
            timestamp=datetime.now().isoformat(),
            episode=episode
        )
        
        changes.append(record)
        return changes
    
    def detect_section_changes(self, old_content: str, new_content: str,
                              file_path: str, episode: str) -> List[ChangeRecord]:
        """检测章节级变更"""
        changes = []
        
        # 解析章节结构
        old_sections = self._parse_sections(old_content)
        new_sections = self._parse_sections(new_content)
        
        old_keys = set(old_sections.keys())
        new_keys = set(new_sections.keys())
        
        # 新增章节
        for section in new_keys - old_keys:
            record = ChangeRecord(
                id=f"{episode}_{Path(file_path).stem}_{section}_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                file_path=file_path,
                change_type="added",
                scope="section",
                old_content=None,
                new_content=new_sections[section],
                timestamp=datetime.now().isoformat(),
                episode=episode,
                reason=f"新增章节: {section}"
            )
            changes.append(record)
        
        # 删除章节
        for section in old_keys - new_keys:
            record = ChangeRecord(
                id=f"{episode}_{Path(file_path).stem}_{section}_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                file_path=file_path,
                change_type="deleted",
                scope="section",
                old_content=old_sections[section],
                new_content=None,
                timestamp=datetime.now().isoformat(),
                episode=episode,
                reason=f"删除章节: {section}"
            )
            changes.append(record)
        
        # 修改章节
        for section in old_keys & new_keys:
            if old_sections[section] != new_sections[section]:
                # 计算差异
                diff = self._compute_diff(
                    old_sections[section],
                    new_sections[section]
                )
                
                record = ChangeRecord(
                    id=f"{episode}_{Path(file_path).stem}_{section}_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                    file_path=file_path,
                    change_type="modified",
                    scope="section",
                    old_content=old_sections[section],
                    new_content=new_sections[section],
                    timestamp=datetime.now().isoformat(),
                    episode=episode,
                    reason=f"修改章节: {section}\n{diff}"
                )
                changes.append(record)
        
        return changes
    
    def _parse_sections(self, content: str) -> Dict[str, str]:
        """解析章节结构"""
        sections = {}
        current_section = "header"
        current_content = []
        
        for line in content.split('\n'):
            # 匹配章节标题
            if line.strip().startswith('##'):
                if current_content:
                    sections[current_section] = '\n'.join(current_content)
                current_section = line.strip().lstrip('#').strip()
                current_content = []
            else:
                current_content.append(line)
        
        if current_content:
            sections[current_section] = '\n'.join(current_content)
        
        return sections
    
    def _compute_diff(self, old: str, new: str) -> str:
        """计算文本差异"""
        old_lines = old.split('\n')
        new_lines = new.split('\n')
        
        diff = list(difflib.unified_diff(
            old_lines, new_lines, lineterm='', n=3
        ))
        
        return '\n'.join(diff[:20])  # 限制输出长度
    
    # ========== 增量更新 ==========
    
    def apply_incremental_update(self, file_path: str, new_content: str,
                                 episode: str, detect_scope: str = "section") -> Dict:
        """执行增量更新"""
        file_path = Path(file_path)
        target_path = self.project_dir / file_path
        
        # 读取旧内容
        old_content = ""
        if target_path.exists():
            old_content = target_path.read_text(encoding='utf-8')
        
        # 检测变更
        if detect_scope == "file":
            changes = self.detect_file_changes(old_content, new_content, 
                                              str(file_path), episode)
        else:
            changes = self.detect_section_changes(old_content, new_content,
                                                 str(file_path), episode)
        
        # 保存版本快照
        if old_content:
            self._save_version_snapshot(str(file_path), old_content, episode)
        
        # 应用更新
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(new_content, encoding='utf-8')
        
        # 记录变更历史
        self.change_records.extend(changes)
        self.save_change_history()
        
        return {
            "success": True,
            "changes_count": len(changes),
            "changes": [c.to_dict() for c in changes]
        }
    
    def _save_version_snapshot(self, file_path: str, content: str, episode: str):
        """保存版本快照"""
        self.versions_dir.mkdir(parents=True, exist_ok=True)
        
        version_id = f"{Path(file_path).stem}_{episode}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        snapshot = VersionSnapshot(
            version_id=version_id,
            file_path=file_path,
            content_hash=self.compute_hash(content),
            content=content,
            timestamp=datetime.now().isoformat(),
            episode=episode,
            description=f"自动保存: {file_path}"
        )
        
        # 保存快照_file = self.versions_dir / f"{version_id}.
        snapshotjson"
        with open(snapshot_file, 'w', encoding='utf-8') as f:
            json.dump(asdict(snapshot), f, ensure_ascii=False, indent=2)
    
    # ========== 版本回滚 ==========
    
    def get_versions(self, file_path: str) -> List[VersionSnapshot]:
        """获取文件的所有版本"""
        versions = []
        
        file_stem = Path(file_path).stem
        
        for version_file in self.versions_dir.glob(f"{file_stem}_*.json"):
            with open(version_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                versions.append(VersionSnapshot(**data))
        
        # 按时间排序
        versions.sort(key=lambda v: v.timestamp, reverse=True)
        
        return versions
    
    def rollback_to_version(self, file_path: str, version_id: str) -> Dict:
        """回滚到指定版本"""
        version_file = self.versions_dir / f"{version_id}.json"
        
        if not version_file.exists():
            return {"success": False, "error": "版本不存在"}
        
        with open(version_file, 'r', encoding='utf-8') as f:
            snapshot = VersionSnapshot(**json.load(f))
        
        # 应用回滚
        target_path = self.project_dir / file_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(snapshot.content, encoding='utf-8')
        
        # 记录回滚操作
        record = ChangeRecord(
            id=f"rollback_{version_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            file_path=file_path,
            change_type="rollback",
            scope="file",
            old_content=None,
            new_content=snapshot.content,
            timestamp=datetime.now().isoformat(),
            episode=snapshot.episode,
            reason=f"回滚到版本: {version_id}"
        )
        
        self.change_records.append(record)
        self.save_change_history()
        
        return {
            "success": True,
            "rolled_back_to": version_id,
            "timestamp": snapshot.timestamp
        }
    
    # ========== 变更查询 ==========
    
    def get_change_history(self, file_path: str = None, 
                          episode: str = None,
                          change_type: str = None) -> List[ChangeRecord]:
        """查询变更历史"""
        results = self.change_records
        
        if file_path:
            results = [r for r in results if r.file_path == file_path]
        
        if episode:
            results = [r for r in results if r.episode == episode]
        
        if change_type:
            results = [r for r in results if r.change_type == change_type]
        
        return results
    
    def get_latest_changes(self, file_path: str, limit: int = 5) -> List[ChangeRecord]:
        """获取文件的最近变更"""
        changes = self.get_change_history(file_path=file_path)
        changes.sort(key=lambda c: c.timestamp, reverse=True)
        return changes[:limit]
    
    # ========== 增量导出 ==========
    
    def export_incremental(self, episode: str, 
                          since_version: str = None) -> Dict:
        """导出增量变更"""
        changes = self.get_change_history(episode=episode)
        
        if since_version:
            # 过滤指定版本之后的变更
            versions = self.get_versions(f"outputs/{episode}/")
            version_timestamps = {v.version_id: v.timestamp for v in versions}
            
            if since_version in version_timestamps:
                since_time = version_timestamps[since_version]
                changes = [c for c in changes if c.timestamp > since_time]
        
        # 生成增量包
        incremental = {
            "episode": episode,
            "export_time": datetime.now().isoformat(),
            "since_version": since_version,
            "changes_count": len(changes),
            "changes": [c.to_dict() for c in changes]
        }
        
        return incremental
    
    def import_incremental(self, incremental_data: Dict) -> Dict:
        """导入增量变更"""
        changes_data = incremental_data.get("changes", [])
        
        imported = []
        for change_data in changes_data:
            record = ChangeRecord(**change_data)
            
            # 应用变更
            target_path = self.project_dir / record.file_path
            
            if record.change_type == "added":
                target_path.write_text(record.new_content, encoding='utf-8')
            elif record.change_type == "modified":
                # 读取当前内容
                current = target_path.read_text(encoding='utf-8') if target_path.exists() else ""
                
                # 替换内容
                if record.old_content and record.old_content in current:
                    new_content = current.replace(record.old_content, record.new_content)
                else:
                    new_content = record.new_content
                
                target_path.write_text(new_content, encoding='utf-8')
            elif record.change_type == "deleted":
                if target_path.exists():
                    target_path.unlink()
            
            imported.append(record.id)
        
        # 更新变更历史
        self.change_records.extend([ChangeRecord(**c) for c in changes_data])
        self.save_change_history()
        
        return {
            "success": True,
            "imported_count": len(imported)
        }


def main():
    """命令行入口"""
    import argparse
    
    parser = argparse.ArgumentParser(description="增量更新工具")
    parser.add_argument("project_dir", help="项目目录")
    parser.add_argument("--update", type=str, help="执行增量更新")
    parser.add_argument("--history", action="store_true", help="查看变更历史")
    parser.add_argument("--versions", type=str, help="查看版本列表")
    parser.add_argument("--rollback", type=str, help="回滚到指定版本")
    parser.add_argument("--export", type=str, help="导出增量包")
    parser.add_argument("--import", dest="import_file", type=str, help="导入增量包")
    
    args = parser.parse_args()
    
    system = IncrementalUpdateSystem(args.project_dir)
    
    if args.history:
        history = system.get_change_history()
        for record in history[-10:]:
            print(f"{record.timestamp} | {record.change_type} | {record.file_path} | {record.episode}")
    
    elif args.versions:
        versions = system.get_versions(args.versions)
        for v in versions:
            print(f"{v.version_id} | {v.timestamp}")
    
    elif args.rollback:
        parts = args.rollback.split(':')
        if len(parts) == 2:
            result = system.rollback_to_version(parts[0], parts[1])
            print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.export:
        result = system.export_incremental(args.export)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.import_file:
        with open(args.import_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        result = system.import_incremental(data)
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```

---

## 使用示例

### 1. 检测变更

```python
from incremental_update_tool import IncrementalUpdateSystem

system = IncrementalUpdateSystem("/path/to/project")

# 模拟旧内容
old_content = """
# 导演分析 - ep01

## P01 剧情点
讲戏：江辰穿越到古代...

## 人物清单
1. 江辰 - 主角
"""

# 新内容（修改了人物清单）
new_content = """
# 导演分析 - ep01

## P01 剧情点
讲戏：江辰穿越到古代...

## 人物清单
1. 江辰 - 主角
2. 崔云秀 - 女主角
"""

# 检测变更
changes = system.detect_section_changes(
    old_content, new_content,
    "outputs/ep01/01-director-analysis.md",
    "ep01"
)

for change in changes:
    print(f"变更类型: {change.change_type}")
    print(f"变更范围: {change.scope}")
    print(f"变更原因: {change.reason}")
```

### 2. 执行增量更新

```python
# 执行增量更新
result = system.apply_incremental_update(
    file_path="outputs/ep01/01-director-analysis.md",
    new_content=new_content,
    episode="ep01",
    detect_scope="section"  # 章节级检测
)

print(f"更新成功，检测到 {result['changes_count']} 处变更")
```

### 3. 版本回滚

```python
# 获取文件的所有版本
versions = system.get_versions("outputs/ep01/01-director-analysis.md")

for v in versions:
    print(f"版本: {v.version_id}, 时间: {v.timestamp}")

# 回滚到指定版本
result = system.rollback_to_version(
    file_path="outputs/ep01/01-director-analysis.md",
    version_id="01-director-analysis_ep01_20240315"
)

print(f"回滚结果: {result}")
```

### 4. 查询变更历史

```python
# 查询 ep01 的所有变更
history = system.get_change_history(episode="ep01")

for record in history:
    print(f"{record.timestamp} - {record.change_type} - {record.file_path}")

# 查询特定文件的最近变更
latest = system.get_latest_changes(
    file_path="outputs/ep01/01-director-analysis.md",
    limit=5
)
```

### 5. 增量导出/导入

```python
# 导出增量包
incremental = system.export_incremental(
    episode="ep01",
    since_version="v1.0"  # 可选：导出指定版本之后的变更
)

# 保存到文件
with open("ep01-incremental.json", 'w', encoding='utf-8') as f:
    json.dump(incremental, f, ensure_ascii=False, indent=2)

# 导入增量包
with open("ep01-incremental.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

result = system.import_incremental(data)
print(f"导入成功: {result['imported_count']} 个变更")
```

---

## 命令行工具

```bash
# 查看变更历史
python incremental_update_tool.py /path/to/project --history

# 查看文件版本列表
python incremental_update_tool.py /path/to/project --versions "outputs/ep01/01-director-analysis.md"

# 回滚到指定版本
python incremental_update_tool.py /path/to/project --rollback "outputs/ep01/01-director-analysis.md:v1.0"

# 导出增量包
python incremental_update_tool.py /path/to/project --export ep01

# 导入增量包
python incremental_update_tool.py /path/to/project --import ep01-incremental.json
```

---

## 与现有系统集成

### 在导演分析阶段使用增量更新

```python
# director-skill 中集成增量更新
def update_director_analysis(episode: str, new_content: str):
    """更新导演分析，仅保存变更部分"""
    system = IncrementalUpdateSystem(project_dir)
    
    result = system.apply_incremental_update(
        file_path=f"outputs/{episode}/01-director-analysis.md",
        new_content=new_content,
        episode=episode,
        detect_scope="section"
    )
    
    return result
```

### 在版本管理中使用

```python
# 创建版本快照
system._save_version_snapshot(
    "outputs/ep01/01-director-analysis.md",
    content,
    "ep01"
)

# 恢复到历史版本
system.rollback_to_version(
    "outputs/ep01/01-director-analysis.md",
    "01-director-analysis_ep01_20240315"
)
```

---

## 缓存目录结构

```
.cache/
├── changes.json          # 变更历史记录
└── versions/
    ├── 01-director-analysis_ep01_20240315.json
    ├── 01-director-analysis_ep01_20240316.json
    └── ...
```

---

## 最佳实践

1. **自动保存版本**：每次更新前自动保存版本快照
2. **增量导出**：定期导出增量包，便于协作和备份
3. **变更审查**：通过变更历史进行代码/内容审查
4. **回滚策略**：保留最近 N 个版本，支持快速回滚

