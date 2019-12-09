# https://adventofcode.com/2019/day/1

def fuel(mass):
    return (mass // 3) - 2

total = 0
with open('input') as f:
    for line in f:	
        total += fuel(int(line))
        
print(total)