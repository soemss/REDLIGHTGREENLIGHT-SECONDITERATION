import pygame
import time
import sys
from pygame.locals import *
from scripts.player import Player
import datetime

# constants
pygame.font.init()
font = pygame.font.SysFont('Arial', 25)
fps = 60

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1000


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('RED LIGHT GREEN LIGHT')
        self.clock = pygame.time.Clock()
        self.win = False
        self.dead = False
        self.start = pygame.time.get_ticks()
        self.mainloop = True
        self.player = Player()
        self.countdown = 15
        self.elapsed = 0

    def update(self):
        pygame.display.flip()
        self.clock.tick(fps)

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def draw(self):
        self.display.fill('black')

    def timer(self):
        """Depending on the level, the time decreases on the harder levels"""

        self.elapsed = (pygame.time.get_ticks() - self.start) / 1000
        # print(self.elapsed)
        remaining_time = max(self.countdown - self.elapsed, 0)

        if remaining_time <= 10:
            text = font.render(
                f"Time: {int(remaining_time)}", True, (255, 0, 0))
            text_rect = text.get_rect(
                midtop=(SCREEN_WIDTH // 2, 10))
            self.display.blit(text, text_rect)
            if remaining_time <= 0:
                self.mainloop = False

        text = font.render(
            f"Time: {int(remaining_time)}", True, (255, 255, 255))
        text_rect = text.get_rect(
            midtop=(SCREEN_WIDTH // 2, 10))
        self.display.blit(text, text_rect)

    def running(self):
        while self.mainloop:
            self.update()
            self.checkEvents()
            self.draw()
            self.timer()
            if not self.player.shot:
                self.player.update(self.display)


if __name__ == '__main__':
    game = Game()
    game.running()
