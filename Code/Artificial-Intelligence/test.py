"""Simple test file that is a simulation of main.py but much simpler; it retains the main flow and logic structure."""

# I didn't how to make main.py at first, so I made this simple test file to simulate its behavior and
# see how it would work

import random
from time import sleep
while True:  # loop
    if input("Do you want to run the test? (y/n): ").lower() != 'y': #  confirmation
        break
    number = random.randint(1, 100)  # represents where the AI would process
    sleep(3)
    print(number) # returns the final AI output
