import random
import time
import threading
from collections import Counter

from stats import load_stats, save_stats, reset_stats  # Import stats functions
import animation  # Import the animation module
from anti_lock import nudge_mouse  # Import the anti-lock function
from timer import format_elapsed_time  # Import the timer 

def run_flips(n):
    flips = random.choices(["Heads", "Tails"], k=n)
    return Counter(flips)

def main():
    stats = load_stats()

    print("Welcome to Oscar's Coin Flip Simulator!")
    print("Choose an option (1 or 2):")
    print("1) Flip coins")
    print("2) Reset all-time stats")
    choice = input().strip()

    if choice == "2":
        confirm = input("Are you sure you want to reset stats? (y/n): ").lower()
        if confirm == "y":
            stats = reset_stats()
            save_stats(stats)
            print("Stats have been reset.")
            return
        elif confirm == "n":
            print("Reset cancelled.")
            return

    try:
        flips_per_repeat = int(input("How many flips per repeat? "))
        if flips_per_repeat < 1:
            raise ValueError("Number of flips must be at least 1.")

        repeats = int(input("How many repeats? "))
        if repeats < 1:
            raise ValueError("Number of repeats must be at least 1.")
    except ValueError as e:
        print("Error:", e)
        return

    start_time = time.time()  # Start timing

    # Start anti-lock mouse nudge thread
    mouse_thread = threading.Thread(target=nudge_mouse, daemon=True)
    mouse_thread.start()

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

    stats["Heads"] += total_counts.get("Heads", 0)
    stats["Tails"] += total_counts.get("Tails", 0)
    stats["Total"] += total_counts.total()

    save_stats(stats)

    print("\n=== All repeats combined ===")
    print(f"Heads: {total_counts.get('Heads', 0):,}")
    print(f"Tails: {total_counts.get('Tails', 0):,}")
    print("Success: Results saved to coin_stats.txt.")

    end_time = time.time()  # End timing
    elapsed = end_time - start_time
    print(f"\nTime taken - {format_elapsed_time(elapsed)}")

if __name__ == "__main__":
    main()
