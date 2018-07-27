from functions import *

gridInString = '7......943..9.217......13856...78.2.5...1...8.2.35...94961......836.5..717......3'

# Displays sudoku board
print("\n---Creating initial sudoku board---\n")
board_initial = create_initial_board(gridInString)
display(board_initial)
print("\n---Initial sudoku board successfully created---");
print ("\n\n")

print("\n---Creating all possibilities for each node---\n")
board_with_possibilities = create_board_with_possibilities(gridInString)
display(board_with_possibilities)
print("\n---Possibilities generated for each empty node---\n")
print("\n\n")

print("\n---Eliminating the values from every one of its peers---\n")
board_eliminated = eliminate(board_with_possibilities)
display(board_eliminated)
print("\n---Elimination completed---\n")
print("\n\n")

print("\n---Checking for only choices---\n")
board_only_choice = only_choice(board_eliminated)
display(board_only_choice)
print("\n---Only choices generated---\n")
print("\n\n")

print("\n---Reducing puzzle---\n")
board_reduced = reduce_puzzle(board_only_choice)
display(board_reduced)
print("\n---Puzzle reduced---\n")
print("\n\n")

print("\n---Final search---\n")
board_search = search(board_reduced)
display(board_search)
print("\n---Search completed---\n")
print("\n\n")