from graphics import *
from projectile import *

def main():
    win = GraphWin('Projectile Animation', 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)
    Line(Point(-10,0), Point(210,0)).draw(win)
    for x in range(0, 210, 50):
        Text(Point(x,-5), str(x)).draw(win)
        Line(Point(x,0), Point(x,2)).draw(win)    
    angle, vel, height = 45.0, 40.0, 2.0
    target = Target(win, 210)
    hit_target = False
    while not(hit_target):
        inputwin = InputDialog(angle, vel, height)
        choice = inputwin.interact()
        if choice == 'Quit':
            break
        angle, vel, height = inputwin.getValues()
        shot = ShotTracker(win, angle, vel, height)
        while 0 <= shot.getY() and 0 <= shot.getX() <= 210:
            shot.update(1/50)
            update(50)
        inputwin.close()
        if 0 <= shot.getX() <= 210:
            hit_target = target.hitTarget(shot)
    win.close()


if __name__=='__main__':main()