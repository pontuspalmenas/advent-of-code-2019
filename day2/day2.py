# https://adventofcode.com/2019/day/2

data = []
with open('input') as f:
	data = [int(i) for i in f.readline().split(',')]
	
	data[1] = 12
	data[2] = 2
	
	opcode_pos = 0
	while True:
		opcode = data[opcode_pos]
		if opcode not in [1,2]: break
		a = data[opcode_pos + 1]
		b = data[opcode_pos + 2]
		c = data[opcode_pos + 3]
		if opcode == 1:
			data[c] = data[a] + data[b]
		elif opcode == 2:
			data[c] = data[a] * data[b]
			
		opcode_pos += 4	
print(data[0])