import time
import random

def generate_random_graph(num_vertices):
    graph = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        graph[i][i] = 0
        for j in range(i + 1, num_vertices):
            weight = random.randint(-100, 100)  # Generate random edge weights (-100 to 100, including negative weights)
            graph[i][j] = weight
            graph[j][i] = weight
    return graph

def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = [[0 if i == j else graph[i][j] for j in range(num_vertices)] for i in range(num_vertices)]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def shortest_path(source, destination, distances):
    if distances[source][destination] == float('inf'):
        return "No path exists"
    path = [source]
    while source != destination:
        min_neighbor = min(range(len(distances[source])), key=lambda x: distances[source][x])
        path.append(min_neighbor)
        source = min_neighbor
    return path

# Analyze time and space complexity for different graph sizes
for num_vertices in [100]:
    graph = generate_random_graph(num_vertices)
    start_time = time.time()
    shortest_distances = floyd_warshall(graph)
    end_time = time.time()
    execution_time = end_time - start_time
    space_complexity = num_vertices * num_vertices * 8  # Assuming each entry in the matrix occupies 8 bytes (float64)
    print(
        f"Graph size: {num_vertices}x{num_vertices}, Execution time: {execution_time:.6f} seconds, Space complexity: {space_complexity} bytes")

