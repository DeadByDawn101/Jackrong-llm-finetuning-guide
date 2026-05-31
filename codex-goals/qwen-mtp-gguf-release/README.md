# ⚙️ Qwen MTP GGUF Release Goal

Use this template to run the canonical Qwen MTP GGUF pipeline through Codex Goal mode.

## Files

- [GOAL_TEMPLATE.md](GOAL_TEMPLATE.md): editable Goal prompt.
- [USER_CONFIG.example.env](USER_CONFIG.example.env): public-safe config values.

## Canonical Implementation

The implementation stays in [`../../qwen-mtp-gguf/`](../../qwen-mtp-gguf/). This Goal template points Codex to the existing scripts and docs instead of copying conversion logic.

## Safety Notes

- Run `--preflight-only` first.
- Keep upload disabled unless separately authorized.
- Keep cleanup disabled unless confirmed uploads are verified.
- Treat disk shortages, RAM shortages, missing tools, and config mismatches as blockers.
