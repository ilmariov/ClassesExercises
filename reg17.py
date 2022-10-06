from graphics import *
from button import Button
from regression import Regression

def main():
    win = GraphWin('Regression Line', 600, 500)
    cartesian_plane(win, 300, 250)
    plot_button = Button(win, Point(250, -200), 50, 20, 'Plot')
    plot_button.activate()
    msg = Text(Point(0,200), 'Click to add points')
    msg.draw(win)
    linear_reg = Regression()
    n = 0
    pt = win.getMouse()
    while not plot_button.clicked(pt):
        x = pt.getX()
        y = pt.getY()
        Circle(Point(x,y), 1).draw(win)
        linear_reg.addPoint(x,y)
        n = linear_reg.getN()
        pt = win.getMouse()
    if n >=2:
        draw_line(win, 300, 250, linear_reg)
        msg.setText('Click to exit')
    else:
        msg.setText('More points needed. Click to exit')
    win.getMouse()
    win.close()

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
    
def draw_line(window, x_max, y_max, reg_obj):
    for x in range(-x_max, x_max, 3):
        y = reg_obj.predict(x)
        line_dots = Circle(Point(x,y), 1)
        line_dots.setOutline('green')
        line_dots.draw(window)


if __name__=='__main__':
    main()