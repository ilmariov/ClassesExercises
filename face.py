from graphics import *
import math

class Face:

    def __init__(self, window, center, size):
        self.window = window
        self.center = center
        self.size = size
        self.eyeSize = 0.15 * size
        eyeOff = size / 3.0
        self.mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, self.eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, self.eyeSize)
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
        k = self.center.getY() + self.mouthSize/4
        x1 = round(h - self.mouthSize*0.65)
        x2 = round(h + self.mouthSize*0.65)
        a = self.mouthSize*0.65
        b = self.mouthSize/2
        for i in range(x1,x2+1):
            y = (b * math.sqrt(1 - ((i-h)**2 / a**2))) + k
            Point(i,y).draw(self.window)

    def wink(self):
        self.mouth.undraw()
        h = self.center.getX()
        k = self.center.getY() + self.mouthSize/4
        x1 = round(h - self.mouthSize*0.65)
        x2 = round(h + self.mouthSize*0.65)
        a = self.mouthSize*0.65
        b = self.mouthSize/2
        for i in range(x1,x2+1):
            y = (b * math.sqrt(1 - ((i-h)**2 / a**2))) + k
            Point(i,y).draw(self.window)
        eye_center = self.leftEye.getCenter()
        self.leftEye.undraw()
        h1 = eye_center.getX()
        k1 = eye_center.getY() + self.eyeSize/4
        x3 = round(h1 - self.eyeSize*2/3)
        x4 = round(h1 + self.eyeSize*2/3)
        a1 = self.eyeSize*2/3
        b1 = self.eyeSize/5
        for j in range(x3,x4+1):
            y1 = -(b1 * math.sqrt(1 - ((j-h1)**2 / a1**2))) + k1
            Point(j,y1).draw(self.window)

    def frown(self):
        self.mouth.undraw()
        h = self.center.getX()
        k = self.center.getY() + self.mouthSize*2/3
        x1 = round(h - self.mouthSize*0.65)
        x2 = round(h + self.mouthSize*0.65)
        a = self.mouthSize*0.65
        b = self.mouthSize/2
        for i in range(x1,x2+1):
            y = -(b * math.sqrt(1 - ((i-h)**2 / a**2))) + k
            Point(i,y).draw(self.window)
    
    def flinch(self):
        self.mouth.undraw()
        h = self.center.getX()
        k = self.center.getY() + self.mouthSize*2/3
        x1 = round(h - self.mouthSize*0.65)
        x2 = round(h + self.mouthSize*0.65)
        a = self.mouthSize*0.65
        b = self.mouthSize/2
        for i in range(x1,x2+1):
            y = -(b * math.sqrt(1 - ((i-h)**2 / a**2))) + k
            Point(i,y).draw(self.window)
        eye_center1 = self.leftEye.getCenter()
        self.leftEye.undraw()
        h1 = eye_center1.getX()
        k1 = eye_center1.getY() + self.eyeSize/4
        x3 = round(h1 - self.eyeSize*2/3)
        x4 = round(h1 + self.eyeSize*2/3)
        a1 = self.eyeSize*2/3
        b1 = self.eyeSize/5
        for j in range(x3,x4+1):
            y1 = -(b1 * math.sqrt(1 - ((j-h1)**2 / a1**2))) + k1
            Point(j,y1).draw(self.window)
        eye_center2 = self.rightEye.getCenter()
        self.rightEye.undraw()
        h2 = eye_center2.getX()
        k2 = eye_center2.getY() + self.eyeSize/4
        x5 = round(h2 - self.eyeSize*2/3)
        x6 = round(h2 + self.eyeSize*2/3)
        a2 = self.eyeSize*2/3
        b2 = self.eyeSize/5
        for m in range(x5,x6+1):
            y2 = -(b2 * math.sqrt(1 - ((m-h2)**2 / a2**2))) + k2
            Point(m,y2).draw(self.window)