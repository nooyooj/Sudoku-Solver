from functions import *

gridInString = '7......943..9.217......13856...78.2.5...1...8.2.35...94961......836.5..717......3'

# Displays sudoku board
print("\n---Creating initial sudoku board---\n")
display(create_initial_board(gridInString))
print("\n---Initial sudoku board successfully created---");
print ("\n\n")

print("\n---Creating possibilities for each node---\n")
display(create_board_with_possibilities(gridInString))
print("\n---Possibilities generated for each empty node---\n")
print("\n\n")

eliminate(create_board_with_possibilities(gridInString))
print("\n---Checking for only choices---\n")
display(only_choice(create_board_with_possibilities(gridInString)))
print("\n---Only choices generated---\n")
print("\n\n")