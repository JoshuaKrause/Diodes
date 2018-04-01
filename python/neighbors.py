GOAL = 4
width = 8
height = 8

def find_neighbors(coordinates):
    x,y = coordinates
    x_range = range(x - GOAL + 1, x + GOAL)
    y_range = range(y - GOAL + 1, y + GOAL)
    scope = range(GOAL * 2 - 1)

    horizontal = [(x_range[i], y) for i in scope]
    vertical = [(x, y_range[i]) for i in scope]
    down_diagonal = [(x_range[i],y_range[i]) for i in scope]
    up_diagonal = [(x_range[i],y_range[::-1][i]) for i in scope]

    neighbors = []
    for each in [horizontal, vertical, down_diagonal, up_diagonal]:
        filtered_coords = list(filter(lambda x: (x[0] >= 0 and x[1] >= 0) and (x[0] <= width - 1 and x[1] <= height - 1), each))
        #filtered_coords = list(filter(lambda x,y: (x >= 0 and y >= 0) and (x <= width - 1 and y <= height - 1), each))

        if len(filtered_coords) >= GOAL:
            neighbors.append(filtered_coords)

    return neighbors

x = (2,3)

print(find_neighbors(x))
