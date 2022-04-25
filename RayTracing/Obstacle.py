import math
import numpy as np

class Obstacle(object):

    def __init__(self, points):
        self.points = points # bottom_left -> top_left -> top_right -> bottom_right

    def get_upper(self):
        return self.points[1], self.points[2]

    def get_bottom(self):
        return self.points[0], self.points[3]

    def get_right(self):
        return self.points[2], self.points[3]

    def get_left(self):
        return self.points[0], self.points[1]

    def get_walls(self):
        return [self.get_bottom(), self.get_right(), self.get_upper(), self.get_left()]
