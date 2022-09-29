from graphics import *
import math

class Face:

    def __init__(self, window, center, size):
        self.window = window
        self.center = center
        self.size = size
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        self.mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-self.mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(self.mouthSize/2, mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(window)

    def smile(self):
        self.mouth.undraw()
        h = self.center.getX()
        k = self.center.getY()
        x1 = round(h - self.mouthSize/2)
        x2 = round(h + self.mouthSize/2)
        a = self.mouthSize/2
        b = self.mouthSize/3
        for i in range(x1,x2+1):
            y = (b * math.sqrt(1 - ((i-h)**2 / a**2))) + k
            Point(i,y).draw(self.window)
