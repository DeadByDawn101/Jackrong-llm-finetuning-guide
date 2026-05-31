# Repository Resource Portal Goal

Use `$repository-resource-portal`.

## Objective

Maintain the repository as a growing educational LLM knowledge base while keeping the root README concise and navigational.

## Editable Inputs

- `OBJECTIVE`
- `CONTENT_TYPE`
- `TARGET_DIRECTORIES`
- `LANGUAGES_TO_UPDATE`
- `NEW_LINKS`
- `FILES_TO_EXCLUDE`

## Required Steps

1. Inspect the affected directories and existing landing pages.
2. Add detailed content to the relevant directory-level catalog or subproject first.
3. Update the root README only with concise navigation.
4. Update English, Chinese, Korean, and Japanese landing pages when homepage navigation changes.
5. Preserve moderate, consistent emojis.
6. Preserve relative links.
7. Keep detailed MTP documentation inside `qwen-mtp-gguf/`.
8. Run Markdown relative-link validation.
9. Run privacy scans for tokens, private paths, private SSH aliases, logs, model weights, datasets, caches, and temporary outputs.
10. Stop before remote sync unless the user sends exactly `同步` in the current Codex session.

## Maintenance Rule For New Goal Templates And Skills

| New content type | Canonical location | Navigation to update |
|---|---|---|
| New Codex Goal workflow or Skill | `.agents/skills/` and `codex-goals/` | `codex-goals/README.md`, root repository map, localized landing pages |
