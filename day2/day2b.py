# https://adventofcode.com/2019/day/2

with open('input') as f:
	input = [int(i) for i in f.readline().split(',')]

def work(noun, verb):
	data = input.copy()

	data[1] = noun
	data[2] = verb
	
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
		
	return data[0]

for noun in range(0,99):
	for verb in range(0,99):
		if work(noun, verb) == 19690720:
			answer = 100 * noun + verb
			print(answer)