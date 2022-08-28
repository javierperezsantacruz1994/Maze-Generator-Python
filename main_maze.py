import random
from functions_maze import *

### Author: Javier Pérez Santacruz
### Freely use this code for your use
### Project description: the objective of this code consist of randomly creating a rectangle 
### maze with L_width number of columns and L_heigh number of rows of the corresponding maze matrix
### Used maze algorithm: Recursive Backtracking
### Source: http://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking

#####################################
########## Main parameters ##########
#####################################
L_width = 10                     # Number of columns of the maze matrix
L_height = 10                    # Number of rows of the maze matrix
rect_height,rect_width = 1, 1    # Height and width of the rectangles that represent each cell of the maze matrix (for representation)

### Maze matrixes creation
M_array = matrix_index_create(L_height, L_width)          # Create matrix with the index number of each cell
M_grid = matrix_vertex_create(M_array, L_height, L_width) # Create array with the vertex of the maze (excluding external ones) (main matrix -> maze matrix)
                                                          # A vertex is defined between the indexes of two cell that are neighbours (excluding the diagonal neighbours)
M_visit = np.full((L_height, L_width), 0)                 # Create visited matrix cells. 0 indicates that the cell has not been visited meanwhile 1 means the opposite
cell_init = random.randint(1, L_width*L_height)           # Select a random inital cell in the maze
#cell_init = 1

### Initialization of the parameters of the main loop
cell_current = cell_init                                  # Index of the current cell
cel_previous = cell_current                               # Index of the previous visited cell
M_grid_maze = M_grid.copy()                               # Create a copy of the vertex array that define the maze
exit = False                                              # Boolean that define to exit the main maze loop
N_neig_vi = sum(sum(M_visit))                             # Calculate the number of visited cells (no strictly necessary for the maze realization)
n = 0                                                     # Counter of the number of visited cells
cell_visited_vector = []                                  # Create the vector that determines the visited cells
cell_visited_vector.insert(n, cell_init)                  # Insert the current cell to the visited cells vector
n_step_back = 0                                           # Counter to move back in the visited cells vector in case that the current cell does not have not-visited cells

### Determine that the current cell has been visited
pos_init = matrix_index(cell_current , L_width, L_height) # Get the matrix indexes of the cell_current index
M_visit[pos_init[0], pos_init[1]] = 1                     # Specify that the current_cell is visited in the M_visit matrix

###################################################
##### Main maze loop: Recursive Backtracking ######
###################################################
while exit==False:
    N_neig_vi = sum(sum(M_visit))                                                     # Calculate the number of visited cells inside the loop (no strictly necessary)
    M_neig_current = det_neigh(M_grid_maze, cell_current, L_width, L_height, M_visit) # Determine neighbours indexes that have not been visited of the current cell
    if(len(M_neig_current)>0):                                                   # If there neighbours that have not been visited
        ### Selec next random step
        ran_walk_index = random.randint(0, len(M_neig_current)-1)                # Randomly choose one of the not visited neighbour cells
        cel_previous = cell_current                                              # Update cell_previous
        cell_current = M_neig_current[ran_walk_index]                            # Update cell_current
        n = n + 1                                                                # Increase counter of visited cells
        n_step_back = 0                                                          # Counter to move back in the visited cells vector in case that 
        cell_visited_vector.insert(n, cell_current)                              # Update vector of visited cells
        pos_current = matrix_index(cell_current , L_width, L_height)
        M_visit[pos_current[0], pos_current[1]] = 1                              # Update matrix of visited cells
        M_grid_maze = remove_vertix(M_grid_maze, cell_current, cel_previous)     # Remove vertix between cell_current and cell_previous
    else:                                                                        # If all the neighbours of the current cell have been visited
        n_step_back = n_step_back + 1                                            # Increase the counter to move back in the visited cells vector
        cell_current = cell_visited_vector[len(cell_visited_vector)-n_step_back] # The current cell is the previous cell visited using the cell visited vector

    if(cell_current == cell_init):            # The loop ends when the current cell is equal to the inital cell
    #if(cell_current == (L_width*L_height)):
        exit = True
        
### Represent full maze
rep_maze(M_grid_maze, L_width, L_height, rect_width, rect_height)
