import pygame

screen = pygame.display.set_mode((600,600))



class Player():
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

player = Player(300,300, 10)
player_rect = player.get_rect()

while True:
    screen.fill("black")