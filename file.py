#This program shows the simulation of 8 balls bouncing under gravitational acceleration.
#It is also accompanied by eleastic collission with walls of the container.
#It is fun to watch.
import pygame
import time
import random

pygame.init()

#setting screen size of pygame window to 1000 by 800 pixels
screen=pygame.display.set_mode((1000,800))
background=pygame.image.load('background-img.png')

#Adding title
pygame.display.set_caption('Bouncing Ball Simulation')

class ball:
    ball_image=pygame.image.load('ball.png')
    g=1
    def __init__(self):
        self.velocityX=6
        self.velocityY=6
        self.X=random.randint(0,968)
        self.Y=random.randint(0,550)

    def render_ball(self):
        screen.blit(ball.ball_image, (self.X,self.Y))
    def move_ball(self):
        #changing y component of velocity due to downward acceleration
        self.velocityY+=ball.g

        #changing position based on velocity
        self.X+=self.velocityX
        self.Y+=self.velocityY

        #collission with the walls lead to change in velocity
        if self.X<0 or self.X>968:
            self.velocityX*=-1

        if self.Y<0 and self.velocityY<0:
            self.velocityY*=-1
            self.Y=0

        if self.Y>768 and self.velocityY>0:
            self.velocityY*=-1
            self.Y=768

#list of balls created as objects
Ball_List=[ball(),ball(), ball(), ball(), ball(), ball(), ball(), ball()]

#The main program loop
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    time.sleep(0.02)
    screen.blit(background, (0,0))
    for ball_item in Ball_List:
        ball_item.render_ball()
        ball_item.move_ball()
    pygame.display.update()