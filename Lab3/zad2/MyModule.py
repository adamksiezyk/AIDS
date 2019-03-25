import math

class triangle:
    a = 0
    b = 0
    c = 0

    def __init__(self, x1, x2, x3):
        self.a = x1
        self.b = x2
        self.c = x3
    
    def obw(self):
        o = self.a + self.b + self.c
        return o

    def pole(self):
        p = self.obw() / 2
        P = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return P

class circle:
    r = 0

    def __init__(self, r_):
        self.r = r_

    def obw(self):
        o = 2 * math.pi * self.r
        return o

    def pole(self):
        P = math.pow(self.r , 2) * math.pi
        return P

class square:
    a = 0

    def __init__(self, a_):
        self.a = a_

    def obw(self):
        o = 4 * self.a
        return o

    def pole(self):
        P = self.a * self.a
        return P