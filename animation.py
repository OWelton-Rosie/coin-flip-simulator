# animation.py
import time

done_flipping = False  # Shared flag between threads

def flip_animation():
    frames = ['.  ', '.. ', '...', ' ..', '  .', '   ']
    i = 0
    while not done_flipping:
        print(f"\rFlipping{frames[i % len(frames)]}", end="", flush=True)
        time.sleep(0.2)
        i += 1
    print("\rFlipping... Done!        ")
