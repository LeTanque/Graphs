def getNeighbors(vertex, matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = set()
    # north
    yOffset = y - 1
    if yOffset >= 0 and matrix[yOffset][x] == 1:
        neighbors.add((x, yOffset))
    # south
    yOffset = y + 1
    if yOffset < len(matrix) and matrix[yOffset][x] == 1:
        neighbors.add((x, yOffset))
    # west
    xOffset = x - 1
    if xOffset >= 0 and matrix[y][xOffset] == 1:
        neighbors.add((xOffset, y))
    # east
    xOffset = x + 1
    if xOffset < len(matrix) and matrix[y][xOffset] == 1:
        neighbors.add((xOffset, y))
    return neighbors
