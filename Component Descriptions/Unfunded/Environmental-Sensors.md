# Environmental Sensors

Photoresistor:

<img width="385" height="443" alt="image" src="https://github.com/user-attachments/assets/fff8231b-e282-4e6a-ab6c-3be9acef9de9" />

Thermistor:

<img width="332" height="344" alt="image" src="https://github.com/user-attachments/assets/f18dbd95-a2be-4574-9820-29f6dd425c59" />

DHT11 Humidity:

<img width="538" height="453" alt="image" src="https://github.com/user-attachments/assets/260301a6-6865-4f70-8b51-de612a9e54a7" />

### Photoresistor

Its resistance varies with light. It has an analog output, so it is connected to the Pico. It provides context as to the light level, giving additional environmental sensing to GPT On Wheels.

### Thermistor

Its resistance varies with temperature. It has analog output, so it is connected to the Pico. It provides context as to the temperature, giving additional environmental sensing to GPT On Wheels.

### DHT11 Humidity

It records humidity, but does not have an analog output, so it is connected to the Pi 5. It provides humidity (and temperature), giving additional environmental sensing to GPT On Wheels.

## All

All of them are connected to the MB102's 3V3 rail.
Together they are very valuable in the project. Ex: if light increases, temperature fluctuates, and humidity changes then GPT On Wheels might be next to an open door or outside.
