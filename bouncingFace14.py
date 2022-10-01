from face import Face
from random import randint
from graphics import GraphWin, Point, update

def main():
    win_width = 500
    win_height = 400
    win = GraphWin('Faces', win_width, win_height, autoflush=False)
    size = 120
    face = Face(win, Point(win_width/2, win_height/2), size)
    dx, dy = 1, 1
    for i in range(1000):
        face.moveFace(dx,dy)
        center = face.getHeadCenter()
        x, y = center.getX(), center.getY()
        if x + size >= win_width:
            switchFace(face)
            dx = -1
        elif x - size <= 0:
            switchFace(face)         
            dx = 1
        elif y + size >= win_height:
            switchFace(face)
            dy = -1
        elif y - size <= 0:
            switchFace(face)
            dy = 1
        update(30)
    win.getMouse()
    win.close()

def switchFace(face):
    ran_num = randint(0,4)
    if ran_num == 0:
        return face.grim()
    elif ran_num == 1:
        return face.smile()
    elif ran_num == 2:
        return face.wink()
    elif ran_num == 3:
        return face.frown()
    else:
        return face.flinch()


if __name__=='__main__':
    main()