import pygame
import math
import random

window_width = 900
window_height = 600

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True
dt = ground_cycle = 0
player_frames = [pygame.image.load("./run1.png").convert(), pygame.image.load("./run2.png").convert()]
ground_image = pygame.image.load("./ground.png").convert()
cactus_image = pygame.image.load("./cactus.png").convert()
ground_speed = 10
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()
jump_height = 200

def parabola(x):
    return (-x ** 2) + jump_height
def remap(val, in_min, in_max, out_min, out_max):
    return out_min + (val - in_min) * (out_max - out_min) / (in_max - in_min)

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cactus_image
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.state = False
        self.image = player_frames[self.state]
        self.rect = self.image.get_rect()
        self.rect.centery = window_height - int(self.rect.height / 2) - 6
        self.rect.centerx += 50
        self.cycle_count = 0
        self.jumping = False
        self.default_y = self.rect.centery
        self.last_parabola = 999
    
    def cycle(self):
        if self.jumping:
            para = parabola(self.cycle_count - math.sqrt(jump_height))
            self.rect.centery = self.default_y - int(para)
            self.cycle_count += 1
            if self.last_parabola > 0 and para < 0:
                self.jumping = False
                self.rect.centery = self.default_y
            self.last_parabola = para
        else:
            self.cycle_count += 1
            if self.cycle_count >= 10:
                self.state = not self.state
                self.image = player_frames[self.state]
                self.cycle_count = 0

    def jump(self):
        if self.jumping:
            return
        self.cycle_count = 0
        self.jumping = True



player = Player()
sprites = pygame.sprite.Group()
sprites.add(player)
cacti = []

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    #render
    screen.fill("white")
    screen.blit(ground_image, (ground_cycle, window_height - ground_height))
    screen.blit(ground_image, (ground_width + ground_cycle, window_height - ground_height))
    if ground_cycle <= -ground_width:
        screen.blit(ground_image, (ground_width + ground_cycle, 0))
        ground_cycle = 0
    sprites.draw(screen)

    #logic
    ground_cycle -= ground_speed
    for i in range(0, len(cacti)):
        if player.rect.colliderect(cacti[i].rect):
            pygame.quit()

        cacti[i].rect.centerx -= ground_speed

    player.cycle()
    if random.randint(1, 100) == 50:
        cactus = Cactus()
        cactus.rect.centerx = window_width
        cactus.rect.centery = window_height - int(cactus_image.get_height() / 2)
        cacti.append(cactus)
        sprites.add(cactus)




    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.jump()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
