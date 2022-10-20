import pygame
import sys
import time
from framework import *
from board import *
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
screen.fill((200, 200, 200))
myfont = 'AdobeArabic-BoldItalic.otf'


class CLS_framwork(object):
    def __init__(self):
        self.board = CLS_board()
        self.mx, self.my = 10, 10
        self.f = 0
        self.pos = 0
        self.e = 0

    def draw(self, scr):
        self.board.draw(scr)
        if self.e >= 3:
            pygame.draw.rect(screen, (255, 255, 255), (100, 230, 380, 80), 0)
            font = pygame.font.Font(myfont, 100)
            img = font.render('Game Over', True, (50, 80, 100))
            screen.blit(img, (110, 215))
            font = pygame.font.Font(myfont, 45)
            img = font.render('Press SPACE to continue', True, (215, 80, 100))
            screen.blit(img, (120, 315))
            self.f = 4
        if self.f == 0:
            pygame.draw.rect(screen, (250, 140, 190), (65, 247, 456, 86), 0)
            pygame.draw.rect(screen, (100, 200, 200), (68, 250, 453, 83), 0)
            pygame.draw.rect(screen, (255, 255, 255), (68, 250, 450, 80), 0)
            font = pygame.font.Font(myfont, 45)
            img = font.render('Press SPACE to start the game',
                              True, (200, 80, 100))
            screen.blit(img, (80, 245))
            img = font.render('Press Enter to choose level',
                              True, (50, 80, 100))
            screen.blit(img, (95, 285))
        if self.win() == True and self.f == 3:
            pygame.draw.rect(screen, (255, 255, 255), (145, 230, 280, 80), 0)
            font = pygame.font.Font(myfont, 100)
            img = font.render('you win', True, (50, 80, 100))
            screen.blit(img, (160, 215))
            img = font.render('you win', True, (215, 80, 100))
            screen.blit(img, (162, 217))
            img = font.render('you win', True, (255, 255, 255))
            screen.blit(img, (161, 216))
            font = pygame.font.Font(myfont, 45)
            img = font.render('Press SPACE to continue', True, (215, 80, 100))
            screen.blit(img, (110, 320))
        if self.f == 2:
            font = pygame.font.Font(myfont, 45)
            pygame.draw.rect(screen, (255, 255, 255), (200, 165, 190, 50), 0)
            img = font.render('Press 1:Easy', True, (200, 80, 100))
            screen.blit(img, (207, 165))
            pygame.draw.rect(screen, (255, 255, 255), (180, 245, 230, 50), 0)
            img = font.render('Press 2:Midium', True, (50, 80, 100))
            screen.blit(img, (190, 245))
            pygame.draw.rect(screen, (255, 255, 255), (200, 325, 190, 50), 0)
            img = font.render('Press 3:Hard', True, (50, 150, 150))
            screen.blit(img, (207, 325))
        pygame.draw.rect(screen, (200, 200, 200), (50, 550, 100, 50), 0)
        font = pygame.font.Font(myfont, 45)
        img = font.render(str(self.e)+'/3', True, (200, 80, 100))
        screen.blit(img, (50, 540))
        pygame.draw.rect(screen, (200, 200, 200), (150, 550, 100, 50), 0)

    def start(self):
        self.board.daluan()

    def mousedown(self, pos, b):
        print(self.e)
        self.pos = pos
        mx, my = pos[0], pos[1]
        self.mx, self.my = (mx-65)//50, (my-65)//50
        if 50 <= pos[0] <= 130 and 10 <= pos[1] <= 50:
            self.f = 0
            self.board.boardList = [[[5, 0], [8, 0], [6, 0], [2, 0], [3, 0], [1, 0], [4, 0], [7, 0], [9, 0]],
                                    [[4, 0], [3, 0], [7, 0], [8, 0], [9, 0],
                                        [5, 0], [1, 0], [6, 0], [2, 0]],
                                    [[9, 0], [1, 0], [2, 0], [4, 0], [6, 0],
                                        [7, 0], [5, 0], [3, 0], [8, 0]],
                                    [[6, 0], [2, 0], [9, 0], [1, 0], [7, 0],
                                     [8, 0], [3, 0], [4, 0], [5, 0]],
                                    [[1, 0], [5, 0], [8, 0], [9, 0], [4, 0],
                                     [3, 0], [7, 0], [2, 0], [6, 0]],
                                    [[3, 0], [7, 0], [4, 0], [6, 0], [5, 0],
                                     [2, 0], [8, 0], [9, 0], [1, 0]],
                                    [[8, 0], [6, 0], [5, 0], [7, 0], [2, 0],
                                     [4, 0], [9, 0], [1, 0], [3, 0]],
                                    [[2, 0], [4, 0], [3, 0], [5, 0], [1, 0],
                                     [9, 0], [6, 0], [8, 0], [7, 0]],
                                    [[7, 0], [9, 0], [1, 0], [3, 0], [8, 0], [6, 0], [2, 0], [5, 0], [4, 0]]]
            self.board.answerList = [[5, 8, 6, 2, 3, 1, 4, 7, 9],
                                     [4, 3, 7, 8, 9, 5, 1, 6, 2],
                                     [9, 1, 2, 4, 6, 7, 5, 3, 8],
                                     [6, 2, 9, 1, 7, 8, 3, 4, 5],
                                     [1, 5, 8, 9, 4, 3, 7, 2, 6],
                                     [3, 7, 4, 6, 5, 2, 8, 9, 1],
                                     [8, 6, 5, 7, 2, 4, 9, 1, 3],
                                     [2, 4, 3, 5, 1, 9, 6, 8, 7],
                                     [7, 9, 1, 3, 8, 6, 2, 5, 4]]
        return

    def keydown(self, key):
        if key == 13 and self.f == 0:
            self.f = 2
        if key == pygame.K_SPACE and self.f == 0:
            self.start()
            self.f = 1
        if key == pygame.K_SPACE and self.f == 3:
            self.f = 0
        if pygame.K_1 <= key <= pygame.K_9:
            if self.mx != 10 and self.my != 10:
                if self.board.boardList[self.my][self.mx][1] != 0 and self.f == 1:
                    if self.board.boardList[self.my][self.mx][0] == key-48:
                        self.board.boardList[self.my][self.mx][0] = ' '
                    else:
                        self.board.boardList[self.my][self.mx][0] = key-48
                    if self.board.boardList[self.my][self.mx][0] != self.board.answerList[self.my][self.mx] and self.board.boardList[self.my][self.mx][0] != ' ':
                        self.e += 1
        if pygame.K_1 <= key <= pygame.K_3 and self.f == 2:
            if key == pygame.K_1:
                self.board.n = 1
                self.f = 0
            if key == pygame.K_2:
                self.board.n = 2
                self.f = 0
            if key == pygame.K_3:
                self.board.n = 3
                self.f = 0
        if self.f == 4 and key == pygame.K_SPACE:
            print('hi')
            self.e = 0
            self.f = 0
            self.board.boardList = [[[5, 0], [8, 0], [6, 0], [2, 0], [3, 0], [1, 0], [4, 0], [7, 0], [9, 0]],
                                    [[4, 0], [3, 0], [7, 0], [8, 0], [9, 0],
                                        [5, 0], [1, 0], [6, 0], [2, 0]],
                                    [[9, 0], [1, 0], [2, 0], [4, 0], [6, 0],
                                        [7, 0], [5, 0], [3, 0], [8, 0]],
                                    [[6, 0], [2, 0], [9, 0], [1, 0], [7, 0],
                                     [8, 0], [3, 0], [4, 0], [5, 0]],
                                    [[1, 0], [5, 0], [8, 0], [9, 0], [4, 0],
                                     [3, 0], [7, 0], [2, 0], [6, 0]],
                                    [[3, 0], [7, 0], [4, 0], [6, 0], [5, 0],
                                     [2, 0], [8, 0], [9, 0], [1, 0]],
                                    [[8, 0], [6, 0], [5, 0], [7, 0], [2, 0],
                                     [4, 0], [9, 0], [1, 0], [3, 0]],
                                    [[2, 0], [4, 0], [3, 0], [5, 0], [1, 0],
                                     [9, 0], [6, 0], [8, 0], [7, 0]],
                                    [[7, 0], [9, 0], [1, 0], [3, 0], [8, 0], [6, 0], [2, 0], [5, 0], [4, 0]]]
            self.board.answerList = [[5, 8, 6, 2, 3, 1, 4, 7, 9],
                                     [4, 3, 7, 8, 9, 5, 1, 6, 2],
                                     [9, 1, 2, 4, 6, 7, 5, 3, 8],
                                     [6, 2, 9, 1, 7, 8, 3, 4, 5],
                                     [1, 5, 8, 9, 4, 3, 7, 2, 6],
                                     [3, 7, 4, 6, 5, 2, 8, 9, 1],
                                     [8, 6, 5, 7, 2, 4, 9, 1, 3],
                                     [2, 4, 3, 5, 1, 9, 6, 8, 7],
                                     [7, 9, 1, 3, 8, 6, 2, 5, 4]]

    def win(self):
        for y in range(9):
            for x in range(9):
                if self.board.boardList[y][x][0] == ' ':
                    return False
                elif self.board.boardList[y][x][0] != self.board.answerList[y][x]:
                    return False
        if self.f == 1:
            self.f = 3
        return True
