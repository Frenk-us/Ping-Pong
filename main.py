from pygame import *
 
window = display.set_mode((700, 500))
display.set_caption('Пинг Понг')
background = transform.scale(image.load('stol.jpg'), (700, 500))

clock = time.Clock()
FPS = 60
game = True
finish = False
num_fire = 0
rel_time = False 
font.init()
font1 = font.SysFont(None, 36)
width = 80
height = 50 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def draw(self, window):
        window.blit(self.image, self.rect)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < 700 - 65:
            self.rect.x += self.speed
    def update_1(self):
        if keys_pressed[K_UP] and self.rect.y < 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -50


























while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                ship.fire()
       
    if not finish:
        window.blit(background,(0,0))

        ship.update()
        ship.draw(window)

        enemies.update()
        enemies.draw(window)

        asteroids.update()
        asteroids.draw(window)

        bullets.update()
        bullets.draw(window) 

     
        collides = sprite.groupcollide(enemies, bullets, True, True)
        
        for c in collides:
            killed_enemies += 1
            enemy = Enemy('ufo.png', randint(0, 700 - width), -50, randint(1, 4))
            enemies.add(enemy)

       
        if sprite.spritecollide(ship, enemies, False):
            finish = True
        
        if sprite.spritecollide(ship, asteroids, False):
            finish = True

        
        if missed_enemies > 5:
            finish = True

        text_missed = font1.render("Пропущено: " + str(missed_enemies), 1, (255, 255, 255))
        window.blit(text_missed, (10, 10))

        text_killed = font1.render("Расфигачено: " + str(killed_enemies), 1, (255, 255, 255))
        window.blit(text_killed, (10, 50))
    else:
        text_lose = font1.render('ТЫ ПРОИГРАЛ!', True, (255, 255, 255))
        window.blit(text_lose, (250, 200))

    display.update()
    clock.tick(FPS)