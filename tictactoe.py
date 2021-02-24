import pygame
import sys
import numpy

pygame.init()

#SCREEN
screen = pygame.display.set_mode((600, 600))

#COLORS
BG_COLOR = (255, 255, 204)
BLACK = (0, 0, 0)
colorX = (255, 102, 102)
colorO = (224, 224, 224)
bar_width = 15
space_of_X = 55
CANVAS_ROWS = 3
CANVAS_COLS = 3

#TITLE
pygame.display.set_caption('TIC TAC TOE 2.0')
screen.fill(BG_COLOR)
canvas = numpy.zeros((CANVAS_ROWS, CANVAS_COLS))

def drawing_lines():
    pygame.draw.line(screen, BLACK, (0, 200), (600, 200), bar_width)  # horizontal line
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), bar_width)  # horizontal line
    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), bar_width)  # vertical line
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), bar_width)  # vertical line


def drawing_x_o():
    for row in range(CANVAS_ROWS):
        for col in range(CANVAS_COLS):
            if canvas[row][col] == 1:
                pygame.draw.circle(screen, colorO, (int(col * 200 + 100), int(row * 200 + 100)), radius=60, width=15)
            elif canvas[row][col] == 2:
                pygame.draw.line(screen, colorX, (col * 200 + space_of_X, row * 200 + 200 - space_of_X),
                                 (col * 200 + 200 - space_of_X, row * 200 + space_of_X), width=25)
                pygame.draw.line(screen, colorX, (col * 200 + space_of_X, row * 200 + space_of_X),
                                 (col * 200 + 200 - space_of_X, row * 200 + 200 - space_of_X), width=25)


def marking(row, col, Player):
    canvas[row][col] = Player


def empty(row, col):

    if canvas[row][col] == 0:
        return True
    else:
        return False


def canvas_full():

    for row in range(CANVAS_ROWS):
        for col in range(CANVAS_COLS):
            if canvas[row][col] == 0:
                return False

    return True

def win(Player):

    for col in range(CANVAS_COLS):
        if canvas[0][col] == Player and canvas[1][col] == Player and canvas[2][col] == Player:
            vertical_win_line(col, Player)
            return True

    for row in range(CANVAS_ROWS):
        if canvas[0][row] == Player and canvas[1][row] == Player and canvas[2][row] == Player:
            horizontal_win_line(row, Player)
            return True

        if canvas[0][0] == Player and canvas[1][1] == Player and canvas[0][2] == Player:
            left_diagnol_win_line(Player)
            return True

        if canvas[0][0] == Player and canvas[1][0] == Player and canvas[2][2] == Player:
            right_diagonal_win_line(Player)
            return True

        return False


def vertical_win_line(col, Player):  # height = 600 , width = 600
    positionX = col * 200 + 100

    if Player == 1:
        color = colorO
    elif Player == 2:
        color = colorX

    pygame.draw.line(screen, color, (positionX, 15), (positionX, (600 - 15)), 15)  # height


def horizontal_win_line(row, Player):
    positionY = row * 200 + 100

    if Player == 1:
        color = colorO
    elif Player == 2:
        color = colorX

    pygame.draw.line(screen, color, (positionY, 15), (positionY, (600 - 15)), 15)  # width

def left_diagnol_win_line(Player):
    if Player == 1:
        color = colorO
    elif Player == 2:
        color = colorX

    pygame.draw.line(screen, color, (15, (600 - 15)), ((600 - 15), 15), 15)  # width

def right_diagonal_win_line(Player):
    if Player == 1:
        color = colorO
    elif Player == 2:
        color = colorX

    pygame.draw.line(screen, color, (15, 15), ((600 - 15), (600 - 15)), 15)

def restart():
    screen.fill(BG_COLOR)
    drawing_lines()
    Player == 1
    for row in range(CANVAS_ROWS):
        for col in range(CANVAS_COLS):
            canvas[row][col] = 0

drawing_lines()
Player = 1
gameover = False

# Gameplay
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:

            mouseclickX = event.pos[0]
            mouseclickY = event.pos[1]

            click_row = int(mouseclickY // 200)
            click_col = int(mouseclickX // 200)

            if empty(click_row, click_col):
                if Player == 1:
                    marking(click_row, click_col, 1)
                    win(Player)
                    Player = 2
                elif Player == 2:
                    marking(click_row, click_col, 2)
                    win(Player)
                    Player = 1

                drawing_x_o()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()
