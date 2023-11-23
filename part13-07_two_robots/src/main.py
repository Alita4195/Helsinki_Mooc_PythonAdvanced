# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

upper_x = 0
upper_y = 100
upper_velocity = 1

lower_x = 0
lower_y = 300
lower_velocity = 2  # Double the speed of the upper robot

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((0, 0, 0))

    window.blit(robot, (upper_x, upper_y))
    window.blit(robot, (lower_x, lower_y))

    pygame.display.flip()

    upper_x += upper_velocity
    if upper_velocity > 0 and upper_x + robot.get_width() >= 640:
        upper_velocity = -upper_velocity
    if upper_velocity < 0 and upper_x <= 0:
        upper_velocity = -upper_velocity

    lower_x += lower_velocity
    if lower_velocity > 0 and lower_x + robot.get_width() >= 640:
        lower_velocity = -lower_velocity
    if lower_velocity < 0 and lower_x <= 0:
        lower_velocity = -lower_velocity

    clock.tick(60)
