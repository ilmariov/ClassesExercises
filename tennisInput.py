from graphics import *
from button import Button

class TennisInput:
    """A custom window for getting simulation values (probA, probB,
    and games) from the user."""

    def __init__(self, probA, probB, games):
        """Build and display the input window"""

        self.win = win = GraphWin('Initial Values', 400, 300)
        win.setCoords(0, 4.5, 6, 0.5)

        Text(Point(2,1), 'Prob. Player A').draw(win)
        self.probA = Entry(Point(4.5,1), 5)
        self.probA.draw(win)
        self.probA.setText(str(probA))

        Text(Point(2,2), 'Prob. Player B').draw(win)
        self.probB = Entry(Point(4.5,2), 5)
        self.probB.draw(win)
        self.probB.setText(str(probB))

        Text(Point(2,3), 'Num of games').draw(win)
        self.games = Entry(Point(4.5,3), 7)
        self.games.draw(win)
        self.games.setText(str(games))

        self.fire = Button(win, Point(3,4), 1.25, .5, 'Fire!')
        self.fire.activate()

    def interact(self):
        """wait for user to click Quit or Fire button returns a string 
        indicating which button was clicked"""

        while True:
            pt = self.win.getMouse()
            if self.fire.clicked(pt):
                return 'Fire!'

    def getValues(self):
        """ return input values """
        probA = float(self.probA.getText())
        probB = float(self.probB.getText())
        games = int(self.games.getText())
        return probA, probB, games

    def close(self):
        """ close the input window """
        self.win.close()