# MB102 Power Supply Module

MB-102 MB102 Breadboard 400 830 Point 65 Jumper Wires Solderless PCB Bread Board Test Develop DIY for Arduino Power Module


<img width="454" height="287" alt="image" src="https://github.com/user-attachments/assets/c507d7f6-1aaf-485a-ac87-f964a05c932a" />

## Significance

This is neccessary for powering the TOF sensors and the distance sensors and the accelerometer. It also has breadboard in its name because it gives these
other components power by powering into the breadboard. You put it in and then one of the vcc breadboard rails becomes the 3.3V rail and the other one becomes
the 5V rail. Which is which depends on where you put the jumpers, if you put the left jumper on 3.3 it becomes 3.3 if you put the left jumper on 5 it becomes 5.

In the worst case scenario where the MB102 does not work I will just use the pi's voltage but I am not going to fully rely on this because the pi's pins are 
affected by too many external factors like what the pi is doing and the powerbank, so it is unreliable and unsafe.

## Software

The MB102 does not interact with the software, but everything that powers it does.

## Wiring

<img width="359" height="491" alt="image" src="https://github.com/user-attachments/assets/a2b46136-dafa-4129-a477-9ab76d875186" />

The MC-102 fits nicely into the breadboard and occupies the rails. The way I have put it is left rail as 5V and right rail as 3.3V. The MB102
will be powered by another one of the same Miady powerbanks that powers the pi. However the MB102 accepts usb but the powerbank output is usb-c
, in order to solve this I am just going to be using a usb to usb-c connector or just making sure that the output from the powerbank is actually
usb.

Something else to beware of is to put it the right way, which is where the sideways text reds upright, but this view looks upside but its not
so its a bit confusing. I accidently put it upside down making + blue and - red, and then after some time realized it was backwards and spend a
lot of time deleting and flipping it back up then doing all of the connections again.

<img width="868" height="685" alt="mbwrongvright" src="https://github.com/user-attachments/assets/4882eb9b-6310-4cb4-8d8a-504b7360b6b2" />

The MB102 is exactly what I need to power all of the components.
