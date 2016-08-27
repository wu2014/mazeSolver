"""
File: mazeSolver.py

Implement backtracking algorithms using a stack and two-dimensional
array (Grid class).
"""
from stack import ArrayStack
from grid import Grid
import copy


def get_maze():
    file_name = raw_input('Please enter the maze file name as ****.txt:    ')

    maze_file = open(file_name, 'r')

    num_row = int(maze_file.readline()) # get number of row
    num_col = int(maze_file.readline()) # get number of column

    maze = Grid(num_row, num_col, "*")

    starting_pt = (0, 0)
    target_pt = (0, 0)

    for row_num in xrange(num_row): # change previous maze to the maze in the file
        row = maze_file.readline()
        for col_num in xrange(num_col):
            maze[row_num][col_num] = row[col_num]
            if row[col_num] == 'P':
                starting_pt = (row_num, col_num)
            if row[col_num] == 'T':
                target_pt = (row_num, col_num)

    return maze, starting_pt, target_pt


def check_neighbours(maze, x, y):
    """check the location neighbours. if not '*', add it to a list."""
    num_rows = maze.getHeight()
    num_cols = maze.getWidth()
    neighbours = []
    if y >= 1 and maze[x][y-1] != '*' and maze[x][y-1] != '.': #left
        nl = (x, y-1)
        neighbours.append(nl)
    if x >= 1 and maze[x-1][y] != '*' and maze[x-1][y] != '.': #up
        nu = (x-1, y)
        neighbours.append(nu)
    if x < num_rows-1 and maze[x+1][y] != '*' and maze[x+1][y] != '.': #down
        nd = (x+1, y)
        neighbours.append(nd)
    if y < num_cols-1 and maze[x][y+1] != '*' and maze[x][y+1] != '.': #right
        nr = (x, y+1)
        neighbours.append(nr)
    return neighbours


def get_path(path_dict, end):
    """return a list of move."""
    path_list = []
    curr = end
    while curr in path_dict:
        path_list.insert(0, curr)
        curr = path_dict[curr]

    path_list.insert(0, 'P')
    path_list[-1] = 'T'
    return path_list


def print_path(path_list, maze_original):
    """print the path of move."""
    maze_path = copy.deepcopy(maze_original)
    for loc in path_list[1:-1]:
        row = loc[0]
        col = loc[1]
        maze_path.__getitem__(row)[col] = "."
    return maze_path


def maze_solver(maze, starting_pt, target_pt):
    """Implement backtracking algorithms using a stack to solve a maze"""
    if_solvable = False
    maze_stack = ArrayStack()
    path = {}
    maze_stack.push(starting_pt)
    while not maze_stack.isEmpty():
        location = maze_stack.pop()
        if maze[location[0]][location[1]] == 'T':
            if_solvable = True
        elif maze[location[0]][location[1]] != '.':
            maze[location[0]][location[1]] = '.'
            nrs = check_neighbours(maze, location[0], location[1])
            for nr in nrs:
                maze_stack.push(nr)
                path[nr] = location
    return if_solvable, path


if __name__ == "__main__":
    maze, starting_pt, target_pt = get_maze()
    maze_copy = copy.deepcopy(maze)
    if_solvable, path = maze_solver(maze, starting_pt, target_pt)
    if if_solvable:
        print "SUCCESS"
        print "==========================================================="
        path_list = get_path(path, target_pt)
        print "Moves to Target: " + path_list.__str__()
        print "==========================================================="
        print print_path(path_list, maze_copy)

    else:
        print "FAILURE"
