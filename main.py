import pygame
pygame.init()
pygame.display.init()

SCREENWIDTH = 600
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))



class Player():
    def __init__(self,x,y,speedx,speedy):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy

    def update(self):
        self.x += self.speedx
        self.y += self.speedy

class Projectile():
    def __init__(self,x,y,speedx, speedy):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy

    def update(self):
        self.x += self.speedx
        self.y += self.speedy

        
class Enemy():
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        if player.x < self.x:
            self.x -= self.speed
        if player.x > self.x:
            self.x += self.speed
        if player.y < self.y:
            self.y -= self.speed
        if player.y > self.y:
            self.y += self.speed
        
PLAYERSPEED = 5
player = Player(300,300, 0, 0)

projectiles = []

enemies = []

clock = pygame.time.Clock()

player_prevButton = "a"

while True:
    screen.fill("black")
    player_rect = pygame.Rect(player.x, player.y ,50, 50)

    pygame.draw.rect(screen, (100,0,0), player_rect)
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.speedx = -PLAYERSPEED
            player_prevButton = "a"
        elif keys[pygame.K_d]:
            player.speedx = PLAYERSPEED
            player_prevButton = "d"
        else:
            player.speedx = 0

        if keys[pygame.K_w]:
            player.speedy = -PLAYERSPEED
            player_prevButton = "w"
        elif keys[pygame.K_s]:
            player.speedy = PLAYERSPEED
            player_prevButton = "s"
        else:
            player.speedy = 0

        if keys[pygame.K_e]:
            enemies.append(Enemy(0,0,3))

        if keys[pygame.K_SPACE]:
            speedx = 0
            speedy = 0
            if player_prevButton == "a":
                speedx = -7
            elif player_prevButton == "d":
                speedx = 7
            elif player_prevButton == "w":
                speedy = -7
            elif player_prevButton == "s":
                speedy = 7

            projectiles.append(Projectile(player.x,player.y, speedx, speedy))

    for projectile in projectiles:
        projectile_rect = pygame.Rect(projectile.x, projectile.y, 10, 10)
        pygame.draw.rect(screen, (0,100,0), projectile_rect)
        projectile.update()

        if projectile.x < 0 or projectile.x > SCREENWIDTH or projectile.y < 0 or projectile.y > SCREENHEIGHT:
            projectiles.remove(projectile)

    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy.x,enemy.y, 25,25)
        pygame.draw.rect(screen, (0,0,100), enemy_rect)
        enemy.update()

    player.update()
    print(player_prevButton)


    pygame.display.flip()
    clock.tick(30)