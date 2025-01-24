# Animation
# Difficulty: medium
# Material:. Modulino Pixels

# Exercise:
# Using the Modulino Pixels, create a continuous animation (that never ends) that lights up one LED at a time starting from LED 0 to LED 7
# and then goes back lighting up one LED from LED 6 to LED 0 (and then repeats the sequence without ever stopping).
# At any given moment, one and only one LED is on.

# The sequence should be as follows, executed forever:
# - LED 0 on, LED 0 off, LED 1 on, LED 1 off,..., LED 7 on, LED 7 off
# - LED 6 on, LED 6 off, LED 5 on, LED 5 off, … , LED 1 on, LED 1 off


# from modulino import VirtualModulinoPixels, ModulinoColor
from v_modulino import ModulinoColor, ModulinoPixels
from time import sleep

pixels = ModulinoPixels()

pixels.set_rgb(0, 0, 0, 0, 20)
pixels.show()

# print(ModulinoColor.GREEN)

# for index in range(0, 8):
#     color_wheel_colors = [
#         (255, 0, 0),
#         (255, 85, 0),
#         (255, 255, 0),
#         (0, 255, 0),
#         (0, 255, 255),
#         (0, 0, 255),
#         (255, 0, 255),
#         (255, 0, 0)
#     ]
#     pixels.set_rgb(index, *color_wheel_colors[index], 40)
# pixels.show()


# pixels.set_all_rgb(255, 255, 255)
# pixels.show()


# Night Rider animation

for j in range(0, 3):
    for i in range(0, 8):
        pixels.clear_all()
        pixels.set_rgb(i, 255, 0, 0, 100)
        pixels.show()
        sleep(0.05)

    for i in range(7, -1, -1):
        pixels.clear_all()
        pixels.set_rgb(i, 255, 0, 0, 100)
        pixels.show()
        sleep(0.05)


# Turn off all LEDs
pixels.clear_all()
pixels.show()
