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

def create_board(gridInString):
        values = []
        digits = '123456789'

        for c in gridInString:
                if c == '.':
                        values.append(digits)
                elif c in digits:
                        values.append(c)
        
	assert len(values) == 81
	
        return dict(zip(nodes, gridInString))
