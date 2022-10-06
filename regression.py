from graphics import *

class Regression:

    def __init__(self):
        self.n = 0
        self.total_x = 0
        self.total_y = 0
        self.sum_xy_prod = 0
        self.sum_x_square = 0

    def addPoint(self, x, y):
        self.n = self.n + 1
        self.total_x = self.total_x + x
        self.total_y = self.total_y + y
        self.sum_xy_prod = self.sum_xy_prod + (x*y)
        self.sum_x_square = self.sum_x_square + (x*x)

    def predict(self, x):
        x_avg = self.total_x / self.n
        y_avg = self.total_y / self.n
        if self.n > 1:
            m = self.__slope__(x_avg, y_avg)
            y = y_avg + (m * (x - x_avg))
            return y
        else:
            return self.total_y

    def getN(self):
        return self.n

    def __slope__(self, x_avg, y_avg):
        numerator = self.sum_xy_prod - (self.n * x_avg * y_avg)
        denominator = self.sum_x_square - (self.n * x_avg)
        return numerator/denominator  