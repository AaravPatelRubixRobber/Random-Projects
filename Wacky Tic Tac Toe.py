#3-PLAYER TIC TAC TOE ON 4X4 BOARD

import pygame
import time
import random


pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Roboto', 30)

black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
dark_green = (0, 155, 0)
dark_green = (0, 200, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)
grey = (100, 100, 100)

screen_x, screen_y = 600, 600
screen = pygame.display.set_mode((screen_x, screen_y), 0, 32)

clock = pygame.time.Clock()

class player:
    def __init__(self, symbol, board):
        self.symbol = symbol
        self.board = board
    def take_turn(self):
        empty, pos = self.board.CLICK_NEW_SQUARE()
        if empty:
            cube = self.board.cubes[pos[1]][pos[0]]
            cube.set_val(self.symbol)

class cube:
    def __init__(self, pos, unit_dim):
        self.val = None
        self.unit_dim = unit_dim
        self.x_unit = pos[0]
        self.y_unit = pos[1]
    def set_val(self, val):
        self.val = val
    def draw(self):
        myfont = pygame.font.SysFont('Roboto', 50)
        textsurface = myfont.render(self.val, False, black)
        text_rect = textsurface.get_rect(center=(int((self.x_unit + 0.5) * self.unit_dim), int((self.y_unit + 0.5) * self.unit_dim)))
        screen.blit(textsurface,text_rect)

class board:
    def __init__(self, units, unit_dim):
        self.rows = units
        self.cols = units
        self.unit_dim = unit_dim
        
        self.cubes = [[cube([i, j], self.unit_dim) for i in range(units)] for j in range(units)]
    def draw(self):

        
        for row in self.cubes:
            for cube in row:
                
                cube.draw()

        for i in range(1, self.cols):
            pygame.draw.line(screen, black, (i*self.unit_dim, 0), (i*self.unit_dim, screen_y))

        #hori line
        for i in range(1, self.rows):
            pygame.draw.line(screen, black, (0, i*self.unit_dim), (screen_x, i*self.unit_dim))

    def CLICK_NEW_SQUARE(self):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            x = mouse_x//self.unit_dim
            y = mouse_y//self.unit_dim

            try:
                if self.cubes[y][x].val == None:
                    return [True, (x, y)]
            except:
                pass
        
        return [False, -1]

class game:
    def __init__(self, players, board, min_seq):
        self.board = board
        self.players = players
        self.current_player = players[0]
        self.current_player_num = 0
        self.min_seq = min_seq
    def update_current_player(self):
        if self.current_player_num + 1 >= len(self.players):
            self.current_player = self.players[0]
            self.current_player_num = 0
        else:
            self.current_player_num += 1
            self.current_player = self.players[self.current_player_num]
    def draw(self):
        myfont = pygame.font.SysFont('Roboto', 20)
        textsurface = myfont.render(self.current_player.symbol + " player", False, black)
        screen.blit(textsurface, (0, 0))
    def CHECK_SEQUENCE(self):
        
        sequence_found = False
        #check hori(-)
        for i in range(self.board.rows):
            for j in range((self.board.cols)-(self.min_seq - 1)):
                val = self.board.cubes[i][j].val
                temp = True
                for k in range(self.min_seq):
                    if val != self.board.cubes[i][j + k].val:
                        temp = False

                if val == None:
                    temp = False
                if temp:
                    sequence_found = True

        #check vert(|)
        for i in range(self.board.cols):
            for j in range((self.board.rows)-(self.min_seq - 1)):
                val = self.board.cubes[j][i].val
                temp = True
                for k in range(self.min_seq):
                    if val != self.board.cubes[j+k][i].val:
                        temp = False

                if val == None:
                    temp = False
                if temp:
                    sequence_found = True

        #check diag (\)
        for i in range((self.board.cols)-(self.min_seq - 1)):
            for j in range((self.board.cols)-(self.min_seq - 1)):
                val = self.board.cubes[i][j].val
                temp = True
                for k in range(self.min_seq):
                    if val != self.board.cubes[i+k][j + k].val:
                        temp = False

                if val == None:
                    temp = False
                if temp:
                    sequence_found = True

        #check diag (/)
        for i in range((self.board.cols - 1), self.board.cols - self.min_seq - 2, -1):
            for j in range((self.board.cols)-(self.min_seq - 1)):
                val = self.board.cubes[i][j].val
                temp = True
                for k in range(0, -self.min_seq, -1):
                    if val != self.board.cubes[i+k][j - k].val:
                        temp = False

                if val == None:
                    temp = False
                if temp:
                    sequence_found = True
                        
        return sequence_found


grid = board(7, 150)

p1 = player('X', grid)
p2 = player('O', grid)
p3 = player('+', grid)

p = [p1, p2, p3]

g = game(p, grid, 3)


run = True

while run:

    screen.fill(white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if g.CHECK_SEQUENCE():
        myfont = pygame.font.SysFont('Roboto', 100)
        textsurface = myfont.render(g.players[g.current_player_num - 1].symbol + " Wins!", False, black)
        text_rect = textsurface.get_rect(center=(screen_x//2, screen_y//2))
        screen.blit(textsurface,text_rect)

        run = False
        
    elif grid.CLICK_NEW_SQUARE()[0]:    
        g.current_player.take_turn()
        g.update_current_player()

        

    grid.draw()
    g.draw()
    
    pygame.display.update()
