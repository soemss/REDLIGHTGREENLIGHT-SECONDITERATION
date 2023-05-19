import pygame
import time
import sys
import string
import random


playerRun = [
    pygame.transform.scale(pygame.image.load(
        'assets/playerRun/playerRun1.png'), (32, 48)),
    pygame.transform.scale(pygame.image.load(
        'assets/playerRun/playerRun2.png'), (32, 48)),
    pygame.transform.scale(pygame.image.load(
        'assets/playerRun/playerRun3.png'), (32, 48)),
    pygame.transform.scale(pygame.image.load(
        'assets/playerRun/playerRun4.png'), (32, 48))
]

playerIdle = [pygame.transform.scale(
    pygame.image.load('./assets/playerForward.png'), (32, 48))]


class Player():
    def __init__(self):
        self.frame = 0
        self.image = playerIdle[0]
        self.animation = self.image
        self.rect = self.image.get_rect(center=(0, 0))
        self.position = pygame.math.Vector2(0, 0)
        self.speed = 1
        self.shot = False
        self.playerID = lambda: ''.join(random.choices(
            string.ascii_letters + string.digits, k=5)) 

    def get_id(self):
        return self.playerID

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.position[1] -= self.speed
        if keys[pygame.K_a]:
            self.position[0] -= self.speed
        if keys[pygame.K_s]:
            self.position[1] += self.speed
        if keys[pygame.K_d]:
            self.position[0] += self.speed

    def animation(self, display):

        # if self.velocity[0] == 0:
        #     self.animation = playerIdle
        #     self.frame += 0.15
        # if self.velocity[0] != 0:
        #     self.animation = playerRun
        #     self.frame += 0.15
        # if self.frame >= len(self.animation):
        #     self.frame = 0

        # self.image = self.animation[int(self.frame)]

        display.blit(self.image, (self.position[0], self.position[1]))

    def update(self, display):
        self.movement()
        self.animation(display)