import math


class Ray(object):

    def __init__(self, origin, angle):
        self.origin = origin
        self.angle = angle
        self.vector = self.update_vector()
        self.moving_speed = 3

    def update_vector(self):
        vx = math.cos(math.radians(self.angle))
        vy = math.sin(math.radians(self.angle))
        self.vector = vx, vy
        return vx, vy

    def collides_segment(self, segment):

        x1, y1 = segment[0]
        x2, y2 = segment[1]

        x, y = self.origin
        dx, dy = self.vector
        if x1 == x2:
            x1 -= 0.000001
        if dy / dx != (y2 - y1) / (x2 - x1):
            d = dx * (y2 - y1) - dy * (x2 - x1)
            if d:
                r = (((y - y1) * (x2 - x1)) - (x - x1) * (y2 - y1)) / d
                s = (((y - y1) * dx) - (x - x1) * dy) / d
                if r >= 0 and s >= 0 and s <= 1:
                    return x + r * dx, y + r * dy

        return False

    def end_pos(self, range):
        return self.origin[0] + range * self.vector[0], self.origin[1] + range * self.vector[1]

    def move_right(self):
        self.angle += self.moving_speed
        self.update_vector()

    def move_left(self):
        self.angle -= self.moving_speed
        self.update_vector()