#log 002
#AI plays flappy bird
import pygame
import neat
import time
import os
import random

#sets the width of game screen
win_width = 600
#sets the height of game screen
win_height = 800

#tells the program where the bird images are, loads them, and scales them up 2x
bird_imgs = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png")))], [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png")))], [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
#loads the pipe image, and scales it 2x
pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
#loads the bottom background area and scales it 2x
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
#loads the background image and scales it 2x
bg_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

#Creates the class for our bird, , and the timer for animation cycles
class bird:
    #sets it's img = to the value of bird_imgs
    imgs = bird_imgs
    #How uch the image of the bird will tilt when we move
    max_rotation = 25
    #How much we rotate the bird per frame
    rot_vel = 20
    #How long we show each bird animation // affects how fast bird flaps wings in frame
    animation_time = 5

    #sets the start position of our bird
    def __init__(self, x, y):
        #sets the images position on the X axis
        self.x = x
        #sets the images position on the Y axis
        self.y = y
        #How much the image is actually tilted, we start at 0 because we want the bird upright and looking forward
        self.tilt = 0
        #measures time i.e. how many seconds we've been moving forward
        self.tick_count = 0
        #sets the initial velocity of object to 0
        self.vel = 0
        #ADD NOTE WHEN LEARNED
        self.height = self.y
        #contains the # of the currently loaded image
        self.img_count = 0
        #sets a container = to what we put in the array so we can change images
        self.img = self.imgs[0]

    #variable for jump function
    def jump(self):
        #Define the initial velocity 0x0 is top left corner so use -
        self.vel = -10.5
        #Tracks when we last jumped
        self.tick_count = 0
        #Tracks the position before the jump was initiated
        self.height = self.y

    def move(self):
        #how many times we've moved since last jump
        self.tick_count += 1
        #displacement, how many pixels we move up or down per frame
        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        #failsafe to prevent velocity going to far up/down
        if d >= 16:
            d = 16
        #makes the jump a bit smoother going up by adjusting the value
        if d < 0:
            d -= 2
        #adds the result of the displacement to our co-ordinates making us move
        self.y = self.y + d
        #if our displacement is upwards hold the tilt upwards till the tilt at the apex
        if d < 0 or self.y < self.height + 50:
            #if our tilt value is less then max rotation set tilt to max rotation
            if self.tilt < self.max_rotation:
                    self.tilt = self.max_rotation
            else:
            #if our tilt value is greater than -90
                if self.tilt > -90:
                    #we want to tilt all the way down as the bird is freefalling
                    self.tilt -= self.rot_vel

    #Function to change the animations frame
    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.animation_time:
            self.img = self.imgs[0]
        elif self.img_count < self.animation_time*2:
            self.img = self.imgs[1]
        elif self.img_count < self.animation_time*3:
            self.img = self.imgs[2]
        elif self.img_count < self.animation_time*4:
            self.img = self.imgs[1]
        elif self.img_count == self.animation_time*4 + 1:
            self.img = self.imgs[0]
            self.img_count = 0

    #Stopped @8:37 https://www.youtube.com/watch?v=ps55secj7iU&list=PLzMcBGfZo4-lwGZWXz5Qgta_YNX3_vLS2&index=2