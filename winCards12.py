from card import Card
from graphics import GraphWin, Point
from random import randint

def main():
    win = GraphWin('Cards', 400, 200)
    win.setCoords(0, 0, 60, 20)
    suits = ['d', 'c', 'h', 's']
    x = 10
    for i in range(5):
        rank = randint(1,13)
        suit_num = randint(0,3)
        suit = suits[suit_num]
        card = Card(rank, suit)
        card.draw(win, Point(x,10))
        x = x + 10
    win.getMouse()
    win.close()


if __name__=='__main__':
    main()