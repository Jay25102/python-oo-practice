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
        """
        initializes the SerialGenerator() class with the start param

        Attributes
        -----------------------
        start: int
            the starting number serialization will begin from and reset to
        currNum: int
            the current number being serialized

        """
        self.start = start
        self.currNum = start


    def __repr__(self):
        """basic description of this class"""
        return f"SerialGenerator() is a serial number generator with start value={self.start}"
    
    def generate(self):
        """add one to the current number but return value before adding"""
        temp = self.currNum
        self.currNum += 1
        return temp
    
    def reset(self):
        """resets the value of currNum back to the start number"""
        self.currNum = self.start
        