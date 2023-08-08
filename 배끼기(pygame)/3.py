import pygame

screen_w = 800
screen_h = 600

white = (255, 255, 255)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()

color = black

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = red
        elif event.type == pygame.KEYUP:
            color = black
    screen.fill(white)
    rect = pygame.Rect(400,300,100,100)
    pygame.draw.rect(screen, color, rect , 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit(quit)
delattr()
