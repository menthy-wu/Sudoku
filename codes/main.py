import pygame
import sys
import time
from framework import *

SCREEN_W, SCREEN_H = 600, 600  # 屏幕大小
framwork = CLS_framwork()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            framwork.keydown(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            framwork.mousedown(event.pos, event.button)
    framwork.draw(screen)
    pygame.display.update()
