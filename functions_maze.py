import numpy as np
import math
from matplotlib import pyplot as plt

### Create matrix with the index number of each cell
def matrix_index_create(L_height, L_width):
    M_array = np.full((L_height, L_width), 0)
    p = 1
    for y in reversed(range(0, L_height)):
        for x in range(0, L_width):
            M_array[y,x] = p
            p = p + 1
    return M_array

### Create array with the vertex of the maze (excluding external ones)
def matrix_vertex_create(M_array, L_height, L_width):
    M_grid = []
    c = 0
    for y in range(0, L_height):
        for x in range(0, L_width):
            if x < L_width-1:
                M_grid.insert(c,[M_array[y,x],M_array[y,x+1]])
                c = c+1
            if y > 0:
                M_grid.insert(c,[M_array[y,x],M_array[y-1,x]])
            c = c+1
    return M_grid

### This function return an array of two umber indicated the index numbers of the row and column for a given number in M_array matrix
def matrix_index(index, width,height):
    row = height - math.ceil(index/width)
    row_aux = math.ceil(index/width)-1
    col = index-row_aux*width-1
    return [row, col]

### This function finds the neighbours (not taking into account the diagonals ones) of a given cell that have not been visited in the maze matrix
def det_neigh(M_maze, cell, width,height, M_v):
    M_neig_current = []
    t=0
    for s in range(0,len(M_maze)):
        if(M_maze[s][0] == cell):
            pos_aux = matrix_index(M_maze[s][1], width,height)
            if M_v[pos_aux[0]][pos_aux[1]] == 0:
                M_neig_current.insert(t, M_maze[s][1])
                t= t+1
        if(M_maze[s][1] == cell):
            pos_aux = matrix_index(M_maze[s][0], width,height)
            if M_v[pos_aux[0]][pos_aux[1]] == 0:
                M_neig_current.insert(t, M_maze[s][0])
                t= t+1
    return M_neig_current

### This function remove in the maze matrix of vertices a specific vertex that is in between cell_current and cell_previous
def remove_vertix(M_grid_maze, cell_current, cell_previous):
    M_grid_maze_aux = M_grid_maze.copy()
    for s in range(0,len(M_grid_maze_aux)):
        if ((M_grid_maze_aux[s][0]==cell_previous) and (M_grid_maze_aux[s][1]== cell_current)):
            M_grid_maze_aux.remove([cell_previous, cell_current])
            break
        if ((M_grid_maze_aux[s][1]==cell_previous) and (M_grid_maze_aux[s][0]== cell_current)):
            M_grid_maze_aux.remove([cell_current, cell_previous])
            break
    return M_grid_maze_aux

### This funtion represent the maze matrix
def rep_maze(M_grid, L_width, L_height, rect_width, rect_height):
    fig = plt.figure()
    for s in range(0,len(M_grid)):
        y_level1 = math.ceil(M_grid[s][0]/L_width)
        y_level2 = math.ceil(M_grid[s][1]/L_width)
        if y_level1==y_level2:
            x_point = math.ceil((M_grid[s][0])%L_width)*rect_width
            y_points = [(y_level1-1)*rect_height, y_level1*rect_height]
            plt.plot([x_point, x_point], y_points, color='k')
        else:
            y_point = min([y_level1, y_level2])*rect_height
            x_point = min(M_grid[s])%L_width
            if x_point == 0:
                x_point = L_width
            plt.plot([(x_point-1)*rect_width, x_point*rect_width], [y_point, y_point], color='k')

    plt.plot([0, L_width*rect_width], [0, 0], color='k')
    plt.plot([L_width*rect_width, L_width*rect_width], [0, L_height*rect_height], color='k')
    plt.plot([L_width*rect_width, 0], [L_height*rect_height, L_height*rect_height], color='k')
    plt.plot([0, 0], [L_height*rect_height, 0], color='k')
    plt.show()

