import pygame, random
from time import sleep

#게임 화면 설정
screen_width = 800
screen_height = 600
grid_size = 20
grid_width = (screen_width/grid_size)
grid_height = (screen_height/grid_size)


#색깔 설정
white = (255,255,255)
orange = (250,150,0)
gray = (100,100,100)
black = (0,0,0)

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

#스네이크 만들기
class Snake():
    def __init__(self) :
        self.create()
    
    #스네이크 길이, 처음 시작 방향 설정
    def create(self):
        self.length = 2
        self.positions = [(int(screen_width/2), int(screen_height/2))]
        self.direction = random.choice([up, down, left, right])
    def control(self, xy):  #xy에 up, down, left, right의 값이 들어간다~~~
        if (xy[0]*-1, xy[1]*-1) == self.direction:
            return
        else:
            self.direction = xy
    #움직이기 함수
    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (cur[0]+(x*grid_size), (cur[1]+(y*grid_size)))

        if new in self.positions[2:]:
            sleep(1)
            self.create()
        elif new[0] < 0 or new[0]>=screen_width or new[1] < 0 or new[1] >=screen_height:
            sleep(1)
            self.create()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
    def eat(self):
        self.length +=1
    def draw(self, screen):
        for p in self.positions:
            rect = pygame.Rect(p[0], p[1], grid_size, grid_size)
            pygame.draw.rect(screen, gray, rect)

#먹이 설정
class Feed():
    def __init__(self):
        self.position = (0,0)
        self.color = orange
        self.create()
    #먹이 위치 정하기
    def create(self):
        x = random.randint(0, grid_width)
        y = random.randint(0, grid_height)
        self.position = x*grid_size, y*grid_size
    #먹어 그리기
    def draw(self, screen):
        rect = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(screen, self.color, rect)        

#걍 게임 운영
class Game:
    def __init__(self):
        self.snake = Snake()
        self.feed = Feed()
        self.speed = 5
    
    #방향키 입력 받기
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_UP:
                    self.snake.control(up)
                elif event.key == pygame.K_DOWN:
                    self.snake.control(down)
                elif event.key == pygame.K_LEFT:
                    self.snake.control(left)
                elif event.key == pygame.K_RIGHT:
                    self.snake.control(right)
        return False
    def run_logic(self):
        self.snake.move()
        self.check_eat(self.snake, self.feed)
        self.speed = (10+self.snake.length)/2

    def check_eat(self, snake, feed):
        if snake.positions[0] == feed.position:
            snake.eat()
            feed.create()
    
    def draw_info(self, length, speed, screen):
        info = "Length:"+str(length)+"/ Speed:"+str(speed)
        font = pygame.font.SysFont("FixedSys", 30,False, False )
        text_obj = font.render(info, True, black)
        text_rect = text_obj.get_rect()
        text_rect.x, text_rect.y = 10, 10
        screen.blit(text_obj, text_rect)

    def display_frame(self, screen):
        screen.fill(white)
        self.draw_info(self.snake.length, self.speed, screen)
        self.feed.draw(screen)
        self.snake.draw(screen)
        screen.blit(screen, (0,0))



            

def main():
    pygame.init()
    pygame.display.set_caption("snake game")
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    done = False
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        
        clock.tick(game.speed)
    pygame.quit()


if __name__ == '__main__':
    main()