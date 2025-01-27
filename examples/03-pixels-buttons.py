
from modulino import ModulinoButtons, VirtualModulinoPixels

buttons = ModulinoButtons()
pixels = VirtualModulinoPixels()


buttons.on_button_a_press = lambda : print("Button A pressed")
buttons.on_button_b_press = lambda : print("Button B pressed")
buttons.on_button_c_press = lambda : print("Button C pressed")

buttons.on_button_a_release = lambda : print("Button A released")
buttons.on_button_b_release = lambda : print("Button B released")
buttons.on_button_c_release = lambda : print("Button C released")

while True:
    buttons_state_changed = buttons.update()
    if buttons_state_changed:
        if buttons.is_pressed(0):
            pixels.set_rgb(0, 255, 255, 255)
        if buttons.is_pressed(1):
            pixels.set_rgb(1, 255, 255, 255)
        if buttons.is_pressed(2):
            pixels.set_rgb(2, 255, 255, 255)
        if not buttons.is_pressed(0):
            pixels.set_rgb(0, 0, 0, 0)
        if not buttons.is_pressed(1):
            pixels.set_rgb(1, 0, 0, 0)
        if not buttons.is_pressed(2):
            pixels.set_rgb(2, 0, 0, 0)
        pixels.show()
