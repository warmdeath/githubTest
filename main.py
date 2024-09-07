import pygame

pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("pYGAME")

x = 0
y = 0
w = 20
h = 20

run = True

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1
        
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,w,h))
    pygame.display.update()
