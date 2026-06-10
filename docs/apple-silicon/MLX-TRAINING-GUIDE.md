# Apple Silicon Training Guide — MLX on Mac

**Fine-tune ANY model on Apple Silicon using MLX. No cloud required.**

## Supported Models

| Model | Architecture | MLX Support | Flip Needed? |
|-------|-------------|-------------|-------------|
| Qwen 3/3.5/3.6 | qwen2/qwen2_moe | ✅ Native | No |
| Llama 3/3.1/4 | llama | ✅ Native | No |
| Gemma 2/3 | gemma2 | ✅ Native | No |
| **Gemma 4** | **gemma4_unified** | **✅ Flip-Train-Flip** | **Yes!** |
| Mistral/Mixtral | mistral | ✅ Native | No |
| Phi-3/4 | phi3 | ✅ Native | No |
| DeepSeek V2/V3 | deepseek_v2 | ✅ Native | No |

## Hardware Requirements

| Machine | RAM | Max Model (Q4) | Max Model (F16) |
|---------|-----|----------------|-----------------|
| M1/M2 8GB | 8GB | 7B | 3B |
| M1/M2 Pro 16GB | 16GB | 14B | 7B |
| M1/M2 Max 32GB | 32GB | 30B | 14B |
| M3/M4 Max 64GB | 64GB | 70B | 30B |
| **M4 Max 128GB** | **128GB** | **120B+** | **70B** |
| M3/M4 Ultra 192GB+ | 192GB+ | 200B+ | 120B+ |

## Training Methods (RavenX Stack)

### 1. OpenMythos — Depth Extrapolation
Train at 2 loops → test at 8 loops → 4x deeper reasoning.
[github.com/DeadByDawn101/OpenMythos-MLX](https://github.com/DeadByDawn101/OpenMythos-MLX)

### 2. GRAM — Width Scaling
Generate N trajectories, select the best. Stochastic guidance for diversity.
[github.com/DeadByDawn101/GRAM-MLX](https://github.com/DeadByDawn101/GRAM-MLX)

### 3. OpenMAI — Hill-Climbing
Progressive domain-specific RL climbs with efficiency gain tracking.
[github.com/DeadByDawn101/OpenMAI](https://github.com/DeadByDawn101/OpenMAI)

### 4. OpenSelfRevise — Self-Revision
Builder/Breaker adversarial loop with MDL-gated regime transitions.
[github.com/DeadByDawn101/OpenSelfRevise](https://github.com/DeadByDawn101/OpenSelfRevise)

## Distributed Training (WWDC 2026)

```bash
# JACCL RDMA over Thunderbolt 5 (50-60 Gbps!)
mlx.launch --hostfile cluster.json -- mlx_lm.lora --model ... --data ... --train

# MLX CUDA backend (Linux GPUs join the cluster!)
pip install mlx[cuda12]
```

## Contributors
Built by [@DeadByDawn101](https://github.com/DeadByDawn101) / RavenX LLC + Claude (Anthropic)
