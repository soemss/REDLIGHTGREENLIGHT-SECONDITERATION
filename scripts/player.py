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

playerIdle = [pygame.transform.scale(pygame.image.load('./assets/playerIdle/playerIdle1.png'), (32, 48)),
              pygame.transform.scale(pygame.image.load('./assets/playerIdle/playerIdle2.png'), (32, 48))]

playerKeys = {
    0: [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d],
    1: [pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l],
    2: [pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT],
    }

class Player():
    def __init__(self):
        self.frame = 0
        self.a = playerIdle[0]
        self.name = f"Player {random.randint(1, 100)}"
        self.image = self.a
        self.playerAnimation = self.image
        self.rect = self.image.get_rect(center=(0, 0))
        self.velocity = pygame.math.Vector2(360, 800)
        self.speed = 1
        self.shot = False
        self.id = random.randint(10000, 99999)
        self.score = 0

    def get_id(self):
        return self.id

    def get_score(self):
        return self.score

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity[1] -= self.speed
        if keys[pygame.K_a]:
            self.velocity[0] -= self.speed
        if keys[pygame.K_s]:
            self.velocity[1] += self.speed
        if keys[pygame.K_d]:
            self.velocity[0] += self.speed
        if keys[pygame.K_c]:
            self.shot = True

    def animation(self, display):

        if self.velocity[0] == 0:
            self.playerAnimation = playerIdle
            self.frame += 0.15
        if self.velocity[0] != 0:
            self.playerAnimation = playerRun
            self.frame += 0.15
        if self.frame >= len(self.playerAnimation):
            self.frame = 0

        self.image = self.playerAnimation[int(self.frame)]

        display.blit(self.image, (self.velocity[0], self.velocity[1]))

    def update(self, display):
        self.movement()
        self.animation(display)
