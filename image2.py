import pygame
import os
#창 크기 설정(가로, 세로)
screen_width = 640
screen_height = 320
#색
Land = (160,120,40)
#초기화
pygame.init()
pygame.display.set_caption("image")
screen = pygame.display.set_mode((screen_width, screen_height)) #큐플의 형태로 사용(오류 코드:TypeError: size must be two numbers)
# 화면 업데이트 속도
clock = pygame.time.Clock()


#그림 불러오기
current_path = os.path.dirname(__file__) #현 작업 중 file을 current_path에 들어감(os.path.dirname)
assets_path = os.path.join(current_path, "assets")
background_image = pygame.image.load(os.path.join(assets_path, "terrain.png"))
mushroom1 = pygame.image.load(os.path.join(assets_path, "mushroom1.png"))
mushroom2 = pygame.image.load(os.path.join(assets_path, "mushroom2.png"))
mushroom3 = pygame.image.load(os.path.join(assets_path, "mushroom3.png"))


#게임 반복 구간
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(Land)
    screen.blit(background_image, background_image.get_rect())
    screen.blit(mushroom1, [100, 50])
    screen.blit(mushroom2, [200, 115])
    screen.blit(mushroom3, [350, 136])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()