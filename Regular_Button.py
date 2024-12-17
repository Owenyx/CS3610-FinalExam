from Button import Button
from Subscriber import Subscriber

#Subscriber to the Click_Handler class
class Regular_Button(Button, Subscriber):
    def __init__(self, text, x, y):
        super().__init__(text, x, y)
        self.status = "unregistered"

    # Move button
    def update(self, direction):
        if direction == "up":
            self.y += 1
        elif direction == "down":
            self.y -= 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        print("Moved " + self.text + " " + direction + " to (" + str(self.x) + ", " + str(self.y) + ")")

    def click(self):
        if self.status == "registered":
            self.status = "unregistered"
        else:
            self.status = "registered"
        print(self.status + " " + self.text)
