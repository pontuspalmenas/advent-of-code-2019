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
        
top_layer = [None]*w*h
prev_layer = None
for l in enumerate(layers):
    for n in range(0, len(l)):
        if l[n] == '2' and prev_layer != None:
            top_layer[n] = prev_layer[n]
        else:
            top_layer[n] = l[n]
    prev_layer = l

print(top_layer)