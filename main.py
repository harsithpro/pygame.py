import pygame
pygame.init()
screen=pygame.display.set_mode((1000,1000))
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
pygame.quit()