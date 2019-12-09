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
        
top_layer = ['x' for i in range(w*h)]
prev_layer = []

print(f'layers: {len(layers)}')

for l in layers:
    for n in range(0, len(l)):
        if l[n] == '2' and len(prev_layer) > 0:
            top_layer[n] = prev_layer[n]
        else:
            top_layer[n] = l[n]
    prev_layer = l

print(top_layer)