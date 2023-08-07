import pygame

screen_w = 800
screen_h = 600

white = (255, 255, 255)
black = (0,0,0)

pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.draw.rect(screen, black, [50, 50, 100, 100], False )
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
