from Regular_Button import Regular_Button
from Control_Button import Control_Button
from Click_Handler import Click_Handler

up_button = Control_Button("up", 5, 6)
down_button = Control_Button("down", 5, 4)
left_button = Control_Button("left", 4, 5)
right_button = Control_Button("right", 6, 5)

button1 = Regular_Button("Button 1", 1, 1)
button2 = Regular_Button("Button 2", 2, 2)
button3 = Regular_Button("Button 3", 3, 3)

# Add buttons so they can be clicked
click_handler = Click_Handler()
click_handler.add_button(up_button)
click_handler.add_button(down_button)
click_handler.add_button(left_button)
click_handler.add_button(right_button)
click_handler.add_button(button1)
click_handler.add_button(button2)
click_handler.add_button(button3)

# Click the regular buttons to add them as subscribers so they can be notified
click_handler.click(1, 1)
click_handler.click(2, 2)
click_handler.click(3, 3)

print("--------------------------------")
click_handler.click(5, 6) # Click the up button
print("--------------------------------")
click_handler.click(2, 3) # Unregister button 2
print("--------------------------------")
click_handler.click(6, 5) # Click the right button
print("--------------------------------")
click_handler.click(5, 4) # Click the down button
print("--------------------------------")
click_handler.click(2, 3) # Register button 2 again
print("--------------------------------")
click_handler.click(4, 5) # Click the left button