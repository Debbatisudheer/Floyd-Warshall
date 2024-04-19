code: 
=======

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



output:
=======
Shortest distance from vertex 0 to vertex 0 is 0
Shortest distance from vertex 0 to vertex 1 is 3
Shortest distance from vertex 0 to vertex 2 is 5
Shortest distance from vertex 0 to vertex 3 is 6
Shortest distance from vertex 1 to vertex 0 is 5
Shortest distance from vertex 1 to vertex 1 is 0
Shortest distance from vertex 1 to vertex 2 is 2
Shortest distance from vertex 1 to vertex 3 is 3
Shortest distance from vertex 2 to vertex 0 is 3
Shortest distance from vertex 2 to vertex 1 is 6
Shortest distance from vertex 2 to vertex 2 is 0
Shortest distance from vertex 2 to vertex 3 is 1
Shortest distance from vertex 3 to vertex 0 is 2
Shortest distance from vertex 3 to vertex 1 is 5
Shortest distance from vertex 3 to vertex 2 is 7
Shortest distance from vertex 3 to vertex 3 is 0



The Floyd-Warshall algorithm is a method used in graph theory to find the shortest paths between all pairs of vertices in a weighted graph. Here's a clear explanation of how it works:

    Initialization: Start by creating a matrix to store the shortest distances between every pair of vertices in the graph. Initially, this matrix will contain the direct distances between vertices if there's an edge connecting them, and infinity otherwise. Also, set the distance from a vertex to itself as 0.

    Iterative Updates: The core of the Floyd-Warshall algorithm is its iterative process. It systematically considers every possible intermediate vertex between any two vertices and checks if using that intermediate vertex could provide a shorter path between them.

    a. For each pair of vertices (i, j), consider every other vertex (k) in the graph as a potential intermediate vertex.

    b. Check if going from vertex i to vertex k, then from vertex k to vertex j (using the intermediate vertex) is shorter than the current shortest path from i to j.

    c. If it is shorter, update the shortest path from vertex i to vertex j to go through vertex k instead.

    Completing the Matrix: Repeat the process of considering each vertex as a potential intermediate until every possible pair of vertices has been examined.

    Identifying Shortest Paths: After the iterative process is complete, the matrix will contain the shortest distances between every pair of vertices in the graph.

    Negative Cycle Detection: Optionally, you can check for negative cycles in the graph by examining the diagonal of the matrix. If any diagonal element is negative, it indicates the presence of a negative cycle in the graph.

    Result: The final matrix represents the shortest paths between all pairs of vertices in the graph.

The Floyd-Warshall algorithm is efficient for dense graphs, where the number of edges is close to the maximum possible number of edges. Its time complexity is O(V^3), where V is the number of vertices in the graph.



Let's break down the Floyd-Warshall algorithm step by step:

    Initialization:
        Create a matrix, let's call it dist[][], where dist[i][j] represents the shortest distance from vertex i to vertex j.
        Initialize this matrix with the direct distances between vertices if there's an edge connecting them, and infinity otherwise. Also, set the distance from a vertex to itself as 0.

    Iterative Updates:
        For each vertex k in the graph:
            For each pair of vertices (i, j):
                Check if the distance from i to k plus the distance from k to j is shorter than the current shortest distance from i to j.
                If it is, update dist[i][j] to be the sum of the distances from i to k and from k to j.

    Completing the Matrix:
        Repeat the above step for every vertex k in the graph.

    Identifying Shortest Paths:
        After all iterations are complete, the dist[][] matrix will contain the shortest distances between every pair of vertices in the graph.

    Negative Cycle Detection:
        Optionally, you can check for negative cycles in the graph by examining the diagonal of the matrix. If any diagonal element is negative, it indicates the presence of a negative cycle in the graph.

    Result:
        The final dist[][] matrix represents the shortest paths between all pairs of vertices in the graph.
