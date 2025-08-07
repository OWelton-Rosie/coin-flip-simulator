# stats.py
import os

STATS_FILE = "coin_stats.txt"

def load_stats():
    if not os.path.exists(STATS_FILE):
        return {"Heads": 0, "Tails": 0, "Total": 0}
    with open(STATS_FILE, "r") as f:
        lines = f.readlines()
    stats = {"Heads": 0, "Tails": 0, "Total": 0}
    for line in lines:
        if line.strip() == "":
            continue
        key, value = line.strip().split(": ")
        if " (" in value:
            value = value.split(" (")[0]
        stats[key] = int(value.replace(",", ""))
    return stats

def save_stats(stats):
    heads = stats.get("Heads", 0)
    tails = stats.get("Tails", 0)
    total = stats.get("Total", 0)

    head_pct = (heads / total * 100) if total else 0
    tail_pct = (tails / total * 100) if total else 0

    with open(STATS_FILE, "w") as f:
        f.write(f"Heads: {heads:,} ({head_pct:.5f}%)\n")
        f.write(f"Tails: {tails:,} ({tail_pct:.5f}%)\n")
        f.write(f"Total: {total:,}\n")

def reset_stats():
    return {"Heads": 0, "Tails": 0, "Total": 0}
