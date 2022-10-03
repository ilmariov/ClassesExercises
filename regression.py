class Regression:

    def __init__(self):
        self.n = 0
        self.total_x = 0
        self.total_y = 0
        self.sum_xy_prod = 0
        self.sum_x_square = 0
        self.x_avg = self.total_x / self.n
        self.y_avg = self.total_y / self.n

    def addPoint(self, x, y):
        self.n = self.n + 1
        self.total_x = self.total_x + x
        self.total_y = self.total_y + y
        self.sum_xy_prod = self.sum_xy_prod + (x*y)
        self.sum_x_square = self.sum_x_square + (x*x)

    def predict(self, x):
        if self.n > 1:
            m = self.__slope__()
            y = self.y_avg + (m * (x - self.x_avg))
            return y
        else:
            return self.total_y

    def __slope__(self):
        numerator = self.sum_xy_prod - (self.n * self.x_avg * self.y_avg)
        denominator = self.sum_x_square - (self.n * self.x_avg)
        return numerator/denominator