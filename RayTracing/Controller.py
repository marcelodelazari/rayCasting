import math

class Controller(object):

    def __init__(self, lightSource, obstacles, drawer):
        self.obstacles = obstacles
        self.lightSouce = lightSource
        self.drawer = drawer

    def get_collisions(self):
        def distance(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        collisions = []
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
            collisions.append(first_collision)
        return collisions

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            self.drawer.draw_obstacle(obstacle)

    def draw_rays(self):
        for index, collision_point in enumerate(self.get_collisions()):
            ray = self.lightSouce.rays[index]
            self.drawer.draw_ray(ray.origin, collision_point)
