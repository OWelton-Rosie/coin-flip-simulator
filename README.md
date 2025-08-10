This program was to help with a stats assignment on the difference between experimental and theoretical probability. It helped a great deal by letting me do virtually unlimited simulations. I'm now releasing it to the public. 

<strong>NOTE:</strong> This program uses a **lot** of battery power. If you need to conserve battery life, do not run this program!

# Installation
You need Python 3 to run this project.

First, clone the repo:
```
git clone https://github.com/OWelton-Rosie/coin-flip-simulator
```

Navigate to it:
```
cd coin-flipper
```

Run the program by executing:
```
python3 flipper.py
```

Shortly after executing, you will be asked to give permissions to your terminal/code editor to manage your computer. This is a result of the `anti_lock.py` file, which stops your computer from locking while you're running the simulation

Immediately after the program does the first flip, a `coin_stats.txt` file will be created. This logs the total amount of flips, the amount of times it's landed on heads or tails, and the percentage values of each. You can reset the stats file at any time by selecting option 2 and confirming. 

In addition, after your first flip, a  `__pycache__` directory will be created. This stores binary `.pyc` files.
