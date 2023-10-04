import pygame,os
import random

screen_w = 900
screen_h = 700
white = (255, 255, 255)
orange = (250, 170, 70)
red = (255,0,0)
yellow = (255,255,51)
blue = (0,0,255)
black = (0,0,0)
sky_blue = (135, 206, 235)
yellow_orange = (255, 214, 77)
white_green = (204, 255, 204)
color = red
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")
대머리모음 = "대머리1.png"


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
        self.image = pygame.image.load(os.path.join(assets_path, 대머리모음))
        self.radius = 15
        self.rect = self.image.get_rect()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.score = 0
        self.reset()

    def reset(self):
        self.rect.x = screen_w // 2 - self.width // 2 
        self.rect.y = screen_h - self.height // 2 -50
        
        
    def move(self, direction):
        speed = 5
        self.rect.move_ip(direction * speed, 0)
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
        
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

class Coin:
    def __init__(self):
        self.initialize_rect()
        
    def initialize_rect(self):  # 위치와 충돌 영역 초기화
        self.x = random.randint(50, 750)
        self.y = 0
        self.speed = 3
        self.radius = 10
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                self.radius * 2,self.radius * 2)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,0), (self.x,self.y), self.radius)

    def move(self):
        self.y += self.speed

    def check_crush(self,player):
        if player.rect.colliderect(self.rect):  
            player.score +=1  
            self.initialize_rect()  
        
            
def display_score(screen, font,score ):  
    score_text = font.render(f"Coin: {score}", True,(0 ,0 ,0))
    screen.blit(score_text,(screen_w -200 ,10))

def display_life(screen, font, life):
    text = font.render(f"머리카락 수: {life.get_life()}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

def display_timer(screen, font, start_time):



    milliseconds = pygame.time.get_ticks() - start_time

    seconds = milliseconds // 1000

    timer_text = font.render(f"Time: {seconds}", True, (0, 0, 0))

    screen.blit(timer_text, (screen_w - 100, 10))

def display_story(screen, font):
    story_text1 = font.render("탈모인에게 비는 매우 위험한 존재입니다.", True, (0, 0, 0))
    story_text2 = font.render("특히 산성비는 더욱 위험하지요.", True, (0, 0, 0))
    story_text3 = font.render("우리 탈모친구가 비를 피할수 있게 도와주세요!", True, (0, 0 ,255))
    screen.blit(story_text1, (20,200))
    screen.blit(story_text2, (20,260))
    screen.blit(story_text3, (20,320))
    




def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("산성비 피하기")
    clock = pygame.time.Clock()
    enemy_count = 10
    player = Player()
    life_font = pygame.font.Font(None, 36)
    timer_font = pygame.font.Font(None, 36)
    story_font = pygame.font.SysFont("Malgun Gothic", 36, 0,0)
    score_font = pygame.font.Font(None, 36)
    font = pygame.font.SysFont("Malgun Gothic", 30, True, True)
    font1 = pygame.font.SysFont("Malgun Gothic", 70, False, False)
    menu_text = font.render("Press space key to start game", True, (0, 0, 0))
    menu_text1 = font1.render("산성비를 조심해!", True, (0, 0, 100))  #이름(위)


    life = Life(5)
    best_time = 0
    start_time = None 
    enemies = [Enemy()for _ in range(enemy_count)]
    color = red
    running = True
    menu = True
    show_story = False
    coins = []
    spawn_coin = 0
    spawn_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:  
                    if menu:
                        menu = False
                        show_story = True
                    elif show_story:
                        show_story = False
                        start_time = pygame.time.get_ticks()
        if life == Life(4):
            대머리모음 = "대머리2.png"

        keys = pygame.key.get_pressed()
        if not menu and not show_story:
            if keys[pygame.K_LEFT]:
                player.move(-1)
            if keys[pygame.K_RIGHT]:
                player.move(1)

        if not menu and not show_story and pygame.time.get_ticks() - spawn_time > 3000:
            coins.append(Coin())
            spawn_time = pygame.time.get_ticks()

        for coin in coins[:]:
            coin.move()

            if coin.y > screen_h:
                coins.remove(coin)
                
            else:
                coin.draw(screen)

                if player.rect.colliderect(coin.rect):
                    player.score += 1
                    coins.remove(coin)

                
        if menu:
            screen.fill(yellow_orange)
            player.draw(screen)
            screen.blit(menu_text, (225,400))
            screen.blit(menu_text1, (200,175))

        elif show_story:        
            screen.fill(white_green)
            display_story(screen, story_font)

        else:
            for enemy in enemies:
                enemy.move()
                enemy.check_crush(player, life)

            screen.fill(sky_blue)
            player.draw(screen)


            for enemy in enemies:
                enemy.draw(screen)

            display_life(screen, life_font, life)
            display_score(screen,score_font, player.score)

            if start_time is not None:  
                display_timer(screen,timer_font,start_time)

            if life.get_life() <= 0:
                menu  = True
                life  = Life(5)
                start_time = None
       
                for enemy in enemies: 
                    enemy.reset()

                
        pygame.display.flip()
        clock.tick(120)

if __name__ == '__main__':
    main()