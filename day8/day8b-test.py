layers = []

w = 2
h = 2

line = "0222112222120000"

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
prev_layer = None

# get the highest previous layers value that is non-transparent
def get_highest(ix, curr_layer):
    for i in range(0, curr_layer):
        if layers[i][ix] != '2':
            return layers[i][ix]


print('test')
print(get_highest(3, 4))
print(get_highest(0, 1))

for i, l in enumerate(layers[::-1]):
    for n in range(0, w*h):
        if l[n] == '2':
            top_layer[n] = get_highest(n, i)
        else:
            top_layer[n] = l[n]
    prev_layer = l            

print(top_layer)