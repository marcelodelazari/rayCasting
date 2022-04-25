class Ray(object):

    def __init__(self, origin, vector):
        self.origin = origin
        self.vector = vector

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