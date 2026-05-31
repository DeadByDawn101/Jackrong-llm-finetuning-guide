# 🏋️ Qwopus 27B RL Training Goal

Use this template to prepare a guarded Codex Goal workflow for a configurable Qwopus 27B GRPO or GSPO run.

## Files

- [GOAL_TEMPLATE.md](GOAL_TEMPLATE.md): editable Goal prompt.
- [USER_CONFIG.example.env](USER_CONFIG.example.env): public-safe config values.
- [render_goal.py](render_goal.py): renders the template with config values.

## Render Locally

```bash
python codex-goals/qwopus27b-rl-training/render_goal.py \
  --config codex-goals/qwopus27b-rl-training/USER_CONFIG.example.env \
  --output /tmp/qwopus27b_rl_goal.md
```

## Safety Notes

- The repository includes a public GSPO-style script at `train_code/Qwopus3.6-27B-GSPO/qwopus3_6_27b_gspo_training.py`.
- TRL still uses `GRPOConfig` and `GRPOTrainer` class names in that script; verify the GSPO-style settings before launch.
- Keep `DRY_RUN=true` until environment, dataset, rewards, trainer construction, monitoring, resume, and stop commands are validated.
- Do not upload to Hugging Face unless upload is separately authorized.
