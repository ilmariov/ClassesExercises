from graphics import *
from button import Button
from regression import Regression

def main():
    win = GraphWin('Regression Line', 600, 500)
    cartesian_plane(win, 300, 250)

def cartesian_plane(window, x_max, y_max):
    window.setCoords(-x_max, -y_max, x_max, y_max)
    x_axis = Line(Point(-x_max, 0), Point(x_max, 0))
    x_axis.setOutline('blue')
    x_axis.setWidth(2)
    x_axis.draw(window)
    y_axis = Line(Point(0, -y_max), Point(0, y_max))
    y_axis.setOutline('blue')
    y_axis.setWidth(2)
    y_axis.draw(window)


if __name__=='__main__':
    main()