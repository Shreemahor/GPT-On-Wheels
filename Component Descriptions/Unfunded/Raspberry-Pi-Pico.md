# Raspberry Pi Pico W
<img width="441" height="420" alt="image" src="https://github.com/user-attachments/assets/6c491ca1-736d-4e44-9b84-914ba18daf27" />

## Why its necessary

The photoresistor and thermistor have analog outputs. The Pi 5 does not accept analog outputs, but the Pico does. So, I am going to use the Pico to communicate with them,
then use the Pi 5 to communicate with the Pico. This is a good workaround by not requiring an SDC to convert analog to digital for the Pi 5, since the Pico can do it.
The Pico is also powered by the MB102's 3V3 rail, but just in case the rail does not have enough remaining, the Pi 5's pin can also be used.

## How it Communicates with the Pi 5

There are 3 Ways that I could do this:
1. USB Connection
2. UART Pin Connection
3. Wifi

Because UART consumes 2 pins and Wifi leads to the Pico consuming of more mA of power and I don't want to risk the MB-102's power rail supply ending, I will use usb.
Pi has 4 ports total: 1 I used for storage, 1 I used for the mic, 1 I used for the speaker, leaving one for the pico.

Additionally, if the Pi 5 runs out of GPIO, the Pico is available.
