# Qwopus 27B RL Training Goal

## Objective

{{OBJECTIVE}}

## Configuration

| Setting | Value |
|---|---|
| Execution mode | `{{EXECUTION_MODE}}` |
| SSH host | `{{SSH_HOST}}` |
| Project root | `{{PROJECT_ROOT}}` |
| Model | `{{MODEL_ID}}` |
| Public Qwopus 27B tutorial | `{{BASE_TUTORIAL_PATH}}` |
| RL implementation script | `{{RL_SCRIPT_PATH}}` |
| Dataset | `{{DATASET_PATH}}` |
| Output directory | `{{OUTPUT_DIR}}` |
| Algorithm | `{{ALGORITHM}}` |
| Context length | `{{CONTEXT_LENGTH}}` |
| Generated completions | `{{NUM_GENERATIONS}}` |
| Learning rate | `{{LEARNING_RATE}}` |
| Maximum steps | `{{MAX_STEPS}}` |
| Dry run | `{{DRY_RUN}}` |
| Long training allowed | `{{ALLOW_LONG_TRAINING}}` |
| Hugging Face upload allowed | `{{ALLOW_HF_UPLOAD}}` |
| Destructive actions allowed | `{{ALLOW_DESTRUCTIVE_ACTIONS}}` |

## Required Steps

1. Confirm the selected algorithm is `GRPO` or `GSPO`.
2. Inspect `{{BASE_TUTORIAL_PATH}}` and `{{RL_SCRIPT_PATH}}`; report whether each file actually implements SFT, GRPO, GSPO-style, or another variant.
3. For GSPO-style scripts using TRL `GRPOConfig` or `GRPOTrainer`, verify the GSPO settings such as sequence-level importance sampling, `dr_grpo` loss, and truncation masking.
4. Stop if `{{RL_SCRIPT_PATH}}` is a placeholder or if the implementation does not match `{{ALGORITHM}}`.
5. Run environment checks for Python, CUDA or accelerator availability, disk, RAM, `torch`, `transformers`, `trl`, `datasets`, `peft`, and `unsloth` when applicable.
6. Validate the dataset schema with a small sample before trainer construction.
7. Run reward-function tests for format, correctness, repetition, and invalid-output cases where those rewards exist.
8. Run a trainer-construction smoke test without long training.
9. Produce a launch plan with the exact command, expected output directory, checkpoint cadence, monitoring command, resume command, and stop command.
10. If `{{DRY_RUN}}` is `true`, stop after validation and do not claim a completed training run.
11. If long training is requested, require `ALLOW_LONG_TRAINING=true` and user confirmation before launching.

## Memory Policy

Do not silently reduce quality to fit memory. Recommend reductions in this order:

1. Reduce context length.
2. Reduce per-device batch size.
3. Reduce number of generated completions.
4. Reduce LoRA rank when appropriate.
5. Increase gradient accumulation to recover optimizer batch size.
6. Use stronger hardware or SSH mode.

## Safety Gates

- Do not upload to Hugging Face unless `ALLOW_HF_UPLOAD=true` and the user separately authorizes upload.
- Do not delete outputs, overwrite checkpoints, or kill remote jobs unless `ALLOW_DESTRUCTIVE_ACTIONS=true` and the exact target is confirmed.
- Do not embed private paths, private SSH aliases, tokens, logs, or temporary outputs in public files.
