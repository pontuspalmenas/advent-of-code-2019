# https://adventofcode.com/2019/day/1

def fuel(mass):	 
	fuel_req = 0
	new_fuel = (mass // 3) - 2
	fuel_req += new_fuel
	while True:
		new_fuel = (new_fuel // 3) - 2
		if (new_fuel < 0):
			break
		fuel_req += new_fuel

	return fuel_req

total = 0

with open('input') as f:
    for line in f:	
        total += fuel(int(line))
        
print(total)