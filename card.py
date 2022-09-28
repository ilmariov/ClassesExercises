from graphics import GraphWin, Image, Point

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        if self.rank == 1:
            return 1
        elif self.rank > 10:
            return 10
        else:
            return self.rank

    def draw(self, win, center):
        filename = str(self.rank) + self.suit +'.ppm'
        card1 = Image(center, filename)
        card1.draw(win)
    
    def __str__(self):
        ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        suits = ['d', 'c', 'h', 's']
        suits_name = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

        for i in range(4):
            for j in range(13):
                if self.rank == j+1 and suits[i] == self.suit:
                    return '{0} of {1}'.format(ranks[j], suits_name[i])