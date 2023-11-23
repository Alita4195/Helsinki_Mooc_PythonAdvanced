# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))
# window.blit(robot, (100, 50))  # blit draws the image at the location (100, 50)
width = robot.get_width()
height = robot.get_height()
rows = 10
columns = 10
for i in range(rows):
    for j in range(columns):
        x = j * width + (i * width // 4)
        y = i * height // 4
        window.blit(robot, (x, y))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
