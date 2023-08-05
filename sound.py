import pygame
import os
black = (0,0,0)
screen_width = 640
screen_height = 400


pygame.init()
pygame.display.set_caption("몰라")
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")
sound_image = pygame.image.load(os.path.join(assets_path, "equalizer.png"))
pygame.mixer.music.load(os.path.join(assets_path, "bgm.wav"))
pygame.mixer.music.play(-1)
sound = pygame.mixer.Sound(os.path.join(assets_path, "sound.wav"))





done = False

while not done:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound.play()
    screen.fill(black)
    screen.blit(sound_image, [0,0,600,400])
    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()