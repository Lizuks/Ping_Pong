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
win = font.render('YOU WIN!', True, (255, 0, 0))
lose = font.render('YOU LOSE!', True, (255, 0, 0))
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
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed   
    def fire(self):
        bullet = Carrot('carrot.png', self.rect.centerx, self.rect.top, 60, 70, -15)
        carrots.add(bullet)
game = True
finish = False
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(backgroud,(0,0))
        
    display.update()
    clock.tick(FPS)