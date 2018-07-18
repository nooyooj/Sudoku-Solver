# sudoku-solver


## Purpose
To make an agent that only considers reasonable solution candidates and efficiently solves any Sudoku puzzle.


## Techniques Used
Constraint Propagation with backtracking search.


## Functions
```
display(data)
```
Displays the data in dictionary form as a 2-D grid
**Input**: A grid in dictionary form
**Output**: None

```
create_board(gridInString)
```
Converts grid in string into a dictionary form -> {node: char}.
**Input**: A grid in string form
**Output**: A grid in dictionary form -> {key, value}


## Usage
```
$ python main.py
```


## Author
[Jooyoon Byun](https://github.com/nooyooj)
