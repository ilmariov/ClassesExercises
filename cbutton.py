from graphics import *
import math

class CButton:

    """A button is a labeled circle in a window. It is activated 
    or deactivated with the activate () and deactivate () methods. 
    The clicked (p) method returns true if the button is active and 
    p is inside it."""

    def __init__(self, win, center, radius, label):
        """Creates a circular button , eg:
        qb = Button (myWin, centerPoint, radius , 'Quit')"""

        self.radius = radius
        self.h = center.getX()
        self.k = center.getY()
        self.circ = Circle(center, radius)
        self.circ.setFill('lightgray')
        self.circ.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns True if button is active  and p is inside"
        x, y = p.getX(), p.getY()
        r = math.sqrt((x - self.h)**2 + (y - self.k)**2)
        return (self.active and self.radius >= r)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.circ.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.circ.setWidth(1)
        self.active = False