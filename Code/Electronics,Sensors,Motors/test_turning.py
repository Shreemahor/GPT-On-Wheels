from basic_motor import motor_a, motor_b
# So I don't need to define everything again
from time import sleep

def stop():
    motor_a.stop()
    motor_b.stop()

SPEED = 0.8

# This is second place for the best turning method (after main.py's turn_right function)
# It is Random Arcs, arcing back and forth back and forth in this way to take advatage
# of weight and speed difference to slowly turn. This takes 20-30s and is unreliable,
# but at least it works. I used this before the other complicated physics turn in turn_right
# was discovered from testing the car
for i in range(10): # here 10 but can be variable
    # First possible working combo
    motor_a.forward(1) 
    motor_b.forward(SPEED)         
    sleep(1.5)
    motor_a.stop()
    motor_b.stop()
    sleep(0.3)
                    
    # Second possible working combo
    motor_a.backward(SPEED)
    motor_b.backward(1) 
    sleep(1.5)
    motor_a.stop()
    motor_b.stop()
    sleep(0.3)


stop()
motor_a.close()
motor_b.close()
print("Cleanup done.")

# This is second place but there are way more I tested:
# 3 Point Turn, Stop One Wheel Completely, Backward Arc, Small Arc, Zigzag Turn
# Hybrid Quick Turn, Stop-Go Arc, Double Arc Turns, Powerful Pivot, Back Full Power
# These were all unreliable, slow, and barely worked, they were found by just randomly testing
# The code for these is not here because it is unnecessary but it is just combinations of motors
#  forward and backward at different speeds and times
