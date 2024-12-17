from Control_Button import Control_Button
from Subscriber import Subscriber

# Subject that is observed
class Click_Handler:
    def __init__(self):
        self.buttons = []
        self.subscribers = []

    # A button must be added in order to be clicked
    def add_button(self, button):
        self.buttons.append(button)

    def remove_button(self, button):
        self.buttons.remove(button)

    # Click on a button at the given coordinates if one exists there
    # If the button is a control button, notify all subscriber buttons of the direction pressed
    # If the button is a subscriber button, click it to register/unregister it, and add/remove it from the list of subscribers depending on the button's status
    def click(self, x, y):
        for button in self.buttons:
            if button.x == x and button.y == y:
                button.click()
                if isinstance(button, Subscriber):
                    if button.status == "registered":
                        self.add_subscriber(button) # Register the button since it was clicked and is now registered
                    else:
                        self.remove_subscriber(button) # Unregister the button since it was clicked and is now unregistered

                if isinstance(button, Control_Button):
                    direction = button.text
                    self.notify(direction)

    # Notify all subscriber buttons of the direction pressed
    def notify(self, direction):
        for button in self.subscribers:
            button.update(direction)

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)
