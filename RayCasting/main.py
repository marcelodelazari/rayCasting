import sys
import pygame

from Controller import Controller
from Drawer import Drawer
from LightSource import LightSource
from Obstacle import Obstacle

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RayCasting")

# Obstacles
grid = Obstacle([(-1, HEIGHT), (-1, 0), (WIDTH, 0), (WIDTH, HEIGHT)])
ob1 = Obstacle([(300, 450), (250, 200), (500, 200), (450, 550)])
ob2 = Obstacle([(700, 300), (800, 400), (1100, 600), (900, 250)])
obstacles = [grid, ob1, ob2]

# Classes
lightSource = LightSource((WIDTH//2, HEIGHT//2))
drawer = Drawer(screen, lightSource, obstacles)
controller = Controller(lightSource, obstacles, drawer)

running = True
clock = pygame.time.Clock()
show_casting = 1
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                # switch ray type
                show_casting = abs(show_casting - 1)
            elif event.key == pygame.K_r:
                # low range / infinite range
                controller.change_range()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        lightSource.aim_right()
    elif keys[pygame.K_LEFT]:
        lightSource.aim_left()

    lightSource.update_pos(pygame.mouse.get_pos())
    controller.update_collisions()
    if show_casting == 1:
        controller.draw_rays()
    else:
        controller.draw_test()

    controller.draw_obstacles()
    pygame.display.update()

    clock.tick()
    print("FPS:", clock.get_fps())