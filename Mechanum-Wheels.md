# Mechanum Wheels

4pieces/lot 48mm 60mm 80mm 97mm High Hardness Plastic Mecanum Wheel Omni-Directional for TT Motor Smart Robot Car with 6mm hubs
<img width="369" height="375" alt="image" src="https://github.com/user-attachments/assets/65536de9-33ef-459d-8a65-a5f27005dc3a" />

## Significance

### Issue

Currently, my wheels consistently pop off, and the biggest problem is that they have a hard time turning. I spent one entire devlog addressing
this key issue. My workaround was sort of using physics by lowering the friction of the front right wheel and then making hte back heavy. The end result
is the back becoming an anchor, and with the low friction of the right front wheel, only the left wheel spins but since the center of the mass of the car
is around the back and the back does not move, the car just pivots. I used tape and this plastic band and even weight and a lab for this clever workaround more
details are in my devlog. The main point is that the current turning system is very bad and slow - its not a real turning system, its just a clever
workaround because turning did not work. ***Turning is the biggest bottleneck the car is facing, and mechanum wheels would remove that bottleneck.**** 
Since the turning is so akward, the car often bumps into walls or gets itself into a position where the distance sensor can't help after executing the turning maneaver. **Turning
leads to wheel damage which leads to more inaccurate turning which leads to more wheels damage and sensor damage, everyhting eventually resulting in the 
car breaking down.** Turning is the main reason the car runs end or fail.

### Fix - Mechanum Wheels

**Mechanum wheels skip that turning process entirely.** With mechanum wheels, you can acheive perfect omni-directional movement with the correct movement.
This is the main benefit but they also bring more.

1. *Turning becomes easier* - if I want to turn, then the mechnum wheels are bigger along with their quality and new car chassis will definitely
improve if not fix the turning issue.
2. *Less damage* - Turning used to lead to damge wich would lead to an infinite feedback loop of destruction to the car. Even though turning has
been skipped and corrected, if somehow the car gets damage, the big wheels would absorb the damage instead of the distance sensor or any other components.
And since they are strong they will not pop off or end the run because of the damage to the car.

## Physics

Mechanum wheels move using vector additon in physics, allowing them to acheive perfect omin-directional movement.

### How one wheel moves

Normal wheels move by using the friction force of the wheel moving. Mecuanum wheels get this force at another direction.
Consider two wheels, wheel A and wheel B. Wheel A has one roller at 90 degrees and Wheel B has one roller at 0 degrees. If you push the roller of roller A,
the roller only will spin but the wheel will not move. If you push the roller of roller B the wheel will move then every time the roller hits the ground it will
inch towards the right. But none of this is true turning.

*Wheel A:*

<img width="513" height="461" alt="image" src="https://github.com/user-attachments/assets/92a86a29-7f18-4d30-8669-35b15f94c55e" />

*Wheel B:*

<img width="604" height="335" alt="image" src="https://github.com/user-attachments/assets/ad4a25af-e2e2-4356-8574-85bb945dfb38" />

The solution is between in 45 degrees.
If you line a wheel with these 45 degree rollers than it is a combination of Wheel A and Wheel B. You can break apart the fricitonal force (green arrow)
into the x component (purple arrow) and y component (yelllow arrow). Since the yellow arrow behaves like Wheel A, it will not actually do anything.
Since the purple arrow behaves like Wheel B, it causes sideways motion.

<img width="712" height="574" alt="image" src="https://github.com/user-attachments/assets/7d575b38-efd1-4a97-8657-0324691d8d9e" />

The final key to perfecting the wheel is to create perforations on the wheel to better house all of the rollers and chisel the sides of the rollers so 
they don't bump into the ground. This adapts the rollers into the wheel and creates the mechanum wheel!

<img width="162" height="61" alt="image" src="https://github.com/user-attachments/assets/9e1cfa66-ecae-41ba-95a6-dcf90263f166" />

### How the wheels work together

Configureing four mechanum wheels isn't as simple as normal wheels. There must be two different mechanum wheel models so that the vector forces balance out, 
and just flipping the wheel will not help because this new wheel must have rotated rollers 45 degrees in the other direction. This is why the mechanum wheels
have 2 right and 2 left. With this setup, in order for the forces to work out, the right mechanum wheels must occupy right front and left back and the left
mechanum wheels must occupy left front and right back.

<img width="921" height="656" alt="image" src="https://github.com/user-attachments/assets/230bcb65-b549-441f-a401-30526f0f0f87" />

In the diagram, two of the arrows are pointing to the left (-y) and two of the arrows are pointing to the right (+y)/ This means that the y components of all
of the arrows will perfectly cancel out. But, all of the arrows, point forward (+x). This means taht all of the xs add up, resulting in sideways motion. Any
combination of spinning the wheels counter-clockwise vs clockwise can create any motion possible by mnipulating the direction of the arrows so certain parts cancel
out and certain parts don't.

## Software

By understanding how the wheels work together one can imagine how to program them. You would need to time when each pair is clockwise or counter-clockwise based
on where you want the arrows to point.

<img width="1920" height="999" alt="image" src="https://github.com/user-attachments/assets/af0bd591-fd08-41de-b599-34dbece254b5" />

This image has some common maneauvers but there are way more. The image depicts which way to turn the wheels (forward arrow clocwise and backward arrow counter-
clockwise. But how do you calculate how to acheive the arrows better and for more complicated movements?

The key is to use trignometry and angles. You can tilt everything and imagine angle theta. Then you can map each 
wheel to sin or cos with the angle detrmining where the arrow will point. Ex Pseudocode: left_front = power * cos(theta)

<img width="615" height="594" alt="image" src="https://github.com/user-attachments/assets/25aab56f-7bb6-4d84-8249-97b85b3b047a" />

The math gets more complicated after that when you involve complex turns and double checking for no accidental rotation, but that concept of using trignometry to 
determine the arrows is the main principle.

## Wiring

<img width="975" height="532" alt="image" src="https://github.com/user-attachments/assets/9a55c75d-2fcf-4411-b8dd-56046a0314dd" />

The front left and right back wheels should actually be like the diagram next to them with rollers rotated the other direction, but this is hard to do in Crikit
because flipping the wheel horizontally cannot acheive this. At the end, rollers should be pointed like an X. I previoulsy mentioned this; the way mechanum wheels
work just flipping them is not enough for the fornt left and front right. Crikit does not have this so I have a simple diagram of the correct orientation right next
to the wrong wheels.
Also, if the right hand wheels seem slightly smaller than the left hand wheels its because they are because I made a little mistake selecting the right one but it does
not affect functionality. The wires leading down just go to the Pi's GPIO pins. This is the same type of orientation as the current prototype but with double battery
pairs and double L298Ns.

Some good videos I watched and rewatched and places I learned everything from: https://www.youtube.com/watch?v=AlsCUzCCc-k, https://en.wikipedia.org/wiki/Mecanum_wheel, https://www.youtube.com/watch?v=noqBUEgyQ8A, https://www.youtube.com/watch?v=gnSW2QpkGXQ

**In summary, mechanum wheels are great for the car's movement and function by using physics vectors**
