# https://adventofcode.com/2019/day/1

def fuel(mass):
	return 

	# 100756
	# 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2
	100756 // 3 - 2
    # fuel = fuel(mass + fuel)	

total = 0
with open('input') as f:
    #for line in f:	
    #    total += fuel(int(line))
	#total += fuel(100756, 0) # should be 50346
	total_fuel = 0
	mass = 100756
	fuel = mass // 3 - 2
	while (mass > 0):
		total_fuel += mass // 3 - 2
		mass = fuel

        
print(total)