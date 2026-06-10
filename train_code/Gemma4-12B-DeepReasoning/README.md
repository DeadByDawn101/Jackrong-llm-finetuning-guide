# Gemma 4 12B Deep Reasoning — First-Ever LoRA Fine-Tuning

**WORLD FIRST: LoRA training on Gemma 4 12B OBLITERATED (gemma4_unified architecture)**

Nobody has done this before. Gemma 4's `gemma4_unified` model type isn't supported by standard training frameworks. We solved it with the **flip-train-flip** technique.

## The Problem

```
mlx-lm: ValueError: Model type gemma4_unified not supported
Unsloth: No gemma4_unified support
HuggingFace TRL: Partial support, misses multimodal tower
```

## The Solution: Flip-Train-Flip

```bash
# 1. Backup config
cp config.json config.json.bak

# 2. Flip gemma4_unified → gemma4 (tricks the trainer)
python3 -c "
import json
c = json.load(open('config.json'))
c['model_type'] = 'gemma4'
json.dump(c, open('config.json', 'w'), indent=2)
"

# 3. Train LoRA (only touches text transformer weights)
mlx_lm.lora --model . --data data --train ...

# 4. Flip back → gemma4_unified (preserves multimodal!)
cp config.json.bak config.json
```

**Why it works:** LoRA adapters only modify text transformer layer weights. Vision/audio towers are untouched. The adapter works with BOTH `gemma4` and `gemma4_unified` configs.

## Key Discoveries

| Discovery | Impact |
|-----------|--------|
| Chat template REQUIRED | Raw strings → garbled; `apply_chat_template()` → perfect |
| Gemma 4 has 256K native context | Built into architecture, no RoPE scaling needed |
| `<\|channel>thought` blocks | Model uses thought channels for reasoning (like Qwen's `<think>`) |
| 26GB peak memory | Fits on ANY 32GB+ Mac |
| 18 tok/s inference | Fast enough for interactive use |

## Training Rules for Gemma 4 12B

```
DATA SCALING:
  20 examples   → 200 iters, LR 3e-6 (proof of concept)
  69 examples   → 300 iters, LR 3e-6 (vocabulary learned)
  292 examples  → 500 iters, LR 3e-6 (concepts work)
  1000 examples → 800 iters, LR 3e-6 (functional)
  5000+ examples → 1500 iters, LR 3e-6 (production)
  
NEVER use LR 1e-5 except first round on 500K+ data!
ALWAYS use apply_chat_template() for testing!
ALWAYS have train.jsonl + valid.jsonl!
```

## Quick Start

```bash
# Install
pip install mlx mlx-lm datasets

# Download model
python3 -c "
from huggingface_hub import snapshot_download
snapshot_download('OBLITERATUS/Gemma-4-12B-OBLITERATED', local_dir='model')
"

# Download training data
python3 -c "
from huggingface_hub import hf_hub_download
hf_hub_download('deadbydawn101/ravenx-gemma4-deep-reasoning-data',
    'round7_train.jsonl', repo_type='dataset', local_dir='data')
"

# Run flip-train-flip
bash train_gemma4.sh
```

## Results

| Round | Examples | Iters | Val Loss | Result |
|-------|----------|-------|----------|--------|
| R2 | 20 | 200 | 2.857 | Concepts learned, fragile |
| R3 | 69 | 300 | 1.344 | Method vocabulary absorbed |
| R4 | 292 | 500 | 0.970 | 9-pass code reasoning! |
| R5 | 1019 | 800 | 0.907 | General reasoning strong |
| R6 | 1039 | 500 | 0.882 | Expert knowledge reinforced |
| R7 | 8039 | 1500 | TBD | Claude distilled + coding |

## Methods Integrated

| Method | What It Adds |
|--------|-------------|
| [OpenMythos](https://github.com/DeadByDawn101/OpenMythos-MLX) | 4x depth extrapolation (train 2 → test 8) |
| [GRAM](https://github.com/DeadByDawn101/GRAM-MLX) | Multi-trajectory best-of-N reasoning |
| [OpenMAI](https://github.com/DeadByDawn101/OpenMAI) | Hill-climbing progressive optimization |
| [OpenSelfRevise](https://github.com/DeadByDawn101/OpenSelfRevise) | Builder/Breaker adversarial self-revision |

## Model Card

- **Base:** [OBLITERATUS/Gemma-4-12B-OBLITERATED](https://huggingface.co/OBLITERATUS/Gemma-4-12B-OBLITERATED)
- **Params:** 23.9B total, 11.9B effective, 2.734M LoRA trainable
- **Context:** 256K tokens (native)
- **Modalities:** Text + Image + Audio
- **License:** Gemma + MIT (adapter)

## Contributors

Built by [@DeadByDawn101](https://github.com/DeadByDawn101) / RavenX LLC + Claude (Anthropic)

---

## GGUF Conversion Fix (Gemma 4 Tokenizer Patch)

Every GGUF converter crashes on Gemma 4 because `extra_special_tokens` is a **list** but the code expects a **dict**.

### The One-Line Fix

```python
import json
tc = json.load(open("your-model/tokenizer_config.json"))
est = tc.get("extra_special_tokens", [])
if isinstance(est, list):
    tc["extra_special_tokens"] = {t: t for t in est} if est else {}
    json.dump(tc, open("your-model/tokenizer_config.json", "w"), indent=2)
```

### GGUF Conversion Steps (Isolated venv)

```bash
# Must use venv — llama.cpp deps conflict with mlx-lm
python3 -m venv /tmp/gguf-env
source /tmp/gguf-env/bin/activate
git clone --depth 1 https://github.com/ggerganov/llama.cpp.git /tmp/llama.cpp
pip install -r /tmp/llama.cpp/requirements.txt

# Patch tokenizer, flip config, convert
python3 /tmp/llama.cpp/convert_hf_to_gguf.py \
  your-model --outfile model.gguf --outtype f16

deactivate  # Back to system python for mlx-lm
```

Without this patch you get:
```
AttributeError: 'list' object has no attribute 'keys'
```
