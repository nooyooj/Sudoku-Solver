rows = 'ABCDEFGHI'
cols = '123456789'

def concatenate(a, b):

        """Returns the list formed by all the possible concatenations of a letters in strings

        Example: If concatenate('abc', 'def'), returns ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

        Args:
                a: first letters
                b: second letters
        Returns:
                Array of all the possible concatenations of two sets of letters
        """

        return [s + t for s in a for t in b]


nodes = concatenate(rows, cols)

row_units = [concatenate(r, cols) for r in rows]
column_units = [concatenate(rows, c) for c in cols]
node_units = [concatenate(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]

unitlist = row_units + column_units + node_units
units = dict((s, [u for u in unitlist if s in u]) for s in nodes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in nodes)


def display(values):

        """Displays the values as a 2D grid.

        Args:
                values: The sudoku in dictionary form
        Returns:
                None
        """

        width = 1 + max(len(values[s]) for s in nodes)
        line = '+'.join(['-' * (width * 3)] * 3)
        for r in rows:
	        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '') for c in cols))
	        if r in 'CF': 
		        print(line)


def create_initial_board(gridInString):
        
        """Converts grid string into {<node>: <value>} dictionary with '.' value for empties.
        
        Args:
                gridInString: Sudoku grid in string form, 81 characters long (9x9)
        Returns:
                Sudoku grid in dictionary form:
                - keys: Node labels, e.g. 'A1'
                - values: Value in corresponding node, e.g. '8', or '.' if it is empty
        """
        
        assert len(gridInString) == 81, "Input grid must be a string of length 81 (9x9)"
        return dict(zip(nodes, gridInString))


def create_board_with_possibilities(gridInString):
        
        """Converts grid string into {<node>: <value>} dictionary with '123456789' value for empties.
        
        Args:
                gridInString: Sudoku grid in string form, 81 characters long (9x9)
        Returns:
                Sudoku grid in dictionary form:
                - keys: Node labels, e.g. 'A1'
                - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty
        """
        
        values = []
        digits = '123456789'
        for c in gridInString:
                if c == '.':
                        values.append(digits);
                elif c in digits:
                        values.append(c)
        assert len(values) == 81, "Input grid must be a string of length 81 (9x9)"
        return dict(zip(nodes, values))


def eliminate(values):

        """Eliminates values from peers of each node with a single value.
        
        Goes through all the nodes, and whenever there is a node with a single value, 
        eliminate this value from the set of values of all its peers.

        Args:
                values: Sudoku in dictionary form
        Returns:
                Resulting Sudoku in dictionary form after eliminating values
        """

        solved_values = [node for node in values.keys() if len(values[node]) == 1]
        for node in solved_values:
                digit = values[node]
                for peer in peers[node]:
                        values[peer] = values[peer].replace(digit, '')
        return values


def only_choice(values):

        """Finalizes all values that are the only choice for a unit.

        Goes through all the units, and whenever there is a unit with a value
        that only fits in one node, assigns the value to this node.

        Args:
                values: Sudoku in dictionary form
        Returns:
                Resulting Sudoku in dictionary form after filling in only choices
        """

        for unit in unitlist:
                for digit in '123456789':
                        dplaces = [node for node in unit if digit in values[node]]
                        if len(dplaces) == 1:
                                values[dplaces[0]] = digit
        return values


def reduce_puzzle(values):

        """Receives as input an unsolved puzzle and applies our two constraints repeatedly in an attempt to solve it

        Iterates eliminate() and only_choice(). 
        
        If at some point, there is a node with no available values, returns False.
        
        If after an iteration of both functions, the sudoku remains the same,
        returns the sudoku.

        Args:
                values: A sudoku in dictionary form
        Returns:
                The resulting sudoku in dictionary form
        """
        stalled = False
        while not stalled:
                # Checking how many nodes have a determined value
                solved_values_before = len([node for node in values.keys() if len(values[node]) == 1])
                # Using the Eliminate Strategy
                values = eliminate(values)
                # Using the Only Choice Strategy
                values = only_choice(values)
                # Checking how many nodes have a determined value, to compare
                solved_values_after = len([node for node in values.keys() if len(values[node]) == 1])
                # If no new values were added, stops the loop
                stalled = solved_values_before == solved_values_after
                # Sanity check. Returns False if there is a node with zero available values
                if len([node for node in values.keys() if len(values[node]) == 0]):
                        return False
        return values


def search(values):

        """Creates a tree of possibilities and traverse it using DFS until it finds a solution for the sudoku puzzle

        Using depth-first search and propagation, tries all possible values.

        Args:
                values: A sudoku in dictionary form
        Returns:
                The resulting sudoku in dictionary form
        """

        # First, reduce the puzzle using the previous function
        values = reduce_puzzle(values)
        if values is False:
                return False ## Failed already
        if all(len(values[s]) == 1 for s in nodes):
                return values ## Solved!
        # Choose one of the unfilled nodes with the fewest possibilities
        n,s = min((len(values[s]), s) for s in nodes if len(values[s]) > 1)
        #Now using recurrence to solve each one of the resulting sudokus
        for value in values[s]:
                new_sudoku = values.copy()
                new_sudoku[s] = value
                attempt = search(new_sudoku)
                if attempt:
                        return attempt
