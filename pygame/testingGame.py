import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 50
y = 50
movement_change = (0, 0)
width = 50
height = 50
velocity = 5

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        movement_change = (-1, 0)
    if keys[pygame.K_RIGHT]:
        movement_change = (1, 0)
    if keys[pygame.K_UP]:
        movement_change = (0, -1)
    if keys[pygame.K_DOWN]:
        movement_change = (0, 1)
    x += movement_change[0] * velocity
    y += movement_change[1] * velocity
    win.fill((0,0,0))
    pygame.draw.rect(win, (200,50,150), (x, y, width, height))
    pygame.display.update()

pygame.quit()