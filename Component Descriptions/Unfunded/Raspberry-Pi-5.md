# Raspberry Pi 5

<img width="894" height="581" alt="image" src="https://github.com/user-attachments/assets/0e008de2-25d4-4f4f-94f1-0465d68b48da" />

The perfect SBC for Edge AI. It also has ports for 5V and 3.3V just in case the MB-102 fails, and it has the perfect way to connect to 
the camera with the flat ribbon cable. Being the newest pi, it has the most GPIO and robustness, almost all of which I use in this project.

### Connections

The way I connect my pi is not standard.

##### Power

I use the *Miady Powerbank into the USB-c*. The strange thing is that initially the pi would say low voltage but I figured out htat the powerbanks
just needed more charging.

##### Display

Here it where I get creative, before I used to just plug the HDMI into my monitor but thats impossible on a moving car. So, I have RealVNC Player,
an app that allows me to access my pi remotely on my computer using a shared network. RealVNC makes it easy to just plug in power, open RealVNC and 
get going.

##### Memory

Most pis use micro-SD cards, but since I have a pi 5, I have more options. The other option was a hat, a cord like extension from the pi's top,
for storage, but the hat broke a long time ago so I used a different method. When the hat broke, the hat broke, not the NVMe card that actually
had the storage connected to the hat. So, I got a *NVMe to USB adapter* because the pi has 4 USB ports. But it does not end there - the adapter 
converted the *card* to USB-c so I needed another USB-c to USB then plugged it into the pi. In the end there is just another component connected
to the pi via USB, but the card is truly powerful. In all of the pictures, the components wrapped in the white bag is this.

![WhatsApp Image 2025-11-17 at 19 49 38_32018dcf](https://github.com/user-attachments/assets/996b9f88-4ff9-46e6-b68b-28054182bbd6)

##### Case

That is the black encasing that is visible at the front. It protect the pi from damage and is very useful.

### Other

The pi has a great CPU, GPU, and overall performance. That's exactly why its good for a big AI project like this. Also, everything I code in the 
pi 5 is python in VS Code.

