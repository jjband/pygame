import pygame
import os
screen_width = 800
screen_height = 600

gray = (200, 200, 200)

pygame.init()
pygame.display.set_caption("키보드")
screen = pygame.display.set_mode((screen_width, screen_height))
clock=  pygame.time.Clock()

current_pathh = os.path.dirname(__file__)
assets_path = os.path.join(current_pathh, "assets")
keyboard_image = pygame.image.load(os.path.join(assets_path, "keyboard.png"))
keyboard_x = int(screen_width/2)
keyboard_y = int(screen_height/2)
keyboard_dx = 0
keyboard_dy = 0


done = False
#게임 반복 구간
while not done:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            done = True
        elif event == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyboard_dx = -5
            elif event.key == pygame.K_RIGHT:
                keyboard_dx = 5
            elif event.key == pygame.K_UP:
                keyboard_dy = -5
            elif event.key == pygame.K_DOWN:
                keyboard_dy = 5
        elif event.type == pygame.KEYUP:
            keyboard_dx = 0
            keyboard_dy = 0
    screen.fill(gray)
    keyboard_x += keyboard_dx
    keyboard_y +=keyboard_dy
    screen.blit(keyboard_image, [keyboard_x, keyboard_y])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()