
import heapq

def a_star(graph, start, goal, heuristic_function):

    # Priprity Queue
    pq = []

    distances = {node: float('inf') for node in graph}  #inf =Infinity
    distances[start] = 0  # g(start) = 0

    f_costs = {node: float('inf') for node in graph}
    f_costs[start] = heuristic_function(start, goal)

    # OPEN list: Priority Queue stores (f_cost, node)
    heapq.heappush(pq, (f_costs[start], start))

    # Stores parent nodes for path reconstruction
    came_from = {}

    while pq:

        current_f, current_node = heapq.heappop(pq)

        # Ignore outdated Priority Queue entries
        if current_f != f_costs[current_node]:
            continue

        # Goal reached: reconstruct the shortest path
        if current_node == goal:
            return reconstruct_path(came_from, current_node), distances[goal]

        # Explore all neighboring nodes
        for neighbor, weight in graph[current_node].items():

            tentative_distance = distances[current_node] + weight

            if tentative_distance < distances[neighbor]:

                distances[neighbor] = tentative_distance  # Update g(n)

                # Calculate f(n) = g(n) + h(n)
                f_costs[neighbor] = tentative_distance + heuristic_function(neighbor, goal)

                came_from[neighbor] = current_node

                heapq.heappush(pq, (f_costs[neighbor], neighbor))

    return None, float('inf')


def reconstruct_path(came_from, current_node):

    path = [current_node]

    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)

    path.reverse()
    return path


def heuristic_function(node, goal):

    heuristic_map = {
        'A': {'D': 6},
        'B': {'D': 5},
        'C': {'D': 3},
        'D': {'D': 0}
    }

    return heuristic_map.get(node, {}).get(goal, 0)


# Graph: Node -> Neighbors and edge costs
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}

start_node = 'A'
goal_node = 'D'

shortest_path, cost = a_star(graph, start_node, goal_node, heuristic_function)

print("Shortest Path:", shortest_path)
print("Total Cost:", cost)
