# Qwen MTP GGUF Release Goal

Use `$qwen-mtp-gguf-release`.

## Objective

Prepare a Qwen MTP GGUF release with the canonical `qwen-mtp-gguf/` pipeline. Do not upload, publish, or clean up generated artifacts unless the user separately authorizes those actions.

## Editable Configuration

Copy [USER_CONFIG.example.env](USER_CONFIG.example.env) to a private config file and edit:

- `OBJECTIVE`
- `SOURCE_REPO`
- `MTP_SOURCE_REPO`
- `OUTPUT_REPO`
- `WORK_ROOT`
- `LLAMA_CPP`
- `FILENAME_PREFIX`
- `QUANT_FORMATS`
- `UPLOAD_STRATEGY`
- `ALLOW_HF_UPLOAD`
- `CLEANUP_AFTER_UPLOAD`
- `TOKEN_ENV`

## Required Steps

1. Read `qwen-mtp-gguf/SKILL.md` and `qwen-mtp-gguf/README.md`.
2. Reuse `qwen-mtp-gguf/scripts/qwen_mtp_gguf_pipeline.py`; do not copy conversion scripts into `codex-goals/`.
3. Verify the target model and MTP source model are architecture-compatible.
4. Run a preflight command with `--preflight-only`.
5. Review `preflight_report.md` and stop on blockers.
6. Produce the exact full-pipeline command only after preflight passes.
7. Keep Hugging Face upload disabled unless `ALLOW_HF_UPLOAD=true` and upload is separately authorized.
8. Keep cleanup disabled unless uploads have been verified.

## Command Pattern

```bash
python3 qwen-mtp-gguf/scripts/qwen_mtp_gguf_pipeline.py \
  --source-repo "$SOURCE_REPO" \
  --mtp-source-repo "$MTP_SOURCE_REPO" \
  --output-repo "$OUTPUT_REPO" \
  --work-root "$WORK_ROOT" \
  --llama-cpp "$LLAMA_CPP" \
  --filename-prefix "$FILENAME_PREFIX" \
  --quant-types "$QUANT_FORMATS" \
  --upload-strategy "$UPLOAD_STRATEGY" \
  --token-env "$TOKEN_ENV" \
  --preflight-only
```

## Safety Gates

- Stop on disk shortage, RAM shortage, missing tools, missing token access, or model-config mismatch.
- Do not upload model artifacts merely because GitHub sync is approved.
- Do not commit tokens, private paths, raw logs, safetensors files, GGUF files, or checkpoints.
