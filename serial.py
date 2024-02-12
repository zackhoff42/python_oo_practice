"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.copy = start
        self.counter = 0

    def generate(self):
        """Returns incremented self.start value each time it is ran. Returns the initial self.start value the first time."""
        if self.counter != 0:
            self.start += 1
            return self.start
        
        self.counter += 1
        return self.start
    
    def reset(self):
        """Resets self.start and self.counter back to their initial values."""
        self.counter = 0
        self.start = self.copy