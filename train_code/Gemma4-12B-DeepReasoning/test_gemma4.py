"""Test Gemma 4 12B with LoRA adapter using flip technique."""
import json, shutil, sys

MODEL_DIR = sys.argv[1] if len(sys.argv) > 1 else "model"
ADAPTER = sys.argv[2] if len(sys.argv) > 2 else "models/checkpoints/gemma4-lora"
CONFIG = f"{MODEL_DIR}/config.json"

shutil.copy(CONFIG, f"{CONFIG}.test.bak")
config = json.load(open(CONFIG))
config["model_type"] = "gemma4"
json.dump(config, open(CONFIG, "w"), indent=2)

try:
    from mlx_lm import load, generate
    from mlx_lm.sample_utils import make_sampler

    model, tokenizer = load(MODEL_DIR, adapter_path=ADAPTER)
    sampler = make_sampler(temp=0.7, top_p=0.9)

    prompts = [
        "What is depth extrapolation in AI reasoning?",
        "Write a Python function to find all prime numbers up to n. Use multi-pass verification.",
        "Explain when to use multi-trajectory reasoning vs single-pass inference.",
    ]

    for prompt in prompts:
        print(f"\n{'='*60}")
        print(f"  PROMPT: {prompt[:60]}...")
        print(f"{'='*60}")
        messages = [{"role": "user", "content": prompt}]
        formatted = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        generate(model, tokenizer, prompt=formatted, max_tokens=400, sampler=sampler, verbose=True)

finally:
    shutil.copy(f"{CONFIG}.test.bak", CONFIG)
    import os; os.remove(f"{CONFIG}.test.bak")
    print("\n✅ Config restored to gemma4_unified")
