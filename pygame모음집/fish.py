import pygame
import os

screen_w = 900
screen_h = 700

white = (255, 255, 255)
sea = (80, 180, 220)
ground = (140, 120, 40)
dark_groud = (70, 60, 20)

current_path = os.path.dirname(__name__)
assets_path = os.path.join(current_path, "assets")
#플레이어(물고기) 생성
class Fish():
    def __init__(self):
        self.image = pygame.image.load(os.path.join(assets_path, "fish.png"))
        self.sound = pygame.mixer.Sound(os.path.join(assets_path, "swim.wav"))
        self.rect = self.image.get_rect()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.reset()
    
    def reset(self):
        self.rect.x = 250
        self.rect.y = 250
        self.dx = 0
        self.dy = 0
    
    def swim(self):
        self.dy -=10
        self.sound.play()
    
    def update(self):
        self.dy +=.3
        self.rect.y += self.dy

        #물고기가 화면 위로 올라갔을 때
        if self.rect.y <= 0:
            self.rect.y = 0
        #물고기가 화면 아래로 내려갔을 때
        if self.rect.y > screen_h-self.height:
            self.rect.y = screen_h-self.height
            self.dy = 0
        
        if self.dy > 20:
            self.dy = 20

    def draw(self, screen):
        screen.blit(self.image, self.rect)




def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("물고기의 여행")
    clock = pygame.time.Clock()
    fish = Fish()
    running = True
    while running:
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fish.update()
        screen.fill(sea)
        fish.draw(screen)
        pygame.display.flip()
        clock.tick(120)
pygame.quit()

main()