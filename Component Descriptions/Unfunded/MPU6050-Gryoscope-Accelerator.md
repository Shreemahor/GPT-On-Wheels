# MPU6050 Gyroscope Accelerator

<img width="894" height="746" alt="image" src="https://github.com/user-attachments/assets/da23e3c1-471b-4740-983b-d0ba29474ab6" />

### Why its necessary

At first its not obvious what gryroscope accelerator does or means at it was not obvious to me to at first. But all the MPU6050 does is 
gather data on the speed and location of the car, so you can determine its coordinates, how fast its going, and more motionwise.

#### Collision

Now collisions can be detected, if speed  suddenly drops to zero the AI knows it has collided and instead of just coninuing it actually backs up
and turns. This is extremely useful if any sensor fail or it just collides somehow. If there is a slow decline in speed with the same motor
power, the AI can tell something is wrong.

#### Angle (Turn)

The prototype just turns the strange way I programmed it to, then when it collides it just gets more damaged and turns worst.
If the AI knows what angle it at, it can calculate what to do and immediately correct itself by programming what way to point the mechanum wheel
arrows using the angle and rotate using mecahnum wheels (as described in Mechanum-Wheels.md). This is just another solution to the prototype's
biggest bottleneck.

#### Future

For LIDAR, SLAM, sensor data combining or any other more advanced program I want to implement in the future, this is necessary. It's best
to just get it now, improve collision reaction and angle reaction and pave the way for future upgrades.

### Other

Connected using the I2C bus. Programming is nothing complicated but just getting values off of it and then knowing what they represent and 
how to use them. Knowing how to calculate speed and angle from its values - which is just math.
