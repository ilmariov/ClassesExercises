# dieview.py
from graphics import *
from random import randint

class DieView:
    """DieView is a widget that displays a graphical representation
    of a standard six-sided die."""

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.: d1 = DieView(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides of length 20."""

        self.win = win
        self.background = 'white'
        self.psize = 0.1 * size
        hsize = size / 2.0
        offset = 0.6 * hsize

        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        self.pip1 = self.__makepip(cx-offset, cy-offset)
        self.pip2 = self.__makepip(cx-offset, cy)
        self.pip3 = self.__makepip(cx-offset, cy+offset)
        self.pip4 = self.__makepip(cx, cy)
        self.pip5 = self.__makepip(cx+offset, cy-offset)
        self.pip6 = self.__makepip(cx+offset, cy)
        self.pip7 = self.__makepip(cx+offset, cy+offset)

        self.setValue(1)

    def __makepip(self, x, y):
        "Internal helper method to draw a pip at (x,y)"
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        "Set this die to display value"
        self.value = value
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        foreground = color_rgb(r,g,b)
        self.setColor(foreground)

    def setColor(self, color):
        if self.value == 1:
            self.pip4.setFill(color)
        elif self.value == 2:
            self.pip1.setFill(color)
            self.pip7.setFill(color)
        elif self.value == 3:
            self.pip1.setFill(color)
            self.pip4.setFill(color)
            self.pip7.setFill(color)
        elif self.value == 4:
            self.pip1.setFill(color)
            self.pip3.setFill(color)
            self.pip5.setFill(color)
            self.pip7.setFill(color)
        elif self.value == 5:
            self.pip1.setFill(color)
            self.pip3.setFill(color)
            self.pip4.setFill(color)
            self.pip5.setFill(color)
            self.pip7.setFill(color)
        else:
            self.pip1.setFill(color)
            self.pip2.setFill(color)
            self.pip3.setFill(color)
            self.pip5.setFill(color)
            self.pip6.setFill(color)
            self.pip7.setFill(color)