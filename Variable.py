# Created by =: Owen Whalley
# Created on: 2022/09/27
#
# This program sets the counter's value to 0 on start.

counter = 0
counter = 0

# Created by: Owen Whalley
# Created on: 2022/09/27
# 
# This program increases the counter by 1 every time you press A. 

def on_buttton_pressed_a():
    global counter
    counter += 1 
input.on_button_pressed(Button.A, on_button_pressed_a)

# Created by: Owen Whalley
# Created on: 2022/09/27
#
# This program shows the number on the counter every time you press A+B.

def on_button_pressed_ab():
    basic.show_number(counter)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Created by: Owen Whalley
# Created on: 2022/09/27
#
# This program decreased the counter by 1 each time you press B.

def on_button_pressed_ab():
    global counter 
    counter += -1
input.on_button_pressed(Button.B, on_button_pressed_b)
