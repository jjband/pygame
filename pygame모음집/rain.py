import pygame
import os

current_path = os.path.dirname(__name__)
assets_path = os.path.join(current_path, "assets")

screen_w = 900
screen_h = 700

white = (255, 255, 255)
orange = (250,170,70)

class Player():
    def __init__(self):

        self.image = pygame.image.load(os.path.join(assets_path, "New Piskel-1.png (1).png"))
        self.rect = self.image.get_rect()
        self.reset()
        self.rect = pygame.Rect(screen_w//2, 660, 15, 15)
        self.reset()

    def reset(self):
        self.rect.x = screen_w//2
        self.rect.y = 660
        self.dx = 0

    def draw(self,screen):
        screen.blit()


    def reset(self):
        self.rect.x = screen_w//2
        self.rect.y = 660
        self.dx = 0


    def draw(self,screen):
        screen.blit(self.image, self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("산성비 피하기")
    clock = pygame.time.Clock()
    player = Player()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #screen.fill(white)
        player.draw(screen)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("산성비 피하기")
    clock = pygame.time.Clock()
    player = Player()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(white)
        player.draw(screen)

        pygame.display.flip()
        clock.tick(120)
    pygame.quit()


main()

