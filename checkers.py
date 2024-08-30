#THIS IS A BASIC CHECKERS GAME AND GUI

import pygame
import time
import random


pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Roboto', 30)

black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
dark_green = (0, 200, 0)
red = (255, 0, 0)
dark_red = (155, 0, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)
grey = (100, 100, 100)
beige = (200, 180, 150)

screen_x, screen_y = 560, 560
screen = pygame.display.set_mode((screen_x, screen_y), 0, 32)

#clock = pygame.time.Clock()

class player:
    def __init__(self, board, start_pieces, player_num, direction):
        self.board = board
        self.start_pieces = start_pieces
        self.player_num = player_num
        self.dir = direction

        for piece in self.start_pieces:
            
            self.board.cubes[piece[0]][piece[1]].set_val(self.player_num)
            
    def take_turn(self):
        own_square, pos = self.CLICK_OWN_SQUARE()
        if own_square:
            print("own square clicked")
            moved_to_square, new_pos = self.CLICK_MOVE_TO_SQUARE(pos)
            while True:
                if moved_to_square:

                    self.move_piece(pos, new_pos)
                    break

    def move_piece(self, start, end):
        cube = self.board.cubes[end[1]][end[0]]
        cube.set_val(self.player_num)
        old_cube = self.board.cubes[start[1]][start[0]]
        old_cube.set_val(None)

    def capture(self, start, pos_map):

        print(start)

        print(pos_map)
        
        if len(pos_map) == 0:
            return
        else:
            self.board.cubes[start[1]][start[0]].set_val(None)

            mid_y = int(start[1] + (pos_map[0][1] - start[1])/2)
            mid_x = int(start[0] + (pos_map[0][0] - start[0])/2)

            cube = self.board.cubes[mid_y][mid_x]
            cube.set_val(None)
            self.board.cubes[pos_map[0][1]][pos_map[0][0]].set_val(self.player_num)
            return self.capture(pos_map[0], pos_map[1:])

    def CLICK_OWN_SQUARE(self):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            

            x = mouse_x//self.board.unit_dim
            y = mouse_y//self.board.unit_dim

            try:
                #print(self.board.cubes[y][x].val, '-', self.player_num)
                if self.board.cubes[y][x].val == self.player_num:
                    return [True, (x, y)]
            except:
                pass
        
        return [False, -1]

    def CLICK_MOVE_TO_SQUARE(self, clicked_pos):
        if True:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            x = mouse_x//self.board.unit_dim
            y = mouse_y//self.board.unit_dim


            c_x = clicked_pos[0]
            c_y = clicked_pos[1]

            if True:
                for pos in self.get_new_squares(clicked_pos):#get both possible squares for the peice#[[c_y - self.dir[1], c_x + 1], [c_y - self.dir[1], c_x - 1]]
                    
                    #pygame.draw.circle(screen, blue, (int((pos[1]+0.5)*self.board.unit_dim), int((pos[0]+0.5)*self.board.unit_dim)), 20)
                    if pos[0] >= self.board.rows or pos[0] < 0 or pos[1] >= self.board.cols or pos[1] < 0:
                        #print('out')
                        pass
                    elif pos[0] == y and pos[1] == x:
                        desired_location = pos[:]
                        if self.board.cubes[desired_location[0]][desired_location[1]].val == None:
                            return [True, (desired_location[1], desired_location[0]), []]
                        break
            if True:
                for pos in self.get_capture_squares(clicked_pos):#return 2nd var that gives order for double jump
                    if pos[0] == y and pos[1] == x:
                        desired_location = pos[:]
                        return [True, (desired_location[1], desired_location[0]), [[desired_location[1], desired_location[0]]]]#################################################change to allow for double     jump



#change to allow double jump


            
            #if self.dir[1] == 0:
            ''''if self.dir[1] == 0:
                print('wrong dir')'''

        
        return [False, -1, []]
    def get_new_squares(self, pos):#gives in y, x format
        if self.dir[0] == 0:
            return [[pos[1] - self.dir[1], pos[0] + 1], [pos[1] - self.dir[1], pos[0] - 1]]
        elif self.dir[1] == 0:
            return [[pos[1] -1, pos[0] - self.dir[0]], [pos[1] +1, pos[0] -self.dir[0]]]
        else:
            print('there was a dir error')
            raise Exception

    def get_capture_squares(self, pos):#returns in y, x format

        ret = []
        
        if self.dir[0] == 0:

            #print('pos: ', pos)
            #print('jumped over square right: ', [pos[1] - self.dir[1]][ pos[0] + 1])
            #print('right landing jumped over square: ', [pos[1] - 2*self.dir[1], pos[0] + 2])
            try:
                if self.board.cubes[pos[1] - self.dir[1]][pos[0] + 1].val != None and self.board.cubes[pos[1] - self.dir[1]][pos[0] + 1].val != self.player_num:# and self.board.cubes[pos[1] - 2*self.dir[1]][ pos[0] + 2] == None:
                    ret.append([pos[1] - 2*self.dir[1], pos[0] + 2])
            except:
                pass
            try:
                if self.board.cubes[pos[1] - self.dir[1]][pos[0] - 1].val != None and self.board.cubes[pos[1] - self.dir[1]][pos[0] - 1].val != self.player_num:# and self.board.cubes[pos[1] - 2*self.dir[1]][ pos[0] - 2] == None:
                    ret.append([pos[1] - 2*self.dir[1], pos[0] - 2])
            except:
                pass


            #for square in  [[pos[1] - self.dir[1], pos[0] + 1], [pos[1] - self.dir[1], pos[0] - 1]]:
            '''if self.board.cubes[square[0]][square[1]] != None and self.board.cubes[square[0]][square[1]] != self.player_num:
                    ret.append([])'''
        elif self.dir[1] == 0:
            #return [[pos[1] -1, pos[0] - self.dir[0]], [pos[1] +1, pos[0] -self.dir[0]]]
            if self.board.cubes[pos[1] -1][pos[0] - self.dir[0]] != None and self.board.cubes[pos[1] -1][pos[0] - self.dir[0]] != self.player_num and self.board.cubes[pos[1] -2][ pos[0] - 2*self.dir[0]] == None:
                ret.append([pos[1] -2, pos[0] - 2*self.dir[0]])
            if self.board.cubes[pos[1] +1][pos[0] - self.dir[0]] != None and self.board.cubes[pos[1] +1][pos[0] - self.dir[0]] != self.player_num and self.board.cubes[pos[1] +2][ pos[0] - 2*self.dir[0]] == None:
                ret.append([pos[1] +2 , pos[0] - 2*self.dir[0]])
        else:
            print('there was a dir error')
            raise Exception

        return ret


    def draw_possible_moves(self, clicked_pos):
        for pos in self.get_new_squares(clicked_pos):
            pygame.draw.circle(screen, blue, (int((pos[1]+0.5)*self.board.unit_dim), int((pos[0]+0.5)*self.board.unit_dim)), 20)
        for pos in self.get_capture_squares(clicked_pos):
            pygame.draw.circle(screen, blue, (int((pos[1]+0.5)*self.board.unit_dim), int((pos[0]+0.5)*self.board.unit_dim)), 20)
        



                    
        '''if self.board.cubes[c_y + self.dir[1]][c_x - 1].val == None or self.board.cubes[c_y + self.dir[1]][c_x + 1].val == None:
                        return
                elif self.dir[1] == 0:
                    if self.board.cubes[c_y + 1][c_x + self.dir[0]].val == None or self.board.cubes[c_y - 1][c_x + self.dir[0]].val == None:
                        return
                if self.board.cubes[y][x].val == self.val:
                    return [True, (x, y)]
            except:
                pass
        
        return [False, -1]'''
    
class cube:
    def __init__(self, pos, unit_dim):
        self.val = None
        self.king = False
        self.unit_dim = unit_dim
        self.x_unit = pos[0]
        self.y_unit = pos[1]
    def set_val(self, val):
        self.val = val
    def draw(self):
        if self.val == 1:
            pygame.draw.circle(screen, red, (int((self.x_unit + 0.5)*self.unit_dim), int((self.y_unit + 0.5)*self.unit_dim)), int(3/8*self.unit_dim))
            if self.king:
                pygame.draw.rect(screen, dark_red, (int((self.x_unit + 0.3)*self.unit_dim), int((self.y_unit + 0.3)*self.unit_dim), 0.4*self.unit_dim, 0.4*self.unit_dim))
        if self.val == 2:
            pygame.draw.circle(screen, white, (int((self.x_unit + 0.5)*self.unit_dim), int((self.y_unit + 0.5)*self.unit_dim)), int(3/8*self.unit_dim))
            

class board:
    def __init__(self, units, unit_dim):
        self.rows = units
        self.cols = units
        self.unit_dim = unit_dim
        
        self.cubes = [[cube([i, j], self.unit_dim) for i in range(units)] for j in range(units)]
    def draw(self):

        for i in range(1, self.cols):
            pygame.draw.line(screen, black, (i*self.unit_dim, 0), (i*self.unit_dim, screen_y))

        #hori line
        for i in range(1, self.rows):
            pygame.draw.line(screen, black, (0, i*self.unit_dim), (screen_x, i*self.unit_dim))

        for i in range(1, self.rows, 2):
            for j in range(0, self.cols, 2):
                pygame.draw.rect(screen, black, (self.unit_dim*i, self.unit_dim*j,self.unit_dim, self.unit_dim))
                #pygame.draw.rect(screen, dark_green, (pos[0]*self.game.unit_dim, pos[1]*self.game.unit_dim, self.game.unit_dim, self.game.unit_dim))

        for i in range(0, self.rows, 2):
            for j in range(1, self.cols, 2):
                
                pygame.draw.rect(screen, black, (self.unit_dim*i, self.unit_dim*j,self.unit_dim, self.unit_dim))

    def draw_cubes(self):
        for row in self.cubes:
            for cube in row:
                
                cube.draw()

class game:
    def __init__(self, players):
        self.phase = None
        self.players = players
        self.player_turn_num = 0
        self.player_turn = players[0]
    def change_phase(self, new_phase):
        self.phase = new_phase
    def next_player(self):
        self.player_turn_num += 1
        if self.player_turn_num >= len(self.players):
            self.player_turn_num = 0

        self.player_turn = self.players[self.player_turn_num]
    




gameBoard = board(8, 70)
p1 = player(gameBoard, [[7, 0], [7, 2], [7, 4], [7, 6],
                        [6, 1], [6, 3], [6, 5], [6, 7],
                        [5, 0], [5, 2], [5, 4], [5, 6]], 1, [0, 1])

p2 = player(gameBoard, [[0, 1], [0, 3], [0, 5], [0, 7],
                        [1, 0], [1, 2], [1, 4], [1, 6],
                        [2, 1], [2, 3], [2, 5], [2, 7]], 2, [0, -1])

g = game([p1, p2])

g.change_phase('select piece')

run = True

while run:

    screen.fill(beige)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    gameBoard.draw()

    if g.phase == 'select piece':
        p1_square, pos = g.player_turn.CLICK_OWN_SQUARE()
        if p1_square:
            print("own square clicked")
            g.change_phase('move piece')#chagnge phase to click move to square phase

    elif g.phase == 'move piece':
        g.player_turn.draw_possible_moves(pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            moved_to_square, new_pos, pieces_captured_pos = g.player_turn.CLICK_MOVE_TO_SQUARE(pos)
        #print(moved_to_square, new_pos)
            if moved_to_square:
                #new_pos = (4, 4)
                if len(pieces_captured_pos) <= 0:
                    g.player_turn.move_piece(pos, new_pos)
                    g.change_phase('select piece')
                    g.next_player()
                else:
                    g.player_turn.capture(pos, pieces_captured_pos)
                    g.change_phase('select piece')
                    g.next_player()
            else:
                g.change_phase('select piece')

    gameBoard.draw_cubes()

    pygame.display.update()
    
