import pygame
import os

current_path = os.path.dirname(__file__)   # 현재 파일이 있는 디렉토리를 가져옵니다.
assets_path = os.path.join(current_path, "assets")

screen_w = 900
screen_h = 700

white = (255, 255, 255)
orange = (250, 170, 70)


class Player():
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = screen_w // 2
        self.y = 660
        self.dx = 0
        self.radius = 15
        self.color = orange

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


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


if __name__ == '__main__':
    main()
