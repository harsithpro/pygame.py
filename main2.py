import pygame
pygame.init()
screen_width,screen_height=500,500
display_surface=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("background image")
background_image=pygame.transform.scale(pygame.image.load("naruto.jpg").convert(),(screen_height,screen_width))
background_rect=background_image.get_rect(center=(screen_width//2,screen_height//2-30))
def gameloop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        display_surface.blit(background_image,(0,0))
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=='__main__':
    gameloop()