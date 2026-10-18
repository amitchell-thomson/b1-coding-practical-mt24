class Controller:
    def __init__(self, gain_p, gain_d):
        self.gain_p = gain_p
        self.gain_d = gain_d
        self.e_0 = 0

    def control(self, reference, height):
         e = reference - height
         u = self.gain_p*e + self.gain_d*(e - self.e_0)
         self.e_0 = e
         return u