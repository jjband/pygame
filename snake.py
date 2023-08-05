import pygame, random
from time import sleep

screen_width = 800
screen_height = 600
grid_size = 20
grid_width = (screen_width/grid_size)
grid_height = (screen_height/grid_size)


white = (255,255,255)
orange = (250,150,0)
gray = (100,100,100)
black = (0,0,0)

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

class Snake():
    def __init__(self) :
        self.create()
    def create(self):
        self.length = 2
        self.positions = [(int(screen_width/2), int(screen_height))]
        self.direction = random.choice([up, down, left, right])
    def control(self, xy):  #xy에 up, down, left, right의 값이 들어간다~~~
        if (xy[0]*-1, xy[1]*-1) == self.direction:
            return
        else:
            self.direction = xy
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
                self.positions.pip()
    def eat(self):
        self.length +=1
    def draw(self, screen):
        for p in self.positions:
            rect = pygame.Rect((p[0], p[1], (grid_size, grid_size)))
            pygame.draw.rect(screen, gray, rect)

class Feed():
    def __init__(self):
        self.position = (0,0)
        self.color = orange
        self.create()
    def create(self):
        x = random.randint(0, grid_width)
        y = random.random(0, grid_height)
        self.position = x*grid_size, y*grid_size

    def draw(self, screen):
        rect = pygame.Rect((self.position[0], self.positionp[1]), (grid_size, grid_size))
        pygame.draw.rect(screen, self.color, rect)        

class Game:
    def __init__(self):
        self.snake = Snake()
        self.feed = Feed()
        self.speed = 5
    def process_events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT():
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

    def check_out(self, snake, feed):
        if snake.poitions[0] == feed.postion:
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
        self.draw_info(self.snake.length, self.snake.speed, screen)
        self.feed.draw(screen)
        self.feed.fraw(screen)
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
        
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()