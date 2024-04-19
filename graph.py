def floyd_warshall(graph):
    num_vertices = len(graph)

    # Initialize the distance matrix with direct edge weights
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]

    # Update the distance matrix by considering all possible intermediate vertices
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Example graph represented as an adjacency matrix
graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

# Run Floyd-Warshall algorithm on the graph
shortest_distances = floyd_warshall(graph)

# Print the shortest distances between all pairs of vertices
for i in range(len(graph)):
    for j in range(len(graph)):
        if shortest_distances[i][j] == float('inf'):
            print(f"Shortest distance from vertex {i} to vertex {j} is infinity")
        else:
            print(f"Shortest distance from vertex {i} to vertex {j} is {shortest_distances[i][j]}")
