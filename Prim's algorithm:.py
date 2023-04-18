import heapq

def prim(graph, start) -> set:
  """Алгоритм Прима"""
    visited = set()
    edges = (0, start)
    while edges:
        weight, vertex = heapq.heappop(edges)
        if vertex not in visited:
            visited.add(vertex)
            for neighbor, neighborweight in graph[vertex].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (neighborweight, neighbor))
    return visited
