# bas

from time import sleep
from gpiozero import Motor

motor_a = Motor(forward=23, backward=24, enable=18, pwm=True)
motor_b = Motor(forward=20, backward=21, enable=19, pwm=True)

motor_b.forward(0.5)
motor_a.forward(0.5)
#motor_b.forward(0.5)
sleep(8)
motor_a.stop()
motor_b.stop()
motor_a.close()
motor_b.close()


# uncomment below to run a simple forward/backward test

# try:
#     print("forward for 6")
#     motor_a.forward(0.7)
#     motor_b.forward(0.7)
#     sleep(6)

#     print("stop for 1")
#     motor_a.stop()
#     motor_b.stop()
#     sleep(1)

#     print("backward for 2")
#     motor_a.backward(0.7)
#     motor_b.backward(0.7)
#     sleep(2)

#     print("stop")
#     motor_a.stop()
#     motor_b.stop()
# except KeyboardInterrupt:
#     print("stopped, done")
# finally:
#     motor_a.stop()
#     motor_b.stop()
