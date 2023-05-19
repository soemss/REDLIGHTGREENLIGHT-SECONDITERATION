import pygame
import time
import sys
from pygame.locals import *
from scripts.player import Player
from scripts.robot import Chulsoo
import datetime

# constants
pygame.font.init()
font = pygame.font.SysFont('Arial', 25)
fps = 60

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1000

backgroundColor = (228, 216, 159)
titleColor = (255, 255, 255)


titleWidth = 400
titleHeight = 200

titleSurface = pygame.Surface((titleWidth, titleHeight))
titleSurface.fill((255, 255, 255))
titleSurface.set_alpha(0)

titleFont = pygame.font.Font(None, 64)

titleText = titleFont.render("SUI GAMING", True, titleColor)

title_rect = titleText.get_rect()
title_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
titleX = (SCREEN_WIDTH - titleWidth) // 2
titleY = (SCREEN_HEIGHT - titleHeight) // 2
title_speed = 0.5


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('RUBY ILLUMINATION PEA ILLUMINATION')
        self.clock = pygame.time.Clock()
        self.win = False
        self.dead = False
        self.startTicks = pygame.time.get_ticks()
        self.gameTick = 0
        self.mainloop = True
        self.player = Player()
        self.countdown = 18  # add three seconds :)
        self.elapsed = 0
        self.startGame = False
        self.robot = Chulsoo()

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

        self.elapsed = (pygame.time.get_ticks() - self.startTicks) / 1000
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

    def runTitleScreen(self):

        titleAlpha = 0
        titleX = (SCREEN_WIDTH - titleWidth) // 2
        titleY = (SCREEN_HEIGHT - titleHeight) // 2
        while titleAlpha < 2000:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            titleAlpha += 3
            titleText.set_alpha(titleAlpha)

            self.display.fill(backgroundColor)
            titleX += title_speed

            if titleX > SCREEN_WIDTH:
                titleX = -title_rect.width

            self.display.blit(titleText, (titleX, titleY))

            pygame.display.flip()

        pygame.time.wait(2000)
        self.startGame = True

        titleText.set_alpha(0)

    def running(self):
        self.runTitleScreen()
        if self.startGame:
            while self.mainloop:
                seconds = (pygame.time.get_ticks() - self.startTicks) / 1000
                self.update()
                self.checkEvents()
                self.draw()
                self.timer()
                self.robot.update(seconds, self.display)
                self.player.update(self.display)


if __name__ == '__main__':
    game = Game()
    game.running()
