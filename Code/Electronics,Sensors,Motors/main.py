"""This is the main initial testing file and the best of the basic electronic cpmponent code, and this one was the most
helpful one. This just makes the car go, then turn if it detects an obstacle, and repeat. This is where many of the issues
physically and in code were revealed."""

from gpiozero import Motor, DistanceSensor
from time import sleep

IN1 = 23
IN2 = 24
ENA = 18
IN3 = 20
IN4 = 21
ENB = 19
ECHO = 6
TRIGGER = 13

motor_a = Motor(forward=IN1, backward=IN2, enable=ENA, pwm=True)
motor_b = Motor(forward=IN3, backward=IN4, enable=ENB, pwm=True)
sensor = DistanceSensor(echo=ECHO, trigger=TRIGGER, max_distance=4)

SAFE_DISTANCE = 80     
BACKUP_DISTANCE = 50    
NORMAL_SPEED = 0.6      
TURN_SPEED = 1.0       
BACKUP_TIME = 2.5       
TURN_TIME = 5       

def move_forward():
    motor_a.forward(NORMAL_SPEED)
    motor_b.forward(NORMAL_SPEED)


def move_backward():
    motor_a.backward(NORMAL_SPEED)
    motor_b.backward(NORMAL_SPEED)


def turn_right():
    print("turning")
    motor_a.stop()  
    motor_b.forward(TURN_SPEED)  
    sleep(TURN_TIME)  
    stop_motors()

def stop_motors():
    motor_a.stop()
    motor_b.stop()


def avoid_obstacle():
    print("OBSTACLE - Executing avoidance maneuver")
    stop_motors()
    sleep(0.3)
    
    # Check if its too close - back up if it is
    current_distance = sensor.distance * 100
    if current_distance < BACKUP_DISTANCE:
        print(f"Too close ({round(current_distance, 2)} cm) - Backing up...")
        move_backward()
        sleep(BACKUP_TIME)
        stop_motors()
        sleep(0.3)

    print("Turning right...")
    turn_right()
    
    # Check if path is clear after turning
    new_distance = sensor.distance * 100
    if new_distance < SAFE_DISTANCE:
        print(f"Path still blocked ({round(new_distance, 2)} cm) - Turning right again...")
        # Turn right again to find clear path
        turn_right()
    
    print("Resuming forward motion")


print("starting")

if __name__ == "__main__":
    try:
        while True:
            # Get distance reading
            distance_cm = sensor.distance * 100
            
            # Check if obstacle detected
            if distance_cm > 400:
                # Out of range - assume clear path
                print("Clear path (out of range) - moving forward")
                move_forward()
            elif distance_cm < SAFE_DISTANCE:
                # Obstacle detected - avoid it
                avoid_obstacle()
            else:
                # Clear path - move forward
                print(f"Clear path ({round(distance_cm, 2)} cm) - moving forward")
                move_forward()
            
            sleep(1)  # Check distance frequently for quick response

    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        # Clean shutdown
        stop_motors()
        motor_a.close()
        motor_b.close()
        sensor.close()
        print("Robot stopped and cleaned up.")
