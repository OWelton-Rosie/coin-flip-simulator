import random
import time
import threading
from collections import Counter

from stats import load_stats, save_stats, reset_stats
import animation
from anti_lock import nudge_mouse
from timer import format_elapsed_time

def run_flips(n):
    return Counter(random.choices(["Heads", "Tails"], k=n))

def main():
    stats = load_stats()

    print("Welcome to Oscar's Coin Flip Simulator!")
    print("1) Flip coins\n2) Reset all-time stats")
    choice = input().strip()

    if choice == "2":
        if input("Are you sure you want to reset stats? (y/n): ").lower() == "y":
            stats = reset_stats()
            save_stats(stats)
            print("Stats have been reset.")
        else:
            print("Reset cancelled.")
        return

    try:
        flips_per_repeat = int(input("How many flips per repeat? "))
        repeats = int(input("How many repeats? "))
        if flips_per_repeat < 1 or repeats < 1:
            raise ValueError
    except ValueError:
        print("Error: Please enter integers greater than 0.")
        return

    start_time = time.time()

    threading.Thread(target=nudge_mouse, daemon=True).start()

    total_counts = Counter()

    for i in range(1, repeats + 1):
        print(f"\n--- Repeat {i} ---")

        animation.done_flipping = False
        anim_thread = threading.Thread(target=animation.flip_animation)
        anim_thread.start()

        counts = run_flips(flips_per_repeat)

        animation.done_flipping = True
        anim_thread.join()

        print(f"Heads: {counts.get('Heads', 0):,}")
        print(f"Tails: {counts.get('Tails', 0):,}")

        total_counts.update(counts)

    for key in ["Heads", "Tails"]:
        stats[key] += total_counts.get(key, 0)
    stats["Total"] += total_counts.total()

    save_stats(stats)

    print("\n=== All repeats combined ===")
    print(f"Heads: {total_counts.get('Heads', 0):,}")
    print(f"Tails: {total_counts.get('Tails', 0):,}")
    print("Success: Results saved to coin_stats.txt.")

    print(f"\nTime taken - {format_elapsed_time(time.time() - start_time)}")

if __name__ == "__main__":
    main()
