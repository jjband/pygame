import pygame

screen_w = 800
screen_h = 600

white = (255, 255, 255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)


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
    rect2 = pygame.Rect(0,0,50,50)
    rect2.center = (screen_w//2, screen_h//2)
    pygame.draw.rect(screen, blue , rect2, 0)
    rect3 = pygame.Rect(200, 200, 20, 20)
    rect4 = pygame.Rect(200, 200, 40, 40)
    pygame.draw.rect(screen , green, rect4, False)
    pygame.draw.rect(screen , red, rect3, False)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
