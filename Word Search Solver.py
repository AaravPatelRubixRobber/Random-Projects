#WORD SEARCH SOLVER

rows = int(input('how many rows are there? '))
colms = int(input('how many colms are there? '))
w_count = int(input('how many words are there? '))

#makes 2d grid var
print('put the board in below')
grid = []
for row in range(rows):
    grid.append(input().strip().lower().split())

#makes 1d words var
print('put the words you want to find below')
words = []
for j in range(w_count):
    words.append(input().strip().lower())
        
#solve will make the working combo capitalized
def solve(g, w):#g means grid. w means word to look for

    #checks if the word works horizontally
    for i in range(len(g)):
        for j in range(len(g[0])-(len(w) - 1)):
            c_w = ''
            for k in range(len(w)):
                c_w += g[i][j + k]
            if w.lower() == c_w.lower():
                for k in range(len(w)):
                    g[i][j + k] =  g[i][j+k].upper()
                return
            c_w = ''
            for k in range(len(w)):
                c_w += g[i][(j + len(w) - 1) - k]#make sure no index error
            if w.lower() == c_w.lower():
                for k in range(len(w)):
                    g[i][j + k] =  g[i][j+k].upper()
                return

    #checks if the word works vertically
    for i in range(len(g[0])):
        for j in range(len(g)-(len(w) - 1)):
            c_w = ''
            for k in range(len(w)):
                c_w += g[j + k][i]
            if w.lower() == c_w.lower():
                for k in range(len(w)):
                    g[j + k][i] =  g[j+k][i].upper()
                return
            c_w = ''
            for k in range(len(w)):
                c_w += g[(j + len(w) - 1) - k][i]#make sure no index error
            if w.lower() == c_w.lower():
                for k in range(len(w)):
                    g[(j + len(w) - 1) - k][i] =  g[(j + len(w) - 1) - k][i].upper()
                return

    #checks if the word works (\) diagonally
    for i in range(len(g) - (len(w) - 1)):
        for j in range(len(g) - (len(w) - 1)):
            c_w = ''
            for k in range(len(w)):
                c_w += g[i + k][j + k]
            if w.lower() == c_w.lower():
                for k in range(len(w)):
                    g[i + k][j + k] =  g[i +k][j+k].upper()
                return
            c_w = ''
            for k in range(len(w)):
                c_w += g[i - k + (len(w) - 1)][j - k + (len(w) - 1)]
            if w.lower() == c_w.lower():
                for k in range(len(w)):
                    g[i - k + (len(w) - 1)][j - k + (len(w) - 1)] =  g[i -k + (len(w) - 1)][j-k + (len(w) - 1)].upper()
                return

    #checks if the word works (/) diagonally
    '''iii = [p for p in range(len(g) - (len(w) - 1))]
    iii.reverse()'''
    for i in range(len(g) - 1, len(g) - 1 - len(w) - 1, -1):#may cause error
        for j in range(len(g) - (len(w) - 1)):#may cause error
            c_w = ''
            for k in range(0, -len(w), -1):
                c_w += g[i + k][j - k]
            if w.lower() == c_w.lower():
                for k in range(0, -len(w), -1):
                    g[i + k][j - k] =  g[i +k][j-k].upper()
                return
            c_w = ''
            for k in range(0, -len(w), -1):
                c_w += g[i - k - (len(w) - 1)][j + k + (len(w) - 1)]
            if w.lower() == c_w.lower():
                for k in range(0, -len(w), -1):
                    g[i - k - (len(w) - 1)][j + k + (len(w) - 1)] =  g[i -k - (len(w) - 1)][j+k + (len(w) - 1)].upper()
                return

    #forwards
    pass
    #backwards
    pass

#main body
for wo in range(w_count):
    solve(grid, words[wo])

import pygame
import random

pygame.init()

black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)
gray = (100, 100, 100)

screen_x, screen_y = 600, 600
screen = pygame.display.set_mode((screen_x, screen_y), 0, 32)

go = True
myfont = pygame.font.SysFont('Arial', 25)
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
    screen.fill(white)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            textsurface = myfont.render(grid[i][j], False, black if grid[i][j].islower() else (random.randint(0, 225),random.randint(0, 225) ,random.randint(0, 225)))
            screen.blit(textsurface,(round(screen_x/colms)* j, round(screen_y/rows)* i))
    pygame.display.update()
            
'''#returns the modified grid
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[i][j], end = ' ')
    print('')'''
