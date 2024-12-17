from abc import ABC, abstractmethod

class Button(ABC):
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

    @abstractmethod
    def click(self):
        pass
