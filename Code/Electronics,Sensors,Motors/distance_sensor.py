"""I used this to test the ditance sensor, and here is wher I discovered the NoEcho error and the other
distance sensor issues due to ground wiring problems. This is just a simple loop that prints the distance every 2 seconds"""

from gpiozero import DistanceSensor
from time import sleep
from main import sensor

while True:
    print("Distance to nearest object is", round(sensor.distance * 100, 2), "cm")
    sleep(2)
