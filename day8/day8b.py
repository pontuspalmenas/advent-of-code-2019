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

# get the highest previous layers value that is non-transparent
def get_highest(pos_in_layer):
    for i in range(0, len(layers)):
        if layers[i][pos_in_layer] != '2':
            return layers[i][pos_in_layer]

l = layers[0]
for n in range(0, w*h):
    if l[n] == '2':
        top_layer[n] = get_highest(n)
    else:
        top_layer[n] = l[n]

line = ""
for n in range(0,w*h):
    if n > 0 and n % w == 0:
        print(line)
        line = ""
    if top_layer[n] == '1':
        line += "█"
    else:
        line += " "
print(line)