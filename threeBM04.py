from button import Button
from random import randint
from graphics import *

def main():
    win = GraphWin('Three Button Monte', 400, 400)
    b1 = Button(win, Point(200, 130), 60, 30, 'Door 1')
    b1.activate()
    b2 = Button(win, Point(200, 200), 60, 30, 'Door 2')
    b2.activate()
    b3 = Button(win, Point(200, 270), 60, 30, 'Door 3')
    b3.activate()
    quit_button = Button(win, Point(200, 340), 40, 20, 'Quit')
    msg = Text(Point(200, 60), 'Click on one of the buttons')
    msg.draw(win)

    pt = win.getMouse()

    Text(Point(100, 190), 'Wins:').draw(win)
    Text(Point(300, 190), 'Looses:').draw(win)
    wins = 0
    w_count = Text(Point(100, 210), '0')
    w_count.draw(win)
    looses = 0
    l_count = Text(Point(300, 210), '0')
    l_count.draw(win)
    while not quit_button.clicked(pt):
        if b1.clicked(pt) or b2.clicked(pt) or b3.clicked(pt):
            won = randint(1,3)
            if (won==1 and b1.clicked(pt)) or (won==2 and b2.clicked(pt)) or (won==3 and b3.clicked(pt)):
                msg.setText('You Win!!!')
                wins = wins + 1
                w_count.setText(str(wins))
                quit_button.activate()
            else:
                output_msg = 'You loss, the correct button was: "Door {0}"'.format(won)
                msg.setText(output_msg)
                looses = looses + 1
                l_count.setText(str(looses))
                quit_button.activate()
        pt = win.getMouse()
    win.close()

if __name__=='__main__':
    main()