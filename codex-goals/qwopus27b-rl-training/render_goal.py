#!/usr/bin/env python3
"""Render the Qwopus 27B RL Codex Goal template from a .env-style config."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PLACEHOLDER_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
VALID_ALGORITHMS = {"GRPO", "GSPO"}
VALID_MODES = {"local", "ssh"}


def parse_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise ValueError(f"{path}:{line_number}: expected KEY=VALUE")
        key, value = line.split("=", 1)
        key = key.strip()
        if not re.fullmatch(r"[A-Z0-9_]+", key):
            raise ValueError(f"{path}:{line_number}: invalid key {key!r}")
        values[key] = value.strip().strip('"').strip("'")
    return values


def render(template: str, values: dict[str, str]) -> str:
    missing = sorted({key for key in PLACEHOLDER_RE.findall(template) if key not in values})
    if missing:
        raise ValueError(f"missing config values: {', '.join(missing)}")
    return PLACEHOLDER_RE.sub(lambda match: values[match.group(1)], template)


def validate(values: dict[str, str]) -> None:
    algorithm = values.get("ALGORITHM", "")
    if algorithm not in VALID_ALGORITHMS:
        raise ValueError(f"ALGORITHM must be one of {', '.join(sorted(VALID_ALGORITHMS))}")
    mode = values.get("EXECUTION_MODE", "")
    if mode not in VALID_MODES:
        raise ValueError(f"EXECUTION_MODE must be one of {', '.join(sorted(VALID_MODES))}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path, help="Path to USER_CONFIG.example.env or USER_CONFIG.env")
    parser.add_argument("--template", type=Path, help="Goal template path")
    parser.add_argument("--output", required=True, type=Path, help="Rendered Markdown output path")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    template_path = args.template or script_dir / "GOAL_TEMPLATE.md"
    values = parse_env(args.config)
    validate(values)
    rendered = render(template_path.read_text(encoding="utf-8"), values)
    args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
