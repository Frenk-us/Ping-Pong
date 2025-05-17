from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пинг Понг')
background = transform.scale(image.load('stol.jpg'), (700, 500))

clock = time.Clock()
FPS = 60
game = True
finish = False

font.init()
font1 = font.SysFont(None, 36)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
font2 = font.SysFont(None, 36)
lose2 = font2.render('PLAYER 2 LOSE!', True, (180, 0, 0))

racket_width = 50
racket_height = 100
ball_size = 30

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def draw(self, window):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 5:
            self.rect.y += self.speed
            
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 5:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
        self.speed_x = player_speed
        self.speed_y = player_speed
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.y <= 0 or self.rect.y >= 500 - self.rect.height:
            self.speed_y *= -1
        
        if sprite.collide_rect(self, player1) or sprite.collide_rect(self, player2):
            self.speed_x *= -1

player1 = Player('raketka.png', 30, 200, 4, 50, 50)
player2 = Player('raketka.png', 650, 200, 4, 50, 50)
ball = Ball('ball.png', 350, 250, 3, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        window.blit(background, (0, 0))
        
        player1.update_left()
        player2.update_right()
        ball.update()
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (250, 250))
        elif ball.rect.x > 700:
            finish = True
            window.blit(lose2, (250, 250))
        
        player1.draw(window)
        player2.draw(window)
        ball.draw(window)
    
    display.update()
    clock.tick(FPS)
