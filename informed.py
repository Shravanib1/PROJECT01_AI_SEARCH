import heapq
import math

from uninformed import make_result


def straight_line_km(locations, place_a, place_b):
    lat1 = math.radians(locations[place_a]["lat"])
    lon1 = math.radians(locations[place_a]["lon"])
    lat2 = math.radians(locations[place_b]["lat"])
    lon2 = math.radians(locations[place_b]["lon"])

    a = (math.sin((lat2 - lat1) / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2)
    return 2 * 6371 * math.asin(math.sqrt(a))


def greedy(graph, locations, start, goal):
    frontier = [(straight_line_km(locations, start, goal), [start])]
    visited = set()
    nodes_expanded = 0

    while frontier:
        h, path = heapq.heappop(frontier)
        place = path[-1]

        if place in visited:
            continue
        visited.add(place)
        nodes_expanded += 1

        if place == goal:
            return make_result(graph, path, nodes_expanded)

        for neighbor in graph[place]:
            if neighbor not in visited:
                h = straight_line_km(locations, neighbor, goal)
                heapq.heappush(frontier, (h, path + [neighbor]))

    return make_result(graph, None, nodes_expanded)


def a_star(graph, locations, start, goal):
    frontier = [(straight_line_km(locations, start, goal), 0, [start])]
    best_g = {start: 0}
    nodes_expanded = 0

    while frontier:
        f, g, path = heapq.heappop(frontier)
        place = path[-1]

        if g > best_g[place]:
            continue
        nodes_expanded += 1

        if place == goal:
            return make_result(graph, path, nodes_expanded)

        for neighbor, distance in graph[place].items():
            new_g = g + distance
            if neighbor not in best_g or new_g < best_g[neighbor]:
                best_g[neighbor] = new_g
                new_f = new_g + straight_line_km(locations, neighbor, goal)
                heapq.heappush(frontier, (new_f, new_g, path + [neighbor]))

    return make_result(graph, None, nodes_expanded)
