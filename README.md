# ✨🤖 GPT On Wheels ⚙️💡

***My homemade autonomous AI robot: What happens when you put a pan-tilt camera, speaker & mic, tof distance sensors, environmental sensors, and more on omni-directional wheels
and then let an AI control the body?***

Prototype:

<img width="1260" height="945" alt="image" src="https://github.com/user-attachments/assets/cadff312-ba82-44c8-aa8c-f7b8f666c1b0" />

https://github.com/user-attachments/assets/273ef500-5f55-4df4-99f9-baea8b3e9454

Rough Visualization once completed:

<img width="1920" height="1080" alt="render" src="https://github.com/user-attachments/assets/28723cca-3c67-482b-ab85-2bde168d2d86" />
(More on this later)

## What is it?

It's my homemade robot car designed to be able to do just as much as a human. I didn't just chose any sensor I could think of; each component is designed to mimic something that a human can do.
Eyes with a rotating head: camera with pan-tilt, Amazing acrobatic movement with legs: mechanum wheels, Ears to hear: microphone, Skin that feels: photoresistor thermistor humiditure, Mouth to talk:
Speaker, That intutive sense of where you're going: accelerometer/gyroscope, tof (time of flight) sensors, distance sensors, Face full of emotion: LCD Display, RGB LED, and finally most important of
all the brain: raspberry pi 5 and a pico. Along with batteries and power supply components like the wires, MB102, powerbanks, resistors, and breadboard - the blood, tissue, and flesh, and a huge 3-tiered 
chassis - the skeleton, it will work. but how will everything play together; humans can control and reason they are living, and you can't replicate that so GPT On Wheels seems impossible. But thats where AI
comes in - it takes the role of 'life'. Using new software like Embodied AI, Agentic AI and today's AI stack, GPT On Wheels could do many things that a human would.
It would be able to lots like: go around the environment, observe the environment, keep track of what's happening, speak, listen, interact, reason, think, do.

## Why?

Other than just inspiration from sci-fi movies, like the prototype is to the full GPT On Wheels, the full GPT On Wheels is a prototype for the future of robotics and AI.
It is the starting point for robots doing physical work human-like using reasoning like cooking, delivery, manufacturing, and more, and it explores whats happening right now with AI at the same time.
Its the idea of these specialized sensors with robotics and using AI creatively in an innovative way, what GPT On Wheels is, that;s is going to eventually become the future. Also, A human-like 
homemade robot for 211 dollars is a dream come true. It proves that you don't need thousands of dollars to experiment with hardware & AI that is cutting-edge. GPT On Wheels makes it accessible;
All you need is 211 dollars to build your own version what is changing our world. It's how I am learning robotics and preparing for the future.

## Prototype

There is a large variety of hardware components, so creating this human-like robot is an incredibly large task. So, using the components I already have, I created a prototype of GPT On Wheels. It's this prototype's wiring diagram, videos, pictures, and code that I already have. I will expand on and use the prototype as reference for the full GPT On Wheels.

## Project Guide

#### ***All of the project files, everything is divided into 4 Folders***

### 1. Component Descriptions

This folder has detailed descriptions of components in GPT On Wheels.

### 2. Wiring Diagrams

This has wiring diagrams for the prototype and full GPT On Wheels.
But I am also including the final version's wiring diagram in the README.

**Wiring of the full GPT On Wheels:**

<img width="3000" height="5079" alt="image" src="https://github.com/user-attachments/assets/5f15fbbc-46fd-4284-897f-afd6ef702710" />

### 3. Code

This has the entire code for the current working prototype, paving the way for the code for the full GPT On Wheels and proving that this is possible.

### 4. Outcome

This folder has videos and images of the prototype performing and the AI responses. It has all of the final output of the prototype. I managed to get this one video above in this README, by resizing and compressing it
but the other videos in Outcome are longer and cannot be viewed in github (download).

Check the folders in that order.
***Please actually fully read each of the 4 folders - they have lots of important information and work that is not in this in this README***

## Model

I am using cardboard for the chassis. Creating a full new CAD would be unnecessary since I already have a full prototype instead. Also, since I don't have a 3d printer
at home, and sensor placement is versatile, cardboard is the best option anyways. Also, I experimented with a CAD at the very start, and I found that cardboard was the best
option for GPT On Wheels.
<img width="1260" height="945" alt="image" src="https://github.com/user-attachments/assets/bb2a4fe2-950f-4367-a48a-4f529f4bebc9" />
<img width="1260" height="945" alt="image" src="https://github.com/user-attachments/assets/da179252-2af4-4dfd-a9e5-5a4a0cf10314" />
<img width="1260" height="945" alt="image" src="https://github.com/user-attachments/assets/699494c4-41ef-4ce2-b5c5-11e9f99b1851" />
<img width="1260" height="945" alt="image" src="https://github.com/user-attachments/assets/92d6716b-db62-4ed3-8d80-0b1d47a82a1d" />
CAD Model for visualization (not printing):
<img width="892" height="751" alt="image" src="https://github.com/user-attachments/assets/bdc7e365-2078-43ba-a9bb-9f48e20d3f9b" />
For the full version, I would replicate this design but stronger, with standoffs, screws more, and with 2 more floors.


***BUT - that is the prototype - not the full one***


3d blender visualization of the full GPT On Wheels:

<img width="1920" height="1080" alt="render" src="https://github.com/user-attachments/assets/f1762547-502b-49ed-bba3-0589948c798c" />

**This does not have all of the components, only the main front facing ones** *The wheels and chips are from the free blenderkit marketplace because designing a detailed circuit in blender would 
require way to much time*

The front facing cubes are the TOF sensors, and the goggle-like sensors are distance sensors. This setup ensures that the powerful sensor for distance is front with the other sensro preventing side rams.
In between the TOF sensors there is the RGB LED and behind is the L298N (closest thing I could find). The metallic sheet is the LCD Display. The red rectangular prisms are servos for pan-tilt. The pentagon on it is the camera. The wheels should be mechanum. On the second floor, behind is the raspberry pi 5. On the top floor, the black chip (hard to see in the render) represents a raspberry pi pico. The green parts on the top floor
represnt the photoresistor, thermistor, accelerometer. Also there would be the mic and speaker behind the pi on floor 2, but this is not visible in the picture. Most importantly all of the various long 
and extremley important collection of power, wires, resistors, screws, powerbanks, the MB102, breadboards and more are not represnted because the focus is on the human parallel, but they are still important.

## Insipiration & Resources

For hardware: https://docs.sunfounder.com

For hardware control: https://gpiozero.readthedocs.io/en/stable

For hardware guidance (this is not copy or guide because GPT On Wheels has lots of more and different components - mecanum mpu6050 v1l pan-tilt tof sensors and more
and this does not have any software, this was just guidance after I got the idea): https://www.youtube.com/watch?v=IT1uBUsOmUY

For software guidance - I watched 0 youtube videos on software - I mainly used my previous knowledge and this book: https://www.discountmags.com/products/generative-ai-w-langchain-2n-paperback
That book and its resources are where I got most of my fancy AI vocablulary.

Also 98% of the core logic code is by me, I barely used AI, only once or twice for path errors. I got most of the hardware code from online sources though.

Note on the JOURNAL.md: most of my devlogs are a slightly above 5 hours, but these ones have thousands of characters and lots of images to justify the time spent.

## BOM

<img width="1555" height="780" alt="image" src="https://github.com/user-attachments/assets/6c9eb229-152f-4136-a909-b642bfadd1cc" />

Additional charges of 6.77
<img width="371" height="348" alt="image" src="https://github.com/user-attachments/assets/a7641601-e017-4a8f-a5db-fd81d15a251c" />

**What I mean by this:**

<img width="537" height="466" alt="image" src="https://github.com/user-attachments/assets/20773847-cecc-410a-b4b7-a49f3faeeabd" />

*Aliexpress just gives a sales tax of 6.77 'As required by the relevant State Sales Tax Laws, the marketplace facilitator is required to collect Sales Tax and remit to the relevant tax authorities.'
Just like the 20.89 for shipping, I have no control over this sales tax of 6.77*

I cant wait to start building the full ✨🤖 GPT On Wheels ⚙️💡:)
