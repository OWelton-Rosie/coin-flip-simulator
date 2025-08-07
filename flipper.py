# coinflip.py
import random
import time
import threading
from collections import Counter
from stats import load_stats, save_stats, reset_stats
import animation  # Import the new animation module

def run_flips(n):
    flips = random.choices(["Heads", "Tails"], k=n)
    return Counter(flips)

def main():
    stats = load_stats()

    print("Welcome to the Coin Flip Simulator!")
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
        else:
            print("Reset cancelled.")
            return

    try:
        flips = int(input("How many times do you want to flip the coin? "))
        if flips < 1:
            raise ValueError("Number of flips must be at least 1.")
    except ValueError as e:
        print("Error:", e)
        return

    # Start the animation in a separate thread
    animation.done_flipping = False
    anim_thread = threading.Thread(target=animation.flip_animation)
    anim_thread.start()

    counts = run_flips(flips)

    # Stop the animation
    animation.done_flipping = True
    anim_thread.join()

    # Update stats
    stats["Heads"] += counts.get("Heads", 0)
    stats["Tails"] += counts.get("Tails", 0)
    stats["Total"] += flips

    save_stats(stats)

    print(f"Heads: {counts.get('Heads', 0):,}")
    print(f"Tails: {counts.get('Tails', 0):,}")
    print("Success: Results saved to coin_stats.txt.")

if __name__ == "__main__":
    main()