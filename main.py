import time
import random


def generate_random_graph(num_vertices):
    graph = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        graph[i][i] = 0
        for j in range(i + 1, num_vertices):
            weight = random.randint(1, 100)  # Generate random edge weights (1 to 100)
            graph[i][j] = weight
            graph[j][i] = weight
    return graph


def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = [[0 if i == j else graph[i][j] for j in range(num_vertices)] for i in range(num_vertices)]

    start_time = time.time()

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    end_time = time.time()

    return end_time - start_time, dist


# Analyze time and space complexity for different graph sizes
for num_vertices in [100, 200, 300, 400, 500]:
    graph = generate_random_graph(num_vertices)
    execution_time, _ = floyd_warshall(graph)
    space_complexity = num_vertices * num_vertices * 8  # Assuming each entry in the matrix occupies 8 bytes (float64)
    print(
        f"Graph size: {num_vertices}x{num_vertices}, Execution time: {execution_time:.6f} seconds, Space complexity: {space_complexity} bytes")