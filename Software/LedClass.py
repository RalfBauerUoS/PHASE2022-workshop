#!/usr/bin/env python

from matrix11x7 import Matrix11x7

class LED():
    def __init__(self):
        self.matrix11x7 = Matrix11x7()
        self.x = 0.5
        
    def LEDon(self):
        self.matrix11x7.fill(self.x, 0, 0, 11, 7)
        self.matrix11x7.show()
        
    def LEDoff(self):
        self.matrix11x7.fill(0)
        self.matrix11x7.show()
        
    def LEDbrightness(self, brightness):
        self.x = brightness/10
        self.matrix11x7.fill(self.x, 0, 0, 11, 7)
        self.matrix11x7.show()
        return self