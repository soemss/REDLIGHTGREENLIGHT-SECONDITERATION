import pygame
import time
import sys
import string
import random

pygame.mixer.init()
chulsooState = [
    pygame.transform.scale(pygame.image.load(
        'assets/chulsoo/chulsoo1.png'), (50, 68)),
    pygame.transform.scale(pygame.image.load(
        'assets/chulsoo/chulsoo2.png'), (50, 68)),
]
seconds3 = pygame.mixer.music.load('assets/audio/jingleS3.wav')
seconds4 = pygame.mixer.music.load('assets/audio/jingleS4.wav')
seconds5 = pygame.mixer.music.load('assets/audio/jingleS5.wav')

class Chulsoo:  # Imma do you
    def __init__(self):
        self.dollActive = False
        self.randomTime = random.randrange(3, 6)
        self.timeLimit = 0

    def update(self, seconds, display):
        self.randomTime = random.randrange(3, 6)
        if seconds >= self.timeLimit and not self.dollActive:
            display.blit(chulsooState[0], (360, 20))
        elif seconds >= self.timeLimit and self.dollActive:
            display.blit(chulsooState[1], (360, 20))
            if self.randomTime == 5:
                pygame.mixer.music.play(seconds5)
            elif self.randomTime == 4:
                pygame.mixer.music.play(seconds4)
            else:
                pygame.mixer.music.play(seconds3)

