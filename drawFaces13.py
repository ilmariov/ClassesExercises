from face import Face
from graphics import GraphWin, Point
from button import Button

def main():
    win = GraphWin('Faces', 500, 400)
    face = Face(win, Point(170,200), 120)
    grim_button = Button(win, Point(400, 75), 80, 25, 'Grim')
    grim_button.activate()
    smile_button = Button(win, Point(400, 125), 80, 25, 'Smile')
    smile_button.activate()
    wink_button = Button(win, Point(400, 175), 80, 25, 'Wink')
    wink_button.activate()
    frown_button = Button(win, Point(400, 225), 80, 25, 'Frown')
    frown_button.activate()
    flinch_button = Button(win, Point(400, 275), 80, 25, 'Flinch')
    flinch_button.activate()
    quit_button = Button(win, Point(400, 325), 60, 25, 'Quit!')
    pt = win.getMouse()
    while not quit_button.clicked(pt):
        if smile_button.clicked(pt):
            face.smile()
            quit_button.activate()
        elif wink_button.clicked(pt):
            face.wink()
            quit_button.activate()
        elif frown_button.clicked(pt):
            face.frown()
            quit_button.activate()
        elif flinch_button.clicked(pt):
            face.flinch()
            quit_button.activate()
        elif grim_button.clicked(pt):
            face.grim()
            quit_button.activate()
        pt = win.getMouse()
    win.close()


if __name__=='__main__':
    main()