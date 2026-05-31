# Qwopus 27B RL Training Checklist

Use this checklist before any GRPO or GSPO launch.

## Algorithm And Source Validation

- Inspect the public Qwopus 27B tutorial path.
- Inspect the requested RL implementation path.
- Verify whether each file uses `SFTTrainer`, `GRPOTrainer`, `GSPOTrainer`, or another trainer.
- For GSPO-style TRL scripts that still use `GRPOTrainer`, verify sequence-level importance sampling, `dr_grpo` loss, and truncation masking before labeling the workflow GSPO-style.
- Refuse to relabel SFT as RL.
- Stop if the selected `ALGORITHM` does not match the implementation.

## Environment Checks

- Confirm Python and package manager.
- Confirm accelerator availability and driver/runtime compatibility.
- Confirm free disk and checkpoint destination.
- Confirm `torch`, `transformers`, `trl`, `datasets`, `peft`, and `unsloth` where needed.
- Confirm no real tokens or private paths are written into public docs.

## Dataset Checks

- Load a small sample.
- Confirm required fields such as prompt, answer, messages, or task-specific labels.
- Confirm answer extraction logic.
- Check for empty prompts, empty answers, duplicate IDs, and malformed rows.

## Reward Checks

- Test strict-format rewards on valid and invalid completions.
- Test correctness rewards on exact, equivalent, and wrong answers.
- Test repetition or length penalties when present.
- Record reward ranges and failure behavior.

## Trainer Smoke Test

- Construct tokenizer, model or adapter config, dataset slice, reward functions, and trainer.
- Avoid long training unless `ALLOW_LONG_TRAINING=true`.
- For dry runs, stop after construction or a minimal non-training validation path.

## Launch Plan

- Show exact launch command.
- Show monitoring command.
- Show resume command.
- Show stop command.
- Show output directory and checkpoint policy.
- Record any memory-reduction changes.
