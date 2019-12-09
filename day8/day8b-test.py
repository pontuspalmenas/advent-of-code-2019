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

# get the highest previous layers value that is non-transparent
def get_highest(pos_in_layer, curr_layer):
    for i in range(curr_layer, len(layers)-1):
        if layers[i][pos_in_layer] != '2':
            return layers[i][pos_in_layer]

for curr_layer, l in enumerate(layers):
    print(l)
    for n in range(0, w*h):
        if l[n] == '2':
            print('?')
            top_layer[n] = get_highest(n, curr_layer)
        else:
            if top_layer[n] != '0' and top_layer[n] != '1':
                top_layer[n] = l[n]
    print(top_layer)
print(top_layer)



# 0222112222120000
# layers = [0222, 1122, 2212, 0000]