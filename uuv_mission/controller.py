class Controller:
    def __init__(self, gain):
        self.gain = gain

    def control(self, reference, height):
         e = reference - height
         u = self.gain*e
         
         return u