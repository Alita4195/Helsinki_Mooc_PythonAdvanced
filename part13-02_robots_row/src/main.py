# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))
# window.blit(robot, (100, 50))  # blit draws the image at the location (100, 50)
width = robot.get_width()

n = 1
x = 0
y = 0
while n <= 10:
    window.blit(robot, (x, y))
    x += width
    n += 1


width = robot.get_width()
height = robot.get_height()


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
