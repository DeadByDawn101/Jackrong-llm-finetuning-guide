# 🤖 Codex Goal Template Catalog

Editable automation workflows for Codex Goal mode. Each folder contains a beginner-facing template, public-safe example configuration, and workflow-specific safety gates.

| Workflow | Use it for | Editable template |
|---|---|---|
| 🏋️ Qwopus 27B RL Training | Prepare, validate, launch, monitor, and resume a GRPO or GSPO run | [Open](qwopus27b-rl-training/) |
| ⚙️ Qwen MTP GGUF Release | Preflight, inject MTP heads, convert, smoke-test, quantize, and optionally release GGUF files | [Open](qwen-mtp-gguf-release/) |
| 🗺️ Repository Resource Portal | Maintain the knowledge-base homepage and directory catalogs | [Open](repository-resource-portal/) |

## Common Invocation

```text
/goal Use $<skill-name>. Read <goal-file> and complete the objective step by step. Preserve the safety gates and stopping conditions.
```

## Goal Commands

```text
/goal
/goal pause
/goal resume
/goal clear
```

## Safety Defaults

- Use placeholders or config values for paths, hosts, models, datasets, outputs, algorithms, quant formats, upload behavior, and cleanup behavior.
- Do not embed private paths, private SSH aliases, tokens, raw logs, checkpoints, model weights, datasets, GGUF files, safetensors files, or cache folders.
- Run privacy scans and repository-relative link checks before any sync.
