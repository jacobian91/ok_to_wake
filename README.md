# Ok To Wake
This is a simple micropython project I did with my kids.

The primary function is that the RGB LED will light up different colors based on the time. The general idea is a visual alarm clock that means;
 - red: stay in bed
 - yellow: almost time
 - green: ok to wake up
 - white: idle

It is a simple project, and they enjoyed it. I used a raspberry pi pico, an RGB LED, and 3x 2.2kohm resistors.

# MicroPython
Thanks to the micropython team for all their hard work.
https://www.raspberrypi.com/documentation/microcontrollers/micropython.html

# WEBREPL
I added webrepl which from my reading isn't baked into the pico yet (but may be soon?). So there is a folder of the copied code from the micropython libary with the necessary files.

I made a change to the webrepl code where I made it so that previous connections would get dropped if a new one is requested. The reason behind this is that I was frustrated when my browser would have an error and leave the connection open and I had to restart the pico to get it back. There also is a config file I added that gives it a default password of '1234' to avoid needing seperate setup.

I pulled the files from here:
https://github.com/micropython/micropython-lib/tree/master/micropython/net/webrepl

Incase this moves here is the commit that added the files: https://github.com/micropython/micropython-lib/commit/cc2cdeb94bb1cac3bb6b32fcd06ddae323ceb771