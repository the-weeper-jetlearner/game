import pygame
import random
import os

pygame.init()

WIDTH = 1024
HEIGHT = 572
running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game = True

bg = pygame.image.load("poster.png")
bg = pygame.transform.scale(bg,(1024,1000))
red = pygame.image.load("star1.png")
blue = pygame.image.load("star2.png")
stoneframes=[red,blue]
#rarity=[[stone,90], [tree,30]]
ground_y = 0
stones = pygame.sprite.Group()


font_path = pygame.font.match_font("consolas") or pygame.font.match_font("Courier New")
font = pygame.font.Font(font_path, 36)
font_large = pygame.font.Font(font_path, 54)

score = 0
high_score = 0


class block(pygame.sprite.Sprite):
    def __init__(self,x,y,name,health,points,image,rarity):
        self.x = float(x)
        self.y = float(y)
        self.name = name
        self.health = health
        self.points = points
        self,rarity = rarity 

class poorblocks(block):
    def __init__(self,x,y):
        roll = random.randint(1,100)
        







while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(bg, (0, ground_y))

    pygame.display.flip()

pygame.quit()
