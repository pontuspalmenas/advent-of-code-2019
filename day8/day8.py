layers = []

w = 25
h = 6

with open('input') as f:
    line = f.readline()

n = 0
temp = ""
for c in line:
    temp += c
    n += 1
    if n == w*h:
        layers.append(temp)
        temp = ""
        n = 0
        
def count(c, s):
    return sum(map(lambda x : 1 if c in x else 0, s)) 

fewest_zeros = w*h # Assume the worst
layers_with_fewest = []
for i, l in enumerate(layers):
    n = count('0', l)
    if n < fewest_zeros:
        layers_with_fewest = l
        fewest_zeros = n
        print(f'new smallest layer: {l} with {fewest_zeros}')

print(count('1', l) * count('2', l))