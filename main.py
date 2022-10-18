import pygame
import copy
from pygame.locals import *
from random import randrange
from piece import Piece


pygame.init()

FPS  = 30
green = (  0, 255,   0)
blue =  (  0,   0, 128)
red =   (255,  20,  20)
black = (  0,   0,   0)
white = (255, 255, 255)
Nx = 10
Ny = 20
squaresize = 30
MarginX = 20
MarginBot = 20
MarginTop = 50
gridwidth = 1

W,H = Nx*squaresize+2*MarginX+200, Ny*squaresize+MarginBot+MarginTop

clock = pygame.time.Clock()

def create_preview_grid(piece):
    nextpiece = copy.deepcopy(piece)
    if nextpiece.shape == 0:
        nextpiece.move(-2)
        nextpiece.fall(3)
    elif nextpiece.shape in [1,2,3,4]:
        nextpiece.move(-1)
        nextpiece.fall(4)
    elif nextpiece.shape == 5:
        nextpiece.move(-2)
        nextpiece.fall(2)
    elif nextpiece.shape == 6:
        nextpiece.move(-1)
        nextpiece.fall(3)
        
    [(x1,y1),(x2,y2),(x3,y3),(x4,y4)] = nextpiece.pos
    grid = []
    for x in range(Nx):
        column = []
        for y in range(Ny):
            if x == x1 and y == y1:
                column.append(nextpiece.color)
            elif x == x2 and y == y2:
                column.append(nextpiece.color)
            elif x == x3 and y == y3:
                column.append(nextpiece.color)
            elif x == x4 and y == y4:
                column.append(nextpiece.color)                                            
            else:
                column.append(black)
        grid.append(column)
    return grid
    
def create_grid():
    grid = []
    for x in range(Nx):
        column = []
        for y in range(Ny):
            column.append(black)
        grid.append(column)
    return grid
    
def draw_grid(screen, grid):
    screen.fill( white )
    for x in range(Nx):
        for y in range(Ny):     
            pygame.draw.rect(screen, grid[x][y], pygame.Rect(MarginX+x*squaresize+gridwidth, MarginTop+y*squaresize, squaresize-gridwidth, squaresize-gridwidth) )   

def draw_next_piece(screen, next_piece_grid):
    offsetx = Nx*squaresize+30
    for x in range(6):
        for y in range(6):  
            pygame.draw.rect(screen, next_piece_grid[x][y], pygame.Rect(offsetx+MarginX+x*squaresize+gridwidth, MarginTop+y*squaresize, squaresize-gridwidth, squaresize-gridwidth) )   
    
def draw_level(screen, level):
    textlvl = "Level %s" %(level)
    font = pygame.font.SysFont(None, 50)
    text = font.render(textlvl, True, black, (255,255,255))
    textRect = text.get_rect()
    textRect.center = Nx*squaresize+30+30*3, 350
    screen.blit(text, textRect)

def update_grid(grid, current_piece, base):
    x1,y1 = current_piece.pos[0]
    x2,y2 = current_piece.pos[1]
    x3,y3 = current_piece.pos[2]
    x4,y4 = current_piece.pos[3]
    if x1 in range(Nx) and y1 in range(Ny): grid[x1][y1] = current_piece.color
    if x2 in range(Nx) and y2 in range(Ny): grid[x2][y2] = current_piece.color
    if x3 in range(Nx) and y3 in range(Ny): grid[x3][y3] = current_piece.color
    if x4 in range(Nx) and y4 in range(Ny): grid[x4][y4] = current_piece.color
    for x in range(Nx):
        for y in range(Ny):
            if base[x][y] != black:
                grid[x][y] = base[x][y]
    return grid

def draw_piece():
    piece = Piece(randrange(7))
    return piece
    
def has_contact(piece, base):
    # Check if it touches the base
    for x in range(Nx):
        for y in range(Ny):
            for (xpos,ypos) in piece.pos:
                if base[x][y] != black:
                    if xpos==x and ypos==y:
                        return True
                if ypos >= Ny:
                    return True
    # Check if it touches boundaries
    for (xpos,ypos) in piece.pos:
        if xpos < 0:
            return True
        elif xpos > (Nx-1):
            return True 
    return False
    
def place_piece(base, piece):
    for (x,y) in piece.pos:
        base[x][y] = piece.color
    return base
    
def delete_full_lines(grid):
    # First detect which lines to remove
    lines_to_delete = []
    for y in reversed(range(Ny)):
        delete_line = True
        for x in range(Nx):
            if grid[x][y] == black:
                delete_line = False 
        if delete_line:
            lines_to_delete.append(y)
    # Now remove line
    for x in range(Nx):
        for y in lines_to_delete:
            grid[x].pop(y)
            
    # Now move everything down
    for i in range(len(lines_to_delete)):
        for x in range(Nx):
            grid[x].insert(0, black)        
    return grid, len(lines_to_delete)
    
def game_over(grid):
    for x in range(Nx):
        if grid[x][0] != black:
            return True
    return False 

################################################################################
################################################################################
################################################################################

def main():
    level = 1
    Nlines_tot = 0
    Nlines_next_lvl = 10
    fallspeed = 3
    
    # Definieren und Oeffnen eines neuen Fensters
    pygame.display.set_caption("Tetris")

    screen = pygame.display.set_mode((W, H))

    current_piece = draw_piece()
    next_piece = draw_piece()
    
    base = create_grid()


    # Start game loop
    running = True
    counter = pygame.time.get_ticks()
    while running:
        if Nlines_tot >= Nlines_next_lvl:
            Nlines_next_lvl += 10
            level += 1
            fallspeed += 0.5
        
        grid = create_grid()
        grid = update_grid(grid, current_piece, base)
        draw_grid(screen, grid)
        next_piece_grid = create_preview_grid(next_piece)
        draw_next_piece(screen, next_piece_grid)
        draw_level(screen, level)
        pygame.display.update()
        
        # Keyboard inputs
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    current_piece.move(-1)
                    if has_contact(current_piece, base):
                        current_piece.undo_move()
                elif event.key == K_RIGHT:
                    current_piece.move(1)
                    if has_contact(current_piece, base):
                        current_piece.undo_move()
                elif event.key == K_DOWN:
                    current_piece.fall()
                    if has_contact(current_piece, base):
                        current_piece.undo_move()
                        base = place_piece(base, current_piece)
                        base, Nlines = delete_full_lines(base)
                        Nlines_tot += Nlines
                        current_piece = next_piece
                        next_piece = draw_piece()
                        if game_over(base):
                            running = False
                elif event.key == K_UP:
                    current_piece.rotate()
                    
        # This controlles how fast pieces fall
        if pygame.time.get_ticks() > counter:
            counter += 1000/fallspeed
            current_piece.fall()
            if has_contact(current_piece, base):
                current_piece.undo_move()
                base = place_piece(base, current_piece)
                base, Nlines = delete_full_lines(base)
                Nlines_tot += Nlines
                current_piece = next_piece
                next_piece = draw_piece()
                if game_over(base):
                    running = False
            
        # Control the FPS
        clock.tick(FPS)

if __name__ == "__main__":
    main()
