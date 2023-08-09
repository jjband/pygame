import pygame
import random

life = 3


screen_w = 900
screen_h = 700

white = (255, 255, 255)
orange = (250, 170, 70)
red = (255,0,0)
yellow = (255,255,51)


color  = red


class Player():
    def __init__(self):
        self.rect()

    def rect(self):
        self.x = screen_w // 2
        self.y = 660
        self.dx = 0
        self.radius = 15

    def move(self, direction):
        speed = 5
        self.x += direction * speed

    def draw(self, screen):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
        


class Enemy():
    def __init__(self):
        self.rect()

    def rect(self):
        self.x = random.randint(0, screen_w)


class Game():
    


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("비 피하기")
    clock = pygame.time.Clock()
    player = Player()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1)
        if keys[pygame.K_RIGHT]:
            player.move(1)



        screen.fill(white)
        player.draw(screen)

        pygame.display.flip()
        clock.tick(120)
    pygame.quit()


if __name__ == '__main__':
    main()