# L298N Driver

## Significance

The way that mechanum wheels work is that each motor must be controlled seperately so that each motor goes in the reverse direction. *4 Motors* need to controlled at the same time.
Each L298N controlls *two motors*. I already have 1 L298N, so I need one more L298N to make sure that the mechanum wheels can be properly controlled.

## Software

I will use gpiozero's Motor to control each motor. So in total there will be 4 of these, right now I only have 2.

## Wiring
