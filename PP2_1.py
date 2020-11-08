import pygame
import random

pygame.init()
screen = pygame.display.set_mode((900,600))

def wildPanting():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    x = random.randint(0, screen.get_size()[0])
    y = random.randint(0, screen.get_size()[1])
    R = random.randint(10,500)

    pygame.draw.circle(screen, (r,g,b), (x,y), R)

run = True
FPS = 6
clock = pygame.time.Clock()

while run:
    millis = clock.tick(FPS)
    second = millis / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_u:
                FPS+=5
            if event.key == pygame.K_d:
                FPS-=5



    pygame.draw.circle((screen), (0,0,255), (50,50),50)
    #wildPanting()
    pygame.display.flip()