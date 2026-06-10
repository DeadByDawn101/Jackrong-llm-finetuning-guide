#!/bin/bash
# Flip-Train-Flip for Gemma 4 12B OBLITERATED
# First-ever LoRA training on gemma4_unified architecture
MODEL_DIR="${1:-model}"
DATA_DIR="${2:-data}"
ITERS="${3:-1500}"
LR="${4:-3e-6}"
CONFIG="$MODEL_DIR/config.json"

echo "============================================"
echo "  Gemma 4 12B — Flip-Train-Flip Pipeline"
echo "============================================"

echo "[1/4] Backing up config..."
cp "$CONFIG" "${CONFIG}.bak"

echo "[2/4] Flipping gemma4_unified → gemma4..."
python3 -c "
import json
c = json.load(open('$CONFIG'))
print(f'  Was: {c[\"model_type\"]}')
c['model_type'] = 'gemma4'
json.dump(c, open('$CONFIG', 'w'), indent=2)
print('  Now: gemma4')
"

echo "[3/4] Training ($ITERS iters, LR $LR)..."
python3 -m mlx_lm lora \
  --model "$MODEL_DIR" \
  --data "$DATA_DIR" \
  --train \
  --batch-size 1 \
  --num-layers 4 \
  --iters $ITERS \
  --learning-rate $LR \
  --max-seq-length 1024 \
  --grad-checkpoint \
  --clear-cache-threshold 0.5 \
  --steps-per-eval 200 \
  --adapter-path models/checkpoints/gemma4-lora

echo "[4/4] Flipping back → gemma4_unified..."
cp "${CONFIG}.bak" "$CONFIG"
echo "✅ Restored gemma4_unified"
echo "✅ DONE!"
