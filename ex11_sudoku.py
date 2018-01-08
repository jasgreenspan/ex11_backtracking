##############################################################################
# FILE : ex11_sudoku.py
# WRITER : Jason Greenspan , jasonmg , 336126362
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION: ****
##############################################################################
import sys
import os.path
from ex11_backtrack import general_backtracking

ROW_SEPARATOR = '\n'
CELL_SEPARATOR = ','
SUDOKU_ASSIGNMENTS = range(1,10)
STANDARD_BOARD_SIZE = 9
EMPTY_CELL = '0'

def print_board(board, board_size=STANDARD_BOARD_SIZE):
    """ prints a sudoku board to the screen

    ---  board should be implemented as a dictinary 
         that points from a location to a number {(row,col):num}
    """ 
    for row in range(board_size):
        if(row%3 == 0):
            print('-------------')
        toPrint = ''
        for col in range(board_size):
            if(col%3 == 0):
                toPrint += '|'
            toPrint += str(board[(row,col)])
        toPrint += '|'
        print(toPrint)
    print('-------------')


def load_game(sudoku_file):
    current_board = {}    
    full_board = []
    
    # Complete the path name of sudoku_file from cd of current file.
    dir_path = os.path.dirname(os.path.realpath(__file__)).replace('\\','/')
    sudoku_file = dir_path + '/' + sudoku_file
    
    # Divide up file into list of rows, where each row is list of cells.
    board_reader = open(sudoku_file, 'r')
    board_read = board_reader.read()
    board_from_file = board_read.split(ROW_SEPARATOR)
    for row in board_from_file:
        cell = row.split(CELL_SEPARATOR)
        full_board.append(cell)
    board_reader.close()
    
    # Add contents of each cell to a dictionary with coordinates as key.
    for row in range(len(full_board)):
        for column in range(len(full_board[row])):
            current_board[(row, column)] = full_board[row][column]
            
    return current_board


def check_board(board, x, *args):
    """board - dictionary similar to the result of load_game
    X - tuple representing the location on the board (row, column)
    *args - what is given from general_backtrack
    this function is given to general_backtracking as legal_assignment_func"""
    
    current_assignment = board[x]
    assign_row = x[0]
    assign_column = x[1]
    
    for cell in board:
        cell_row = cell[0]
        cell_column = cell[1]
        cell_assignment = board[cell]
        # Check whole board for value of potential assignment.
        # Return False if value in same row, column, or 3x3 section as cell.
        if cell_assignment == current_assignment and cell != x:
            if (cell_row//3 == assign_row//3 and 
                cell_column//3 == assign_column//3):
                return False
            elif cell_row == assign_row:
                return False
            elif cell_column == assign_column:
                return False
    return True


def run_game(sudoku_file, print_mode = False):
    starting_index = 0
    list_of_items = []
    
    board = load_game(sudoku_file)
    
    for key in board:
        if board[key] == EMPTY_CELL:
            list_of_items.append(key)
            list_of_items.sort()
    
    if general_backtracking(list_of_items, board, starting_index,
                             SUDOKU_ASSIGNMENTS, check_board):
        print_mode = True
        
    if print_mode == True:    
        print_board(board)


if __name__ == "__main__":
    run_game(sys.argv[1])
    
