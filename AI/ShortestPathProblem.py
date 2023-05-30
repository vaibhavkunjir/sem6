import heapq

def dijkstra(graph, start):
    # Create a dictionary to store the shortest distances from the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Create a priority queue (min heap) to store nodes to visit
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Skip if the current distance is greater than the already calculated distance
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

if __name__ == '__main__':
    # Example graph represented as an adjacency list
    graph = {
        'A': {'B': 5, 'C': 3},
        'B': {'D': 2},
        'C': {'B': 1, 'D': 6},
        'D': {'A': 2}
    }

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    print("Shortest distances from node", start_node + ":")
    for node, distance in shortest_distances.items():
        print("Node:", node, "- Distance:", distance)

