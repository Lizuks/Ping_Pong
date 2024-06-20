from pygame import *
from random import randint
from time import time as tm
window = display.set_mode((700, 500))
display.set_caption('Пинг Понг')
backgroud = transform.scale(image.load('fon.jpg'), (700, 500))

clock = time.Clock()
FPS = 60

speed = 10

font.init()
font = font.SysFont('Arial', 45)
lose1 = font.render('YOU LOSE! player 1', True, (255, 0, 0))
lose2 = font.render('YOU LOSE! player 2', True, (255, 0, 0))
class Game_sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(Game_sprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 370:
            self.rect.y += self.speed  
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 370:
            self.rect.y += self.speed   
raketka_1 = Player('raketka.png', 0, 200, 70, 130, 5)
raketka_2 = Player('raketka.png', 630, 0, 70, 130, 5)
speed_x = 3
speed_y = 3
bal = Game_sprite('ball.png', 200, 200, 60, 60, 3)
game = True
finish = False
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(backgroud,(0,0))
        raketka_1.reset()
        raketka_1.update_1()
        raketka_2.reset()
        raketka_2.update_2()
        bal.reset()
        bal.rect.x += speed_x
        bal.rect.y += speed_y
    if bal.rect.y > 440 or bal.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(raketka_1, bal) or sprite.collide_rect(raketka_2, bal):
        speed_x *= -1
    if bal.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if bal.rect.x > 630:
        finish = True
        window.blit(lose2, (200, 200))
    display.update()
    clock.tick(FPS)
