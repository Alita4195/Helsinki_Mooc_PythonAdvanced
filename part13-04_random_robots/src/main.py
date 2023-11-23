# WRITE YOUR SOLUTION HERE:
import pygame

import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))
# window.blit(robot, (100, 50))  # blit draws the image at the location (100, 50)

width = robot.get_width()
height = robot.get_height()

num_robots = 1000

for num in range(num_robots):
    x = random.randint(0, 640 - width)  # Random x position within window width
    y = random.randint(0, 480 - height)  # Random y position within window height
    window.blit(robot, (x, y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
