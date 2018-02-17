# Banana Drone - The Bug-free Buggy
This repository is for my autonomous RC car project using a Raspberry Pi and an off-the-shelf RC car. Training and navigation are handled by Keras and TensorFlow.

This project was started shortly after November 24th, when the RC car was purchased. If a human can drive the car visually using only the video from the camera broadcast, then a convolutional neural network should be able to learn how to do it as well.

More documentation can be found in each directory.

One of the assumptions made was that any single frame should be sufficient to determine a direction for the car to go and so every file is considered to be a miniature dataset all by itself. This could open up interesting training opportunities with shuffling the collected datasets during training and testing.

The hardware is comprised of a remote control car purchased for about $15 on sale (typical retail is $30 to $50), a standard drone camera ($15), an easycap analog video digitizer ($15), three 16850 cells reclaimed from laptops ($5-$10 each if new), and a number of wires and connectors. Keeping costs low was another design goal.

Testing on the batteries showed the Pi and video reciever to remain powered for about 8 hours under no load. Under full load on the Raspberry Pi, the batteries should last about 3 hours.

One of the design goals was to modify the original RC car as little as possible.A small amount of moldable plastic was used to affix the drone camera to the top of the vehicle. The remote was taken apart and new connections were soldered to the PCB pads but it remains completely functional. An added benefit of the direct connection to the remote is that the Pi can change the mode of the GPIO pins to either control the car or record a human driver.

