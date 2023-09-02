import pygame
import random
import sys

screen_w = 900
screen_h = 700

white = (255, 255, 255)
orange = (250, 170, 70)
red = (255,0,0)
yellow = (255,255,51)
blue = (0,0,255)
black = (0,0,0)


color = red

class Life():
    def __init__(self, life2):
        self.life = life2

    def get_life(self):
        return self.life

    def set_life(self, life2):
        self.life += life2
        return self.life


class Player():
    def __init__(self):
        self.rect = pygame.Rect((screen_w // 2, 660, 30, 30))

    def move(self, direction):
        speed = 5
        self.rect.move_ip(direction * speed, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, color, self.rect.center, 15)
        

class Enemy():
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, screen_w)
        self.y = 0
        self.speed = random.randint(3, 7)
        self.radius = 5
        self.color = blue
        self.rect = pygame.Rect((self.x, self.y, 10, 10))

    def move(self):
        self.y += self.speed
        self.rect.move_ip(0, self.speed)
        if self.y > screen_h:
            self.reset()

    def check_crush(self, player, life):
        if self.rect.colliderect(player.rect):
            life.set_life(-1)
            self.reset()


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)


def display_life(screen, font, life):
    text = font.render(f"Life: {life.get_life()}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
        




def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("비 피하기")
    clock = pygame.time.Clock()
    player = Player()

    life_font = pygame.font.Font(None, 36)

    life = Life(3)
    enemies = [Enemy()for _ in range(15)]

    color = red
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


        for enemy in enemies:
            enemy.move()
            enemy.check_crush(player, life)


        screen.fill(white)
        player.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        display_life(screen, life_font, life)

        if life.get_life() <= 0:
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(140)
    pygame.quit()


if __name__ == '__main__':
    main()