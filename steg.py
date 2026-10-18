import argparse
import json
import os
import random
import re
from datetime import datetime
from pathlib import Path
import yaml
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True)
args = parser.parse_args()

with open(args.config) as f:
    cfg = yaml.safe_load(f)

client = OpenAI(api_key=os.environ["OPEN_ROUTER_API_KEY"], base_url=cfg["base_url"])

prompts = cfg["prompts"]
scheme = cfg["scheme"]


def ask(messages):
    resp = client.chat.completions.create(
        model=cfg["model"], messages=messages, max_tokens=cfg["max_tokens"],
        temperature=cfg["temperature"], reasoning_effort=cfg["reasoning_effort"],
    )
    return resp.choices[0].message.content or ""


rng = random.Random(cfg["seed"])
n_exact = 0
n_correct = 0
n_samples = cfg["n_samples"]
n_values = cfg["n_values"]

run_dir = Path(cfg["results_dir"]) / datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
run_dir.mkdir(parents=True)
out = open(run_dir / "completions.jsonl", "w")

for i in range(n_samples):
    task = rng.choice(cfg["tasks"])
    values = [rng.randrange(cfg["value_max"]) for _ in range(n_values)]

    # encode
    answer = ask([
        {"role": "system", "content": prompts["encode_system"].format()},
        {"role": "user", "content": prompts["encode_user"].format(
            task=task, values=" ".join(str(v) for v in values), scheme=scheme)},
    ])

    # decode
    decoded_raw = ask([
        {"role": "user", "content": prompts["decode_user"].format(
            answer=answer, scheme=scheme)},
    ])
    decoded = [int(x) for x in re.findall(r"-?\d+", decoded_raw)][:n_values]

    exact = decoded == values
    n_exact += exact
    n_correct_values = sum(a == b for a, b in zip(decoded, values))
    n_correct += n_correct_values

    out.write(json.dumps({
        "task": task,
        "values": values,
        "answer": answer,
        "decoded": decoded,
        "exact": exact,
        "values_correct": n_correct_values,
    }) + "\n")

    print(f"\n=== sample {i + 1}/{n_samples} ===")
    print("task:   ", task)
    print("values: ", values)
    print("answer: ", answer)
    print("decoded:", decoded, "(exact)" if exact else "")

out.close()

with open(run_dir / "metrics.json", "w") as f:
    json.dump({
        "exact_match_rate": n_exact / n_samples,
        "values_correct_rate": n_correct / (n_samples * n_values),
        "n_samples": n_samples,
        "model": cfg["model"],
    }, f, indent=2)

print("\n=== summary ===")
print("exact matches:", n_exact / n_samples)
print("values correct:", n_correct / (n_samples * n_values))
print("results saved to", run_dir)
