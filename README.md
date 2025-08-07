This program was to help with a stats assignment on the difference between experimental and theoretical probability. It helped a great deal by letting me do virtually unlimited simulations.

<strong>NOTE:</strong> I find that Zsh kills the process and my terminal crashes if I attempt more than 10,000,000,000 (10 billion) flips at a time. 
This is a hardware issue (I'm on a MacBook Air 2024), so if you have an extremely powerful computer, you'll be able to handle more flips at a time.

# Installation
You need Python to run this project.

First, clone the repo:
```
git clone https://github.com/OWelton-Rosie/coin-flip-simulator
```

Navigate to it:
```
cd coin-flip-simulator
```

Run the program by executing:
```
python3 flipper.py
```

Or, if you're using an older version of Python:
```
python flipper.py
```

Immediately after the program does the first flip, a "coin_stats.txt" file will be created. This logs the total amount of flips, the amount of times it's landed on heads or tails, and the percentage values of each. You can reset the stats file at any time by selecting option 2 and confirming. 

In addition, a __pycache__ directory will be created. This stores `.pyc` files.
