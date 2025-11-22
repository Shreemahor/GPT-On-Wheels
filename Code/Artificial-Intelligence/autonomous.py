"""File for autnomous robot that naviagtes around obstacles and logs its journey
Combines the main.py from Electronics,Sensors,Motors with the AI logic in MCP_agent.py"""

# imports
from MCP_agent import llm, agent, viewer
from langchain_core.messages.human import HumanMessage
from picamera2 import Picamera2, Preview
from gpiozero import Motor, DistanceSensor
from time import sleep
import asyncio
import random

# pins and values
ENA = 18
IN1 = 23
IN2 = 24
ENB = 19
IN3 = 20
IN4 = 21
ECHO_PIN = 6
TRIGGER_PIN = 13
SAFE_DISTANCE = 80
BACKUP_DISTANCE = 50
MOTOR_SPEED = 0.6
TURN_SPEED = 1.0
BACKUP_TIME = 2
TIME = 5.1

# will store the log of what AI sees
log = ""

# cooldown for periodic image capture
periodic = 0

# starting camera
cam = Picamera2()
camera_config = cam.create_still_configuration(main={"size": (1920, 1080)})
cam.configure(camera_config)
cam.start()
sleep(2) # 2 seconds for the camera to warm up
front_motors = Motor(forward=IN1, backward=IN2, enable=ENA, pwm=True) # motors
back_motors = Motor(forward=IN3, backward=IN4, enable=ENB, pwm=True)
sensor = DistanceSensor(echo=ECHO_PIN, trigger=TRIGGER_PIN, max_distance=4) # sensor

def forward(): # to go forward
    front_motors.forward(MOTOR_SPEED)
    back_motors.forward(MOTOR_SPEED)

def backward(): # to go backward
    front_motors.backward(MOTOR_SPEED)
    back_motors.backward(MOTOR_SPEED)

def turn(): # turning with the modified wheel
    print("turning")
    front_motors.stop()
    back_motors.forward(TURN_SPEED)
    sleep(TIME)
    stop()

def stop(): # stop
    front_motors.stop()
    back_motors.stop()

if __name__ == "__main__":
    try:
        while True:
            # updating values
            distance = sensor.distance * 100
            periodic += 1
            
            if distance < SAFE_DISTANCE: # obstacle detected
                print(f"obstacle at {round(distance, 2)}!")
                stop()
                print("Capturing")
                cam.capture_file("/home/shreemahor5/Python/Artificial-Intelligence/image.jpg")
                sleep(0.5)
                answer = asyncio.run(viewer())
                print(answer)
                log = log + "\n" + answer

                print("obstacle")
                stop()  
                current_distance = sensor.distance * 100
                if current_distance < BACKUP_DISTANCE: # too close
                    print("Too close")
                    backward()
                    sleep(BACKUP_TIME)
                    stop()
                    sleep(0.3)
                turn() # avoid it
                
                new_distance = sensor.distance * 100
                if new_distance < SAFE_DISTANCE: # to make sure the path is still not blocked
                    print("blocked")
                    turn()
                periodic = 0
                
            else:
                print(f"Clear path ({round(distance, 2)} cm) - moving forward")
                forward()
                
                if periodic >= 8.7: # periodic image capture
                    print("Periodic image capture...")
                    cam.capture_file("/home/shreemahor5/Python/Artificial-Intelligence/image.jpg")
                    sleep(0.5)
                    answer = asyncio.run(viewer()) # using MCP_agent
                    print(answer)
                    log = log + "\n" + answer
                    periodic = 0
            
            sleep(1) # cooldown for sensor

    except KeyboardInterrupt:
        print("\nStopped")
    finally:
        print("\nDone")
        print(log) # final output
        # stopping everything
        stop()
        cam.stop()
        cam.close()
        front_motors.close()
        back_motors.close()
        sensor.close()
        print("Stopped")
