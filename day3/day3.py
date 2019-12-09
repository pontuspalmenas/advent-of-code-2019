moves1 = []
moves2 = []
wire1 = [(0,0)]
wire2 = [(0,0)]
intersections = []

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def build_wire(moves, wire):
    for move in moves:
        start_point = wire[-1]
        len = int(move[1:])
        if move[0] == 'U':
            p = (int(start_point[0]), int(start_point[1]) + len)
        if move[0] == 'D':
            p = (int(start_point[0]), int(start_point[1]) - len)
        if move[0] == 'L':
            p = (int(start_point[0] - len), int(start_point[1]))
        if move[0] == 'R':
            p = (int(start_point[0] + len), int(start_point[1]))
        wire.append(p)

def find_intersections():
    wire1.sort(key=lambda tup: tup[1])
    wire2.sort(key=lambda tup: tup[1])

    # How to find intersection between two lines?
    # Now we only store the points of the segments
    for p1 in wire1:
        for p2 in wire2:
            if p1[0] == p2[0] and p1[1] == p2[1] and p1[0] != 0 and p1[1] != 0:
                intersections.append(p1)

with open('input') as f:
    moves1 = f.readline().rstrip('\n').split(",")
    moves2 = f.readline().rstrip('\n').split(",")

#build_wire(moves1, wire1)
#build_wire(moves2, wire2)

build_wire(['U2','R2','U1'], wire1)
build_wire(['L1','U1','R2'], wire2)

print(wire1)
print(wire2)

find_intersections()

distances = []
for p in intersections:
    distances.append(manhattan(p, (0,0)))
print(distances)

print(manhattan((0,0), (1,3)))
#print(intersections)




