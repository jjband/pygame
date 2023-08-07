import pygame


screen_w = 800
screen_h = 600

rect_x = screen_w//2
rect_y = screen_h//2

dx = 0
dy = 0


white = (255, 255, 255)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -5
            elif event.key == pygame.K_DOWN:
                dy = 5
            elif event.key == pygame.K_RIGHT:
                dx = 5
            elif event.key == pygame.K_LEFT:
                dx = -5
        if event.type == pygame.KEYUP:
            dx = 0
            dy = 0
    
    if rect_x == 700 or rect_y == 0 or rect_x == 0 or rect_y == 500:
        pygame.quit()

    rect_x += dx
    rect_y += dy
    
             

    screen.fill(white)
    rect = pygame.Rect(rect_x,rect_y,100,100)
    pygame.draw.rect(screen, blue , rect, 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
