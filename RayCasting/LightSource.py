from Ray import Ray


class LightSource(object):

    def __init__(self, pos):
        self.pos = pos
        self.rays = []
        self.ray_amount = 720

        self.angle = 60
        self.generate_rays()

    def generate_rays(self):
        origin = self.pos
        current_angle = 0
        while current_angle < self.angle:
            self.rays.append(Ray(origin, current_angle))
            current_angle += self.angle / self.ray_amount

    def update_pos(self, new_pos):
        self.pos = new_pos
        for ray in self.rays:
            ray.origin = self.pos

    def aim_right(self):
        for ray in self.rays:
            ray.move_right()

    def aim_left(self):
        for ray in self.rays:
            ray.move_left()
