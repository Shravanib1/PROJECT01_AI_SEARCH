import heapq
from collections import deque


def path_cost(graph, path):
    total = 0
    for i in range(len(path) - 1):
        total += graph[path[i]][path[i + 1]]
    return round(total, 2)


def make_result(graph, path, nodes_expanded):
    if path is None:
        return {"path": [], "cost": 0, "nodes_expanded": nodes_expanded}
    return {
        "path": path,
        "cost": path_cost(graph, path),
        "nodes_expanded": nodes_expanded,
    }


def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    nodes_expanded = 0

    while queue:
        path = queue.popleft()
        place = path[-1]
        nodes_expanded += 1

        if place == goal:
            return make_result(graph, path, nodes_expanded)

        for neighbor in graph[place]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return make_result(graph, None, nodes_expanded)


def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    nodes_expanded = 0

    while stack:
        path = stack.pop()
        place = path[-1]

        if place in visited:
            continue
        visited.add(place)
        nodes_expanded += 1

        if place == goal:
            return make_result(graph, path, nodes_expanded)

        for neighbor in graph[place]:
            if neighbor not in visited:
                stack.append(path + [neighbor])

    return make_result(graph, None, nodes_expanded)


def ucs(graph, start, goal):
    frontier = [(0, [start])]
    expanded = set()
    nodes_expanded = 0

    while frontier:
        cost, path = heapq.heappop(frontier)
        place = path[-1]

        if place in expanded:
            continue
        expanded.add(place)
        nodes_expanded += 1

        if place == goal:
            return make_result(graph, path, nodes_expanded)

        for neighbor, distance in graph[place].items():
            if neighbor not in expanded:
                heapq.heappush(frontier, (cost + distance, path + [neighbor]))

    return make_result(graph, None, nodes_expanded)


def depth_limited(graph, path, goal, limit):
    place = path[-1]
    expanded = 1

    if place == goal:
        return path, expanded
    if limit == 0:
        return None, expanded

    for neighbor in graph[place]:
        if neighbor not in path:
            found, count = depth_limited(graph, path + [neighbor], goal, limit - 1)
            expanded += count
            if found:
                return found, expanded

    return None, expanded


def ids(graph, start, goal):
    nodes_expanded = 0

    for limit in range(len(graph)):
        found, count = depth_limited(graph, [start], goal, limit)
        nodes_expanded += count
        if found:
            return make_result(graph, found, nodes_expanded)

    return make_result(graph, None, nodes_expanded)
