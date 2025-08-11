# stats.py
STATS_FILE = "coin_stats.txt"

def load_stats():
    stats = {"Heads": 0, "Tails": 0, "Total": 0}
    try:
        with open(STATS_FILE, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                key, val = line.split(":", 1)
                # Extract number before any parentheses, remove commas, convert to int
                num_str = val.split("(")[0].strip().replace(",", "")
                stats[key] = int(num_str)
    except FileNotFoundError:
        pass
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
