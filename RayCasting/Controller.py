import math


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


class Controller(object):

    def __init__(self, lightSource, obstacles, drawer):
        self.obstacles = obstacles
        self.lightSouce = lightSource
        self.drawer = drawer

        self.collisions = []

        self.ray_range = 0
        self.ray_ranges = [10000, 300]

    def update_collisions(self):
        collisions = self.collisions
        collisions.clear()
        for ray in self.lightSouce.rays:
            first_collision = (10000, 10000)
            first_collision_distance = 100000
            for obstacle in self.obstacles:
                for wall in obstacle.get_walls():
                    collision_point = ray.collides_segment(wall)
                    if collision_point:
                        current_distance = distance(ray.origin, collision_point)
                        if current_distance < first_collision_distance:
                            first_collision = collision_point
                            first_collision_distance = current_distance

            if distance(ray.origin, first_collision) > self.ray_ranges[self.ray_range]:
                first_collision = self.get_ray_end_pos(ray)
            collisions.append(first_collision)
        return collisions

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            self.drawer.draw_obstacle(obstacle)

    def draw_rays(self):
        collisions = self.collisions
        for index, collision_point in enumerate(collisions):
            ray = self.lightSouce.rays[index]
            self.drawer.draw_ray(ray.origin, collision_point)

    def draw_test(self):
        polygons = []
        collisions = self.collisions
        origin = self.lightSouce.pos
        for i in range(len(collisions)-1):
            col1 = collisions[i]
            if i != len(collisions) - 1:
                col2 = collisions[i + 1]
            else:
                col2 = collisions[0]
            polygons.append((origin, col1, col2))
        for polygon in polygons:
            self.drawer.draw_test(polygon)

    def change_range(self):
        self.ray_range += 1
        self.ray_range %= len(self.ray_ranges)

    def get_ray_end_pos(self, ray):
        return ray.end_pos(self.ray_ranges[self.ray_range])
