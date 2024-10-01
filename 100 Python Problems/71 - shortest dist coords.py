# Write a program that accepts neighbors (a set of 2D coordinates) and a point (a single 2D coordinate) and tells the nearest neighbor (in terms of Euclidean distance).

def nearest_neighbour(neighbours, you):
    def calculate_distance(c1, c2):
        return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5
    
    distances = []
    
    for i in neighbours:
        distances.append(calculate_distance(you, i))
    
    neighbour_index, distance = sorted(list(enumerate(distances)), key=lambda x: x[1])[0]
    
    print('Nearest neighbour is:', neighbour_index, 'at the distance of:', distance)

neighbours = [
    [89, 34],
    [12, 35],
    [10, 89],
    [90, 90]
]

you = [-9, 7]

nearest_neighbour(neighbours, you)