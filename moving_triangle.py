#! /usr/bin/python3
#
# lines.py - Screensaver like animation
# 

# TODO:

import pygame
import sys
import random

screen_size_x = 960
screen_size_y = 540
background_color = (0, 0, 0)
lines_drawn = 1
coolors = [(249,65,68),(243,114,44),(248,150,30),(249,132,74),(249,199,79),(144,190,109),(67,170,139),(77,144,142),(87,117,144),(39,125,161)]
ci1 = 0
ci2 = len(coolors) // 2
ci3 = len(coolors)-1

line_one_x1 = random.random()*screen_size_x
line_one_y1 = random.random()*screen_size_y
line_one_x2 = random.random()*screen_size_x
line_one_y2 = random.random()*screen_size_y
line_two_x1 = random.random()*screen_size_x
line_two_y1 = random.random()*screen_size_y

line_one_velocityx1 = 3-random.random()*6
line_one_velocityy1 = 3-random.random()*6
line_one_velocityx2 = 3-random.random()*6
line_one_velocityy2 = 3-random.random()*6
line_two_velocityx1 = 3-random.random()*6
line_two_velocityy1 = 3-random.random()*6

pygame.init()
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
s = pygame.Surface((screen_size_x, screen_size_y), pygame.SRCALPHA)
screen.fill(background_color)

clock = pygame.time.Clock()

frames = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    line_one_x1  += line_one_velocityx1
    line_one_y1  += line_one_velocityy1
    line_one_x2  += line_one_velocityx2
    line_one_y2  += line_one_velocityy2
    line_two_x1  += line_two_velocityx1
    line_two_y1  += line_two_velocityy1



    if (line_one_x1<0 or line_one_x1>screen_size_x):
        line_one_velocityx1 *= -1
    if (line_one_y1<0 or line_one_y1>screen_size_y):
        line_one_velocityy1 *= -1
    if (line_one_x2<0 or line_one_x2>screen_size_x):
        line_one_velocityx2 *= -1
    if (line_one_y2<0 or line_one_y2>screen_size_y):
        line_one_velocityy2 *= -1
    if (line_two_x1<0 or line_two_x1>screen_size_x):
        line_two_velocityx1 *= -1
    if (line_two_y1<0 or line_two_y1>screen_size_y):
        line_two_velocityy1 *= -1
    
    pygame.display.set_caption("Code in place 2021 - Moving triangle")
    s.fill((0,0,0,1))
    screen.blit(s, (0,0))
    if lines_drawn % 250 == 0:
        ci1 += 1
        ci2 += 1
        ci3 += 1
        if ci1 == len(coolors):
            ci1 = 0
        if ci2 == len(coolors):
            ci2 = 0
        if ci3 == len(coolors):
            ci3 = 0

    pygame.draw.line(screen, coolors[ci1], (line_one_x1, line_one_y1), (line_one_x2, line_one_y2), 1)
    pygame.draw.line(screen, coolors[ci2], (line_one_x2, line_one_y2), (line_two_x1, line_two_y1), 1)
    pygame.draw.line(screen, coolors[ci3], (line_two_x1, line_two_y1), (line_one_x1, line_one_y1), 1)
    lines_drawn += 1

    pygame.display.update()
    ms = clock.tick(frames)