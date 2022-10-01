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
        self.grim_mouth = Line(p1,p2)
        self.grim_mouth.draw(window)
        self.__set_booleans(True, False, False, False, False)
        # initializing lists of coordinates to undraw
        self.smile_pts = []
        self.frown_pts = []
        self.leftEye_pts = []
        self.rightEye_pts = []

    def grim(self):
        self.__undrawing()
        self.grim_mouth.draw(self.window)
        if self.booleans[3]:
            self.leftEye.draw(self.window)
        if self.booleans[4]:
            self.rightEye.draw(self.window)
        self.__set_booleans(True, False, False, False, False)

    def smile(self):
        self.__undrawing()
        self.__smile_mouth()
        if self.booleans[3]:
            self.leftEye.draw(self.window)
        if self.booleans[4]:
            self.rightEye.draw(self.window)
        self.__set_booleans(False, True, False, False, False)

    def wink(self):
        self.__undrawing()
        self.__smile_mouth()
        self.__left_blink()
        if self.booleans[4]:
            self.rightEye.draw(self.window)
        self.__set_booleans(False, True, False, True, False)

    def frown(self):
        self.__undrawing()
        self.__frown_mouth()
        if self.booleans[3]:
            self.leftEye.draw(self.window)
        if self.booleans[4]:
            self.rightEye.draw(self.window)
        self.__set_booleans(False, False, True, False, False)
    
    def flinch(self):
        self.__undrawing()
        self.__frown_mouth()
        self.__left_blink()
        self.__right_blink()
        self.__set_booleans(False, False, True, True, True) 

    def __smile_mouth(self):
        h = self.center.getX()
        k = self.center.getY() + self.mouthSize/4
        x1 = round(h - self.mouthSize*0.65)
        x2 = round(h + self.mouthSize*0.65)
        a = self.mouthSize*0.65
        b = self.mouthSize/2
        for i in range(x1,x2+1):
            y = round((b * math.sqrt(1 - ((i-h)**2 / a**2))) + k)
            pt = Point(i,y).draw(self.window)
            self.smile_pts.append(pt)

    def __frown_mouth(self):
        h = self.center.getX()
        k = self.center.getY() + self.mouthSize*2/3
        x1 = round(h - self.mouthSize*0.65)
        x2 = round(h + self.mouthSize*0.65)
        a = self.mouthSize*0.65
        b = self.mouthSize/2
        for i in range(x1,x2+1):
            y = -(b * math.sqrt(1 - ((i-h)**2 / a**2))) + k
            pt = Point(i,y).draw(self.window)
            self.frown_pts.append(pt)

    def __left_blink(self):
        eye_center = self.leftEye.getCenter()
        self.leftEye.undraw()
        h = eye_center.getX()
        k = eye_center.getY() + self.eyeSize/4
        x1 = round(h - self.eyeSize*2/3)
        x2 = round(h + self.eyeSize*2/3)
        a = self.eyeSize*2/3
        b = self.eyeSize/5
        for i in range(x1,x2+1):
            y = -(b * math.sqrt(1 - ((i-h)**2 / a**2))) + k
            pt = Point(i,y).draw(self.window)
            self.leftEye_pts.append(pt)

    def __right_blink(self):
        eye_center = self.rightEye.getCenter()
        self.rightEye.undraw()
        h = eye_center.getX()
        k = eye_center.getY() + self.eyeSize/4
        x1 = round(h - self.eyeSize*2/3)
        x2 = round(h + self.eyeSize*2/3)
        a = self.eyeSize*2/3
        b = self.eyeSize/5
        for i in range(x1,x2+1):
            y = -(b * math.sqrt(1 - ((i-h)**2 / a**2))) + k
            pt = Point(i,y).draw(self.window)
            self.rightEye_pts.append(pt)

    def __set_booleans(self, isGrim, isSmile, isFrown, is_left_blink, is_right_blink):
        '''Setting face status (i.e. isSmile = True if mouth is smiling)'''
        self.booleans = [isGrim, isSmile, isFrown, is_left_blink, is_right_blink]

    def __deleteSemiEllipse(self, list):
        '''To delete the curve made to form a blinking eye or a smiling or frowning mouth'''
        for i in list:
            i.undraw()
        list = []

    def __undrawing(self):
        actions = [self.grim_mouth.undraw(), self.__deleteSemiEllipse(self.smile_pts),
            self.__deleteSemiEllipse(self.frown_pts), self.__deleteSemiEllipse(self.leftEye_pts),
            self.__deleteSemiEllipse(self.rightEye_pts)]
        for i in range(5):
            if self.booleans[i]:
                actions[i]