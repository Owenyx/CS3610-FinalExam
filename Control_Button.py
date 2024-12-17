from Button import Button

class Control_Button(Button):  
    # Ensure only one of each control button exists
    _up_exists = False
    _down_exists = False
    _left_exists = False
    _right_exists = False

    def __init__(self, text, x, y):
        # Perform checks to ensure only one of each control button exists
        # As well as ensuring the text is one of the four valid directions
        if text == "up":
            if Control_Button._up_exists:
                raise ValueError("Up control button already exists")
            Control_Button._up_exists = True
        elif text == "down":
            if Control_Button._down_exists:
                raise ValueError("Down control button already exists")
            Control_Button._down_exists = True
        elif text == "left":
            if Control_Button._left_exists:
                raise ValueError("Left control button already exists")
            Control_Button._left_exists = True
        elif text == "right":
            if Control_Button._right_exists:
                raise ValueError("Right control button already exists")
            Control_Button._right_exists = True
        else:
            raise ValueError("Control button text must be 'up', 'down', 'left', or 'right'")
        super().__init__(text, x, y)

    def click(self):
        print(self.text + " control button pressed")