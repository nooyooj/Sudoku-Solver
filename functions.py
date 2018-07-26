rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
	return [s + t for s in a for t in b]

nodes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
node_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
unitlist = row_units + column_units + node_units
units = dict((s, [u for u in unitlist if s in u]) for s in nodes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in nodes)

def display(data):
	width = 1 + max(len(data[s]) for s in nodes)
	
	line = '+'.join(['-' * (width * 3)] * 3)

	for r in rows:
		print(''.join(data[r + c].center(width) + ('|' if c in '36' else '') for c in cols))
		if r in 'CF': 
			print(line)

def create_initial_board(gridInString):
        assert len(gridInString) == 81

        return dict(zip(nodes, gridInString))

def create_board_with_possibilities(gridInString):
        values = []
        digits = '123456789'

        for c in gridInString:
                if c == '.':
                        values.append(digits);
                elif c in digits:
                        values.append(c)
        
        assert len(values) == 81
	
        return dict(zip(nodes, values))

def eliminate(values):
        solved_values = [node for node in values.keys() if len(values[node]) == 1]

        for node in solved_values:
                digit = values[node]

                for peer in peers[node]:
                        values[peer] = values[peer].replace(digit, '')
        
        return values

def only_choice(values):
        for unit in unitlist:
                for digit in '123456789':
                        dplaces = [node for node in unit if digit in values[node]]

                        if len(dplaces) == 1:
                                values[dplaces[0]] = digit

        return values

def reduce_puzzle(values):
        stalled = False

        while not stalled:
                solved_values_before = len([node for node in values.keys() if len(values[node]) == 1])

                values = eliminate(values)
                values = only_choice(values)

                solved_values_after = len([node for node in values.keys() if len(values[node]) == 1])

                stalled = solved_values_before == solved_values_after

                if len([node for node in values.keys() if len(values[node]) == 0]):
                        return False
        
        return values

def search(values):
        values = reduce_puzzle(values)

        if values is False:
                return False 
        if all(len(values[s]) == 1 for s in nodes):
                return values
        
        n,s = min((len(values[s]), s) for s in nodes if len(values[s]) > 1)

        for value in values[s]:
                new_sudoku = values.copy()
                new_sudoku[s] = value
                attempt = search(new_sudoku)

                if attempt:
                        return attempt