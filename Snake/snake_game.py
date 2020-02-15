from pygame.locals import *
import pygame
from random import randrange
import os

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN = pygame.display.set_mode((800, 600))
x, y = SCREEN.get_size()
clock = pygame.time.Clock()
FPS = 30

cell = 20
body_pos = [[cell*2,0],[cell,0],[0,0]]
snake_pos = [3*cell, 0]
food_pos = [randrange(x/cell-1)*cell, randrange(y/cell-1)*cell]
background = pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__),"img"),"grass.jpeg"))
background = pygame.transform.scale(background,(800,600))


def game_map():
    evenColor = BLACK
    oddColor = WHITE
    for row in range(int(y/cell)):
        cell_y = cell*row
        for col in range(int(x/cell)):
            cell_x = cell*col
            if row % 2 == 0:
                if col % 2 == 0:
                    color = evenColor
                else:
                    color = oddColor
            else:
                if col % 2 == 0:
                    color = oddColor
                else:
                    color = evenColor
            pygame.draw.rect(SCREEN, color, (cell_x, cell_y, cell, cell))


def move(KEY):
    #snake movement
    body_pos.pop()
    body_pos.insert(0,list(snake_pos))
    if KEY[K_LEFT]:
        snake_pos[0] -= cell
    elif KEY[K_RIGHT]:
        snake_pos[0] += cell
    elif KEY[K_UP]:
        snake_pos[1] -= cell
    elif KEY[K_DOWN]:
        snake_pos[1] += cell
    #if the snake out of the screen
    if snake_pos[0]>x-cell:
        snake_pos[0] = 0
    elif snake_pos[0]<0:
        snake_pos[0] = x-cell
    elif snake_pos[1]>y-cell:
        snake_pos[1] = 0
    elif snake_pos[1]<0:
        snake_pos[1] = y-cell
    if snake_pos in body_pos:
        print("Game Over")
        exit()


def draw():
    #game_map()
    SCREEN.blit(background,(0,0))
    pygame.draw.rect(SCREEN, GREEN, (snake_pos[0], snake_pos[1], cell, cell))
    for i in body_pos:
        pygame.draw.rect(SCREEN, BLUE, (i[0], i[1], cell, cell))
    pygame.draw.rect(SCREEN, BLUE, (food_pos[0], food_pos[1], cell, cell))


def game_screen():
    global food_pos
    key = [0 for x in range(323)]
    key[275] = 1
    key = tuple(key)
    pre_key = key
    while True:
        clock.tick(FPS)
        if snake_pos == food_pos:
            body_pos.append(food_pos)
            food_pos = [randrange(x/cell-1)*cell, randrange(y/cell-1)*cell]
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN and 273<=event.key<=276:
                    key = pygame.key.get_pressed()
            if pre_key[K_RIGHT]:
                if not key[K_LEFT]:
                    pre_key = key
            elif pre_key[K_LEFT]:
                if not key[K_RIGHT]:
                    pre_key = key
            elif pre_key[K_UP]:
                if not key[K_DOWN]:
                    pre_key = key
            elif pre_key[K_DOWN]:
                if not key[K_UP]:
                    pre_key = key

            move(pre_key)
            draw()
            pygame.display.update()

    
if __name__ =="__main__":
    game_screen()
