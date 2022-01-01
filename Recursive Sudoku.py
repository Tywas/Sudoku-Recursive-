# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 18:15:19 2021

@author: tyler
"""


grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


#checks if selected position matches one inside its row
def check_horozontal(row, num): # returns true if value of position in grid is alreday inside its row
    for i in range(9):
        if grid[row][i] == num: #checks cols inside row 
            return True
#checks if selected position matches one inside its colum            
def check_vertical(col, num): # returns true if value of position in grid is alreday inside its column
    for i in range(9):
        if grid[i][col] == num: #checks rows inside col 
            return True

# use of add_on method to check the 3by3 area of the grid
def check_box(row, col, num): # returns true if selected value in position is not already inside its 3by3 box        
    row_add = (row // 3)*3
    col_add = (col // 3)*3
    for i in range(3):
        for j in range(3):
            if grid[i + row_add][j + col_add] == num:
                return True
                
#prints out grid with spaces between 3by3 grids    
def print_grid(): 
    for i in range(9):
        print('')
        if (i-1) % 3 == 2:
            print('')
        for j in range(9):
            print(grid[i][j], end=' ')
            if j % 3 == 2:
                print(" ", end='')

# method makes sure the specified number for its position follows three conditions 
def try_number(row, col, number): # returns true if the parameter number does not already have that number in its row, col, or 3by3 box
    if check_horozontal(row, number):
        return False
    elif check_vertical(col, number):
        return False
    elif check_box(row, col, number):
        return False
    return True
    
#method attempts to solve sudoku puzzle
def solve():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0: # finds a position in the grid that has no value (0)
                for i in range(1 , 10): # Possible options
                    if try_number(row, col, i): #checks and sees if number follows the rules
                        grid[row][col] = i 
                        solve() # recursion
                        grid[row][col]  = 0 # resets to 0 to try next value
                return
    print_grid()


#
#
#   

solve()





