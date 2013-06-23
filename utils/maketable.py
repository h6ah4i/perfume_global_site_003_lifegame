#! /usr/bin/python


X_SIZE = 10
Y_SIZE = 10

def make_neighbors_lut(table_offset):
	# top-left, top, top-right, left, center right, bottom-left, bottom, bottom-right
	neighbor_table = [
		(-1, -1, "TOP-LEFT"),
		(-1,  0, "TOP"),
		(-1,  1, "TOP-RIGHT"), 
		( 0, -1, "LEFT"), 
	#	( 0,  0, "CENTER"),
		( 0,  1, "RIGHT"), 
		( 1, -1, "BOTTOM-LEFT"),
		( 1,  0, "BOTTOM"),
		( 1,  1, "BOTTOM-RIGHT"), 
	]

	for neighbor in neighbor_table:
		tmp = '# {} (OFFSET = {})\n'.format(neighbor[2], table_offset)
		for y in range(Y_SIZE):
			for x in range(X_SIZE):
				y2 = ((y + neighbor[0]) + Y_SIZE) % Y_SIZE
				x2 = ((x + neighbor[1]) + X_SIZE) % X_SIZE
				index = y * X_SIZE + x
				index2 = y2 * X_SIZE + x2
				offset = index2 - index
				tmp += ('[{}]'.format(offset))
			tmp += ('\n')
		print tmp
		table_offset += (Y_SIZE * X_SIZE)

	return table_offset

def calc_next_gen(is_alive, neighbors):
	if is_alive:
		return {
			# case - 0
			0: 0,
			1: 0,
			# case - 1
			2: 1,
			3: 1,
			# case - 2
			4: 0,
			5: 0,
			6: 0,
			7: 0,
			8: 0,
		}[neighbors]
	else:
		return {
			# 
			0: 0,
			1: 0,
			2: 0,
			# case - 4
			3: 1,
			# 
			4: 0,
			5: 0,
			6: 0,
			7: 0,
			8: 0,
		}[neighbors]


def make_next_gen_lut(table_offset):
	print "# Next generation cell state LUT (OFFSET = {})".format(table_offset)

	tmp = ''
	for x in range(8):
		tmp += '[{}]'.format(calc_next_gen(False, x))
	print "# Current cell is dead"
	print tmp

	tmp = ''
	for x in range(8):
		tmp += '[{}]'.format(calc_next_gen(True, x))
	print "# Current cell is alive"
	print tmp

	return table_offset + 16


offset = 0
offset += make_neighbors_lut(offset)
offset += make_next_gen_lut(offset)
