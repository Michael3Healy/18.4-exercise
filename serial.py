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

    def __init__(self, start=0):
        self.start = start
        self.counter = 0

    def __repr__(self):
        return f'<SerialGenerator start={self.start} next={self.generate()}'

    def generate(self):
        """Adds one to the serial number"""
        serial_number = self.start + self.counter
        self.counter += 1
        return serial_number
    
    def reset(self):
        """Resets serial number back to starting number"""
        self.counter = 0
