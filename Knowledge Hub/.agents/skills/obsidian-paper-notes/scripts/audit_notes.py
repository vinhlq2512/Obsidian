#!/usr/bin/env python3
"""Filesystem QA for Knowledge Hub paper notes.

The script intentionally uses only Python's standard library so it can run in
minimal Codex environments. It performs conservative checks and reports warnings
instead of rewriting files.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
WIKILINK_RE = re.compile(r"!?\[\[([^\]\n]+)\]\]")
PDF_PAGE_RE = re.compile(r"\[\[([^\]\n|]+?\.pdf)#page=(\d+)(?:\\?\|[^\]\n]+)?\]\]", re.IGNORECASE)
UNESCAPED_TABLE_PIPE_RE = re.compile(r"^\|.*\[\[[^\]\n]+#page=\d+(?<!\\)\|[^\]]+\]\]")


@dataclass
class Issue:
    level: str
    path: Path
    line: int
    message: str


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def split_frontmatter(text: str) -> tuple[str | None, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, text
    return match.group(1), text[match.end() :]


def parse_scalar_fields(frontmatter: str | None) -> dict[str, str]:
    fields: dict[str, str] = {}
    if not frontmatter:
        return fields
    for line in frontmatter.splitlines():
        if not line or line.startswith(" ") or line.startswith("-") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        fields[key] = value
    return fields


def duplicate_frontmatter_keys(frontmatter: str | None) -> list[tuple[str, int]]:
    if not frontmatter:
        return []
    seen: dict[str, int] = {}
    dupes: list[tuple[str, int]] = []
    for idx, line in enumerate(frontmatter.splitlines(), start=2):
        if not line or line.startswith(" ") or line.startswith("-") or ":" not in line:
            continue
        key = line.split(":", 1)[0].strip()
        if key in seen:
            dupes.append((key, idx))
        else:
            seen[key] = idx
    return dupes


def normalize_doi(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
    value = re.sub(r"^doi:\s*", "", value)
    return value


def normalize_arxiv(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"^arxiv:", "", value)
    value = re.sub(r"v\d+$", "", value)
    return value


def pdf_page_count(path: Path) -> int | None:
    try:
        from pypdf import PdfReader  # type: ignore

        return len(PdfReader(str(path)).pages)
    except Exception:
        pass
    try:
        data = path.read_bytes()
    except OSError:
        return None
    # Conservative fallback; may overcount malformed PDFs, but catches obvious
    # out-of-range links when pypdf is unavailable.
    matches = re.findall(rb"/Type\s*/Page\b", data)
    return len(matches) or None


def collect_notes(paths: list[Path]) -> list[Path]:
    notes: list[Path] = []
    for path in paths:
        if path.is_dir():
            notes.extend(sorted(p for p in path.rglob("*.md") if ".obsidian" not in p.parts))
        elif path.suffix.lower() == ".md":
            notes.append(path)
    return sorted(dict.fromkeys(notes))


def build_link_index(vault_root: Path) -> tuple[dict[str, list[Path]], dict[str, list[Path]], dict[str, list[Path]]]:
    by_name: dict[str, list[Path]] = defaultdict(list)
    by_stem: dict[str, list[Path]] = defaultdict(list)
    aliases: dict[str, list[Path]] = defaultdict(list)
    for path in vault_root.rglob("*.md"):
        if ".obsidian" in path.parts:
            continue
        rel = path.relative_to(vault_root).as_posix()
        by_name[rel].append(path)
        by_name[path.name].append(path)
        by_stem[path.stem].append(path)
        text = path.read_text(encoding="utf-8", errors="replace")
        frontmatter, _ = split_frontmatter(text)
        if frontmatter and re.search(r"^aliases:\s*$", frontmatter, re.MULTILINE):
            in_aliases = False
            for line in frontmatter.splitlines():
                if line.startswith("aliases:"):
                    in_aliases = True
                    continue
                if in_aliases and line.startswith("  - "):
                    aliases[line[4:].strip().strip('"').strip("'")].append(path)
                elif in_aliases and line and not line.startswith(" "):
                    in_aliases = False
    return by_name, by_stem, aliases


def resolve_wikilink(target: str, vault_root: Path, indexes: tuple[dict[str, list[Path]], dict[str, list[Path]], dict[str, list[Path]]]) -> list[Path]:
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    if not target:
        return []
    by_name, by_stem, aliases = indexes
    if target.lower().endswith(".pdf"):
        candidate = vault_root / target
        if candidate.exists():
            return [candidate]
        matches = list(vault_root.rglob(Path(target).name))
        return [p for p in matches if p.suffix.lower() == ".pdf"]
    if target in by_name:
        return by_name[target]
    if f"{target}.md" in by_name:
        return by_name[f"{target}.md"]
    if target in by_stem:
        return by_stem[target]
    if target in aliases:
        return aliases[target]
    return []


def audit_note(path: Path, vault_root: Path, indexes: tuple[dict[str, list[Path]], dict[str, list[Path]], dict[str, list[Path]]]) -> tuple[list[Issue], dict[str, str]]:
    issues: list[Issue] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    frontmatter, body = split_frontmatter(text)
    fields = parse_scalar_fields(frontmatter)

    if text.startswith("---\n") and frontmatter is None:
        issues.append(Issue("error", path, 1, "Malformed YAML frontmatter fence"))
    for key, line in duplicate_frontmatter_keys(frontmatter):
        issues.append(Issue("error", path, line, f"Duplicate frontmatter key: {key}"))

    if fields.get("type") == "paper":
        status = fields.get("status")
        reading_status = fields.get("reading_status")
        if status and status not in {"draft", "reviewed", "stable", "archived", "unread", "reading", "completed"}:
            issues.append(Issue("warn", path, 1, f"Unexpected paper status: {status}"))
        if reading_status and reading_status not in {"not-started", "in-progress", "completed"}:
            issues.append(Issue("warn", path, 1, f"Unexpected reading_status: {reading_status}"))
        if fields.get("created_at") and fields.get("updated_at") and fields["created_at"] > fields["updated_at"]:
            issues.append(Issue("warn", path, 1, "created_at is later than updated_at"))

    for match in UNESCAPED_TABLE_PIPE_RE.finditer(text, re.MULTILINE):
        issues.append(Issue("error", path, line_number(text, match.start()), "Unescaped alias pipe in table PDF wikilink"))

    for match in PDF_PAGE_RE.finditer(text):
        pdf_target = match.group(1)
        page = int(match.group(2))
        matches = resolve_wikilink(pdf_target, vault_root, indexes)
        line = line_number(text, match.start())
        if not matches:
            issues.append(Issue("error", path, line, f"PDF link does not resolve: {pdf_target}"))
            continue
        pdf_path = matches[0]
        count = pdf_page_count(pdf_path)
        if count is not None and page > count:
            issues.append(Issue("error", path, line, f"PDF page {page} exceeds page count {count}: {pdf_target}"))

    for match in WIKILINK_RE.finditer(body):
        raw = match.group(1)
        target = raw.split("|", 1)[0].split("#", 1)[0].strip()
        if not target or target.startswith("http"):
            continue
        matches = resolve_wikilink(raw, vault_root, indexes)
        if not matches:
            issues.append(Issue("warn", path, line_number(text, match.start()), f"Wikilink does not resolve: {raw}"))
        elif len(matches) > 1 and not target.lower().endswith(".pdf"):
            issues.append(Issue("warn", path, line_number(text, match.start()), f"Ambiguous wikilink: {raw}"))

    return issues, fields


def duplicate_metadata(notes: list[tuple[Path, dict[str, str]]]) -> list[Issue]:
    buckets: dict[str, dict[str, list[Path]]] = {
        "doi": defaultdict(list),
        "arxiv": defaultdict(list),
        "citekey": defaultdict(list),
    }
    for path, fields in notes:
        if fields.get("doi"):
            buckets["doi"][normalize_doi(fields["doi"])].append(path)
        if fields.get("arxiv"):
            buckets["arxiv"][normalize_arxiv(fields["arxiv"])].append(path)
        if fields.get("citekey"):
            buckets["citekey"][fields["citekey"].strip().lower()].append(path)
    issues: list[Issue] = []
    for key, bucket in buckets.items():
        for value, paths in bucket.items():
            if value and len(paths) > 1:
                joined = ", ".join(str(p) for p in paths)
                issues.append(Issue("warn", paths[0], 1, f"Duplicate {key} '{value}' across: {joined}"))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Obsidian paper notes.")
    parser.add_argument("paths", nargs="*", default=["20 - Research"], help="Markdown files or directories to audit")
    parser.add_argument("--vault-root", default=".", help="Vault root directory")
    args = parser.parse_args()

    vault_root = Path(args.vault_root).resolve()
    input_paths = [Path(p).resolve() for p in args.paths]
    notes = collect_notes(input_paths)
    indexes = build_link_index(vault_root)

    all_issues: list[Issue] = []
    note_fields: list[tuple[Path, dict[str, str]]] = []
    for note in notes:
        issues, fields = audit_note(note, vault_root, indexes)
        all_issues.extend(issues)
        note_fields.append((note, fields))
    all_issues.extend(duplicate_metadata(note_fields))

    for issue in sorted(all_issues, key=lambda item: (str(item.path), item.line, item.level, item.message)):
        rel = os.path.relpath(issue.path, vault_root)
        print(f"{issue.level.upper()} {rel}:{issue.line}: {issue.message}")

    errors = sum(1 for issue in all_issues if issue.level == "error")
    warnings = sum(1 for issue in all_issues if issue.level == "warn")
    print(f"Audited {len(notes)} note(s): {errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
