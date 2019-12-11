import pygame
import os
from random import getrandbits
randtah = bool(getrandbits(1))
if randtah == True:
    turn ="kruzko"
elif randtah == False:
    turn ="xko"
run = True
Black = (0,0,0)
A1 = 0
A2 = 0
A3 = 0
B1 = 0
B2 = 0
B3 = 0
C1 = 0
C2 = 0
C3 = 0
vyhralx = False
vyhralO = False

def drawWindow():
    if vyhralO == False or vyhralx == False:
        win.fill((255,255,255))
        pygame.draw.rect(win,Black,(156,0,15,520))
        pygame.draw.rect(win, Black, (326, 0, 15, 520))
        pygame.draw.rect(win, Black, (0, 156, 500, 15))
        pygame.draw.rect(win, Black, (0, 326, 500, 15))
        pygame.draw.rect(win, Black, (0, 495, 500, 25))
        krizik()
        koliesko()
    winScreen()
    pygame.display.update()

def krizik():
    if A1 == 1:#
        pygame.draw.line(win, Black, (10, 10), (145, 145), 6)
        pygame.draw.line(win, Black, (10, 145), (145, 10), 6)
    if A2 == 1:#
        pygame.draw.line(win, Black, (180, 10), (315, 145), 6)
        pygame.draw.line(win, Black, (180, 145), (315, 10), 6)
    if A3 == 1:#
        pygame.draw.line(win, Black, (350, 10), (485, 145), 6)
        pygame.draw.line(win, Black, (350, 145), (485, 10), 6)
    if B1 == 1:#
        pygame.draw.line(win, Black, (10, 180), (145, 315), 6)
        pygame.draw.line(win, Black, (10, 315), (145, 180), 6)
    if B2 == 1:#
        pygame.draw.line(win, Black, (180, 180), (315, 315), 6)
        pygame.draw.line(win, Black, (180, 315), (315, 180), 6)
    if B3 == 1:
        pygame.draw.line(win, Black, (350, 180), (485, 315), 6)
        pygame.draw.line(win, Black, (350, 315), (485, 180), 6)
    if C1 == 1:#
        pygame.draw.line(win, Black, (10, 350), (145, 485), 6)
        pygame.draw.line(win, Black, (10, 485), (145, 350), 6)
    if C2 == 1:
        pygame.draw.line(win, Black, (180, 350), (315, 485), 6)
        pygame.draw.line(win, Black, (180, 485), (315, 350), 6)
    if C3 == 1:
        pygame.draw.line(win, Black, (350, 350), (485, 485), 6)
        pygame.draw.line(win, Black, (350, 485), (485, 350), 6)

def koliesko():
    if A1 == 2:
        pygame.draw.circle(win,Black,(77,77),67,6)
    if A2 == 2:
        pygame.draw.circle(win,Black,(247,77),67,6)
    if A3 == 2:
        pygame.draw.circle(win,Black,(417,77),67,6)
    if B1 == 2:
        pygame.draw.circle(win,Black,(77,247),67,6)
    if B2 == 2:
        pygame.draw.circle(win,Black,(247,247),67,6)
    if B3 == 2:
        pygame.draw.circle(win,Black,(417,247),67,6)
    if C1 == 2:
        pygame.draw.circle(win,Black,(77,417),67,6)
    if C2 == 2:
        pygame.draw.circle(win,Black,(247,417),67,6)
    if C3 == 2:
        pygame.draw.circle(win,Black,(417,417),67,6)

def winScreen():
    if vyhralx == True:
        pygame.draw.rect(win,Black,(0,0,500,520))
        font = pygame.font.SysFont('arial',80)
        text = font.render(('X Vyhral'),True,(255,255,255))
        win.blit(text,(90,190))
    if vyhralO == True:
        pygame.draw.rect(win, Black, (0, 0, 500, 520))
        font = pygame.font.SysFont('arial', 80)
        text = font.render(('O Vyhral'), True, (255, 255, 255))
        win.blit(text, (90, 190))
pygame.init()
win = pygame.display.set_mode((500,520))
pygame.display.set_caption("Piskvorky")

while run:
    pygame.time.delay(16)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        A1 = 0
        A2 = 0
        A3 = 0
        B1 = 0
        B2 = 0
        B3 = 0
        C1 = 0
        C2 = 0
        C3 = 0
    mousex, mousey = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == 1:
        if vyhralO == True or vyhralx == False:
            if 0 <= mousex <= 155 and 0 <= mousey <= 155:
                if turn == 'xko' and A1 ==0:
                    A1=1
                    turn='kruzko'
                elif turn == 'kruzko' and A1 == 0:
                    A1=2
                    turn = 'xko'
            if 170 <= mousex <= 340 and 0 <= mousey <= 155:
                if turn == 'xko' and A2 == 0:
                    A2 = 1
                    turn = 'kruzko'
                elif turn == 'kruzko' and A2 == 0:
                    A2 = 2
                    turn = 'xko'
            if 355 <= mousex <= 500 and 0 <= mousey <= 155:
                if turn == 'xko' and A3 == 0:
                    A3 = 1
                    turn = 'kruzko'
                elif turn == 'kruzko' and A3 == 0:
                    A3 = 2
                    turn = 'xko'
            if 0 <= mousex <= 155 and 170 <= mousey <= 340:
                if turn == 'xko' and B1 == 0:
                    B1 = 1
                    turn = 'kruzko'
                elif turn == 'kruzko' and B1 == 0:
                    B1 = 2
                    turn = 'xko'
            if 170 <= mousex <= 340 and 170 <= mousey <= 340:
                if turn == 'xko' and B2 == 0:
                    B2 = 1
                    turn = 'kruzko'
                elif turn == 'kruzko' and B2 == 0:
                    B2 = 2
                    turn = 'xko'
            if 355 <= mousex <= 500 and 170 <= mousey <= 340:
                if turn == 'xko' and B3 == 0:
                    B3 = 1
                    turn = 'kruzko'
                elif turn == 'kruzko' and B3 == 0:
                    B3 = 2
                    turn = 'xko'
            if 0 <= mousex <= 155 and 355 <= mousey <= 500:
                if turn == 'xko' and C1 == 0:
                    C1 = 1
                    turn = 'kruzko'
                elif turn == 'kruzko' and C1 == 0:
                    C1 = 2
                    turn = 'xko'
            if 170 <= mousex <= 340 and 355 <= mousey <= 500:
                if turn == 'xko' and C2 == 0:
                    C2 = 1
                    turn = 'kruzko'
                elif turn == 'kruzko' and C2 == 0:
                    C2 = 2
                    turn = 'xko'
            if 355 <= mousex <= 500 and 355 <= mousey <= 500:
                if turn == 'xko' and C3 == 0:
                    C3 = 1
                    turn = 'kruzko'
                elif turn == 'kruzko' and C3 == 0:
                    C3 = 2
                    turn = 'xko'
        if A1 == 1 and A2 == 1 and A3 == 1 and vyhralx == False and vyhralO == False:
            vyhralx = True
        if B1 == 1 and B2 == 1 and B3 == 1 and vyhralx == False and vyhralO == False:
            vyhralx = True
        if C1 == 1 and C2 == 1 and C3 == 1 and vyhralx == False and vyhralO == False:
            vyhralx = True
        if A1 == 1 and B1 == 1 and C1 == 1 and vyhralx == False and vyhralO == False:
            vyhralx = True
        if A2 == 1 and B2 == 1 and C2 == 1 and vyhralx == False and vyhralO == False:
            vyhralx = True
        if A3 == 1 and B3 == 1 and C3 == 1 and vyhralx == False and vyhralO == False:
            vyhralx = True
        if A1 == 1 and B2 == 1 and C3 == 1 and vyhralx == False and vyhralO == False:
            vyhralx = True
        if C1 == 1 and B2 == 1 and A3 == 1 and vyhralx == False and vyhralO == False:
            vyhralx = True
        #
        if A1 == 2 and A2 == 2 and A3 == 2 and vyhralx == False and vyhralO == False:
            vyhralO = True
        if B1 == 2 and B2 == 2 and B3 == 2 and vyhralx == False and vyhralO == False:
            vyhralO = True
        if C1 == 2 and C2 == 2 and C3 == 2 and vyhralx == False and vyhralO == False:
            vyhralO = True
        if A1 == 2 and B1 == 2 and C1 == 2 and vyhralx == False and vyhralO == False:
            vyhralO = True
        if A2 == 2 and B2 == 2 and C2 == 2 and vyhralx == False and vyhralO == False:
            vyhralO = True
        if A3 == 2 and B3 == 2 and C3 == 2 and vyhralx == False and vyhralO == False:
            vyhralO = True
        if A1 == 2 and B2 == 2 and C3 == 2 and vyhralx == False and vyhralO == False:
            vyhralO = True
        if C1 == 2 and B2 == 2 and A3 == 2 and vyhralx == False and vyhralO == False:
            vyhralO = True
    winScreen()
    drawWindow()