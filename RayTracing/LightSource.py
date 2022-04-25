import math

from Ray import Ray


class LightSource(object):

    def __init__(self, pos):
        self.pos = pos
        self.rays = []
        self.ray_amount = 180
        self.generate_rays()

    def generate_rays(self):
        origin = self.pos
        angle = 0
        while angle < 360:
            vx = math.cos(math.radians(angle))
            vy = math.sin(math.radians(angle))
            self.rays.append(Ray(origin, (vx, vy)))
            angle += 360 / self.ray_amount

    def update_pos(self, new_pos):
        self.pos = new_pos
        for ray in self.rays:
            ray.origin = self.pos