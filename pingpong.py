from pygame import *
from random import randint
from time import *




game = True
finish = False
clock = time.Clock()
FPS = 60




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80 :
            self.rect.x += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80 :
            self.rect.x += self.speed



racket1 = Player("racket.png", 5, 200, 4, 50, 150)
racket2 = Player("racket.png", 5, 200, 4, 50, 150)
ball = GameSprite("tenis_ball.png", 200,200,4,50,50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)

