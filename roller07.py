from random import randint
from graphics import GraphWin, Point
from cbutton import CButton
from dieview import DieView

def main():
    win = GraphWin('Dice Roller', 300, 300)
    win.setCoords(0, 0, 30, 30)
    win.setBackground('green2')

    die1 = DieView(win, Point(10, 22), 7)
    die2 = DieView(win, Point(20, 22), 7)
    rollButton = CButton(win, Point(10, 10), 4.5, 'Roll Dice')
    rollButton.activate()
    quitButton = CButton(win, Point(20, 10), 3, 'Quit')

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randint(1,6)
            die1.setValue(value1)
            value2 = randint(1,6)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    win.close()


if __name__=='__main__':
    main()