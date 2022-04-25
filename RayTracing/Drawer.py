import pygame
import pygame.gfxdraw

class Drawer(object):
    def __init__(self, screen, lightSource, obstacles):
        self.screen = screen
        self.lightSource = lightSource
        self.obstacles = obstacles


    def draw_obstacle(self, obstacle):
        pygame.gfxdraw.aapolygon(self.screen, obstacle.points,  (200, 200, 200))
    def draw_ray(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        pygame.gfxdraw.line(self.screen, x1, y1, x2, y2, (220, 220, 220))