# VL53L1X TOF Sensor

2Pcs 1PCS MCU-531 VL53L1X Laser Distance Measurement Time-of-Flight Sensor Module 400 cm Distance Measurement with Pin Array

<img width="426" height="481" alt="image" src="https://github.com/user-attachments/assets/e388ae70-c8dc-45c1-8528-dca2f7ae86f2" />

## Significance

This is necessary so that the car truly knows where its going. Unlike the HC-SR04, this TOF, time of flight, sensor can go very long range and not be
affected by surfaces. It is also a lot more accurate than the HC-SR04. Considering that I already have 2 HC-SR04 and was planning to get more range 
detection, rather than buying more HC-SR04 buying this upgraded sensor is the better choice. At worst case scenario, if this does not work, the HC-SR04s are there
and on worst case scenario, the HC-SR04s are not working, this will serve as backup. The variety is good.

## Software

This sensor communicates to the via the I2C bus. I have worked with the I2C bus of the pi 5 in the past, and it usually involves running some commands and 
working with the bus in code. One of these commands is 'i2cdetect -y 1' to see what is in the I2C, it should show three ports (2 TOF sesors, 1 Accelerometor).

### Role of XShut

The MPU6050 accelerometer is on the same bus as the sensor, but the pi can distinguish them because they are different. However, if there are two sensor, then 
how will the pi differenciate them? Thats why XShut is needed to control the behavior of the VL53L1X. It can sort of 'turn off' a sensor so that the pi does
not detect it.

The code will:
1. Pull XShut low (turn the second sensor off)
2. Get the first sensor's address (0*29 is the defualt)
3. Pull XShut high (turn the second sensor on)
4. Change the second sensor's address to something else

So the pi is not confused, and all of the sensors can work in harmony.

## Wiring
