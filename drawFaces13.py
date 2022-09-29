from face import Face
from graphics import GraphWin, Point
from button import Button

def main():
    win = GraphWin('Faces', 500, 400)
    win.setCoords(0,40,50,0)
    Face(win, Point(17,20), 12)
    grim_button = Button(win, Point(40, 7.5), 8, 2.5, 'Grim')
    grim_button.activate()
    smile_button = Button(win, Point(40, 12.5), 8, 2.5, 'Smile')
    smile_button.activate()
    wink_button = Button(win, Point(40, 17.5), 8, 2.5, 'Wink')
    wink_button.activate()
    frown_button = Button(win, Point(40, 22.5), 8, 2.5, 'Frown')
    frown_button.activate()
    flinch_button = Button(win, Point(40, 27.5), 8, 2.5, 'Flinch')
    flinch_button.activate()
    quit_button = Button(win, Point(40, 32.5), 6, 2.5, 'Quit!')
    pt = win.getMouse()
    while not quit_button.clicked(pt):
        quit_button.activate()
        pt = win.getMouse()
    win.close()


if __name__=='__main__':
    main()