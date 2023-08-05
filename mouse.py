import pygame
import os
screen_width = 800
screen_height = 600
white = (255,255,255)

pygame.init()
pygame.display.set_caption("마우스")
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")
mouse_image = pygame.image.load(os.path.join(assets_path, "mouse.png"))


pygame.mouse.set_visible(False)

done = False
while not done:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            done = True
    pos = pygame.mouse.get_pos()
    screen.fill(white)
    screen.blit(mouse_image, pos)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

