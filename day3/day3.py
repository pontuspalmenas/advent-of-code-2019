moves1 = []
moves2 = []
wire1 = [(0,0)]
wire2 = [(0,0)]
intersections = []

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[0] - p2[0])

def build_wire(moves, wire):
    for move in moves:
        start_point = wire[-1]
        if move[0] == 'U':
            for i in range(1, int(move[1:])+1):
                p = (int(start_point[0]), int(start_point[1]) + i)
                wire.append(p)
        if move[0] == 'D':
            for i in range(1, int(move[1:])+1):
                p = (int(start_point[0]), int(start_point[1]) - i)
                wire.append(p)
        if move[0] == 'L':
            for i in range(1, int(move[1:])+1):
                p = (int(start_point[0] - i), int(start_point[1]))
                wire.append(p)
        if move[0] == 'R':
            for i in range(1, int(move[1:])+1):
                p = (int(start_point[0] + i), int(start_point[1]))
                wire.append(p)

def find_intersections():
    wire1.sort(key=lambda tup: tup[1])
    wire2.sort(key=lambda tup: tup[1])
    for x in wire1:
        for y in wire2:
            if x[0] == y[0] and x[1] == y[1] and x[0] != 0 and x[1] != 0:
                intersections.append(x)

with open('example1') as f:
    moves1 = f.readline().rstrip('\n').split(",")
    moves2 = f.readline().rstrip('\n').split(",")

#build_wire(['R75','D30','R83','U83','L12','D49','R71','U7','L72'], wire1)
#build_wire(['U62','R66','U55','R34','D71','R55','D58','R83'], wire2)

build_wire(['R8','U5','L5','D3'], wire1)
build_wire(['U7','R6','D4','L4'], wire2)


find_intersections()

distances = []
for p in intersections:
    distances.append(manhattan(p, (0,0)))
print(distances)

#print(intersections)