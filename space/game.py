import pygame
import random
import math
score=0
pygame.init()

#color
white=(255,255,255)
#screen
screenwidth=800
screenheight=600
screen=pygame.display.set_mode((screenwidth,screenheight))
w1=screenwidth/2
h1=screenheight/2
#title
pygame.display.set_caption("SPACE INVADERS")
#icon
icon=pygame.image.load("player.png")
pygame.display.set_icon(icon)
#player
playerx=400
playery=500
playerxchange=0
playerychange=0
playerimage=pygame.image.load("player right.png")
#background
background=pygame.image.load("background.gif")
#enemy
enemyx=random.randint(0,710)
enemyy=random.randint(0,50)
enemyxchange=1
enemyychange=40
enemyimage=pygame.image.load("enemy.png")
#bullet
bulletx=0
bullety=500
bulletxchange=0
bulletychange=3                                    
bulletimage=pygame.image.load("bulletplayer.gif")
bulletstate="ready"
def firebullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimage,(x+50,y))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((math.pow(enemyx-bulletx,2)) + (math.pow(enemyy-bullety,2)))
    if distance < 27:
        return True
    else:
        return False
#game loop
running=True
while running:
    screen.blit(background,(0,0))
    screen.blit(playerimage,(playerx,playery))
    screen.blit(enemyimage,(enemyx,enemyy))
    #font
    myfont=pygame.font.SysFont("times-new-roman",30)
    font=myfont.render(f"SCORE: {score}",10,(255,255,255))
    screen.blit(font,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerxchange=-2
            if event.key==pygame.K_RIGHT:
                playerxchange=2
            if event.key==pygame.K_SPACE:
                if bulletstate is "ready":
                    bulletx=playerx
                    firebullet(bulletx,bullety)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or  event.key==pygame.K_RIGHT:
                playerxchange=0
    #collision
    collision=iscollision(enemyx,enemyy,bulletx,bullety)
    if collision:
        bullety=500
        bulletstate="ready"
        enemyx=random.randint(0,710)
        enemyy=random.randint(0,50)
        score+=1
    #bullet
    if bullety <=0:
        bullety=500
        bulletstate="ready"
    if bulletstate is "fire":
        firebullet(bulletx,bullety)
        bullety-=bulletychange
    #enemy
    if enemyx <= 0:
        enemyxchange=+1
        enemyy+=enemyychange
    elif enemyx >= 710:
        enemyxchange=-1
        enemyy+=enemyychange
    enemyx+=enemyxchange
    '''
    if screenheight > playery:
        myfont=pygame.font.SysFont("times-new-roman",30)
        font=myfont.render(f"GAME OVER!!!",10,(255,255,255))
        screen.blit(font,(w1,h1))
    '''
    #player
    playerx+=playerxchange
    if playerx <= 0:
        playerx=0
    elif playerx >= 710:
        playerx=710


   
    
    pygame.display.update()
pygame.quit()




































